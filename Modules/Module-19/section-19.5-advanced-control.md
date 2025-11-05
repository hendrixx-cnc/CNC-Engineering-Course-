# 19.5 Advanced Control Techniques

## Beyond Basic PID

Basic PID control provides excellent performance for many CNC applications, but advanced techniques can further improve:

- **Following error reduction**: Feedforward control
- **Resonance suppression**: Notch and low-pass filters
- **Load compensation**: Adaptive control
- **Multi-axis coordination**: Cross-coupling control
- **Precision enhancement**: Dual-loop control, backlash compensation

This section covers practical advanced techniques applicable to CNC servo systems.

## Feedforward Control

### The Feedforward Concept

**Fundamental Limitation of Feedback**: PID control is inherently **reactive** — it responds to errors after they occur.

**Feedforward Solution**: Add control terms based on **commanded motion** (not error).

**Analogy**: Driving a car
- **Feedback only**: Wait until speed drops below target, then press gas (slow response)
- **Feedforward**: Anticipate hill ahead, press gas before speed drops (proactive)

**CNC Application**:
- **Feedback (PID)**: Corrects position errors
- **Feedforward**: Anticipates required motor torque for commanded motion

**Result**: Dramatically reduced following error during motion.

### Velocity Feedforward (FF1)

**Principle**: During constant velocity motion, motor must produce torque to overcome friction and viscous damping.

**Without FF1**:
- Commanded velocity: 100 IPM
- Actual position lags by 0.005" (following error)
- PID works hard to correct this persistent error

**With FF1**:
- Add command proportional to commanded velocity
- Motor immediately receives correct command for steady-state velocity
- Following error reduced to 0.0005" (10× improvement!)

**Formula**:
$$u_{FF1} = \text{FF1} \times \dot{r}(t)$$

where:
- FF1 = velocity feedforward gain
- $\dot{r}(t)$ = commanded velocity

**Total Control**:
$$u_{total} = K_P e + K_I \int e \, dt + K_D \frac{de}{dt} + \text{FF1} \cdot \dot{r}$$

**Tuning FF1**:

**Step 1**: Tune PID first (P, D, I)

**Step 2**: Command constant-velocity motion (e.g., 200 IPM jog)

**Step 3**: Observe following error during constant velocity portion

**Step 4**: Increase FF1 from 0 to 1.0 (typically)
- FF1 = 0: No feedforward (baseline following error)
- FF1 = 0.5: Following error reduced by ~50%
- FF1 = 1.0: Following error minimal (may need fine-tuning)
- FF1 > 1.0: Overshoot, position leads command (too much)

**Optimal FF1**: Following error during constant velocity < 0.001" (±1 encoder count)

**Typical Values**: FF1 = 0.9-1.0 for well-tuned systems

**Example**:
- Without FF1: Following error = 0.006" at 300 IPM
- With FF1 = 0.95: Following error = 0.0005" at 300 IPM
- **12× improvement**

**LinuxCNC Configuration**:
```
setp pid.x.FF1 0.95
```

### Acceleration Feedforward (FF2)

**Principle**: During acceleration, motor must produce torque proportional to acceleration (Newton's 2nd law: $F = ma$).

**Without FF2**:
- Commanded acceleration: 200 in/s²
- Position lags during acceleration phase
- Following error peaks during acceleration (transient error)

**With FF2**:
- Add command proportional to commanded acceleration
- Motor receives correct torque for acceleration instantly
- Following error during acceleration reduced

**Formula**:
$$u_{FF2} = \text{FF2} \times \ddot{r}(t)$$

where:
- FF2 = acceleration feedforward gain
- $\ddot{r}(t)$ = commanded acceleration

**Total Control** (with FF1 and FF2):
$$u_{total} = K_P e + K_I \int e \, dt + K_D \frac{de}{dt} + \text{FF1} \cdot \dot{r} + \text{FF2} \cdot \ddot{r}$$

**Tuning FF2**:

**Step 1**: Tune PID and FF1 first

**Step 2**: Command trapezoidal move (acceleration → constant velocity → deceleration)

**Step 3**: Observe following error during acceleration and deceleration phases

**Step 4**: Increase FF2 from 0
- Start with FF2 = 0.0001-0.001 (small values)
- Increase until transient following error minimized
- Too high: Overshoot during acceleration

**Optimal FF2**: Following error spike during acceleration < 0.001-0.002"

**Typical Values**: FF2 = 0.0001-0.005 (depends on inertia and units)

**Example**:
- 1" rapid move, 200 in/s² acceleration
- Without FF2: Peak following error = 0.004" during acceleration
- With FF2 = 0.002: Peak following error = 0.001" during acceleration
- **4× improvement in transient response**

**LinuxCNC Configuration**:
```
setp pid.x.FF1 0.95
setp pid.x.FF2 0.002
```

### Feedforward Gain Calculation (Theoretical)

**Velocity Feedforward** (first-order plant):

For plant $G(s) = \frac{K}{\tau s + 1}$:

$$\text{FF1} = \frac{1}{K}$$

**Acceleration Feedforward** (second-order plant):

For plant $G(s) = \frac{1}{ms^2 + bs + k}$ (mass-spring-damper):

$$\text{FF2} = m$$

**CNC Context**:
- $m$ = moving mass + reflected load inertia
- $b$ = viscous damping
- $k$ = spring stiffness (if flexible coupling)

**Example**:
- Axis moving mass: 50 kg
- Ballscrew pitch: 5 mm/rev
- Motor inertia (reflected): 0.5 kg equivalent
- Total effective mass: 50.5 kg

$$\text{FF2} = 50.5 \text{ kg} = 50.5 \text{ N/(m/s}^2\text{)}$$

Convert to system units (if needed).

**Practical Note**: Calculated values are starting points; empirical tuning gives best results.

### Bias (Constant Offset)

**Purpose**: Compensate for constant disturbances (gravity on vertical axis, friction).

**Formula**:
$$u_{bias} = \text{constant}$$

**Total Control**:
$$u_{total} = \text{PID} + \text{FF1} \cdot \dot{r} + \text{FF2} \cdot \ddot{r} + u_{bias}$$

**Example**: Vertical Z-axis with 100 lb spindle head
- Gravity force: 100 lb downward (always)
- Without bias: Integral term accumulates to compensate (slow, windup risk)
- With bias: Constant upward force = 100 lb (instantaneous compensation)

**Tuning**:
- Move axis to mid-position, hold
- Measure steady-state PID output
- Set bias = measured output
- Verify axis holds position with minimal integral accumulation

**LinuxCNC Configuration**:
```
setp pid.z.bias 2.5  # Units: velocity command (in/s typically)
```

## Input Shaping

### Concept

**Problem**: Step commands in position excite mechanical resonances (ringing).

**Solution**: Shape input command to avoid exciting resonances.

**Method**: Convolve step input with filter designed to cancel resonance.

**Zero-Vibration (ZV) Shaper**:
- Split step command into two smaller steps
- Timing and amplitude chosen to cancel resonance

**Example**:
- System with resonance at 50 Hz (period = 0.02 s)
- Instead of single step at $t=0$:
  - Apply 0.5 step at $t=0$
  - Apply 0.5 step at $t=0.01$ s (half period later)
- Second pulse arrives when first pulse oscillation is at peak → cancels

**Implementation**:
- Some CNC controllers have built-in input shaping
- LinuxCNC: External HAL component or trajectory planning
- Mach4: Plugin support (limited)

**Trade-off**: Slightly slower response (delay = half resonance period), but eliminates ringing.

**Application**: Lightweight gantries, long unsupported axes (3D printers, pick-and-place)

## Filtering Techniques

### Low-Pass Filters

**Purpose**: Attenuate high-frequency noise and commands.

**First-Order Low-Pass**:
$$H(s) = \frac{1}{\tau s + 1}$$

**Cutoff Frequency**: $f_c = \frac{1}{2\pi\tau}$

**Effect**:
- Frequencies below $f_c$: Pass through (minimal attenuation)
- Frequencies above $f_c$: Attenuated (-20 dB/decade)

**Application**:
- Filter derivative term (reduce noise amplification)
- Filter command input (smooth jerky commands)
- Filter encoder signal (reduce quantization noise)

**Example**:
- Encoder quantization: ±0.00005" jitter
- Without filter: Derivative term amplifies noise
- With 100 Hz low-pass on derivative: Noise attenuated, derivative still effective

**LinuxCNC**:
```
loadrt lowpass names=lowpass.d-term
setp lowpass.d-term.gain 1.0
setp lowpass.d-term.time-constant 0.002  # 2 ms = ~80 Hz cutoff
```

### Notch Filters

**Purpose**: Eliminate specific frequency (resonance) from control loop.

**Transfer Function**:
$$H(s) = \frac{s^2 + \omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

where:
- $\omega_n$ = notch center frequency (rad/s)
- $\zeta$ = damping ratio (notch width)

**Effect**:
- At $\omega_n$: Gain ≈ 0 (complete rejection)
- Away from $\omega_n$: Gain ≈ 1 (passes through)

**Frequency Response**:
- Narrow notch (high Q): $\zeta$ = 0.1 (rejects ±5 Hz around center)
- Wide notch (low Q): $\zeta$ = 0.5 (rejects ±20 Hz around center)

**Identification of Resonance Frequency**:

**Method 1: Tap Test**
- Tap axis with hammer (or similar)
- Measure ring-down with accelerometer or encoder
- FFT of response shows resonance peak

**Method 2: Frequency Sweep**
- Apply sinusoidal command at varying frequencies
- Measure response amplitude
- Peak in response = resonance frequency

**Method 3: Increase Gains Until Oscillation**
- Gradually increase P and D gains
- Note frequency of oscillation when system becomes unstable
- Resonance frequency ≈ oscillation frequency

**Example**:
- Tap test shows resonance at 247 Hz
- Design notch filter: $f_n = 247$ Hz, $\zeta = 0.15$ (narrow notch)
- Implement in control loop
- **Result**: Can increase PID gains 50-100% without exciting resonance

**LinuxCNC**:
```
# Notch filter for 247 Hz resonance
loadrt notch names=notch.x-axis
setp notch.x-axis.freq 247
setp notch.x-axis.q 6.67  # Q = 1/(2*zeta), zeta=0.075
```

**Application**:
- Flexible gantries (100-300 Hz typical)
- Long unsupported screws (50-150 Hz)
- Spindle mounted on Z-axis (200-500 Hz)

**Trade-off**: Notch filter adds phase lag (reduces phase margin slightly). Use narrowest notch possible.

### Bi-Quad Filter

**Bi-Quadratic Filter**: General second-order filter (can implement low-pass, high-pass, band-pass, notch).

**Transfer Function**:
$$H(s) = \frac{b_0 s^2 + b_1 s + b_2}{s^2 + a_1 s + a_2}$$

**Advantage**: Flexible, can implement multiple filter types with coefficient changes.

**CNC Use**: Less common than simple notch/low-pass (more complex to tune).

## Dual-Loop Control

### Position and Velocity Loops

**Cascaded Control**: Outer position loop commands inner velocity loop.

```
Position     Position    Velocity    Velocity    Current      Motor
Command  →   Loop    →   Command →   Loop    →   Command  →
             (CNC)                   (Drive)
              ↑                        ↑
         Position FB              Velocity FB
          (Encoder)               (Encoder derivative
                                   or tachometer)
```

**Division of Labor**:
- **Outer loop** (position): Slow (1-2 kHz), CNC controller
- **Inner loop** (velocity): Fast (8-16 kHz), servo drive

**Advantages**:
- Velocity loop bandwidth higher than position loop (faster disturbance rejection)
- Velocity loop stabilizes motor (prevents runaway)
- Easier to tune (tune inner loop first, then outer)

**Tuning**:
1. **Velocity loop** (drive): Manufacturer often pre-tunes
2. **Position loop** (CNC): User tunes P, I, D as usual

**Example**:
- Velocity loop bandwidth: 500 Hz (drive internal)
- Position loop bandwidth: 50 Hz (CNC controller)
- **10:1 separation** (rule of thumb: inner loop 5-10× faster than outer)

**Industrial Servo Drives**: Almost always implement velocity loop internally (user tunes position loop only).

## State-Space Control

### Overview

**State-Space Representation**: Modern control theory, models system as first-order differential equations.

**State Vector**: $x = [position, \, velocity, \, ...]^T$

**State Equations**:
$$\dot{x} = Ax + Bu$$
$$y = Cx + Du$$

where:
- $A$ = state matrix (system dynamics)
- $B$ = input matrix
- $C$ = output matrix
- $D$ = feedthrough matrix

**Example** (mass-spring-damper):
$$\ddot{y} + 2\zeta\omega_n\dot{y} + \omega_n^2 y = u$$

**State-space form** ($x_1 = y$, $x_2 = \dot{y}$):
$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -\omega_n^2 & -2\zeta\omega_n \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u$$

**Controller**: $u = -Kx$ (state feedback)

where $K = [K_1, \, K_2]$ = gain vector

**Equivalent to**:
- $K_1$ ≈ proportional gain (position error)
- $K_2$ ≈ derivative gain (velocity error)

### LQR (Linear Quadratic Regulator)

**Optimal Control**: Design $K$ to minimize cost function:

$$J = \int_0^\infty (x^T Q x + u^T R u) dt$$

**Tuning**: Adjust $Q$ (state weighting) and $R$ (control effort weighting)

**Solution**: Solve Algebraic Riccati Equation (ARE) for $K$.

**Advantages**:
- Provably optimal (for given Q, R)
- Systematic design
- Guaranteed stability

**CNC Application**: Research topic, not common in commercial controllers (LinuxCNC, Mach4 use PID).

**When Useful**:
- Multi-axis coordinated control (gantry synchronization)
- Complex system dynamics (flexible structures)
- Academic/research CNC projects

## Adaptive Control

### Concept

**Fixed Gains**: Traditional PID has constant $K_P$, $K_I$, $K_D$.

**Adaptive Gains**: Controller adjusts gains automatically based on operating conditions.

**Why Adaptive**:
- System dynamics change (load inertia varies, temperature affects friction)
- Fixed gains optimized for one condition may be suboptimal for others
- Adaptive control maintains performance across conditions

### Gain Scheduling

**Method**: Pre-compute gains for multiple operating points, interpolate.

**Example** (Lathe):
- Light workpiece (low inertia): $K_P = 200$
- Heavy workpiece (high inertia): $K_P = 100$
- Controller measures load inertia (from acceleration response)
- Automatically adjusts $K_P$ based on measurement

**Implementation**:
- Create lookup table: Inertia vs. Gains
- Measure or estimate inertia (online or offline)
- Interpolate gains from table

**Application**:
- Variable payload robots
- Machine tools with different workpiece masses
- Systems with configuration changes (e.g., gantry position affects dynamics)

### Model Reference Adaptive Control (MRAC)

**Concept**: Define reference model (desired behavior), adapt gains to match.

**Reference Model**: Ideal system (e.g., critically damped second-order)

**Adaptation Law**: Continuously adjust controller gains to minimize tracking error vs. reference model.

**Advantages**:
- Handles unknown plant parameters
- Robust to parameter changes

**Disadvantages**:
- Complex implementation
- Requires careful stability analysis
- Not common in CNC (research topic)

## Cross-Coupling Control

### Gantry Synchronization Problem

**Dual-Motor Gantry** (e.g., plasma table with two Y-axis motors):

**Problem**: Motors may not track perfectly, causing gantry to rack (skew).

**Traditional Approach**: Tune each motor independently.

**Limitation**: If one motor lags, gantry skews, causes binding and inaccuracy.

### Cross-Coupling Solution

**Add Cross-Coupling Term**: Each motor's controller receives feedback from both motors.

**Example**:
- Motor 1 position: $y_1$
- Motor 2 position: $y_2$
- **Cross-coupling error**: $e_{cc} = y_1 - y_2$

**Motor 1 command**:
$$u_1 = \text{PID}_1(r - y_1) - K_{cc} \cdot e_{cc}$$

**Motor 2 command**:
$$u_2 = \text{PID}_2(r - y_2) + K_{cc} \cdot e_{cc}$$

**Effect**:
- If Motor 1 leads: $e_{cc} > 0$ → reduce $u_1$, increase $u_2$ (synchronize)
- If Motor 2 leads: $e_{cc} < 0$ → increase $u_1$, reduce $u_2$

**Result**: Motors stay synchronized (gantry remains square).

**Tuning $K_{cc}$**:
- Start low ($K_{cc}$ = 10-20% of $K_P$)
- Increase until synchronization error < 0.001"
- Too high: Can cause instability (fighting between axes)

**LinuxCNC**: HAL component `gantrykins` or custom HAL logic.

**Application**:
- Dual-motor gantries (plasma, router, laser)
- Coordinated multi-axis (parallel robots)

## Backlash Compensation

### The Backlash Problem

**Backlash**: Play/clearance in mechanical transmission (nut-screw gap, gear lash).

**Effect**:
- Hysteresis in motion
- Lost motion during direction reversal
- Position error during bidirectional moves

**Example**:
- Ballscrew has 0.002" backlash
- Move +X, then -X
- Actual position lags by 0.002" during reversal

### Software Compensation

**Method**: Add backlash correction term when direction reverses.

**Algorithm**:
1. Detect direction change (velocity sign change)
2. Add offset = backlash amount
3. Gradually remove offset over short time/distance

**LinuxCNC**:
```
setp axis.x.backlash 0.002  # inches
```

Controller automatically compensates during direction reversals.

**Limitations**:
- Compensation perfect only for slow moves
- Fast reversals: Compensation incomplete (inertia, dynamics)
- Better solution: **Eliminate backlash mechanically** (anti-backlash nut, preload)

**When to Use**:
- Legacy machines with worn screws
- Temporary fix until mechanical repair
- Non-critical applications (not precision machining)

## Summary

Advanced control techniques extend PID performance:

**Feedforward** (FF1, FF2):
- Reduce following error 5-10×
- Essential for high-speed machining
- Easy to implement, huge benefit

**Notch Filters**:
- Eliminate specific resonances
- Allow higher gains (faster response)
- Requires resonance identification (tap test, sweep)

**Dual-Loop Control**:
- Fast inner loop (velocity), slow outer loop (position)
- Standard in industrial servo drives
- Easier tuning, better performance

**Adaptive/Cross-Coupling**:
- Handle varying dynamics
- Synchronize multi-motor axes
- More complex, specialized applications

**Practical Priority**:
1. **PID tuning** (foundation)
2. **Feedforward** (FF1, FF2) (biggest bang for buck)
3. **Notch filters** (if resonances present)
4. **Advanced techniques** (as needed for specific applications)

**Next Steps**:
- Apply advanced control to trajectory planning (Section 19.6)
- Design optimal motion profiles (Section 19.7)
- Implement in LinuxCNC/Mach4 (Sections 19.10-19.11)

---

**Next**: [19.6 Trajectory Planning Fundamentals](section-19.6-trajectory-planning.md)
