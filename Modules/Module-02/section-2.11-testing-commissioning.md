# Section 2.11 – Testing and Commissioning

## Overview

Systematic testing validates mechanical assembly and establishes baseline performance before production use. This section covers mechanical verification, counterbalance optimization, servo tuning procedures, and performance validation specific to vertical axis systems.

## Pre-Commissioning Safety Checks

### Mechanical Safety Verification

**Critical checks before applying power:**

1. **Emergency stop functionality**
   - E-stop button accessible and clearly marked
   - E-stop circuit wired to brake (fail-safe)
   - Test: Press E-stop, verify brake engages
2. **Brake operation**
   - With power off, brake should be engaged (spring-applied type)
   - Apply power, brake should release (audible click typical)
   - Cut power, brake should re-engage immediately
3. **Limit switches**
   - Upper and lower travel limits installed
   - Switches positioned 5-10mm beyond desired travel endpoints
   - Test continuity with multimeter
4. **Carriage support**
   - Before releasing brake: Verify counterbalance supports carriage
   - If insufficient, manually support carriage when testing
5. **Guards and covers**
   - Moving parts enclosed (ball screw, coupling)
   - Pinch points protected
   - Cable carrier cannot be contacted during normal operation

**CRITICAL SAFETY RULE:** Never release the Z-axis brake without verified counterbalance or manual support. Unsupported vertical axes can fall rapidly, causing injury or damage.

## Mechanical Verification Tests

### Test 1: Static Stiffness

**Objective:** Verify column deflection under load matches design calculations.

**Equipment:**
- Calibrated weights (5-50 kg depending on machine size)
- Dial indicator (0.001mm resolution)
- Magnetic base

**Procedure:**
1. **Mount indicator** against spindle mount or carriage
   - Reading perpendicular to column face (X or Y direction)
   - Zero indicator with no load
2. **Apply known force** at tool mounting point
   - Hang calibrated weight from spindle nose
   - Typical test: 10-20 kg (100-200 N force)
3. **Record deflection** from indicator
4. **Calculate actual stiffness:**
   $$k_{actual} = \frac{F}{\delta}$$
   Where F = applied force (N), δ = measured deflection (mm)
5. **Compare to design value** (from Section 2.3 calculations)
   - Actual should be ≥80% of designed stiffness
   - If lower: Check column mounting, rail installation, fastener torque

**Example:**
- Applied force: 150 N (15.3 kg weight)
- Measured deflection: 35 µm
- Actual stiffness: 150 / 0.035 = 4,286 N/mm
- Design stiffness: 5,000 N/mm
- Ratio: 86% (acceptable, within 80% threshold)

### Test 2: Backlash Measurement

**Objective:** Quantify total system backlash.

**Equipment:**
- Dial indicator
- Magnetic base
- Manual control or MDI (Manual Data Input)

**Procedure:**
1. **Position carriage** at mid-travel
2. **Mount indicator** against carriage, reading Z-direction
3. **Command upward motion** (+Z) 5mm, wait for settling
4. **Zero indicator**
5. **Command downward motion** (-Z) 0.1mm increments
6. **Note commanded distance** before indicator begins moving
   - This dead zone = backlash
7. **Repeat at 3-5 locations** along Z-travel (top, middle, bottom)
8. **Record maximum backlash**

**Acceptance criteria:**
- General purpose: <50 µm
- Precision work: <20 µm
- Ultra-precision: <5 µm

**If excessive:**
- Check ball screw preload (may be adjustable)
- Inspect coupling for slop
- Verify motor mounting (no deflection under load)

### Test 3: Runout Over Travel

**Objective:** Measure spindle perpendicularity variation over Z-axis travel.

**Equipment:**
- Dial indicator mounted in spindle or on carriage
- Precision ground disc or surface plate on table

**Procedure:**
1. **Mount indicator** in spindle (or attach to carriage)
   - Indicator tip contacts table reference surface
2. **Position Z-axis** at lowest point in travel
3. **Zero indicator**
4. **Traverse Z-axis** to highest point while observing indicator
5. **Record total indicated runout (TIR)** over full travel
6. **Repeat in X and Y directions** (rotate indicator orientation)

**Acceptance criteria:**
- Hobby/light-duty: <100 µm TIR
- General purpose: <50 µm TIR
- Precision: <25 µm TIR

**If excessive:**
- Check column perpendicularity to base
- Verify rail parallelism (re-tram if necessary)
- Inspect for column deflection under carriage weight

### Test 4: Smooth Motion Test

**Objective:** Verify smooth, consistent motion without binding or stick-slip.

**Equipment:**
- Motor drive (low-speed jog)
- Observation

**Procedure:**
1. **Enable motor** and release brake
2. **Jog Z-axis upward** at slow speed (50-100 mm/min)
   - Observe motion: Should be smooth and continuous
   - Listen for unusual noises (grinding, clicking)
3. **Jog Z-axis downward** at same speed
4. **Repeat at multiple speeds** (100, 500, 1000 mm/min)
5. **Note any irregularities:**
   - Binding or tight spots (alignment issue)
   - Jerky motion (stick-slip from friction or servo tuning)
   - Vibration (imbalance, coupling misalignment)

**Resolution:**
- Binding: Re-check rail parallelism and ball screw alignment
- Stick-slip: Improve lubrication, adjust servo gains
- Vibration: Balance toolholder, check coupling alignment

## Counterbalance Optimization

### Force Balance Verification

**Objective:** Adjust counterbalance to neutralize gravitational load.

**Equipment:**
- Motor current meter (drive display or oscilloscope)
- Position feedback (encoder readout or DRO)

**Procedure:**

**Method 1: Static Balance Test (Preferred)**
1. **Position carriage** at mid-travel
2. **Enable motor** (servo on, zero torque command)
3. **Release brake carefully** (support carriage if balance uncertain)
4. **Observe carriage motion:**
   - Sinks downward: Counterbalance too weak
   - Rises upward: Counterbalance too strong
   - Holds position: Balanced
5. **Adjust counterbalance:**
   - Gas spring: Replace with different force rating
   - Pneumatic: Adjust air pressure regulator
   - Weight-cable: Add/remove counterweight mass
6. **Re-test until carriage holds position** (±5% drift acceptable)

**Method 2: Current Monitoring (Quantitative)**
1. **Jog carriage upward** at constant velocity (e.g., 500 mm/min)
2. **Record motor current** during constant-velocity phase (RMS value)
3. **Jog carriage downward** at same velocity
4. **Record motor current** during descent
5. **Calculate balance error:**
   $$\text{Balance error} = \frac{I_{up} + I_{down}}{2}$$
   Ideal balance: $I_{up} = -I_{down}$ (equal magnitude, opposite direction)
6. **Adjust counterbalance** to minimize balance error
7. **Repeat until balance error <10% of rated current**

**Example:**
- Upward current: 1.2 A
- Downward current: -0.3 A
- Balance error: (1.2 + (-0.3)) / 2 = 0.45 A
- Target: <0.5 A for 5A rated drive (10% threshold)
- Result: Acceptable balance

### Dynamic Balance Verification

**Test acceleration symmetry:**

1. **Command rapid upward move** (e.g., +100mm at maximum acceleration)
2. **Record peak current** during acceleration
3. **Command rapid downward move** (-100mm, same acceleration)
4. **Record peak current**
5. **Compare peak currents:**
   - Good balance: Peak currents within 20% of each other
   - Poor balance: Significant asymmetry (adjust counterbalance)

## Electrical Commissioning

### Motor Phasing Verification

**Ensure motor wired correctly:**

**Symptoms of reversed phasing:**
- Motor runs in opposite direction than commanded
- Motor vibrates or doesn't move smoothly

**Correction:**
- Swap any two motor power leads (for 3-phase)
- Update control configuration if needed

**Encoder Direction:**
- Jog motor in +Z direction, verify encoder count increases
- If reversed: Swap encoder A+/A- signals or configure in drive

### Home Switch Setup

**Establish machine zero reference:**

1. **Install home switch** at known Z position
   - Typically near top of travel
   - Repeatable trigger point (proximity or mechanical switch)
2. **Configure homing routine** in control
   - Approach speed (slow, 100-200 mm/min for accuracy)
   - Home offset (distance from switch to actual zero)
3. **Test homing sequence:**
   - Command home (G28 Z0 or control-specific command)
   - Verify carriage moves to switch, triggers, and backs off
   - Repeatability: Home 5× times, measure variation (<10 µm target)

### Limit Switch Testing

**Verify travel limit protection:**

1. **Jog to upper limit** until switch triggers
   - Motion should stop immediately
   - Record position
2. **Jog to lower limit** until switch triggers
   - Motion should stop
   - Record position
3. **Calculate actual travel:** Upper position - Lower position
4. **Set soft limits** in control software
   - 5-10mm inside hard limits (prevents crashes)
5. **Test soft limits:**
   - Command move beyond soft limit
   - Control should reject move or stop at limit

## Servo Tuning

### Prerequisites

**Before tuning:**
1. Counterbalance optimized (balance error <10%)
2. All mechanical issues resolved (no binding, smooth motion)
3. Encoder and motor phasing verified
4. Safety systems operational (E-stop, limits, brake)

### Tuning Procedure

**Step 1: Disable All Gains**
- Set Kp, Ki, Kd, FF to zero
- Motor should not respond to position commands (only brake holds position)

**Step 2: Proportional Gain (Kp)**
1. **Increase Kp gradually** from zero
   - Start: Kp = 10-50 (depending on drive units)
   - Increment: Double Kp each step
2. **Test response** after each increase
   - Command small move (±10mm)
   - Observe: System should become more responsive
3. **Continue until oscillation** begins (carriage oscillates around target)
4. **Note Kp at onset of oscillation** (critical gain, Kc)
5. **Reduce Kp to 40-60% of Kc** for stability margin
   - Example: Kc = 500, use Kp = 200-300

**Step 3: Derivative Gain (Kd)**
1. **Add derivative damping** to reduce overshoot
   - Start: Kd = Kp / 10
   - Adjust: Increase if oscillation persists, decrease if sluggish
2. **Test with rapid moves**
   - 100mm move at high acceleration
   - Observe settling time and overshoot
3. **Target: Critically damped response**
   - Minimal overshoot (<5%)
   - Fast settling (<200ms for typical servo)

**Step 4: Integral Gain (Ki)**
1. **Add integral to eliminate steady-state error**
   - Start: Ki = Kp / 100
   - Increase slowly (can destabilize system if too high)
2. **Test positioning accuracy**
   - Command position, wait for settling
   - Check final error (should be <1 encoder count)
3. **Increase Ki until error eliminated** but before oscillation begins

**Step 5: Feed-Forward Tuning**

**Velocity Feed-Forward (FFv):**
- Reduces following error during constant velocity
- Start: FFv = 0.8
- Increase to 1.0 if following error present during moves
- Measure following error: Position error during constant-velocity phase

**Acceleration Feed-Forward (FFa):**
- Reduces following error during acceleration
- Start: FFa = 0.5
- Adjust based on following error during accel/decel
- Too high: Overshoot at end of move
- Too low: Lag during acceleration

**Step 6: Gravity Compensation (If Available)**
- Some drives allow constant torque offset
- Set to compensate for residual gravitational torque (if counterbalance not perfect)
- Value: Feed-forward torque = T_gravity (from Section 2.6)

### Tuning Verification Tests

**Test 1: Step Response**
- Command 50mm move from rest
- Record position vs time
- Analyze:
  - Rise time (time to reach 90% of target)
  - Overshoot (should be <5%)
  - Settling time (time to reach ±10 µm of target)

**Test 2: Following Error**
- Command constant-velocity move (500 mm/min)
- Monitor following error (commanded position - actual position)
- Target: <100 µm during motion, <10 µm at rest

**Test 3: Bi-Directional Repeatability**
- Move to position from above (+Z approach)
- Record final position
- Move away, return from below (-Z approach)
- Record final position
- Repeatability = difference between approaches
- Target: <20 µm for precision work

**Test 4: High-Speed Moves**
- Command rapid traverse at maximum speed
- Verify no overshoot or instability
- Check motor current (should not exceed rated)

## Performance Validation

### Accuracy Testing

**Circular interpolation test (if multi-axis):**
1. Program circular move in XZ or YZ plane
2. Measure actual path with indicator or laser interferometer
3. Calculate circularity error
4. Target: <50 µm for general purpose

**Positioning accuracy:**
1. Command move to known position (use gage blocks or precision height gage)
2. Measure actual position
3. Repeat at 5-10 positions across Z-travel
4. Calculate maximum error
5. ISO 230-2 standard: Positioning accuracy (A) and repeatability (R)

### Thermal Stability Test

**Objective:** Measure thermal drift over operating cycle.

**Equipment:**
- Dial indicator (µm resolution)
- Temperature sensor (column, ambient)
- Timer

**Procedure:**
1. **Cold start:** Machine at ambient temperature
2. **Mount indicator** reading against spindle face or carriage
3. **Zero indicator**
4. **Run warm-up cycle:**
   - Spindle at 50-75% rated speed
   - Z-axis jogging over full travel
5. **Record indicator reading** every 10 minutes for 2 hours
6. **Record temperatures** (column, spindle, ambient)
7. **Plot drift vs time**

**Analysis:**
- Initial drift rate: µm/hour (first 30 minutes)
- Stabilized drift: After 60-90 minutes (should be <10 µm/hour for precision work)
- Total drift: From cold to stabilized (indicates warm-up requirement)

**Example results:**
- 0-30 min: 45 µm expansion (high rate, machine heating)
- 30-60 min: 12 µm expansion (slowing)
- 60-120 min: <5 µm variation (thermally stable)
- Conclusion: 60-minute warm-up required before precision work

### Cutting Test

**Objective:** Validate performance under realistic cutting loads.

**Test piece:**
- Aluminum or steel block
- Face milling operation (controlled depth of cut and feed rate)

**Procedure:**
1. **Mount test piece** on table
2. **Program simple face milling** routine
   - Multiple passes in Z-axis (stepping down)
   - Record spindle load, feed rate, depth of cut
3. **Execute program**
   - Monitor motor current (should not exceed rated)
   - Listen for unusual sounds (chatter, vibration)
   - Observe surface finish
4. **Measure result:**
   - Surface flatness (sweep with indicator)
   - Surface finish (visual or profilometer)
   - Dimensional accuracy (depth of cut)

**Acceptance criteria:**
- Flatness: <50 µm over machined area
- Surface finish: Appropriate for material and tooling
- Dimensional accuracy: ±25 µm or better
- No chatter or excessive vibration

### Repeatability Test

**Procedure:**
1. **Program routine:** Move to position, dwell, return to start
2. **Execute 30 cycles** (statistical significance)
3. **Measure final position** after each cycle
   - Indicator against carriage reference surface
4. **Calculate standard deviation** of position measurements
5. **Repeatability (R) = 4× standard deviation** (per ISO 230-2)

**Target performance:**
- Hobby/light-duty: R < 50 µm
- General purpose: R < 20 µm
- Precision: R < 10 µm

**Example:**
- 30 measurements: Mean = 0.0 µm, StdDev = 3.2 µm
- Repeatability: 4 × 3.2 = 12.8 µm (meets general-purpose target)

## Commissioning Documentation

### Performance Report

**Create comprehensive record:**

```
Z-Axis Commissioning Report
============================
Date: __________
Machine ID: __________
Technician: __________

MECHANICAL VERIFICATION
-----------------------
Static Stiffness:
  Applied force: _____ N
  Deflection: _____ µm
  Measured stiffness: _____ N/mm
  Design stiffness: _____ N/mm
  Ratio: _____ %

Backlash: _____ µm (max over travel)

Runout Over Travel:
  X-direction: _____ µm TIR
  Y-direction: _____ µm TIR

Smooth Motion: [  ] Pass  [  ] Fail
  Notes: _________________________

COUNTERBALANCE
--------------
Balance method: [  ] Gas spring  [  ] Pneumatic  [  ] Weight-cable
Balance force: _____ N (target: _____ N)
Static balance: [  ] Holds position  [  ] Drifts up  [  ] Drifts down
Current balance error: _____ A (_____ % of rated)

SERVO TUNING
------------
Final gains:
  Kp = _____
  Ki = _____
  Kd = _____
  FFv = _____
  FFa = _____

Step response:
  Rise time: _____ ms
  Overshoot: _____ %
  Settling time: _____ ms

Following error (at 500 mm/min): _____ µm

PERFORMANCE VALIDATION
----------------------
Positioning accuracy: ±_____ µm
Repeatability: ±_____ µm
Thermal stability: _____ µm/hour (after warm-up)
Warm-up time required: _____ minutes

Cutting test results:
  Material: __________
  Depth of cut: _____ mm
  Feed rate: _____ mm/min
  Surface flatness: _____ µm
  Surface finish: [  ] Acceptable  [  ] Poor
  Dimensional accuracy: ±_____ µm

ACCEPTANCE
----------
System meets performance specifications: [  ] Yes  [  ] No

Approved by: ________________  Date: __________

Notes:
_____________________________________________
```

### Baseline Configuration File

**Save control parameters:**
- Servo gains (Kp, Ki, Kd, FF values)
- Counterbalance settings
- Soft limits and home position
- Acceleration/velocity limits
- Thermal compensation coefficients (if used)

**Purpose:** Allows restoration of known-good configuration after changes or troubleshooting.

## Troubleshooting Common Issues

### Issue: Excessive Following Error

**Symptoms:**
- Position lags behind commanded during moves
- "Following error" alarm from drive

**Causes:**
- Insufficient proportional gain (Kp too low)
- Counterbalance not adjusted (gravitational bias)
- Mechanical friction (binding)

**Solutions:**
1. Increase Kp (verify stability afterward)
2. Optimize counterbalance to reduce gravitational load
3. Check for mechanical binding, improve lubrication
4. Add velocity feed-forward (FFv)

### Issue: Oscillation or Instability

**Symptoms:**
- Carriage oscillates around target position
- High-pitched whine from motor
- Cannot tune system stable

**Causes:**
- Excessive proportional gain (Kp too high)
- Insufficient damping (Kd too low)
- Mechanical resonance in structure

**Solutions:**
1. Reduce Kp to 40-60% of critical gain
2. Increase Kd for damping
3. Add velocity feedback filter (if available in drive)
4. Check for loose mechanical components (resonance source)

### Issue: Asymmetric Response (Up vs Down)

**Symptoms:**
- Different behavior moving up vs down
- Overshoot in one direction only
- Current draw imbalanced

**Causes:**
- Inadequate counterbalancing (gravitational bias)
- Asymmetric friction (e.g., brake dragging)

**Solutions:**
1. Optimize counterbalance force
2. Add gravity feed-forward compensation in drive
3. Check brake releases fully (measure air gap or check current)
4. Verify rails lubricated evenly

### Issue: Poor Repeatability

**Symptoms:**
- Returns to different positions on repeated moves
- Backlash measurement inconsistent

**Causes:**
- Mechanical backlash (ball screw, coupling)
- Thermal variation (position changes with temperature)
- Inadequate servo gains (position not held tightly)

**Solutions:**
1. Check and adjust ball screw preload
2. Inspect coupling for wear or slop
3. Increase integral gain (Ki) to eliminate steady-state error
4. Implement thermal compensation if drift related to temperature

## Key Takeaways

1. **Safety first:** Verify brake and E-stop before any motion testing
2. **Mechanical before electrical:** Resolve all binding and alignment issues before servo tuning
3. **Counterbalance optimization** critical for good servo performance and reduced wear
4. **Systematic tuning:** Kp first (stability), then Kd (damping), then Ki (accuracy), finally FF
5. **Following error** indicates under-tuned system or mechanical issues
6. **Oscillation** indicates over-tuned system (reduce Kp, add Kd)
7. **Thermal stability testing** reveals warm-up requirements for precision work
8. **Documentation** enables future troubleshooting and maintenance
9. **Cutting test** validates system under realistic loads (essential final check)
10. **Baseline configuration** saved after successful commissioning (reference for future)

***

**Next**: [Section 2.12 – Conclusion](section-2.12-conclusion.md)

**Previous**: [Section 2.10 – Assembly and Alignment](section-2.10-assembly-alignment.md)
