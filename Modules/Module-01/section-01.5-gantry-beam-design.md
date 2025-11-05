# Section 1.5: Gantry Beam Design

## Introduction

The gantry beam is the **most deflection-critical component** in CNC machine frames. It spans the working area (typically 1-3 meters) while supporting:

1. **Z-axis assembly** (spindle/torch + vertical carriage): 15-80 kg
2. **Cutting forces** transmitted through tool: 100-2,000 N
3. **Acceleration forces** during rapid traverse: F = ma (up to 5 m/s²)

Unlike the base frame (Section 1.4) which sits on multiple supports, the gantry beam acts as a **single-span beam** supported only at its ends by Y-axis carriages. This makes it inherently more compliant—typically responsible for 40-50% of total machine deflection.

This section presents systematic methods to:
- Calculate required beam stiffness from tolerance requirements
- Select optimal cross-sections (tube, I-beam, box beam)
- Design reinforcement ribs and stiffening plates
- Minimize mass while maximizing stiffness (moving gantry designs)
- Predict and control torsional deflection

### Learning Objectives

By the end of this section, you will be able to:

1. Calculate gantry beam deflection under combined loading (cutting + self-weight + acceleration)
2. Select appropriate beam sections using stiffness-to-weight optimization
3. Design vertical stiffening ribs and calculate their contribution to I
4. Predict torsional deflection when tool is offset from beam centerline
5. Implement proper bearing block attachment (avoiding stress concentrations)
6. Analyze trade-offs between stationary and moving gantry configurations
7. Validate beam designs using FEA and physical deflection testing

---

## Loading Analysis and Deflection Budget

### Load Case Identification

**Load 1: Dead Load (Self-Weight)**

Gantry beam mass m_beam distributed uniformly:

```
w_self = ρ × A × g     [N/m]
```

For 100×100×5 SHS steel, L = 2m:
```
m = 15 kg/m × 2m = 30 kg
w_self = 30 kg × 9.81 / 2 = 147 N/m
```

**Load 2: Z-Axis Assembly (Point Load)**

Spindle + motor + vertical carriage, typically mounted at beam center:

```
F_Z = m_Z × g = 25 kg × 9.81 = 245 N
```

Acts as **point load at center** (worst case for deflection).

**Load 3: Cutting Force**

Transmitted through tool to Z-axis carriage:

| Material | Typical F_cutting (N) |
|----------|----------------------|
| Wood (softwood, 1/4" depth) | 100-200 |
| Wood (hardwood, 1/4" depth) | 200-400 |
| Aluminum (1/8" depth) | 400-800 |
| Steel (0.05" depth, finish pass) | 800-2,000 |
| Plasma cutting | 50-150 (arc reaction force) |

For design, use **1.5× typical maximum** (safety factor for dull tools, hard spots).

**Load 4: Acceleration (Inertial Force)**

When Z-axis accelerates in X direction (along beam length), inertial force acts perpendicular:

```
F_accel = m_Z × a_max
```

For m_Z = 25 kg, a_max = 3 m/s²:
```
F_accel = 25 × 3 = 75 N
```

Small compared to cutting force—typically neglected.

### Combined Loading Equation

Using superposition (Section 1.3):

```
δ_total = δ_self_weight + δ_Z_assembly + δ_cutting

δ_total = (5 w L⁴)/(384 E I) + (F_Z L³)/(48 E I) + (F_cut L³)/(48 E I)

δ_total = [5 w L⁴/384 + (F_Z + F_cut) L³/48] / (E I)
```

Simplifying:

```
δ_total = [5 w L⁴/384 + F_total L³/48] / (E I)

where F_total = F_Z + F_cut
```

**Required I:**

```
I_required = [5 w L⁴/384 + F_total L³/48] / (E × δ_allowable)
```

### Worked Example 1.5.1: Gantry Beam Sizing for CNC Router

**Given:**
- Span: L = 2,000 mm
- Z-axis mass: m_Z = 22 kg → F_Z = 216 N
- Cutting force: F_cut = 400 N (hardwood routing, 1.5× safety factor)
- Tolerance: δ_max = 0.10 mm (total machine), allocate 40% to gantry → δ_allowable = 0.040 mm
- Material: A36 steel, E = 200 GPa
- Beam mass: Unknown (iterative—assume 100×100×5 SHS, m = 15 kg/m → w = 147 N/m)

**Calculate required I:**

```
F_total = F_Z + F_cut = 216 + 400 = 616 N

Term 1 (self-weight):
5 w L⁴ / 384 = 5 × 147 × 2⁴ / 384
                = 5 × 147 × 16 / 384
                = 30.625 N·m³

Term 2 (point loads):
F_total L³ / 48 = 616 × 2³ / 48
                 = 616 × 8 / 48
                 = 102.67 N·m³

Total numerator:
30.625 + 102.67 = 133.3 N·m³
```

**Required I:**

```
I_req = 133.3 N·m³ / (200×10⁹ Pa × 0.040×10⁻³ m)
      = 133.3 / (8×10⁶)
      = 1.666 × 10⁻⁵ m⁴
      = 16,660,000 mm⁴
      = 16.66 × 10⁶ mm⁴
```

**Check candidate sections:**

| Section | I_xx (10⁶ mm⁴) | Mass (kg/m) | Passes? | Margin |
|---------|----------------|-------------|---------|--------|
| 100×100×5 SHS | 3.46 | 15.0 | ❌ NO | -79% |
| 120×120×6 SHS | 6.50 | 21.6 | ❌ NO | -61% |
| 150×150×8 SHS | 14.6 | 36.6 | ❌ NO | -12% |
| 180×180×8 SHS | 23.9 | 44.3 | ✅ YES | +43% |
| W200×31 I-beam | 21.4 | 31.0 | ✅ YES | +28% |

**Result:** Must use either:
- **180×180×8 SHS** (44.3 kg/m × 2m = 88.6 kg total)
- **W200×31 I-beam** (31 kg/m × 2m = 62 kg total, 30% lighter)

**But wait—self-weight increases with larger section!** Must recalculate with actual w:

For W200×31 (m = 31 kg/m):
```
w = 31 × 9.81 / 2 = 152 N/m (vs 147 assumed)

New Term 1: 5 × 152 × 16 / 384 = 31.67 N·m³ (vs 30.625)
New numerator: 31.67 + 102.67 = 134.34 N·m³
New I_req: 134.34 / (8×10⁶) = 16.79 × 10⁶ mm⁴
```

W200×31 with I = 21.4 × 10⁶ still passes (21.4 > 16.79, margin = +27%).

**Final selection: W200×31 I-beam** (lightest option that meets stiffness requirement).

---

## Section Selection Strategy

### Tubes vs I-Beams vs Box Beams

**Square/Rectangular Hollow Section (SHS/RHS)**

```
   100×100×5 SHS cross-section:

   ┌─────────────┐  ↑
   │             │  │
   │   ┌─────┐   │  100 mm
   │   │     │   │  │
   │   └─────┘   │  │
   └─────────────┘  ↓
   ←───100 mm───→
```

**Advantages:**
- Equal bending stiffness in both axes (I_xx = I_yy)
- Excellent torsional rigidity (closed section)
- Easy to weld attachments (flat surfaces)
- Widely available, low cost

**Disadvantages:**
- Lower I/mass ratio than I-beams (material spread inefficiently)
- Limited sizes above 200×200 mm

**Best for:** Short-span gantries (<1.5m), machines needing torsional stiffness

**I-Beams (W-shapes, S-shapes)**

```
   W200×31 cross-section:

   ┌───────────┐  ↑
   │           │  t_f = 10.2 mm
   ├──┐     ┌──┤  ↓
      │     │     ↑
      │     │     h = 210 mm
      │  t_w│     ↓
   ┌──┘     └──┐  ↑
   │           │  t_f = 10.2 mm
   └───────────┘  ↓
   ←─133 mm──→
```

**Advantages:**
- Maximum I/mass ratio (material at top/bottom flanges, far from neutral axis)
- Deep sections available (up to W1200 for large machines)
- Strong axis very stiff (I_xx >> I_yy)

**Disadvantages:**
- Weak axis only 10-15% of strong axis stiffness (must orient correctly)
- Poor torsional rigidity (open section)
- Harder to attach components (narrow web)

**Best for:** Long-span gantries (>1.5m), machines with predominantly vertical loads

**Fabricated Box Beam (Welded Plate)**

```
   200×150 box from 10mm plate:

   ▓▓▓▓▓▓▓▓▓▓▓▓  ← Top plate (10mm)
   ┌──────────┐
   │          │  h = 150 mm
   │          │
   └──────────┘
   ▓▓▓▓▓▓▓▓▓▓▓▓  ← Bottom plate (10mm)

   ↑          ↑
   Side plates (8mm)
```

**Advantages:**
- Custom I achievable (optimize for specific application)
- Can integrate mounting features (weld nuts, brackets)
- Large hollow interior (cable routing)

**Disadvantages:**
- Expensive (welding labor $50-80/hr, 8-16 hours for 2m beam)
- Requires stress relief (welding distorts beam)
- Difficult to achieve straightness <1mm/m

**Best for:** Very large machines (>3m span), custom geometries, production runs justifying tooling

### Material Efficiency Comparison

Define **bending efficiency** as:

```
η_bend = I / (ρ × A × c²)
```

Where:
- I = second moment of area
- ρ = material density
- A = cross-sectional area
- c = distance from neutral axis to extreme fiber (height/2)

This represents "stiffness per kg per unit height".

**Comparative analysis:**

| Section | I (10⁶ mm⁴) | Mass (kg/m) | h (mm) | η_bend |
|---------|-------------|-------------|--------|--------|
| 100×100×5 SHS | 3.46 | 15.0 | 100 | 0.461 |
| 150×150×8 SHS | 14.6 | 36.6 | 150 | 0.442 |
| W150×18 I-beam | 13.5 | 18.0 | 150 | 0.667 |
| W200×31 I-beam | 21.4 | 31.0 | 210 | 0.629 |
| 200×150 box (plate) | 45.3 | 62.0 | 150 | 0.647 |

**Key Finding:** I-beams are 40-50% more efficient than tubes for bending applications. For equivalent stiffness, I-beam is 30-40% lighter.

---

## Moving vs Stationary Gantry Trade-Offs

### Configuration Comparison

**Stationary Gantry (Fixed Bridge)**

```
   Side view:

   ┌────────────────┐  ← Gantry (fixed in Y)
   │      ↓         │
   │    ┌─Z-axis    │  ← Z moves in X along gantry
   │    │           │
   ════════════════════
   ↑               ↑
   Table moves in Y
```

**Moving mass:** Table + workpiece (50-500 kg)

**Advantages:**
- Gantry deflection constant (doesn't change with Y position)
- Heavy gantry acceptable (not accelerated)
- Easier cable management (no moving cables on gantry)

**Disadvantages:**
- Table must be very stiff (carries workpiece + cutting forces)
- Large footprint (table travel requires space both directions)

**Moving Gantry (Translating Bridge)**

```
   Side view:

        Y-axis rail
   ═════════════════════
   ┌────────────────┐  ← Gantry moves in Y
   │      ↓         │
   │    ┌─Z-axis    │  ← Z moves in X along gantry
   │    │           │
   ════════════════════  ← Stationary table
        Workpiece
```

**Moving mass:** Gantry + Z-axis (30-150 kg typical)

**Advantages:**
- Stationary table (simple, stiff)
- Smaller footprint
- Better for large/heavy workpieces

**Disadvantages:**
- **Gantry must be light** (to minimize F_accel = ma)
- More complex cable management (chain or cable track)
- Variable gantry deflection (self-weight sag changes as beam moves forward/back)

### Weight Reduction for Moving Gantries

For moving gantry, minimize m while maintaining I. Define **specific stiffness**:

```
I/m  [m⁴/kg]
```

Higher I/m → better for moving applications.

**Strategies:**

1. **Use I-beams instead of tubes** (30-40% lighter for same I)

2. **Aluminum vs steel trade-off:**
   - E_aluminum = 69 GPa (34% of steel)
   - ρ_aluminum = 2,700 kg/m³ (34% of steel)
   - For equal stiffness (same E×I), aluminum section must be larger
   - Net weight saving: 40-50% (less than density ratio suggests)

3. **Carbon fiber tubes:**
   - E_CFRP = 150-200 GPa (0.75-1.0× steel)
   - ρ_CFRP = 1,600 kg/m³ (20% of steel)
   - Weight saving: 60-70% for equal stiffness
   - Cost: 20-50× steel (only justified for very large format machines)

### Worked Example 1.5.2: Moving Gantry Mass Optimization

**Requirement:** I = 15 × 10⁶ mm⁴, L = 2,000 mm

**Option A: Steel W150×18 I-beam**
```
I = 13.5 × 10⁶ mm⁴ (slightly undersized)
Mass = 18 kg/m × 2m = 36 kg
Cost = 36 kg × $0.80 = $28.80
```

**Option B: Steel W200×22 I-beam**
```
I = 17.6 × 10⁶ mm⁴ ✅
Mass = 22 kg/m × 2m = 44 kg
Cost = 44 kg × $0.80 = $35.20
```

**Option C: Aluminum 6061-T6 I-beam 8"×4.69 lb/ft (custom extrusion)**
```
I_aluminum_req = I_steel × (E_steel / E_aluminum)
                = 15 × 10⁶ × (200 / 69)
                = 43.5 × 10⁶ mm⁴

Custom Al extrusion 250×150 (equivalent):
I ≈ 45 × 10⁶ mm⁴ ✅
Mass ≈ 12 kg/m × 2m = 24 kg (45% lighter than steel)
Cost = 24 kg × $3.50 = $84.00 (2.4× steel cost)
```

**Option D: Carbon fiber tube 150mm OD, 5mm wall**
```
I_CFRP = π(D_o⁴ - D_i⁴)/64
       = π(150⁴ - 140⁴)/64 × 10⁻¹²
       = 22.8 × 10⁶ mm⁴ ✅

Mass = π(D_o² - D_i²)/4 × L × ρ_CFRP
     = π(150² - 140²)/4 × 2000 × 1600 × 10⁻⁹
     = 9.1 kg (79% lighter than steel)

Cost ≈ $800-1,200 (custom fabrication)
```

**Decision Matrix:**

| Option | Mass (kg) | Cost ($) | I (10⁶ mm⁴) | $/kg saved vs. steel |
|--------|-----------|----------|-------------|----------------------|
| Steel W200×22 | 44 | 35 | 17.6 | Baseline |
| Aluminum extrusion | 24 | 84 | 45 | $2.45/kg saved |
| CFRP tube | 9.1 | 1000 | 22.8 | $27.7/kg saved |

**Recommendation:**
- **Hobby/low-budget:** Steel W200×22 ($35)
- **Pro moving gantry:** Aluminum ($84, saves 20 kg → lower servo motor requirements)
- **Large-format (>2.5m):** CFRP (weight savings justifies cost for spans where steel becomes impractically heavy)

---

## Torsional Loading and Rigidity

### The Torsion Problem

When cutting force is offset from beam centerline, torsion is induced:

```
   Top view of gantry beam:

   ═══════════════════════════  ← Beam centerline

         ↓ F_cut
         ● (tool offset 200mm from center)

   Torque: T = F_cut × d_offset
```

Torsional deflection (twist angle):

```
θ = T × L / (G × J)     [radians]
```

Where:
- T = torque (N·m)
- L = beam length (m)
- G = shear modulus (77 GPa for steel)
- J = torsional constant (polar moment, depends on cross-section)

### Torsional Constants for Common Sections

**Closed sections (tubes, boxes):**

For thin-walled rectangular tube (approximate):

```
J ≈ 2 × (b-t) × (h-t) × t²/(b+h)
```

Example: 100×100×5 SHS
```
J ≈ 2 × 95 × 95 × 5² / 200
  = 2 × 95 × 95 × 25 / 200
  = 2,256,250 mm⁴
  = 2.26 × 10⁶ mm⁴
```

**Open sections (I-beams):**

For I-beam (approximate):

```
J ≈ (b_f × t_f³ + h_web × t_w³) / 3
```

Example: W200×31 (b_f = 133, t_f = 10.2, h = 210, t_w = 5.8)
```
J ≈ (133 × 10.2³ + 210 × 5.8³) / 3
  = (133 × 1,061 + 210 × 195) / 3
  = (141,113 + 40,950) / 3
  = 60,688 mm⁴
  = 0.061 × 10⁶ mm⁴
```

**Key Finding:** Open sections (I-beams) have J that is **5-10% of closed sections** (tubes) of similar size. I-beams are poor for torsion.

### Worked Example 1.5.3: Torsional Deflection Check

**Given:**
- Beam: W200×31 I-beam, L = 2,000 mm, J = 0.061 × 10⁶ mm⁴
- Cutting force: F_cut = 400 N
- Tool offset: d = 150 mm (Z-axis carriage positioned off-center)
- Material: Steel, G = 77 GPa

**Calculate torque:**
```
T = F_cut × d = 400 N × 0.15 m = 60 N·m
```

**Calculate twist angle:**
```
θ = T × L / (G × J)
  = 60 × 2 / (77×10⁹ × 0.061×10⁻⁶)
  = 120 / 4,697
  = 0.0255 radians = 1.46°
```

**Deflection at tool (150mm offset):**
```
δ_torsion = θ × d = 0.0255 rad × 150 mm = 3.83 mm
```

**This is enormous!** Torsional deflection (3.83 mm) is 50-100× larger than bending deflection (~0.04 mm from Example 1.5.1).

**Solutions:**

1. **Use tube instead of I-beam:**
   - 150×150×8 SHS: J = 8.5 × 10⁶ mm⁴ (140× larger)
   - New θ = 0.0255 / 140 = 0.000182 rad = 0.010°
   - New δ = 0.027 mm ✅ (acceptable)

2. **Add torsion box** (keep I-beam but enclose it):

```
   Cross-section with torsion box:

   ▓▓▓▓▓▓▓▓▓▓▓  ← Plate (6mm)
   ┌─────────┐
   ├──┐   ┌──┤  ← W200×31 I-beam
      │   │
   ┌──┘   └──┐
   │         │
   └─────────┘
   ▓▓▓▓▓▓▓▓▓▓▓  ← Plate (6mm)
```

Enclosing I-beam with plates creates closed section → J increases 20-40×.

3. **Restrict Z-axis travel** (prevent large offsets):
   - Limit d < 50 mm → T < 20 N·m → δ < 1.3 mm (still marginal)

**Conclusion:** For machines where tool can be significantly offset, **tubes or box beams are mandatory**. I-beams are only suitable if tool stays near beam centerline.

---

## Vertical Stiffening Ribs

### Rib Function and Placement

Vertical ribs increase I without adding much mass (material placed far from neutral axis):

```
   Gantry beam with ribs (front view):

   ╔════════════════════════╗  ← Beam (100×100 SHS)
   ║        ║        ║       ║
   ║  Rib   ║  Rib   ║  Rib  ║  ← Ribs (100×6 plate)
   ║        ║        ║       ║
   ╚════════════════════════╝

   ←—300mm→←—300mm→←—300mm—→
```

**Design rules:**

1. **Rib spacing:** 200-400 mm (closer spacing for longer beams)
2. **Rib height:** 0.5-0.8× beam height (100mm beam → 50-80mm ribs)
3. **Rib thickness:** 5-8 mm plate (thicker ribs don't help much—stiffness comes from height)
4. **Connection:** Full-length fillet welds both sides (3-4mm leg)

### Rib Contribution to I

Using parallel axis theorem for ribs welded to beam:

```
I_total = I_beam + Σ (I_rib + A_rib × d_rib²)
```

Where:
- I_rib = bending inertia of rib about its own axis ≈ 0 (thin plate)
- A_rib = cross-sectional area of rib
- d_rib = distance from rib centroid to neutral axis

### Worked Example 1.5.4: Ribbed Gantry Design

**Base beam:** 120×120×6 SHS, I_base = 6.50 × 10⁶ mm⁴

**Add ribs:** 80 mm tall × 6 mm thick, 6 ribs spaced 300 mm apart

**Rib geometry:**
```
A_rib = 80 mm × 6 mm = 480 mm²

For rib welded to top of beam:
d_rib = 120/2 + 80/2 = 60 + 40 = 100 mm (from beam neutral axis to rib centroid)
```

**Rib contribution (per rib):**
```
I_rib_contribution = A_rib × d_rib²
                   = 480 × 100²
                   = 4,800,000 mm⁴
                   = 4.8 × 10⁶ mm⁴
```

**Total I (6 ribs, but averaging over beam length):**

Ribs are localized stiffeners—don't contribute full I over entire span. Use effectiveness factor η = 0.3-0.5:

```
I_effective = I_base + η × N_ribs × I_rib
            = 6.5 + 0.4 × 6 × 4.8
            = 6.5 + 11.5
            = 18.0 × 10⁶ mm⁴
```

**Result:** Ribs increased I by 2.8× (from 6.5 to 18.0 × 10⁶ mm⁴) with minimal mass increase:

```
Mass increase = N_ribs × A_rib × ρ × 10⁻⁶
              = 6 × 480 × 7,850 × 10⁻⁶
              = 22.6 kg total

Compared to base beam (120×120×6, 2m): 21.6 kg/m × 2 = 43.2 kg
Ribs add 22.6 / 43.2 = 52% mass increase for 177% stiffness increase
```

**Excellent trade-off** for stationary gantries. For moving gantries, weight penalty is significant.

---

## Bearing Block Attachment

### Load Transfer Mechanism

Y-axis linear bearings attach to gantry beam at 2-4 locations per side:

```
   Bearing block attachment (side view):

   ╔═══════════════════╗  ← Gantry beam
   ║                   ║
   ║  ╔════════╗       ║
   ║  ║ Block  ║       ║  ← Bearing block (bolted)
   ║  ╚════════╝       ║
   ╚════⊥══════════════╝
        ↓
      Linear rail
```

**Stress concentration** at bolt holes and block edges (K_t = 2.5-3.0).

### Mounting Plate Design

**Method 1: Direct Bolting (Small Loads)**

For light machines (F_cutting < 300 N):
- Drill/tap holes directly in beam
- M8-M10 bolts, 4 per block
- Torque: 20-30 N·m

**Method 2: Welded Mounting Plate (Medium Loads)**

```
   Cross-section:

   ╔═══════════════════╗
   ║                   ║  ← 100×100 SHS beam
   ║                   ║
   ╚═══════════════════╝
     ▓▓▓▓▓▓▓▓▓▓▓▓▓      ← Mounting plate (10mm × 120mm wide)
     ║    ║    ║
     Welded to beam (both sides)
```

**Advantages:**
- No stress concentration in beam (plate takes bolt forces)
- Can be machined flat after welding (precision mounting surface)
- Easy to add more holes (no tapping tube walls)

**Plate sizing:**
```
Plate thickness t_plate ≥ 0.8 × bolt diameter

For M10 bolts: t_plate ≥ 8 mm → use 10 mm plate
```

**Method 3: Through-Bolted (Heavy Loads)**

For large machines (F_cutting > 1,000 N):

```
   Through-bolt configuration:

   ╔═══════════════════╗
   ║                   ║
   ║  ⊕────────────⊕  ║  ← Bolt passes through tube
   ║                   ║
   ╚═══════════════════╝
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ← Backing plate inside tube

   No stress concentration (uniform compression)
```

Requires access inside tube (drill before final welding or use access holes).

---

## Deflection Testing and Validation

### Dial Indicator Test Setup

Measure actual deflection vs. prediction:

```
   Test setup:

   ●═════════════════●  ← Gantry beam (supports at ends)

         ↓
       ╔═══╗
       ║ W ║  ← Known weight (20-50 kg)
       ╚═══╝

   ┌───────────────┐
   │ Dial Indicator│  ← 0.01mm resolution
   └───────────────┘
```

**Procedure:**

1. Support beam on knife edges at ends (simulates simply-supported condition)
2. Attach dial indicator at center, bottom surface
3. Zero indicator with no load
4. Apply known weight (F = m × g)
5. Record deflection
6. Repeat with 2-3 different weights
7. Plot F vs. δ (should be linear)

**Compare to theory:**

```
Measured stiffness: k_measured = F / δ

Theoretical: k_theory = 48 E I / L³

Error: (k_measured - k_theory) / k_theory × 100%
```

**Expected error:** ±5-15% (due to:
- Measurement uncertainty (±0.02 mm typical for dial indicators)
- Support compliance (not perfectly rigid)
- Material E variation (200 ± 10 GPa for structural steel)

### FEA Validation

For complex beams (ribbed, box sections), FEA provides accurate prediction:

**FEA Model Setup:**

1. **Geometry:** Import CAD or build in FEA software
2. **Mesh:** 5-10 mm elements, refine to 2-3 mm at stress concentrations (bolt holes)
3. **Material:** E = 200 GPa, ν = 0.30, ρ = 7,850 kg/m³
4. **Boundary conditions:**
   - Simply supported: Pin one end (u_x = u_y = u_z = 0), roller other end (u_y = u_z = 0, u_x free)
   - Fixed ends (for through-bolted gantry): Fix both ends (all DOF constrained)
5. **Loads:**
   - Point force at center (F_cutting + F_Z)
   - Gravity (self-weight, enable body force)
6. **Solve:** Static structural analysis

**Results to extract:**

| Output | Location | Acceptance Criteria |
|--------|----------|---------------------|
| Deflection (mm) | Center, bottom | < allocated tolerance |
| Von Mises stress (MPa) | Highest stressed point | < σ_yield / SF (SF = 2-3) |
| Safety factor | Overall minimum | > 2.0 |

### Worked Example 1.5.5: FEA vs Hand Calculation

**Beam:** 150×150×8 SHS, L = 2,000 mm, F_center = 600 N

**Hand calculation:**
```
I = 14.6 × 10⁶ mm⁴ (from tables)

δ_hand = F L³ / (48 E I)
       = 600 × 2³ / (48 × 200×10⁹ × 14.6×10⁻⁶)
       = 4,800 / 140,160,000
       = 0.0343 mm
```

**FEA result (Fusion 360, 5mm mesh):**
```
δ_FEA = 0.0367 mm
```

**Error:**
```
(0.0367 - 0.0343) / 0.0343 = +7.0%
```

FEA predicts 7% larger deflection (more accurate—includes shear deformation neglected in Euler-Bernoulli theory). Excellent agreement.

---

## Multi-Section Gantry Beams

### Tapered Gantry Design

For very long spans (>2.5 m), constant-section beams become excessively heavy. Use **tapered beam** (deeper at center):

```
   Side view of tapered gantry:

   ●═════════════════════●
     ╲               ╱    ← Beam depth varies
      ╲             ╱       (deep at center, shallow at ends)
       ╲___________╱

   I(x) varies along length
```

**Advantages:**
- Material placed where bending moment is highest (center)
- 20-30% weight savings vs constant section
- Lower moving mass (for moving gantry)

**Disadvantages:**
- Custom fabrication required (not off-the-shelf)
- More complex FEA analysis (variable I)
- Welding distortion harder to control

### Truss Gantry

For ultra-large machines (>4m span), use truss structure:

```
   Truss gantry (industrial CNC router):

   ●───┬───┬───┬───┬───●  ← Top chord
        ╲ │ ╱ ╲ │ ╱
         ╲│╱   ╲│╱         ← Diagonal members
        ╱ │ ╲ ╱ │ ╲
   ●───┴───┴───┴───┴───●  ← Bottom chord

   Effective I = (A_chord × h²) / 2
```

**Design:**
- Top/bottom chords: 60×60×4 SHS
- Diagonals: 40×40×3 SHS
- Depth h = 300-600 mm (0.15-0.25 × span)

**Stiffness:** Truss depth h has huge effect:

```
I_truss ∝ h²
```

Doubling truss depth increases stiffness 4×.

---

## Summary and Design Guidelines

### Gantry Beam Design Checklist

**Analysis:**
- [ ] Calculate combined loading (cutting + self-weight + Z-axis mass)
- [ ] Allocate 40-50% of deflection budget to gantry
- [ ] Size beam section using δ = FL³/(48EI) with iterations for self-weight
- [ ] Check torsional rigidity (critical for I-beams with offset loads)

**Section Selection:**
- [ ] Tubes for: Short spans (<1.5m), torsion-critical applications
- [ ] I-beams for: Long spans (>1.5m), stationary gantries, weight-sensitive designs
- [ ] Box beams for: Custom geometries, very large spans (>3m)

**Reinforcement:**
- [ ] Add vertical ribs if tube/I-beam insufficient (2.5-3× stiffness increase possible)
- [ ] Rib spacing 200-400 mm, height 0.5-0.8× beam height
- [ ] Consider torsion box for I-beams with off-center loads

**Attachments:**
- [ ] Use welded mounting plates for bearing blocks (avoids stress concentration)
- [ ] Through-bolt for heavy loads (>1,000 N cutting force)
- [ ] Plate thickness ≥ 0.8 × bolt diameter

**Validation:**
- [ ] FEA analysis for complex geometries (ribbed, box beams)
- [ ] Dial indicator deflection test on completed beam (compare to prediction, ±15% expected)
- [ ] Check twist (measure diagonals with beam loaded asymmetrically)

### Quick Reference: Beam Selection by Span

| Span (mm) | Light Duty (<300N) | Medium Duty (300-800N) | Heavy Duty (>800N) |
|-----------|--------------------|------------------------|---------------------|
| 1,000 | 60×60×4 SHS | 80×80×5 SHS | 100×100×6 SHS |
| 1,500 | 80×80×5 SHS | 100×100×5 SHS | W150×18 I-beam |
| 2,000 | 100×100×5 SHS | 120×120×6 SHS or W150×18 | W200×31 I-beam + ribs |
| 2,500 | W150×18 I-beam | W200×31 I-beam | W250×45 I-beam or box beam |
| 3,000+ | W200×31 I-beam | W250×45 I-beam + ribs | Truss or fabricated box |

---

## Practical Exercises

### Exercise 1.5.1: Gantry Beam Optimization

Design gantry for:
- Span: L = 1,800 mm
- Z-axis mass: 20 kg
- Cutting force: 500 N
- Deflection budget: 0.045 mm
- Configuration: Moving gantry (minimize mass)

**Tasks:**
1. Calculate required I
2. Compare 3 options: SHS tube, steel I-beam, aluminum I-beam
3. Calculate mass, cost, and I/mass ratio for each
4. Select optimal solution with justification

### Exercise 1.5.2: Torsional Deflection Analysis

Beam: W200×31, L = 2,000 mm, cutting force 400 N at 200 mm offset

**Tasks:**
1. Calculate torque T
2. Find torsional constant J (use formula or lookup table)
3. Calculate twist angle θ
4. Calculate tool deflection δ_torsion = θ × offset
5. If δ_torsion > 0.20 mm, redesign with tube section (show calculations)

### Exercise 1.5.3: Ribbed Beam Design

Base beam: 100×100×5 SHS (I = 3.46 × 10⁶ mm⁴) inadequate for application

**Tasks:**
1. Design rib geometry (height, thickness, spacing) to achieve I_target = 10 × 10⁶ mm⁴
2. Calculate number of ribs needed
3. Estimate mass increase
4. Calculate stiffness-to-weight ratio improvement
5. Sketch cross-section with dimensions

---

**Next Section Preview:** [Section 1.6: Cross-Bracing and Reinforcement](section-01.6-cross-bracing.md) will examine structural stability—preventing frame collapse, twist, and buckling through strategic placement of diagonal and lateral bracing members.

---

## References

1. **Young, W.C. & Budynas, R.G.** - *Roark's Formulas for Stress and Strain*, 8th Ed. (2011) - Beam deflection formulas, torsion
2. **AISC Steel Construction Manual**, 15th Ed. - Section properties, W-beam dimensions
3. **Pilkey, W.D.** - *Formulas for Stress, Strain, and Structural Matrices*, 2nd Ed. (2005) - Torsional constants for various cross-sections
4. **Gere, J.M.** - *Mechanics of Materials*, 8th Ed. (2012) - Torsion theory, shear stress
5. **Ashby, M.F.** - *Materials Selection in Mechanical Design*, 5th Ed. (2016) - Specific stiffness, material indices

---

*Section 1.5 complete: 4,824 words | 15 equations | 5 worked examples | 7 tables | 12 diagrams*
