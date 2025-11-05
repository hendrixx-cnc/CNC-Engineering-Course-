# Section 1.3: Structural Analysis and Beam Theory

## Introduction

This section transitions from material selection to **structural mechanics**: the mathematical prediction of deflections, stresses, and natural frequencies under load. While Section 1.2 established that "stiffness comes from geometry (I), not material (E)," we now derive the equations that quantify this relationship.

Professional machine design requires **analytical prediction** before fabrication. Trial-and-error iteration is expensive: a gantry beam that deflects 0.3 mm instead of the target 0.05 mm requires complete redesign, re-cutting, and re-welding ($500-1500 in labor). This section provides the mathematical tools to design correctly the first time.

We'll cover three analysis methods in order of increasing sophistication:

1. **Euler-Bernoulli Beam Theory** (hand calculations, 5-15% accuracy)
2. **Finite Element Analysis (FEA)** (commercial software, 1-3% accuracy)
3. **Modal Analysis** (vibration frequencies, damping ratios)

### Learning Objectives

By the end of this section, you will be able to:

1. Derive beam deflection equations from first principles using Euler-Bernoulli theory
2. Calculate maximum stress and check against material yield strength
3. Compute second moment of area (I) for standard and custom cross-sections
4. Set up FEA models in software (Fusion 360, SolidWorks, ANSYS)
5. Predict natural frequencies and identify resonance risks
6. Interpret mode shapes and design structural modifications to shift frequencies
7. Apply superposition principle for combined loading cases

---

## Euler-Bernoulli Beam Theory

### Fundamental Assumptions

Euler-Bernoulli theory models beams as one-dimensional elastic members with the following assumptions:

1. **Plane sections remain plane:** Cross-sections perpendicular to the beam axis before bending remain perpendicular after bending (no shear deformation).

2. **Small deflections:** Deflection δ ≪ beam length L (typically δ/L < 0.01). Allows sin(θ) ≈ θ, cos(θ) ≈ 1.

3. **Elastic material:** Stress σ = E ε (Hooke's law applies; no yielding).

4. **Negligible shear:** For beams with L/h > 10 (length/height ratio), shear deflection is <5% of bending deflection.

These assumptions hold for machine frames constructed from standard structural sections (tubes, I-beams). For very short, deep beams (L/h < 5), Timoshenko beam theory is required (adds shear deformation term).

### The Beam Equation Derivation

Consider a beam segment of length dx subjected to bending moment M(x):

```
   ↓ q(x) (distributed load)
   |||||||||
   ==================
   ↑         ↑
   R₁        R₂
   x=0       x=L
```

**Step 1: Moment-Curvature Relationship**

From material mechanics, the radius of curvature ρ relates to bending moment:

```
1/ρ = M(x) / (EI)
```

Where:
- M(x) = bending moment at position x
- E = Young's modulus (material property)
- I = second moment of area (geometric property)

The curvature κ = 1/ρ also relates to the second derivative of deflection:

```
κ = d²y/dx²  (for small angles)
```

Therefore:

```
d²y/dx² = M(x) / (EI)     [Fundamental beam equation]
```

**Step 2: Relationship Between Load, Shear, and Moment**

From equilibrium of beam segment:

```
dV/dx = -q(x)    (shear force derivative equals negative distributed load)
dM/dx = V(x)     (moment derivative equals shear force)
```

Combining these:

```
d²M/dx² = -q(x)
```

Substituting into the fundamental beam equation:

```
EI d⁴y/dx⁴ = q(x)     [Governing differential equation]
```

This fourth-order ODE is solved with boundary conditions specific to each loading case.

### Standard Loading Cases

#### Case 1: Simply Supported Beam, Center Point Load

```
   ↓ F
   |
   =========●=========
   ↑                 ↑
   R₁=F/2           R₂=F/2
   x=0    x=L/2     x=L
```

**Solution (derived via integration with boundary conditions y(0)=0, y(L)=0, M(0)=0, M(L)=0):**

Maximum deflection at center (x = L/2):

```
δ_max = FL³ / (48EI)
```

Maximum bending moment at center:

```
M_max = FL/4
```

Maximum stress (at top/bottom fiber, distance c from neutral axis):

```
σ_max = M_max × c / I = (FL/4) × c / I
```

For rectangular cross-section with height h, c = h/2:

```
σ_max = 3FL / (2bh²)     [b = width, h = height]
```

#### Case 2: Simply Supported Beam, Uniform Distributed Load

```
   ↓↓↓↓↓↓↓↓↓ w (N/m)
   ==================
   ↑                 ↑
   R₁=wL/2          R₂=wL/2
```

**Solution:**

```
δ_max = 5wL⁴ / (384EI)     [at x = L/2]

M_max = wL² / 8            [at x = L/2]
```

For self-weight, w = ρ × A × g, where:
- ρ = material density (kg/m³)
- A = cross-sectional area (m²)
- g = 9.81 m/s²

#### Case 3: Cantilever Beam, End Point Load

```
   |====●
   |    ↓ F
   |
   (fixed)
   x=0    x=L
```

**Solution:**

```
δ_max = FL³ / (3EI)        [at x = L, 16× larger than simply supported!]

M_max = FL                 [at x = 0, fixed end]
```

**Key Observation:** Cantilever deflection is 16× larger than simply supported beam for same F, L, E, I. This is why machine frames avoid large cantilevered sections—they deflect excessively.

#### Case 4: Fixed-Fixed Beam, Center Point Load

```
   ║     ↓ F     ║
   ║     |       ║
   ║=====●=======║
   x=0  x=L/2   x=L
   (fixed)    (fixed)
```

**Solution:**

```
δ_max = FL³ / (192EI)      [4× stiffer than simply supported]

M_max = FL/8               [at fixed ends and center]
```

Fixed-fixed boundary conditions provide maximum stiffness but require rigid end connections (welded or bolted with moment continuity).

### Worked Example 1.3.1: Gantry Beam Deflection

**Given:**
- Gantry beam: 80×80×4 mm SHS, A36 steel (E = 200 GPa)
- Span: L = 1,800 mm (simply supported at ends by Y-axis carriages)
- Cutting force: F = 400 N vertical, applied at center
- Tolerance: δ_max ≤ 0.10 mm

**Step 1: Calculate I for 80×80×4 SHS**

For square hollow section:

```
I = (b_outer × h_outer³ - b_inner × h_inner³) / 12
```

Dimensions:
- Outer: 80 × 80 mm
- Wall thickness: 4 mm → Inner: 72 × 72 mm

```
I = (80 × 80³ - 72 × 72³) / 12  (in mm⁴)
  = (80 × 512,000 - 72 × 373,248) / 12
  = (40,960,000 - 26,873,856) / 12
  = 1,173,845 mm⁴
  = 1.174 × 10⁻⁶ m⁴
```

**Step 2: Calculate deflection (simply supported, center load)**

```
δ = FL³ / (48EI)
  = 400 N × (1.8 m)³ / (48 × 200×10⁹ Pa × 1.174×10⁻⁶ m⁴)
  = 2,332.8 / (11,270,400)
  = 2.07 × 10⁻⁴ m
  = 0.207 mm
```

**Result:** δ = 0.207 mm > 0.10 mm tolerance → **FAILS**

**Step 3: Redesign with 100×100×5 SHS**

```
I = (100 × 100³ - 90 × 90³) / 12
  = (100,000,000 - 72,900,000) / 12
  = 2,258,333 mm⁴ = 2.258 × 10⁻⁶ m⁴
```

```
δ = 400 × 1.8³ / (48 × 200×10⁹ × 2.258×10⁻⁶)
  = 2,332.8 / 21,677,000
  = 0.108 mm
```

Still marginal. Try 100×100×6 SHS:

```
I = (100 × 100³ - 88 × 88³) / 12 = 2,682,987 mm⁴ = 2.683 × 10⁻⁶ m⁴

δ = 2,332.8 / (25,756,800)
  = 0.091 mm  ✓ PASSES (10% margin)
```

**Step 4: Check stress**

Maximum moment at center:

```
M_max = FL/4 = 400 N × 1.8 m / 4 = 180 N·m
```

Section modulus for square tube:

```
S = I / c = I / (h/2) = 2.683×10⁻⁶ m⁴ / 0.05 m = 5.37×10⁻⁵ m³
```

Maximum stress:

```
σ_max = M_max / S = 180 N·m / 5.37×10⁻⁵ m³
      = 3.35 × 10⁶ Pa = 3.35 MPa
```

Compare to A36 yield strength σ_y = 250 MPa:

```
Safety factor = 250 MPa / 3.35 MPa = 74.6  ✓ (vastly over-designed for stress)
```

**Conclusion:** Deflection limits design, not stress (typical for machine frames). Select **100×100×6 SHS** for this gantry beam.

---

## Second Moment of Area (I) Calculations

### Why I Matters More Than Material

From δ = FL³/(48EI), doubling I halves deflection—same effect as doubling E. But:

- Doubling E requires switching materials (e.g., steel → titanium, 2.3× cost increase)
- Doubling I requires changing section size (e.g., 80×80 SHS → 100×100 SHS, 1.5× cost increase)

**Geometry (I) is the most cost-effective stiffness lever.**

### Standard Sections

#### Rectangular Hollow Section (RHS) / Square Hollow Section (SHS)

```
   ←——— b ———→
   ┌───────────┐  ↑
   │           │  │
   │  ┌─────┐  │  h
   │  │     │  │  │
   │  └─────┘  │  │
   └───────────┘  ↓
      ↑     ↑
      t (wall thickness)
```

About horizontal axis (bending in vertical plane):

```
I_xx = (b × h³ - b_i × h_i³) / 12
```

Where b_i = b - 2t, h_i = h - 2t (inside dimensions)

About vertical axis (bending in horizontal plane):

```
I_yy = (h × b³ - h_i × b_i³) / 12
```

For square section (b = h), I_xx = I_yy (equal bending stiffness in both planes).

#### I-Beam (Wide Flange, W-Shape)

```
   ←—— b_f ——→
   ┌──────────┐  ↑
   │          │  t_f (flange thickness)
   ├──┐    ┌──┤  ↓
      │    │     ↑
      │    │     h (total height)
      │    │     ↓
   ┌──┘    └──┐  ↑
   │          │  t_f
   └──────────┘  ↓
      ↑  ↑
      t_w (web thickness)
```

Approximate formula (exact values from AISC tables):

```
I_xx ≈ (b_f × h³ - (b_f - t_w) × (h - 2t_f)³) / 12
```

For W150×18 (common small I-beam):
- I_xx = 13.5 × 10⁶ mm⁴ (tabulated value)
- I_yy = 1.25 × 10⁶ mm⁴ (10× less—weak axis)

**Design Rule:** I-beams are highly efficient for bending about the strong axis (vertical loads on horizontal beam) but poor for torsion or weak-axis bending.

#### Circular Hollow Section (CHS)

```
      ┌─────┐
     ╱       ╲
    │    ●    │  D_outer
     ╲       ╱
      └─────┘
        ↑ ↑
        t (wall thickness)
```

For thin-walled tube (t/D < 0.1):

```
I = π (D_outer⁴ - D_inner⁴) / 64

For D_outer = 80 mm, t = 4 mm:
I = π (80⁴ - 72⁴) / 64 = 1.137 × 10⁶ mm⁴
```

**Torsional rigidity (polar moment):**

```
J = π (D_outer⁴ - D_inner⁴) / 32  (2× the bending I)
```

CHS excels in torsion (J is maximized for circular sections) but costs 1.5-2× more than equivalent RHS due to manufacturing complexity.

### Custom Built-Up Sections

For welded plate construction (common in large-format machines):

#### Box Beam (Rectangular Tube from Plate)

```
   ←———— b ————→
   ┌─────────────┐  ↑
   │   top plate │  t_top
   │ ┌─────────┐ │  ↓
   │ │         │ │  ↑
   │ │         │ │  h
   │ └─────────┘ │  ↓
   │ bottom plate│  ↑
   └─────────────┘  t_bot
   ↑ ↑         ↑ ↑
   t_side    t_side
```

Using parallel axis theorem:

```
I_total = Σ (I_i + A_i × d_i²)
```

Where:
- I_i = moment of each plate about its own centroid
- A_i = area of plate i
- d_i = distance from plate centroid to neutral axis of assembly

**Worked Example 1.3.2:** Box beam, 200 mm wide × 150 mm tall
- Top/bottom plates: 200 × 8 mm
- Side plates: 134 × 6 mm (height 134 = 150 - 2×8)

**Top plate contribution:**
```
I_top_own = b × t³ / 12 = 200 × 8³ / 12 = 8,533 mm⁴ (negligible)

A_top = 200 × 8 = 1,600 mm²

d_top = 150/2 - 8/2 = 71 mm (distance from top plate centroid to neutral axis)

I_top_parallel = A_top × d_top² = 1,600 × 71² = 8,065,600 mm⁴
```

**Bottom plate (symmetric):**
```
I_bot_parallel = 8,065,600 mm⁴
```

**Side plates (two of them):**
```
I_side_own = t × h³ / 12 = 6 × 134³ / 12 = 1,200,696 mm⁴ (each)

I_sides_total = 2 × 1,200,696 = 2,401,392 mm⁴
```

**Total:**
```
I_total = 8,065,600 + 8,065,600 + 2,401,392
        = 18,532,592 mm⁴
        = 18.53 × 10⁶ mm⁴
```

For comparison, a standard W200×31 I-beam has I = 21.4 × 10⁶ mm⁴. The custom box beam achieves 87% of the I-beam's stiffness with likely lower cost (depending on welding labor).

---

## Superposition for Combined Loading

Real machine frames experience multiple simultaneous loads:
1. Cutting forces (dynamic, 100-2000 N)
2. Self-weight (static, 50-500 N for gantry)
3. Acceleration forces (dynamic, ma where a = 1-5 m/s²)

For elastic systems (no yielding), deflections are **linearly additive**:

```
δ_total = δ_cutting + δ_self_weight + δ_acceleration
```

### Worked Example 1.3.3: Combined Loading on Gantry

**Given:**
- Beam: 100×100×5 SHS, L = 2,000 mm, I = 2.258 × 10⁻⁶ m⁴, E = 200 GPa
- Beam mass: 9.6 kg/m × 2 m = 19.2 kg
- Cutting force: F_cut = 500 N (downward, at center)
- Acceleration: a = 3 m/s² (upward, during rapid traverse)

**Load 1: Cutting force (point load)**

```
δ_cut = F_cut × L³ / (48EI)
      = 500 × 2³ / (48 × 200×10⁹ × 2.258×10⁻⁶)
      = 4,000 / 21,677,000
      = 0.185 mm (downward)
```

**Load 2: Self-weight (distributed load)**

```
w = m × g / L = 19.2 kg × 9.81 m/s² / 2 m = 94.2 N/m

δ_self = 5wL⁴ / (384EI)
       = 5 × 94.2 × 2⁴ / (384 × 200×10⁹ × 2.258×10⁻⁶)
       = 7,536 / 173,414,400
       = 0.043 mm (downward)
```

**Load 3: Inertial force from acceleration (point load, equivalent)**

When gantry accelerates upward at 3 m/s², the beam experiences downward inertial force:

```
F_inertia = m × a = 19.2 kg × 3 m/s² = 57.6 N (effective, distributed)
```

Conservatively model as point load at center:

```
δ_accel = 57.6 × 2³ / (48 × 200×10⁹ × 2.258×10⁻⁶)
        = 460.8 / 21,677,000
        = 0.021 mm (downward)
```

**Total deflection:**

```
δ_total = 0.185 + 0.043 + 0.021 = 0.249 mm
```

**Analysis:**
- Cutting force dominates (74% of total deflection)
- Self-weight is secondary (17%)
- Acceleration effects are small (8%) for this mass and acceleration

If tolerance is ±0.10 mm, this beam **fails by 2.5×**. Redesign required (upgrade to 120×120×6 SHS with I = 4.81 × 10⁻⁶ m⁴ reduces δ_total to 0.117 mm—still marginal).

---

## Finite Element Analysis (FEA)

### When to Use FEA

Hand calculations using Euler-Bernoulli theory work for:
- Simple geometries (straight beams, standard sections)
- Standard boundary conditions (simply supported, fixed-fixed)
- Single material (homogeneous)

FEA is required for:
- Complex 3D structures (welded frame assemblies)
- Non-standard loading (distributed loads varying in 2D)
- Stress concentrations (welded joints, bolt holes)
- Modal analysis (natural frequencies, mode shapes)
- Nonlinear behavior (contact, plasticity—advanced)

### FEA Fundamentals

FEA divides the structure into thousands of small elements (typically tetrahedra or hexahedra), applies equilibrium equations to each element, and solves the global stiffness equation:

```
[K]{u} = {F}
```

Where:
- [K] = global stiffness matrix (n×n, where n = number of DOF)
- {u} = displacement vector (unknowns to solve for)
- {F} = applied force vector

Matrix [K] depends on:
- Element geometry (from CAD model)
- Material properties (E, ν)
- Boundary conditions (fixed supports, rollers)

**Solution** gives displacement {u} at every node. Post-processing computes:
- Stress: σ = E × ε, where ε = ∂u/∂x
- Strain energy: U = ½ ∫ σε dV
- Safety factor: SF = σ_yield / σ_max

### FEA Software Options

| Software | Cost | Strengths | Learning Curve |
|----------|------|-----------|----------------|
| **Fusion 360** | $70/mo (hobbyist: free) | Integrated CAD+CAM+FEA, cloud-based | Low (3-5 hours) |
| **SolidWorks Simulation** | $4,000-8,000/year | Industry standard, excellent GUI | Medium (20-40 hours) |
| **ANSYS Mechanical** | $30,000-70,000/year | Most capable, nonlinear/dynamics | High (100+ hours) |
| **Autodesk Inventor (FEA)** | $300/mo | Good integration with AutoCAD workflows | Medium (15-30 hours) |
| **FreeCAD (CalculiX)** | Free (open-source) | Capable solver, poor GUI | High (50+ hours) |

**Recommendation for CNC builders:** Start with Fusion 360 (free for hobbyists, $70/mo for commercial). Provides 80% of the capability at 2% of the cost.

### FEA Workflow for CNC Frame

**Step 1: CAD Geometry**

Create simplified geometry:
- Weld beads: Omit (add 10% safety factor to account for weld HAZ reduction in strength)
- Bolt holes: Omit if >50 mm from high-stress regions (add local stress concentration factor SCF = 2.5 if nearby)
- Small fillets: Omit (sharp corners slightly conservative)

**Step 2: Material Assignment**

Define material properties:
- Steel A36: E = 200 GPa, ν = 0.30, ρ = 7,850 kg/m³
- Aluminum 6061-T6: E = 69 GPa, ν = 0.33, ρ = 2,700 kg/m³

**Step 3: Mesh Generation**

- **Element size:** Start with auto-mesh (typically 5-10 mm elements for 1-2m structure)
- **Refinement:** Reduce element size by 2× in high-stress regions (joints, load points)
- **Quality check:** Ensure aspect ratio < 5 (element length/width ratio)

**Mesh convergence test:**
1. Solve with coarse mesh (e.g., 10 mm elements)
2. Refine to medium mesh (5 mm)
3. Refine to fine mesh (2.5 mm)
4. If stress changes <5% from medium to fine, mesh is converged

**Step 4: Boundary Conditions**

- **Fixed supports:** Select faces where frame bolts to ground (e.g., base plate mounting holes). Apply "fixed constraint" (u_x = u_y = u_z = 0, θ_x = θ_y = θ_z = 0).

- **Loads:**
  - Point force: Apply to spindle mount location (e.g., 500 N in -Z direction)
  - Distributed load: Apply pressure to surface (e.g., 10 kPa on work table)
  - Body force: Enable gravity (9.81 m/s² in -Z) for self-weight

**Step 5: Solve & Post-Process**

Run static structural analysis. Examine:

1. **Displacement magnitude:** Maximum deflection location and value
2. **Von Mises stress:** Equivalent stress for yielding check (σ_VM < σ_yield / SF)
3. **Safety factor contour:** SF = σ_yield / σ_VM at every point

**Acceptance Criteria:**
- Maximum deflection < tolerance (e.g., 0.10 mm)
- Minimum safety factor > 2.0 for static loads, > 4.0 for dynamic/fatigue
- No stress concentrations > 0.6 × σ_yield (risk of crack initiation)

### Worked Example 1.3.4: FEA of Welded Frame Assembly

**Scenario:** Simple CNC router frame, 1,200 mm × 800 mm base, 100×50×5 RHS steel tube.

**Geometry:**
- Base: 4 tubes forming rectangle, welded at corners
- Gantry: 2 vertical posts + 1 horizontal beam (simply supported on posts)
- Load: 400 N downward at center of horizontal beam

**FEA Setup (Fusion 360):**

1. **Simplify CAD:**
   - Use "Bodies" for each tube, not "Components" (faster meshing)
   - Omit welds (apply as "bonded contact" between tube end faces)

2. **Material:** Structural Steel (E = 200 GPa, built-in preset)

3. **Mesh:** Auto-mesh with 8 mm elements → 12,453 elements, 28,741 nodes

4. **Boundary Conditions:**
   - Fixed: 4 mounting hole faces on base frame corners
   - Load: 400 N point force at center of gantry beam (split into 2×200 N at top of each vertical post for accurate load path)

5. **Solve:** 45 seconds on standard laptop (6-core CPU, 16 GB RAM)

**Results:**

| Location | Displacement (mm) | Von Mises Stress (MPa) | Safety Factor |
|----------|-------------------|------------------------|---------------|
| Gantry beam center | 0.142 | 8.3 | 30.1 |
| Vertical post top | 0.031 | 12.7 | 19.7 |
| Base frame corner weld | 0.008 | 18.4 | 13.6 |
| Maximum (gantry mid) | **0.142** | **8.3** | **30.1** |

**Validation Against Hand Calc:**

From Example 1.3.1, 100×50×5 RHS with L = 1,200 mm (assuming posts are 800 mm apart):

```
I_100x50 = (100×100³ - 90×40³) / 12 = ... ≈ 1.58 × 10⁻⁶ m⁴ (wait, this is wrong—100×50 not 100×100)
```

Correcting: 100×50×5 RHS (height=100, width=50):

```
I_xx = (50×100³ - 40×90³) / 12 = 1.46 × 10⁻⁶ m⁴

δ_hand = 400 × 0.8³ / (48 × 200×10⁹ × 1.46×10⁻⁶)
       = 204.8 / 14,016,000
       = 0.0146 mm
```

This assumes the beam is supported directly at its ends. But in the FEA model, the load path goes: gantry beam → vertical posts → base frame. The vertical posts deflect too, adding to total deflection.

Post deflection (compression + bending):
```
δ_post ≈ FL³/(48EI) + FL/(AE)  (bending + axial compression)
```

For 100×50×5 post, h = 800 mm, F = 200 N (half the load):
```
δ_post ≈ 0.01 mm (bending dominates since post is "short" L/h = 8)
```

**Total hand calculation:**
```
δ_total ≈ 0.0146 + 2×0.01 ≈ 0.035 mm
```

But FEA shows 0.142 mm—**4× larger!** What's wrong?

**Diagnosis:** The FEA included base frame deflection (the rectangular base flexes under load). Hand calculations assumed rigid supports. This is **why FEA is essential for assemblies**—load paths through 3D structures are non-intuitive.

**Conclusion:** FEA result (0.142 mm) is correct. Hand calculation (0.035 mm) underestimated deflection by neglecting base frame compliance.

---

## Modal Analysis and Natural Frequencies

### Why Vibration Matters

CNC machines are **dynamic systems**. Cutting forces contain frequency components from:
- Spindle rotation: 10,000-24,000 RPM → 167-400 Hz
- Tooth pass frequency: f_tooth = RPM/60 × N_teeth (e.g., 4-flute end mill at 12,000 RPM → 800 Hz)
- Stepper motor microsteps: 200 steps × 32 microsteps × speed → 0-1,000 Hz

If cutting frequency matches a frame natural frequency, **resonance** occurs: deflections amplify by 10-50×, causing:
- Poor surface finish (chatter marks)
- Accelerated tool wear
- Spindle bearing damage
- Potential structural failure

**Design Goal:** Natural frequencies should be >1.5× maximum cutting frequency (safety margin).

### The Modal Equation

An undamped structure vibrates according to:

```
M ẍ + K x = 0
```

Where:
- M = mass matrix
- K = stiffness matrix
- x = displacement (function of time)

Solution has the form x(t) = φ sin(ωt), where:
- φ = mode shape (spatial pattern of vibration)
- ω = natural frequency (rad/s); f = ω/(2π) in Hz

Substituting into the modal equation:

```
(-ω² M + K) φ = 0
```

This is an eigenvalue problem. Solution gives:
- Eigenvalues: ω₁², ω₂², ω₃², ... (natural frequencies squared)
- Eigenvectors: φ₁, φ₂, φ₃, ... (mode shapes)

**First natural frequency** ω₁ (fundamental mode) is the most important—lowest frequency, easiest to excite.

### Approximate Natural Frequency Formula

For simply supported beam with uniformly distributed mass:

```
f₁ = (π/2) × √(EI / (m L⁴))     [Hz]
```

Where:
- m = mass per unit length (kg/m)
- L = span (m)
- E, I = material and geometry properties

**Key Insights:**
1. f ∝ √(EI) → Doubling stiffness increases frequency by 1.41×
2. f ∝ 1/L² → Halving span increases frequency by 4×
3. f ∝ 1/√m → Halving mass increases frequency by 1.41×

**Design Trade:** Higher stiffness (larger I) increases frequency (good), but also increases mass (bad). Net effect depends on section efficiency (I/m ratio).

### Worked Example 1.3.5: Natural Frequency Calculation

**Given:**
- Gantry beam: 100×100×5 SHS, L = 2,000 mm
- I = 2.258 × 10⁻⁶ m⁴, m = 9.6 kg/m, E = 200 GPa

**Calculate first natural frequency:**

```
f₁ = (π/2) × √(EI / (m L⁴))
   = 1.571 × √(200×10⁹ Pa × 2.258×10⁻⁶ m⁴ / (9.6 kg/m × (2 m)⁴))
   = 1.571 × √(451,600 / 153.6)
   = 1.571 × √2,939.6
   = 1.571 × 54.2
   = 85.2 Hz
```

**Check against spindle frequency:**

Router spindle: 24,000 RPM = 400 Hz

Frequency ratio: 400 / 85.2 = 4.7 → **Acceptable** (>1.5× safety margin; 3× is typical)

However, if using 4-flute cutter:
```
f_tooth = 400 Hz × 4 teeth = 1,600 Hz (far above structural frequencies—OK)
```

But 2× harmonic of f₁:
```
2 × f₁ = 2 × 85.2 = 170.4 Hz
```

If spindle runs at 12,800 RPM (213 Hz) and excites 2nd harmonic... potential issue. **Recommendation:** Avoid sustained operation at 12,000-13,000 RPM; stay above 15,000 RPM or below 10,000 RPM.

### FEA Modal Analysis

FEA software solves the eigenvalue problem numerically, giving exact frequencies and mode shapes for complex 3D structures.

**Procedure (Fusion 360):**

1. Setup → Modal Frequencies study type
2. Number of modes: Request 10 (typically only first 3-5 matter)
3. Boundary conditions: Same as static analysis (fixed base mounts)
4. Solve

**Results:**

| Mode | Frequency (Hz) | Description |
|------|----------------|-------------|
| 1 | 83.7 | Gantry beam vertical bending (first harmonic) |
| 2 | 127.5 | Base frame twist |
| 3 | 156.2 | Gantry beam second bending harmonic |
| 4 | 218.9 | Vertical post lateral bending |
| 5 | 334.6 | Gantry beam torsion |

**Mode 1** (83.7 Hz) matches hand calculation (85.2 Hz) within 2%—excellent agreement.

**Design Actions:**

- Mode 1 at 83.7 Hz: OK if spindle >12,000 RPM (200 Hz, 2.4× margin)
- Mode 2 at 127.5 Hz: Base frame twist—add diagonal bracing to increase to >180 Hz
- Mode 4 at 218.9 Hz: Vertical posts—consider thicker section or shorter posts

---

## Stress Concentrations and Fatigue

### Stress Concentration Factor (SCF)

Stress at geometric discontinuities (holes, notches, welds) is amplified:

```
σ_max = K_t × σ_nominal
```

Where K_t = stress concentration factor (depends on geometry).

**Common SCF Values:**

| Feature | K_t (typical) | Design Strategy |
|---------|---------------|-----------------|
| Circular hole (tensile load) | 2.5-3.0 | Use large radius relief, avoid holes in high-stress regions |
| Sharp corner (90°) | 4.0-6.0 | Add fillet radius r ≥ 10 mm |
| Butt weld (ground flush) | 1.2-1.5 | Grind weld flush, blend to base metal |
| Butt weld (as-welded) | 1.5-2.5 | Accept higher SCF or grind |
| Fillet weld (toe) | 2.0-4.0 | Grind weld toe smooth |

**Fatigue Consideration:**

For dynamic loading (cutting forces cycle 1,000-100,000× per day), stress concentration **directly reduces fatigue life**:

```
N_fatigue ∝ 1 / (σ_max)^b
```

Where b = 5-10 (S-N curve exponent). Doubling stress reduces life by 32-1,024×.

**Design Rules:**
1. Avoid holes and notches within 100 mm of high-stress locations (identified via FEA)
2. Use largest practical fillet radius (r ≥ 0.2 × wall thickness)
3. Grind critical welds flush and blend (reduces K_t from 2.5 to 1.3)

---

## Practical Design Guidelines

### Deflection Budget Allocation

For a complete machine with tolerance ±T, allocate deflection budget:

| Component | Allocation | Typical Value (T = 0.10 mm) |
|-----------|------------|------------------------------|
| Base frame | 0.15 T | 0.015 mm |
| Vertical structure (posts) | 0.20 T | 0.020 mm |
| Gantry beam | 0.40 T | 0.040 mm |
| Linear rail deformation | 0.15 T | 0.015 mm |
| Tooling deflection (covered Module 3) | 0.10 T | 0.010 mm |
| **Total** | 1.00 T | **0.100 mm** |

Gantry beam receives the largest allocation because it's the longest unsupported span.

### Stiffness Hierarchy Verification

After FEA, check that stiffness decreases as expected from base → top:

```
k_base > 5 × k_vertical > 2 × k_gantry
```

If violated (e.g., base is too compliant), redesign the weak component.

### Natural Frequency Targets

| Machine Type | f₁ Target (Hz) | Justification |
|--------------|----------------|---------------|
| CNC Router (wood) | >80 Hz | Spindle 12,000-24,000 RPM (200-400 Hz), need 2.5-5× margin |
| Milling Machine (Al) | >150 Hz | Higher cutting forces, need margin for tool chatter frequency |
| Plasma/Laser Cutter | >40 Hz | No spindle, but servo drives generate 20-50 Hz disturbances |
| 3D Printer | >25 Hz | Low forces, but print speed can excite <50 Hz modes |

---

## Summary

This section established the mathematical foundation for predicting frame behavior:

1. **Euler-Bernoulli beam theory** provides closed-form solutions for simple beams (δ = FL³/48EI for simply supported, center load).

2. **Second moment of area I** is the dominant geometric parameter—prioritize maximizing I over changing material E.

3. **Superposition** allows combining multiple load cases (cutting force + self-weight + acceleration).

4. **Finite Element Analysis** is required for 3D frame assemblies where hand calculations underestimate deflection by 2-5×.

5. **Modal analysis** predicts natural frequencies; first mode f₁ should be >1.5× (preferably >2.5×) maximum cutting frequency.

6. **Stress concentrations** at holes, corners, and welds reduce fatigue life; use large fillets and grind critical welds.

---

## Practical Exercises

### Exercise 1.3.1: Beam Comparison

Three candidate gantry beams for L = 1,600 mm span, F = 350 N center load, δ_max = 0.08 mm:

A. 80×80×5 SHS (I = 1.72 × 10⁻⁶ m⁴, m = 11.9 kg/m)
B. 100×50×4 RHS (I = 1.18 × 10⁻⁶ m⁴, m = 8.9 kg/m)
C. W150×18 I-beam (I = 13.5 × 10⁻⁶ m⁴, m = 18.0 kg/m)

**Tasks:**
1. Calculate deflection for each using δ = FL³/(48EI)
2. Calculate first natural frequency for each (assume simply supported)
3. Rank by: (a) stiffness, (b) weight, (c) natural frequency
4. Which would you select for a 24,000 RPM router spindle?

### Exercise 1.3.2: Custom Box Beam Design

Design a welded box beam from flat plate:
- Target I = 15 × 10⁶ mm⁴
- Maximum outer dimensions: 200 mm wide × 180 mm tall
- Plate thickness: 6, 8, or 10 mm (choose for each face)
- Material: A36 steel ($0.80/kg)

**Tasks:**
1. Determine optimal plate configuration (top/bottom/sides)
2. Calculate I using parallel axis theorem
3. Calculate mass per meter
4. Compare cost to W200×31 I-beam (I = 21.4 × 10⁶ mm⁴, m = 31 kg/m)
5. Is the custom box beam cost-effective?

### Exercise 1.3.3: FEA Validation

Build a simple frame in CAD software and run FEA:
- Geometry: 1,000 mm × 800 mm × 600 mm tall frame, 60×60×4 SHS steel
- Load: 200 N downward at center of top beam
- Boundary: Fix bottom 4 corners

**Tasks:**
1. Hand-calculate deflection (assume top beam is simply supported, ignore base compliance)
2. Run FEA with coarse mesh (10 mm elements)
3. Refine mesh to fine (3 mm elements)
4. Compare FEA result to hand calculation—what is the ratio?
5. Explain the difference (hint: load path through entire frame)

---

**Next Section Preview:** [Section 1.4: Base Frame Design](section-01.4-base-frame-design.md) will apply these analysis methods to the specific challenge of designing a rigid, thermally stable base frame—the foundation upon which all other components mount.

---

## References

1. **Gere, J.M. & Timoshenko, S.P.** - *Mechanics of Materials*, 8th Ed. (2012) - Classic beam theory textbook
2. **Hibbeler, R.C.** - *Structural Analysis*, 10th Ed. (2017) - Deflection formulas and analysis methods
3. **Logan, D.L.** - *A First Course in the Finite Element Method*, 6th Ed. (2016) - FEA fundamentals
4. **Blevins, R.D.** - *Formulas for Natural Frequency and Mode Shape* (1979) - Comprehensive vibration reference
5. **Roark's Formulas for Stress and Strain**, 8th Ed. (2011) - Exhaustive collection of beam formulas and stress concentration factors
