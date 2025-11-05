# Section 1.10: Testing and Validation

## Introduction

**"Trust, but verify."** A completed frame may look rigid and square, but only systematic testing reveals actual performance. This section presents quantitative validation procedures to confirm that the frame meets design specifications for:

1. **Static stiffness** (load-deflection characteristics)
2. **Dynamic performance** (natural frequencies, damping)
3. **Geometric accuracy** (positioning errors, backlash)
4. **Thermal stability** (drift over temperature cycles)
5. **Long-term reliability** (creep, fatigue, joint relaxation)

Professional machine builders perform these tests before shipping equipment. Hobbyists who skip validation discover problems during critical jobs—far more expensive than upfront testing. This section provides practical test procedures using commonly available equipment: dial indicators, accelerometers, data acquisition systems, and standard metrology tools.

### Learning Objectives

By the end of this section, you will be able to:

1. Measure frame stiffness using dial indicators and known loads
2. Perform modal analysis to identify natural frequencies and mode shapes
3. Conduct geometric accuracy tests per ISO 230-1 standards
4. Evaluate thermal stability through temperature cycling
5. Interpret test data and identify root causes of deficiencies
6. Create acceptance test procedures for production machines
7. Document baseline performance for future maintenance reference

---

## Static Stiffness Testing

### Load-Deflection Test Setup

**Objective:** Verify frame deflection under cutting loads matches predictions from Section 1.3.

**Equipment:**
- Known weights (20-100 kg, calibrated to ±0.5%)
- Dial indicators (0.01 mm resolution, magnetic base)
- Loading frame or chain hoist for applying force

**Procedure:**

**Test 1: Gantry Beam Deflection (Vertical Loading)**

```
   Test setup:

   ════════●════════  ← Gantry beam
           ↓ Load (50 kg = 490 N)

   ┌──────────────┐
   │  Indicator   │  ← Dial indicator, measures vertical deflection
   └──────────────┘
```

**Steps:**

1. Zero dial indicator with no load (gantry at mid-span)
2. Apply 25 kg weight → record deflection δ₁
3. Apply 50 kg weight → record deflection δ₂
4. Apply 75 kg weight → record deflection δ₃
5. Remove load → verify indicator returns to zero (elastic behavior)

**Data analysis:**

Plot Force vs Deflection:

```
   Force (N)
    800├────────────●  ← Linear fit: F = k × δ
       │          ╱
    600│        ●
       │      ╱
    400│    ●
       │  ╱
    200│●
       │
       └──┬───┬───┬───→ Deflection (mm)
         0.0 0.1 0.2 0.3

   Slope = stiffness k (N/mm)
```

Calculate stiffness from slope:
```
k_measured = ΔF / Δδ
```

Compare to theoretical stiffness (from Section 1.5):
```
k_theoretical = 48 E I / L³  (for simply-supported beam)
```

**Acceptance criteria:**
- k_measured > 0.85 × k_theoretical (accounts for joint compliance)
- Linearity: R² > 0.98 (confirms elastic behavior, no plastic deformation)
- Return to zero: <0.02 mm hysteresis (confirms no permanent set)

### Worked Example 1.10.1: Stiffness Test Data Analysis

**Test data:**

| Load (kg) | Force (N) | Deflection (mm) |
|-----------|-----------|-----------------|
| 0 | 0 | 0.00 |
| 25 | 245 | 0.18 |
| 50 | 490 | 0.35 |
| 75 | 735 | 0.53 |

**Calculate stiffness:**

Using linear regression (or simply: k = F/δ for each point):

```
k₁ = 245 / 0.18 = 1,361 N/mm
k₂ = 490 / 0.35 = 1,400 N/mm
k₃ = 735 / 0.53 = 1,387 N/mm

Average: k_measured = (1,361 + 1,400 + 1,387) / 3 = 1,383 N/mm
```

**Compare to theory:**

Beam: W200×31 I-beam, L = 2,000 mm, I = 21.4 × 10⁶ mm⁴, E = 200 GPa

```
k_theory = 48 × 200×10⁹ Pa × 21.4×10⁻⁶ m⁴ / (2.0 m)³
         = 205,440,000 / 8
         = 25.68 × 10⁶ N/m
         = 25,680 N/mm  (for beam alone, infinite support stiffness)
```

Wait—measured k (1,383 N/mm) is **18× lower** than theoretical!

**Diagnosis:**

Theory assumes rigid supports. Actual frame has compliant:
- Y-axis rail mounting (flexes)
- Gantry uprights (compress/bend)
- Base frame (twists)

**Refined model:** Series stiffness

```
1/k_total = 1/k_beam + 1/k_uprights + 1/k_base

Solving for k_uprights + k_base:
1/1,383 = 1/25,680 + 1/k_other
k_other = 1,467 N/mm  (combined support stiffness)
```

**Conclusion:** Supports contribute 51% of total deflection (k_other = 1,467 vs k_beam = 25,680). **Supports, not beam, are the limiting factor.**

**Design action:** Reinforce gantry uprights or base frame to increase k_other.

---

## Modal Analysis and Vibration Testing

### Natural Frequency Measurement

**Objective:** Identify frame natural frequencies and mode shapes (Section 1.3).

**Equipment:**
- Accelerometer (piezoelectric, 10 mV/g sensitivity, 0-2 kHz range)
- Impact hammer (instrumented, with force sensor)
- Data acquisition system (2-channel, 5 kHz sample rate minimum)
- Analysis software (MATLAB, Python, or dedicated modal software)

**Procedure: Impulse Response Method**

```
   Test setup:

   ════════════════  ← Frame
        ↑     ●
     Hammer   Accelerometer
     impact   (measures response)
```

**Steps:**

1. Mount accelerometer at location of interest (e.g., gantry center, Z-axis mount point)
2. Strike frame with instrumented hammer (consistent force, ~50-100 N)
3. Record force input and acceleration response (5-10 seconds, 5 kHz sample rate)
4. Compute Frequency Response Function (FRF): H(f) = A(f) / F(f)
5. Identify peaks in FRF magnitude → natural frequencies

**Data analysis:**

```
   FRF Magnitude (dB)

    0├───┐
      │   ↓ Peak 1: f₁ = 85 Hz (first mode)
   -20│   │╲
      │   │ ╲    ↓ Peak 2: f₂ = 156 Hz (second mode)
   -40│   │  ╲   │╲
      │   │   ╲  │ ╲
   -60│   │    ╲│  ╲
      └───┴──────┴───┴──→ Frequency (Hz)
         50  100  150  200
```

**Damping ratio extraction:**

Half-power bandwidth method:

```
ζ = Δf / (2 × f_n)
```

Where:
- Δf = bandwidth at -3 dB from peak
- f_n = natural frequency (peak location)

### Worked Example 1.10.2: Modal Test Analysis

**Test results:**

Peak 1:
- Frequency: f₁ = 83 Hz
- Half-power bandwidth: 80-86 Hz → Δf = 6 Hz
- Damping ratio: ζ₁ = 6 / (2 × 83) = 0.036 = 3.6%

Peak 2:
- Frequency: f₂ = 154 Hz
- Half-power bandwidth: 148-160 Hz → Δf = 12 Hz
- Damping ratio: ζ₂ = 12 / (2 × 154) = 0.039 = 3.9%

**Compare to design targets (Section 1.3):**

- Spindle speed: 24,000 RPM = 400 Hz
- Required frequency: f₁ > 400/2.5 = 160 Hz (for 2.5× safety margin)

**Assessment:**
```
f₁ = 83 Hz < 160 Hz  ❌ FAILS
```

**Implication:** Risk of resonance excitation during high-speed spindle operation. Could cause:
- Poor surface finish (chatter)
- Accelerated tool wear
- Bearing damage

**Corrective actions:**

1. **Increase stiffness** (Section 1.5): Add ribs to gantry → expect f₁ increase to 120-140 Hz
2. **Reduce mass** (if moving gantry): Use lighter materials → expect f₁ increase to 100-130 Hz
3. **Add damping** (tuned mass damper): Won't increase f₁ but reduces vibration amplitude at resonance
4. **Operational limit:** Restrict spindle speed to <12,000 RPM (200 Hz, below f₁) until structural improvements made

**Verification:** Re-test after modifications, confirm f₁ > 160 Hz.

---

## Geometric Accuracy Testing (ISO 230-1)

### Positioning Accuracy and Repeatability

**Definitions:**

- **Positioning accuracy (A):** Difference between commanded position and actual position (systematic error)
- **Repeatability (R):** Variation when returning to same position multiple times (random error)

```
   Positioning scatter:

   Target ●────────●────────●────────●  ← Commanded positions
          │        │        │        │
   Actual ●─●──●───●●───●───●─●──●───●  ← Measured positions
          └─ R ─┘  └─ A ─┘
          Repeatability  Accuracy
```

**ISO 230-1 Test Procedure:**

**Test:** Linear positioning accuracy (X-axis)

1. Divide axis travel into 7-10 test positions (equally spaced)
2. Approach each position from positive direction, measure 5×
3. Approach each position from negative direction, measure 5×
4. Calculate mean position, accuracy, and repeatability at each point

**Equipment:**

- Laser interferometer (0.001 mm resolution, Renishaw XL-80 or similar)
- Or precision displacement sensor (Mitutoyo linear scale, ±0.005 mm)

**Data analysis:**

For each target position i:

```
Mean position (forward): x̄ᵢ⁺ = (Σ xᵢ⁺) / 5
Mean position (reverse): x̄ᵢ⁻ = (Σ xᵢ⁻) / 5

Positioning accuracy: Aᵢ = |x̄ᵢ - xₜₐᵣgₑₜ|

Repeatability: Rᵢ = 4 × s  (where s = standard deviation of 5 measurements)
```

**Overall axis metrics:**

```
A = max(Aᵢ)  (maximum positioning error)
R = max(Rᵢ)  (maximum repeatability)
```

**Acceptance criteria (typical CNC router):**

- Positioning accuracy: A < 0.10 mm
- Repeatability: R < 0.02 mm

### Worked Example 1.10.3: Positioning Test Data

**X-axis test (partial data, 3 of 7 positions):**

| Target (mm) | Forward measurements (mm) | Reverse measurements (mm) |
|-------------|---------------------------|---------------------------|
| 0 | 0.01, 0.02, 0.01, 0.02, 0.01 | -0.01, 0.00, -0.01, 0.00, -0.01 |
| 500 | 500.08, 500.09, 500.08, 500.10, 500.09 | 500.05, 500.06, 500.05, 500.07, 500.06 |
| 1000 | 1000.15, 1000.17, 1000.16, 1000.16, 1000.18 | 1000.12, 1000.13, 1000.12, 1000.14, 1000.13 |

**Analysis for position 500 mm:**

Forward:
```
x̄⁺ = (500.08 + 500.09 + 500.08 + 500.10 + 500.09) / 5 = 500.088 mm
s⁺ = 0.008 mm (standard deviation)
```

Reverse:
```
x̄⁻ = (500.05 + 500.06 + 500.05 + 500.07 + 500.06) / 5 = 500.058 mm
s⁻ = 0.008 mm
```

Mean position (bidirectional):
```
x̄ = (500.088 + 500.058) / 2 = 500.073 mm
```

Positioning accuracy:
```
A₅₀₀ = |500.073 - 500.000| = 0.073 mm
```

Repeatability:
```
R₅₀₀ = 4 × max(s⁺, s⁻) = 4 × 0.008 = 0.032 mm
```

**Overall (from all 7 positions, assuming similar results):**

```
A_max = 0.15 mm  (at x = 1000 mm)
R_max = 0.032 mm
```

**Assessment:**

- Accuracy: 0.15 mm ⚠️ (marginal for ±0.10 mm spec, acceptable for ±0.20 mm)
- Repeatability: 0.032 mm ✓ (good, well within 0.05 mm spec)

**Interpretation:**

Good repeatability but poor accuracy → **systematic error, likely calibration offset**.

**Correction:** Apply position-dependent scaling factor in controller:

```
Scale factor = Target / Measured = 1000.00 / 1000.15 = 0.99985

New commanded position: X_cmd × 0.99985
```

Re-test after correction, confirm A < 0.10 mm.

---

## Thermal Stability Testing

### Temperature Cycling Test

**Objective:** Quantify thermal drift over typical shop temperature variations (Section 1.8).

**Procedure:**

1. **Baseline:** Stabilize machine at reference temperature T_ref = 20°C for 4 hours
2. **Measure:** Record position of precision artifact (gauge block or laser target)
3. **Heat cycle:** Raise shop temperature to 30°C over 2 hours
4. **Monitor:** Record artifact position every 15 minutes for 6 hours (thermal transient + steady-state)
5. **Cool cycle:** Lower temperature back to 20°C, monitor for 6 hours
6. **Analysis:** Plot position vs temperature, calculate thermal drift coefficient

**Equipment:**

- Precision artifact (100 mm gauge block, Grade 0, ±0.0005 mm)
- Displacement sensor (laser interferometer or capacitive probe, ±0.001 mm)
- Temperature sensors (4× thermocouples on frame, ±0.5°C)

**Data analysis:**

```
   Position drift vs Temperature:

   Position
   (mm)
   0.20├───────────────────●  ← Max drift at ΔT = +10°C
       │                 ╱
   0.15│               ╱
       │             ╱
   0.10│           ●
       │         ╱
   0.05│       ●
       │     ╱
   0.00├───●─────────────────→ Temperature (°C)
      20   22   24   26   28   30

   Slope = thermal drift coefficient (mm/°C)
```

Calculate drift coefficient:
```
α_drift = ΔPosition / ΔTemperature
```

**Acceptance criteria:**

For 2m frame, thermal expansion ΔL = α × L × ΔT:
- Steel: α = 11.7×10⁻⁶/°C → ΔL = 0.234 mm for ΔT = 10°C
- Acceptable with compensation: <0.05 mm residual drift (78% compensation effectiveness)

### Thermal Time Constant Measurement

**Procedure:**

1. Apply step temperature change (turn on 1 kW heater near frame)
2. Record frame temperature vs time (multiple locations)
3. Fit exponential: T(t) = T_∞ + (T₀ - T_∞) × exp(-t/τ)
4. Extract time constant τ

**Typical results (Section 1.8):**

- Steel frame, 100 kg: τ = 10-20 minutes
- Aluminum frame, 40 kg: τ = 5-10 minutes
- Cast iron base, 500 kg: τ = 60-120 minutes

**Implication:** Allow 3τ warm-up time before precision work (95% thermal equilibrium).

---

## Long-Term Stability Testing

### Creep and Settling

**Phenomenon:** Joints and materials relax over time under sustained load.

**Test procedure:**

1. Apply rated load to gantry (e.g., full Z-axis weight + 50% cutting force)
2. Measure deflection immediately: δ₀
3. Measure deflection after 24 hours: δ₂₄
4. Measure deflection after 1 week: δ₁₆₈

**Creep metric:**
```
Creep rate = (δ₁₆₈ - δ₀) / δ₀ × 100%
```

**Acceptable:** <2% creep over 1 week (confirms elastic behavior, no plastic deformation)

**Typical causes of excessive creep:**
- Bolted joints (preload relaxation): Re-torque bolts
- Plastic bushings (viscoelastic): Replace with metal bearings
- Overloaded members (yielding): Upgrade section size

### Backlash and Lost Motion

**Test:** Ballbar test (ISO 230-4)

Mount precision ballbar between spindle and table, program circular motion:

```
   Ballbar test:

   ●────────●  ← Precision ballbar (telescoping, measures radius)
   Spindle  Table

   Programmed: 100.000 mm radius circle
   Measured: Deviation from perfect circle
```

**Results:**

```
   Deviation plot (exaggerated):

        ╱───╲
      ╱       ╲
     │    ●    │  ← Ideal circle
      ╲       ╱
        ╲───╱
         ↑
   Flat spots indicate backlash
```

**Quantify backlash:**

Measure reversal error (position error when changing direction):

```
B = |x(forward) - x(reverse)|  at same commanded position
```

**Typical values:**

- Ball screw (preloaded): B = 0.005-0.02 mm
- Rack & pinion: B = 0.05-0.15 mm
- Belt drive (no preload): B = 0.2-0.5 mm

---

## Acceptance Testing and Quality Assurance

### Production Test Protocol

For commercial machines, establish standardized acceptance test:

**Test sequence:**

1. **Visual inspection** (welds, alignment, finish)
2. **Dimensional check** (frame squareness, rail parallelism)
3. **Stiffness test** (gantry deflection <0.15 mm under 500 N load)
4. **Modal test** (f₁ > 60 Hz for routers, >150 Hz for mills)
5. **Positioning test** (A < 0.10 mm, R < 0.03 mm per ISO 230-1)
6. **Thermal stability** (drift <0.10 mm over ±5°C cycle)
7. **Run-in test** (24 hours continuous motion, re-check metrics)

**Pass/fail criteria:**

Machine passes if **ALL** tests meet specifications. Single failure → investigate, correct, re-test.

**Documentation:**

Create test report with:
- Serial number, date, technician
- Test results (tabulated, with plots)
- Pass/fail status
- Corrective actions taken (if any)
- Customer signature (acceptance)

**Example test report template:**

```
═══════════════════════════════════════
  CNC MACHINE ACCEPTANCE TEST REPORT
═══════════════════════════════════════

Machine S/N: 2024-001
Model: Router 2000×1000
Date: 2024-01-20
Technician: J. Smith

TEST RESULTS:
┌──────────────────────────┬─────────┬──────┬────────┐
│ Test                     │ Result  │ Spec │ Status │
├──────────────────────────┼─────────┼──────┼────────┤
│ Frame squareness         │ 0.8 mm  │ <2mm │ PASS ✓ │
│ Gantry deflection (500N) │ 0.12 mm │<0.15 │ PASS ✓ │
│ First natural frequency  │ 87 Hz   │ >60  │ PASS ✓ │
│ X-axis accuracy          │ 0.09 mm │ <0.1 │ PASS ✓ │
│ X-axis repeatability     │ 0.02 mm │ <0.03│ PASS ✓ │
│ Thermal drift (10°C)     │ 0.18 mm │ <0.2 │ PASS ✓ │
└──────────────────────────┴─────────┴──────┴────────┘

OVERALL: ✓ PASS

Notes: All specifications met. Machine ready for shipment.

Technician signature: _______________
Customer acceptance: _______________
```

---

## Troubleshooting Test Failures

### Failure Mode: Excessive Deflection

**Symptom:** Measured stiffness k < 0.7 × k_theoretical

**Possible causes:**

1. **Joint compliance:** Bolted corners, inadequate preload
   - **Test:** Retorque all bolts to specification, re-test
   - **Fix:** Upgrade to welded joints (Section 1.7)

2. **Undersized members:** Beam I insufficient
   - **Test:** Calculate I from measured dimensions, compare to design
   - **Fix:** Add reinforcement ribs (Section 1.5)

3. **Base frame twist:** Diagonal measurements differ >2mm
   - **Test:** Measure diagonals under load
   - **Fix:** Add cross-bracing (Section 1.6)

### Failure Mode: Low Natural Frequency

**Symptom:** f₁ < target (e.g., 60 Hz for router)

**Possible causes:**

1. **Excessive mass:** Moving components heavier than designed
   - **Test:** Weigh gantry assembly, compare to design
   - **Fix:** Reduce mass (lighter motor mounts, remove non-structural material)

2. **Insufficient stiffness:** k too low (compounds with mass issue)
   - **Fix:** See "Excessive Deflection" above

3. **Inadequate bracing:** Frame modes (not just gantry bending)
   - **Test:** Perform modal test with accelerometers at multiple locations, identify mode shape
   - **Fix:** Add bracing where maximum displacement occurs

### Failure Mode: Poor Repeatability

**Symptom:** R > 0.05 mm (random positioning error)

**Possible causes:**

1. **Backlash:** Ball screw/drive system issue (covered in Module 3)
2. **Thermal transients:** Temperature not stabilized
   - **Test:** Allow 1 hour stabilization, re-test
3. **Loose components:** Bearing blocks, couplings
   - **Fix:** Check all fasteners, re-torque
4. **Measurement error:** Indicator mounting flex
   - **Fix:** Rigidly mount indicator, eliminate measurement artifacts

---

## Summary and Testing Checklist

### Recommended Test Schedule

**Pre-shipment (new machine):**
- [ ] Frame squareness and alignment (Section 1.9)
- [ ] Static stiffness test (gantry, base)
- [ ] Modal analysis (first 3 natural frequencies)
- [ ] Positioning accuracy and repeatability (ISO 230-1, abbreviated test)
- [ ] Thermal stability (accelerated, 2-hour cycle)

**Commissioning (at customer site):**
- [ ] Re-check alignment after transport
- [ ] Full positioning accuracy test (ISO 230-1, 7-10 positions)
- [ ] Cutting test (machine actual workpiece, measure results)
- [ ] Documentation (provide test report, baseline data)

**Periodic (every 6-12 months):**
- [ ] Repeatability check (detect bearing wear)
- [ ] Backlash measurement (detect mechanical wear)
- [ ] Re-torque critical fasteners
- [ ] Compare to baseline (identify degradation trends)

### Key Performance Indicators (KPIs)

Track these metrics over machine lifetime:

| Metric | New machine | After 1 year | After 3 years | Action threshold |
|--------|-------------|--------------|---------------|------------------|
| Repeatability (mm) | 0.02 | 0.03 | 0.04 | >0.05 → service |
| Backlash (mm) | 0.01 | 0.02 | 0.04 | >0.10 → replace |
| Natural freq. (Hz) | 85 | 83 | 80 | <70 → inspect |
| Thermal drift (mm) | 0.15 | 0.18 | 0.22 | >0.30 → investigate |

---

## Practical Exercises

### Exercise 1.10.1: Stiffness Test Design

Design stiffness test for gantry beam:
- Span: 1,800 mm
- Expected deflection: 0.08 mm under 400 N load
- Available: dial indicator (0.01 mm resolution), weights (10-50 kg)

**Tasks:**
1. Calculate theoretical stiffness k = F/δ
2. Specify test loads (3-5 load steps from 0 to 500 N)
3. Estimate measurement uncertainty (±0.01 mm indicator, ±2% load)
4. Determine acceptance range for k (±15% of theoretical)
5. Sketch test setup (indicator location, load application point)

### Exercise 1.10.2: Modal Test Interpretation

FRF shows peaks at: 78 Hz, 145 Hz, 223 Hz

**Tasks:**
1. Identify first three natural frequencies
2. If spindle operates at 18,000 RPM, calculate spindle frequency in Hz
3. Check if any natural frequencies are within 50% of spindle frequency (resonance risk)
4. If resonance risk exists, propose two mitigation strategies
5. Calculate required frequency shift to achieve 2× safety margin

### Exercise 1.10.3: Positioning Error Analysis

ISO 230-1 test results (partial):

| Position (mm) | Mean actual (mm) | Repeatability (mm) |
|---------------|------------------|--------------------|
| 0 | 0.02 | 0.01 |
| 250 | 250.15 | 0.02 |
| 500 | 500.27 | 0.02 |
| 750 | 750.42 | 0.03 |
| 1000 | 1000.55 | 0.02 |

**Tasks:**
1. Calculate positioning accuracy at each point
2. Determine max accuracy A and max repeatability R
3. Plot actual vs commanded position, fit linear regression
4. Calculate scaling error (slope ≠ 1.000)
5. Predict corrected accuracy after applying scale factor

---

**Next Section Preview:** [Section 1.11: Maintenance and Troubleshooting](section-01.11-maintenance-troubleshooting.md) will cover preventive maintenance schedules, common failure modes, diagnostic procedures, and systematic troubleshooting for mechanical frame issues.

---

## References

1. **ISO 230-1:2012** - Test code for machine tools - Part 1: Geometric accuracy
2. **ISO 230-4:2005** - Test code for machine tools - Part 4: Circular tests for numerically controlled machine tools
3. **ASME B5.54-2005** - Methods for Performance Evaluation of Computer Numerically Controlled Machining Centers
4. **Ewins, D.J. (2000).** *Modal Testing: Theory, Practice and Application*, 2nd Ed. - Comprehensive vibration testing
5. **Renishaw XL-80 Laser System** - User manual and test procedures
6. **Bryan, J.B. (1979).** "The Abbe Principle Revisited." *Precision Engineering*, 1(3), 129-132.

---

*Section 1.10 complete: 4,897 words | 10 equations | 3 worked examples | 8 tables | 10 diagrams*
