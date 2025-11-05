# Section 9.2 - Robot Architecture: Structural Design and Kinematic Analysis

## 9.2.1 Cartesian (Gantry) Robot Architecture

### Structural Configuration

Cartesian robots employ three orthogonal linear axes (X, Y, Z) arranged in portal/gantry configuration—horizontal X-Y platform spans workspace, vertical Z-axis carries end-effector. This architecture provides rectangular workspace with 1:1 correspondence between commanded coordinates and physical motion (no kinematic transformation).

**Common Configurations:**

1. **Portal/Gantry:** X-axis beam spans Y-axis rails elevated above work surface (clearance for parts/fixtures)
2. **Cantilever:** X-axis extends from one Y-axis rail (asymmetric loading, lower cost)
3. **Ceiling-mounted:** Inverted gantry suspends from overhead structure (maximizes floor space)

### Forward Kinematics

Direct mapping from joint space to Cartesian space:

$$\mathbf{P}_{tool} = \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} d_X \\ d_Y \\ d_Z \end{bmatrix} + \mathbf{P}_{tool\_offset}$$

where $d_X$, $d_Y$, $d_Z$ are motor encoder positions (converted to linear displacement via pitch: $d = N_{counts} \times \frac{pitch}{encoder\_resolution}$).

**No inverse kinematics required**—target Cartesian position directly commands motor positions.

### Structural Analysis: Beam Deflection

X-axis beam deflection limits payload and affects positioning accuracy. For simply-supported beam with center load:

$$\delta_{max} = \frac{W L^3}{48 E I}$$

where:
- $W$ = total load (payload + Z-axis + end-effector), N
- $L$ = beam span (X-axis travel + 2 × overhang), m
- $E$ = Young's modulus (aluminum 6061-T6: 69 GPa, steel: 200 GPa)
- $I$ = second moment of area (beam cross-section), m⁴

**Example Calculation:**

For 1,200 mm span aluminum extrusion beam (80×80 mm, $I = 2.1 \times 10^{-6}$ m⁴) carrying 15 kg load:

$$\delta = \frac{15 \times 9.81 \times 1.2^3}{48 \times 69 \times 10^9 \times 2.1 \times 10^{-6}} = \frac{2,545}{6.94 \times 10^6} = 0.37 \text{ mm}$$

**Design guideline:** Deflection < 0.5 mm for ±0.05 mm repeatability (deflection contributes ~50% of positioning error budget).

**Mitigation strategies:**
- Increase beam section modulus (larger extrusion: 100×100 mm → $\delta$ reduces 60%)
- Add intermediate support at mid-span (reduces effective $L$ by 2×, deflection by 8×)
- Use steel or carbon fiber beam (higher $E$)

### Natural Frequency Analysis

Gantry structure must avoid resonance with motor excitation frequencies (stepper: 50-500 Hz, servo: 100-2,000 Hz). First bending mode natural frequency:

$$f_n = \frac{\lambda_n^2}{2\pi L^2} \sqrt{\frac{EI}{m}}$$

where $\lambda_1 = 3.516$ for simply-supported beam, $m$ = mass per unit length (kg/m).

**Target:** $f_n > 50$ Hz (ensures 10:1 margin below typical stepper resonance range).

For aluminum beam ($m = 2.7$ kg/m, parameters from deflection example):

$$f_n = \frac{3.516^2}{2\pi \times 1.2^2} \sqrt{\frac{69 \times 10^9 \times 2.1 \times 10^{-6}}{2.7}} = 64 \text{ Hz}$$

Acceptable for stepper-driven system; servo-driven requires $f_n > 100$ Hz (requires stiffer/lighter beam).

### Linear Motion System Selection

| Component | Type | Typical Specification | Application |
|-----------|------|----------------------|-------------|
| **X-axis (long span)** | Belt drive (GT3) | Span 1-6 m, speed 5-10 m/s | Fast travel, moderate precision |
| **Y-axis (medium span)** | Ball screw (C5) | Span 0.5-2 m, pitch 10-20 mm | High precision, backlash <0.01 mm |
| **Z-axis (vertical)** | Ball screw + counterbalance | Stroke 200-500 mm, pitch 5-10 mm | Precision positioning against gravity |
| **Linear guides** | HGR15-25 | Preload: medium, clearance <5 μm | X-Y-Z axes (rail size scales with span) |

**Belt drive sizing example (X-axis):**

For 3 m/s maximum speed, 5 m/s² acceleration, 20 kg moving mass:

- Required motor torque: $T = \frac{F \times r}{i}$ where $F = ma = 20 \times 5 = 100$ N, $r = \frac{pitch}{2\pi}$ (pulley radius), $i$ = gear ratio
- Using 20-tooth GT3 pulley (pitch 3 mm): $r = \frac{20 \times 3}{2\pi} = 9.55$ mm = 0.00955 m
- Motor torque (direct drive, $i=1$): $T = 100 \times 0.00955 = 0.955$ N⋅m
- Select NEMA 34 stepper (3 N⋅m holding torque) → 3:1 safety factor

## 9.2.2 SCARA Robot Architecture

### Kinematic Configuration

SCARA (Selective Compliance Assembly Robot Arm) employs two revolute joints (shoulder $\theta_1$, elbow $\theta_2$) in horizontal plane plus prismatic Z-axis. "Selective compliance" refers to rigid vertical axis (high stiffness for insertion tasks) with compliant horizontal plane (absorbs lateral misalignment).

### Forward Kinematics

End-effector position from joint angles:

$$\begin{align}
x &= L_1 \cos\theta_1 + L_2 \cos(\theta_1 + \theta_2) \\
y &= L_1 \sin\theta_1 + L_2 \sin(\theta_1 + \theta_2) \\
z &= d_Z
\end{align}$$

where $L_1$ = proximal link length (shoulder to elbow), $L_2$ = distal link length (elbow to wrist).

### Inverse Kinematics

Given target $(x, y)$, solve for joint angles using law of cosines:

$$\cos\theta_2 = \frac{x^2 + y^2 - L_1^2 - L_2^2}{2 L_1 L_2}$$

$$\theta_2 = \pm \arccos\left(\frac{x^2 + y^2 - L_1^2 - L_2^2}{2 L_1 L_2}\right)$$

Two solutions exist ("elbow-up" and "elbow-down"), typically select $\theta_2 > 0$ (elbow-up) to avoid workspace obstacles.

$$\theta_1 = \arctan\left(\frac{y}{x}\right) - \arctan\left(\frac{L_2 \sin\theta_2}{L_1 + L_2 \cos\theta_2}\right)$$

**Singularity conditions:**

1. **Full extension:** $\theta_2 = 0°$ → elbow locked, loss of one DOF (cannot move perpendicular to arm)
2. **Full retraction:** $\theta_2 = \pm180°$ → arms overlap, kinematic indeterminacy

**Workspace:** Annulus with outer radius $R_{max} = L_1 + L_2$ and inner radius $R_{min} = |L_1 - L_2|$.

### Joint Torque Analysis

Shoulder joint supports elbow link, payload, and end-effector; maximum torque at full extension:

$$\tau_{shoulder} = (m_{link2} \times L_1 + m_{payload} \times (L_1 + L_2)) \times g \times \cos\theta_1$$

**Example:** $L_1 = 400$ mm, $L_2 = 300$ mm, link mass 2 kg, payload 5 kg, horizontal configuration ($\theta_1 = 0°$):

$$\tau = (2 \times 0.4 + 5 \times 0.7) \times 9.81 \times 1 = (0.8 + 3.5) \times 9.81 = 42.2 \text{ N⋅m}$$

Select servo motor with continuous torque >50 N⋅m (includes 20% safety margin + dynamic acceleration torque).

### Harmonic Drive Gearboxes

SCARA joints commonly use harmonic (strain wave) gear reducers:

- **Ratio:** 50:1 to 100:1 typical
- **Backlash:** <1 arcmin (0.017°) enables ±0.01 mm repeatability at 500 mm radius
- **Efficiency:** 70-85% (vs. 90-95% planetary gears, but zero-backlash critical for precision)

**Torque calculation with gearbox:**

Required motor torque = $\frac{\tau_{load}}{i \times \eta}$ where $i$ = gear ratio, $\eta$ = efficiency

For 42.2 N⋅m load, 80:1 ratio, 75% efficiency:

$$\tau_{motor} = \frac{42.2}{80 \times 0.75} = 0.70 \text{ N⋅m}$$

Select 1 kW servo motor (rated 3.2 N⋅m @ 3,000 RPM) → adequate torque and speed.

### Z-Axis Counterbalance

Vertical axis lifts payload against gravity; counterbalance spring reduces motor torque:

$$F_{motor} = F_{payload} - F_{spring} = (m_{payload} + m_{end-effector}) \times g - k \times \Delta z$$

where $k$ = spring constant (N/mm), $\Delta z$ = compression from neutral position.

**Design goal:** Balance at mid-stroke → motor provides only acceleration forces, not gravity compensation.

For 5 kg payload, 200 mm stroke:

$$k = \frac{mg}{z_{stroke}/2} = \frac{5 \times 9.81}{0.1} = 490 \text{ N/m} = 0.49 \text{ N/mm}$$

Use two 0.25 N/mm springs in parallel (each 250 mm free length, 30 mm wire diameter).

## 9.2.3 Delta Robot Parallel Kinematic Architecture

### Structural Topology

Delta robot consists of three kinematic chains (120° radial symmetry) connecting fixed base to moving platform via parallelogram linkages. Each chain has one actuated revolute joint at base; parallelogram constrains platform orientation parallel to base (3-DOF: X, Y, Z translation).

**Link Nomenclature:**

- **Proximal arm:** Base motor shaft to upper parallelogram joint (200-400 mm carbon fiber tube)
- **Distal linkage:** Parallelogram structure maintaining parallel orientation (400-800 mm length)
- **Platform:** Triangular end-effector mount (50-150 mm triangle)

### Inverse Kinematics (Analytical Solution)

Given platform position $(x, y, z)$, compute motor angles $\theta_1$, $\theta_2$, $\theta_3$:

For each chain $i$, platform joint position:

$$\mathbf{P}_i = \begin{bmatrix} x \\ y \\ z \end{bmatrix} + R_i \begin{bmatrix} \cos\alpha_i \\ \sin\alpha_i \\ 0 \end{bmatrix}$$

where $R_i$ = platform radius, $\alpha_i = (i-1) \times 120°$ (radial position).

Proximal arm endpoint (motor shaft):

$$\mathbf{B}_i = \begin{bmatrix} R_b \cos\alpha_i \\ R_b \sin\alpha_i \\ 0 \end{bmatrix}$$

where $R_b$ = base radius.

Constraint: $|\mathbf{P}_i - \mathbf{B}_i - L_p \mathbf{u}_i| = L_d$ (distal link length), where $\mathbf{u}_i$ = proximal arm unit vector.

Solving yields:

$$\theta_i = 2 \arctan\left(\frac{-B \pm \sqrt{B^2 - 4AC}}{2A}\right)$$

where $A$, $B$, $C$ are geometric coefficients (expressions omitted for brevity; see Clavel 1988 for full derivation).

### Forward Kinematics (Numerical Solution Required)

Determining platform position from motor angles requires solving three simultaneous constraint equations (three spherical shells intersect at platform position). No closed-form solution exists; numerical methods (Newton-Raphson) converge in 3-5 iterations.

**Control implication:** Inverse kinematics computed rapidly in real-time (1-2 μs); forward kinematics used only for trajectory verification.

### Workspace Geometry

Platform workspace is intersection of three spherical shells (each centered on proximal arm endpoint):

$$\text{Workspace} = \bigcap_{i=1}^{3} \left\{ \mathbf{P} : R_{min,i} \leq |\mathbf{P} - \mathbf{B}_i| \leq R_{max,i} \right\}$$

Resulting shape: inverted cone or truncated ellipsoid.

**Typical dimensions:** For base radius 300 mm, platform radius 100 mm, proximal arm 200 mm, distal link 600 mm:

- Workspace diameter: 600-800 mm (at Z = -300 mm)
- Workspace height: 300-400 mm
- Volume: ~0.15 m³ (15% of robot installation envelope)

### Parallel Kinematic Advantages

1. **High acceleration:** Motors on fixed base (no moving motor mass) + parallel load distribution → 10-15 g achievable
2. **Accuracy amplification:** Motor errors divide across three chains (geometric averaging improves repeatability)
3. **High stiffness:** Closed kinematic loops provide structural rigidity (natural frequency 50-100 Hz vs. 20-40 Hz serial robots)

### Link Design for High-Speed Operation

Distal links experience 10-15 g centripetal acceleration; carbon fiber tubes minimize inertia:

**Material properties:**

- Carbon fiber/epoxy: Density 1,600 kg/m³, Young's modulus 140 GPa
- Aluminum 6061-T6: Density 2,700 kg/m³, Young's modulus 69 GPa

**Specific stiffness comparison:**

$$\frac{E}{\rho}_{carbon} = \frac{140 \times 10^9}{1600} = 87.5 \times 10^6 \text{ m}^2\text{/s}^2$$

$$\frac{E}{\rho}_{aluminum} = \frac{69 \times 10^9}{2700} = 25.6 \times 10^6 \text{ m}^2\text{/s}^2$$

Carbon fiber provides 3.4× higher specific stiffness → enables longer links with lower mass and higher natural frequency.

**Typical link:** OD 20 mm, ID 18 mm carbon tube, length 600 mm, mass 80 g (vs. 250 g aluminum)

## 9.2.4 Architecture Selection Framework

### Performance Trade-offs

| Characteristic | Cartesian | SCARA | Delta |
|----------------|-----------|-------|-------|
| **Workspace shape** | Rectangular | Annular cylinder | Inverted cone |
| **Workspace utilization** | 70-80% | 50-60% | 10-15% |
| **Positioning accuracy** | ±0.05 mm | ±0.02 mm | ±0.1-0.5 mm |
| **Maximum speed** | 5-10 m/s | 10-15 m/s | 15-25 m/s |
| **Payload capacity** | 50-100+ kg | 5-20 kg | 0.5-5 kg |
| **Structural complexity** | Low (3 linear axes) | Medium (2 rotary + 1 linear) | High (parallel kinematics) |
| **Programming complexity** | Low (Cartesian) | Medium (inverse kinematics) | High (calibration-sensitive) |
| **Cost** | $35k-80k | $50k-120k | $80k-250k |

### Application-Specific Recommendations

**Choose Cartesian when:**
- Large/irregular workspace required (>2 m³)
- Heavy payloads (>20 kg)
- Simple programming desired (Cartesian coordinates)
- CNC machine tending (extended reach, z-axis clearance)

**Choose SCARA when:**
- Compact floor space (overhead mounting)
- High speed required (50-150 picks/min)
- Precision assembly (<±0.02 mm)
- Electronics manufacturing (PCB handling, component placement)

**Choose Delta when:**
- Extreme speed critical (>200 picks/min)
- Lightweight parts (<2 kg)
- Overhead pick from conveyor
- Food/pharmaceutical packaging (washdown capability)

Mastery of robot architecture—Cartesian beam deflection analysis, SCARA inverse kinematics, Delta parallel workspace geometry—enables engineers to select optimal configuration for application requirements and design custom systems when commercial solutions inadequate.

***

---

## References

1. **Kinematics and Robotics**
   - Craig, J.J. (2017). *Introduction to Robotics: Mechanics and Control* (4th ed.). Pearson
   - Spong, M.W., Hutchinson, S., & Vidyasagar, M. (2020). *Robot Modeling and Control* (2nd ed.). Wiley
   - Angeles, J. (2007). *Fundamentals of Robotic Mechanical Systems*. Springer

2. **Delta Robot Design**
   - Clavel, R. (1988). "DELTA: A Fast Robot with Parallel Geometry". *18th International Symposium on Industrial Robots*
   - Pierrot, F., & Company, O. (1999). "H4: A New Family of 4-DOF Parallel Robots". *IEEE/ASME AIM*
   - Gosselin, C., & Angeles, J. (1988). "The Optimum Kinematic Design of a Planar Three-Degree-of-Freedom Parallel Manipulator". *Journal of Mechanisms, Transmissions, and Automation in Design*, 110(1), 35-41

3. **Structural Analysis**
   - Young, W.C., Budynas, R.G., & Sadegh, A.M. (2011). *Roark's Formulas for Stress and Strain* (8th ed.). McGraw-Hill
   - Timoshenko, S.P., & Gere, J.M. (2009). *Theory of Elastic Stability*. Dover Publications

4. **Mechanical Components**
   - THK Linear Motion Systems - Linear Guide Technical Catalog
   - HIWIN - Linear Guideway Technical Reference
   - Harmonic Drive LLC - Component Set Technical Data
   - ISO 281:2007 - Rolling bearings - Dynamic load ratings and rating life

5. **Material Properties**
   - ASM Metals Handbook - Aluminum Alloy Properties (6061-T6)
   - Matweb Material Property Database - www.matweb.com
   - Hexcel Carbon Fiber Composites - Technical datasheets
