# Section 16.5: Tolerancing and Geometric Dimensioning & Tolerancing (GD&T)

## Introduction

**No manufacturing process creates perfect parts. The question isn't "will there be variation?"—it's "how much variation can we afford?"**

Every dimension has variation—the art of engineering design is specifying how much variation is acceptable for function while remaining economical to produce. This section covers traditional tolerancing methods and introduces Geometric Dimensioning and Tolerancing (GD&T), the international language for precisely communicating design intent.

**Real-World Impact:**

**Scenario 1: Over-Toleranced Part**
- Designer specifies ±0.01mm on all 50 dimensions
- Shop quote: $450 per part (requires grinding, precision inspection)
- **Reality check:** Only 5 dimensions actually need ±0.01mm
- **Redesign** with appropriate tolerances: $85 per part
- **Savings:** $365 per part (81% cost reduction!)

**Scenario 2: Under-Toleranced Part**
- Designer leaves all tolerances unspecified
- Machinist assumes ±0.2mm (shop standard)
- Parts arrive: bearing hole is 20.35mm (should be 20.00mm +0.02/-0)
- **Result:** Bearings won't fit, 100 parts scrapped
- **Cost:** $8,500 scrap + $1,200 rework + 2 weeks delay

**The lesson:** Tolerancing is about communicating clearly what matters (and what doesn't).

## Understanding Manufacturing Variation

**Manufacturing variation is like archery—even the best archer doesn't hit the exact center every time.**

The goal is to define an acceptable "target zone" large enough to be economical, but small enough to ensure function.

### Sources of Variation

Understanding WHY variation occurs helps you tolerance intelligently:

**Machine-Related Variation:**
- Positioning accuracy (±0.005-0.05mm typical for CNC mills)
- Thermal expansion of machine components (20°C → 30°C = 0.01mm/meter in steel)
- Spindle runout (worn bearings = ±0.005-0.02mm radial error)
- Linear guide wear (older machines = looser positioning)
- Backlash in drive systems (direction reversal = small position error)

**Real Example:**
- Cold morning (15°C): Machine calibrated
- Afternoon (25°C): Machine body expanded 0.05mm
- Parts machined in afternoon: 0.05mm oversized on long dimensions
- **Solution:** Environmental temperature control OR wider tolerances

***

**Tool-Related Variation:**
- Tool deflection under cutting forces (thin tool + heavy cut = part undersized)
- Tool wear progression (first part vs 100th part = different sizes)
- Cutting edge sharpness variation (dull tool = larger burrs, worse finish)
- Tool runout in holder (tool wobbles = oversize holes)

**Real Example:**
- Drilling ⌀10mm holes with worn drill bit
- First hole: ⌀10.05mm (acceptable)
- 50th hole: ⌀10.18mm (out of tolerance!)
- **Solution:** Tool replacement schedule OR compensate in programming

***

**Material-Related Variation:**
- Inconsistent material properties (hardness varies = cutting forces vary)
- Internal stresses causing warping (thin walls bend after machining)
- Thermal expansion during/after machining (hot part = oversized, cools to smaller size)
- Grain structure variations (some areas cut cleaner than others)

**Real Example:**
- Machine aluminum part to exact size while hot from cutting
- Part cools overnight: shrinks 0.03mm
- **Result:** Part now undersized
- **Solution:** Allow cooldown before final measurement, or compensate for thermal expansion

***

**Process-Related Variation:**
- Fixturing repeatability (part position varies ±0.01-0.05mm between setups)
- Operator skill variation (manual operations = higher variation)
- Environmental conditions (temperature, humidity affect dimensions and tools)
- Measurement uncertainty (even measuring tools have ±0.001-0.01mm error)

**Real Example:**
- Inspector A measures part: 50.02mm (pass)
- Inspector B measures same part: 49.98mm (pass)
- **Actual size:** 50.00mm ±0.02mm (measurement uncertainty)
- **Solution:** Use calibrated instruments, establish inspection procedures

***

**Result:** Even well-controlled processes produce parts with dimensional variation.

**Key Insight:** Variation is NORMAL and EXPECTED. Good design accounts for it rather than fighting it.

### Process Capability

**Different processes have natural "comfort zones" for tolerance—push beyond them and costs skyrocket.**

| Process | Typical Tolerance | Best Achievable | Relative Cost | Limitations |
|---------|------------------|----------------|---------------|-------------|
| **Plasma Cutting** | ±0.5 mm | ±0.2 mm | 1× | Kerf width, heat distortion |
| **Laser Cutting** | ±0.1 mm | ±0.05 mm | 1.5× | Material thickness, heat input |
| **Waterjet** | ±0.15 mm | ±0.08 mm | 1.3× | Taper, abrasive variation |
| **CNC Milling** | ±0.05 mm | ±0.01 mm | 2× | Tool deflection, thermal effects |
| **CNC Turning** | ±0.025 mm | ±0.005 mm | 2× | Rigidity, tooling quality |
| **Wire EDM** | ±0.01 mm | ±0.002 mm | 8× | Wire diameter, thermal |
| **Grinding** | ±0.005 mm | ±0.001 mm | 6× | Wheel wear, thermal |
| **FDM 3D Printing** | ±0.3 mm | ±0.1 mm | 1× | Layer adhesion, shrinkage |
| **Resin 3D Printing** | ±0.1 mm | ±0.05 mm | 2× | Resin properties, curing |

**Tolerance Cost Multipliers (Relative to Standard Machining ±0.05mm):**

| Tolerance | Process Required | Cost Multiplier | Time Impact |
|-----------|-----------------|-----------------|-------------|
| ±0.5 mm | Standard plasma/laser | 0.3× | Fast |
| ±0.1 mm | Standard laser/milling | 1× (baseline) | Standard |
| ±0.05 mm | Careful milling | 1× | Standard |
| ±0.025 mm | Precision milling | 1.5× | +30% |
| ±0.01 mm | Grinding or EDM | 4× | +200% |
| ±0.005 mm | Precision grinding | 8× | +400% |
| ±0.001 mm | Ultra-precision (lapping) | 20× | +1000% |

**Real-World Example:**

**Part A: 100mm × 50mm plate with 4 mounting holes**

**Version 1 - Over-Toleranced:**
```
All dimensions: ±0.01mm
Hole positions: ±0.01mm
Surface finish: 0.4 µm Ra (mirror finish)
```
- **Process Required:** Precision grinding + hand polishing
- **Time:** 4 hours per part
- **Cost:** $320 per part @ $80/hr
- **Inspection:** CMM required (30 min, $60)
- **Total:** $380 per part

**Version 2 - Appropriately Toleranced:**
```
Overall dimensions: ±0.2mm (not critical)
Hole positions: ±0.05mm (functional requirement for motor mounting)
Surface finish: 3.2 µm Ra (standard milled)
```
- **Process Required:** Standard CNC milling
- **Time:** 25 minutes per part
- **Cost:** $33 per part @ $80/hr
- **Inspection:** Standard calipers (5 min, included)
- **Total:** $33 per part

**Savings: $347 per part (91% cost reduction!)** — Same function, 1/11th the cost.

***

**Key Insights:**

✓ **Stay within "typical" tolerance for each process** → Standard cost
✓ **Push to "best achievable"** → 2-4× cost increase
✓ **Exceed process capability** → 5-20× cost increase + secondary operations

**Design Rule:** Only specify tighter than "typical" tolerances when there's a documented functional need (bearing fit, precision assembly, sealing surface, etc.)

## Traditional Tolerancing Methods

### Plus/Minus Tolerancing

Most common method: nominal dimension ± tolerance value.

**Symmetric Tolerance:**
```
50 ±0.1 mm
  → Acceptable: 49.9 to 50.1 mm
```

**Asymmetric Tolerance:**
```
50 +0.2/-0.05 mm
  → Acceptable: 49.95 to 50.2 mm
```

**When to use asymmetric:**
- Mating features (shaft/hole) where one direction matters more
- Features limited by material removal (can't add material back)

### Limit Tolerancing

Specifies maximum and minimum dimensions directly:

```
Shaft diameter: 19.95 / 20.00 mm
Hole diameter:  20.10 / 20.15 mm
  → Guaranteed clearance: 0.10 to 0.20 mm
```

**Advantage:** Immediately clear what's acceptable; no mental math.

**Use case:** Critical mating features, manufacturing drawings.

### General Tolerance Notes

Specify default tolerances for undimensioned features:

```
UNLESS OTHERWISE SPECIFIED:
  - Decimal dimensions: ±0.1 mm
  - Angular dimensions: ±1°
  - Hole diameters: +0.2/0 mm
  - Surface finish: 3.2 µm Ra
```

**Advantage:** Reduces drawing clutter; only critical dimensions need individual callouts.

**Critical:** Must match shop capabilities. If shop standard is ±0.2mm, don't specify ±0.05mm as general tolerance.

### Tolerance Accumulation (Stack-Up)

**Problem:** Tolerances accumulate across chains of dimensions.

**Example:**
```
Part 1 length: 100 ±0.1 mm
Part 2 length: 100 ±0.1 mm
Part 3 length: 100 ±0.1 mm

Assembly length (3 parts end-to-end):
  Nominal: 300 mm
  Worst case: 299.7 to 300.3 mm  (±0.3 mm total variation)
```

**Worst-Case Stack-Up Formula:**
```
Total variation = ±(Tol₁ + Tol₂ + Tol₃ + ... + Tolₙ)
```

**Statistical Stack-Up (RSS - Root Sum Square):**
Assumes normal distribution of manufactured parts:
```
Total variation = ±√(Tol₁² + Tol₂² + Tol₃² + ... + Tolₙ²)
```

**Example with same parts:**
```
RSS stack: ±√(0.1² + 0.1² + 0.1²) = ±0.173 mm
```

**When to use RSS:** High-volume production where statistical variation applies.

**When to use worst-case:** Safety-critical applications, low volumes where statistics don't apply.

### Tolerance Chain Management

**Design strategy to minimize stack-up:**

**Poor approach (long chain):**
```
┌─────┬─────┬─────┬─────┐
│  A  │  B  │  C  │  D  │
└─────┴─────┴─────┴─────┘
 ←─────────────────────→
  Total = A+B+C+D ± (TolA + TolB + TolC + TolD)
```

**Better approach (direct dimension):**
```
┌─────┬─────┬─────┬─────┐
│  A  │     │     │     │
└─────┴─────┴─────┴─────┘
 ←─────────────────────→
  Total dimension specified directly ± single tolerance
```

**Best approach (datum-based dimensioning):**
All critical features measured from single datum = zero stack-up between them.

## Introduction to GD&T

### Why GD&T?

Traditional plus/minus tolerancing has limitations:

**Problem 1: Ambiguous Intent**
```
Hole position: X = 50 ±0.1, Y = 50 ±0.1
```
Does this create a ±0.1mm square zone, or ±0.141mm circular zone?
Different inspectors might interpret differently.

**Problem 2: Doesn't Control Form**
```
Surface: 100 ±0.1 mm
```
Surface could be bowed, twisted, tapered—as long as all points fall between 99.9 and 100.1mm.

**Problem 3: Doesn't Capture Functional Requirements**
A hole might be positioned perfectly but tilted at an angle—plus/minus tolerancing doesn't address orientation.

**GD&T Solution:**
Geometric Dimensioning and Tolerancing (ASME Y14.5 / ISO 1101) provides unambiguous symbols and rules for specifying:
- Form (straightness, flatness, circularity, cylindricity)
- Orientation (perpendicularity, parallelism, angularity)
- Location (position, concentricity, symmetry)
- Profile (surface profile, line profile)
- Runout (circular runout, total runout)

### GD&T Philosophy

**Key concepts:**

1. **Datums Define Reference Frames**
   - Datum = theoretically exact reference (surface, axis, plane)
   - Measurements made relative to datums, not arbitrary coordinate systems

2. **Feature Control Frames Specify Tolerances**
   - Standardized symbols eliminate ambiguity
   - Tolerance zones clearly defined (cylindrical, rectangular, etc.)

3. **Maximum Material Condition (MMC) Bonuses**
   - Parts that deviate from worst-case size get tolerance bonus
   - Encourages functional dimensioning

4. **Separation of Size and Form/Orientation/Location**
   - Diameter tolerance controls size
   - GD&T controls geometry independently

## GD&T Fundamentals

### Datum Reference Frames

Datums establish the coordinate system for measurements.

**Primary Datum (A):** Constrains 3 degrees of freedom
- Typically a flat surface (represents plane)
- Part sits against this surface

**Secondary Datum (B):** Constrains 2 more degrees of freedom
- Typically a perpendicular surface or axis
- Stops rotation, establishes direction

**Tertiary Datum (C):** Constrains final degree of freedom
- Completes the 3-2-1 locating scheme
- Fully defines part orientation

**Example: Rectangular Block**
```
Datum A: Bottom surface (establishes XY plane, constrains Z position and XY rotation)
Datum B: Left edge (establishes X direction, constrains X position and Z rotation)
Datum C: Front edge (establishes Y direction, constrains Y position)

Total: 6 degrees of freedom constrained (3 translation + 3 rotation)
```

**Datum Selection Priority:**
1. Primary: Most important mating surface or functional feature
2. Secondary: Perpendicular feature that defines orientation
3. Tertiary: Completes full constraint

**Real-World Example:**
Motor mount plate:
- Datum A: Mounting surface (bolts to machine)
- Datum B: Motor shaft bore (establishes rotation axis)
- Datum C: Locating pin hole (prevents rotation about shaft axis)

### Feature Control Frames

The "language" of GD&T—standardized symbols in rectangular boxes:

```
┌───┬────────┬───┬───┬───┐
│ ⊕ │ ⌀0.1   │ M │ A │ B │
└───┴────────┴───┴───┴───┘
 │      │      │   │   │
 │      │      │   │   └─ Secondary datum
 │      │      │   └───── Primary datum
 │      │      └───────── Material condition modifier
 │      └──────────────── Tolerance value
 └─────────────────────── Geometric characteristic symbol
```

### Common GD&T Symbols

**Form Controls (No Datum Required):**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| — | Straightness | Line elements | Two parallel lines |
| ⬜ | Flatness | Surface | Two parallel planes |
| ○ | Circularity (Roundness) | Circular cross-sections | Two concentric circles |
| ⌭ | Cylindricity | Cylindrical surface | Two coaxial cylinders |

**Orientation Controls (Require Datum):**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| ⊥ | Perpendicularity | 90° relationship to datum | Two parallel planes (or cylinder if applied to axis) |
| ∥ | Parallelism | Parallel relationship to datum | Two parallel planes (or cylinder) |
| ∠ | Angularity | Specific angle to datum | Two parallel planes at defined angle |

**Location Controls (Require Datum):**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| ⊕ | Position | Location of feature | Cylindrical (holes) or rectangular (features) |
| ⌖ | Concentricity | Centerpoint alignment | Cylindrical about datum axis |
| ≡ | Symmetry | Symmetry about datum plane | Two parallel planes |

**Profile Controls:**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| ⌓ | Profile of a Line | 2D profile tolerance | Equal bilateral or unilateral band |
| ⌒ | Profile of a Surface | 3D surface tolerance | Equal bilateral or unilateral 3D zone |

**Runout Controls:**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| ↗ | Circular Runout | Surface variation at single cross-section | Radial distance at each position |
| ↗↗ | Total Runout | Surface variation along entire surface | Full surface composite variation |

### Material Condition Modifiers

**Maximum Material Condition (MMC) - Ⓜ:**
- For holes: smallest diameter
- For shafts: largest diameter
- Tolerance gets bonus as feature deviates from MMC

**Least Material Condition (LMC) - Ⓛ:**
- For holes: largest diameter
- For shafts: smallest diameter

**Regardless of Feature Size (RFS) - Default if no symbol:**
- Tolerance applies regardless of actual feature size

**Example - Positional Tolerance with MMC:**
```
Hole: ⌀10 +0.2/0 mm
Position tolerance: ⌀0.1 (M) relative to Datum A

If hole diameter = 10.0 mm (MMC):
  Position tolerance = ⌀0.1 mm

If hole diameter = 10.2 mm (LMC):
  Bonus tolerance = 0.2 mm
  Total position tolerance = ⌀0.3 mm
```

**Why this works:**
Larger hole = more clearance for mating fastener = can tolerate more position error.

## Practical GD&T Application Examples

### Example 1: Simple Mounting Plate

**Part:** Aluminum plate with four M6 mounting holes

**Drawing callouts:**

```
1. Datum A: Bottom surface
   Flatness: 0.05 mm

2. Hole diameters: ⌀6.6 +0.1/0 mm (4 places)

3. Hole positions: ⌀0.15 (M) | A |
   True position: 80mm x 60mm rectangular pattern centered on plate

4. Hole perpendicularity: ⊥ ⌀0.1 (M) | A |
```

**Interpretation:**
- Bottom surface must be flat within 0.05mm (reference for all other measurements)
- Holes between 6.6-6.7mm diameter (M6 clearance)
- Hole centers within ⌀0.15mm cylindrical zone from true position when holes at minimum diameter (6.6mm)
- Bonus tolerance: if hole is 6.7mm, position tolerance becomes ⌀0.25mm
- Holes must be perpendicular to bottom surface within ⌀0.1mm cylindrical zone at MMC

### Example 2: Shaft with Bearing Journals

**Part:** Steel shaft with two bearing mounting surfaces

**Drawing callouts:**

```
1. Datum A: Axis of left bearing journal
   (⌀20.00 / 19.98 mm)

2. Right bearing journal: ⌀20.00 / 19.98 mm
   Concentricity: ⌖ 0.02 | A |
   (Center axis must be within ⌀0.02mm cylindrical zone about Datum A axis)

3. Right bearing shoulder face:
   Perpendicularity: ⊥ 0.05 | A |
   (Surface must be within 0.05mm zone between two parallel planes perpendicular to Datum A)

4. Surface finish on bearing journals: 0.8 µm Ra
```

**Interpretation:**
- Left journal defines rotation axis (primary datum)
- Right journal must be concentric within 0.02mm (prevents bearing misalignment)
- Shoulder face perpendicular within 0.05mm (ensures bearing seats flat)
- Surface finish supports bearing operation (smooth rotation, reduced wear)

### Example 3: Machined Block with Perpendicular Hole

**Part:** Milled block with precision cross-hole

**Drawing callouts:**

```
1. Datum A: Bottom surface
   Flatness: 0.03 mm

2. Datum B: Front surface
   Perpendicularity: ⊥ 0.05 | A |

3. Cross-hole: ⌀8.00 / 7.98 mm
   Position: ⊕ ⌀0.05 (M) | A | B |
   Perpendicularity: ⊥ ⌀0.03 (M) | A |
```

**Interpretation:**
- Bottom surface flat within 0.03mm (foundation for all measurements)
- Front surface perpendicular to bottom within 0.05mm (establishes X-Y reference)
- Hole positioned within ⌀0.05mm cylindrical zone relative to Datum A and B intersection (at MMC)
- Hole axis perpendicular to Datum A within ⌀0.03mm cylindrical zone (at MMC)
- Bonus tolerance applies if hole diameter toward LMC (8.00mm)

## GD&T for CNC Processes

### Milling and Turning

**Achievable GD&T tolerances (typical CNC machining):**
- Flatness: 0.02-0.05 mm
- Perpendicularity: 0.02-0.05 mm
- Parallelism: 0.02-0.05 mm
- Position: ⌀0.05-0.1 mm
- Concentricity: 0.02-0.05 mm
- Cylindricity: 0.01-0.02 mm

**Tighter tolerances require:**
- Precision grinding
- Increased inspection
- Temperature-controlled environment

### Plasma, Laser, Waterjet (2D Cutting)

**GD&T typically not applied to edge geometry:**
- Edge perpendicularity poor (taper, dross, HAZ)
- Position tolerances loose (±0.1 to ±0.5mm)

**Where GD&T helps:**
- Flatness of starting material (purchase spec)
- Hole position for parts that undergo secondary machining

### 3D Printing (FDM)

**Challenges:**
- Layer lines create inherent straightness/flatness errors
- Anisotropic properties (different in Z vs XY)
- Shrinkage and warping

**Achievable GD&T:**
- Flatness: 0.2-0.5 mm (top/bottom surfaces)
- Position: ⌀0.3-0.5 mm
- Perpendicularity: 0.3-0.5 mm

**Workaround:** Design witness surfaces for secondary machining if tight GD&T required.

## Tolerance Analysis and Stack-Up with GD&T

### Fixed Fastener Assembly Example

**Problem:** Two plates bolted together. Ensure bolts always fit through both parts.

**Variables:**
- Bolt diameter: 6mm (M6)
- Clearance hole nominal: 6.6mm
- Hole tolerance: +0.1/0 (6.6-6.7mm)
- Hole pattern: 80mm x 60mm

**Without GD&T (traditional):**
```
Hole position: 40 ±0.1 mm from edges
Stack-up: ±0.1 + ±0.1 = ±0.2mm total variation between parts
Required clearance per hole: 6.6 - 6.0 = 0.6mm diameter
Available after stack-up: 0.6 - 2×0.2 = 0.2mm clearance (tight!)
```

**With GD&T and MMC:**
```
Hole diameter: 6.6 +0.1/0 mm
Position: ⌀0.1 (M) | A | B |

At MMC (6.6mm hole):
  Virtual condition = 6.6 - 0.1 = 6.5mm

At LMC (6.7mm hole):
  Virtual condition = 6.7 - 0.2 = 6.5mm (same!)

Clearance per hole: 6.6 - 6.0 = 0.6mm
Projected tolerance zone for mating: ⌀0.1mm guaranteed

Worst case: Both parts at opposite extremes
  Bolt sees virtual condition: 6.5mm
  Minimum hole: 6.6mm
  Guaranteed clearance: 0.1mm minimum (acceptable)
```

**Advantage:** MMC bonus tolerance makes manufacturing easier while guaranteeing assembly.

## Inspection and Verification

### Measuring GD&T Callouts

**Flatness:**
- Surface plate + dial indicator (manual)
- Coordinate Measuring Machine (CMM) with probe
- Laser scanner or optical comparator

**Position:**
- CMM probe measures hole centers
- Software calculates deviation from true position
- Compares to tolerance zone (cylindrical or rectangular)

**Perpendicularity:**
- Precision square + indicator (manual)
- CMM measures surface normal vectors
- Optical methods (autocollimator)

**Concentricity:**
- Part rotated on one datum, runout of other feature measured
- CMM measures multiple points, calculates axes

**Cylindricity:**
- CMM measures surface at multiple heights and angles
- Software generates best-fit cylinder, measures deviation

### Functional Gauging

**Go/No-Go Gauges:**
Simulate worst-case assembly condition.

**Example: Position gage for holes**
```
Gage pins diameter = Virtual Condition
  = Hole MMC - Position Tolerance
  = 6.6 - 0.1 = 6.5mm

If gage pins fit through all holes → Part PASS
If any pin doesn't fit → Part FAIL
```

**Advantage:** Fast, no calculations, anyone can use.

**Disadvantage:** Binary (pass/fail), doesn't indicate how far off.

## Summary

Proper tolerancing is critical for manufacturable, functional parts:

**Traditional Tolerancing:**
- Plus/minus dimensioning: simple, widely understood
- General tolerance notes: reduce drawing clutter
- Stack-up analysis: predict worst-case assembly variation
- Limitations: ambiguous, doesn't control form/orientation

**Geometric Dimensioning & Tolerancing (GD&T):**
- Unambiguous symbols (ASME Y14.5 / ISO 1101)
- Datums define reference frames
- Feature control frames specify exact tolerance zones
- Material condition modifiers (MMC) provide bonus tolerances
- Captures functional requirements precisely

**Best Practices:**
1. Match tolerances to process capabilities
2. Tolerance only critical features tightly
3. Use GD&T for complex parts, assemblies, high-volume production
4. Specify datums that match manufacturing and inspection methods
5. Consider inspection methods during design
6. Communicate with machinists—ensure tolerances are achievable

**Next section** covers how material selection impacts design decisions and manufacturability.

***

**Next:** [Section 16.6: Material Selection for Design](section-16.6-material-selection.md)

**Previous:** [Section 16.4: DFM Principles](section-16.4-dfm-principles.md)
