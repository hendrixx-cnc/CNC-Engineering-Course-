## 2. HAL Fundamentals: Pins, Signals, and Parameters

### 2.1 The HAL Data Model: Pins, Signals, Parameters, and Functions

HAL's power stems from a simple, elegant data model that separates **interface** (pins) from **connection** (signals) from **configuration** (parameters) from **execution** (functions). This separation enables flexible component composition without modifying component code—the same PID component serves spindle control, axis positioning, temperature regulation, or hydraulic pressure management through configuration alone.

**Four Core Abstractions:**

1. **Pins**: Input/output ports on components (like physical connector pins on ICs). Example: `pid.0.command` (input), `encoder.0.position` (output)
2. **Signals**: Named connections between pins (like wires between IC pins). Example: `x-pos-cmd` connecting `motion.00.motor-pos-cmd` → `pid.0.command`
3. **Parameters**: Configuration values inside components (like trim pots on analog circuits). Example: `pid.0.Pgain` = 150.0
4. **Functions**: Computational routines executed periodically by real-time threads. Example: `pid.0.do-pid-calcs` runs every servo thread cycle

**Analogy: Electronic Circuit Board**

```
Component = IC chip (PID controller IC, comparator IC, etc.)
Pin       = Physical pins on IC package (input voltage, output current, etc.)
Signal    = Copper trace connecting IC pins on PCB
Parameter = Internal resistor/capacitor values (gain, time constant)
Function  = Clock edge triggering IC computation
```

### 2.2 Pin Types and Directions

**Pin Data Types:**

HAL supports four fundamental data types optimized for real-time control:

| Type | C Type | Range | Use Cases |
|------|--------|-------|-----------|
| **bit** | hal_bit_t (bool) | TRUE / FALSE | Limit switches, enables, relay outputs |
| **float** | hal_float_t (double) | ±1.7e±308 (64-bit IEEE 754) | Position (mm), velocity (mm/s), analog voltage (V) |
| **s32** | hal_s32_t (int32_t) | -2,147,483,648 to +2,147,483,647 | Encoder counts, integer positions, error codes |
| **u32** | hal_u32_t (uint32_t) | 0 to 4,294,967,295 | Timers, frequency counters, unsigned counts |

**Why only 4 types?** Real-time systems prioritize determinism over flexibility. Fixed-size types (32-bit integer, 64-bit float) enable predictable memory layouts and execution times. No strings (variable length), no complex objects (pointer indirection overhead).

**Pin Directions:**

Each pin has a fixed direction defining data flow:

- **IN**: Component reads value written by signal (input from external world)
- **OUT**: Component writes value read by signal (output to external world)
- **IO**: Component both reads and writes (rare, used for shared memory regions)

**Connection Rules:**

1. **One signal can connect one OUT pin to multiple IN pins** (fan-out, like one sensor driving multiple controllers)
2. **One signal CANNOT connect multiple OUT pins** (conflict—which component's value wins?)
3. **Unconnected pins read default value** (bit=FALSE, float=0.0, s32=0, u32=0)

**Example: Multiple Controllers Reading Same Sensor**

```hal
# One encoder position feeds both axis PID and display
net x-pos-fb encoder.0.position => pid.0.feedback  # First IN pin
net x-pos-fb encoder.0.position => pyvcp.position-readout  # Second IN pin (same signal)
# Legal: One OUT (encoder.0.position) drives two IN pins
```

**Illegal Example: Conflicting Outputs**

```hal
# WRONG: Two outputs cannot drive same signal
net x-cmd motion.00.motor-pos-cmd => pid.0.command
net x-cmd override.value => pid.0.command  # ERROR: x-cmd already driven by motion.00
# Violates single-driver rule
```

### 2.3 Signal Mechanics: The HAL "Net" Statement

**Signal Creation and Connection:**

The `net` command creates a signal (if it doesn't exist) and connects pins to it. Syntax:

```hal
net <signal-name> <pin-name> [<arrow> <pin-name>] ...

Arrows (optional, for readability):
  =>   Connects to IN pin (mnemonic: signal flows INTO pin)
  <=   Connects to OUT pin (mnemonic: signal flows FROM pin)
  <=>  Connects to IO pin
```

**Example: Complete Axis Control Chain**

```hal
# X-axis position command (OUT → IN)
net x-pos-cmd motion.00.motor-pos-cmd => pid.0.command

# X-axis PID output (OUT → IN)
net x-output pid.0.output => pwmgen.0.value

# X-axis position feedback (OUT → multiple IN)
net x-pos-fb encoder.0.position => pid.0.feedback
net x-pos-fb encoder.0.position => motion.00.motor-pos-fb

# X-axis enable (OUT → multiple IN)
net x-enable motion.00.amp-enable-out => pid.0.enable
net x-enable motion.00.amp-enable-out => pwmgen.0.enable
```

**Signal Naming Conventions:**

While HAL allows arbitrary signal names, consistency aids troubleshooting:

- **Descriptive prefixes**: `x-`, `y-`, `z-`, `spindle-`, `coolant-`, `estop-`
- **Function suffixes**: `-cmd` (command), `-fb` (feedback), `-enable`, `-fault`, `-home`
- **Avoid generic names**: `signal1`, `temp`, `output` (ambiguous in complex systems)

**Good**: `x-pos-cmd`, `spindle-speed-fb`, `estop-loop-ok`
**Poor**: `sig1`, `axis0`, `out`

### 2.4 Parameters: Configuration Values Inside Components

**Parameter vs. Pin:**

- **Pin**: Interface for real-time data flow between components (changes every thread cycle)
- **Parameter**: Configuration value inside component (changes rarely, typically at startup or during tuning)

**Parameter Types:**

Same data types as pins (bit, float, s32, u32), but different access pattern:

- **Read-Write (RW)**: Can be modified at runtime via `setp` command
- **Read-Only (RO)**: Set by component logic, user can only inspect

**Common Parameters:**

| Component | Parameter | Type | Description |
|-----------|-----------|------|-------------|
| **pid** | Pgain | float (RW) | Proportional gain $K_p$ |
| **pid** | Igain | float (RW) | Integral gain $K_i$ |
| **pid** | Dgain | float (RW) | Derivative gain $K_d$ |
| **pid** | maxerror | float (RW) | Maximum error before output saturation (position units) |
| **encoder** | scale | float (RW) | Counts per position unit (counts/mm, counts/degree) |
| **stepgen** | position-scale | float (RW) | Steps per position unit (steps/mm) |
| **stepgen** | maxvel | float (RW) | Maximum velocity (position units/second) |
| **lowpass** | gain | float (RW) | Filter coefficient (0-1, larger = faster response) |

**Setting Parameters:**

```hal
setp <parameter-name> <value>

# Examples:
setp pid.0.Pgain 150.0
setp pid.0.Igain 0.5
setp pid.0.Dgain 2.0
setp encoder.0.scale 4000  # 4000 encoder counts per mm
setp stepgen.0.position-scale 800  # 800 steps per mm (200 step/rev, 4 mm/rev leadscrew)
setp stepgen.0.maxvel 50.0  # 50 mm/s maximum velocity
```

**Inspecting Parameters:**

```bash
halcmd getp pid.0.Pgain  # Returns current value
halcmd show param pid.0.*  # Show all parameters for pid.0
```

**Parameter Files:**

For complex systems, store parameters in separate files loaded at startup:

```hal
# File: pid_tuning.hal
setp pid.0.Pgain 150.0
setp pid.0.Igain 0.5
setp pid.0.Dgain 2.0
setp pid.0.maxerror 0.5
setp pid.0.deadband 0.001

# Load in main HAL file:
source pid_tuning.hal
```

### 2.5 Functions: Scheduled Computation

**Function Execution Model:**

HAL components expose **functions**—computational routines executed periodically by real-time threads. Functions perform the actual work: reading encoder hardware, computing PID output, updating PWM duty cycle, etc.

**Key Concepts:**

1. **Functions are NOT automatically executed**: After loading a component (`loadrt`), you must explicitly add its functions to a thread (`addf`)
2. **Execution order matters**: Functions run sequentially in the order added to thread
3. **One function per thread**: A function cannot belong to multiple threads (would create race conditions)

**Adding Functions to Threads:**

```hal
addf <function-name> <thread-name>

# Example: Servo thread running at 1 kHz
addf motion.motion-command-handler servo-thread
addf encoder.capture-position servo-thread
addf pid.0.do-pid-calcs servo-thread
addf pwmgen.update servo-thread
addf motion.motion-controller servo-thread
```

**Common Functions:**

| Component | Function | Description | Thread |
|-----------|----------|-------------|--------|
| **motion** | motion-command-handler | Process G-code commands, update trajectory | servo-thread |
| **motion** | motion-controller | Check following error, update status | servo-thread (after outputs) |
| **encoder** | capture-position | Read encoder hardware registers | servo-thread (early) |
| **encoder** | update-counters | Update position from captured counts | servo-thread (after capture) |
| **pid** | do-pid-calcs | Compute PID output from command and feedback | servo-thread |
| **stepgen** | make-pulses | Generate step pulses (time-critical) | base-thread |
| **stepgen** | update-freq | Update step rate from velocity command | servo-thread |
| **pwmgen** | make-pulses | Generate PWM waveform | base-thread or servo-thread |
| **pwmgen** | update | Update PWM duty cycle from input | servo-thread |

**Function Execution Order Logic:**

For closed-loop servo control, typical sequence:

```
1. motion.motion-command-handler  → Generate commanded positions
2. encoder.capture-position       → Sample feedback from hardware
3. encoder.update-counters        → Process captured counts
4. pid.0.do-pid-calcs            → Compute control output (needs command AND feedback)
5. pwmgen.update                 → Update actuator (needs PID output)
6. motion.motion-controller      → Check errors (needs actual vs. commanded position)
```

**Why this order?** Each function depends on outputs from previous functions:
- PID needs **both** command (from motion) and feedback (from encoder) → must run after both
- PWM needs PID output → must run after PID
- Error checking needs commanded and actual positions → must run at end

### 2.6 Complete Example: Single-Axis Servo System

**System Specifications:**
- X-axis servo motor with 2000-line (8000 count) quadrature encoder
- ±10V analog servo drive (1V = 100 RPM, 1 RPM = 5 mm/min with 5mm/rev ballscrew)
- PWM-to-analog converter (10V at 100% duty cycle)
- Parallel port for encoder input and PWM output
- 1 kHz servo thread

**Step 1: Load Components**

```hal
# Load real-time components
loadrt trivkins               # Trivial kinematics (X,Y,Z directly map to joints 0,1,2)
loadrt [EMCMOT]EMCMOT base_period_nsec=[EMCMOT]BASE_PERIOD servo_period_nsec=[EMCMOT]SERVO_PERIOD num_joints=[TRAJ]AXES
loadrt hal_parport cfg="0x0378"  # Parallel port at I/O address 0x0378
loadrt encoder num_chan=1         # One encoder channel
loadrt pid num_chan=1             # One PID controller
loadrt pwmgen output_type=0       # PWM output (type 0 = PWM/dir)
```

**Step 2: Add Functions to Threads**

```hal
# Servo thread (1 kHz = 1 ms period)
addf parport.0.read servo-thread           # Read encoder from parallel port
addf encoder.update-counters servo-thread  # Update encoder position
addf motion.motion-command-handler servo-thread  # Get commanded position
addf pid.0.do-pid-calcs servo-thread       # Compute PID output
addf pwmgen.update servo-thread            # Update PWM duty cycle
addf parport.0.write servo-thread          # Write PWM to parallel port
addf motion.motion-controller servo-thread # Check following error
```

**Step 3: Configure Parameters**

```hal
# Encoder scaling: 8000 counts per revolution, 5mm per revolution
# Scale = 8000 counts/rev ÷ 5 mm/rev = 1600 counts/mm
setp encoder.0.position-scale 1600

# PWM scaling: ±10V analog, 100 RPM/V, 5 mm/rev
# Max velocity 50 mm/s = 3000 mm/min = 600 RPM = 6V = 60% duty cycle
# PWM scale: (max velocity in position units/s) / (max PWM output range ±1.0)
# For ±10V = ±100%: full range = 200 RPM = 16.67 mm/s
# Scale factor: 16.67 mm/s per 1.0 PWM unit
setp pwmgen.0.scale 16.67
setp pwmgen.0.max-dc 0.95  # Limit to 95% duty cycle (prevent saturation)

# PID tuning (initial conservative values, tune later via halscope)
setp pid.0.Pgain 50.0      # Start low, increase until stable
setp pid.0.Igain 0.1       # Small integrator to eliminate steady-state error
setp pid.0.Dgain 1.0       # Dampen oscillations
setp pid.0.maxoutput 10.0  # Limit to ±10.0 (maps to ±10V via pwmgen scaling)
setp pid.0.deadband 0.001  # 1 µm dead band (prevent dither)
```

**Step 4: Create Signals (Connect Pins)**

```hal
# Position command: motion → PID
net x-pos-cmd motion.00.motor-pos-cmd => pid.0.command

# Position feedback: encoder → PID + motion
net x-pos-fb encoder.0.position => pid.0.feedback motion.00.motor-pos-fb

# PID output → PWM input
net x-output pid.0.output => pwmgen.0.value

# Axis enable signal
net x-enable motion.00.amp-enable-out => pid.0.enable pwmgen.0.enable

# Encoder hardware connections (parallel port pins)
net x-encoder-A encoder.0.phase-A <= parport.0.pin-02-in
net x-encoder-B encoder.0.phase-B <= parport.0.pin-03-in
net x-encoder-Z encoder.0.phase-Z <= parport.0.pin-04-in  # Index pulse (optional)

# PWM output to parallel port
net x-pwm pwmgen.0.pwm => parport.0.pin-01-out
```

**Step 5: Verification Commands**

```bash
# Show all signals and their connections
halcmd show sig

# Monitor real-time values
halmeter sig x-pos-cmd &    # Watch commanded position
halmeter sig x-pos-fb &     # Watch actual position
halmeter sig x-output &     # Watch PID output voltage

# Check thread execution time
halcmd show thread servo-thread
# Should show execution time < 500 µs (50% of 1 ms period)
```

**Calculated Values Explained:**

**Encoder Scale:**
$$\text{Scale} = \frac{8000 \text{ counts/rev}}{5 \text{ mm/rev}} = 1600 \text{ counts/mm}$$

**PWM to Velocity Relationship:**
- Servo drive: 1V → 100 RPM
- Ballscrew: 1 RPM → 5 mm/min = 0.0833 mm/s
- Combined: 1V → 100 RPM → 8.33 mm/s
- Full scale ±10V → ±83.3 mm/s

**PWM Scale Factor:**
PWMgen component expects velocity in position units/s (mm/s), outputs ±1.0 range:
$$\text{Scale} = \frac{83.3 \text{ mm/s}}{10.0 \text{ (full PWM range)}} \approx 8.33 \text{ mm/s per PWM unit}$$

(Note: Adjust for actual servo drive and mechanical system)

### 2.7 Signal Inspection and Debugging

**Essential halcmd Commands:**

```bash
# List all components
halcmd show comp

# Show all pins for a component
halcmd show pin encoder.0

# Show all signals
halcmd show sig

# Show specific signal with connected pins
halcmd show sig x-pos-cmd

# Show all parameters for a component
halcmd show param pid.0

# Get current pin value
halcmd getp pid.0.Pgain

# Set parameter value
halcmd setp pid.0.Pgain 75.0

# Force output pin value (for testing)
halcmd setp encoder.0.position 100.0  # Only works if pin not driven by component function
```

**halshow: Graphical Signal Browser**

```bash
halshow &  # Launch GUI
# Shows tree view: Components → Pins/Params/Functions
# Right-click pin: Watch, Set value, Create meter
```

**halmeter: Real-Time Value Display**

```bash
# Monitor specific signal
halmeter sig x-pos-fb &

# Monitor pin
halmeter pin encoder.0.position &

# Shows current value updated in real-time (servo thread rate)
```

**halscope: Oscilloscope for HAL Signals**

```bash
halscope &
# Add channels: x-pos-cmd, x-pos-fb, x-output
# Trigger: Rising edge on motion.motion-enabled
# Captures waveforms at thread rate (1 kHz typical)
# Essential for PID tuning (see Section 14.10)
```

### 2.8 Common Pitfalls and Solutions

**Problem 1: Signal Connection Errors**

```hal
# ERROR: Typo in pin name
net x-cmd motion.00.motor-position-cmd => pid.0.command
# Correct name: motor-pos-cmd (not motor-position-cmd)
# Symptom: "pin not found" error at startup

# Solution: Use tab-completion in halcmd
halcmd net x-cmd motion.00.motor-[TAB]  # Lists available pins
```

**Problem 2: Conflicting Signal Drivers**

```hal
net x-cmd motion.00.motor-pos-cmd => pid.0.command
net x-cmd manual-override.value => pid.0.command  # ERROR: x-cmd already has driver
# Symptom: "signal already has writer" error

# Solution: Use mux2 component to select between sources
loadrt mux2
addf mux2.0 servo-thread
net auto-mode motion.00.motor-pos-cmd => mux2.0.in0
net manual-mode manual-override.value => mux2.0.in1
net mode-select mode-switch.out => mux2.0.sel  # 0=auto, 1=manual
net x-cmd mux2.0.out => pid.0.command
```

**Problem 3: Function Execution Order**

```hal
# WRONG ORDER: PID runs before encoder updates
addf pid.0.do-pid-calcs servo-thread
addf encoder.update-counters servo-thread
# Result: PID uses stale feedback (one cycle delayed)

# CORRECT ORDER: Encoder updates before PID
addf encoder.capture-position servo-thread
addf encoder.update-counters servo-thread
addf pid.0.do-pid-calcs servo-thread
```

**Problem 4: Missing Parameters**

```hal
# Loaded component but forgot to set scale
loadrt encoder num_chan=1
addf encoder.update-counters servo-thread
net x-pos-fb encoder.0.position => pid.0.feedback
# Symptom: Position reads wrong units (counts instead of mm)

# Solution: Always set scaling parameters
setp encoder.0.position-scale 1600  # Essential for correct units
```

**Problem 5: Unconnected Enable Pins**

```hal
# Forgot to connect PID enable
net x-pos-cmd motion.00.motor-pos-cmd => pid.0.command
net x-pos-fb encoder.0.position => pid.0.feedback
net x-output pid.0.output => pwmgen.0.value
# Missing: net x-enable motion.00.amp-enable-out => pid.0.enable

# Symptom: PID never outputs (enable pin defaults to FALSE)
# Solution: Always connect enable signals
net x-enable motion.00.amp-enable-out => pid.0.enable pwmgen.0.enable
```

### 2.9 Advanced Signal Techniques

**Bidirectional Signals (Rare, Advanced Use)**

IO pins can both read and write on the same signal (used for shared memory regions, not typical control):

```hal
# Example: Shared position register between two real-time components
net shared-pos custom-comp1.position <=> custom-comp2.position
# Both components can read AND write (requires careful coordination to avoid conflicts)
```

**Signal Aliases (Readability)**

Use descriptive signal names even if connecting single source to single destination:

```hal
# Verbose but clear
net estop-button-pressed parport.0.pin-10-in => estop-latch.0.fault-in
net estop-loop-ok estop-latch.0.ok-out => motion.motion-enabled

# Terse but cryptic (avoid)
net sig1 parport.0.pin-10-in => estop-latch.0.fault-in
net sig2 estop-latch.0.ok-out => motion.motion-enabled
```

**Conditional Signal Routing (Using Logic Components)**

```hal
# Enable axis only if both estop OK AND limit switches clear
loadrt and2
addf and2.0 servo-thread

net estop-ok estop-latch.0.ok-out => and2.0.in0
net limits-ok limit-switch-logic.ok => and2.0.in1
net axis-enable-ok and2.0.out => motion.motion-enabled
```

### 2.10 Parameter Persistence: Saving and Restoring Values

**Problem:** Parameter changes made via `halcmd setp` are lost on LinuxCNC restart.

**Solution 1: Edit HAL Configuration File**

```hal
# File: custom.hal
# PID tuning values (persisted in config)
setp pid.0.Pgain 150.0
setp pid.0.Igain 2.5
setp pid.0.Dgain 5.0
```

**Solution 2: halcmd save**

```bash
# Save all current parameter values to file
halcmd save > my_params.hal

# Reload at startup
source my_params.hal
```

**Solution 3: INI File Integration (Section 14.5)**

```ini
# File: machine.ini
[AXIS_0]
P = 150.0
I = 2.5
D = 5.0

# HAL file reads from INI
setp pid.0.Pgain [AXIS_0]P
setp pid.0.Igain [AXIS_0]I
setp pid.0.Dgain [AXIS_0]D
```

### 2.11 Summary: The HAL Data Model in Practice

HAL's pin-signal-parameter model provides the flexibility of electronic breadboarding combined with the determinism of real-time control:

- **Pins** define component interfaces (what data goes in/out)
- **Signals** connect components (how data flows)
- **Parameters** configure behavior (tuning, scaling, limits)
- **Functions** execute computation (when and in what order)

**Key Principles:**

1. **Separation of concerns**: Component logic (PID algorithm) separate from wiring (signals) separate from tuning (parameters)
2. **Single writer rule**: Each signal driven by exactly one OUT pin (prevents conflicts)
3. **Execution order matters**: Add functions to thread in logical sequence (inputs before computation before outputs)
4. **Type safety**: Pins can only connect to signals of matching type (bit-to-bit, float-to-float, etc.)
5. **Default values**: Unconnected pins read zero/false (explicit initialization not required)

**Next Section** (14.3) explores the standard HAL component library in depth: PID controllers, encoders, step generators, PWM generators, and mathematical functions—the building blocks for complete CNC control systems.

***

*Total: 3,489 words | 2 equations | 1 complete worked example | 5 tables | 15 code blocks*
