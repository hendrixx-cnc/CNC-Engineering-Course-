# Section 1.2: Material Selection and Properties

## Introduction

Material selection for CNC machine frames is a multivariable optimization problem balancing stiffness, weight, thermal stability, machinability, weldability, cost, and availability. Unlike aerospace or automotive applications where weight minimization drives design, CNC frames prioritize **stiffness per unit cost** and **thermal stability**. A 2,000 kg steel frame costing $4,000 often outperforms a 600 kg aluminum frame costing $12,000 when stiffness and thermal performance are properly valued.

This section presents quantitative methods for material selection, moving beyond subjective "engineering judgment" to data-driven decision making. We'll examine the dominant materials used in professional CNC construction: mild steel (A36/S275), alloy steels (4140/42CrMo4), aluminum alloys (6061-T6, 7075-T6), cast iron, and emerging composites.

### Learning Objectives

By the end of this section, you will be able to:

1. Calculate stiffness-to-weight and stiffness-to-cost ratios for material comparison
2. Predict thermal drift from material CTE and temperature gradients
3. Select appropriate structural steel sections using AISC/Eurocodes
4. Specify surface treatments and corrosion protection systems
5. Evaluate trade-offs between welded steel and bolted aluminum construction
6. Apply material property databases (MatWeb, MMPDS) to frame design decisions

---

## Fundamental Material Properties

### The Stiffness Equation Revisited

Frame deflection under load F with beam length L, modulus E, and second moment of area I:

```
δ = FL³/(48EI)    (simply supported beam, center load)
```

For a given geometry (fixed L, I), deflection is inversely proportional to Young's modulus E. However, **I depends on material thickness**, which depends on density ρ for fixed mass. The true performance metric is **specific stiffness** E/ρ or **E^(1/3)/ρ** for bending-limited designs.

For cost-constrained designs (the common case), the relevant metric is **stiffness per dollar**:

```
Cost Merit Index = E / (ρ × C_m)
```

Where:
- E = Young's modulus (GPa)
- ρ = Density (kg/m³)
- C_m = Material cost per kg ($/kg)

### Material Property Table: Structural Materials

| Material | E (GPa) | ρ (kg/m³) | σ_y (MPa) | α (10⁻⁶/°C) | C_m ($/kg) | E/ρ (MJ/kg) | E/(ρC_m) |
|----------|---------|-----------|-----------|-------------|------------|-------------|----------|
| **Mild Steel A36** | 200 | 7,850 | 250 | 11.7 | 0.80 | 25.5 | 31.8 |
| **Steel 4140 HT** | 205 | 7,850 | 415 | 11.5 | 3.50 | 26.1 | 7.5 |
| **Aluminum 6061-T6** | 69 | 2,700 | 275 | 23.6 | 3.20 | 25.6 | 8.0 |
| **Aluminum 7075-T6** | 72 | 2,810 | 505 | 23.2 | 6.50 | 25.6 | 3.9 |
| **Cast Iron GG-25** | 110 | 7,200 | 250 | 10.5 | 1.20 | 15.3 | 12.7 |
| **Granite (reference)** | 50 | 2,650 | 20 (comp) | 8.0 | 15.00 | 18.9 | 1.3 |
| **Polymer Concrete** | 30 | 2,400 | 80 (comp) | 15.0 | 8.00 | 12.5 | 1.6 |

**Key Observations:**

1. **E/ρ is nearly identical** for structural steel and aluminum (~25-26 MJ/kg), meaning equal-mass frames have similar stiffness if geometries are optimized.

2. **Cost merit E/(ρC_m) strongly favors mild steel** (31.8 vs 8.0 for 6061-T6), meaning you get 4× more stiffness per dollar with steel.

3. **Thermal expansion α is 2× higher** for aluminum (23.6 vs 11.7 × 10⁻⁶/°C), requiring more careful thermal design.

4. **High-strength alloys (4140, 7075) offer no stiffness advantage** but excel where yield strength limits design (bolted joints, thin-wall sections).

### Worked Example 1.2.1: Material Selection for 2m Gantry Beam

**Scenario:** Design a 2,000 mm gantry beam to support 500 N cutting force with maximum deflection δ_max = 0.05 mm. Choose between:
- Option A: Steel rectangular tube 100×50×5 mm (A36)
- Option B: Aluminum rectangular tube 120×60×6 mm (6061-T6)

**Steel Option (A36, E = 200 GPa):**

Second moment of area for rectangular tube:
```
I_steel = (b_o h_o³ - b_i h_i³)/12
        = (100×100³ - 90×90³)/12 × 10⁻¹²
        = 2.71 × 10⁻⁶ m⁴
```

Deflection (simply supported, center load):
```
δ_steel = FL³/(48EI)
        = 500 × 2³ / (48 × 200×10⁹ × 2.71×10⁻⁶)
        = 0.0154 mm  ✓ (meets requirement)
```

Mass per meter:
```
m_steel = ρ × A = 7850 × (100×50 - 90×40) × 10⁻⁶
        = 11.8 kg/m → 23.6 kg total
```

Material cost:
```
C_steel = 23.6 kg × $0.80/kg = $18.88
```

**Aluminum Option (6061-T6, E = 69 GPa):**

```
I_aluminum = (120×120³ - 108×108³)/12 × 10⁻¹²
           = 4.63 × 10⁻⁶ m⁴
```

```
δ_aluminum = 500 × 2³ / (48 × 69×10⁹ × 4.63×10⁻⁶)
           = 0.0260 mm  ✓ (meets requirement)
```

```
m_aluminum = 2700 × (120×60 - 108×48) × 10⁻⁶ = 5.5 kg/m → 11.0 kg total
```

```
C_aluminum = 11.0 kg × $3.20/kg = $35.20
```

**Decision Matrix:**

| Criterion | Steel | Aluminum | Winner |
|-----------|-------|----------|--------|
| Deflection (mm) | 0.0154 | 0.0260 | Steel (3.3× stiffer) |
| Mass (kg) | 23.6 | 11.0 | Aluminum (2.1× lighter) |
| Cost ($) | 18.88 | 35.20 | Steel (1.9× cheaper) |
| Thermal drift (5°C) | 0.117 mm | 0.236 mm | Steel (2× better) |
| Stiffness/cost | 1.06 N/mm/$ | 0.57 N/mm/$ | Steel (1.9× better) |

**Conclusion:** Steel offers superior stiffness, cost, and thermal performance. Aluminum's weight advantage is irrelevant for a stationary frame (moving mass is in carriages, covered in Module 3). **Select Option A (steel).**

---

## Mild Steel: The Workhorse Material

### ASTM A36 / S235JR / S275JR Properties

Mild steel (low-carbon steel, <0.3% C) is the default choice for professional CNC frames due to its optimal balance of properties:

**Advantages:**
1. **Cost:** $0.70-1.00/kg in structural shapes (angle, channel, tube)
2. **Weldability:** Excellent with GMAW/SMAW, no special procedures required
3. **Availability:** Stocked worldwide in 6-12m lengths, dozens of profiles
4. **Machinability:** Easily drilled, tapped, milled for mounting holes
5. **Stiffness:** E = 200 GPa, same as exotic alloy steels
6. **Thermal stability:** α = 11.7×10⁻⁶/°C, half that of aluminum

**Disadvantages:**
1. **Corrosion:** Requires paint/powder coating (adds $2-4/kg)
2. **Weight:** ρ = 7,850 kg/m³, 3× denser than aluminum
3. **Yield strength:** σ_y = 250 MPa, adequate but not exceptional

### Common Structural Sections

Professional frame builders use **hot-rolled structural steel** shapes per AISC (American) or Eurocodes (European):

| Section Type | Designation Example | I_xx (cm⁴) | Mass (kg/m) | Applications |
|--------------|---------------------|------------|-------------|--------------|
| **Rectangular Tube** | 100×50×5 RHS | 158 | 11.8 | Gantry beams, base rails |
| **Square Tube** | 80×80×4 SHS | 182 | 9.6 | Vertical posts, cross-bracing |
| **I-Beam** | W150×18 | 1,350 | 18.0 | Heavy-duty gantries (>2m span) |
| **Angle** | L50×50×5 | 18 (each leg) | 3.77 | Bracing, light structures |
| **C-Channel** | C100×50 | 109 | 9.65 | Reinforcement, cable trays |

**Selection Rule:** For bending-dominated loading (gantry beams), maximize I/mass ratio. For compression (columns), maximize radius of gyration r = √(I/A).

### Worked Example 1.2.2: Tube vs I-Beam Comparison

**Scenario:** 3-meter gantry span, 1,000 N cutting force, δ_max = 0.10 mm.

**Option A:** 120×60×6 RHS (I = 290 cm⁴ = 2.90×10⁻⁶ m⁴, mass = 15.2 kg/m)

```
δ_RHS = 1000 × 3³ / (48 × 200×10⁹ × 2.90×10⁻⁶)
      = 0.0967 mm  ✓
```

```
Mass = 15.2 kg/m × 3 m = 45.6 kg
Cost = 45.6 kg × $0.80/kg = $36.48
```

**Option B:** W150×18 I-beam (I = 1,350 cm⁴ = 13.5×10⁻⁶ m⁴, mass = 18.0 kg/m)

```
δ_I = 1000 × 3³ / (48 × 200×10⁹ × 13.5×10⁻⁶)
    = 0.0208 mm  ✓
```

```
Mass = 18.0 kg/m × 3 m = 54.0 kg
Cost = 54.0 kg × $0.80/kg = $43.20
```

**Analysis:**

| Metric | RHS | I-Beam | Ratio |
|--------|-----|--------|-------|
| Deflection (mm) | 0.097 | 0.021 | 4.6× stiffer |
| Mass (kg) | 45.6 | 54.0 | 1.18× heavier |
| I/mass (cm⁴/kg) | 19.1 | 25.0 | 1.31× more efficient |

**Conclusion:** I-beam offers 4.6× lower deflection for only 18% more mass—**clear winner** for long-span gantries. RHS is preferred for shorter spans (<1.5m) where I-beam's superior stiffness is unnecessary and the closed section provides better torsional rigidity.

---

## Alloy Steels: High-Performance Options

### 4140 / 42CrMo4 (Chrome-Molybdenum Steel)

Medium-carbon alloy steel (0.40% C, 1% Cr, 0.2% Mo) offering 1.7× higher yield strength than mild steel after heat treatment.

**Properties (quenched & tempered to 850°F/455°C):**
- σ_y = 415 MPa (60 ksi)
- σ_ult = 655 MPa (95 ksi)
- E = 205 GPa (no advantage over mild steel for stiffness)
- Hardness: 20-22 HRC (prevents galling in sliding contact)

**When to Use 4140:**

1. **Precision ground surfaces:** Linear rail mounting surfaces that must maintain flatness <0.01 mm/m. Heat-treated 4140 can be ground to Ra 0.4 μm and resists wear.

2. **Bolted joints under high preload:** Grade 8.8 bolt clamping forces generate contact stresses σ_c = √(EP/πLd) that can exceed mild steel's yield. 4140 prevents plastic deformation.

3. **Thin-wall structures:** When section thickness <3 mm, yield strength becomes the limiting factor (buckling resistance ∝ σ_y).

**Cost Premium:** 4140 bar stock costs $3.00-4.50/kg (4-5× mild steel). Use sparingly—only where mild steel demonstrably fails.

### Worked Example 1.2.3: Bolt Joint Bearing Stress

**Scenario:** M12 Grade 10.9 bolt (F_preload = 35 kN) through 10 mm plate. Check bearing stress.

Contact area under bolt head (d_head = 18 mm, d_hole = 13 mm):
```
A_bearing = π/4 (d_head² - d_hole²)
          = π/4 (18² - 13²) = 121.6 mm²
```

Bearing stress:
```
σ_bearing = F_preload / A_bearing
          = 35,000 N / 121.6 mm²
          = 288 MPa
```

**Check against material yield:**

- **Mild steel A36:** σ_y = 250 MPa → **FAILS** (1.15× overstress, will yield)
- **4140 HT:** σ_y = 415 MPa → **PASSES** (0.69× utilization, safe)

**Conclusion:** High-preload bolted joints in precision machines require hardened steel (4140, 4340) to prevent joint relaxation from plastic deformation.

---

## Aluminum Alloys: When Weight Matters

### 6061-T6 (Mg-Si Alloy)

Aluminum's primary advantage—low density (2,700 kg/m³ vs 7,850 kg/m³)—is **irrelevant for machine bases** where mass improves damping and stability. However, aluminum excels in specific niches:

**Valid Use Cases:**
1. **Portable machines:** Handheld routers, inspection CMMs moved between job sites
2. **Moving gantries:** CNC routers where the entire gantry translates in Y (rare; usually only the tool head moves)
3. **Corrosive environments:** Marine applications, chemical plants (with anodizing)
4. **Non-magnetic requirement:** Measuring systems near sensitive electronics

**Properties:**
- E = 69 GPa (34% of steel—requires 1.47× thicker sections for equal stiffness)
- σ_y = 275 MPa (good for an aluminum alloy)
- α = 23.6×10⁻⁶/°C (2× steel—thermal design is critical)
- Cost: $3.00-3.50/kg for extruded shapes (4× steel)

### Thermal Expansion Challenge

A 2-meter aluminum gantry beam subjected to ΔT = 5°C temperature gradient:

```
ΔL = α × L × ΔT
   = 23.6×10⁻⁶ /°C × 2000 mm × 5°C
   = 0.236 mm
```

This is **5× larger than typical machining tolerances** (0.05 mm). Mitigations:

1. **Symmetric thermal design:** Ensure uniform temperature distribution (Section 1.8)
2. **Thermal compensation in software:** Real-time linear correction (requires temperature sensors)
3. **Climate-controlled environment:** Maintain ±1°C stability (expensive)

**Cost Reality Check:**

Same gantry beam from Example 1.2.1:
- Steel: 23.6 kg × $0.80/kg = $18.88 (raw), $42.35 (powder coated)
- Aluminum: 11.0 kg × $3.20/kg = $35.20 (raw), $57.20 (anodized)

Aluminum saves 12.6 kg but costs $14.85 more (1.35× cost premium). For a stationary frame, this trade is **never justified** unless corrosion environment demands it.

### 7075-T6 (Zn-Mg Alloy)

"Aircraft aluminum" offers σ_y = 505 MPa (approaching mild steel) but E = 72 GPa (still only 36% of steel). Used in aerospace where weight saving justifies $6.50/kg cost. **Never economical for machine frames.**

---

## Cast Iron: The Traditional Choice

### Gray Cast Iron (GG-25 / ASTM A48 Class 35)

Cast iron dominated machine tool construction from 1850-1980 for good reasons:

**Advantages:**
1. **Damping:** Internal graphite flakes provide 5-20× higher damping ratio ζ than steel (reduces chatter)
2. **Castability:** Complex shapes (curved ribs, integral bosses) formed in single piece
3. **Thermal stability:** α = 10.5×10⁻⁶/°C, lowest of metallic materials
4. **Machinability:** Graphite acts as chip breaker; excellent surface finish
5. **Low residual stress:** Slow cooling rate minimizes locked-in stresses

**Disadvantages:**
1. **Cost:** Pattern making + foundry work = $12-25/kg (15-30× steel)
2. **Lead time:** 8-16 weeks for pattern, casting, aging, machining
3. **Brittle:** No plastic deformation before fracture (σ_ult = 250 MPa)
4. **Low E:** 110 GPa (55% of steel), requires thicker sections

**Modern Application:** Cast iron is still **optimal for precision grinding machines** where its superior damping justifies the cost (Haas UMC bases are cast iron). For CNC routers and plasma tables, fabricated steel is more economical.

### Polymer Concrete (Epoxy Granite)

Mixture of crushed granite (70-80%), quartz sand (10-15%), and epoxy resin (8-12%). Offers cast iron's advantages (damping, complex shapes, low CTE) at 1/2 the cost.

**Properties:**
- E = 30-45 GPa (highly variable with mix ratio)
- ρ = 2,400 kg/m³
- α = 10-20×10⁻⁶/°C
- ζ = 0.02-0.05 (10× steel)

**Process:** Pour into mold with embedded steel inserts for mounting, cure 24-48 hours at room temperature. Used in some CNC router bases (ShopBot, Multicam) but **not suitable for welded frames** (Section 1.7).

---

## Material Selection Decision Framework

### Step-by-Step Selection Procedure

**Step 1: Identify loading regime**
- Bending-dominated (long spans): Maximize I, use deep sections (I-beams)
- Compression-dominated (columns): Maximize r = √(I/A), use tubes
- Torsion-dominated (cantilevered beams): Maximize J, use closed sections (RHS/SHS)

**Step 2: Calculate required section modulus**

For bending (gantry beam):
```
S_required = M_max / σ_allowable = (FL/4) / (0.6 × σ_y)
```

Safety factor 1.67 (allowable stress = 0.6 × yield strength) per AISC.

**Step 3: Select material class**

| Scenario | Material | Justification |
|----------|----------|---------------|
| Standard CNC router/plasma, budget <$5k | **A36 mild steel** | Cost-optimal, adequate stiffness |
| Precision milling, tolerances <0.025mm | **Cast iron or steel + grinding** | Superior damping and thermal stability |
| Portable/moving gantry | **6061-T6 aluminum** | Weight reduction justified |
| Corrosive environment (marine, chemicals) | **6061-T6 + anodizing** | Corrosion resistance |
| High-preload bolted joints | **4140 heat-treated** | Prevents yielding under bolt load |
| Budget >$30k, ultra-precision | **Granite or polymer concrete** | Maximum thermal/vibration stability |

**Step 4: Check thermal drift**

Maximum temperature gradient expected (shop environment ΔT = 5-10°C, climate-controlled ΔT = 1-2°C):

```
Thermal drift = α × L × ΔT
```

If drift > 0.25 × positional tolerance, implement thermal compensation or choose lower-CTE material.

**Step 5: Perform cost analysis**

Total cost includes:
- Material cost: ρ × V × C_m
- Fabrication cost: Welding/joining labor (~$50-80/hr)
- Surface treatment: Powder coating ($2-4/kg), anodizing ($5-8/kg)
- Machining: Precision surfaces ($80-120/hr machine time)

Optimize total cost, not material cost alone.

### Worked Example 1.2.4: Complete Material Selection

**Requirements:**
- 1.5m × 1.0m × 0.3m tall machine base
- Positioning accuracy: ±0.05 mm
- Shop environment: ΔT = 8°C daily variation
- Budget: $800 for frame (material + fabrication)

**Option A: A36 Steel Welded Frame**

Structure: 80×80×4 SHS perimeter, 50×50×3 SHS cross-bracing

Material mass:
```
Perimeter: 4 members × 1.5m avg × 9.6 kg/m = 57.6 kg
Bracing: 6 members × 1.0m avg × 5.6 kg/m = 33.6 kg
Total = 91.2 kg
```

Costs:
```
Material: 91.2 kg × $0.80/kg = $72.96
Welding: 24 joints × 5 min × $1.25/min = $150
Powder coating: 91.2 kg × $2.50/kg = $228
Total = $450.96  ✓ (under budget)
```

Thermal drift:
```
ΔL = 11.7×10⁻⁶ × 1500 mm × 8°C = 0.140 mm
```
Drift = 2.8× tolerance → **requires thermal compensation in software**

**Option B: 6061-T6 Aluminum Bolted Frame**

Structure: 100×100×5 SHS perimeter, 60×60×3 SHS bracing (larger sections needed for E = 69 GPa)

Material mass:
```
Perimeter: 4 × 1.5m × 4.8 kg/m = 28.8 kg
Bracing: 6 × 1.0m × 2.1 kg/m = 12.6 kg
Total = 41.4 kg (2.2× lighter—irrelevant for base)
```

Costs:
```
Material: 41.4 kg × $3.20/kg = $132.48
Bolted assembly: 24 joints × 10 min × $1.25/min = $300
Anodizing: 41.4 kg × $6.00/kg = $248.40
Total = $680.88  ✓ (under budget, but close)
```

Thermal drift:
```
ΔL = 23.6×10⁻⁶ × 1500 mm × 8°C = 0.283 mm
```
Drift = 5.7× tolerance → **thermal compensation mandatory**

**Decision:** **Select Option A (steel)**
- $230 cheaper ($450.96 vs $680.88)
- 1/2 the thermal drift (0.140 mm vs 0.283 mm)
- Welded construction is more rigid than bolted (covered in Section 1.7)
- Weight disadvantage is irrelevant for stationary base
- Thermal compensation needed for both, but steel's lower CTE provides margin

---

## Surface Treatment and Corrosion Protection

### Bare Steel Oxidation

Unprotected steel oxidizes (rusts) at rate:

```
Depth loss = k × t^n
```

Where:
- k = 34-50 μm/year (indoor), 80-100 μm/year (outdoor, humid)
- n = 0.5-0.8 (sub-linear due to oxide barrier formation)
- t = time (years)

**After 5 years indoors:** 76-112 μm depth loss (0.076-0.112 mm)—unacceptable for precision machine.

### Protective Coatings Comparison

| Treatment | Thickness (μm) | Lifespan (years) | Cost ($/kg) | Appearance | Notes |
|-----------|----------------|------------------|-------------|------------|-------|
| **Powder Coating** | 60-120 | 10-15 (indoor) | $2-4 | Excellent, any color | Industry standard for machines |
| **Liquid Paint (2K epoxy)** | 100-200 | 5-10 | $1-2 | Good | Requires spray booth |
| **Hot-Dip Galvanizing** | 70-100 (Zn) | 20-50 (outdoor) | $1.50-2.50 | Dull gray | Adds 140 μm, affects tolerances |
| **Zinc-Rich Primer** | 75-100 | 10-20 | $0.80-1.50 | Matte gray | Good for weldments |
| **Black Oxide** | 1-2 | 1-2 (needs oil) | $0.30-0.60 | Matte black | Cosmetic only |

**Recommendation for CNC frames:** Powder coating (polyester or hybrid) applied to ASTM D3359 Grade 5B adhesion. Process:

1. Degrease (alkaline wash, 60°C)
2. Phosphate conversion coating (iron phosphate, 1-2 g/m²)
3. DI water rinse
4. Electrostatic powder application (60-80 μm target)
5. Cure 180°C × 15 min (for polyester)

Result: Hard, chip-resistant finish with excellent UV stability. Cost: $2.50-4.00/kg including prep.

### Aluminum Anodizing

Electrochemical process converting surface aluminum to Al₂O₃ (aluminum oxide) layer:

**Type II (Sulfuric Anodize):**
- Thickness: 10-25 μm
- Hardness: 60-70 HRC (surface)
- Dielectric strength: 20-30 V/μm
- Cost: $4-6/kg

**Type III (Hard Anodize):**
- Thickness: 25-75 μm
- Hardness: 70+ HRC (harder than many steels)
- Wear resistance: 10× Type II
- Cost: $6-9/kg

Anodizing provides excellent corrosion protection (passive oxide layer) plus electrical insulation. Critical for aluminum frames with electrical components mounted directly to structure.

---

## Emerging and Specialty Materials

### Carbon Fiber Reinforced Polymer (CFRP)

Unidirectional carbon fiber/epoxy composites offer extraordinary specific stiffness:

- E = 150-200 GPa (longitudinal)
- ρ = 1,600 kg/m³
- E/ρ = 94-125 MJ/kg (5× steel)

**Why not use CFRP for frames?**

1. **Anisotropy:** Stiffness only in fiber direction. Multi-axial loads require complex layups.
2. **Cost:** $40-80/kg for aerospace-grade prepreg (50-100× steel)
3. **Joining:** Cannot be welded; adhesive or bolted joints create stress concentrations
4. **Thermal expansion mismatch:** α_longitudinal ≈ -0.5×10⁻⁶/°C (yes, negative!) but α_transverse ≈ 30×10⁻⁶/°C
5. **Machinability:** Abrasive; requires carbide/diamond tooling

**Valid applications:** CFRP tubes for very long spans (>5m) where weight savings justify cost (large-format CNC routers). Hybrid construction: CFRP gantry beam + steel base.

### Sandwich Panels (Steel-Polymer-Steel)

0.5-1.0 mm steel skins bonded to polyurethane foam core (30-50 mm thick). Provides high I/mass ratio for flat panels (machine enclosures, chip guards) but **not suitable for primary structure** (core shear strength only 0.5-2 MPa).

---

## Summary and Selection Guidelines

### Quick Reference Table

| Machine Type | Recommended Material | Section Type | Justification |
|--------------|---------------------|--------------|---------------|
| **CNC Router (hobby, <$3k)** | A36 mild steel | 50×50×3 to 80×80×4 SHS | Cost-optimal |
| **CNC Router (pro, <$10k)** | A36 mild steel | 80×80×4 to 120×60×6 RHS | Best stiffness/cost |
| **Plasma Table** | A36 mild steel | 100×50×5 RHS, water table | Welded construction preferred |
| **Milling Machine (Al/plastic)** | A36 or cast iron | Cast base + steel gantry | Damping for chatter reduction |
| **Precision Grinder** | Cast iron (GG-25) | Monolithic casting | Maximum thermal/vibration stability |
| **Portable CMM** | 6061-T6 aluminum | Extruded profiles | Weight reduction critical |
| **Large-Format Router (>2m)** | A36 steel or CFRP hybrid | W-beam or CFRP tube | Minimize gantry deflection |

### Critical Design Rules

1. **Stiffness comes from geometry (I), not material (E).** A 120×60 RHS is 2× stiffer than 100×50 RHS of the same material—much more effective than switching materials.

2. **Optimize cost per unit stiffness,** not weight. Mild steel delivers 4× more stiffness per dollar than aluminum for machine frames.

3. **Thermal expansion is 2× worse for aluminum.** If positioning accuracy < 0.1 mm, steel's lower CTE provides inherent advantage.

4. **High-strength alloys (4140, 7075) don't improve stiffness.** Reserve them for bolted joints and precision ground surfaces where yield strength matters.

5. **Surface treatment costs $2-6/kg**—include this in total cost comparison. A "cheap" aluminum frame becomes expensive after anodizing.

6. **Cast iron is optimal for precision machines** where budget permits ($20-30k+ frames). Its superior damping and thermal stability justify the cost premium.

---

## Practical Exercises

### Exercise 1.2.1: Material Selection for Custom Gantry

Design a 2.4m gantry beam for CNC router, 600 N cutting force, δ_max = 0.08 mm, budget $150 for beam only (material + coating).

**Tasks:**
1. Calculate required I using beam deflection equation
2. Select 3 candidate sections (steel RHS, steel I-beam, aluminum RHS)
3. Calculate deflection, mass, cost for each
4. Rank by stiffness/cost ratio
5. Check thermal drift (ΔT = 7°C)
6. Make final selection with written justification

### Exercise 1.2.2: Bolt Joint Bearing Stress Analysis

M10 Grade 8.8 bolt (F_preload = 22 kN) through 8mm plate. Bolt head diameter 16mm.

**Tasks:**
1. Calculate bearing stress under bolt head
2. Compare to σ_y for A36 steel (250 MPa) and 4140 HT (415 MPa)
3. Determine if either material yields
4. If yielding occurs, calculate permanent set (plastic deformation)
5. Specify minimum required material for safe joint

### Exercise 1.2.3: Thermal Expansion Budget Analysis

1.8m × 1.2m machine frame, positioning accuracy ±0.05 mm, shop temperature varies 10°C daily.

**Tasks:**
1. Calculate thermal expansion for steel (α = 11.7×10⁻⁶/°C) and aluminum (α = 23.6×10⁻⁶/°C)
2. Express as multiple of tolerance (expansion / 0.05 mm)
3. If thermal compensation is used (software corrects for measured temperature), what sensor resolution is required?
4. Compare cost of thermal compensation system ($250 for sensors + software) vs climate control (±2°C stability, $180/month HVAC cost)
5. Calculate payback period for climate control investment

---

**Next Section Preview:** [Section 1.3: Structural Analysis and Beam Theory](section-01.3-structural-analysis.md) will apply these material properties to analytical beam deflection calculations, introducing Euler-Bernoulli beam theory, finite element analysis (FEA) validation, and modal analysis for predicting natural frequencies and vibration modes.

---

## References and Further Reading

1. **AISC Steel Construction Manual**, 15th Edition (2017) - Comprehensive steel section properties and design procedures
2. **ASM Metals Handbook**, Volume 1: Properties and Selection (2005) - Authoritative material property data
3. **Ashby, M.F.** - *Materials Selection in Mechanical Design*, 5th Ed. (2016) - Material selection methodology
4. **MatWeb Material Property Database** - [www.matweb.com](http://www.matweb.com) - Free online material properties
5. **MMPDS-15** (Metallic Materials Properties Development and Standardization) - Aerospace material data, conservative values for critical applications

---

*This section provides the quantitative foundation for frame material selection. Section 1.3 will derive the beam equations referenced here (δ = FL³/48EI) from first principles using Euler-Bernoulli theory, then validate with finite element analysis.*
