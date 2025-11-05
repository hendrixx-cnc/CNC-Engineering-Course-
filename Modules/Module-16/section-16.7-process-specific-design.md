# Section 16.7: Process-Specific Design Considerations

## Introduction

Each CNC manufacturing process has unique capabilities, constraints, and optimal design practices. This section synthesizes knowledge from Modules 5-12 of this course, providing CAD design guidelines tailored to each process. Understanding these process-specific considerations allows you to design parts that are not just manufacturable, but optimized for the intended production method.

## CNC Milling (Module 6)

### Process Overview

**Capabilities:**
- 3-axis: X, Y, Z motion (most common)
- 3+2 axis: 3-axis with tilting table/head (indexed positioning)
- Full 5-axis: Simultaneous 5-axis motion (complex surfaces)

**Typical tolerances:** ±0.05 mm (standard), ±0.01 mm (precision)

**Surface finish:** 1.6-3.2 µm Ra (standard), 0.8 µm Ra (finish passes)

### Design Guidelines for Milling

#### 1. Tool Access and Corner Radii

**Internal corners MUST have radius:**
```
Minimum radius = Tool diameter / 2

Practical minimum radius:
  - 1.5 mm (using 3 mm endmill) - common
  - 3 mm (using 6 mm endmill) - robust
  - 6 mm (using 12 mm endmill) - fast material removal
```

**Real-World Cost Impact:**

**Part: 150mm × 100mm aluminum bracket with 80mm × 50mm pocket**

| Corner Specification | Machining Method | Tool Size | Time | Cost @ $80/hr |
|---------------------|------------------|-----------|------|---------------|
| **R0 (sharp 90°)** | Wire EDM required | N/A | 120 min | **$160** |
| **R1.5 (3mm endmill)** | CNC milling | ⌀3mm | 45 min | **$60** |
| **R3 (6mm endmill)** | CNC milling | ⌀6mm | 18 min | **$24** |
| **R6 (12mm endmill)** | CNC milling | ⌀12mm | 12 min | **$16** |

**Key insights:**
- Sharp corners (R0) require EDM: **$160 cost, 7-day lead time**
- R3 corners with standard 6mm tool: **$24 cost (85% savings!), same-day turnaround**
- Larger radii = larger tools = faster material removal = lower cost

**Poor CAD design (Amateur):**
```
┌──────────┐
│          │
│  ┌────┐  │  ← Sharp 90° internal corners
│  │    │  │     IMPOSSIBLE to machine with rotating tool
│  └────┘  │     → Requires EDM: $160, 7-day lead time
│          │
└──────────┘
```

**Good CAD design (Professional):**
```
┌──────────┐
│          │
│  ┌────╮  │  ← R3 internal corners (matches 6mm endmill)
│  │    │  │     → Standard CNC milling: $24, same-day
│  └────╯  │
│          │
└──────────┘
```

**Optimal CAD design (Cost-conscious Professional):**
```
┌──────────┐
│          │
│  ┌────╮  │  ← R6 internal corners (matches 12mm endmill)
│  │    │╮ │     → Fast CNC milling: $16, 2-hour turnaround
│  └────╯╯ │     → 33% faster than R3 version!
│          │
└──────────┘
```

**Design decision workflow:**
1. **Does function REQUIRE sharp corner?** → 95% of time: NO
2. **What's the largest acceptable radius?** → Use that for fastest machining
3. **If sharp corner truly required:** Budget for EDM ($150-300 extra + lead time)

**T-slot exception:**
Undercut features possible with form tools, but limit depth and specify standard form cutter sizes.

#### 2. Pocket Depth Guidelines

**Depth-to-diameter ratio:**
```
Standard pockets: Depth ≤ 3 × Tool_Diameter
Deep pockets: Depth ≤ 5 × Tool_Diameter (slow, higher tool wear)

Example:
  6mm endmill → Maximum practical pocket depth = 18mm (standard), 30mm (deep)
```

**Reducing cycle time:**
- Shallow pockets machine faster (higher feeds/speeds)
- Multiple shallow pockets better than one deep pocket if design allows
- Contour pockets faster than zig-zag in many cases

#### 3. Wall Thickness

**Minimum wall thickness:**
```
Aluminum: 2-3 mm (standard), 1.5 mm (thin-wall with care)
Steel: 3-5 mm (standard), 2 mm (thin-wall)
Plastic: 3-4 mm (standard), 2 mm (thin-wall)
```

**Thin walls deflect during machining:**
- Leave extra stock, rough to near-final, finish in light passes
- Design temporary support tabs (remove in secondary op)
- Add ribs or gussets to strengthen during machining

#### 4. Through Holes vs. Blind Holes

**Through holes (preferred):**
- Faster (drill exit without dwell)
- Easier chip evacuation
- No depth tolerance issues
- Can be drilled from both sides if needed

**Blind holes (when necessary):**
- Specify depth to full diameter (not including drill point)
- Standard drill point angle: 118°
- Add extra depth for point clearance if mating part requires flat bottom

**CAD specification:**
```
Blind hole callout:
  ⌀8 mm × 20 mm deep
  + 4 mm point depth allowance
  = 24 mm total drilling depth
```

#### 5. Chamfers vs. Fillets (External Edges)

**Chamfers (preferred for machining):**
- Single-pass operation
- Faster cycle time
- Standard chamfer mill sizes: 45°, 60°, 82°, 90°
- Removes burrs in same operation
- Good for assembly lead-ins

**Fillets (when required):**
- Need ball endmill or corner radius endmill
- Multiple passes for large radii
- Slower cycle time
- Better for stress reduction in loaded parts

**CAD decision tree:**
```
External edge:
  └─ Is stress concentration a concern?
      ├─ YES → Use fillet (stress relief)
      └─ NO → Use chamfer (faster machining)
```

#### 6. Feature Accessibility

**3-Axis milling constraints:**
```
✓ Features accessible from top
✓ Vertical walls
✗ Undercuts (without flipping/repositioning)
✗ Compound angle holes
```

**Design for single setup:**
- All critical features on same side
- Minimize need for part flipping
- If flip required, design locating features (dowel pins, precision holes)

**Multi-setup design:**
```
Setup 1 (primary datum establishment):
  - Machine Datum A surface (reference plane)
  - Drill datum B and C locating holes

Setup 2 (using established datums):
  - Locate part using datum holes and pins
  - Machine all secondary features referenced to A, B, C
```

#### 7. Material-Specific Milling Considerations

| Material | Cutting Speed | Feed Considerations | Design Implications |
|----------|---------------|---------------------|---------------------|
| Aluminum | High (200-500 m/min) | High feeds possible | Complex features economical |
| Mild Steel | Medium (50-150 m/min) | Moderate feeds | Simpler features preferred |
| Stainless | Low (30-80 m/min) | Light feeds (work-hardens) | Minimize deep pockets, thin walls |
| Plastics | Variable | Risk of melting | Sharp tools, conservative speeds |

### Milling CAD Checklist

- [ ] All internal corners radiused ≥ 1.5 mm
- [ ] Pocket depths ≤ 3× tool diameter
- [ ] Wall thickness ≥ 2 mm (aluminum), ≥ 3 mm (steel)
- [ ] Through holes used instead of blind holes where possible
- [ ] Chamfers specified on external edges (unless stress relief needed)
- [ ] All features accessible from single setup when possible
- [ ] Datums specified for multi-setup parts
- [ ] Tolerances appropriate for milling capability (±0.05 mm standard)

***

## CNC Turning (Lathe Operations)

### Process Overview

**Capabilities:**
- Axially symmetric parts (cylindrical)
- External turning, facing, grooving, threading
- Internal boring, drilling, threading
- Typical tolerances: ±0.025 mm (standard), ±0.005 mm (precision)

### Design Guidelines for Turning

#### 1. Axial Symmetry Requirement

**Ideal for turning:**
```
Shafts, bushings, spacers, pulleys, threaded rods
  - All features concentric about central axis
  - Diameters, grooves, threads
```

**Not ideal for turning:**
```
Features off-axis (flats, cross-holes, keyways)
  - Requires secondary milling operations
  - Or mill-turn machine
```

#### 2. Diameter Changes and Shoulders

**Smooth transitions preferred:**
```
Gradual diameter reduction = efficient cutting
Sharp shoulders = tool changes, slower cycle time
```

**Undercuts and grooves:**
```
Groove width = Tool width + clearance
  Standard grooving tool widths: 2, 3, 4, 5, 6 mm

Minimize groove depth:
  Deep grooves = slow, potential chatter
  Depth < 2× width (preferred)
```

**Relief grooves for threads:**
```
Thread relief: Allow threading tool runout
  Width ≥ thread pitch × 2
  Depth ≥ thread depth × 1.2
```

#### 3. Length-to-Diameter Ratio

**Rigidity concerns:**
```
L/D < 3: Very rigid, no tailstock support needed
L/D = 3-10: Moderate, may need tailstock or steady rest
L/D > 10: Flexible, requires support, slow cutting
```

**CAD design optimization:**
- Reduce length where possible
- Add diameter where length required (↑ stiffness)
- Design for stock support (live centers, steady rests)

#### 4. Internal Features (Boring)

**Through bores (preferred):**
```
✓ Tool passes completely through
✓ Easier chip evacuation
✓ No depth tolerance issues
```

**Blind bores:**
```
Depth ≤ 4× Diameter (practical limit)
  Deeper = slow, risk of tool deflection/chatter
```

**Minimum bore diameter:**
```
Typically: ≥ 5 mm (small lathes)
           ≥ 10 mm (production lathes)
Limited by smallest available boring bar rigidity
```

#### 5. Threading Considerations

**External threads (standard):**
```
Thread relief groove required at shoulder
  Allows threading tool to exit cleanly

Chamfer start of thread:
  45° chamfer = easier assembly, protects thread start
```

**Internal threads:**
```
Thread relief groove or through-bore preferred
Blind tapped holes: ensure adequate thread engagement
  Steel into steel: 1× diameter
  Aluminum into aluminum: 1.5× diameter
```

**Standard pitches preferred:**
```
Metric: M6×1.0, M8×1.25, M10×1.5 (coarse standard)
Unified: 1/4-20, 5/16-18, 3/8-16 (coarse standard)
```

#### 6. Knurling

**Knurled surfaces for grip:**
```
Standard knurl patterns:
  - Diamond knurl (crossed diagonal)
  - Straight knurl (parallel to axis)

Knurl dimensions:
  - Increases diameter by ~0.1-0.2 mm
  - Specify diameter BEFORE knurling
  - Tolerance after knurling: ±0.2 mm typical
```

### Turning CAD Checklist

- [ ] Part is axially symmetric (or can be made so)
- [ ] Diameter changes have fillets/chamfers (not sharp shoulders)
- [ ] Grooves match standard tool widths
- [ ] Thread reliefs specified
- [ ] Length-to-diameter ratio < 10 (or supports designed)
- [ ] Through bores used when possible
- [ ] Standard thread pitches specified
- [ ] Tolerances appropriate for turning (±0.025 mm standard)

***

## Plasma Cutting (Module 5)

### Process Overview

**Capabilities:**
- 2D profiles from sheet metal
- Material thickness: 1-50 mm (typical systems)
- Typical tolerance: ±0.5 mm
- Kerf width: 1-4 mm (depending on material/thickness)

### Design Guidelines for Plasma Cutting

#### 1. Kerf Width Compensation

**Kerf = width of cut removed by plasma arc**
```
Design hole: ⌀50 mm
Kerf width: 2 mm
CAM compensation: Path offset inward by 1 mm (radius compensation)
Actual hole: ~⌀50 mm (after kerf)
```

**Real-World Example: Precision Holes in Plasma-Cut Parts**

**Amateur Mistake:**
- CAD model: ⌀25.0mm hole for ⌀25mm shaft
- Plasma cuts with 2mm kerf, NO compensation applied
- **Actual hole:** ⌀27mm (2mm oversized!)
- **Result:** Shaft has 2mm slop, part rejected

**Professional Approach:**
- CAD model: ⌀25.0mm hole (nominal dimension)
- CAM applies kerf compensation automatically
- Plasma torch path: ⌀24.0mm (offset inward 1mm radius)
- **Actual hole:** ⌀25.0mm ±0.5mm (within tolerance)
- **Result:** Part accepted

**Cost Impact of Kerf Compensation Errors:**

| Mistake | Consequence | Cost |
|---------|-------------|------|
| No compensation | 50-part batch rejected, all holes oversized | **$1,200 scrap** |
| Wrong compensation direction | Holes undersized, requires secondary drilling | **+$15 per part** |
| Correct compensation | Parts within tolerance | **$0 extra** |

**CAD Best Practice:**
- Model nominal dimensions (what you want final part to be)
- Let CAM software apply kerf compensation
- Don't manually adjust CAD unless you're compensating for known process variations
- Always run test cut on first part to verify actual dimensions

#### 2. Minimum Feature Size

**Minimum hole diameter:**
```
Min diameter ≥ Material thickness
  3 mm plate → ⌀3 mm holes okay
  10 mm plate → ⌀10 mm holes minimum
```

**Minimum slot width:**
```
Min width ≥ Material thickness
```

**Reason:** Thicker materials require higher power, larger kerf, harder to cut small features.

#### 3. Edge Quality and Taper

**Plasma cut edges are NOT square:**
```
Top edge: slight roundover (arc initiation)
Cut face: 1-5° taper
Bottom edge: dross (molten metal)
```

**CAD design implications:**
- Specify top or bottom surface as reference
- Don't expect tight fit assemblies without secondary machining
- If precision required, leave stock for milling/grinding

**Dross attachment:**
- Worse on bottom edge
- Thicker materials = more dross
- Design parts to hide bottom edge or plan for grinding

#### 4. Pierce Points and Lead-Ins

**Pierce point = where arc starts (burns through material)**
```
Never pierce:
  ✗ On finished edge
  ✗ In small holes
  ✗ On critical features

Pierce location:
  ✓ In scrap area
  ✓ Lead-in path from scrap to part edge
```

**CAD design tip:**
- Provide scrap areas for pierce points
- Avoid tiny internal cutouts (require pierce per feature)

#### 5. Corner Radii and Sharp Corners

**Plasma can cut sharp external corners:**
```
External 90° corners: Okay (slight radius from kerf)
```

**Internal corners have kerf radius:**
```
Internal corners: Minimum radius ~ kerf width / 2
  Kerf 2 mm → internal corners ~1 mm radius
```

**CAD approach:**
- External corners: can be sharp (CAD shows sharp, plasma will add slight radius)
- Internal corners: model with radius ≥ kerf/2 for accuracy

#### 6. Nesting and Material Utilization

**CAD design for nesting:**
```
Spacing between parts: ≥ 10 mm (allows cut path without interference)
Edge margin: ≥ 5 mm from sheet edge
```

**Part orientation:**
- Rectangular parts: align with sheet edges (minimize waste)
- Interlocking shapes for maximum material usage

**Material comes in standard sheets:**
```
Common sizes:
  4' × 8' (1220 × 2440 mm)
  5' × 10' (1525 × 3050 mm)
```

Design part dimensions to nest efficiently on standard sheets.

### Plasma Cutting CAD Checklist

- [ ] All parts are 2D profiles (no 3D features)
- [ ] Hole diameters ≥ material thickness
- [ ] Tolerances appropriate for plasma (±0.5 mm typical)
- [ ] Top or bottom edge specified as datum (not center of edge)
- [ ] Pierce point locations considered (scrap areas provided)
- [ ] Part designed for efficient nesting
- [ ] If tight tolerances needed, stock left for secondary machining

***

## Laser Cutting (Module 7)

### Process Overview

**Capabilities:**
- 2D profiles from sheet metal
- Material thickness: 0.5-25 mm (fiber laser typical)
- Typical tolerance: ±0.1 mm
- Kerf width: 0.1-0.5 mm (much smaller than plasma)

### Design Guidelines for Laser Cutting

#### 1. Precision and Tolerances

**Laser cutting is more precise than plasma:**
```
Achievable tolerances: ±0.1 mm (vs ±0.5 mm plasma)
Kerf width: 0.2 mm typical (vs 2-4 mm plasma)
Edge perpendicularity: Better (less taper)
```

**CAD implications:**
- Can design tighter-fitting assemblies
- Smaller features practical
- Tab-and-slot joints feasible

#### 2. Minimum Feature Size

**Thinner materials allow smaller features:**
```
Material | Min Hole Diameter | Min Slot Width
---------|-------------------|---------------
1 mm     | 1 mm              | 0.5 mm
3 mm     | 3 mm              | 1.5 mm
6 mm     | 6 mm              | 3 mm
12 mm    | 12 mm             | 6 mm

Rule: Min feature ≈ Material thickness
```

#### 3. Heat-Affected Zone (HAZ)

**Laser creates narrow heat-affected zone:**
```
HAZ width: 0.1-0.5 mm from cut edge
Material near cut edge:
  - Hardened (steel)
  - Annealed (aluminum)
  - Discolored (stainless - "blueing")
```

**CAD design considerations:**
- Avoid tight bends immediately adjacent to cut edge (HAZ is brittle)
- Leave ≥ 2 mm between cut edge and bend line
- If cosmetic appearance critical, specify edge finishing

#### 4. Tab-and-Slot Joints

**Laser precision enables snap-fit assemblies:**
```
Slot width = Tab width + Fit clearance

Press fit: Clearance = -0.05 to 0 mm (interference)
Slide fit: Clearance = +0.05 to +0.1 mm
Loose fit: Clearance = +0.2 to +0.3 mm
```

**Design example: Sheet metal enclosure**
```
3 mm material thickness
Slot width: 3.05 mm (slide fit for 3 mm tab)
Tab length: 10 mm (engagement length)
```

**CAD parametric approach:**
```
material_thickness = 3 mm
fit_clearance = 0.05 mm   # Slide fit
slot_width = material_thickness + fit_clearance
tab_width = material_thickness
```

#### 5. Engraving and Marking

**Laser can engrave surfaces (defocused beam):**
```
Engraving depth: 0.1-0.5 mm typical
Applications:
  - Part numbers
  - Logos, text
  - Reference marks
```

**CAD specification:**
```
Create sketch on part surface with text/graphics
Specify engraving depth in CAM (not part geometry)
```

#### 6. Cutting Order and Small Part Retention

**Small parts can tip into cut kerf before completion:**
```
Solution: Cut internal features first, external perimeter last
  - Keeps part supported until final cut
  - CAM software typically handles this automatically
```

**Micro-tabs:**
```
Small connecting tabs (0.5-1 mm) hold part to sheet
Broken off after cutting (leave small witness marks)
```

### Laser Cutting CAD Checklist

- [ ] Tolerances appropriate for laser (±0.1 mm achievable)
- [ ] Minimum feature sizes ≥ material thickness
- [ ] Tab-and-slot joints dimensioned with appropriate clearance
- [ ] Bend lines ≥ 2 mm from cut edges (HAZ consideration)
- [ ] Engraving/marking specified if needed
- [ ] Part retention (tabs or cutting order) considered for small parts

***

## Waterjet Cutting (Module 8)

### Process Overview

**Capabilities:**
- 2D profiles from virtually any material
- Material thickness: 0.5-200 mm (abrasive waterjet)
- Typical tolerance: ±0.15 mm
- Kerf width: 0.8-1.5 mm
- No heat-affected zone (cold cutting)

### Design Guidelines for Waterjet Cutting

#### 1. Taper Compensation

**Waterjet stream diverges as it penetrates material:**
```
Top surface: Entry point (smaller)
Bottom surface: Exit point (larger) due to jet expansion

Typical taper: 1-3° (depending on thickness, pressure, abrasive)

Example:
  12 mm thick material, 1.5° taper
  Top edge: 50.00 mm
  Bottom edge: 50.63 mm
  (larger by ~0.3 mm)
```

**CAD approach for critical dimensions:**
```
Specify which surface is critical:
  - Top surface critical: Cut with taper compensation
  - Bottom surface critical: Flip part orientation
  - Both critical: Secondary machining required
```

**Modern waterjet CAM:**
- 5-axis waterjet can tilt cutting head to compensate for taper
- Creates near-vertical edges even in thick material

#### 2. Material Thickness Considerations

**Waterjet excels at thick materials:**
```
Thickness | Cut Speed | Edge Quality
----------|-----------|-------------
3 mm      | Fast      | Excellent
12 mm     | Medium    | Good
25 mm     | Slow      | Fair
50 mm+    | Very slow | Requires slow feed for quality
```

**CAD design tip:**
- For thick materials (>25 mm), consider if plasma (steel) or bandsaw (rough cutting) + milling (finishing) is more economical

#### 3. Abrasive Considerations

**Abrasive creates slightly rough edge:**
```
Surface finish: 3-6 µm Ra (smooth pass)
              10-15 µm Ra (fast pass)

Not suitable for:
  - Sealing surfaces (without secondary finishing)
  - High-precision mating (tolerance too loose)
```

**CAD specification:**
- If smooth edge required, specify "quality pass" in CAM (slower cutting)
- If precision required, leave stock for grinding/milling

#### 4. No Heat-Affected Zone

**Major advantage over plasma/laser:**
```
✓ No thermal distortion
✓ No hardening (metals)
✓ No melting (plastics)
✓ Can cut composite/laminate materials without delamination
```

**Ideal materials for waterjet:**
- Hardened steel (already heat-treated)
- Aluminum (no HAZ concerns)
- Glass, stone, ceramics
- Composite materials (carbon fiber, fiberglass)

#### 5. Piercing and Delicate Features

**Piercing creates larger hole than cutting path:**
```
Pierce diameter: ~2× normal kerf width

Design approach:
  - Pierce in scrap area or large feature
  - Lead-in to final feature
  - Avoid piercing in small holes
```

#### 6. Stack Cutting

**Waterjet can cut multiple sheets stacked together:**
```
Stack 2-5 sheets of thin material
Cut all at once (economic for production runs)

Requirements:
  - Sheets must be clamped/secured (prevent shifting)
  - Top sheet can have slight variation from bottom sheet (taper)
```

**CAD approach:**
- Design allows for slight variation between parts (±0.2 mm)

### Waterjet Cutting CAD Checklist

- [ ] Tolerances appropriate for waterjet (±0.15 mm typical)
- [ ] Taper considered for thick materials (specify critical surface)
- [ ] Edge quality requirement specified (standard or quality pass)
- [ ] Pierce points located in scrap or large features
- [ ] Material thickness within waterjet capabilities
- [ ] If precision mating required, stock left for secondary machining

***

## FDM 3D Printing (Module 11)

### Process Overview

**Capabilities:**
- Complex 3D geometries
- Build volume: 200×200×200 mm (desktop) to 1000×1000×1000 mm (large format)
- Typical tolerance: ±0.3 mm (desktop), ±0.5 mm (large format)
- Layer height: 0.1-0.4 mm

### Design Guidelines for FDM

#### 1. Layer Orientation and Strength Anisotropy

**FDM parts are anisotropic (directional strength):**
```
Strength parallel to layers (XY): ~100%
Strength perpendicular to layers (Z): ~50-70%

Failure mode: Delamination between layers
```

**CAD design strategy:**
```
Orient part so primary loads are parallel to layer lines

Example: Hook design
  Poor orientation:  Load pulls perpendicular to layers → delamination
  Good orientation: Load pulls parallel to layers → high strength
```

**CAM decision (not CAD):**
- Part orientation set in slicer software
- But CAD designer should consider orientation during design

#### 2. Overhangs and Support Material

**Maximum overhang angle without support:**
```
45° rule: Angles ≤ 45° from vertical can self-support
          Angles > 45° require support material

Example:
  Wall at 30° from vertical: Okay without support
  Wall at 60° from vertical: Requires support
```

**Support material:**
```
Printed structure beneath overhangs
Must be removed after printing (manual or dissolvable)
Leaves rough surface where support contacted part
```

**Real-World Cost Impact: Bracket Design**

**Part: 80mm × 60mm × 40mm mounting bracket with overhang**

**Amateur Design (no consideration for supports):**
- Horizontal mounting flange (90° overhang)
- Requires dense support material underneath
- Print time: **6 hours**
- Support material: 45g PLA @ $0.05/g = **$2.25**
- Support removal time: **15 minutes** @ $30/hr = **$7.50**
- Surface finish: Rough on support contact areas (requires sanding)
- **Total extra cost from supports: $9.75 per part**

**Professional Design (45° chamfer instead of flat overhang):**
- Mounting flange with 45° chamfer (no support needed)
- Print time: **4.5 hours** (25% faster!)
- Support material: **$0**
- Support removal time: **$0**
- Surface finish: Clean on all surfaces
- **Total savings: $9.75 per part + better quality**

**Comparison for 50-part production run:**
- Amateur design: 50 × $9.75 = **$487.50 extra cost** + 12.5 hours labor
- Professional design: **$0 extra cost**, clean finish, 75 hours less print time

**CAD Design Strategies to Minimize Supports:**

| Design Feature | Poor (Needs Support) | Good (No Support) | Savings per Part |
|----------------|----------------------|-------------------|------------------|
| Mounting flange | Horizontal (90°) | 45° chamfer | $9.75 |
| Through hole | Vertical hole (ceiling) | Horizontal hole or teardrop | $3.50 |
| Overhang boss | Circular boss beneath | Chamfered or tiered | $5.25 |
| Cable channel | Enclosed tunnel | Open channel (print upside down) | $12.00 |

**CAD design to minimize supports:**
```
✓ Avoid overhangs > 45° (design with chamfers)
✓ Use chamfers instead of overhanging curves
✓ Orient part to minimize overhangs
✓ Add built-in support structures (tearaway tabs) if needed
✓ Use teardrop-shaped holes instead of circular (for horizontal holes)
✗ Don't create large flat overhanging surfaces
✗ Don't design features that create trapped pockets (support can't be removed)
```

#### 3. Bridging

**Bridging = horizontal unsupported span:**
```
Maximum bridge distance: 10-20 mm (material/printer dependent)

Example:
  Bridge across 10 mm gap: Usually okay
  Bridge across 50 mm gap: Requires support
```

**CAD design for bridging:**
```
✓ Keep horizontal unsupported spans < 15 mm
✓ Add vertical support columns if larger spans required
```

#### 4. Wall Thickness and Shell Design

**Minimum wall thickness:**
```
Single wall: 0.4 mm (nozzle diameter, fragile)
2 walls: 0.8 mm (minimum practical)
3 walls: 1.2 mm (good strength)
4+ walls: 1.6 mm+ (structural)

Recommended minimum: 2 mm (robust, easy to print)
```

**Shell and infill:**
```
Exterior shells: Solid (printer default: 2-4 perimeters)
Interior: Infill pattern (20% infill common)

Solid parts: 100% infill (slow, expensive, often unnecessary)
```

**CAD design:**
- Model solid geometry (CAD shows full part)
- Slicer software applies shell/infill settings
- No need to model infill in CAD

#### 5. Hole Compensation

**Holes print undersized:**
```
Designed hole: ⌀8 mm
Actual printed: ⌀7.7-7.9 mm (material shrinkage, thermal contraction)

Compensation:
  Design holes +0.2 to +0.3 mm oversized
  OR drill/ream after printing
```

**Vertical vs horizontal holes:**
```
Vertical holes (parallel to build axis):
  More accurate (circular cross-section each layer)

Horizontal holes (perpendicular to build axis):
  Less accurate (stair-stepping from layer lines)
  Oval cross-section if small diameter
```

**CAD parametric compensation:**
```
nominal_hole = 8 mm
fdm_compensation = 0.2 mm
print_hole_size = nominal_hole + fdm_compensation  # = 8.2 mm
```

#### 6. Threads and Fasteners

**Printed threads:**
```
Large threads (M10+): Can be printed directly
  - Coarse pitch preferred
  - Vertical orientation best

Small threads (M6 and smaller): Often unreliable
  - Use threaded inserts instead
```

**Threaded inserts (preferred):**
```
Heat-set inserts: Press into slightly undersized hole with soldering iron
  - Excellent pullout strength
  - Repeatable assembly/disassembly
  - Specify insert size (M3, M4, M5, etc.)

Press-fit inserts: Tapered threads cut into plastic
  - Good for low-cycle applications
```

**CAD approach:**
```
Model hole for insert, not threads:
  Heat-set insert: Hole = Insert OD - 0.2 mm (interference fit)
  Example: M3 insert (OD 4.6 mm) → ⌀4.4 mm hole
```

#### 7. Tolerances and Fits

**Clearance for sliding fits:**
```
Clearance = 0.3-0.5 mm (desktop FDM)
           0.5-0.8 mm (large format FDM)

Example: 8 mm shaft in bearing
  Shaft: ⌀8.0 mm
  Bearing hole: ⌀8.5 mm (0.5 mm clearance)
```

**Press fits:**
```
Interference = 0.1-0.2 mm (light press)
             0.3-0.5 mm (firm press, risk of cracking)
```

#### 8. Print-in-Place Assemblies

**Design parts that assemble as they print:**
```
Requirements:
  - Clearance ≥ 0.3 mm between moving parts
  - Vertical clearance ≥ 1 layer height (0.2 mm typical)

Examples:
  - Chain links
  - Hinges
  - Ball joints
```

**CAD design:**
```
Model assembly in assembled position
Ensure clearance between all moving parts
Verify no fused connections (slicer preview)
```

### FDM 3D Printing CAD Checklist

- [ ] Part oriented so loads parallel to layer lines
- [ ] Overhangs ≤ 45° (or support structures accepted)
- [ ] Horizontal unsupported spans ≤ 15 mm
- [ ] Wall thickness ≥ 2 mm for structural parts
- [ ] Holes oversized by 0.2 mm (compensation for shrinkage)
- [ ] Threaded inserts specified instead of printed threads (M6 and smaller)
- [ ] Tolerances appropriate for FDM (±0.3 mm desktop, ±0.5 mm large format)
- [ ] Print-in-place clearances ≥ 0.3 mm

***

## Hybrid Systems (Module 12)

### Combining Multiple Processes

**Common hybrid workflows:**

**1. Plasma/Laser + Milling:**
```
Step 1: Cut profile from plate (plasma/laser) - fast 2D cutting
Step 2: Mill precision features (holes, pockets, faces) - precise 3D machining

Advantages:
  - Saves milling time (profile already cut)
  - Better material utilization than milling from solid
```

**CAD approach:**
```
Design complete 3D part in CAD
Export 2D profile (DXF) for plasma/laser
Export 3D model for CAM milling program
Specify which features are cut vs milled
```

**2. 3D Print + Machining:**
```
Step 1: FDM print near-net shape - complex organic geometry
Step 2: Mill critical surfaces - precision datum and mating features

Advantages:
  - Complex geometry from 3D printing
  - Precision where needed from machining
```

**CAD approach:**
```
Model final part geometry
Add stock allowance on machined surfaces (0.5-1 mm)
Export STL for 3D printing (with stock)
Export STEP for CAM (final dimensions)
```

**3. Waterjet + Bending:**
```
Step 1: Waterjet cut flat pattern
Step 2: Brake press bend to final shape

Advantages:
  - Complex 2D profiles
  - 3D formed structure
  - No HAZ from waterjet (bending not affected)
```

**CAD approach:**
```
Model 3D folded part
Create flat pattern (sheet metal tools)
Export flat pattern DXF for waterjet
Specify bend lines, radii, angles for press brake
```

### Hybrid CAD Considerations

**Stock allowance for secondary machining:**
```
Plasma/laser cut → mill: +0.5-1 mm on machined faces
Waterjet cut → mill: +0.3-0.5 mm on machined faces
3D print → mill: +0.5-1 mm on machined faces
Casting → mill: +2-3 mm on machined faces
```

**Datum establishment:**
```
Primary process: Establishes locating features
Secondary process: References primary datums

Example:
  Waterjet: Cut perimeter and locating holes
  Milling: Use locating holes to fixture part, mill precision pockets
```

**Tolerance distribution:**
```
Rough process (plasma): ±0.5 mm
Finishing process (milling): ±0.05 mm on finished surfaces

Overall part: Mixed tolerances (specify which features are precision)
```

## Summary

Each CNC process has unique capabilities and constraints that influence CAD design. Understanding process-specific design rules can reduce costs by 40-90% while improving manufacturability.

### Cost Impact Summary: Process-Specific Design Decisions

This section demonstrated real-world cost impacts of process-aware CAD design:

| Process | Design Decision | Poor Design Cost | Good Design Cost | Savings |
|---------|----------------|------------------|------------------|---------|
| **Milling** | Corner radius (sharp vs R6) | $160 (EDM) | $16 (12mm endmill) | **90%** |
| **Plasma** | No kerf compensation | $1,200 (50-part scrap) | $0 (correct CAM) | **100%** |
| **FDM** | Support material | $9.75/part + rough finish | $0/part + clean | **100%** |

**Key Process Capabilities and Constraints:**

| Process | Tolerance | Key Design Considerations | Amateur Mistake | Cost Impact |
|---------|-----------|---------------------------|-----------------|-------------|
| **Milling** | ±0.05mm | Corner radii (R = tool radius), tool access, pocket depth | Sharp internal corners | +$140 per part (EDM) |
| **Turning** | ±0.025mm | Axial symmetry, L/D ratio <10, grooves, threading | High L/D (no tailstock) | Scrap from deflection |
| **Plasma** | ±0.5mm | 2D only, 1-4mm kerf, taper, pierce points | No kerf compensation | 100% scrap rate |
| **Laser** | ±0.1mm | 2D precision, small kerf (0.2-0.5mm), HAZ, tab-and-slot | Tight nested parts | Thermal warping |
| **Waterjet** | ±0.15mm | No HAZ, taper on thick materials, abrasive finish | Ignore taper | Fit issues on assemblies |
| **FDM** | ±0.3mm | Layer orientation, 45° overhangs, hole compensation, inserts | Horizontal overhangs | +$10/part support removal |
| **Hybrid** | Mixed | Stock allowance, datum references, tolerance distribution | No stock allowance | Part dimensions wrong |

### Critical Takeaways by Process

**CNC Milling:**
- **Corner radii cost hierarchy:** R0 = $160 (EDM) → R3 = $24 (6mm tool) → R6 = $16 (12mm tool)
- Larger corner radii = larger tools = faster machining = lower cost
- 95% of designs don't functionally require sharp corners

**Plasma Cutting:**
- **Kerf compensation errors:** $1,200 batch scrap vs $0 with proper CAM setup
- Always model nominal dimensions, let CAM compensate for kerf
- First-part verification critical (±0.5mm tolerance)

**FDM 3D Printing:**
- **Support material avoidance:** $9.75 savings per part + better surface finish
- 45° chamfer design rule eliminates most support needs
- 50-part run: $487 savings by designing for no supports

### Professional Design Workflow

**Step 1: Process Selection**
- Geometry: 2D (plasma/laser/waterjet) vs 3D (milling/FDM)
- Material: Metals (milling/plasma/laser/waterjet) vs Plastics (FDM/milling)
- Quantity: Low (<10) vs Medium (10-100) vs High (>100)
- Tolerance: Rough (±0.5mm) vs Standard (±0.1mm) vs Precision (±0.01mm)

**Step 2: Apply Process-Specific Rules**
- Reference this section's guidelines for chosen process
- Design parts that are EASY to make (not just possible)
- Larger radii, standard features, appropriate tolerances

**Step 3: Cost Validation**
- Review design against cost multipliers
- Sharp corners? EDM adds $150+
- Tight tolerances? Precision grinding adds 4-20× cost
- Support material? FDM adds $10+ per part

**Step 4: CAM Simulation**
- Visualize toolpaths before manufacturing
- Verify tool access, detect collisions
- Estimate accurate cycle times

**Step 5: First Article Inspection**
- Measure critical dimensions on first part
- Validate process capability
- Adjust if needed before full production

**Amateur vs Professional Mindset:**
- **Amateur:** "Design the perfect part, then figure out how to make it"
- **Professional:** "Design for the manufacturing process, optimizing cost and quality simultaneously"

**Next section** covers assembly design, bringing multiple manufactured parts together into functional systems.

***

**Next:** [Section 16.8: Assembly Design](section-16.8-assembly-design.md)

**Previous:** [Section 16.6: Material Selection](section-16.6-material-selection.md)
