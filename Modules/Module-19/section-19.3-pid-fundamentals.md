# 19.3 PID Control Fundamentals

## PID Overview

**Proportional-Integral-Derivative (PID)** control is the most widely used feedback control algorithm in industrial applications, including CNC servo systems.

**Why PID Dominates**:
- Simple to understand conceptually
- Only three parameters to tune
- Effective for most single-input, single-output systems
- Decades of industrial experience and tuning methods
- Implemented in virtually all servo drives and CNC controllers

## The Error Signal

### Position Error Definition

$$e(t) = r(t) - y(t)$$

where:
- $e(t)$ = error at time $t$
- $r(t)$ = reference (commanded position)
- $y(t)$ = measured position (actual)

**Example**:
- Commanded position: 5.0000"
- Actual position: 4.9985"
- Error: 5.0000 - 4.9985 = +0.0015" (positive = lagging)

**Sign Convention**:
- **Positive error**: Actual position lags command (need to speed up)
- **Negative error**: Actual position leads command (need to slow down)

### Continuous vs Discrete Time

**Continuous-Time PID** (theoretical):
$$u(t) = K_P e(t) + K_I \int_0^t e(\tau) d\tau + K_D \frac{de(t)}{dt}$$

**Discrete-Time PID** (actual implementation in digital controller):
$$u[k] = K_P e[k] + K_I \sum_{i=0}^{k} e[i] \Delta t + K_D \frac{e[k] - e[k-1]}{\Delta t}$$

where:
- $k$ = sample index (k, k-1, k-2, ...)
- $\Delta t$ = sample period (e.g., 0.001 s for 1 kHz loop)

**Example**:
1 kHz position loop: $\Delta t$ = 0.001 s
- Sample 0: $t$ = 0.000 s
- Sample 1: $t$ = 0.001 s
- Sample 2: $t$ = 0.002 s
- ...

## Proportional (P) Term

### Theory

**Formula**: 
$$u_P(t) = K_P \cdot e(t)$$

**Physical Meaning**: Spring connecting actual position to commanded position
- Larger error → larger restoring force
- Spring stiffness = $K_P$

**Effect on System**:
- Higher $K_P$ → stiffer position control
- Higher $K_P$ → faster response
- Higher $K_P$ → less steady-state error (but never zero with P alone)

### Steady-State Error with P-Only Control

**Problem**: Proportional control alone cannot eliminate steady-state error.

**Why**: At steady-state, error must be non-zero to produce motor command.

**Example**:
- P-only controller: $K_P$ = 100 (units: command per inch of error)
- Motor requires 50 units to overcome friction and hold position
- At steady-state: $50 = 100 \times e_{ss}$
- Therefore: $e_{ss}$ = 0.50 / 100 = 0.005" (persistent error)

**Doubling $K_P$ to 200**:
- $e_{ss}$ = 50 / 200 = 0.0025" (half the error)

**Key Insight**: Higher $K_P$ reduces but doesn't eliminate steady-state error.

### Proportional Gain Units

**Typical Units**:
- **Command per distance**: volts per inch, % per mm
- **Dimensionless** (if command and error in same units)
- **In some systems**: Force per distance (N/mm) - acts like spring constant

**LinuxCNC Example**:
- $K_P$ = 100 (units: per second)
- With 1 kHz position loop
- Effective gain = 100 / 1000 = 0.1 (10% correction per ms per inch error)

**Example Calculation**:
- Error: 0.010"
- $K_P$ = 100
- Proportional output: 100 × 0.010 = 1.0 (velocity command, inches/second)

Controller commands 1.0 in/s velocity to reduce error.

### Practical Proportional Tuning

**Start Low**:
- Begin with $K_P$ = 10-20
- Verify stable (no oscillation)

**Increase Gradually**:
- Increase by 20-50% each iteration
- Test step response after each increase
- Look for overshoot or oscillation

**Optimal $K_P$**:
- Just below onset of sustained oscillation
- Typically results in 5-15% overshoot
- Will be refined with derivative term

**Example Progression**:
| $K_P$ | Overshoot | Settling Time | Notes |
|-------|-----------|---------------|-------|
| 10 | 0% | 500 ms | Too slow, overdamped |
| 25 | 2% | 200 ms | Better, still slow |
| 50 | 8% | 100 ms | Good response |
| 100 | 25% | 80 ms | Too much overshoot |
| 75 | 12% | 90 ms | **Target: Will add D term** |

## Derivative (D) Term

### Theory

**Formula**:
$$u_D(t) = K_D \cdot \frac{de(t)}{dt}$$

**Physical Meaning**: Damper (shock absorber) 
- Opposes rapid changes in error
- Provides "braking" action as position approaches target

**Effect on System**:
- Reduces overshoot (adds damping)
- Improves stability
- Allows higher $K_P$ without oscillation
- Faster settling time

### Discrete Implementation

**Simple Derivative**:
$$\frac{de[k]}{dt} \approx \frac{e[k] - e[k-1]}{\Delta t}$$

**Problem**: Amplifies high-frequency noise

**Example of Noise Amplification**:
- True error: 0.001"
- Encoder noise: ±0.00005" (typical)
- Measured error jumps: 0.00095" → 0.00105" (due to noise)
- Derivative: (0.00105 - 0.00095) / 0.001 = 0.10 in/s (huge!)
- With $K_D$ = 50: Output = 50 × 0.10 = 5.0 (inappropriate response to noise)

**Solution**: Filter derivative term or use derivative-on-measurement.

### Derivative-on-Measurement (Recommended)

Instead of differentiating error, differentiate measurement:

$$u_D(t) = -K_D \cdot \frac{dy(t)}{dt}$$

**Advantage**: Step changes in setpoint don't cause derivative kick

**Example**:
- Command steps from 0" to 1.000" instantly
- Error derivative: (1.000 - 0) / Δt = huge spike!
- Measurement derivative: smooth change as axis accelerates (no spike)

**Most Modern Controllers**: Use derivative-on-measurement by default.

### Derivative Filtering

**Low-Pass Filter on Derivative**:
$$D_{filtered}(s) = \frac{K_D s}{1 + \tau_D s}$$

where $\tau_D$ = derivative filter time constant (typically $\Delta t$ to 10$\Delta t$)

**Effect**: 
- Reduces noise amplification
- Slightly delays derivative action
- More stable in presence of measurement noise

**Practical Implementation**: First-order digital filter

$$D_{filtered}[k] = \alpha D[k] + (1-\alpha) D_{filtered}[k-1]$$

where $\alpha = \frac{\Delta t}{\Delta t + \tau_D}$ (typical $\alpha$ = 0.1-0.3)

### Derivative Gain Tuning

**Start with Zero**:
- Tune P term first
- Note overshoot and settling time

**Add Derivative Gradually**:
- Start with $K_D$ = $K_P$ / 10
- Increase until overshoot <5-10%
- Typical ratio: $K_D$ = (0.05-0.20) × $K_P$

**Example**:
- $K_P$ = 75, overshoot = 12%
- Add $K_D$ = 5: overshoot = 8%
- Add $K_D$ = 10: overshoot = 4%
- Add $K_D$ = 15: overshoot = 2% (critically damped)
- **Select** $K_D$ = 10-12 for slight underdamping

**Watch for Noise**:
- If system becomes "nervous" (jittery), reduce $K_D$
- Add more filtering if needed

## Integral (I) Term

### Theory

**Formula**:
$$u_I(t) = K_I \int_0^t e(\tau) d\tau$$

**Physical Meaning**: Memory of past errors
- Accumulates error over time
- Generates command proportional to total accumulated error

**Effect on System**:
- Eliminates steady-state error
- Compensates for constant disturbances (friction, gravity, drag)
- Can cause overshoot and oscillation if too high
- Slows response if too high

### Why Integral is Necessary

**Constant Disturbance Example**:
- Vertical axis with gravity load: 50 lb constant force
- P and D terms only: Axis sags until PD command = 50 lb
- Steady-state error remains (position below target)

**With Integral Term**:
- Error accumulates over time
- Integral term ramps up
- Eventually produces 50 lb command to balance gravity
- Position error goes to zero

### Discrete Implementation

**Rectangular Integration**:
$$I[k] = I[k-1] + e[k] \cdot \Delta t$$

**Trapezoidal Integration** (more accurate):
$$I[k] = I[k-1] + \frac{e[k] + e[k-1]}{2} \cdot \Delta t$$

**Example**:
- $\Delta t$ = 0.001 s
- Error sequence: 0.010", 0.008", 0.006", 0.004", 0.002"
- Integral: 0, 0.010×0.001, 0.010×0.001+0.008×0.001, ...
- After 5 samples: $I$ = 0.000030 in·s

With $K_I$ = 1000:
$$u_I = 1000 \times 0.000030 = 0.030$$

### Integral Windup

**Problem**: Integral term accumulates to very large values during:
- Startup (axis far from target)
- Saturated motor (commanded torque exceeds motor capability)
- Mechanical limit encountered

**Result**: 
- Huge integral term persists after error eliminated
- Causes large overshoot
- Slow recovery (must "unwind" integral term)

**Example**:
- Commanded move: 0" → 10"
- During move: large error accumulates (integral = 10 in·s)
- Arrive at target: error = 0, but integral term remains
- Integral term pushes past target (overshoot)
- Takes time for negative error to cancel accumulated integral

### Anti-Windup Techniques

**Method 1: Integral Clamping**
Limit maximum integral value:
```
if (integral > MAX_INTEGRAL) integral = MAX_INTEGRAL;
if (integral < MIN_INTEGRAL) integral = MIN_INTEGRAL;
```

**Method 2: Conditional Integration**
Only integrate when error small (near target):
```
if (abs(error) < 0.010) {
    integral += error * dt;
}
```

**Method 3: Back-Calculation Anti-Windup**
When output saturates, reduce integral:
```
if (output > MAX_OUTPUT) {
    integral -= (output - MAX_OUTPUT) / Ki;
    output = MAX_OUTPUT;
}
```

**Method 4: Output Saturation Feedback** (most common in servo drives)
Stop integrating when output saturates.

### Integral Gain Tuning

**Start with Zero**:
- Tune P and D terms first
- System should be stable but with steady-state error

**Add Small Integral**:
- Start with $K_I$ = $K_P$ / 10
- Typical starting value: $K_I$ = 5-20

**Increase Slowly**:
- Increase by 20-50% each iteration
- Watch for oscillation or excessive overshoot
- Stop when steady-state error eliminated

**Optimal $K_I$**:
- Just high enough to eliminate steady-state error
- Not so high that it causes overshoot or slow settling
- Typical: $K_I$ = (0.1-0.3) × $K_P$

**Example**:
- $K_P$ = 75, $K_D$ = 10
- With P-D only: steady-state error = 0.0005"
- Add $K_I$ = 5: error = 0.0002" after 1 second
- Add $K_I$ = 10: error = 0.00005" after 0.5 seconds
- Add $K_I$ = 20: overshoot increases, oscillation
- **Select** $K_I$ = 10-15

## Complete PID Formula

### Continuous Time

$$u(t) = K_P e(t) + K_I \int_0^t e(\tau)d\tau + K_D \frac{de(t)}{dt}$$

### Discrete Time (Position Form)

$$u[k] = K_P e[k] + K_I \sum_{i=0}^k e[i]\Delta t + K_D \frac{e[k]-e[k-1]}{\Delta t}$$

### Discrete Time (Velocity Form)

More numerically stable for embedded systems:

$$\Delta u[k] = K_P (e[k] - e[k-1]) + K_I e[k] \Delta t + K_D (e[k] - 2e[k-1] + e[k-2])$$

$$u[k] = u[k-1] + \Delta u[k]$$

**Advantage**: Avoids summing large arrays (integral computed incrementally)

### Practical Digital PID (LinuxCNC Style)

**Bias Term**: Some systems add output bias for friction compensation:

$$u[k] = K_P e[k] + K_I I[k] + K_D \frac{dy[k]}{dt} + u_{bias}$$

**Deadband**: Ignore very small errors (avoid dither):

```
if (abs(error) < DEADBAND) error = 0;
```

Typical deadband: 0.00005-0.0001" (1-2 encoder counts)

### Units and Scaling

**Consistent Units Critical**:
- Position: inches (or mm)
- Velocity: inches/second (or mm/s)
- Time: seconds

**Example Unit Analysis**:
- $e$ = inches
- $K_P$ = (in/s) / in = s⁻¹
- $K_I$ = (in/s) / (in·s) = s⁻²
- $K_D$ = (in/s) / (in/s) = dimensionless

**LinuxCNC Scaling**:
- Internal position units: "machine units" (counts, inches, mm - configurable)
- Gains scaled by position loop period
- Effective P gain = $K_P$ / (loop frequency)

## PID Tuning Effects Summary

### Increasing Proportional Gain ($K_P$)

**Effects**:
- ✓ Faster rise time
- ✓ Smaller steady-state error (but not zero)
- ✗ Increased overshoot
- ✗ Potential instability (oscillation)

**Use When**: Response too slow, large steady-state error

### Increasing Integral Gain ($K_I$)

**Effects**:
- ✓ Eliminates steady-state error
- ✓ Compensates for constant disturbances
- ✗ Increased overshoot
- ✗ Slower settling time if too high
- ✗ Potential instability

**Use When**: Persistent steady-state error, gravity/friction compensation needed

### Increasing Derivative Gain ($K_D$)

**Effects**:
- ✓ Reduced overshoot (more damping)
- ✓ Improved stability (allows higher $K_P$)
- ✓ Faster settling time
- ✗ Amplifies noise (if too high or unfiltered)
- ✗ Can cause "nervous" behavior

**Use When**: Excessive overshoot, oscillatory response

## Complete PID Tuning Procedure (Manual Method)

### Step 1: Prepare System

**Mechanical**:
- All axes moving freely (no binding)
- Couplings tight, no backlash
- Encoders properly mounted and aligned
- Wipers, guards removed (or loose)

**Electrical**:
- Motor properly phased (for BLDC/AC servo)
- Encoder direction matches motor direction
- Drive enabled and responding
- Emergency stop functional

**Software**:
- Position loop running at 1-2 kHz
- Soft limits disabled (for initial testing)
- Following error limit set high (0.050-0.100")
- Encoder scale factor correct (test: jog 1", measure actual distance)

### Step 2: Set All Gains to Zero

Start with clean slate:
- $K_P$ = 0
- $K_I$ = 0
- $K_D$ = 0

**Verify**: Motor should not respond to position commands (no feedback).

### Step 3: Tune Proportional Gain

**3a. Initial P Gain**:
- Set $K_P$ = 10-20 (conservative)
- Command small move (0.100-0.500")
- Observe response (use Halscope, oscilloscope, or encoder readout)

**3b. Increase P Gain**:
- If stable (no oscillation), increase by 50%
- Repeat until one of:
  - Sustained oscillation appears → reduce 30% and stop
  - Overshoot >20% → note value, continue to Step 4
  - Following error acceptable for application → note value, continue

**3c. Record P-Only Response**:
- Overshoot: ____%
- Settling time: ____ ms
- Steady-state error: ____ inches

**Target**: $K_P$ value with 10-20% overshoot or just below oscillation onset.

**Example**: 
- $K_P$ = 100 → 25% overshoot, ringing
- $K_P$ = 75 → 12% overshoot, damps quickly
- **Select** $K_P$ = 75 for derivative tuning

### Step 4: Tune Derivative Gain

**4a. Initial D Gain**:
- Set $K_D$ = $K_P$ / 10 (start)
- Command same test move
- Observe overshoot reduction

**4b. Increase D Gain**:
- If overshoot still excessive, increase $K_D$ by 25-50%
- Repeat until overshoot <5-10%
- Watch for "nervous" behavior (noise amplification)

**4c. Optimal D Gain**:
- Overshoot: 2-8% (slight underdamping)
- Smooth, well-damped response
- No high-frequency jitter

**Example**:
- $K_P$ = 75, $K_D$ = 0 → 12% overshoot
- $K_P$ = 75, $K_D$ = 5 → 8% overshoot
- $K_P$ = 75, $K_D$ = 10 → 3% overshoot
- $K_P$ = 75, $K_D$ = 15 → 1% overshoot, getting jittery
- **Select** $K_P$ = 75, $K_D$ = 10

**Note**: Can now increase $K_P$ further for faster response (derivative adds damping).

**4d. Retune P with D**:
- With $K_D$ = 10, try $K_P$ = 100
- If stable with <10% overshoot, even faster response achieved!

### Step 5: Tune Integral Gain

**5a. Verify Steady-State Error Exists**:
- Command move to position, hold
- Wait 2-5 seconds
- Measure final position error
- Typical: 0.0002-0.002" error with P-D only

**5b. Initial I Gain**:
- Set $K_I$ = $K_P$ / 20 (very conservative)
- Command move, observe
- Error should approach zero over several seconds

**5c. Increase I Gain**:
- If error elimination too slow, increase $K_I$ by 50%
- If overshoot increases excessively, reduce $K_I$
- Target: Error <0.0001" within 0.5-2 seconds

**5d. Check for Overshoot**:
- Integral can cause overshoot on rapid moves
- If overshoot becomes problematic, reduce $K_I$ 
- Balance: Fast error correction vs. acceptable overshoot

**Example**:
- $K_P$ = 100, $K_D$ = 10, $K_I$ = 0 → steady-state error = 0.0005"
- Add $K_I$ = 5 → error = 0.0001" after 2 seconds, no extra overshoot
- Add $K_I$ = 10 → error = 0.00003" after 1 second, 5% overshoot
- Add $K_I$ = 20 → error = 0 after 0.5 seconds, 10% overshoot, ringing
- **Select** $K_I$ = 8-10

### Step 6: Verify Performance

**Test Moves**:
- Small moves (0.100")
- Medium moves (1.000")
- Large moves (full axis travel)
- Rapid reversals (0.500" back and forth)

**Check**:
- No oscillation at any position
- Following error <0.001-0.002" during motion
- Settling time acceptable
- No "nervous" behavior

**Load Testing**:
- Add workpiece weight (if applicable)
- Cutting forces (make test cuts)
- Verify stability under load

### Step 7: Fine-Tuning and Optimization

**Increase All Gains Proportionally**:
- If system very stable, can increase all gains 10-20%
- Faster response while maintaining stability

**Adjust for Different Operations**:
- Some systems use different gains for rapid vs. cutting
- Higher gains for rapids (speed priority)
- Lower gains for cutting (stability priority)

**Document Final Values**:
| Gain | Value | Units | Notes |
|------|-------|-------|-------|
| $K_P$ | 100 | s⁻¹ | Proportional |
| $K_I$ | 10 | s⁻² | Integral |
| $K_D$ | 10 | 1 | Derivative |
| Deadband | 0.0001 | in | Error threshold |
| FF1 | 0.95 | 1 | Velocity feedforward (Section 19.5) |
| Bias | 0.02 | in/s | Friction compensation |

## PID Variants and Modifications

### PI-D Control (Derivative on Measurement)

Instead of:
$$u = K_P e + K_I \int e \, dt + K_D \frac{de}{dt}$$

Use:
$$u = K_P e + K_I \int e \, dt - K_D \frac{dy}{dt}$$

**Advantage**: Eliminates derivative kick on setpoint changes.

### I-PD Control (Proportional on Measurement)

$$u = K_I \int e \, dt + K_P (r - y) - K_D \frac{dy}{dt}$$

Some systems implement as:
$$u = K_I \int e \, dt - K_P y - K_D \frac{dy}{dt} + K_P r$$

**Advantage**: Further reduces setpoint change response (very smooth).

### Parallel vs Series PID

**Parallel** (standard, described above):
$$u = K_P e + K_I \int e \, dt + K_D \frac{de}{dt}$$

**Series** (interacting):
$$u = K_c \left[ e + \frac{1}{T_i} \int e \, dt + T_d \frac{de}{dt} \right]$$

where $K_c$ = controller gain, $T_i$ = integral time, $T_d$ = derivative time

**Conversion**:
- $K_P = K_c$
- $K_I = K_c / T_i$
- $K_D = K_c \cdot T_d$

**Note**: Most CNC systems use parallel form.

### Setpoint Weighting

Some controllers allow weighting setpoint vs. measurement in P and D terms:

$$u = K_P (b \cdot r - y) + K_I \int e \, dt + K_D (c \cdot \frac{dr}{dt} - \frac{dy}{dt})$$

where $b$, $c$ = weighting factors (0-1)

**Effect**: Reduces response magnitude to setpoint changes (smoother).

Typical: $b$ = 0.5, $c$ = 0 (no derivative on setpoint)

## Common PID Tuning Problems

### Problem 1: Oscillation (Instability)

**Symptom**: Sustained or growing oscillation around setpoint

**Causes**:
- $K_P$ too high
- $K_D$ too low (insufficient damping)
- $K_I$ too high (destabilizes)

**Solution**:
- Reduce $K_P$ by 30-50%
- Increase $K_D$ by 50-100%
- Reduce $K_I$ to zero, retune

### Problem 2: Sluggish Response

**Symptom**: Slow rise time, long settling time

**Causes**:
- $K_P$ too low
- $K_D$ too high (overdamped)
- Mechanical issues (binding, friction)

**Solution**:
- Increase $K_P$ by 50-100%
- Reduce $K_D$ by 30-50%
- Check mechanical freedom

### Problem 3: Persistent Steady-State Error

**Symptom**: Error remains after motion stops

**Causes**:
- $K_I$ too low or zero
- Deadband too large
- Friction or load exceeds motor torque

**Solution**:
- Increase $K_I$
- Check deadband setting
- Verify motor capability

### Problem 4: Excessive Overshoot

**Symptom**: Axis overshoots target significantly

**Causes**:
- $K_P$ too high
- $K_I$ too high (windup)
- $K_D$ too low

**Solution**:
- Reduce $K_P$ slightly
- Reduce $K_I$ (or add anti-windup)
- Increase $K_D$

### Problem 5: Noise Amplification ("Nervous" Axis)

**Symptom**: High-frequency jitter, audible whine from motor

**Causes**:
- $K_D$ too high
- Encoder noise or resolution too coarse
- No derivative filtering

**Solution**:
- Reduce $K_D$ by 30-50%
- Add low-pass filter to derivative
- Check encoder mounting (vibration)

### Problem 6: Following Error During Motion

**Symptom**: Position lags command during constant velocity

**Causes**:
- $K_P$ too low
- No velocity feedforward (Section 19.5)
- Friction higher than expected

**Solution**:
- Increase $K_P$
- Add velocity feedforward (FF1)
- Lubricate ways/screws

## PID in CNC Context

### Position Loop Only (Basic)

**CNC Controller** generates position commands at 1-2 kHz
- PID loop calculates velocity command
- Servo drive executes velocity (or torque) command

**Common in**: Hobby CNC, LinuxCNC, Mach4

### Cascaded Loops (Advanced)

**Outer Loop** (position): CNC controller, 1-2 kHz
**Inner Loop** (velocity or current): Servo drive, 8-16 kHz

**Tuning**:
1. Tune inner loop first (drive manufacturer pre-tunes)
2. Tune outer loop (user-accessible)

**Common in**: Industrial servo drives (Yaskawa, Delta, Panasonic)

### Following Error Limit

**Critical Safety Feature**: Alarm if position error exceeds threshold

**Typical Settings**:
- Warning: 0.010-0.020" (alert, no stop)
- Fault: 0.050-0.100" (emergency stop, disable drives)

**Purpose**: Detect crashes, stalls, runaway motion

**Example**:
- Axis encounters obstruction
- Motor stalls, position lags
- Following error grows: 0.005" → 0.020" → 0.050"
- At 0.050": Controller issues FOLLOWING ERROR FAULT
- Drives disable, motion stops

## Summary

PID control provides the foundation for servo position control in CNC systems:

**Three Terms**:
- **P**: Responds proportionally to error (speed, stiffness)
- **I**: Eliminates steady-state error (compensates disturbances)
- **D**: Adds damping (reduces overshoot, improves stability)

**Tuning Process**:
1. Tune P first (until oscillatory)
2. Add D to dampen (reduce overshoot)
3. Add I to eliminate steady-state error
4. Verify performance under all conditions

**Key Insights**:
- Start with low gains, increase gradually
- Test after each change
- Balance speed vs. stability
- Document final values

**Next Steps**:
- Learn systematic tuning methods (Section 19.4)
- Add feedforward for following error reduction (Section 19.5)
- Implement trajectory planning (Sections 19.6-19.9)

---

**Next**: [19.4 PID Tuning Methods](section-19.4-tuning-methods.md)
