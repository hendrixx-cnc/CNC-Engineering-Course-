# Section 1.4: Base Frame Design

## Introduction

The base frame is the **foundation of dimensional accuracy**. Every other component—linear rails, gantry, spindle—ultimately references the base geometry. A twisted or flexing base propagates errors through the entire kinematic chain:

```
Base error × 1.5-3× amplification = Tool path error
```

This section focuses on designing base frames that meet three competing requirements:

1. **Stiffness:** Resist deflection under cutting forces (k > 100 N/mm typical)
2. **Flatness:** Maintain mounting surface planarity <0.05 mm/m
3. **Cost-effectiveness:** Achieve 1-2 within reasonable budget (<$500 for 2m × 1m machine)

We'll examine three construction approaches:

- **Welded tube frames** (most common, good stiffness/cost)
- **Extrusion frames** (bolt-together, lower stiffness but reconfigurable)
- **Cast/fabricated plates** (maximum flatness, high cost)

### Learning Objectives

By the end of this section, you will be able to:

1. Calculate required base frame stiffness from machine specifications
2. Design welded rectangular perimeters with optimal cross-bracing
3. Select appropriate mounting patterns for linear rails
4. Predict and control base frame twist under asymmetric loading
5. Specify flatness tolerances for welded structures
6. Design bolt-together extrusion frames with adequate rigidity
7. Implement stress-relief procedures for welded bases

---

## Base Frame Functional Requirements

### Load Cases

The base frame experiences:

**1. Dead Load (Static, Permanent)**
```
F_dead = (m_rails + m_gantry + m_spindle + m_table) × g
```

Typical: 50-200 kg total → 500-2,000 N distributed over base

**2. Cutting Forces (Dynamic, Cyclic)**
```
F_cutting = 100-2,000 N (depends on material and depth of cut)
```

Acts through gantry → reacted by base at rail mounting points

**3. Acceleration Forces (Dynamic, Transient)**
```
F_accel = m_moving × a_max
```

For m_moving = 20 kg, a_max = 3 m/s²: F_accel = 60 N (small compared to cutting forces)

**4. Thermal Loads (Quasi-Static)**

Temperature gradient ΔT = 5-10°C causes differential expansion:
```
ΔL = α × L × ΔT = 11.7×10⁻⁶ × 2000 mm × 10°C = 0.234 mm
```

Managed through symmetric design (Section 1.8), not base stiffness.

### Stiffness Requirements

From deflection budget (Section 1.3), base allocated 15% of total tolerance:

For T = 0.10 mm total tolerance:
```
δ_base_max = 0.15 × T = 0.015 mm = 15 μm
```

Required base stiffness:
```
k_base = F_cutting / δ_base_max
```

For F_cutting = 1,000 N:
```
k_base = 1,000 N / 0.015 mm = 66,667 N/mm = 66.7 N/μm
```

This is **extremely stiff**—comparable to machine tool cast iron bases. Achieving this with fabricated steel requires careful design.

### Flatness Requirements

Linear rails require mounting surface flatness:

| Rail Type | Flatness Requirement | Base Tolerance |
|-----------|---------------------|----------------|
| **Round rail (SBR/TBR)** | ±0.05 mm per 300 mm | 0.05 mm/m (easy) |
| **Profiled rail (HGR/MGN)** | ±0.02 mm per 300 mm | 0.02 mm/m (moderate) |
| **Box way (grinding machine)** | ±0.005 mm per 300 mm | 0.005 mm/m (difficult) |

**CNC router/plasma bases:** Target 0.05 mm/m (achievable with welded construction)
**Precision milling bases:** Target 0.02 mm/m (requires machined mounting plates)

---

## Welded Tube Frame Construction

### Rectangular Perimeter Design

The simplest effective base: rectangular perimeter from square or rectangular hollow sections (SHS/RHS).

```
   Plan View (looking down)

   ┌────────────────────────────┐
   │                            │
   │   Y-axis rail mounting     │
   │   ════════════════════     │
   │                            │
   │                            │
   │   ════════════════════     │
   │   Y-axis rail mounting     │
   │                            │
   └────────────────────────────┘

   ←────────── L_x ──────────→

   Front elevation (side view)

   ┌────────────────────────────┐  ← Top surface (rail mounting)
   ║                            ║
   ║   80×80×5 SHS (example)    ║  h_frame
   ║                            ║
   └────────────────────────────┘  ← Feet (bolt to floor)
```

**Design Parameters:**

- **Section size:** 60×60×4 to 120×120×6 mm SHS (depends on span)
- **Frame height:** 80-150 mm (taller = stiffer but harder to level)
- **Overhang:** Extend 50-100 mm beyond rail mounting to allow adjustments

### Sizing the Perimeter Members

**Step 1: Determine Loading**

Assume worst-case: Cutting force F_cut applied at center of workspace, reacted through rails:

```
   Top view showing rail reaction points:

   R₁ ●═══════════════════●  R₂
      ↑                   ↑
      Rail 1             Rail 2

            ↓ F_cut
            ● (cutting point)
```

For cutting point at distance a from Rail 1, distance b from Rail 2:
```
R₁ = F_cut × b / (a + b)
R₂ = F_cut × a / (a + b)
```

Center position (a = b = L/2):
```
R₁ = R₂ = F_cut / 2
```

**Step 2: Model Perimeter as Beam**

The side members (parallel to rails) act as beams supporting rail loads:

```
   Side member beam:

   ●─────────────────●  ← Rail bolts (16-20 bolts over 1.5m length)
   ↑                 ↑
   Corner            Corner
   (welded support)  (welded support)

   Simplified: Distributed load w = R₁/L_x
```

**Step 3: Calculate Required I**

For simply supported beam with uniform load w:
```
δ_max = 5wL⁴ / (384EI)
```

Rearranging for required I:
```
I_required = 5wL⁴ / (384Eδ_max)
```

### Worked Example 1.4.1: Base Side Member Sizing

**Given:**
- Base dimensions: L_x = 2,000 mm (X direction), L_y = 1,200 mm (Y direction)
- Cutting force: F_cut = 800 N (worst-case for router in hardwood)
- Rail reaction per side: R = 400 N (distributed over 2,000 mm length)
- Base deflection budget: δ_max = 0.015 mm
- Material: A36 steel, E = 200 GPa

**Calculate distributed load on side member:**
```
w = R / L_x = 400 N / 2 m = 200 N/m
```

**Required second moment of area:**
```
I_req = 5wL⁴ / (384Eδ_max)
      = 5 × 200 × 2⁴ / (384 × 200×10⁹ × 0.015×10⁻³)
      = 16,000 / (1,152,000,000)
      = 1.39 × 10⁻⁵ m⁴
      = 13,900,000 mm⁴
```

**Wait—this is enormous!** For comparison, a W200×31 I-beam has I = 21.4 × 10⁶ mm⁴. This calculation suggests we need almost that large a section just for the base.

**Error Check:** This assumes the side member is simply supported at corners only. In reality, the front and rear members provide continuous support (closed rectangular frame is far stiffer than individual beams).

**Revised Model:** Closed rectangular frame under distributed load is approximately 5-8× stiffer than simply-supported beam. Applying a factor of 6:

```
I_req_adjusted ≈ 13.9 × 10⁶ / 6 ≈ 2.3 × 10⁶ mm⁴
```

**Select standard section:**

| Section | I_xx (mm⁴) | I_yy (mm⁴) | Mass (kg/m) | Cost ($/m) |
|---------|------------|------------|-------------|------------|
| 80×80×5 SHS | 1.72 × 10⁶ | 1.72 × 10⁶ | 11.9 | 9.52 |
| 100×100×5 SHS | 3.46 × 10⁶ | 3.46 × 10⁶ | 15.0 | 12.00 |
| 120×120×6 SHS | 6.50 × 10⁶ | 6.50 × 10⁶ | 21.6 | 17.28 |

**Select 100×100×5 SHS:** I = 3.46 × 10⁶ mm⁴ > 2.3 × 10⁶ mm⁴ required (1.5× safety factor)

**Cost for complete perimeter:**
```
Perimeter = 2 × (2,000 + 1,200) = 6,400 mm = 6.4 m
Material cost = 6.4 m × $12.00/m = $76.80
```

Very affordable. This is why welded tube frames dominate hobbyist and mid-range professional CNC machines.

### Cross-Bracing Patterns

Rectangular perimeter alone has **low torsional rigidity**—frame twists under asymmetric loads. Cross-bracing (diagonal members) prevents this.

#### Pattern 1: X-Bracing (Most Effective)

```
   Top view:

   ┌─────────────────┐
   │╲               ╱│
   │ ╲             ╱ │
   │  ╲           ╱  │
   │   ╲         ╱   │
   │    ╲       ╱    │
   │     ╲     ╱     │
   │      ╲   ╱      │
   │       ╲ ╱       │
   │        ╳        │
   │       ╱ ╲       │
   │      ╱   ╲      │
   │     ╱     ╲     │
   │    ╱       ╲    │
   │   ╱         ╲   │
   │  ╱           ╲  │
   │ ╱             ╲ │
   │╱               ╲│
   └─────────────────┘
```

**Advantages:**
- Maximum torsional stiffness (prevents twist)
- Braces loaded in tension/compression (efficient)

**Disadvantages:**
- Obstructs bottom access (problematic for cable routing, chip removal)
- Requires precise fit-up (diagonal lengths must match exactly)

#### Pattern 2: Grid Bracing (Best for Large Bases)

```
   Top view:

   ┌─────┬─────┬─────┐
   │     │     │     │
   ├─────┼─────┼─────┤
   │     │     │     │
   ├─────┼─────┼─────┤
   │     │     │     │
   └─────┴─────┴─────┘
```

**Advantages:**
- Creates mounting points for intermediate supports
- Easier fabrication (all members perpendicular)
- Good for machines with central work table support

**Disadvantages:**
- Less torsionally stiff than X-bracing (requires more material)
- More welding labor (more joints)

#### Pattern 3: Perimeter-Only with Thick Top Plate (Compromise)

```
   Side view:

   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ← 10-15 mm steel plate
   ┌────────────────┐
   │                │
   │   80×80×5 SHS  │  80-120 mm
   │                │
   └────────────────┘
```

**Advantages:**
- Flat machined top surface (excellent for rail mounting)
- No internal obstructions
- Top plate provides torsional rigidity

**Disadvantages:**
- Expensive (15mm plate costs $60-120 per m²)
- Heavy (15mm × 2m × 1m plate = 235 kg)
- Requires stress-relief after welding (Section 1.8)

**Recommendation:**
- **Small machines (<1.5m):** Perimeter only, no bracing needed
- **Medium machines (1.5-2.5m):** X-bracing or grid
- **Large machines (>2.5m):** Grid bracing + intermediate supports

### Corner Joint Design

Corners are **critical stress points**—poorly welded corners crack under cyclic loading.

#### Butt Joint with Full Penetration Weld (Best)

```
   Top view of corner:

   ╔═══════════════
   ║
   ║    Tube 1
   ║
   ╠═══════════════  ← Weld seam (all 4 sides of tube)
   ║
   ║    Tube 2
   ║
   ╚═══════════════
```

**Procedure:**
1. Cut tube ends square (±0.5°) using miter saw or band saw + sanding
2. Tack weld in 4 places (one per side)
3. Check squareness with framing square (±1 mm over 1,000 mm)
4. Full weld all 4 sides (GMAW, E70S-6 wire, 0.035" diameter, 18-22V, 180-220 IPM)
5. Allow to cool naturally (no quenching—causes distortion)

**Weld size:** Fillet weld leg length ≥ 0.7 × wall thickness (for 5mm tube → 3.5mm leg minimum)

#### Miter Joint (Aesthetic, Not Stronger)

```
   Miter cut (45° angles):

   ╔═══════════╗
   ║           ║
   ║           ╚═══
   ║
   ╚═══════════════
```

**Advantages:** Looks professional, no tube end visible

**Disadvantages:**
- Requires accurate 45° cuts (miter saw or well-tuned band saw)
- Larger weld area (more labor)
- No strength advantage over butt joint

**Recommendation:** Use butt joints for bases (faster fabrication, adequate strength). Reserve miters for visible frame elements (enclosure structure, aesthetic panels).

---

## Extrusion Frame Construction

### 80/20 and V-Slot Extrusion Systems

Bolt-together aluminum extrusions (80/20, T-slot, V-slot) offer:

**Advantages:**
1. **No welding required:** Assemble with bolts and corner brackets
2. **Reconfigurable:** Disassemble and modify layout
3. **Integrated cable channels:** T-slots route wiring
4. **Precision:** Extrusions are straight to 0.5 mm/m (better than welded steel)

**Disadvantages:**
1. **Lower stiffness:** Bolted joints flex under load (2-4× more than welded)
2. **Higher cost:** $4-8 per foot for 40×80mm extrusion (vs $1.50 for equivalent RHS)
3. **Joint complexity:** Requires many fasteners (8-12 bolts per corner for rigidity)
4. **Thermal expansion:** α_aluminum = 2× α_steel

### Extrusion Frame Design Rules

**Rule 1: Larger extrusions than equivalent steel**

For similar stiffness to 80×80×5 SHS steel, use 40×80mm aluminum extrusion (note: aluminum is half the modulus, so requires ~1.5× larger section).

**Rule 2: Bolted joints need gussets**

Simple L-bracket corners are too flexible. Use:

```
   Gusseted corner bracket:

   ╔═══════════╗
   ║           ║
   ║    ┌───── ║ ← Extrusion 1
   ║    │  ╱   ║
   ║    │╱     ║
   ║────┘      ║
   ║           ║
   ╚═══════════╝
     ↑
     Extrusion 2

     Gusset plate (6mm) with 6-8 bolts per corner
```

**Rule 3: Add cross-bracing**

Extrusion frames **require diagonal bracing** (even small machines). Rectangular perimeter alone is too flexible.

**Rule 4: Vertical height ≤ 1× base width**

Tall extrusion frames (h > width) are unstable. Keep low profile.

### Worked Example 1.4.2: Extrusion Frame Cost Comparison

**Steel welded frame (from Example 1.4.1):**
- Perimeter: 6.4 m × $12/m = $76.80
- Diagonal bracing: 3.5 m × $8/m = $28.00 (smaller sections for braces)
- Welding labor: 8 corners × 10 min × $1.25/min = $100
- **Total: $204.80**

**Aluminum extrusion frame:**
- Perimeter: 6.4 m × $6.50/m = $41.60 (for 40×80mm extrusion)
- Diagonal bracing: 3.5 m × $5.00/m = $17.50
- Corner brackets: 4 corners × $15 = $60.00
- Fasteners (80 M6 bolts + T-nuts): $25.00
- Assembly labor: 3 hours × $50/hr = $150 (less skilled than welding)
- **Total: $294.10**

**Result:** Extrusion frame costs 1.44× more ($294 vs $205) but requires no welding equipment. For hobbyists without welders, this trade is acceptable. For production shops with welding capability, steel is clearly more economical.

---

## Cast and Fabricated Plate Bases

### When to Use Solid Plates

Precision milling machines (tolerances <0.025 mm) require flatness <0.01 mm/m—unachievable with tube frames. Two options:

1. **Cast iron plate** (most professional mills and lathes)
2. **Welded structure + machined plate** (large-format CNC routers)

### Welded Steel Structure with Bolt-On Plate

```
   Side elevation:

   ████████████████████  ← 15mm steel plate (machined flat)

   ┌──┬──┬──┬──┬──┬──┐  ← Grid of 60×60×4 SHS
   │  │  │  │  │  │  │
   │  │  │  │  │  │  │  120mm
   │  │  │  │  │  │  │
   └──┴──┴──┴──┴──┴──┘

   ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡  ← Feet (adjustable, M16 bolts)
```

**Design:**
1. Weld grid structure (spacing 300-400 mm) from SHS/RHS
2. Bolt 12-20 mm steel plate on top (do NOT weld—causes warpage)
3. Machine top plate flat (face mill or surface grinder)

**Flatness achievable:** 0.02-0.05 mm/m after machining

**Cost breakdown (2m × 1m base):**
- Grid structure (steel + welding): $250
- 15mm × 2000 × 1000 plate: 235 kg × $1.20/kg = $282
- Machining (face milling 2 m²): 6 hours × $85/hr = $510
- **Total: $1,042**

Compare to commercial machine tool cast iron base: $3,000-8,000. The fabricated approach saves 65-87% while achieving 70-80% of the performance.

### Cast Iron Plate Bases

Gray cast iron (GG-25 / ASTM A48 Class 35) provides:

- **Superior damping:** ζ = 0.003-0.006 (5-10× steel)
- **Dimensional stability:** No residual stresses from welding
- **Machinability:** Excellent surface finish (Ra 0.8-1.6 μm)
- **Thermal stability:** α = 10.5×10⁻⁶/°C (10% better than steel)

**When justified:**
- Production milling machines (>$30k total cost)
- Grinding machines (surface finish critical)
- Measurement CMMs (thermal stability critical)

**Procurement:** Cast iron plates are custom castings (pattern required). Typical lead time: 12-20 weeks. Cost: $15-30/kg.

---

## Mounting Surface Preparation

### Flatness Measurement

Use precision straight edge (1,000 mm, grade 0 per DIN 874) and feeler gauges:

**Procedure:**
1. Place straight edge on mounting surface in 6-8 locations (various orientations)
2. Insert feeler gauges under straight edge, find maximum gap
3. Record gap at each position
4. Calculate flatness: (max gap) / (straight edge length)

**Acceptable values:**
- Welded tube frame: 0.05-0.10 mm per 1,000 mm
- Machined plate: 0.01-0.03 mm per 1,000 mm
- Ground surface: <0.005 mm per 1,000 mm

### Surface Grinding for Rail Mounting

For profiled linear rails (HGR15, HGR20) requiring ±0.02 mm flatness:

**Option 1: Hand Grinding**

1. Weld mounting plates (10 mm × 100 mm × length) to frame
2. Surface grind plates on manual surface grinder (or pay machine shop $60-100/hr)
3. Check flatness with straight edge + dial indicator

**Option 2: Planing**

Use metal planing machine (shaper) to machine top surface:
- Cost: $80-120/hr machine time
- Achievable flatness: 0.03-0.05 mm/m
- Suitable for long bases (>2m) where grinding is impractical

**Option 3: Epoxy Granite Skim Coat**

1. Install rail on base, shimmed to desired height and flatness (±0.05 mm)
2. Apply polymer concrete (epoxy + granite aggregate) around rail
3. Allow to cure 48 hours
4. Remove rail, clean epoxy from mounting surface
5. Re-install rail (now conforms to epoxy surface)

Achieves 0.02-0.04 mm flatness for $5-10/m of rail length.

---

## Twist Prevention and Analysis

### The Twist Problem

Asymmetric loading causes base frame to twist:

```
   Top view of base under asymmetric load:

   A┌──────────────┐B     ← Corner A lifts
    │       ↓ F    │
    │       ●      │      ← Load offset to one side
    │              │
   D└──────────────┘C     ← Corner D presses down

   Twist angle θ causes diagonal distortion:
   AC length increases, BD length decreases
```

**Effect on cutting accuracy:**

For base L × W with twist angle θ (radians):
```
Diagonal error = θ × √(L² + W²) / 2
```

For θ = 0.001 rad (0.057°, barely perceptible), L = 2m, W = 1m:
```
Error = 0.001 × √(4 + 1) / 2 = 0.001 × 1.118 = 0.0011 m = 1.1 mm
```

**This is enormous!** A tiny twist angle destroys accuracy.

### Diagonal Measurement Test

Check twist by measuring diagonals:

```
Measure diagonals AC and BD.
If |AC - BD| < 1 mm, twist is acceptable (<0.0005 rad).
If |AC - BD| > 2 mm, investigate and correct.
```

**Causes of twist:**
1. Uneven floor (base rocks on 3 feet)
2. Asymmetric welding (one side cools before other, shrinks)
3. Missing or inadequate cross-bracing
4. Off-center heavy component (spindle, electronics)

### Twist Stiffness Calculation

Torsional stiffness of rectangular frame with X-bracing:

```
k_twist = G × J_equiv / L_diagonal
```

Where:
- G = shear modulus (for steel, G = E / 2.6 = 77 GPa)
- J_equiv = equivalent polar moment (complex, depends on bracing)
- L_diagonal = length of diagonal brace

For frames **without adequate bracing**, twist stiffness is 10-50× lower (unacceptable).

**Design Rule:** Always include diagonal bracing for bases >1m × 1m.

---

## Leveling and Adjustment

### Adjustable Feet Design

Base frames need height adjustment for:
1. Leveling on uneven floors (±5-20 mm range typical)
2. Vibration isolation (optional rubber pads)

**Foot construction:**

```
   ═══════════════════  ← Base frame tube
         │
         │  M16 bolt (welded nut inside tube)
         │
         ↓
     ┌───────┐
     │       │  T-nut (adjustment)
     └───────┘
         │
      ╱═══╲    ← Rubber pad (optional)
     ╱     ╲
    ═════════  ← Floor
```

**Components:**
- M16 or M20 bolt (length: 80-120 mm)
- Weld nut or tapped plate inside tube
- Lock nut to prevent loosening
- Rubber pad (optional, 10 mm thick, 60 durometer Shore A)

**Adjustment procedure:**
1. Place precision level on base (0.02 mm/m resolution)
2. Adjust feet until level reads <0.02 mm/m in both X and Y directions
3. Re-check diagonals (should not change >0.5 mm during leveling)
4. Tighten lock nuts

### Securing to Floor

For machines >150 kg or with rapid motions (high acceleration), bolt base to floor:

**Concrete floor:**
1. Mark hole positions (typically 4-6 bolts, one near each foot)
2. Drill 12-16 mm holes, 75-100 mm deep
3. Install wedge anchors or drop-in anchors (M12-M16)
4. Torque to 80-120 N·m

**Wood floor:**
1. Locate floor joists (use stud finder)
2. Drill pilot holes
3. Install 12mm lag screws, 100-150 mm length
4. Torque to 40-60 N·m

Bolting to floor reduces transmitted vibration and prevents machine "walking" during rapid moves.

---

## Stress-Relief Heat Treatment

### Why Welding Causes Distortion

Welding locally heats material to 1,400-1,600°C, then cools rapidly. This creates:

1. **Thermal expansion:** Hot zone expands, constrained by cold surrounding metal
2. **Plastic deformation:** Hot zone yields in compression (σ_y drops to ~50 MPa at welding temperature)
3. **Residual stress:** On cooling, the plastically deformed zone shrinks, pulling on adjacent material

**Result:** Welded frames are **not stress-free**. Residual stresses σ_residual can reach 100-200 MPa (40-80% of yield strength), causing:
- Distortion over time (frame "relaxes" over weeks/months)
- Reduced fatigue life (mean stress component in S-N curve)
- Poor dimensional stability (cutting forces relieve stress → geometry shifts)

### Stress-Relief Procedure (Thermal)

**Full stress relief (for precision bases):**

1. **Preheat:** 150-200°C, 1 hour (reduces thermal gradient during heating)
2. **Soak:** 550-650°C, 1 hour per 25 mm thickness (allows diffusion and dislocation rearrangement)
3. **Cool:** Slow cool in furnace, <50°C/hr to 200°C, then air cool

**Reduces residual stress by 80-95%.**

**Equipment required:**
- Annealing furnace or oven (large enough for frame, typically 1-3 m³ interior)
- Thermocouple monitoring
- Inert atmosphere or air (oxidation acceptable for structural steel)

**Cost:** $300-800 per cycle (commercial heat treat shop)

**Alternative: Vibration stress relief**

Clamp frame to vibration table (eccentric mass vibrator, 10-50 Hz, 0.5-2.0 g acceleration), run for 30-60 minutes. Claims to reduce residual stress by 30-60% (controversial—some studies show benefit, others minimal effect).

Cost: $150-300 per session (vs $500+ for thermal)

### When Stress Relief is Required

**Always required:**
- Precision machining bases (tolerance <0.05 mm)
- Bases with machined features (linear rail mounting surfaces)
- Large frames (>2m × 1.5m) with extensive welding

**Not required:**
- Small hobby machines (<1m × 1m)
- Frames with bolted-on machined plates (plate can be stress-relieved separately)
- Tube frames without precision machined features

---

## Summary and Design Checklist

### Base Frame Design Sequence

1. **Calculate loads:** Dead load + cutting force + acceleration
2. **Allocate deflection budget:** 10-20% of total tolerance to base
3. **Select construction:** Welded tube (best), extrusion (no welding), or plate (precision)
4. **Size perimeter:** Use beam deflection equations + closed-frame stiffness factor
5. **Add cross-bracing:** X-bracing or grid for bases >1.5m span
6. **Design corners:** Butt-welded with full-penetration welds
7. **Plan mounting surfaces:** Machined plates or epoxy skim coat for precision rails
8. **Implement leveling:** Adjustable feet with M16-M20 bolts
9. **Check twist:** Measure diagonals (<1 mm difference required)
10. **Stress-relieve if needed:** Thermal anneal for precision bases

### Design Checklist

**Structural:**
- [ ] Base stiffness k > 50 N/mm (minimum for CNC router)
- [ ] Perimeter section I > calculated requirement × 1.5 (safety factor)
- [ ] Cross-bracing installed (diagonal or grid)
- [ ] Corner welds full-penetration, 4-sided

**Geometric:**
- [ ] Diagonals measured, difference <1 mm
- [ ] Flatness <0.05 mm/m (tube frame) or <0.02 mm/m (machined surface)
- [ ] Mounting surface continuous or plates at 300-400 mm spacing

**Assembly:**
- [ ] Adjustable feet at all 4-6 corners
- [ ] Leveling <0.02 mm/m in both axes
- [ ] Secured to floor (machines >150 kg or high acceleration)

**Quality:**
- [ ] Stress-relief performed (if precision base)
- [ ] Visual inspection: no cracks, complete weld penetration
- [ ] Load test: Apply 1.5× rated cutting force, measure deflection

---

## Practical Exercises

### Exercise 1.4.1: Base Frame Sizing

Design base for:
- Machine dimensions: 1,800 mm × 1,000 mm working area
- Cutting force: 600 N
- Tolerance: 0.08 mm
- Budget: $300 material + fabrication

**Tasks:**
1. Calculate base deflection budget (assume 15% allocation)
2. Size perimeter members (choose SHS/RHS)
3. Design cross-bracing pattern
4. Calculate material cost
5. Sketch welding sequence

### Exercise 1.4.2: Twist Analysis

Given: 2,000 mm × 1,200 mm base, diagonal measurements:
- AC = 2,332 mm
- BD = 2,328 mm

**Tasks:**
1. Calculate twist angle θ
2. Estimate resulting diagonal error at corners
3. If tolerance is ±0.10 mm, does this base pass?
4. Propose corrective actions (identify likely cause)

### Exercise 1.4.3: Extrusion vs Welded Cost Analysis

Compare two designs for 1,500 mm × 900 mm base:
- **Design A:** Welded 80×80×5 SHS with X-bracing
- **Design B:** Bolted 40×80mm extrusions with gusset corners

**Tasks:**
1. Calculate material costs (use prices from section)
2. Estimate labor (welding 4 hours @ $50/hr, assembly 2 hours @ $40/hr)
3. Compare total cost
4. Predict relative stiffness (which is stiffer?)
5. Recommend one design with justification

---

**Next Section Preview:** [Section 1.5: Gantry Beam Design](section-01.5-gantry-beam-design.md) will address the most critical structural member—the gantry beam that spans the working area and supports the cutting tool. This is where deflection is most severe and requires careful optimization of section geometry, material, and reinforcement.

---

## References

1. **AISC Steel Construction Manual**, 15th Ed. - Structural steel member design
2. **AWS D1.1 Structural Welding Code** - Welding procedures and quality standards
3. **Oberg, E. et al.** - *Machinery's Handbook*, 31st Ed. (2020) - Machine tool base design practices
4. **80/20 Inc. Technical Reference** - [www.8020.net](http://www.8020.net) - Extrusion frame design
5. **Blodgett, O.W.** - *Design of Welded Structures* (1966) - Classic reference for welded frame analysis
