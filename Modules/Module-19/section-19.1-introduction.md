# 19.1 Introduction to Advanced Control

## Control System Fundamentals

### What is Control?

**Control System**: A system that manages, commands, directs, or regulates the behavior of other devices or systems to achieve desired outcomes.

**CNC Context**: Control systems position machine axes accurately and smoothly while following programmed toolpaths.

### Open-Loop vs Closed-Loop Control

**Open-Loop Control** (Stepper Motors):

```
Command → Controller → Motor → Position
         (no feedback)
```

**Characteristics**:
- No measurement of actual position
- Assumes motor follows commands perfectly
- Simple, low-cost
- Risk: Missed steps undetected

**Example**: Stepper motor commanded to move 1000 steps
- Expected: 1000 steps × 0.0002"/step = 0.200" movement
- Actual: If 10 steps missed → 0.198" movement
- **Problem**: Controller doesn't know steps were missed

**Closed-Loop Control** (Servo Motors):

```
Command → Controller → Motor → Position
    ↑                            ↓
    ←──────── Encoder ←──────────┘
          (feedback)
```

**Characteristics**:
- Continuous measurement of actual position
- Controller corrects deviations from desired position
- Higher cost, more complex
- Detects and corrects errors

**Example**: Servo commanded to move 0.200"
- Encoder measures actual position continuously
- If position lags: Controller increases motor torque
- Achieves 0.200" ± 0.0001" (much more accurate)

### Why Closed-Loop?

**Advantages**:
1. **Higher accuracy**: Feedback compensates for disturbances
2. **Faster motion**: Higher accelerations possible (no resonance issues)
3. **Error detection**: Following errors trigger alarms
4. **Load compensation**: Automatically adjusts for cutting forces
5. **Tunable performance**: Adjust response characteristics

**Disadvantages**:
1. **Higher cost**: $500-3000 per axis vs $50-300 for steppers
2. **Complexity**: Requires tuning and setup
3. **Potential instability**: Poor tuning causes oscillation
4. **Maintenance**: Encoders can fail or drift

**When to Use Servos**:
- High-speed machining (>500 IPM rapids)
- Precision requirements (<0.001" positioning)
- High acceleration requirements (>150 in/s²)
- Variable cutting loads (heavy machining)
- Production environment (reliability critical)

**When Steppers Sufficient**:
- Hobby/DIY projects (cost-sensitive)
- Light cutting loads (3D printing, laser cutting, light routing)
- Moderate speeds (<200 IPM)
- Low acceleration requirements (<100 in/s²)

## Servo System Components

### Motor

**Brushed DC Servo**:
- Commutation via brushes (wearing parts)
- Simple to control (voltage → speed)
- Lower cost ($100-500)
- Maintenance: Brush replacement every 2000-5000 hours

**Brushless DC Servo (BLDC)**:
- Electronic commutation (no brushes)
- Higher efficiency (85-95% vs 75-85%)
- Higher reliability (no brush wear)
- Requires more complex drive
- Cost: $300-1500

**AC Servo (PMSM - Permanent Magnet Synchronous Motor)**:
- Similar to BLDC, different control algorithm
- Highest performance (torque density, efficiency)
- Used in industrial applications
- Cost: $500-3000+

**Key Specifications**:
- **Continuous torque**: Torque motor can sustain indefinitely (thermal limit)
- **Peak torque**: Maximum torque for short duration (2-3× continuous)
- **Speed range**: Typical 0-3000 RPM (some up to 6000 RPM)
- **Inertia**: Rotor inertia affects acceleration (lower better for CNC)

**Example Motor**: 400W BLDC servo
- Continuous torque: 1.27 N·m (180 oz-in)
- Peak torque: 3.82 N·m (540 oz-in)
- Rated speed: 3000 RPM
- Rotor inertia: 0.18 kg·cm²

### Encoder (Feedback Device)

**Incremental Encoder**:
- Outputs pulses as shaft rotates
- A and B channels (quadrature) for direction sensing
- Z index pulse once per revolution
- Resolution: 1000-10,000 PPR (pulses per revolution) typical
- Relative position only (loses position on power-off)

**Quadrature Encoding**:
- A and B channels 90° out of phase
- Rising/falling edges on both → 4× resolution
- 1000 PPR encoder → 4000 counts per revolution

**Example**:
- 2000-line encoder (4× = 8000 counts/rev)
- 5mm pitch ballscrew
- Resolution: 5mm / 8000 = 0.000625 mm = 0.625 μm = 0.000025"

**Absolute Encoder**:
- Outputs actual position (not just increments)
- Retains position on power-off
- More expensive ($200-800 vs $50-200 for incremental)
- Used in industrial applications, robotics

**Linear Encoder** (Glass Scale):
- Directly measures linear position (not rotary)
- Eliminates errors from ballscrew pitch variation, backlash
- Higher cost ($300-1500 per axis)
- Precision applications (<0.0001" positioning)

**Resolver**:
- Analog position sensor (AC excited)
- Extremely rugged (no optical parts)
- Lower resolution than encoder
- Used in harsh environments

### Servo Drive (Amplifier)

**Function**: Converts control signals (position commands) into motor power.

**Typical Drive Specifications**:
- Input: DC bus voltage (24-340 VDC typical)
- Output: 3-phase PWM to motor (for BLDC/AC servo)
- Current rating: 5-30A continuous, 15-90A peak
- Control modes: Position, velocity, torque
- Communication: Analog (±10V), step/direction, EtherCAT, CANopen

**Control Loop**:
Modern servo drives implement cascaded control:

```
Position     Velocity      Current
Command  →  Loop    →    Loop     →   Motor
  ↑           ↑            ↑
  └───────────┴────────────┘
        (feedback)
```

**Example Drive**: 750W AC Servo Drive
- Input voltage: 220 VAC single-phase (rectified to 310 VDC bus)
- Output: 3-phase, 0-220 VAC (PWM)
- Continuous current: 3.4A
- Peak current: 10.2A (3× overload)
- Position loop frequency: 1-2 kHz
- Current loop frequency: 8-16 kHz

### Controller

**CNC Controller Functions**:
1. **Interpret G-code**: Parse commands, generate trajectories
2. **Trajectory planning**: Calculate smooth motion profiles
3. **Position control**: PID loops for each axis
4. **Interpolation**: Coordinate multi-axis motion
5. **I/O management**: Spindle, coolant, tool changer control

**Real-Time Requirements**:
- Position loop update: 1-2 kHz typical (every 0.5-1 ms)
- Jitter: <100 μs (deterministic timing critical)
- Latency: <1 ms (command to motion delay)

**Controller Options**:
- **LinuxCNC**: PC-based, open-source, real-time Linux kernel
- **Mach4**: PC-based, commercial, motion plugin architecture
- **Dedicated controller**: FANUC, Siemens, Haas (industrial, closed-source)
- **Arduino/Teensy**: DIY, limited performance (<1 kHz loop rates typically)

## Performance Metrics

### Following Error

**Definition**: Difference between commanded position and actual position during motion.

$$\text{Following Error} = \text{Position}_{\text{commanded}} - \text{Position}_{\text{actual}}$$

**Sources**:
1. **Proportional gain too low**: Motor doesn't respond fast enough
2. **Velocity feedforward insufficient**: Constant lag during motion
3. **Friction**: Stiction causes position lag
4. **Mechanical compliance**: Frame/coupling flex under load

**Example**:
System moving at 100 IPM (1.67 in/s):
- With velocity feedforward: Following error = 0.0005" (good)
- Without velocity feedforward: Following error = 0.005" (poor)

**Acceptable Limits**:
- High-speed machining: <0.001" during rapids
- Precision machining: <0.0005" during cutting
- Heavy machining: <0.002" acceptable (cutting forces dominate)

**Following Error Alarm**:
When following error exceeds threshold (0.010-0.050" typical), controller issues alarm and stops motion.

**Typical scenario**:
- Axis encounters obstruction (crash, over-torque)
- Motor can't overcome resistance
- Position lags further and further behind
- Following error exceeds limit → ALARM

### Settling Time

**Definition**: Time for position to reach and stay within specified tolerance band after commanded move.

**Standard Specification**: Time to settle within ±5% of final value (sometimes ±2% or ±1%)

**Example**:
- Command: Move 1.000"
- Target band: 1.000" ± 0.005" (±0.5%)
- Settling time: Time from start until position remains in 0.995-1.005" range

**Typical Values**:
- Underdamped system (oscillatory): 100-300 ms
- Critically damped: 50-100 ms
- Overdamped (sluggish): 200-500 ms

**Effect on Cycle Time**:
Shorter settling time = faster point-to-point moves.

For 100 point-to-point moves per part:
- 200 ms settling: 20 seconds wasted
- 50 ms settling: 5 seconds wasted
- **Savings**: 15 seconds per part

At 10 parts/hour: 2.5 minutes saved per hour = 4% cycle time reduction

### Rise Time

**Definition**: Time to reach target position (measured from 10% to 90% of final value).

Fast rise time → high acceleration → high throughput

**Trade-off**: Very fast rise time risks overshoot and oscillation.

### Overshoot

**Definition**: Amount by which response exceeds final value before settling.

$$\text{Percent Overshoot} = \frac{\text{Peak Value} - \text{Final Value}}{\text{Final Value}} \times 100\%$$

**Example**:
- Commanded move: 1.000"
- Peak position: 1.015"
- Overshoot: 0.015" / 1.000" = 1.5%

**Acceptable Overshoot**:
- None: Critical positioning (probing, part handling)
- <5%: Precision machining
- <10%: General machining
- <25%: Non-critical positioning

**Zero Overshoot**: Critically damped or overdamped system (slower response)

### Bandwidth

**Definition**: Frequency at which closed-loop gain drops to -3 dB (70.7% of DC gain).

**Practical Meaning**: Maximum frequency of position commands system can follow accurately.

**Typical CNC Servo Bandwidth**: 20-100 Hz

**Example**:
- Bandwidth: 50 Hz
- System can follow sinusoidal position commands up to ~50 Hz
- At 100 Hz (2× bandwidth): Response significantly attenuated

**Higher Bandwidth** → Faster response → Better contour accuracy during high-speed curves

**Bandwidth Limitations**:
1. Mechanical resonances (typically 100-500 Hz)
2. Control loop update rate (1 kHz loop → ~100 Hz max bandwidth)
3. Motor/drive response time

## Open-Loop vs Closed-Loop Trade-Offs

### Accuracy Comparison

**Stepper Open-Loop** (typical 1/8 microstepping):
- Resolution: 0.0001-0.0005" (depends on screw pitch)
- Repeatability: ±0.001-0.005" (depends on missed steps)
- Absolute accuracy: ±0.005-0.020" (cumulative errors)

**Servo Closed-Loop** (2000-line encoder):
- Resolution: 0.00002-0.00005"
- Repeatability: ±0.0001-0.0005"
- Absolute accuracy: ±0.0005-0.002" (limited by encoder mounting/coupling)

**Linear Encoder Servo**:
- Resolution: 0.00002-0.00005" (0.5-1 μm)
- Repeatability: ±0.00005-0.0002"
- Absolute accuracy: ±0.0001-0.0005" (limited by mechanical loop)

### Speed Comparison

**Stepper**:
- Typical max speed: 100-300 IPM (limited by torque drop-off)
- Acceleration: 50-100 in/s² (limited by resonance)

**Servo**:
- Typical max speed: 300-1000+ IPM (motor-limited)
- Acceleration: 200-500 in/s² (motor torque-limited)

**Time Savings Example**:
1" rapid move:

**Stepper** (150 IPM = 2.5 in/s, 75 in/s² accel):
- Accel distance: v²/(2a) = 2.5²/(2×75) = 0.042"
- Accel time: v/a = 2.5/75 = 0.033 s
- Constant velocity distance: 1.0 - 2×0.042 = 0.916"
- Constant velocity time: 0.916/2.5 = 0.366 s
- Total time: 2×0.033 + 0.366 = 0.432 s

**Servo** (600 IPM = 10 in/s, 300 in/s² accel):
- Accel distance: 10²/(2×300) = 0.167"
- Accel time: 10/300 = 0.033 s
- Constant velocity distance: 1.0 - 2×0.167 = 0.666"
- Constant velocity time: 0.666/10 = 0.067 s
- Total time: 2×0.033 + 0.067 = 0.133 s

**Servo is 3.2× faster** for this rapid move!

For 50 rapids per part: 15 seconds saved (stepper) vs 6.7 seconds (servo) = 8.3 s savings per part

### Cost Comparison (Single Axis)

**Stepper System**:
- Motor: $50-150
- Driver: $30-100
- Power supply: $30-80
- **Total: $110-330 per axis**

**Basic Servo System**:
- Motor with encoder: $200-500
- Servo drive: $250-800
- Power supply: $50-150
- **Total: $500-1450 per axis**

**High-Performance Servo**:
- Motor with high-res encoder: $400-1000
- Industrial servo drive: $500-2000
- Power supply: $100-300
- **Total: $1000-3300 per axis**

**Linear Scale Servo** (ultimate accuracy):
- Motor with encoder: $200-500
- Linear scale (glass): $300-1500
- Servo drive: $500-1500
- **Total: $1000-3500 per axis**

### Cost-Benefit Analysis

**When Steppers Make Sense**:
- DIY/hobby projects (budget < $2000 total)
- Light cutting (3D printing, laser, light routing)
- Cycle time not critical
- Moderate precision requirements (±0.005")

**When Servos Justified**:
- Commercial/production use
- Cycle time reduction pays for itself (months to 1-2 years)
- Precision requirements (±0.001" or better)
- High-speed machining (>400 IPM rapids)

**ROI Example**:
Small production shop, $75/hour machine rate:
- Servo upgrade cost: 3 axes × $800 = $2400
- Cycle time reduction: 25% (from 8 min to 6 min per part)
- Parts per day (8 hrs): 60 parts (stepper) → 80 parts (servo)
- Additional revenue: 20 parts/day × $20 margin = $400/day
- **ROI**: 2400 / 400 = 6 days!

(Of course, bottlenecks elsewhere may prevent full realization of time savings)

## System Dynamics Overview

### Second-Order System Model

Most mechanical systems approximate second-order response:

$$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

where:
- $\omega_n$ = natural frequency (rad/s)
- $\zeta$ (zeta) = damping ratio

**Damping Ratio Effects**:

**Underdamped** ($\zeta$ < 1):
- Oscillatory response
- Overshoot present
- Fast rise time
- Example: $\zeta$ = 0.5 → 16% overshoot

**Critically Damped** ($\zeta$ = 1):
- Fastest response without overshoot
- Optimal for many CNC applications
- No oscillation

**Overdamped** ($\zeta$ > 1):
- Sluggish response
- No overshoot
- Long settling time
- Too conservative for most CNC

**Typical CNC Target**: $\zeta$ = 0.7-0.9 (slightly underdamped, minimal overshoot, fast response)

### Natural Frequency

**Definition**: Frequency at which system oscillates if disturbed with no damping.

**CNC Context**: Higher natural frequency → faster response → higher bandwidth

**Factors Affecting Natural Frequency**:
1. **Mechanical stiffness**: Stiffer machine → higher $\omega_n$
2. **Moving mass**: Heavier axis → lower $\omega_n$
3. **Control gains**: Higher gains → effectively higher $\omega_n$

**Example**:
- Stiff machine: $\omega_n$ = 60 rad/s (9.5 Hz)
- Flexible machine: $\omega_n$ = 20 rad/s (3.2 Hz)

Stiff machine can achieve 3× faster response!

**Why Mechanical Design Matters**:
No amount of control tuning compensates for poor mechanical design. Build it stiff!

## Introduction to PID Control

**PID**: Proportional-Integral-Derivative

**Function**: Calculate motor command based on position error.

**Block Diagram**:

```
Error → [ P ]  →  +
  ↓     [ I ]  →  + → Motor Command
  ↓     [ D ]  →  +
```

**Error** = Commanded Position - Actual Position

### Proportional (P)

**Formula**: $u_P = K_P \times e$

where:
- $u_P$ = proportional output
- $K_P$ = proportional gain
- $e$ = error

**Effect**: Output proportional to current error
- Large error → large correction
- Small error → small correction

**Problem**: Steady-state error remains (P-only can't eliminate error completely)

**Example**:
- $K_P$ = 100
- Error = 0.010"
- Output = 100 × 0.010 = 1.0 (some units, e.g., volts or %)

### Integral (I)

**Formula**: $u_I = K_I \times \int e \, dt$

**Effect**: Accumulates error over time
- Eliminates steady-state error
- Corrects for constant disturbances (friction, gravity)

**Problem**: Can cause overshoot and oscillation if too high

**Example**:
- Error persists at 0.001" for 0.1 seconds
- $K_I$ = 500
- Integral term accumulates: 500 × 0.001 × 0.1 = 0.05

### Derivative (D)

**Formula**: $u_D = K_D \times \frac{de}{dt}$

**Effect**: Responds to rate of change of error
- Anticipates future error
- Provides damping (reduces overshoot)

**Problem**: Amplifies high-frequency noise

**Example**:
- Error changing at 0.1 in/s (rapidly decreasing)
- $K_D$ = 10
- Output = 10 × 0.1 = 1.0 (opposes rapid change)

### Combined PID

$$u = K_P e + K_I \int e \, dt + K_D \frac{de}{dt}$$

**Tuning Goal**: Find $K_P$, $K_I$, $K_D$ values that achieve:
- Fast response (high $K_P$, $K_D$)
- No steady-state error ($K_I$ eliminates)
- Minimal overshoot (balanced $K_P$, $K_D$)
- Stable (gains not too high)

## Preview of Advanced Techniques

### Feedforward Control

**Limitation of Feedback-Only**: PID reacts to error (inherently lagging)

**Feedforward Solution**: Add term based on commanded velocity/acceleration
- Anticipates required motor torque
- Reduces following error during motion

**Example**:
- Without feedforward: 0.005" following error during 200 IPM motion
- With velocity feedforward: 0.0005" following error (10× improvement)

### Notch Filters

**Problem**: Mechanical resonances excite oscillation

**Solution**: Notch filter rejects specific frequency
- Identify resonance (e.g., 247 Hz)
- Apply notch filter at 247 Hz
- Eliminates resonance from control loop

**Result**: Can increase gains (faster response) without exciting resonance

### State-Space Control

**Modern Control Theory**: Model system as set of first-order differential equations

**Advantages**:
- Handle multi-input, multi-output systems
- Optimal controller design (LQR - Linear Quadratic Regulator)
- State estimation (Kalman filter)

**CNC Application**: Mainly research/advanced industrial systems (LinuxCNC uses classical PID)

## Summary

Advanced control systems enable high-performance CNC machines through:

1. **Closed-loop feedback**: Continuous error correction for accuracy
2. **PID control**: Tunable response characteristics
3. **Advanced techniques**: Feedforward, filtering, trajectory optimization
4. **Performance metrics**: Quantify and optimize system behavior

**Next Steps**:
- Learn control theory fundamentals (Section 19.2)
- Master PID tuning (Sections 19.3-19.4)
- Implement trajectory planning (Sections 19.6-19.9)
- Configure real systems (Sections 19.10-19.11)

**Key Takeaway**: Good mechanical design + proper servo tuning = high-performance CNC machine

---

**Next**: [19.2 Control System Theory](section-19.2-control-theory.md)
