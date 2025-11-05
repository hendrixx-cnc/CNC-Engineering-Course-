# 19.4 PID Tuning Methods

## Overview of Tuning Methods

PID tuning can be accomplished through several approaches, each with advantages and trade-offs:

| Method | Complexity | Accuracy | Time Required | Equipment |
|--------|------------|----------|---------------|-----------|
| Manual | Low | Moderate | 30-60 min | Oscilloscope helpful |
| Ziegler-Nichols | Low | Moderate | 15-30 min | None special |
| Relay Auto-Tune | Medium | Good | 5-15 min | Software support |
| Software-Assisted | Medium | Excellent | 10-30 min | Control software |
| Model-Based | High | Excellent | Variable | System ID tools |

**This Section Covers**:
1. Manual tuning (already covered in 19.3)
2. Ziegler-Nichols method (classic, widely used)
3. Relay auto-tuning (automated)
4. Software-assisted tuning (LinuxCNC, Mach4)
5. Advanced model-based methods

## Ziegler-Nichols Tuning Method

### Background

Developed by John Ziegler and Nathaniel Nichols in 1942, this method provides a systematic procedure for finding PID gains based on system response characteristics.

**Two Variants**:
1. **Ultimate Gain Method** (closed-loop): Find gain at onset of oscillation
2. **Reaction Curve Method** (open-loop): Measure step response

**Advantages**:
- Simple, well-established
- No mathematical model required
- Works for wide variety of systems

**Disadvantages**:
- Aggressive tuning (often 25-50% overshoot)
- Requires bringing system to edge of instability (risky)
- May need refinement for CNC applications

### Ultimate Gain Method (Closed-Loop)

**Procedure**:

**Step 1: Set I and D to Zero**
- $K_I = 0$
- $K_D = 0$
- P-only control

**Step 2: Increase $K_P$ Until Sustained Oscillation**
- Start with low $K_P$ (e.g., 10)
- Gradually increase until system oscillates with constant amplitude
- Record **ultimate gain** $K_u$ and **oscillation period** $T_u$

**Example**:
- Increase $K_P$: 10, 20, 40, 60, 80, 100...
- At $K_P = 120$: Sustained oscillation appears
- Measure period: $T_u = 0.15$ seconds
- Ultimate gain: $K_u = 120$

**Step 3: Calculate PID Gains**

**Ziegler-Nichols Formulas**:

| Controller Type | $K_P$ | $K_I$ | $K_D$ |
|----------------|-------|-------|-------|
| P | $0.5 K_u$ | 0 | 0 |
| PI | $0.45 K_u$ | $1.2 K_P / T_u$ | 0 |
| PID | $0.6 K_u$ | $2 K_P / T_u$ | $K_P T_u / 8$ |

**Example Calculation** (PID):
- $K_u = 120$, $T_u = 0.15$ s
- $K_P = 0.6 \times 120 = 72$
- $K_I = 2 \times 72 / 0.15 = 960$
- $K_D = 72 \times 0.15 / 8 = 1.35$

**Step 4: Test and Refine**
- Apply calculated gains
- Test step response
- Typical result: 10-25% overshoot, fast response
- Reduce gains 20-30% if too aggressive for application

**Safety Note**: Bringing system to oscillation can be dangerous. Use:
- Low mass or inertia for initial testing
- Emergency stop readily accessible
- Mechanical stops or soft limits active
- Conservative gain increases (10-20% steps near $K_u$)

### Reaction Curve Method (Open-Loop)

**When to Use**: System unstable or unsafe to oscillate under closed-loop P control.

**Procedure**:

**Step 1: Open-Loop Step Response**
- Disable feedback (open loop)
- Apply small step input to actuator (motor)
- Record position vs. time

**Step 2: Identify Response Parameters**

Typical S-shaped response curve:

```
Position
   |         _____________  <-- Final Value L
   |       /
   |      /
   |     / <-- Inflection Point
   |    /
   | __/
   |________________________ Time
      ↑   ↑
      L   T
```

**Measure**:
- $L$ = Dead time (delay before response begins)
- $T$ = Time constant (time from inflection point to 63% of final value)
- $K$ = DC gain (final output / input step size)

**Alternative**: Tangent Method
- Draw tangent line at steepest point
- $L$ = intersection with time axis
- $T$ = time from $L$ to intersection with final value

**Step 3: Calculate Gains**

**Ziegler-Nichols Reaction Curve Formulas**:

| Controller | $K_P$ | $K_I$ | $K_D$ |
|------------|-------|-------|-------|
| P | $\frac{T}{L \cdot K}$ | 0 | 0 |
| PI | $0.9 \frac{T}{L \cdot K}$ | $\frac{K_P}{3.3 L}$ | 0 |
| PID | $1.2 \frac{T}{L \cdot K}$ | $\frac{K_P}{2L}$ | $0.5 K_P L$ |

**Example**:
- Step input: 1.0 (normalized)
- Dead time: $L = 0.02$ s
- Time constant: $T = 0.08$ s
- DC gain: $K = 0.8$

PID Gains:
- $K_P = 1.2 \times 0.08 / (0.02 \times 0.8) = 6.0$
- $K_I = 6.0 / (2 \times 0.02) = 150$
- $K_D = 0.5 \times 6.0 \times 0.02 = 0.06$

**Limitations**:
- Requires open-loop control (not always practical)
- Assumes first-order + dead-time model (may not fit well)
- Often too aggressive for CNC (needs detuning)

## Relay Auto-Tuning

### Principle

**Relay Feedback Test**: Replace controller with on-off relay, system naturally oscillates at critical frequency.

**Advantages**:
- Automated (no manual gain adjustment)
- Safer than Ziegler-Nichols ultimate gain method (limited relay output)
- Fast (5-15 minutes typical)
- Accurate identification of $K_u$ and $T_u$

**Process**:

```
        +     E          Relay        Motor    Y
Setpoint ──>○──> ±d ──────────> Plant ──────> Position
        -   ↑                            |
            └────────────────────────────┘
```

Relay outputs $+d$ if error positive, $-d$ if error negative.

**Result**: System oscillates with period $T_u$

**Ultimate Gain Calculation**:
$$K_u = \frac{4d}{\pi a}$$

where:
- $d$ = relay amplitude (magnitude of output)
- $a$ = oscillation amplitude (measured from position response)

**Example**:
- Relay output: ±1.0 (normalized)
- Measured oscillation amplitude: $a = 0.0075$ inches
- Period: $T_u = 0.12$ seconds

$$K_u = \frac{4 \times 1.0}{\pi \times 0.0075} = 170$$

**Apply Ziegler-Nichols formulas** with $K_u = 170$, $T_u = 0.12$ s.

### Implementation

**Algorithm**:
1. Move to mid-position (allow oscillation both directions)
2. Apply relay feedback
3. Wait for sustained oscillation (3-5 cycles)
4. Measure amplitude and period
5. Calculate $K_u$, $T_u$
6. Compute PID gains using formulas
7. Switch to PID control with calculated gains

**Refinements**:
- **Hysteresis**: Add deadband to relay (reduces chattering)
- **Pre-load**: Add bias to relay output (compensate friction)
- **Multiple relays**: Test at different amplitudes (check linearity)

**Software Support**:
- Some industrial servo drives have built-in auto-tune (relay or similar method)
- LinuxCNC: External scripts/HAL components
- Mach4: Plugin support

## Cohen-Coon Tuning Method

**Alternative to Ziegler-Nichols**: Better for processes with large dead time ($L/T$ ratio > 0.3).

**Based on**: Open-loop reaction curve (same as Z-N reaction curve method)

**Formulas** (PID):
$$K_P = \frac{T}{L \cdot K} \left(1.35 + \frac{0.25 L}{T}\right)$$

$$K_I = K_P \frac{30 + 3(L/T)}{9 + 20(L/T)} \frac{1}{L}$$

$$K_D = K_P \frac{4}{11 + 2(L/T)} L$$

**When to Use**: Systems with significant transport delay (e.g., temperature control, large pneumatic systems).

**CNC Context**: Rarely needed (CNC servo systems typically have small dead time).

## Lambda Tuning (IMC Method)

**Internal Model Control (IMC)** or **Lambda Tuning**: Tune based on desired closed-loop time constant.

**Philosophy**: Specify desired response speed, calculate gains to achieve it.

**Parameter**: $\lambda$ = desired closed-loop time constant (user-specified)

**For First-Order + Dead-Time Model**:
$$K_P = \frac{T}{K(\lambda + L)}$$

$$K_I = \frac{K_P}{T}$$

$$K_D = 0 \text{ (typically; or small value)}$$

**Choosing $\lambda$**:
- **Small $\lambda$**: Fast response, aggressive (may overshoot or oscillate)
- **Large $\lambda$**: Slow response, conservative (robust)
- **Rule of thumb**: $\lambda = L$ to $\lambda = 3L$

**Example**:
- Dead time: $L = 0.02$ s
- Time constant: $T = 0.08$ s
- DC gain: $K = 0.8$
- Choose: $\lambda = 0.03$ s (1.5 × dead time)

$$K_P = \frac{0.08}{0.8 \times (0.03 + 0.02)} = 2.0$$

$$K_I = \frac{2.0}{0.08} = 25$$

**Advantages**:
- Intuitive parameter ($\lambda$ = desired speed)
- Generally more conservative than Ziegler-Nichols
- Explicit robustness vs. performance trade-off

**Disadvantages**:
- Requires system model (T, L, K)
- May need iteration to find best $\lambda$

## Software-Assisted Tuning

### LinuxCNC Halscope Method

**LinuxCNC** provides excellent tools for servo tuning:

**Tools**:
- **Halscope**: Real-time oscilloscope for HAL signals
- **HAL**: Hardware Abstraction Layer (connects signals)
- **PID Component**: Built-in PID loop

**Procedure**:

**Step 1: Configure Halscope**
- Monitor signals:
  - Commanded position
  - Actual position (encoder feedback)
  - Following error
  - PID output (motor command)
- Trigger on position command change

**Step 2: Set Initial Gains**
- Use conservative values:
  - P = 50-100
  - I = 0
  - D = 0
  - FF1 (velocity feedforward) = 0

**Step 3: Tune Proportional Gain**
- Command small jog (0.1-0.5 inches)
- Observe following error in Halscope
- Increase P until response is fast with slight overshoot (5-10%)

**Step 4: Add Velocity Feedforward (FF1)**
- Set FF1 = 0.9-1.0 (start)
- Jog at constant velocity
- Observe following error during constant-velocity portion
- Adjust FF1 until following error near zero during motion
- **Goal**: Following error < 0.001" during 200 IPM rapid

**Step 5: Add Derivative**
- Add D = P/10 (start)
- Increase D until overshoot reduced to <5%
- Watch for noise amplification (jittery motion)

**Step 6: Add Integral**
- Add I = P/20 (start)
- Increase until steady-state error eliminated
- Check for overshoot increase

**Step 7: Iterate**
- Now that D and I are active, can increase P further (faster response)
- Iterate between P, I, D adjustments
- Test at various speeds and loads

**Example LinuxCNC HAL Configuration**:
```
# PID gains for X-axis
setp pid.x.Pgain 100
setp pid.x.Igain 10
setp pid.x.Dgain 8
setp pid.x.FF1 0.95
setp pid.x.deadband 0.0001
setp pid.x.maxoutput 10.0
```

### Mach4 Tuning

**Mach4 Motor Tuning**:

**Tools**:
- Built-in motor tuning wizard
- Jogging controls
- Position display

**Procedure**:

**Step 1: Motor Configuration**
- Open Motor Configuration for axis
- Set steps per unit (encoder resolution)
- Set maximum velocity, acceleration

**Step 2: Initial Gains**
- P Gain (Proportional): 100-200
- I Gain (Integral): 0-10
- D Gain (Derivative): 0

**Step 3: P Gain Tuning**
- Jog axis back and forth
- Increase P until motion is responsive
- If oscillates, reduce P by 25-30%

**Step 4: I Gain Tuning**
- Add small I gain (5-20)
- Check for hunting (slow oscillation)
- Reduce if unstable

**Step 5: D Gain Tuning**
- Add D gain (10-50)
- Improves damping
- Watch for noise amplification

**Step 6: Velocity Feedforward**
- Some drives support FF (check documentation)
- Set FF = 0.9-1.0
- Reduces following error during motion

**Step 7: Test**
- Run test programs (circles, squares, rapids)
- Check following error display
- Verify smooth motion at all speeds

### Commercial Servo Drive Auto-Tune

**Many Industrial Drives Include Auto-Tune**:

**Examples**:
- **Yaskawa Sigma-7**: Automatic gain tuning function
- **Delta ASDA-A2**: Auto-tuning via drive parameters
- **Panasonic MINAS A6**: One-touch tuning
- **Kollmorgen AKD**: Auto-tune via software

**Typical Auto-Tune Process**:
1. Set motor parameters (inertia, rated specs)
2. Set load inertia ratio (or auto-detect)
3. Select stiffness level (1-100 or similar)
4. Run auto-tune routine
5. Drive performs identification (step, frequency sweep, or relay)
6. Drive calculates and sets gains automatically

**User Input**:
- **Stiffness/Response Level**: 1 = soft (slow), 100 = stiff (fast)
- **Inertia Ratio**: Load inertia / Motor inertia
  - Low inertia ratio (1-5): Higher gains possible
  - High inertia ratio (10-30): Lower gains required (stability)

**Example** (Yaskawa):
- Parameter Pn102: Auto-tuning mode
  - 0 = Manual tuning
  - 1 = Auto-tuning (low response)
  - 2 = Auto-tuning (standard)
  - 3 = Auto-tuning (high response)
- Execute: Set Pn102 = 2, cycle power or issue tune command
- Drive runs auto-tune (30-60 seconds)
- Gains automatically updated

**Advantages**:
- Fast, automated
- Pre-configured for motor model
- Accounts for drive bandwidth, current loop tuning

**Disadvantages**:
- Requires drive support (not all drives have auto-tune)
- May not account for mechanical resonances
- "Black box" (can't see tuning logic)

## Model-Based Tuning

### System Identification

**Goal**: Create mathematical model of plant from measured data.

**Process**:
1. Apply known input signal (step, sine sweep, random)
2. Measure output response
3. Fit transfer function model to data
4. Design controller based on model

**Tools**:
- MATLAB System Identification Toolbox
- Python `scipy.signal` + optimization
- Octave (open-source MATLAB alternative)

**Example** (Step Response):
- Apply 1.0V step to motor
- Record position vs. time
- Fit second-order model: $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$
- Optimize $\omega_n$, $\zeta$ to minimize fit error

**Result**: $\omega_n = 50$ rad/s, $\zeta = 0.2$

**Controller Design**:
- Specify desired closed-loop poles (e.g., $\zeta = 0.7$, $\omega_n = 40$ rad/s)
- Calculate PID gains to achieve desired poles
- Verify via simulation before implementing

### Frequency Response Identification

**Sine Sweep Method**:
- Apply sinusoidal input at varying frequencies (1-100 Hz typical)
- Measure amplitude ratio and phase shift at each frequency
- Plot Bode diagram from measured data
- Fit transfer function model

**Example**:
- Sweep 0.1-100 Hz (logarithmic spacing, 20 points)
- At each frequency, measure gain and phase
- Result: Bode plot of actual system
- Identify resonances, bandwidth, phase lag

**Controller Design**:
- Use loop-shaping techniques
- Design controller to achieve target phase margin (45-60°)
- Maximize bandwidth without exciting resonances

**Advanced**: Use optimization to find PID gains that maximize closed-loop bandwidth subject to phase margin constraint.

### Optimal Control (LQR)

**Linear Quadratic Regulator (LQR)**: State-space optimal control method.

**State-Space Model**:
$$\dot{x} = Ax + Bu$$
$$y = Cx$$

**Cost Function** (to minimize):
$$J = \int_0^\infty (x^T Q x + u^T R u) dt$$

where:
- $Q$ = state weighting matrix (penalize position, velocity error)
- $R$ = control weighting matrix (penalize large control effort)

**LQR Solution**:
$$u = -Kx$$

where $K$ = optimal gain matrix (computed via Riccati equation)

**Tuning**: Adjust $Q$ and $R$ matrices to balance performance vs. control effort.

**Advantages**:
- Provably optimal (for given Q, R)
- Handles multi-input, multi-output naturally
- Guaranteed stability

**Disadvantages**:
- Requires accurate state-space model
- Requires state estimation (Kalman filter if not all states measured)
- Not standard in CNC controllers (research/advanced topic)

**CNC Application**: Mainly in research, advanced industrial systems, robotics.

## Tuning for Specific Applications

### High-Speed Machining

**Goals**:
- Maximum acceleration
- Minimal following error
- Smooth contouring

**Tuning Strategy**:
- Higher P gain (fast response)
- Moderate D gain (damping without noise)
- High velocity feedforward (FF1 ≈ 0.98-1.0)
- Acceleration feedforward (FF2) if supported
- Aggressive trajectory planning (Section 19.7)

**Trade-offs**:
- May sacrifice stability margin for speed
- More sensitive to mechanical resonances
- Requires excellent mechanical construction

### Precision Positioning

**Goals**:
- Sub-micron accuracy
- No overshoot
- Minimal steady-state error

**Tuning Strategy**:
- Moderate P gain (avoid overshoot)
- High D gain (critical damping, $\zeta \approx 1.0$)
- Moderate I gain (eliminate error without oscillation)
- Lower velocity/acceleration limits
- Use linear scales if possible (eliminate screw errors)

**Trade-offs**:
- Slower than high-speed tuning
- Longer settling times acceptable

### Heavy Cutting (High Load Variation)

**Goals**:
- Stable under varying loads
- Compensate for cutting forces
- Avoid chatter

**Tuning Strategy**:
- Moderate P gain (avoid exciting chatter)
- Higher I gain (compensate for load disturbances)
- Moderate D gain
- Velocity feedforward helps maintain speed under load
- Consider notch filters for chatter frequencies

**Trade-offs**:
- Less aggressive than high-speed tuning
- Stability prioritized over raw speed

## Troubleshooting Tuning Problems

### Problem: Cannot Achieve Stable Tuning

**Symptoms**: Oscillation at any reasonable gain values

**Possible Causes**:
1. **Mechanical resonance**: Flexible structure, poor coupling
2. **Encoder mounting**: Vibration, loose mounting
3. **Wrong direction**: Positive feedback instead of negative
4. **Electrical noise**: Encoder signal corruption
5. **Insufficient loop rate**: Controller too slow (<500 Hz)

**Solutions**:
- Tap test: Identify resonances (hammer tap, measure ring-down)
- Add mechanical stiffness (bracing, better couplings)
- Check encoder direction vs. motor direction (must match!)
- Shielded encoder cables, proper grounding
- Increase control loop rate if possible

### Problem: Excessive Following Error

**Symptoms**: Position lags command by 0.005-0.050" during motion

**Possible Causes**:
1. $K_P$ too low
2. No velocity feedforward
3. Excessive friction
4. Motor undersized

**Solutions**:
- Increase P gain (if stable)
- Add velocity feedforward (FF1 = 0.9-1.0)
- Lubricate ways, check for binding
- Verify motor torque adequate for acceleration required

### Problem: Steady-State Error Persists

**Symptoms**: 0.001-0.005" error after motion stops

**Possible Causes**:
1. $K_I$ too low or zero
2. Deadband too large
3. Stiction (static friction) exceeds motor torque

**Solutions**:
- Increase integral gain
- Reduce deadband (0.00005-0.0001" typical)
- Reduce friction, add bias term for gravity compensation

### Problem: Noisy/Jittery Motion

**Symptoms**: High-frequency vibration, audible whine

**Possible Causes**:
1. $K_D$ too high
2. No derivative filtering
3. Encoder resolution too coarse
4. Electrical noise on encoder

**Solutions**:
- Reduce derivative gain 30-50%
- Add or increase derivative filter time constant
- Upgrade encoder (higher resolution)
- Check cabling, grounding, shielding

## Summary

Multiple PID tuning methods available, each suited to different situations:

**Ziegler-Nichols**: Classic, simple, but aggressive (requires refinement)

**Relay Auto-Tune**: Automated, safe, fast (needs software support)

**Software-Assisted**: Best for CNC (LinuxCNC Halscope, Mach4 tools)

**Model-Based**: Most accurate, requires system identification

**General Recommendations**:
1. Start conservative (low gains)
2. Tune P first, then D, then I
3. Add feedforward for following error reduction
4. Test under realistic conditions
5. Document final values

**Next Steps**:
- Implement advanced control techniques (Section 19.5)
- Design optimal trajectories (Sections 19.6-19.9)
- Configure LinuxCNC or Mach4 (Sections 19.10-19.11)

---

**Next**: [19.5 Advanced Control Techniques](section-19.5-advanced-control.md)
