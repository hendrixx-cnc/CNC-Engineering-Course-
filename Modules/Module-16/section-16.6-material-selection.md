# Section 16.6: Material Selection for Design

## Introduction

Material selection profoundly impacts both part performance and manufacturability. The "best" material balances functional requirements (strength, weight, corrosion resistance) with manufacturing constraints (machinability, availability, cost). This section guides you through the material selection process, emphasizing how material properties influence CAD design decisions and manufacturing processes.

### Why Material Selection Matters: Real-World Cost Impact

**Scenario 1: Over-Engineering the Material**

**Designer A's Approach (Amateur):**
- Bracket needs 200 MPa yield strength (safety factor already included)
- Chooses **304 Stainless Steel** (yield: 215 MPa) because "stainless is durable"
- Dimensions: 100mm × 50mm × 10mm bracket

**Cost breakdown:**
- Material: $4.00/kg × 0.393kg = **$1.57**
- Machining time: **45 minutes** (stainless is tough, work-hardens, requires slow feeds)
- Machine rate: $80/hr → **$60.00**
- Tool wear: **+$5.00** (carbide inserts wear faster on stainless)
- **Total: $66.57 per part**

**Designer B's Approach (Professional):**
- Same requirements: 200 MPa yield strength needed
- Chooses **Aluminum 7075-T6** (yield: 503 MPa) - exceeds requirements AND excellent machinability
- Same dimensions: 100mm × 50mm × 10mm bracket

**Cost breakdown:**
- Material: $8.00/kg × 0.135kg = **$1.08**
- Machining time: **15 minutes** (aluminum cuts easily, high speeds possible)
- Machine rate: $80/hr → **$20.00**
- Tool wear: **+$0.50** (minimal aluminum wear)
- **Total: $21.58 per part**

**Result: $45 saved per part (67% cost reduction) with BETTER strength (503 MPa vs 215 MPa)!**

**Scenario 2: Material Cost vs Total Cost**

Many designers focus only on material cost per kg and miss the total picture:

| Material | Cost/kg | Part Material Cost | Machining Time | Machining Cost | Tool Wear | **TOTAL COST** |
|----------|---------|-------------------|----------------|----------------|-----------|----------------|
| **Mild Steel 1018** | $2.50 | $0.98 | 30 min | $40 | $2 | **$42.98** |
| **Aluminum 6061-T6** | $4.50 | $1.22 | 12 min | $16 | $0.50 | **$17.72** |
| **304 Stainless** | $4.00 | $1.57 | 45 min | $60 | $5 | **$66.57** |

**Critical insight: Material cost is only 2-5% of total part cost. Machinability dominates.**

Aluminum has the HIGHEST material cost ($4.50/kg) but LOWEST total cost ($17.72) because it machines so quickly. Steel looks cheap at $2.50/kg but total cost is 2.4× higher than aluminum!

## Material Selection Criteria

### Functional Requirements

**Mechanical Properties:**
- **Strength:** Tensile, compressive, shear (load-bearing applications)
- **Stiffness:** Elastic modulus (deflection-critical applications)
- **Hardness:** Wear resistance, indentation resistance
- **Toughness:** Impact resistance, fracture resistance
- **Fatigue resistance:** Cyclic loading applications

**Physical Properties:**
- **Density:** Weight-critical applications (aerospace, robotics)
- **Thermal conductivity:** Heat sinks, thermal barriers
- **Thermal expansion:** Dimensional stability across temperatures
- **Electrical conductivity:** Grounding, shielding, current-carrying

**Environmental Resistance:**
- **Corrosion resistance:** Outdoor use, chemical exposure
- **UV resistance:** Sunlight exposure
- **Temperature range:** Operating environment (cryogenic to high-temp)
- **Chemical compatibility:** Specific chemicals, solvents, oils

### Manufacturing Considerations

**Machinability:**
- Cutting forces required
- Tool wear rate
- Achievable surface finish
- Achievable tolerances
- Chip formation and evacuation

**Material Availability:**
- Standard stock sizes (plate, bar, tube, sheet)
- Lead times and supply chain reliability
- Minimum order quantities
- Geographic availability

**Cost:**
- Raw material cost per kg/pound
- Machining cost (time × tooling wear)
- Scrap value (recyclability)
- Total cost of ownership

**Secondary Processes:**
- Heat treatment requirements
- Surface coating/finishing needs
- Weldability / joinability
- Post-processing complexity

## Common Engineering Materials

### Metals - Aluminum Alloys

**Advantages:**
- Lightweight (2.7 g/cm³, 1/3 weight of steel)
- Excellent machinability (high material removal rates)
- Good corrosion resistance (natural oxide layer)
- Wide range of alloys for different properties
- Recyclable with minimal property loss

**Disadvantages:**
- Lower strength than steel (alloy-dependent)
- Lower stiffness (E = 69 GPa vs steel's 200 GPa)
- Poor elevated temperature performance (>150°C)
- Galvanic corrosion with dissimilar metals

**Common Alloys:**

| Alloy | Properties | Applications | Machinability |
|-------|-----------|--------------|---------------|
| **6061-T6** | General purpose, weldable, corrosion resistant | Structural frames, brackets, general components | Excellent |
| **7075-T6** | High strength, aerospace grade | High-stress components, aerospace | Good |
| **2024-T3** | High strength, poor weld ability | Aircraft structures, high-stress parts | Good |
| **5052-H32** | Excellent corrosion resistance, formable | Sheet metal, marine environments | Good |
| **MIC-6** | Cast plate, low internal stress, very flat | Precision plates, tooling, machine beds | Excellent |

**Design Considerations for Aluminum:**
- Requires thicker cross-sections than steel for equivalent stiffness
- Excellent for heat sinks (thermal conductivity 205 W/m·K)
- Anodizing provides enhanced corrosion/wear resistance
- Threading: use thread inserts for high-cycle or high-load applications

### Metals - Steel Alloys

**Advantages:**
- High strength and stiffness
- Wide range of properties via heat treatment
- Magnetic (useful for fixturing)
- Low cost (carbon steel)
- Excellent weldability

**Disadvantages:**
- Heavy (7.85 g/cm³)
- Corrosion susceptibility (carbon steel)
- Lower machinability than aluminum (harder, generates more heat)

**Common Alloys:**

| Alloy | Properties | Applications | Machinability |
|-------|-----------|--------------|---------------|
| **1018 (Mild Steel)** | Low carbon, easy to weld, low cost | Structural, non-critical parts | Good |
| **1045** | Medium carbon, higher strength | Shafts, gears, general machine parts | Fair |
| **4140** | Alloy steel, heat treatable to high hardness | High-stress shafts, tooling, wear parts | Fair (annealed), Poor (hardened) |
| **304 Stainless** | Corrosion resistant, non-magnetic (austenitic) | Food equipment, marine, chemical | Fair (work-hardens) |
| **316 Stainless** | Superior corrosion resistance (molybdenum) | Marine, chemical, medical | Fair (work-hardens) |
| **17-4 PH Stainless** | High strength + corrosion resistance, heat treatable | Aerospace, pump shafts, marine hardware | Fair |

**Design Considerations for Steel:**
- Design for appropriate stock sizes (common: 1/4", 1/2", 3/4", 1" plate; 1/2", 1", 2" bar)
- Stainless requires higher cutting forces, sharp tools, generous coolant
- Carbon steel requires corrosion protection (paint, plating, oil)
- Heat treatment distortion: leave stock for final grinding if tight tolerances needed

### Metals - Brass and Bronze

**Brass (Copper + Zinc):**
- Excellent machinability (free-cutting grades)
- Good corrosion resistance
- Decorative appearance
- Low friction (bearing applications)
- Non-sparking (explosive environments)

**Bronze (Copper + Tin/Aluminum/other):**
- Superior wear resistance vs brass
- Excellent for bearings, bushings
- Good corrosion resistance
- More expensive than brass

**Common Alloys:**

| Alloy | Composition | Applications | Machinability |
|-------|------------|--------------|---------------|
| **360 Brass** | 61% Cu, 3% Pb | Free-machining, fittings, valves | Excellent |
| **C932 Bearing Bronze** | Cu-Sn-Ni | Bearings, bushings, wear surfaces | Good |
| **Aluminum Bronze** | Cu-Al | Marine hardware, high-strength bushings | Fair |

**Design Considerations:**
- Excellent for complex features (intricate shapes machine easily in brass)
- Natural lubricity: ideal for sliding contact
- Relatively expensive (copper cost)
- Low strength compared to steel/aluminum

### Plastics - Engineering Thermoplastics

**Advantages:**
- Lightweight
- Corrosion and chemical resistant
- Electrical insulation
- Low friction (some grades)
- Lower machining forces
- Wide color options (molded/extruded)

**Disadvantages:**
- Lower strength and stiffness than metals
- Thermal expansion (5-10× greater than metals)
- Creep under sustained load
- Temperature sensitivity
- Machining challenges (melting, gummy chips)

**Common Engineering Plastics:**

| Material | Properties | Applications | Machinability |
|----------|-----------|--------------|---------------|
| **Acetal (Delrin)** | High stiffness, low friction, good moisture resistance | Gears, bearings, structural parts | Excellent |
| **Nylon (PA)** | Tough, wear-resistant, chemical resistant | Gears, bushings, rollers | Good (moisture-sensitive) |
| **UHMW-PE** | Ultra-low friction, impact resistant | Sliding surfaces, liners, guides | Good (soft, requires sharp tools) |
| **Acrylic (PMMA)** | Transparent, rigid, scratch-resistant | Windows, light guides, displays | Excellent |
| **Polycarbonate (PC)** | High impact resistance, transparent | Safety shields, electronics housings | Good (requires low heat) |
| **PEEK** | High temp (260°C), high strength, chemical resistant | Aerospace, medical, high-performance | Fair (expensive, specialized) |
| **PTFE (Teflon)** | Extreme chemical resistance, lowest friction | Chemical equipment, non-stick surfaces | Poor (soft, tears easily) |

**Design Considerations for Plastics:**
- Account for thermal expansion (design clearances accordingly)
- Minimize thin walls (warping during machining/cooling)
- Use generous radii (stress concentrations more critical due to lower toughness)
- Sharp tools essential (dull tools melt plastic)
- Thread inserts for repeated assembly (molded or heat-set)

### Composites - Carbon Fiber and Fiberglass

**Carbon Fiber (CFRP):**
- Extremely high strength-to-weight ratio
- High stiffness-to-weight ratio
- Anisotropic properties (directional strength)
- Expensive
- Difficult to machine (abrasive, requires carbide/diamond tools)

**Fiberglass (GFRP):**
- Good strength-to-weight ratio
- Lower cost than carbon fiber
- Corrosion resistant
- Electrical insulation

**Design Considerations:**
- Typically molded/laid up, not machined from stock
- Machining used for trimming edges, drilling holes
- Drilling requires backer plate (prevent delamination)
- Specialized tooling (carbide/diamond)
- Dust hazards (health precautions required)

## Material Properties and CAD Design

### Strength and Safety Factors

**Basic stress calculation:**
```
Stress (σ) = Force / Area

Safety Factor (SF) = Material Yield Strength / Applied Stress
```

**Typical safety factors:**
- Static load, known materials, non-critical: SF = 1.5-2
- Dynamic load, well-characterized: SF = 2-3
- Unknown loads, critical application: SF = 3-5
- Impact/shock loading: SF = 5-10

**CAD implications:**
- Lower strength materials require thicker cross-sections
- FEA (Finite Element Analysis) helps optimize material distribution
- Parametric models allow quick material substitution with automatic resizing

### Stiffness and Deflection

**Deflection of beam under load:**
```
Deflection (δ) ∝ (Force × Length³) / (Elastic Modulus × Moment of Inertia)
```

**Key insight:** Geometry (moment of inertia) has greater impact than material elastic modulus.

**Example:**
```
Aluminum beam (E = 69 GPa): δ = 10 mm
Steel beam (same dimensions, E = 200 GPa): δ = 3.45 mm (2.9× stiffer)
Aluminum I-beam (same weight as solid steel): δ = 0.5 mm (20× stiffer!)
```

**CAD design strategy:**
- Don't just swap materials—optimize geometry
- Use ribs, gussets, I-beams, tubes instead of solid sections
- CAD sketches should reference elastic modulus parameter for deflection-critical designs

### Thermal Expansion Management

**Coefficient of Thermal Expansion (CTE):**

| Material | CTE (µm/m·°C) | 100mm part, 50°C ΔT |
|----------|---------------|---------------------|
| Aluminum 6061 | 23.6 | +0.118 mm |
| Steel (carbon) | 11.7 | +0.059 mm |
| Stainless 304 | 17.3 | +0.087 mm |
| Brass | 18.7 | +0.094 mm |
| Acetal (Delrin) | 106 | +0.530 mm |
| Nylon | 80 | +0.400 mm |

**Design implications:**

**Large structures:**
```
Aluminum frame, 1000mm long, 50°C temperature change:
  ΔL = 1000 × 23.6 × 50 / 1,000,000 = 1.18 mm growth

Design solutions:
  - Slotted mounting holes (allow movement)
  - Flexures or spring-loaded connections
  - Symmetrical expansion about center datum
```

**Mixed-material assemblies:**
```
Aluminum plate (CTE = 23.6) + steel fasteners (CTE = 11.7):
  Differential expansion causes stress

Design solutions:
  - Oversized clearance holes in aluminum
  - Belleville washers to maintain clamp load
  - Isolation bushings
```

**Precision applications:**
```
Use low-expansion materials:
  - Invar (CTE = 1.2) for metrology, optics
  - Titanium (CTE = 8.6) for aerospace
  - Carbon fiber (CTE ~0 in fiber direction)
```

### Machinability Index

**Relative machining cost (100 = free-machining brass):**

| Material | Machinability Rating | Tool Wear | Notes |
|----------|---------------------|-----------|-------|
| Free-cutting brass (360) | 100 | Very low | Benchmark material |
| Aluminum 6061-T6 | 90 | Low | Fast cutting, excellent finish |
| Aluminum 7075-T6 | 70 | Low | Harder than 6061 |
| Mild steel (1018) | 70 | Moderate | Higher cutting forces than Al |
| 4140 steel (annealed) | 55 | Moderate | Heat treatable |
| 304 Stainless | 45 | High (work-hardens) | Requires sharp tools |
| 316 Stainless | 40 | High | More difficult than 304 |
| Titanium (Ti-6Al-4V) | 30 | Very high | Specialized tooling/techniques |
| Inconel (nickel superalloy) | 15 | Extreme | Very slow, expensive |
| Acetal (Delrin) | 95 | Very low | Excellent plastic machinability |
| Nylon | 80 | Low | Moisture affects properties |
| Polycarbonate | 75 | Low | Requires low heat |

**Real-World Manufacturing Time Comparison**

**Part: 150mm × 100mm × 25mm block with 6 pockets (identical geometry, different materials)**

| Material | Rough Milling | Finish Milling | Tool Changes | Total Time | Cost @ $80/hr |
|----------|--------------|----------------|--------------|------------|---------------|
| **Aluminum 6061** | 18 min | 7 min | 1 | **25 min** | **$33** |
| **Brass 360** | 15 min | 6 min | 1 | **21 min** | **$28** |
| **Mild Steel 1018** | 28 min | 12 min | 2 | **40 min** | **$53** |
| **304 Stainless** | 55 min | 22 min | 3 | **77 min** | **$103** |
| **Titanium Ti-6Al-4V** | 120 min | 45 min | 6 | **165 min** | **$220** |
| **Inconel 718** | 280 min | 95 min | 12 | **375 min** | **$500** |

**Key insights:**
- **Stainless takes 3× longer than aluminum** (77 min vs 25 min)
- **Titanium takes 6.6× longer than aluminum** (165 min vs 25 min)
- **Inconel takes 15× longer than aluminum!** (375 min vs 25 min)

**Design impact:**
- Difficult-to-machine materials favor simpler geometries
- Complex features in Inconel = prohibitive cost
  - **Example:** 10-pocket design in aluminum = $75; same part in Inconel = $1,200 (16× cost!)
- Same features in aluminum = reasonable cost

## Material Availability and Stock Sizes

### Standard Forms

**Plate:**
- Thickness: 1/16", 1/8", 1/4", 3/8", 1/2", 3/4", 1", 1.5", 2" (and metric equivalents)
- Sheet size: 48" × 96" (4'×8'), 60" × 120" common

**Bar (Rectangular):**
- Common sizes: 1/4" × 1", 1/2" × 2", 1" × 1", etc.
- Lengths: 12 ft (144"), 6 ft (72") common

**Rod (Round):**
- Diameters: 1/4", 3/8", 1/2", 5/8", 3/4", 1", 1.25", 1.5", 2", etc.
- Lengths: 12 ft, 6 ft common

**Tube (Round):**
- OD × Wall: 1" OD × 0.065" wall, 2" OD × 0.125" wall, etc.
- Lengths: 12 ft, 6 ft common

**Tube (Square/Rectangular):**
- Sizes: 1"×1"×0.065", 2"×1"×0.125", etc.

### Design for Stock Sizes

**Good Practice (Professional Designer):**
```
Design part: 48mm thick
→ Use 50mm plate stock (standard), machine both sides to 48mm
→ Minimal waste: 4% material waste

Design part: 19mm diameter shaft
→ Use 20mm rod stock (standard), turn to 19mm
→ Minimal waste: 10% material waste
```

**Poor Practice (Amateur Designer):**
```
Design part: 73mm thick
→ No standard stock size!
→ Option A: Use 75mm plate (custom order, 8-week lead time, $450 minimum)
→ Option B: Use 80mm plate ($95 vs $65 for 75mm), 10% waste
→ Option C: Laminate 50mm + 25mm plates (adds welding, stress relief, $200 extra)

Design part: 17.5mm diameter shaft
→ No standard stock size!
→ Must machine from 20mm stock: 33% material waste
```

**Real-World Cost Comparison:**

**Part: Custom mounting plate**

| Design Choice | Stock Size | Stock Cost | Material Waste | Lead Time | Total Cost |
|--------------|------------|------------|----------------|-----------|------------|
| **73mm thick (poor)** | 80mm custom | $95 | 10% ($9.50) | 8 weeks | **$104.50** |
| **48mm thick (good)** | 50mm standard | $32 | 4% ($1.28) | In stock | **$33.28** |

**Result: 69% cost reduction + immediate availability by designing for standard stock!**

**CAD Parametric Approach:**
```python
# Define standard stock as parameter
stock_thickness = 50 mm    # Standard stock size (parameter)
finish_allowance = 1 mm     # Per side
final_thickness = stock_thickness - 2 * finish_allowance  # = 48 mm

# All features reference final_thickness
pocket_depth = final_thickness - 10 mm  # Updates automatically
```

**Benefits:**
- Change `stock_thickness = 75 mm` → entire design updates to 73mm final thickness
- Quickly explore different stock sizes to find best cost/performance balance
- Design intent captured: "Use standard stock, leave 1mm per side for finish"

## Material Selection Process

### Real-World Example: Robotic Arm Bracket

**Application:** Mounting bracket for robotic arm servo motor
**Environment:** Indoor manufacturing facility, room temperature
**Production volume:** 100 units

### Step 1: Define Requirements

**Create requirements matrix:**

| Requirement | Target | Minimum Acceptable | Why |
|-------------|--------|-------------------|-----|
| Tensile strength | 400 MPa | 300 MPa | Supports 50kg load with SF=3 |
| Elastic modulus | 70 GPa | 60 GPa | Max deflection <0.5mm |
| Density | <3 g/cm³ | <5 g/cm³ | Robot arm weight-sensitive |
| Corrosion resistance | Good | Fair | Indoor use, occasional cleaning |
| Operating temp | -10 to 60°C | 0 to 50°C | Factory environment |
| Machinability | Good | Fair | Complex geometry with pockets |
| Cost target | <$30/part | <$50/part | Budget constraint |

### Step 2: Screen Candidate Materials

**Eliminate materials that fail minimum requirements:**
```
✗ Mild steel 1018: Yield strength 250 MPa (FAIL: below minimum 300 MPa)
✗ Nylon 6: Elastic modulus 3 GPa (FAIL: below minimum 60 GPa)
✗ Acetal: Elastic modulus 3.1 GPa (FAIL: below minimum 60 GPa)
✓ Aluminum 6061-T6: Yield 276 MPa (marginal), E = 69 GPa (meets target), density 2.7 g/cm³ (excellent)
✓ Aluminum 7075-T6: Yield 503 MPa (exceeds!), E = 71.7 GPa (meets target), density 2.81 g/cm³ (excellent)
✓ Stainless 304: Yield 215 MPa (FAIL: below minimum 300 MPa) - ELIMINATED
✓ 4140 Steel: Yield 415 MPa (meets), E = 205 GPa (exceeds), density 7.85 g/cm³ (FAIL: too heavy)
```

**Remaining candidates:** Aluminum 6061-T6, Aluminum 7075-T6

### Step 3: Rank Candidates with Cost Analysis

**Weighted scoring (1-10 scale):**

| Material | Strength (30%) | Stiffness (20%) | Weight (20%) | Machinability (20%) | Cost (10%) | **Total Score** |
|----------|----------------|-----------------|--------------|---------------------|------------|-----------------|
| **Al 6061-T6** | 6 (marginal) | 7 (good) | 9 (excellent) | 9 (excellent) | 10 (best) | **7.5** |
| **Al 7075-T6** | 10 (exceeds) | 7 (good) | 9 (excellent) | 7 (good) | 6 (higher) | **8.2** |

**Detailed cost analysis:**

| Material | Part Volume | Material Cost | Machining Time | Machining Cost | Tool Wear | **Total** |
|----------|------------|---------------|----------------|----------------|-----------|-----------|
| **Al 6061-T6** | 180 cm³ | $2.20 | 22 min | $29.33 | $0.75 | **$32.28** |
| **Al 7075-T6** | 180 cm³ | $4.10 | 28 min | $37.33 | $1.20 | **$42.63** |

**Decision Point:**

- **6061-T6 score: 7.5** - Marginal strength (276 MPa), but **meets $30 target cost**
- **7075-T6 score: 8.2** - Excellent strength (503 MPa), but **$42.63 exceeds $30 target**

**Professional Analysis:**
```
Safety Factor check with 6061-T6:
  Required: 300 MPa minimum
  Actual: 276 MPa
  → FAILS minimum requirement by 8%

Decision: Must use 7075-T6 despite higher cost
  → Negotiate budget increase or redesign to reduce stress
```

**Final Decision: Aluminum 7075-T6**
- Meets all requirements with margin
- Cost: $42.63 per part (need budget approval for $12.63 overage)
- Alternative: Redesign bracket with ribs to reduce stress → might allow 6061-T6

### Step 4: Prototype and Validate

**Prototype Results:**
- Built 3 prototypes in Al 7075-T6
- Load testing: Applied 75kg (1.5× design load)
- Measured deflection: **0.32mm** (target: <0.5mm) ✓
- Stress concentration near mounting hole: **420 MPa** (material yield: 503 MPa) ✓
- **Conclusion: Design validated, proceed with production**

**Cost for 100-unit production:**
- Per-part cost: $42.63
- Setup cost (one-time): $350
- **Total: $4,613** ($46.13 per part including setup)

## Material-Specific Design Guidelines

### Designing with Aluminum

**Optimize for:**
- Thin walls with ribs (lightweight + rigid)
- Large pockets (easy material removal)
- Anodized finishes (specify type II or type III hardcoat)

**Real-World Example: Aluminum Enclosure Design**

**Amateur Design (solid construction):**
- 200mm × 150mm × 80mm solid-walled enclosure
- Wall thickness: 10mm everywhere
- Weight: 1,240g
- Material cost: $33.50
- Machining time: 65 minutes → $86.67
- **Total: $120.17**

**Professional Design (ribbed construction):**
- Same external dimensions
- Wall thickness: 3mm with 5mm ribs every 40mm
- Weight: 420g (66% lighter!)
- Material cost: $11.35 (66% savings)
- Machining time: 42 minutes (less material removal) → $56.00
- **Total: $67.35**

**Result: $52.82 saved per part (44% cost reduction) + 820g weight savings!**

**Avoid:**
- Thin unsupported walls (<2mm without ribs) → **Consequence:** Warping during machining, chatter marks
- Sharp inside corners (stress concentrations, tool access) → **Consequence:** Requires EDM ($150+ extra) or stress risers
- Direct steel contact (galvanic corrosion; use isolators) → **Consequence:** White corrosion powder forms, parts seize

**Thread Considerations:**

| Application | Thread Type | Cost | Strength | Use When |
|------------|-------------|------|----------|----------|
| Low-cycle assembly (<10×) | Tapped aluminum (1.5× depth) | $2 | Fair | Non-critical fastening |
| Medium-cycle (<100×) | Helicoil insert | $4 | Good | Frequent access panels |
| High-cycle or high-load | Threaded insert (PEM, etc.) | $6 | Excellent | Hinges, adjustments |

**Example:**
- M6 threads in 6061-T6 aluminum, 12mm engagement
- Direct tapping: Fails after ~50 assembly cycles
- Helicoil insert: Survives 500+ cycles (10× improvement, +$2 cost)

### Designing with Steel

**Optimize for:**
- Solid construction (strength advantage over aluminum)
- Welded assemblies (excellent weldability)
- Magnetic properties (holding, sensors)

**Avoid:**
- Unnecessary mass (heavy; optimize with pockets, holes)
- Thin stainless walls (work-hardens during machining)

**Corrosion protection:**
- Specify finish: paint, powder coat, zinc plate, chrome plate, or choose stainless

### Designing with Plastics

**Optimize for:**
- Smooth contours (low friction, self-lubricating)
- Electrical insulation
- Corrosion/chemical exposure
- Reduced weight

**Real-World Example: Sliding Guide Block**

**Metal Version (Aluminum 6061):**
- 50mm × 40mm × 20mm guide block
- Requires lubrication (grease every 500 cycles)
- Weight: 108g
- Material + machining: $18.50
- **Maintenance cost:** $120/year (labor for re-lubrication)

**Plastic Version (Acetal/Delrin):**
- Same dimensions
- Self-lubricating (no maintenance)
- Weight: 36g (67% lighter!)
- Material + machining: $12.30
- **Maintenance cost:** $0/year

**5-year total cost:**
- Aluminum: $18.50 + (5 × $120) = **$618.50**
- Acetal: $12.30 + $0 = **$12.30**
- **Savings: $606.20 (98% reduction!)** for appropriate plastic application

**Avoid:**
- Tight tolerances without specifying conditions → **Consequence:** Part dimensions change with temperature/humidity
  - Example: ⌀25.00mm Delrin shaft at 20°C → ⌀25.13mm at 45°C (out of tolerance!)
- Sharp corners (stress concentration critical) → **Consequence:** Crack initiation, brittle failure
- Thin sections prone to warping → **Consequence:** Part warps during machining from internal stresses

**Account for Thermal Expansion:**

**Example calculation:**
```
Delrin guide rail: 200mm long
CTE: 106 µm/m·°C
Temperature range: 15°C to 45°C (ΔT = 30°C)

Expansion = 200mm × (106/1,000,000) × 30°C = 0.636mm

Design clearance = 0.5mm (nominal) + 0.636mm (thermal) = 1.14mm minimum
```

**Poor Design:** 200mm rail with 0.5mm clearance → Binds at high temperature
**Good Design:** 200mm rail with 1.2mm clearance → Functions across full temperature range

**Practical guideline for plastic assemblies:**
- **Room temperature only:** Standard tolerances (±0.1mm)
- **Temperature variation 20-40°C:** Add +0.3mm clearance per 100mm length
- **Temperature variation 0-60°C:** Add +0.6mm clearance per 100mm length

## CAD Material Libraries

### Assigning Material Properties in CAD

Most CAD systems include material libraries:

**SolidWorks:** Material database with density, elastic modulus, Poisson's ratio, thermal properties
**Fusion 360:** Autodesk material library + custom materials
**FreeCAD:** Material editor with mechanical and thermal properties

**Benefits of assigning materials:**
1. **Automatic mass calculation** (BOM, weight estimates)
2. **FEA simulation** (stress, deflection, thermal analysis)
3. **Rendering** (realistic appearance)
4. **Cost estimation** (material cost × volume)

**Example - Parametric Material Selection:**
```
Material parameter: "Aluminum_6061"

Part properties (auto-calculated):
  Density: 2.70 g/cm³
  Volume: 150 cm³
  Mass: 405 g
  Material cost: $4.50/kg → $1.82 per part
```

Switch parameter to "Aluminum_7075":
```
  Density: 2.81 g/cm³
  Mass: 422 g
  Material cost: $8.00/kg → $3.38 per part
```

**Instant comparison** without leaving CAD.

## Summary

Material selection is a critical design decision affecting performance, manufacturability, and cost. This section has shown that **material cost is only 2-5% of total part cost**—machinability and design decisions are the real cost drivers.

**Key Takeaways:**

**1. Total Cost Thinking:**
- Aluminum costs $4.50/kg but total part cost = $17.72
- Steel costs $2.50/kg but total part cost = $42.98
- **Machinability matters more than material price!**

**2. Real Cost Impacts Demonstrated:**
- Material over-engineering: $66.57 vs $21.58 (67% savings with better material choice)
- Ribbed vs solid construction: $120.17 vs $67.35 (44% savings + 66% weight reduction)
- Standard vs custom stock: $104.50 vs $33.28 (69% savings by designing for standard sizes)
- Appropriate plastic application: $618.50 vs $12.30 over 5 years (98% lifecycle cost reduction)

**3. Machinability Time Multipliers:**
- Aluminum baseline: 25 minutes
- Stainless steel: 77 minutes (3× slower)
- Titanium: 165 minutes (6.6× slower)
- Inconel: 375 minutes (15× slower!)

**4. Key Decision Factors:**
- **Functional requirements:** Strength, stiffness, environmental resistance
- **Machinability:** Tool wear, cutting time (dominates cost)
- **Availability:** Standard stock sizes, lead times
- **Total cost:** Material + machining + secondary processes + lifecycle maintenance

**5. Material Categories:**
- **Aluminum:** Lightweight, excellent machinability, good corrosion resistance, best for complex features
- **Steel:** High strength/stiffness, weldable, magnetic, 2-3× slower machining than aluminum
- **Brass/Bronze:** Excellent machinability, decorative, bearing applications, expensive material cost
- **Plastics:** Lightweight, corrosion-resistant, electrical insulation, thermal expansion considerations critical
- **Composites:** High strength/stiffness-to-weight, expensive, difficult machining, typically molded

**6. CAD Integration Best Practices:**
- Assign materials in CAD for automatic mass/cost calculations
- Use parametric material properties (`stock_thickness`, `material_density`) for design optimization
- Design for standard stock sizes (saves 50-70% on material cost + eliminates lead time)
- Account for thermal expansion in assemblies (plastics expand 5-10× more than metals)
- Consider machinability when designing complex features (Inconel pocket = 16× cost vs aluminum!)

**Professional vs Amateur Mindset:**
- **Amateur:** "Material X is stronger, so I'll use that"
- **Professional:** "What's the minimum material performance needed? What's the total cost (material + machining + lifecycle)?"

**Next section** covers process-specific design considerations for each CNC technology in the course.

***

**Next:** [Section 16.7: Process-Specific Design Considerations](section-16.7-process-specific-design.md)

**Previous:** [Section 16.5: Tolerancing and GD&T](section-16.5-tolerancing-gdt.md)
