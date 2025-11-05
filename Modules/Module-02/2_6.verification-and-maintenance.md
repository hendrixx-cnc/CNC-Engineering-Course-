# Module 2 – Vertical Axis and Column Assembly

## 6. Verification & Maintenance Checklist

Comprehensive verification and ongoing maintenance are essential to ensure the vertical axis continues to deliver precision performance throughout its operational life. This section provides detailed procedures, acceptance criteria, and troubleshooting guidance.

### 6.1 Initial Verification Testing

After assembly and before production use, perform the following systematic verification tests to validate design performance.

#### 6.1.1 Column Deflection Test (Static Stiffness)

**Objective:** Verify that column deflection under load meets design specifications.

**Equipment Required:**
- Dial indicator, 0.001 mm resolution
- Magnetic base with articulating arm
- Calibrated weights or force gauge (0-500 N)
- Loading fixture (bar with mounting point at tool location)

**Procedure:**

1. **Mount dial indicator** to stationary reference (machine bed or gantry beam)
   - Position indicator tip at torch/tool mounting location
   - Axis perpendicular to expected deflection direction
   - Zero indicator with no applied load

2. **Apply calibrated load** of 400 N at tool centerline
   - Use weight stack: 40.8 kg suspended from loading fixture
   - Or use horizontal force gauge with calibrated pull
   - Ensure load vector aligns with cutting force direction

3. **Record deflection** after load stabilizes (10-15 seconds)
   - Read dial indicator value
   - Photograph setup for documentation

4. **Remove load** and verify return to zero
   - Residual deflection should be < 0.002 mm
   - Indicates no plastic deformation occurred

5. **Repeat test at multiple positions**
   - Test at top of travel (maximum cantilever)
   - Test at mid-travel
   - Test at bottom of travel
   - Deflection should be consistent (±10%)

**Acceptance Criterion:**
$$\delta_{measured} \leq 0.02 \text{ mm at } 400 \text{ N load}$$

**Typical Results:**
- Excellent design: 0.005-0.010 mm
- Good design: 0.010-0.020 mm
- Marginal design: 0.020-0.030 mm
- Inadequate design: > 0.030 mm (requires redesign)

**If Fails:**
- Verify column cross-section matches design (measure wall thickness)
- Check for loose mounting bolts at column base
- Inspect for cracks or damage in column structure
- Consider adding internal stiffening ribs
- Upgrade to larger column section

**Data Recording:**

| Load (N) | Position (mm) | Deflection (mm) | Status |
|----------|---------------|-----------------|--------|
| 400 | 0 (bottom) | 0.008 | ✓ PASS |
| 400 | 100 (mid) | 0.009 | ✓ PASS |
| 400 | 200 (top) | 0.010 | ✓ PASS |

#### 6.1.2 Rail Parallelism Measurement

**Objective:** Verify linear rails are parallel to each other and to the ball-screw axis within specified tolerances.

**Equipment Required:**
- Precision height gauge or surface plate with indicator stand
- 0.001 mm resolution dial indicator
- Reference straightedge (granite or hardened steel)
- Feeler gauge set (0.01-1.0 mm)

**Procedure:**

1. **Establish reference datum**
   - Use machine bed or precision surface plate as horizontal reference
   - Mount height gauge with indicator

2. **Measure Rail #1 height at multiple points**
   - Positions: 0, 50, 100, 150, 200 mm along travel
   - Measure from reference datum to rail top surface
   - Record heights: $h_1(0), h_1(50), ..., h_1(200)$

3. **Measure Rail #2 height at same positions**
   - Use identical procedure
   - Record heights: $h_2(0), h_2(50), ..., h_2(200)$

4. **Calculate parallelism error**
   $$\Delta h = |h_1(x) - h_2(x)|$$
   
   Maximum variation should be ≤ 0.03 mm

5. **Check for systematic tilt**
   - Plot height vs. position for both rails
   - Slopes should be equal (parallel rails)
   - If slopes differ, rails are not parallel

**Acceptance Criterion:**
$$\text{Max} |\Delta h| \leq 0.03 \text{ mm}$$

**Typical Measurement Data:**

| Position (mm) | Rail #1 Height (mm) | Rail #2 Height (mm) | Δh (mm) | Status |
|---------------|---------------------|---------------------|---------|--------|
| 0 | 50.015 | 50.020 | 0.005 | ✓ |
| 50 | 50.018 | 50.023 | 0.005 | ✓ |
| 100 | 50.022 | 50.025 | 0.003 | ✓ |
| 150 | 50.019 | 50.027 | 0.008 | ✓ |
| 200 | 50.021 | 50.030 | 0.009 | ✓ |

**Maximum deviation:** 0.009 mm (well within 0.03 mm limit)

**If Fails:**
- Check rail mounting bolt torque (may have loosened)
- Add shims under rail to correct height mismatch
- Use 0.025 mm and 0.05 mm shim stock for fine adjustment
- Re-measure after shimming
- If systematic error, may need to re-machine mounting surface

#### 6.1.3 Screw Alignment (Runout and Straightness)

**Objective:** Verify ball-screw is aligned parallel to linear rails and has minimal runout.

**Equipment Required:**
- Dial indicator, 0.001 mm resolution
- Magnetic base
- Precision mandrel or test bar (H6 fit in ball nut bore)
- Rotation tool (hand crank or motor at low speed)

**Procedure:**

1. **Install test mandrel in ball nut**
   - Mandrel should fit snugly (H6 tolerance)
   - Length minimum 100 mm
   - Surface finish Ra < 0.4 μm

2. **Mount dial indicator perpendicular to mandrel**
   - Indicator tip contacts mandrel surface
   - Distance from nut: 50 mm

3. **Rotate ball-screw slowly (< 10 rpm)**
   - Record maximum and minimum indicator readings
   - TIR (Total Indicated Runout) = Max - Min

4. **Traverse carriage along full stroke**
   - Record TIR at multiple positions (every 50 mm)
   - Plot TIR vs. position

5. **Calculate alignment error**
   If TIR varies systematically with position, indicates misalignment:
   $$\text{Misalignment} = \frac{\Delta TIR}{L_{travel}}$$

**Acceptance Criterion:**
- TIR at any position: ≤ 0.02 mm
- Systematic variation: ≤ 0.03 mm over full travel

**Typical Results:**

| Position (mm) | TIR at 0° (mm) | TIR at 90° (mm) | TIR at 180° (mm) | TIR at 270° (mm) | Max TIR (mm) |
|---------------|----------------|-----------------|------------------|------------------|--------------|
| 0 | 0.008 | 0.010 | 0.009 | 0.011 | 0.011 |
| 100 | 0.009 | 0.011 | 0.010 | 0.012 | 0.012 |
| 200 | 0.010 | 0.013 | 0.011 | 0.014 | 0.014 |

**Alignment Quality:** Good (all readings < 0.02 mm limit)

**If Fails:**
- Loosen screw bearing mounts
- Add/remove shims to adjust alignment
- Target: Minimize TIR variation across travel range
- May require iterative shimming process (2-3 cycles)
- If TIR > 0.05 mm, check for bent screw (replace if damaged)

#### 6.1.4 Natural Frequency Measurement (Modal Testing)

**Objective:** Experimentally determine structural natural frequencies and compare to design predictions.

**Equipment Required:**
- Tri-axial accelerometer (piezoelectric or MEMS)
- Data acquisition system (minimum 2 kHz sampling rate)
- Instrumented impact hammer (or alternative excitation)
- FFT analysis software (MATLAB, LabVIEW, or similar)
- Mounting wax or magnetic base for accelerometer

**Procedure:**

1. **Mount accelerometer to carriage**
   - Position at center of mass
   - Orient axes: X (perpendicular to column), Y (parallel to column), Z (vertical)
   - Secure with mounting wax (low mass) or magnetic base

2. **Configure data acquisition**
   - Sampling rate: 2048 or 4096 Hz (Nyquist theorem: > 2× highest frequency of interest)
   - Record length: 2-5 seconds
   - Trigger: Manual or pre-trigger at 10%

3. **Excite structure with impact hammer**
   - Strike column structure at base (low-frequency modes)
   - Strike carriage (high-frequency modes)
   - Use medium-soft tip (excites 0-500 Hz range)
   - Multiple strikes to ensure repeatability

4. **Acquire time-domain data**
   - Record acceleration vs. time for all three axes
   - Verify impact was sufficient (no saturation, clean decay)

5. **Perform FFT (Fast Fourier Transform)**
   - Convert time-domain to frequency-domain
   - Apply windowing function (Hanning or Hamming)
   - Generate frequency response plot (magnitude vs. frequency)

6. **Identify resonant peaks**
   - Locate peaks in frequency spectrum
   - First peak = fundamental natural frequency $f_1$
   - Subsequent peaks = higher-order modes
   - Record frequency and amplitude of each mode

7. **Calculate damping ratio** (optional)
   Use half-power bandwidth method:
   $$\zeta = \frac{f_2 - f_1}{2 f_n}$$
   
   Where $f_1$ and $f_2$ are frequencies at 70.7% of peak amplitude.

**Acceptance Criterion:**
$$f_1 \geq 150 \text{ Hz (for 30 Hz servo bandwidth)}$$

**Typical Frequency Response:**

| Mode | Frequency (Hz) | Damping ζ | Mode Shape | Action Required |
|------|----------------|-----------|------------|-----------------|
| 1 | 182 | 0.012 | X-axis bending | None (adequate) |
| 2 | 188 | 0.011 | Y-axis bending | None (adequate) |
| 3 | 295 | 0.015 | Torsion about Z | Monitor during tuning |
| 4 | 420 | 0.008 | Carriage local mode | May need damping |

**Frequency Margin Check:**

For $f_{servo} = 30$ Hz:
$$\frac{f_1}{f_{servo}} = \frac{182}{30} = 6.07$$ ✓ (exceeds 5× minimum)

**If Fails (f₁ < 150 Hz):**
- Increase column stiffness (larger section or add ribs)
- Reduce moving mass (lighter carriage components)
- Add damping treatment (constrained-layer damping on column)
- Reduce servo bandwidth (short-term fix only)

#### 6.1.5 Counterbalance Force Verification

**Objective:** Confirm counterbalance system provides correct upward force to neutralize gravity.

**Equipment Required:**
- Digital force gauge, 0-100 N range
- Servo amplifier with current monitoring capability
- Spring scale (alternative method)

**Procedure (Method 1: Force Gauge):**

1. **Disable motor drive**
   - Put servo amplifier in disabled state
   - Carriage should be free to move (not brake-locked)

2. **Connect force gauge** to carriage mounting point
   - Use calibrated hook or threaded adapter
   - Ensure force vector is vertical

3. **Pull upward at constant velocity** (approximately 10 mm/s)
   - Read force gauge value
   - Record: $F_{up}$

4. **Pull downward at constant velocity**
   - Read force gauge value (force to overcome counterbalance + friction)
   - Record: $F_{down}$

5. **Calculate balance error**
   $$\text{Balance Error} = \frac{F_{up} - F_{down}}{2}$$
   
   Ideal balance: $F_{up} = F_{down}$

**Procedure (Method 2: Motor Current):**

1. **Enable servo drive** with minimal position gain (free-wheeling mode)

2. **Command slow velocity moves**
   - Upward: 50 mm/min
   - Downward: 50 mm/min
   - Record average motor current for each direction

3. **Calculate current imbalance**
   $$\text{Imbalance} = \frac{|I_{up} - I_{down}|}{I_{avg}} \times 100\%$$

4. **Adjust counterbalance**
   - If $I_{up} > I_{down}$: Increase counterbalance force
   - If $I_{down} > I_{up}$: Decrease counterbalance force
   - Adjust in small increments (5% of total force)

**Acceptance Criterion:**
$$\left|\frac{F_{up} - F_{down}}{F_{avg}}\right| \leq 10\%$$

Or for current method:
$$\frac{|I_{up} - I_{down}|}{I_{avg}} \leq 10\%$$

**Example Data:**

| Direction | Force (N) | Motor Current (A) |
|-----------|----------|-------------------|
| Upward | 38.5 | 0.48 |
| Downward | 42.0 | 0.52 |
| **Average** | **40.25** | **0.50** |
| **Imbalance** | **8.7%** | **8.0%** |

**Result:** Within 10% tolerance (acceptable)

**Fine Adjustment:**
- Increase counterbalance by 2% (add 0.8 N)
- Target: $I_{up} = I_{down} = 0.50$ A

#### 6.1.6 Backlash Measurement

**Objective:** Quantify lost motion (backlash) in drive system for positioning accuracy assessment.

**Equipment Required:**
- Laser interferometer system (e.g., Renishaw XL-80) **OR**
- High-precision dial indicator, 0.001 mm resolution
- Controller with position display

**Procedure (Laser Interferometer Method):**

1. **Setup interferometer**
   - Mount laser head to stationary reference
   - Mount retroreflector to moving carriage
   - Align beam parallel to motion axis

2. **Zero position** at mid-travel (100 mm)

3. **Command bidirectional moves**
   ```
   Position sequence:
   100.00 mm → 110.00 mm (forward)
   110.00 mm → 100.00 mm (reverse)
   100.00 mm → 110.00 mm (forward)
   110.00 mm → 100.00 mm (reverse)
   Repeat 5 cycles
   ```

4. **Record position error** at 100 mm target after each reversal
   - Forward approach: $P_f$
   - Reverse approach: $P_r$
   - Backlash: $B = |P_f - P_r|$

5. **Calculate average backlash** over 10 reversals

**Procedure (Dial Indicator Method - Simplified):**

1. **Mount dial indicator** to stationary column
   - Tip contacts carriage surface
   - Perpendicular to motion axis

2. **Command forward jog** (0.1 mm increments)
   - Observe indicator movement
   - When indicator stops moving, record encoder position

3. **Command reverse jog** (0.1 mm increments)
   - Note encoder position when indicator begins moving
   - Difference = backlash

**Acceptance Criterion:**
$$\text{Backlash} \leq 0.02 \text{ mm}$$

**Typical Results:**
- Preloaded ball-screw: 0.005-0.015 mm (excellent)
- Non-preloaded screw: 0.05-0.15 mm (poor)
- Belt drive: 0.02-0.10 mm (depends on tension)

**If Fails:**
- Increase ball-screw preload (if adjustable type)
- Check for worn ball-screw nut (replace if needed)
- Verify coupling tightness (motor to screw)
- For belt drive: Increase belt tension

#### 6.1.7 Screw Lead Error Mapping and Compensation

**Equipment:** Laser interferometer (1 µm resolution), temperature sensors (screw and column)

**Procedure:**
1. Stabilize machine at reference temperature $T_{ref}$; home Z‑axis.
2. Command 5 mm increments across full travel; record commanded vs. measured position.
3. Build compensation table $e(z)$ at 5 mm intervals; enable interpolation in controller.
4. Repeat measurement to verify residual error reduction.

**Acceptance:**
- Pre‑compensation peak‑to‑peak lead error ≤ ±20 µm; post‑compensation ≤ ±6 µm.
- Residual error remains within the total Z‑axis accuracy budget after thermal compensation.

***

### 6.2 Ongoing Maintenance Schedule

Regular maintenance ensures long-term precision and reliability. Follow this schedule or adjust based on duty cycle and operating environment.

#### 6.2.1 Every 500 Operating Hours (Approximately 3 Months)

**Task 1: Rail Preload Verification**

1. Measure carriage drag force using spring scale
2. Target: 2-5% of dynamic load rating C
3. If drag too high: Reduce preload slightly
4. If drag too low: Increase preload (carriage play develops)

**Task 2: Ball-Screw Lubrication**

1. Clean grease fitting (zerk) on ball nut
2. Inject lithium-based NLGI Grade 2 grease
3. Amount: 2-3 pumps until slight excess visible
4. Wipe away excess grease
5. Cycle axis through full travel to distribute grease

**Task 3: Visual Inspection**

1. Check for chips or debris on rails
2. Inspect cable carrier for wear or cracks
3. Verify all mounting bolts are tight (visual check)
4. Look for signs of oil leakage (gas springs, bearings)

**Time Required:** 30 minutes

#### 6.2.2 Every 1000 Operating Hours (Approximately 6 Months)

**All 500-hour tasks PLUS:**

**Task 4: Counterbalance Force Check**

1. Perform motor current balance test (Section 6.1.5)
2. Adjust gas spring pressure if imbalance > 10%
3. Document force values for trend analysis

**Task 5: Precision Calibration**

1. Run calibrated test program with indicator or laser
2. Measure positioning errors at 0, 50, 100, 150, 200 mm
3. Apply pitch correction in controller if needed
4. Correction formula: $P_{actual} = P_{commanded} + k \times P_{commanded}$

**Task 6: Rail Cleaning and Re-greasing**

1. Remove any protective covers
2. Wipe rails clean with lint-free cloth
3. Apply thin layer of way oil or grease to rail surfaces
4. Manually cycle carriage to distribute lubricant
5. Remove excess to prevent chip accumulation

**Time Required:** 90 minutes

#### 6.2.3 Every 2000 Operating Hours (Approximately 12 Months)

**All 1000-hour tasks PLUS:**

**Task 7: Comprehensive Rail Parallelism Check**

1. Repeat full parallelism measurement (Section 6.1.2)
2. Compare to baseline measurements from commissioning
3. If deviation > 0.05 mm, investigate cause:
   - Loose mounting bolts
   - Column structural fatigue
   - Base settling

**Task 8: Natural Frequency Re-verification**

1. Repeat modal testing (Section 6.1.4)
2. Compare to baseline data
3. If frequency has decreased > 10%, investigate:
   - Loose structural connections
   - Bearing wear increasing compliance
   - Added mass (modifications?)

**Task 9: Ball-Screw Wear Assessment**

1. Measure backlash (Section 6.1.6)
2. If backlash has increased > 50% from baseline:
   - Increase preload (if adjustable nut)
   - Plan for screw/nut replacement
3. Inspect screw surface for:
   - Pitting or spalling
   - Discoloration (overheating)
   - Brinelling (impact damage)

**Task 10: Bearing Condition Monitoring**

1. **Screw Support Bearings:**
   - Check for axial play (should be zero with proper preload)
   - Listen for unusual noise during rotation
   - Feel for rough spots or binding

2. **Linear Rail Carriages:**
   - Check for lateral play (rock carriage side-to-side)
   - Should be zero with proper preload
   - If play detected, adjust preload or replace carriage

**Time Required:** 3 hours

#### 6.2.4 Maintenance Log Template

**Machine ID:** ________________  
**Z-Axis Serial Number:** ________________

| Date | Hours | Task Performed | Measurements | Adjustments Made | Technician |
|------|-------|----------------|--------------|------------------|------------|
| 2024-01-15 | 520 | Rail lube, screw grease | Drag force: 12 N | None | JD |
| 2024-04-10 | 1050 | Full 1000-hr service | Parallelism: 0.012 mm | Counterbalance +2% | JD |
| 2024-07-18 | 1580 | Rail lube, screw grease | Drag force: 14 N | None | SM |
| 2024-10-22 | 2100 | Annual inspection | Backlash: 0.018 mm | Increased preload | JD |

***

### 6.3 Troubleshooting Guide

**Problem: Excessive Position Error (> 0.05 mm)**

| Possible Cause | Diagnostic Test | Solution |
|----------------|----------------|----------|
| Ball-screw backlash | Measure bidirectional repeatability | Increase preload or replace nut |
| Thermal expansion | Test at different temperatures | Add thermal compensation or insulation |
| Servo tuning error | Step response test | Re-tune PID parameters |
| Encoder resolution inadequate | Check encoder specifications | Upgrade to higher resolution encoder |

**Problem: Vibration or Chatter During Motion**

| Possible Cause | Diagnostic Test | Solution |
|----------------|----------------|----------|
| Resonance excitation | Modal analysis (accelerometer) | Add notch filter at resonance frequency |
| Loose mechanical connections | Check all bolt torques | Tighten to specification |
| Worn bearings | Listen for noise, check runout | Replace affected bearings |
| Servo instability | Reduce gains, observe improvement | Reduce bandwidth or add damping |

**Problem: Inconsistent Counterbalance (Motor Current Varying)**

| Possible Cause | Diagnostic Test | Solution |
|----------------|----------------|----------|
| Gas spring losing pressure | Check force at multiple positions | Refill or replace gas springs |
| Cable carrier binding | Manual carriage motion test | Adjust cable carrier routing |
| Friction increase (dirty rails) | Drag force measurement | Clean and lubricate rails |
| Added mass (modifications) | Weigh moving assembly | Re-calculate and adjust counterbalance |

**Problem: High Noise Level**

| Possible Cause | Diagnostic Test | Solution |
|----------------|----------------|----------|
| Ball-screw wear | Visual inspection, measure backlash | Replace screw or nut |
| Bearing failure | Rotation test, listen for grinding | Replace failed bearing immediately |
| Resonance | Frequency analysis | Add damping or structural modification |
| High servo gains | Reduce gains, observe noise change | Optimize servo tuning |

***

### 6.4 Performance Benchmarking

Establish baseline performance metrics during commissioning and compare periodically to detect degradation:

| Parameter | Baseline (New) | After 1000 hrs | After 2000 hrs | Limit | Action if Exceeded |
|-----------|----------------|----------------|----------------|-------|-------------------|
| Deflection @ 400N (mm) | 0.008 | 0.009 | 0.010 | 0.020 | Inspect structure |
| Rail parallelism (mm) | 0.005 | 0.008 | 0.012 | 0.030 | Shim rails |
| Backlash (mm) | 0.010 | 0.015 | 0.022 | 0.030 | Increase preload |
| Natural frequency (Hz) | 185 | 182 | 178 | 150 | Add stiffening |
| Counterbalance (% imbalance) | 4% | 7% | 11% | 15% | Adjust force |
| Positioning accuracy (mm) | ±0.02 | ±0.03 | ±0.04 | ±0.05 | Calibrate or repair |

**Trend Analysis:**

Plot key parameters vs. operating hours. Linear degradation is normal (wear). Sudden changes indicate failure or misalignment requiring immediate investigation.

***

### 6.5 Safety Considerations

**Critical Safety Features:**

1. **Motor Brake:** Must engage on power loss to prevent carriage free-fall
   - Test monthly: Disable power while carriage elevated
   - Brake should hold position with < 1 mm drop

2. **Counterbalance:** Prevents rapid descent if brake fails
   - Should slow (not stop) carriage fall to < 50 mm/s

3. **Software Limits:** Prevent over-travel beyond mechanical range
   - Set soft limits 5-10 mm inside hard limits
   - Test: Jog toward limit, verify deceleration profile

4. **Emergency Stop:** Immediately stops all motion
   - Test weekly: Press E-stop during motion
   - Verify motion halts within 10 mm

5. **Guarding:** Prevents hand/finger pinch points
   - Install bellows or covers over moving carriage
   - Interlock access doors to disable motion when open

**Lockout/Tagout Procedure:**

Before performing maintenance:
1. Press emergency stop button
2. Disconnect motor power at amplifier or main disconnect
3. Manually lower carriage to bottom position (safe height)
4. Install mechanical blocks or pins to prevent carriage motion
5. Attach lockout tag with technician name and date

***

## 6.6 Conclusion: Verification as Ongoing Process

Vertical axis verification is not a one-time commissioning activity—it is an ongoing process of measurement, analysis, and adjustment. Regular verification testing:

- Detects performance degradation before it causes part defects
- Identifies wear patterns guiding proactive component replacement
- Documents machine health over its lifecycle
- Ensures continued compliance with specification
- Maximizes uptime and productivity

**Best Practice:** Treat verification data as a predictive maintenance tool. Trending analysis reveals when components are approaching end-of-life, allowing scheduled replacement during planned downtime rather than reactive failure responses.

The comprehensive checklist and procedures provided in this section form the foundation of a world-class precision machine maintenance program.

***


---

## References

1. **ISO 230-2:2014** - Test code for machine tools - Determination of accuracy and repeatability
2. **ISO 13849-1:2015** - Safety of machinery - Safety-related parts of control systems
3. **Renishaw Ballbar QC20-W User Guide** - Circular interpolation testing
4. **Heidenhain Linear Encoders Catalog** - Measurement system specifications
5. **ASME B89.3.4-2010** - Axes of Rotation: Methods for Specifying and Testing
6. **Machine Tool Maintenance Best Practices** - SME Technical Paper Series
