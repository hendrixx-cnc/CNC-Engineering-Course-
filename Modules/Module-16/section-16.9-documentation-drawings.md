# Section 16.9: Documentation and Engineering Drawings

## Introduction

Engineering drawings are the universal language of manufacturing. While your CAD model contains all geometric information, drawings communicate design intent, specifications, and manufacturing requirements to machinists, inspectors, and assemblers. Well-executed drawings ensure parts are made correctly the first time, reducing errors, scrap, and costly rework.

This section covers drawing standards, view selection, dimensioning strategies, and best practices for creating clear, unambiguous technical documentation.

## Drawing Standards

### International Standards

**ASME Y14.5 (United States):**
- Geometric Dimensioning and Tolerancing (GD&T)
- Dimensioning and tolerancing practices
- Widely used in North America

**ISO 128 / ISO 1101 (International):**
- Technical drawings general principles
- Geometrical tolerancing
- Used globally, especially in Europe and Asia

**Third-Angle vs. First-Angle Projection:**
```
Third-angle (ASME, North America):
  Object between observer and projection plane
  Top view above front view
  Right view to right of front view

First-angle (ISO, Europe):
  Projection plane between observer and object
  Top view below front view
  Right view to left of front view
```

**Symbol to indicate projection type:**
- Third-angle: Truncated cone symbol
- First-angle: Opposite truncated cone orientation

**Consistency:** Use one standard throughout a project. Most CAD systems default to third-angle (ASME).

### Drawing Sheet Formats

**Standard sheet sizes:**

| Size | ANSI (inches) | ISO (mm) |
|------|---------------|----------|
| A | 8.5 × 11 | A4: 210 × 297 |
| B | 11 × 17 | A3: 297 × 420 |
| C | 17 × 22 | A2: 420 × 594 |
| D | 22 × 34 | A1: 594 × 841 |
| E | 34 × 44 | A0: 841 × 1189 |

**Sheet selection:**
- Simple parts: A or A4
- Complex parts, assemblies: B or A3
- Large assemblies, layouts: C, D, or larger

### Title Block

**Required information:**
```
┌─────────────────────────────────────────┐
│ [Drawing Views]                         │
│                                         │
│                                         │
│                                         │
├─────────────────────────┬───────────────┤
│ TITLE BLOCK             │ Rev │ Date    │
│ Part Name: Motor Bracket│ A   │2024-3-15│
│ Part Number: MB-2024-001│     │         │
│ Material: AL 6061-T6    │     │         │
│ Finish: Anodize Type II │     │         │
│ Designer: [Name]        │     │         │
│ Drawn: [Date]          │     │         │
│ Scale: 1:1             │     │         │
│ Sheet: 1 of 1          │     │         │
└─────────────────────────┴───────────────┘
```

**Essential title block fields:**
- Part name / description
- Part number (unique identifier)
- Revision level
- Material specification
- Finish / coating
- Scale
- Designer / drafter
- Date drawn / revised
- Sheet number (if multi-sheet)
- Company name / logo

## View Selection

### Orthographic Projection

**Standard views:**
```
Front view: Primary view (most detail, natural orientation)
Top view: Looking down from above
Right side view: Looking from right side
Left side view: Looking from left side (rarely used with right view)
Bottom view: Looking up from below (rarely needed)
Rear view: Looking from behind (rarely needed)
```

**Minimum views principle:**
- Use only the views necessary to fully define the part
- Typical simple part: 2-3 views
- Symmetrical parts: May need only 1-2 views + note "SYMMETRIC ABOUT CENTERLINE"

**View selection strategy:**
1. **Front view:** Most informative orientation, shows primary features
2. **Top/Side view:** Shows features not clear in front view
3. **Auxiliary/Section views:** Only if standard views insufficient

### Section Views

**When to use section views:**
- Internal features (pockets, bores, cavities)
- Complex internal geometry
- Wall thicknesses
- Assembly interfaces

**Section view types:**

**Full Section:**
```
Cutting plane passes completely through part
Shows entire internal cross-section
Most common type
```

**Half Section:**
```
Quarter of part removed
Shows both exterior and interior in single view
Good for symmetric parts
```

**Offset Section:**
```
Cutting plane offsets to pass through multiple features
Shows features not on same plane
```

**Broken-Out Section:**
```
Small local section (doesn't extend across entire view)
Shows specific internal detail
```

**Section line conventions:**
```
General purpose (most materials): 45° hatching
Cast iron: Random broken lines
Aluminum/magnesium: Wider spacing 45° lines
```

**Section view labeling:**
```
Cutting plane line: A-A
Section view title: SECTION A-A
Scale (if different from main): SCALE 2:1
```

### Detail Views

**Magnified detail of small features:**
```
Main view: Part at 1:2 scale
Detail A: Specific feature at 2:1 scale (magnified)

Label:
  On main view: "DETAIL A" with circle around feature
  Detail view: "DETAIL A" with "SCALE 2:1"
```

**When to use:**
- Threads, small chamfers, complex small features
- Avoid cluttering main view with dimensions
- Clarify geometric complexity

### Auxiliary Views

**View projected at angle to standard views:**

**When needed:**
- Features at angles (not parallel to standard planes)
- True size/shape of angled surfaces
- Hole patterns on angled faces

**Example:**
```
Part with surface at 30° to horizontal
Standard views show surface foreshortened (not true size)
Auxiliary view perpendicular to angled surface shows true dimensions
```

## Dimensioning Strategies

### Dimensioning Principles

**Dimension once:**
- Each feature dimensioned only once
- Avoid redundant dimensions (causes conflicts if tolerances differ)

**Dimension to function:**
- Show dimensions the way the part will be inspected
- Relate features that interact (mating surfaces, bolt patterns)

**Chain vs. Baseline Dimensioning:**

**Chain dimensioning (avoid):**
```
├─ 25 ─┼─ 30 ─┼─ 25 ─┤
Tolerance stack-up: ±0.1 + ±0.1 + ±0.1 = ±0.3mm total
```

**Baseline dimensioning (preferred):**
```
├─ 25 ─┤
├──── 55 ────┤
├──────── 80 ────────┤
Each dimension independent, from common datum
Tolerance: Each dimension ±0.1mm (no stack-up)
```

**Datum-based dimensioning:**
```
All critical dimensions referenced to datum surfaces (A, B, C)
Matches GD&T approach
Aligns with manufacturing setup and inspection
```

### Dimension Placement

**Outside the view (preferred):**
```
        50
    ├────────┤
    ┌────────┐
    │        │  30
    │        │  ↕
    └────────┘
```

**Inside the view (only if necessary):**
- Avoid when possible (clutters view)
- Use for large parts where outside dimension too far from feature

**Leader lines:**
```
Use for holes, callouts, notes
Arrow points to feature
Text at end of leader, horizontal
```

**Dimension line spacing:**
```
First dimension: 10mm from part outline
Subsequent dimensions: 6-8mm spacing between lines
Prevents crowding, improves readability
```

### Dimensioning Specific Features

**Holes:**
```
⌀8.0 +0.1/0  (diameter, unilateral tolerance)
⌀8.0 ±0.05   (diameter, bilateral tolerance)
⌀8 THRU      (through hole, no depth specified)
⌀10 ↧15      (counterbore: diameter 10, depth 15)
⌀8 ⌴90°      (countersink: diameter 8, 90° angle)
```

**Threads:**
```
M6×1.0 – 6H  (metric thread, 6mm diameter, 1mm pitch, 6H fit class)
M8×1.25 THRU (metric thread through-hole)
M6×1.0 ↧12   (metric thread, 12mm deep)
1/4-20 UNC   (unified coarse thread, 1/4" diameter, 20 TPI)
```

**Chamfers:**
```
2 × 45°      (2mm × 45° chamfer)
1 × 30°      (1mm × 30° chamfer)
C2           (shorthand for 2 × 45°)
```

**Fillets and Radii:**
```
R5       (radius 5mm)
R5 TYP   (radius 5mm typical - applies to all similar features)
SR3      (spherical radius 3mm)
```

**Slots:**
```
Width × Length
Example: 8 × 50 SLOT
```

**Patterns:**
```
4× ⌀6.5      (4 places, diameter 6.5mm)
8× ⌀10 EVENLY SPACED ON ⌀100 BOLT CIRCLE
```

## Tolerances and Notes

### General Tolerance Notes

**Block tolerance note:**
```
UNLESS OTHERWISE SPECIFIED:
  - Decimal dimensions: ±0.1 mm
  - Angular dimensions: ±1°
  - Chamfers: 0.5 × 45°
  - Fillets: R2
  - Surface finish: 3.2 µm Ra
  - Break all sharp edges
```

**Benefits:**
- Reduces clutter (don't tolerance every dimension individually)
- Establishes shop capabilities
- Only critical features get specific callouts

### Specific Tolerance Callouts

**Critical dimensions:**
```
50.00 ±0.02   (tight tolerance for functional feature)
25 +0.05/0    (unilateral tolerance, hole clearance)
100 ±0.5      (loose tolerance, non-critical)
```

**GD&T callouts:**
```
Position: ⊕ ⌀0.1 (M) | A | B |
Flatness: ⬜ 0.05
Perpendicularity: ⊥ 0.08 | A |

(Refer to Section 16.5 for detailed GD&T)
```

### Material and Finish Notes

**Material specification:**
```
MATERIAL: ALUMINUM 6061-T6 PER ASTM B209
MATERIAL: STEEL 1018 CRS
MATERIAL: STAINLESS STEEL 304
MATERIAL: DELRIN (ACETAL COPOLYMER)
```

**Surface finish:**
```
[Triangle symbol] 3.2   (Surface finish 3.2 µm Ra)
[Triangle symbol] 1.6   (Finish 1.6 µm Ra on specific surface)
```

**Coating/finish:**
```
FINISH: ANODIZE TYPE II, CLEAR, MIL-A-8625
FINISH: POWDER COAT, RAL 9005 (BLACK)
FINISH: ZINC PLATE, CLEAR CHROMATE
FINISH: MACHINE FINISH, NO COATING
```

**Heat treatment:**
```
HEAT TREAT: HARDNESS 50-55 HRC AFTER QUENCH & TEMPER
HEAT TREAT: STRESS RELIEVE AT 550°F FOR 4 HOURS
```

### Manufacturing Notes

**Machining notes:**
```
DEBURR ALL EDGES
BREAK SHARP EDGES 0.2mm MAX
DO NOT MACHINE SURFACE [A] (as-cast, as-rolled, etc.)
ALL HOLES ±0.1 UNLESS NOTED
```

**Assembly notes (on assembly drawings):**
```
APPLY LOCTITE 243 TO THREADS BEFORE ASSEMBLY
TORQUE FASTENERS TO 10 N·m
GREASE BEARING WITH MOBILITH SHC 100
```

**Inspection notes:**
```
INSPECT PER FIRST ARTICLE INSPECTION (FAI)
CRITICAL DIMENSIONS MARKED WITH [★]
CMM INSPECTION REQUIRED
```

## Drawing Types

### Detail Drawing (Part Drawing)

**Purpose:** Fully defines single part for manufacturing

**Contents:**
- Multiple orthographic views
- Dimensions (all features)
- Tolerances (GD&T, +/-, general)
- Material specification
- Surface finish
- Notes (machining, finishing)
- Title block

**When to create:**
- Every custom-designed part
- Parts manufactured in-house
- Parts sent to vendors for fabrication

### Assembly Drawing

**Purpose:** Shows how parts fit together

**Contents:**
- Assembly views (orthographic, isometric, exploded)
- Item balloons (numbered references to BOM)
- Critical assembly dimensions (overall size, key interfaces)
- Assembly notes (torque specs, adhesives, orientations)
- Bill of Materials (BOM)

**What NOT to include:**
- Individual part dimensions (those go on detail drawings)
- Manufacturing details of parts

**Types of assembly drawings:**

**General assembly:**
```
Shows entire product assembled
Overall dimensions
Subassembly callouts
```

**Subassembly drawing:**
```
Specific subassembly detail
Parts list for subassembly only
Assembly sequence
```

**Exploded assembly:**
```
Parts separated along assembly axis
Clearly shows how parts fit together
Numbered balloons match BOM
Assembly instructions reference this
```

### Installation Drawing

**Purpose:** Guide end-user installation

**Contents:**
- Mounting dimensions
- Required clearances
- Utilities (power, air, coolant connections)
- Foundation requirements (floor mounting, vibration isolation)
- Safety zones (keep clear areas)

### Fabrication Drawing (for cutting processes)

**Purpose:** Guide 2D cutting operations (plasma, laser, waterjet, sheet metal)

**Contents:**
- Flat pattern (unfolded geometry)
- Bend lines and bend angles (sheet metal)
- Material thickness
- Edge finish requirements
- Nesting layout (multiple parts per sheet)

**Formats:**
- DXF export (2D geometry for CAM)
- PDF drawing (notes, material, finish)

## CAD-to-Drawing Workflow

### Creating Drawings from 3D Models

**Typical process:**

**1. Create drawing file from part/assembly:**
```
CAD systems:
  - SolidWorks: New Drawing from part
  - Fusion 360: Create Drawing
  - FreeCAD: TechDraw workbench
```

**2. Insert views:**
```
- Select front view orientation
- Auto-project top, side views
- Add section views where needed
- Add detail views for small features
```

**3. Adjust view scale:**
```
Simple parts: 1:1 (actual size)
Large parts: 1:2, 1:5, 1:10 (reduced)
Small parts: 2:1, 5:1 (enlarged for clarity)

Show scale in view title or general note
```

**4. Add dimensions:**
```
- Import model dimensions (smart dimensioning)
- Add manufacturing-relevant dimensions
- Remove redundant CAD dimensions
- Apply baseline/ordinate dimensioning for critical features
```

**5. Add GD&T callouts:**
```
- Define datums
- Add feature control frames
- Specify tolerances
```

**6. Add notes:**
```
- General notes (material, finish, tolerances)
- Specific notes (manufacturing instructions)
- Revision notes
```

**7. Populate title block:**
```
- Part number, name
- Material
- Scale
- Designer, date
- Revision level
```

**8. Review and export:**
```
- Check: All features dimensioned?
- Check: Tolerances appropriate?
- Check: Views clear and uncluttered?
- Export PDF for distribution
```

### Drawing Best Practices

**Clarity:**
- Avoid dimension crowding (use multiple views)
- Use appropriate scale (large enough to read, not wastefully large)
- Consistent line weights (thick for part outline, thin for dimensions)

**Completeness:**
- Every manufacturing feature dimensioned
- All tolerances specified (specific or general)
- Material and finish clearly stated

**Consistency:**
- Same dimensioning style throughout
- Consistent units (don't mix mm and inches)
- Consistent terminology in notes

**Simplicity:**
- Fewest views necessary
- Avoid unnecessary complexity
- Standard symbols and abbreviations

## Revision Control

### Revision Levels

**Revision naming:**
```
Prototype: Proto-1, Proto-2, ... (not released for production)
Released: RevA, RevB, RevC, ... (production versions)
  OR: Rev 1.0, Rev 1.1, Rev 2.0, ...
```

**Revision block on drawing:**
```
┌─────┬────────────────────┬──────┬──────┐
│ Rev │ Description        │ Date │ By   │
├─────┼────────────────────┼──────┼──────┤
│ A   │ Initial release    │ 3/15 │ JDoe │
│ B   │ Increased hole ⌀  │ 4/02 │ JDoe │
│ C   │ Added chamfers     │ 5/10 │ ASmith│
└─────┴────────────────────┴──────┴──────┘
```

### Engineering Change Orders (ECO)

**Formal change process:**
```
1. Identify need for change (field failure, design improvement, cost reduction)
2. Document change in ECO:
   - ECO number (unique ID)
   - Description of change
   - Reason for change
   - Parts affected
   - Effectivity (which serial numbers get change)
3. Approve ECO (engineering manager, QA, production)
4. Update drawings, CAD models
5. Increment revision level
6. Notify affected parties (manufacturing, purchasing, QA)
```

**Change annotation on drawing:**
```
Cloud/bubble around changed feature
Reference to ECO number in revision block
```

## Export Formats

### File Formats for Different Uses

**PDF (Portable Document Format):**
```
Use: Distribution to machinists, vendors, inspection
Advantages:
  - Universal (any device, no special software)
  - Non-editable (prevents unauthorized changes)
  - Searchable text (if created from CAD, not scanned)
  - Compact file size
```

**DWG/DXF (AutoCAD formats):**
```
Use: Sharing editable drawings, CAM import (2D)
Advantages:
  - Industry standard
  - Editable in AutoCAD, compatible CAD systems
  - 2D geometry for CAM (plasma, laser, waterjet)
Disadvantages:
  - Version compatibility issues
  - Can be altered
```

**STEP (ISO 10303):**
```
Use: 3D model exchange (CAD to CAD, CAD to CAM)
Advantages:
  - Neutral format (cross-platform)
  - Preserves 3D geometry, assemblies
  - Industry standard for 3D model exchange
```

**IGES (older 3D exchange format):**
```
Use: Legacy systems
Disadvantages:
  - Less reliable than STEP
  - Use STEP instead when possible
```

**STL (Stereolithography):**
```
Use: 3D printing, visualization
Advantages:
  - Universal for 3D printing
  - Simple mesh format
Disadvantages:
  - Faceted (not smooth curves)
  - No dimensional accuracy (mesh approximation)
  - Use for visualization and 3D printing only, NOT manufacturing drawings
```

## Summary

Engineering drawings translate CAD models into manufacturing instructions:

**Drawing Standards:**
- ASME Y14.5 (North America) or ISO 128/1101 (International)
- Third-angle or first-angle projection (be consistent)
- Standard sheet sizes (ANSI A-E or ISO A4-A0)

**View Selection:**
- Minimum views to fully define part
- Section views for internal features
- Detail views for small/complex features
- Auxiliary views for angled surfaces

**Dimensioning:**
- Dimension once per feature
- Baseline dimensioning (avoid tolerance stack-up)
- Datum-based (matches manufacturing setup)
- Clear, uncluttered placement

**Tolerances and Notes:**
- General tolerance block (default for non-critical dimensions)
- Specific tolerances for critical features
- GD&T for complex geometric requirements
- Material, finish, manufacturing notes

**Drawing Types:**
- Detail drawings (individual parts)
- Assembly drawings (BOM, balloons, assembly notes)
- Fabrication drawings (2D cutting, flat patterns)

**Revision Control:**
- ECO process for changes
- Revision history on drawing
- Change clouds/annotations

**Next section** covers preparing CAD models for CAM programming and the handoff to manufacturing.

***

**Next:** [Section 16.10: CAD-CAM Integration](section-16.10-cad-cam-integration.md)

**Previous:** [Section 16.8: Assembly Design](section-16.8-assembly-design.md)
