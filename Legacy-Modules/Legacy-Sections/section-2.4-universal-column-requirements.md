# Module 2 – Vertical Axis and Column Assembly

## 4. Universal Column Requirements

This section establishes the comprehensive design requirements that any precision vertical axis column must satisfy, regardless of specific application. These requirements represent industry best practices derived from decades of machine tool engineering and precision manufacturing experience.

### 4.1 Cross-Section: High Second Moment of Area

**Requirement:**
The column cross-section must provide sufficient second moment of area (area moment of inertia) to limit deflection under maximum anticipated cutting forces while maintaining reasonable mass and cost.

**Engineering Specification:**

For precision CNC applications (plasma, laser, light milling):

$$I_{min} = \frac{F_{max} L^3}{3 E \delta_{allowable}}$$

Where typical values:
- $F_{max}$ = 300-800 N (conservative cutting force estimate)
- $L$ = cantilever length (300-500 mm typical)
- $E$ = 200 GPa (steel) or 69 GPa (aluminum)
- $\delta_{allowable}$ = $L$/10,000 to $L$/20,000

**Example Implementation: 150 × 150 × 8 mm Steel Tube with Internal Ribs**

**Base Tube Properties:**

External dimensions: 150 mm × 150 mm
Wall thickness: 8 mm
Internal dimension: 134 mm × 134 mm

$$I_{base} = \frac{b h^3}{12} - \frac{(b-2t)(h-2t)^3}{12}$$

$$I_{base} = \frac{150 \times 150^3}{12} - \frac{134 \times 134^3}{12}$$

$$I_{base} = 42.19 \times 10^6 - 26.99 \times 10^6 = 15.20 \times 10^6 \text{ mm}^4$$

**Internal Rib Configuration:**

Add four longitudinal ribs, 6 mm thick, running full column length:
- Position: At 45° to primary axes (diagonal corners)
- Height: 60 mm (from internal wall toward center)
- Effective area contribution: $4 \times (6 \times 60) = 1440$ mm²

Approximate increase in moment of inertia from ribs:
$$\Delta I \approx A_{ribs} \times d_{centroid}^2$$

Where $d_{centroid} \approx 42$ mm (distance from neutral axis to rib centroid)

$$\Delta I \approx 1440 \times 42^2 = 2.54 \times 10^6 \text{ mm}^4$$

**Total moment of inertia:**
$$I_{total} = 15.20 \times 10^6 + 2.54 \times 10^6 = 17.74 \times 10^6 \text{ mm}^4$$

**Mass Analysis:**

Base tube mass per meter:
$$m_{tube} = \rho \times A_{cross} = 7850 \times (150^2 - 134^2) = 7850 \times 4564 = 35.8 \text{ kg/m}$$

Rib mass per meter:
$$m_{ribs} = 7850 \times 1440 \times 10^{-6} = 11.3 \text{ kg/m}$$

Total: 47.1 kg/m

For 500 mm column: $m = 23.6$ kg (manageable for base-mounted structure)

**Performance Verification:**

For 500 N cutting force, 400 mm cantilever:

$$\delta = \frac{500 \times 0.4^3}{3 \times 200 \times 10^9 \times 17.74 \times 10^{-6}}$$

$$\delta = \frac{32}{10.64 \times 10^6} = 3.0 \times 10^{-6} \text{ m} = 0.003 \text{ mm} = 3 \text{ μm}$$

**Result:** 3 μm deflection at 500 N load (excellent stiffness)

**Design Trade-offs:**

| Column Type | I (×10⁶ mm⁴) | Mass (kg/m) | Cost | Best Application |
|-------------|--------------|-------------|------|------------------|
| 100×100×6 plain | 3.35 | 18.5 | \$ | Light-duty, 3D printing |
| 120×120×8 plain | 7.05 | 28.3 | \$\$ | Medium-duty, laser cutting |
| 150×150×8 plain | 15.20 | 35.8 | \$\$\$ | Heavy plasma, light milling |
| 150×150×8 + ribs | 17.74 | 47.1 | \$\$\$\$ | Precision milling, high forces |
| Cast iron custom | 20-30 | 60-80 | \$\$\$\$\$ | Ultra-precision, damped |

### 4.2 Guide Spacing: Wide Relative to Column Depth

**Requirement:**
Linear rail guides must be spaced as widely as practical to maximize the moment arm resisting pitch and yaw rotations of the carriage.

**Engineering Rationale:**

The moment stiffness about the pitch axis is:

$$k_{moment} = k_{rail} \times d_{spacing}^2$$

Where:
- $k_{rail}$ = individual rail stiffness (N/mm)
- $d_{spacing}$ = center-to-center distance between rails (mm)

**Key Insight:** Moment stiffness scales with the *square* of spacing distance. Doubling rail spacing quadruples moment stiffness!

**Example Implementation: Rails 120 mm Apart**

**Given:**
- HGR20 rails, medium preload (ZA)
- Single rail stiffness: $k_{rail} = 450$ N/μm = $4.5 \times 10^8$ N/m
- Rail spacing: $d = 120$ mm = 0.12 m

**Calculate moment stiffness:**

$$k_M = 4.5 \times 10^8 \times 0.12^2 = 6.48 \times 10^6 \text{ N·m/rad}$$

**Applied moment from cutting force:**

Cutting force: $F = 400$ N
Moment arm from rail centerline to tool: $L = 150$ mm

$$M = 400 \times 0.15 = 60 \text{ N·m}$$

**Angular deflection:**

$$\theta = \frac{M}{k_M} = \frac{60}{6.48 \times 10^6} = 9.26 \times 10^{-6} \text{ rad}$$

**Linear deflection at tool tip (150 mm from rails):**

$$\delta_{angular} = \theta \times L = 9.26 \times 10^{-6} \times 0.15 = 1.39 \text{ μm}$$

**Result:** < 1.5 μm angular deflection contribution (excellent)

**Comparison with Narrow Spacing:**

If rails were only 80 mm apart:

$$k_M = 4.5 \times 10^8 \times 0.08^2 = 2.88 \times 10^6 \text{ N·m/rad}$$

$$\theta = \frac{60}{2.88 \times 10^6} = 20.8 \times 10^{-6} \text{ rad}$$

$$\delta_{angular} = 20.8 \times 10^{-6} \times 0.15 = 3.12 \text{ μm}$$

**Impact:** Narrow spacing causes 2.24× greater angular deflection (3.12 μm vs 1.39 μm)

**Design Rules:**

$$d_{spacing} \geq 0.6 \times column\_width$$ (minimum acceptable)

$$d_{spacing} \geq 0.8 \times column\_width$$ (preferred design)

For 150 mm column:
- Minimum spacing: $0.6 \times 150 = 90$ mm
- Preferred spacing: $0.8 \times 150 = 120$ mm

**Practical Constraints:**

- Column internal clearance (cable routing, gas spring)
- Carriage width (must mount both rails + central components)
- Bearing block mounting screw clearance
- Future modifications (additional sensors, probes)

**Recommended Practice:** Position rails at 75-85% of column width, measured center-to-center.

### 4.3 Screw Alignment: Parallel to Rail Datum ≤ 0.03 mm

**Requirement:**
The ball-screw axis must be parallel to the linear rail datum within 0.03 mm over the full travel length to prevent binding, premature wear, and positioning errors.

**Engineering Impact of Misalignment:**

**Case 1: Perfect Alignment**
- Ball nut travels smoothly along screw
- Uniform preload across all ball circuits
- Minimal friction variation
- Predictable servo performance

**Case 2: Misalignment of 0.05 mm over 200 mm**
- Effective angular error: $\alpha = \arctan(0.05/200) = 0.25$ mrad
- Varying preload (high on one side, low on other)
- Increased friction at maximum misalignment points
- Potential ball skidding and premature failure

**Alignment Measurement Procedure:**

**Equipment Required:**
- Dial indicator with 0.001 mm resolution
- Magnetic base with height adjustment
- Precision height gauge or surface plate
- Mandrel or alignment bar (fits snugly in ball nut bore)

**Procedure:**

1. **Install ball-screw with bearings properly preloaded**
   - Torque bearing lock nuts to specification
   - Verify axial preload (typically 50-200 N)

2. **Install alignment mandrel in ball nut**
   - Mandrel diameter should be H6 tolerance fit
   - Length minimum 100 mm for stability

3. **Mount dial indicator to column structure**
   - Position indicator tip against mandrel surface
   - Indicator axis perpendicular to screw axis

4. **Rotate screw to multiple angular positions**
   - Take readings at 0°, 90°, 180°, 270°
   - Record maximum TIR (Total Indicated Runout)

5. **Traverse carriage along full stroke**
   - Take readings every 50 mm
   - Plot deviation vs. position

**Acceptance Criteria:**

- TIR at any position: ≤ 0.015 mm
- Maximum deviation from straight line: ≤ 0.03 mm over full travel
- No monotonic trend (indicates systematic tilt)

**Example Implementation: Machined or Shimmed Mounting Pads**

**Method 1: Machined Mounting Surface (Precision Approach)**

1. Mount rails to column with dowel pins for repeatability
2. Use rails as machining datum
3. Install column on precision grinding machine
4. Machine screw bearing mounting pads parallel to rail datum
5. Tolerance: ±0.01 mm parallelism

**Cost:** High (requires precision grinding)
**Accuracy:** ±0.01 mm achievable
**Best for:** Production machines, multiple units

**Method 2: Shim-Adjusted Mounting (Practical Approach)**

1. Install rails with basic alignment
2. Mount screw bearings with adjustable shims
3. Use shim stock in 0.025, 0.05, 0.10, 0.25 mm thicknesses
4. Measure alignment with dial indicator
5. Add/remove shims iteratively to achieve parallelism

**Shim Calculation:**

If indicator shows 0.08 mm deviation over 250 mm span:
- Required shim at one end: 0.08 mm
- Use: One 0.05 mm + one 0.025 mm shim

Re-measure and iterate.

**Cost:** Low (shim stock ~$20)
**Accuracy:** ±0.02-0.03 mm with patience
**Best for:** Prototype machines, single units

**Method 3: Slotted Mounting Holes (Design Solution)**

Provide slotted mounting holes in bearing mounts:
- Slot length: ±1.0 mm adjustment range
- Slot perpendicular to desired motion
- Use hardened washers under mounting bolts
- Tighten with calibrated torque wrench

**Adjustment Procedure:**
1. Loosely mount bearing
2. Adjust position while monitoring dial indicator
3. Tighten mounting bolts incrementally (star pattern)
4. Re-verify alignment after tightening
5. Apply thread-locking compound if specified

### 4.4 Counterbalance: Force Within ±10% of Head Weight

**Requirement:**
The counterbalance system must provide upward force equal to 100-110% of the combined weight of all vertically moving components, adjustable to ±10% tolerance.

**Weight Calculation:**

Sum all moving components:

**Example Z-Axis Assembly:**

| Component | Mass (kg) | Notes |
|-----------|----------|-------|
| Spindle motor | 2.5 | AC servo or air-cooled spindle |
| Spindle mounting bracket | 0.4 | Aluminum plate |
| Torch/tool holder | 0.3 | Plasma torch assembly |
| Linear rail carriages (2) | 0.6 | HGR20 bearing blocks |
| Carriage plate | 0.8 | Aluminum, 8 mm thick |
| Ball nut assembly | 0.3 | With mounting bracket |
| Cable carrier chain | 0.2 | Moving section only |
| Fasteners & misc | 0.1 | Bolts, locating pins |
| **Total moving mass** | **5.2 kg** | |

**Required counterbalance force:**

$$F_{req} = m \times g = 5.2 \times 9.81 = 51.0 \text{ N}$$

**Design target:** 51-56 N (100-110% of weight)

**Rationale for Slight Overbalance:**

Setting counterbalance to 105% (53.5 N) compensates for:
1. Friction in linear guides (~2-4% of load)
2. Cable carrier drag force (~1-2% of weight)
3. Ball-screw preload friction (~1-3% of load)

Net result: Balanced motor current for upward and downward motion.

**Example Implementation: Two 250 N Gas Springs**

**Gas Spring Selection:**

- Individual spring force: 250 N at 60% compression
- Quantity: 2 (for symmetric loading)
- Total installed force: 500 N

**Operating Point Adjustment:**

Compress springs to 10.2% of stroke:
$$F_{actual} = 250 \times 2 \times 0.102 = 51.0 \text{ N}$$ ✓

**Mounting Geometry:**

Position gas springs at 45° angle from vertical:
- Vertical force component: $F_v = F_{spring} \times \cos(45°) = F_{spring} \times 0.707$
- Required spring force: $F_{spring} = 51.0 / 0.707 = 72.1$ N (per spring pair)

**Adjustment Procedure:**

1. Remove spindle and tooling (lighten carriage)
2. Connect force gauge to carriage mounting point
3. Pull upward and measure force required for constant-velocity motion
4. Pull downward and measure force
5. Calculate difference: $\Delta F = F_{up} - F_{down}$
6. Adjust gas spring compression or pressure to minimize $\Delta F$
7. Target: $\Delta F < 10$ N (represents <10% imbalance)

**Fine-Tuning with Gas Spring Pressure:**

Most gas springs have a fill valve allowing pressure adjustment:

$$F = P \times A$$

Where:
- $P$ = internal pressure (bar or psi)
- $A$ = piston area (cm²)

For Ø10 mm piston:
$$A = \pi \times 0.5^2 = 0.785 \text{ cm}^2$$

To increase force by 5 N:
$$\Delta P = \frac{5}{0.785} = 6.37 \text{ N/cm}^2 = 0.637 \text{ bar} = 9.2 \text{ psi}$$

Use nitrogen fill kit to add precise pressure increments.

**Verification Test:**

After adjustment:
1. Enable servo drive
2. Command constant-velocity moves (e.g., 50 mm/min)
3. Monitor motor current in both directions
4. Calculate: $Current_{imbalance} = \frac{I_{up} - I_{down}}{I_{avg}} \times 100\%$
5. Target: < 10% current variation

### 4.5 Natural Frequency: ≥ 5× Servo Bandwidth (>150 Hz)

**Requirement:**
The first structural natural frequency must exceed five times the servo control bandwidth to prevent control-structure interaction and ensure stable, repeatable motion.

**Engineering Basis:**

Servo controllers generate command signals with frequency content extending to approximately 5× the specified bandwidth. If structural resonance exists within this range, the controller couples energy into the vibration mode, causing:
- Limit cycle oscillations (sustained ringing)
- Position overshoot and settling time increase
- Audible noise and vibration
- Accelerated component wear
- Potential instability

**Example Implementation: 1st Mode ≈ 180 Hz (FEA Verified)**

**Finite Element Analysis Procedure:**

1. **Create CAD Model:**
   - Full column geometry (including internal ribs)
   - Moving carriage and spindle (as point mass or simplified geometry)
   - Constraint points (base mounting)

2. **Define Material Properties:**
   - Steel: E = 200 GPa, ν = 0.3, ρ = 7850 kg/m³
   - Aluminum: E = 69 GPa, ν = 0.33, ρ = 2700 kg/m³

3. **Apply Boundary Conditions:**
   - Fixed constraint at column base (all DOF = 0)
   - Moving mass at carriage location (representing spindle)

4. **Mesh Generation:**
   - Element size: 5-10 mm for structural members
   - Refine to 2-3 mm at stress concentrations
   - Minimum 3 elements through wall thickness

5. **Modal Analysis:**
   - Extract first 10 modes
   - Frequency range: 0-500 Hz
   - Identify mode shapes (bending, torsion, local)

**Typical Mode Identification:**

| Mode | Frequency (Hz) | Mode Shape | Concern Level |
|------|----------------|------------|---------------|
| 1 | 180 | Cantilever bending (X-axis) | PRIMARY |
| 2 | 185 | Cantilever bending (Y-axis) | PRIMARY |
| 3 | 290 | Column torsion | SECONDARY |
| 4 | 350 | Carriage plate bending | LOW |
| 5 | 420 | Local rail mounting | LOW |

**Servo Bandwidth Check:**

For 30 Hz servo bandwidth:
$$\frac{f_1}{f_{servo}} = \frac{180}{30} = 6.0$$ ✓ (exceeds minimum 5×)

For 40 Hz servo bandwidth:
$$\frac{f_1}{f_{servo}} = \frac{180}{40} = 4.5$$ ✗ (below minimum 5×)

**Design Action:** Limit servo bandwidth to 36 Hz maximum, or stiffen structure to raise $f_1$ above 200 Hz.

**Experimental Verification:**

After physical assembly, verify FEA predictions using accelerometer testing:

**Equipment:**
- Tri-axial piezoelectric accelerometer
- Data acquisition system (minimum 2 kHz sampling rate)
- Impact hammer (instrumented)
- FFT analysis software

**Procedure:**
1. Mount accelerometer to carriage (near center of mass)
2. Strike column structure with impact hammer
3. Record time-domain acceleration response
4. Perform FFT to convert to frequency domain
5. Identify peaks in frequency spectrum
6. Compare measured frequencies to FEA predictions

**Acceptance Criteria:**
- Measured $f_1$ within ±10% of FEA prediction
- Damping ratio ξ > 0.01 (steel) or ξ > 0.02 (cast iron)
- No unexpected low-frequency modes below 100 Hz

**If Results Inadequate:**

Structural modifications to increase natural frequency:

1. **Increase column section:**
   - 120×120 → 150×150 mm (≈ +70% in I)
   - Expected frequency increase: $\sqrt{1.70} = 1.30$ → +30%

2. **Add internal stiffeners:**
   - Longitudinal ribs + transverse bulkheads
   - Expected frequency increase: +15-25%

3. **Reduce moving mass:**
   - Lighter spindle motor
   - Aluminum carriage components
   - Expected frequency increase: $1/\sqrt{m_{ratio}}$

4. **Add damping treatment:**
   - Constrained-layer damping on column walls
   - Does not increase frequency, but increases damping ratio
   - Reduces resonance amplitude by 50-70%

### 4.6 Access: Replace Guides, Adjust Preload

**Requirement:**
The column design must provide practical access for:
1. Linear rail replacement (without disturbing column structure)
2. Bearing preload adjustment (periodic maintenance)
3. Ball-screw lubrication (service intervals)
4. Position encoder access (calibration and replacement)

**Example Implementation: Removable Rear Cover, Jack-Screw Mount**

**Removable Rear Cover Design:**

**Configuration:**
- Column has U-shaped cross-section (three sides welded/structural)
- Fourth side (rear) is bolted cover plate
- Cover plate material: 6 mm aluminum or steel
- Mounting: 8-12 socket head cap screws (M6 or M8)
- Gasket: 1 mm neoprene for dust sealing

**Access Provided:**
- Full-length view of linear rail backsides
- Ball-screw assembly visible
- Cable carrier routing inspection
- Internal column structure

**Manufacturing Considerations:**
- Cover plate machined flat within 0.1 mm
- Threaded inserts in column structure (not tapped directly)
- Dowel pins (2) for repeatable cover alignment
- Captive screws (optional) to prevent loss during service

**Jack-Screw Mount for Bearing Preload Adjustment:**

**Design:**
- Linear rail carriage mounting uses jack-screws for preload adjustment
- Four jack-screws per rail (two per carriage)
- Thread: M6 × 1.0 mm (6 threads/mm)
- Rotation 1 turn = 0.167 mm vertical adjustment

**Preload Adjustment Procedure:**

1. **Loosen primary mounting bolts (4 per carriage)**
   - Torque reduction to 50% (bolts just snug)

2. **Turn jack-screws to adjust vertical position**
   - Clockwise: Increase preload (more interference)
   - Counterclockwise: Decrease preload (less interference)
   - Adjust in small increments: 1/8 to 1/4 turn

3. **Measure carriage drag force**
   - Disconnect motor/screw drive
   - Use spring scale to measure force for constant-velocity motion
   - Target: 2-5% of rated dynamic load (manufacturer specification)

4. **Tighten primary mounting bolts**
   - Torque to specification (typically 8-12 Nm for M6)
   - Tighten in star pattern to prevent distortion
   - Re-measure drag force after tightening

5. **Lock jack-screws**
   - Apply thread-locking compound (medium strength)
   - Or use lock nuts if design provides clearance

**Preload Targets:**

| Rail Size | Dynamic Load Rating C (kN) | Target Preload F₀ (N) | Drag Force (N) |
|-----------|---------------------------|------------------------|----------------|
| MGN12 | 1.7 | 68-136 | 3-7 |
| MGN15 | 2.8 | 112-224 | 6-11 |
| HGR20 | 4.8 | 192-384 | 10-19 |
| HGR25 | 7.3 | 292-584 | 15-29 |

**Guideline:** Preload = 4-8% of C (light preload = 4%, heavy preload = 8%)

**Tool Access Requirements:**

Design clearances around service points:

| Component | Tool Required | Clearance Needed |
|-----------|---------------|------------------|
| Bearing preload jack-screw | 3 mm hex key | Ø10 mm × 50 mm deep |
| Rail mounting bolts | 5 mm hex key | Ø10 mm × 30 mm deep |
| Ball-screw grease fitting | Grease gun with coupler | Ø25 mm × 60 mm clearance |
| Motor mounting bolts | 6 mm hex key or 10 mm socket | Ø15 mm × 40 mm deep |
| Encoder adjustment | Small screwdriver | 8 mm × 100 mm access slot |

**Design Check:** Ensure all service tools can be inserted and operated without removing other components!

***

## 4.7 Universal Requirements Summary Table

| Feature | Universal Requirement | Implementation Example | Verification Method | Acceptance Criterion |
|---------|----------------------|----------------------|-------------------|---------------------|
| **Cross Section** | High second moment of area | 150×150×8 mm steel tube with internal ribs | Deflection test with 500 N load | δ ≤ 0.005 mm |
| **Guide Spacing** | Wide relative to column depth | Rails 120 mm apart (0.8× column width) | Moment stiffness calculation | $k_M$ ≥ 5×10⁶ N·m/rad |
| **Screw Alignment** | Parallel to rail datum ≤ 0.03 mm | Machined or shimmed mounting pads | Dial indicator sweep test | TIR ≤ 0.03 mm over travel |
| **Counterbalance** | Force within ±10% of head weight | Two 250 N gas springs, adjustable | Motor current balance test | $|I_{up} - I_{down}|/I_{avg}$ < 10% |
| **Natural Frequency** | ≥ 5× servo bandwidth (>150 Hz) | 1st mode ≈ 180 Hz (FEA verified) | Accelerometer impact testing | $f_1/f_{servo}$ ≥ 5.0 |
| **Access** | Replace guides, adjust preload | Removable rear cover, jack-screw mount | Functional service simulation | 30-minute rail replacement |

**Design Validation Checklist:**

Before finalizing vertical axis design:

- [ ] Calculate required moment of inertia for deflection spec
- [ ] Select column section with 2-3× safety factor
- [ ] Verify natural frequency exceeds 5× servo bandwidth
- [ ] Confirm ball-screw critical speed > 1.5× max operating speed
- [ ] Design counterbalance for 100-110% of moving mass
- [ ] Position rails at 75-85% of column width
- [ ] Provide alignment adjustment provisions (shims or slots)
- [ ] Include access covers for maintenance
- [ ] Document preload adjustment procedure
- [ ] Create service manual with torque specifications

This comprehensive requirements framework ensures any vertical axis design will deliver precision, reliability, and maintainability across its operational lifetime.

***


---

## References

1. **ISO 230-1:2012** - Test code for machine tools - Geometric accuracy
2. **ISO 10791-2:2001** - Test conditions for machining centres - Geometric tests for vertical or universal machines with horizontal spindle
3. **ANSI/ASME B5.54-2005** - Methods for Performance Evaluation of CNC Machining Centers
4. **Slocum, A.H. (1992).** *Precision Machine Design*. SME
5. **Weck, M. & Brecher, C. (2006).** *Machine Tools 1*. Springer
6. **VDI/DGQ 3441:1982** - Statistical Testing of Machine Tool Accuracy
