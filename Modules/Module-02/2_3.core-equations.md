# Module 2 – Vertical Axis and Column Assembly

## 3. Core Equations for Column Behaviour

Understanding the mathematical relationships governing vertical axis structural behavior is essential for rational design decisions. This section derives and explains the fundamental equations that describe deflection, resonance, critical speeds, and servo stability requirements.

### 3.1 Cantilever Beam Deflection: The Foundation of Structural Design

**Physical Situation:**

The Z-axis column functions as a cantilever beam with:
- Fixed support at the base (machine bed or gantry)
- Free end carrying the moving carriage and tooling
- Concentrated load at the free end from cutting forces

**Fundamental Equation:**

For a cantilever beam with uniform cross-section, subjected to point load $F$ at distance $L$ from the fixed support:

$$\delta_B = \frac{F L^3}{3 E I}$$

**Derivation from Beam Theory:**

Starting with the moment-curvature relationship:
$$\frac{d^2 y}{dx^2} = \frac{M(x)}{E I}$$

For cantilever with tip load $F$, moment at distance $x$ from free end:
$$M(x) = -F x$$

Integrating once for slope:
$$\frac{dy}{dx} = \int \frac{-F x}{E I} dx = \frac{-F x^2}{2 E I} + C_1$$

Boundary condition at fixed end ($x=L$): $dy/dx = 0$
$$C_1 = \frac{F L^2}{2 E I}$$

Slope equation:
$$\frac{dy}{dx} = \frac{F}{2 E I}(L^2 - x^2)$$

Integrating for deflection:
$$y = \int \frac{F}{2 E I}(L^2 - x^2) dx = \frac{F}{2 E I}\left(L^2 x - \frac{x^3}{3}\right) + C_2$$

Boundary condition at fixed end ($x=L$): $y=0$
$$C_2 = -\frac{F}{2 E I}\left(L^3 - \frac{L^3}{3}\right) = -\frac{F L^3}{3 E I}$$

Deflection at free end ($x=0$):
$$\delta_B = y(0) = -\frac{F L^3}{3 E I}$$

The negative sign indicates downward deflection; taking absolute value:

$$\boxed{\delta_B = \frac{F L^3}{3 E I}}$$

**Design Form - Required Moment of Inertia:**

Rearranging to solve for the required structural property:

$$I_{req} = \frac{F L^3}{3 E \delta_{max}}$$

This is the primary design equation for column sizing.

**Worked Example 1: Plasma Cutting Column**

**Requirements:**
- Cantilever length: $L = 350$ mm (from column face to torch tip)
- Maximum cutting force: $F = 300$ N (conservative estimate)
- Material: Steel tube ($E = 200$ GPa)
- Allowable deflection: $\delta_{max} = 0.025$ mm (25 μm)

**Calculate required moment of inertia:**

$$I_{req} = \frac{300 \times 0.35^3}{3 \times 200 \times 10^9 \times 0.000025}$$

$$I_{req} = \frac{300 \times 0.042875}{15 \times 10^6} = \frac{12.8625}{15 \times 10^6}$$

$$I_{req} = 8.58 \times 10^{-7} \text{ m}^4 = 858,000 \text{ mm}^4$$

**Select appropriate section:**

For square RHS (hollow rectangular section), approximate formula for thin-walled section:

$$I = \frac{b h^3}{12} - \frac{(b-2t)(h-2t)^3}{12}$$

For square section ($b = h$):
$$I = \frac{b^4 - (b-2t)^4}{12}$$

**Trial section: 100×100×6 mm**

$$I = \frac{100^4 - 88^4}{12} = \frac{100,000,000 - 59,969,536}{12}$$

$$I = \frac{40,030,464}{12} = 3,335,872 \text{ mm}^4$$

**Verification:**
$$I_{actual} = 3.34 \times 10^6 \text{ mm}^4 > I_{req} = 8.58 \times 10^5 \text{ mm}^4$$

**Safety factor:** $SF = 3.34/0.858 = 3.9$ ✓ (adequate)

**Calculated deflection with selected section:**
$$\delta = \frac{300 \times 0.35^3}{3 \times 200 \times 10^9 \times 3.34 \times 10^{-6}}$$

$$\delta = \frac{12.86}{2.004 \times 10^6} = 6.4 \times 10^{-6} \text{ m} = 0.0064 \text{ mm} = 6.4 \text{ μm}$$

**Result:** Actual deflection is 6.4 μm, well below 25 μm limit. The safety factor of 3.9× provides margin for:
- Dynamic loading (impacts, rapid accelerations)
- Assembly tolerances
- Material property variations
- Thermal effects

**Worked Example 2: Milling Machine Column**

**Requirements:**
- Cantilever length: $L = 400$ mm
- Maximum cutting force: $F = 800$ N (heavy milling)
- Material: Cast iron ($E = 120$ GPa, higher damping than steel)
- Allowable deflection: $\delta_{max} = 0.015$ mm (15 μm, tighter tolerance)

**Calculate required moment of inertia:**

$$I_{req} = \frac{800 \times 0.4^3}{3 \times 120 \times 10^9 \times 0.000015}$$

$$I_{req} = \frac{51.2}{5.4 \times 10^6} = 9.48 \times 10^{-6} \text{ m}^4 = 9.48 \times 10^6 \text{ mm}^4$$

This requires a much larger section due to:
1. Higher cutting forces (800 N vs 300 N)
2. Longer cantilever (400 mm vs 350 mm)
3. Tighter deflection specification (15 μm vs 25 μm)
4. Lower material stiffness (cast iron vs steel)

**Selected section: 150×150×10 mm steel RHS with internal ribs**

$$I_{base} = \frac{150^4 - 130^4}{12} = 15.2 \times 10^6 \text{ mm}^4$$

Internal ribbing adds approximately 25% to effective I:
$$I_{total} \approx 19 \times 10^6 \text{ mm}^4$$

**Safety factor:** $SF = 19/9.48 = 2.0$ ✓ (acceptable for industrial application)

### 3.2 Natural (Resonant) Frequency: Dynamic Stability Analysis

**Physical Principle:**

Every structural system has natural frequencies at which it will vibrate with minimal damping. If external excitation (cutting forces, servo oscillations) occurs near a natural frequency, resonance amplifies vibrations, destroying positioning accuracy and potentially causing structural failure.

**Single-Degree-of-Freedom Model:**

The Z-axis column with moving carriage can be modeled as a spring-mass system:

$$f_n = \frac{1}{2\pi} \sqrt{\frac{k}{m}}$$

Where:
- $k$ = structural stiffness (N/m)
- $m$ = effective mass (kg)

**Cantilever Stiffness:**

From deflection equation $\delta = FL^3/(3EI)$, the spring constant is:

$$k = \frac{F}{\delta} = \frac{3 E I}{L^3}$$

**Natural Frequency of Cantilever with Tip Mass:**

$$f_n = \frac{1}{2\pi} \sqrt{\frac{3 E I}{m L^3}}$$

**Effective Mass Correction:**

For a cantilever with distributed mass $m_{beam}$ and tip mass $m_{tip}$, the effective mass is:

$$m_{eff} = m_{tip} + \alpha m_{beam}$$

Where $\alpha \approx 0.25$ for first-mode cantilever vibration (proven through modal analysis).

**Worked Example 3: Natural Frequency Calculation**

**Given:**
- Column: 120×120×8 mm steel RHS
- Length: $L = 450$ mm
- Moving mass (carriage + spindle): $m_{tip} = 7$ kg
- Column mass: $m_{beam} = 2.5$ kg/m × 0.45 m = 1.125 kg
- $E = 200$ GPa
- $I = 3.85 \times 10^{-6}$ m⁴

**Calculate effective mass:**
$$m_{eff} = 7 + 0.25 \times 1.125 = 7.28 \text{ kg}$$

**Calculate stiffness:**
$$k = \frac{3 \times 200 \times 10^9 \times 3.85 \times 10^{-6}}{0.45^3}$$

$$k = \frac{2.31 \times 10^6}{0.091125} = 25.35 \times 10^6 \text{ N/m}$$

**Calculate natural frequency:**
$$f_n = \frac{1}{2\pi} \sqrt{\frac{25.35 \times 10^6}{7.28}}$$

$$f_n = \frac{1}{6.283} \sqrt{3.482 \times 10^6} = \frac{1866}{6.283} = 297 \text{ Hz}$$

**Result:** First natural frequency is 297 Hz.

**Resonance Implications:**

If servo bandwidth is 30 Hz:
- Frequency ratio: $297 / 30 = 9.9$
- **Status:** ✓ Exceeds minimum 5× requirement (excellent design)

If servo bandwidth is 50 Hz:
- Frequency ratio: $297 / 50 = 5.9$
- **Status:** ✓ Meets minimum 5× requirement (acceptable)

If servo bandwidth is 70 Hz:
- Frequency ratio: $297 / 70 = 4.2$
- **Status:** ✗ Below minimum 5× requirement (resonance risk)

**Design Actions for Low-Frequency Structures:**

If calculated $f_n$ is insufficient:

1. **Increase structural stiffness:**
   - Larger cross-section (I increases with h³)
   - Add internal ribs/stiffeners
   - Use stiffer material (steel over aluminum)

2. **Reduce moving mass:**
   - Lighter spindle/tool assembly
   - Aluminum carriage components
   - Hollow-core designs

3. **Reduce cantilever length:**
   - Minimize tool offset from column
   - Compact carriage design

4. **Reduce servo bandwidth:**
   - Trade response speed for stability
   - Typical: Reduce from 50 Hz to 30 Hz

**Frequency vs. Stiffness Sensitivity:**

$$\frac{df_n}{f_n} = \frac{1}{2}\frac{dk}{k} - \frac{1}{2}\frac{dm}{m}$$

A 20% increase in stiffness → 9.5% increase in natural frequency
A 20% reduction in mass → 9.5% increase in natural frequency

**Priority:** Stiffness increases are more effective than mass reductions because:
- Stiffness scales with I (can increase dramatically with section size)
- Mass reduction limited by functional requirements

### 3.3 Ball-Screw Critical Speed: Rotational Stability Limit

**Physical Phenomenon:**

A rotating shaft (ball-screw) becomes dynamically unstable when rotational speed reaches the critical speed, at which lateral vibrations resonate with shaft rotation. This creates catastrophic whirling motion that can destroy bearings and damage the screw.

**Critical Speed Equation:**

$$n_{cr} = \frac{k_f \times 10^6 \times d_r}{L^2}$$

Where:
- $n_{cr}$ = critical rotational speed (rpm)
- $k_f$ = end-fixity factor (dimensionless)
- $d_r$ = root diameter of screw (mm)
- $L$ = unsupported length between bearings (mm)

**End-Fixity Factors:**

| Support Condition | $k_f$ | Description |
|-------------------|-------|-------------|
| Simply supported - simply supported | 3.14 | Both ends on radial bearings, free to rotate |
| Fixed - simply supported | 3.56 | One end clamped, one end on bearing |
| Fixed - fixed | 4.73 | Both ends rigidly clamped (rare) |
| Fixed - free (cantilever) | 0.56 | One end fixed, other end free (avoid!) |

**Common Configuration:** Fixed-supported (angular contact bearings at one end, radial bearing at other)
$$k_f = 3.56$$

**Worked Example 4: Critical Speed Analysis**

**Given:**
- Ball-screw: Ø20 mm, 5 mm pitch
- Root diameter: $d_r = 17.5$ mm
- Unsupported length: $L = 500$ mm
- Support: Fixed-supported ($k_f = 3.56$)

**Calculate critical speed:**

$$n_{cr} = \frac{3.56 \times 10^6 \times 17.5}{500^2}$$

$$n_{cr} = \frac{62.3 \times 10^6}{250,000} = 249 \text{ rpm}$$

**Maximum linear velocity:**

$$v_{max} = n_{cr} \times p = 249 \times 0.005 = 1.245 \text{ m/min} = 20.8 \text{ mm/s}$$

**Safety Factor Application:**

Industry practice: Operate at ≤ 80% of critical speed

$$n_{operating} = 0.8 \times 249 = 199 \text{ rpm}$$

$$v_{operating} = 199 \times 0.005 = 0.995 \text{ m/min} \approx 1.0 \text{ m/min}$$

**Design Decision:**
For applications requiring $v > 1$ m/min, this screw configuration is inadequate.

**Design Solutions for Higher Speeds:**

1. **Reduce unsupported length:**
   Add center bearing support to create two shorter spans.
   
   Example: 500 mm span → two 250 mm spans
   
   $$n_{cr,new} = \frac{3.56 \times 10^6 \times 17.5}{250^2} = 998 \text{ rpm}$$
   
   $$v_{max,new} = 998 \times 0.005 = 4.99 \text{ m/min}$$
   
   **Result:** 4× speed increase with center support bearing!

2. **Increase screw diameter:**
   Use Ø25 mm screw ($d_r = 22$ mm)
   
   $$n_{cr} = \frac{3.56 \times 10^6 \times 22}{500^2} = 314 \text{ rpm}$$
   
   26% speed increase, but increased cost and mass.

3. **Use preloaded screw:**
   Preloaded screws have effectively higher $k_f$ (≈ 4.0 vs 3.56)
   
   $$n_{cr} = \frac{4.0 \times 10^6 \times 17.5}{500^2} = 280 \text{ rpm}$$
   
   12% improvement.

4. **Switch to belt drive:**
   No critical speed limitation! Practical for rapid positioning axes where forces are moderate.

**Critical Speed vs. Application:**

| Application | Typical Speed | Screw Adequacy |
|-------------|---------------|----------------|
| Precision plasma THC | 0.5 m/min | ✓ Well within limits |
| Laser focal adjustment | 2-3 m/min | ⚠ May require center support |
| Rapid tool change positioning | 5-10 m/min | ✗ Belt drive recommended |
| Probing cycles | 0.1-0.2 m/min | ✓ No concerns |

### 3.4 Servo Resonance Criterion: Control-Structure Interaction

**Control Theory Principle:**

A servo control system with bandwidth $f_{servo}$ generates control signals with frequency content up to approximately $5 \times f_{servo}$. If any structural resonance exists within this range, the controller will excite the resonance, causing instability.

**Stability Criterion:**

$$f_n \geq 5 \times f_{servo}$$ (minimum requirement)

$$f_n \geq 10 \times f_{servo}$$ (preferred for robust control)

**Servo Bandwidth Definition:**

Servo bandwidth is the frequency at which the closed-loop gain drops to -3 dB (70.7% of DC gain). Higher bandwidth = faster response, but increased sensitivity to resonances.

**Typical Bandwidth Values:**

| Application | Servo Bandwidth | Required $f_n$ (5×) | Required $f_n$ (10×) |
|-------------|----------------|---------------------|---------------------|
| Positioning (slow) | 10 Hz | 50 Hz | 100 Hz |
| Standard machining | 30 Hz | 150 Hz | 300 Hz |
| High-speed machining | 50 Hz | 250 Hz | 500 Hz |
| Ultra-precision | 20 Hz | 100 Hz | 200 Hz |

**Worked Example 5: Servo Tuning for Structural Resonance**

**Given:**
- Measured natural frequency: $f_n = 180$ Hz (via accelerometer)
- Desired servo bandwidth: $f_{servo} = 40$ Hz
- Current configuration: PID controller

**Check stability criterion:**

$$\frac{f_n}{f_{servo}} = \frac{180}{40} = 4.5$$

**Result:** 4.5× ratio is below minimum 5× requirement (marginal stability).

**Design Options:**

**Option 1: Reduce Servo Bandwidth (Conservative)**

$$f_{servo,max} = \frac{f_n}{5} = \frac{180}{5} = 36 \text{ Hz}$$

- Reduce bandwidth from 40 Hz to 36 Hz (10% reduction)
- Trade-off: Slightly slower response, but guaranteed stability
- Implementation: Reduce proportional gain by 20%

**Option 2: Add Notch Filter (Sophisticated)**

Design notch filter centered at $f_n = 180$ Hz:

$$H(s) = \frac{s^2 + 2\zeta_z \omega_n s + \omega_n^2}{s^2 + 2\zeta_p \omega_n s + \omega_n^2}$$

Where:
- $\omega_n = 2\pi f_n = 1131$ rad/s
- $\zeta_z = 0.05$ (numerator damping - creates notch)
- $\zeta_p = 0.7$ (denominator damping - limits attenuation width)

This filter attenuates gain by 20-30 dB at 180 Hz while preserving performance at other frequencies.

- Advantage: Maintains 40 Hz bandwidth
- Disadvantage: Adds phase lag, requires tuning

**Option 3: Increase Structural Stiffness (Fundamental)**

Target: $f_n = 250$ Hz (provides 6.25× ratio at 40 Hz bandwidth)

Required stiffness increase:
$$\frac{f_{n,new}}{f_{n,old}} = \sqrt{\frac{k_{new}}{k_{old}}}$$

$$\frac{250}{180} = 1.39 = \sqrt{\frac{k_{new}}{k_{old}}}$$

$$\frac{k_{new}}{k_{old}} = 1.39^2 = 1.93$$

**Requirement:** Increase structural stiffness by 93%

**Approach:**
- Upgrade column from 100×100 to 120×120 mm (+73% in I)
- Add internal ribs (+20% effective stiffness)
- **Total:** 1.73 × 1.20 = 2.08× (meets requirement)

**Recommended Solution:**

For production machines: **Combination approach**
1. Increase structural stiffness to $f_n \geq 200$ Hz
2. Add notch filter for additional margin
3. Set servo bandwidth to 35-40 Hz
4. Verify stability with step response testing

**Verification Testing:**

After tuning, perform step response test:
1. Command 10 mm step input
2. Record position vs. time with high-resolution encoder
3. Measure:
   - Rise time (10%-90% of step)
   - Overshoot (should be < 10%)
   - Settling time (within ±0.01 mm)
   - Ringing frequency (should not match $f_n$)

**Acceptance Criteria:**
- Overshoot < 10%
- Settling time < 3 × rise time
- No sustained oscillations
- Position error < 0.02 mm after settling

***

## 3.5 Equation Integration: Holistic Design Process

The four core equations work together in the design process:

```
1. DEFLECTION → Size column cross-section for stiffness
              ↓
2. NATURAL FREQUENCY → Verify dynamic stability
              ↓
3. CRITICAL SPEED → Confirm ball-screw adequacy
              ↓
4. SERVO CRITERION → Validate control system compatibility
```

**Design Iteration Loop:**

```
Start with requirements (travel, forces, speed)
    ↓
Calculate required I (deflection equation)
    ↓
Select trial column section
    ↓
Calculate natural frequency
    ↓
    Check: f_n ≥ 5 × f_servo?
    ↓               ↓
   NO              YES
    ↓               ↓
Increase I    Calculate screw critical speed
    ↓               ↓
Iterate         Check: v_req ≤ 0.8 × v_critical?
                    ↓               ↓
                   NO              YES
                    ↓               ↓
           Add support bearing   DESIGN COMPLETE
           or use belt drive
```

All four equations must be satisfied simultaneously for a successful vertical axis design. This integrated approach ensures structural, dynamic, and control requirements are met without costly post-build modifications.

***


---

## References

1. **Young, W.C. & Budynas, R.G. (2011).** *Roark's Formulas for Stress and Strain* (8th ed.). McGraw-Hill
2. **Gere, J.M. & Timoshenko, S.P. (2012).** *Mechanics of Materials* (8th ed.). Cengage Learning
3. **Hibbeler, R.C. (2017).** *Structural Analysis* (10th ed.). Pearson
4. **Beer, F.P. et al. (2015).** *Mechanics of Materials* (7th ed.). McGraw-Hill
5. **ISO 11352:2012** - Cranes - Loading and stability calculations
6. **AISC Steel Construction Manual** (15th ed., 2017)
