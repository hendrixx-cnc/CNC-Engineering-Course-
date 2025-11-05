# 19.10 Implementation in LinuxCNC

## LinuxCNC Overview

**LinuxCNC** (formerly EMC2): Open-source CNC control software running on Linux with real-time kernel (RTAI or Preempt-RT).

**Key Features**:
- Real-time trajectory planning (1-2 kHz)
- HAL (Hardware Abstraction Layer) for flexible configuration
- Built-in PID control loops
- Extensive servo tuning tools (Halscope, Halshow)
- Support for steppers and servos
- Free and open-source

**Architecture**:
```
G-Code → Interpreter → Trajectory Planner → Motion Controller
                                                   ↓
                                            HAL (connections)
                                                   ↓
                                     PID Loops → Motor Drivers
                                         ↑
                                   Encoders (feedback)
```

## HAL Configuration Basics

### What is HAL?

**Hardware Abstraction Layer (HAL)**: Flexible system for connecting components.

**Components**:
- **Pins**: Inputs/outputs (like physical pins on IC)
- **Signals**: Connections between pins (wires)
- **Parameters**: Adjustable values (gains, limits)
- **Functions**: Code executed periodically (PID loop, encoder reading)

**Analogy**: Breadboard for CNC control (connect components with virtual wires).

### HAL File Structure

**Main Configuration Files**:
- `machine.ini`: High-level machine configuration (axes, limits, tuning)
- `machine.hal`: HAL component connections
- `custom.hal`: User customizations (optional)
- `postgui.hal`: HAL commands after GUI loads (optional)

### Basic HAL Commands

**Load Component**:
```hal
loadrt pid names=pid.x,pid.y,pid.z
```

**Add Function to Thread**:
```hal
addf pid.x.do-pid-calcs servo-thread
```

**Connect Pins** (create signal):
```hal
net xpos-cmd axis.x.motor-pos-cmd => pid.x.command
net xpos-fb encoder.0.position => pid.x.feedback
```

**Set Parameter**:
```hal
setp pid.x.Pgain 100
setp pid.x.Igain 0.5
setp pid.x.Dgain 10
```

## Servo Configuration in LinuxCNC

### INI File Configuration

**[TRAJ] Section** (Trajectory Planner):
```ini
[TRAJ]
COORDINATES = X Y Z
LINEAR_UNITS = inch
ANGULAR_UNITS = degree
DEFAULT_LINEAR_VELOCITY = 1.0
MAX_LINEAR_VELOCITY = 10.0
DEFAULT_LINEAR_ACCELERATION = 20.0
MAX_LINEAR_ACCELERATION = 200.0
```

**[AXIS_X] Section** (Per-Axis Configuration):
```ini
[AXIS_X]
TYPE = LINEAR
HOME = 0.0
MAX_VELOCITY = 10.0
MAX_ACCELERATION = 200.0
MIN_LIMIT = -0.01
MAX_LIMIT = 24.01

# Servo tuning
FERROR = 0.050
MIN_FERROR = 0.010

# Scale (encoder counts per machine unit)
SCALE = 8000.0

# Home sequence
HOME_OFFSET = 0.0
HOME_SEARCH_VEL = 0.50
HOME_LATCH_VEL = 0.05
HOME_SEQUENCE = 0
```

**Key Parameters**:
- **MAX_VELOCITY**: Axis maximum velocity (in/s or mm/s)
- **MAX_ACCELERATION**: Axis maximum acceleration
- **FERROR**: Maximum allowed following error (triggers fault if exceeded)
- **MIN_FERROR**: Minimum following error (for stationary axis)
- **SCALE**: Encoder counts per machine unit (e.g., 8000 counts/inch)

### HAL File for Servo Axis

**Example X-Axis Configuration** (`machine.hal`):

```hal
# Load PID component
loadrt pid names=pid.x

# Load encoder counter
loadrt encoder num_chan=1
setp encoder.0.position-scale 8000
setp encoder.0.counter-mode 0

# Add functions to servo thread
addf encoder.0.capture-position servo-thread
addf pid.x.do-pid-calcs servo-thread
addf motion-command-handler servo-thread
addf motion-controller servo-thread

# Connect position command from motion controller to PID
net xpos-cmd axis.x.motor-pos-cmd => pid.x.command

# Connect encoder feedback to PID
net xpos-fb encoder.0.position => pid.x.feedback
net xpos-fb => axis.x.motor-pos-fb

# Connect PID output to motor driver (PWM or analog)
net xoutput pid.x.output => pwmgen.0.value

# Connect enable signal
net xenable axis.x.amp-enable-out => pid.x.enable

# Set PID gains
setp pid.x.Pgain 100
setp pid.x.Igain 10
setp pid.x.Dgain 8
setp pid.x.FF1 0.95
setp pid.x.FF2 0.001
setp pid.x.bias 0.0
setp pid.x.deadband 0.0001
setp pid.x.maxoutput 10.0
```

### Encoder Configuration

**Quadrature Encoder**:
```hal
setp encoder.0.position-scale 8000  # counts per machine unit
setp encoder.0.counter-mode 0       # quadrature mode
setp encoder.0.x4-mode 1            # 4x counting (rising/falling edges)
```

**Position Scale Calculation**:
$$\text{Scale} = \frac{\text{Encoder CPR} \times 4}{\text{Distance per Rev}}$$

**Example**:
- Encoder: 2000 CPR (counts per revolution)
- Quadrature (4×): 8000 counts/rev
- Ballscrew pitch: 0.2 in/rev
- Scale: 8000 / 0.2 = **40,000 counts/inch**

**Example 2** (metric):
- Encoder: 2000 CPR → 8000 counts/rev
- Ballscrew pitch: 5 mm/rev
- Scale: 8000 / 5 = **1600 counts/mm**

### Motor Driver Configuration

**Analog Velocity Drive** (±10V):
```hal
setp pwmgen.0.scale 10.0            # ±10V output range
setp pwmgen.0.offset 0.0            # no offset
net xoutput pid.x.output => pwmgen.0.value
```

**Step/Direction Drive** (for servos with step input):
```hal
setp stepgen.0.position-scale 8000  # steps per machine unit
setp stepgen.0.maxvel 10.0          # max velocity (machine units/s)
setp stepgen.0.maxaccel 200.0       # max acceleration
net xpos-cmd axis.x.motor-pos-cmd => stepgen.0.position-cmd
net xpos-fb stepgen.0.position-fb => axis.x.motor-pos-fb
```

## PID Tuning with Halscope

### Halscope Setup

**Launch Halscope**:
```bash
halscope &
```

**Configure Channels**:
1. Click "Add Channel"
2. Select signals to monitor:
   - `axis.x.motor-pos-cmd` (commanded position)
   - `axis.x.motor-pos-fb` (actual position)
   - `axis.x.f-error` (following error)
   - `pid.x.output` (motor command)

**Trigger Setup**:
- Source: `axis.x.motor-pos-cmd`
- Level: 0.1 (trigger when position changes)
- Edge: Rising

**Run**:
- Click "Run" to capture data
- Command axis motion (jog X-axis)
- Observe response in Halscope

### Tuning Procedure with Halscope

**Step 1: Set Initial Gains (Conservative)**
```bash
halcmd setp pid.x.Pgain 50
halcmd setp pid.x.Igain 0
halcmd setp pid.x.Dgain 0
halcmd setp pid.x.FF1 0
```

**Step 2: Test Step Response**
- Jog X-axis 0.5 inches
- Observe in Halscope:
  - Following error magnitude
  - Settling time
  - Overshoot

**Step 3: Increase P Gain**
- Increase Pgain by 50% increments
- Repeat step response test
- Stop when:
  - Overshoot > 10-15%, or
  - Oscillation appears

**Example**:
```bash
halcmd setp pid.x.Pgain 75
# Test, observe response
halcmd setp pid.x.Pgain 100
# Test, observe response
halcmd setp pid.x.Pgain 150
# Test - too oscillatory, back off
halcmd setp pid.x.Pgain 125  # Final P value
```

**Step 4: Add Velocity Feedforward (FF1)**
- Jog at constant velocity (e.g., 100 IPM)
- Observe following error during constant velocity phase
- Set FF1 = 0.9, increase to 1.0
- Optimal: Following error < 0.001" during cruise

```bash
halcmd setp pid.x.FF1 0.90
# Test
halcmd setp pid.x.FF1 0.95
# Test - following error nearly zero
```

**Step 5: Add Derivative Gain**
- Set Dgain = Pgain / 10 (start)
- Test step response
- Increase until overshoot < 5-10%

```bash
halcmd setp pid.x.Dgain 10
# Test, still 15% overshoot
halcmd setp pid.x.Dgain 15
# Test, 8% overshoot - good
```

**Step 6: Add Integral Gain**
- Set Igain = Pgain / 20 (start)
- Test step response
- Increase until steady-state error eliminated
- Watch for increased overshoot

```bash
halcmd setp pid.x.Igain 5
# Test, steady-state error = 0.0002"
halcmd setp pid.x.Igain 10
# Test, steady-state error < 0.0001" - good
```

**Step 7: Add Acceleration Feedforward (FF2)**
- Command rapid move with high acceleration
- Observe following error spike during accel/decel
- Set FF2 = 0.0001, increase incrementally

```bash
halcmd setp pid.x.FF2 0.001
# Test, transient error reduced
halcmd setp pid.x.FF2 0.002
# Test, transient error < 0.001" - good
```

**Step 8: Save Final Values**

Update `machine.ini` [AXIS_X] section:
```ini
[AXIS_X]
P = 125
I = 10
D = 15
FF0 = 0
FF1 = 0.95
FF2 = 0.002
BIAS = 0.0
DEADBAND = 0.0001
MAX_OUTPUT = 10.0
```

## Advanced HAL Configuration

### Notch Filter for Resonance

**Load Notch Filter Component**:
```hal
loadrt notch names=notch.x
setp notch.x.freq 247          # Resonance frequency (Hz)
setp notch.x.q 6.67            # Q factor (1/(2*zeta))
addf notch.x servo-thread
```

**Insert in PID Output Path**:
```hal
# Before: PID output directly to motor
# net xoutput pid.x.output => pwmgen.0.value

# After: PID output through notch filter
net x-pid-out pid.x.output => notch.x.in
net xoutput notch.x.out => pwmgen.0.value
```

**Effect**: Eliminates 247 Hz resonance from control loop, allows higher gains.

### Low-Pass Filter on Derivative

**Load Low-Pass Filter**:
```hal
loadrt lowpass names=lowpass.x-deriv
setp lowpass.x-deriv.gain 1.0
setp lowpass.x-deriv.time-constant 0.002  # 2 ms = ~80 Hz cutoff
addf lowpass.x-deriv servo-thread
```

**Apply to Encoder Velocity Signal** (used by D term):
```hal
# Encoder velocity to low-pass filter
net x-vel-raw encoder.0.velocity => lowpass.x-deriv.in

# Filtered velocity to PID (for derivative term)
net x-vel-filt lowpass.x-deriv.out => pid.x.command-deriv
```

**Effect**: Reduces noise amplification by derivative term.

### Cross-Coupling for Gantry

**Dual-Motor Gantry** (Y1, Y2):

**Load Gantry Kinematics**:
```hal
loadrt trivkins coordinates=xyyz
```

**INI File**:
```ini
[KINS]
KINEMATICS = trivkins coordinates=xyyz
JOINTS = 4

[JOINT_1]  # Y1 (left motor)
TYPE = LINEAR
MAX_VELOCITY = 8.0
# ... (standard config)

[JOINT_2]  # Y2 (right motor)
TYPE = LINEAR
MAX_VELOCITY = 8.0
# ... (standard config)
```

**HAL Configuration**:
```hal
# Both joints receive same command from trajectory planner
net y-pos-cmd axis.y.motor-pos-cmd => joint.1.motor-pos-cmd
net y-pos-cmd => joint.2.motor-pos-cmd

# Individual feedback from each encoder
net y1-pos-fb encoder.1.position => joint.1.motor-pos-fb
net y2-pos-fb encoder.2.position => joint.2.motor-pos-fb

# Gantry kinematics handles coordination automatically
```

**LinuxCNC Automatic Synchronization**: Kinematics module keeps motors synchronized.

## Trajectory Planner Configuration

### INI File Trajectory Settings

**[TRAJ] Section**:
```ini
[TRAJ]
COORDINATES = X Y Z
LINEAR_UNITS = inch
ANGULAR_UNITS = degree

# Maximum velocities
DEFAULT_LINEAR_VELOCITY = 2.0   # Default jog/rapid speed
MAX_LINEAR_VELOCITY = 10.0      # Maximum allowed speed

# Acceleration
DEFAULT_LINEAR_ACCELERATION = 50.0
MAX_LINEAR_ACCELERATION = 200.0

# Trajectory planning
NO_FORCE_HOMING = 1             # Allow motion before homing (testing only)
POSITION_FILE = position.txt    # Save position on shutdown
```

**Blending Mode**:
- G64: Blending mode (set in G-code or GUI)
- G64 P[tolerance]: Blend with tolerance

**Example G-Code**:
```gcode
G64 P0.005  ; Blend corners with max 0.005" deviation
G1 X10 Y10 F100
G1 X10 Y20
```

### Real-Time Performance Tuning

**Check Real-Time Performance**:
```bash
halrun -I
halcmd loadrt threads period1=1000000 name1=servo-thread
halcmd start
halcmd show thread
```

**Latency Test** (critical for real-time):
```bash
latency-test
```

**Acceptable Latency**:
- Base thread: < 25,000 ns (25 µs)
- Servo thread: < 50,000 ns (50 µs)

**High Latency** (>100 µs):
- Disable power management (CPU frequency scaling)
- Disable SMI (System Management Interrupts)
- Use dedicated real-time system

**Config** (`/etc/default/grub`):
```
GRUB_CMDLINE_LINUX="isolcpus=1 idle=poll"
```

## Homing Configuration

### Home Sequence

**[AXIS_X] Homing Parameters**:
```ini
[AXIS_X]
HOME = 0.0                      # Home position (machine coordinates)
HOME_OFFSET = 0.0               # Offset from home switch to home position
HOME_SEARCH_VEL = 0.50          # Fast search velocity
HOME_LATCH_VEL = 0.05           # Slow latch velocity (after switch found)
HOME_USE_INDEX = 1              # Use encoder index pulse (high precision)
HOME_IGNORE_LIMITS = 0          # Don't ignore limit switches during home
HOME_SEQUENCE = 0               # Homing order (all axes with 0 home simultaneously)
HOME_IS_SHARED = 0              # Shared home switch (multiple axes)
```

**Homing Procedure**:
1. Move in direction of home switch at HOME_SEARCH_VEL
2. When switch triggers, back off slowly
3. Approach again at HOME_LATCH_VEL
4. If HOME_USE_INDEX = 1, latch on encoder index pulse (high precision)
5. Set position to HOME + HOME_OFFSET

### Encoder Index Homing (High Precision)

**Why**: Encoder index pulse = precise reference point (repeatable to 1 encoder count).

**Configuration**:
```ini
HOME_USE_INDEX = 1
```

**HAL Connection**:
```hal
net x-index-enable encoder.0.index-enable <=> axis.x.index-enable
```

**Repeatability**: ±1 encoder count (e.g., 0.000025" for 40,000 count/inch encoder).

## Testing and Validation

### Step Response Test

**Procedure**:
1. Home all axes
2. Jog to mid-position
3. Command 1" move
4. Capture in Halscope
5. Analyze: Overshoot, settling time, following error

**Acceptance Criteria**:
- Overshoot: < 10%
- Settling time: < 200 ms
- Following error (during motion): < 0.002"
- Steady-state error: < 0.0001"

### Circular Interpolation Test

**G-Code** (circular path):
```gcode
G0 X2 Y0
G1 Z-0.1 F10
G2 I-2 J0 F100  ; Full circle, radius = 2"
G0 Z0.1
```

**Measure**:
- Actual radius at multiple points (dial indicator or CMM)
- Deviation from nominal = contouring error

**Typical Results**:
- Well-tuned system: ±0.001-0.002" radial error
- Poor tuning: ±0.005-0.010" radial error

### Practical Cutting Test

**Test Part**: Simple square with rounded corners

**G-Code**:
```gcode
G64 P0.005
G0 X0 Y0 Z0.1
G1 Z-0.1 F10
G1 X4 F100
G3 X4.5 Y0.5 I0 J0.5
G1 Y4
G3 X4 Y4.5 I-0.5 J0
G1 X0
G3 X-0.5 Y4 I0 J-0.5
G1 Y0
G3 X0 Y-0.5 I0.5 J0
G0 Z0.1
```

**Measure**:
- Corner radius accuracy
- Surface finish (visual and Ra measurement)
- Dimensional accuracy (calipers/micrometer)

## Summary

LinuxCNC provides powerful, flexible servo control:

**Key Components**:
1. **HAL**: Flexible hardware abstraction (connect anything to anything)
2. **PID Component**: Built-in position loops with feedforward
3. **Halscope**: Real-time oscilloscope for tuning
4. **Trajectory Planner**: Real-time look-ahead with blending

**Tuning Process**:
1. Configure INI file (axes, limits, scales)
2. Set up HAL (PID, encoders, motor drivers)
3. Tune with Halscope (P, FF1, D, I, FF2)
4. Test and validate (step response, circular interp)

**Advanced Features**:
- Notch filters (resonance suppression)
- Gantry kinematics (automatic synchronization)
- Encoder index homing (high precision)
- Real-time performance tuning

**Next**: [19.11 Implementation in Mach4](section-19.11-mach4.md)

---

**Next**: [19.11 Implementation in Mach4](section-19.11-mach4.md)
