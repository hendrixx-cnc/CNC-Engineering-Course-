# Section 16.2: CAD Fundamentals

## Introduction

Think of CAD fundamentals as learning to write before writing novels. You can create complex parts without mastering basics, but they'll be fragile, hard to edit, and difficult for others to understand. This section teaches you the **professional foundations** that separate stable, maintainable CAD models from amateur "spaghetti models" that break when you change a single dimension.

**Why fundamentals matter:**
- **Bad sketch:** Change one dimension → entire model fails → spend 2 hours rebuilding
- **Good sketch:** Change any dimension → model updates cleanly in seconds
- **Impact:** The difference between 5-minute design changes and throwing away your model and starting over

These principles apply to **all CAD software** (FreeCAD, Fusion 360, SolidWorks, Inventor, Onshape). The buttons and menus differ, but the underlying concepts are universal.

## Sketching Best Practices

### The Foundation of Parametric Design

Every 3D feature begins with a 2D sketch. The quality of your sketches directly impacts model stability, editability, and manufacturability.

### Sketch Fully Defined vs. Under-Defined

Understanding constraint status is like the difference between a building on a solid foundation vs. quicksand.

**Fully Defined Sketch (Professional Standard):**
```
Visual indicator: All geometry BLACK (or fully constrained color)
Status: ✓ Fully Defined
What this means:
  - Every line, arc, point has exact position/size defined
  - Nothing can move unless you change a dimension/constraint
  - Editing is predictable (change one thing, others stay fixed)
  - Model won't break when you modify parent features
```

**Under-Defined Sketch (Amateur Warning Sign):**
```
Visual indicator: Geometry BLUE or GREEN (software dependent)
Status: ⚠ Under-Defined
What this means:
  - Some lines/points can move freely
  - Sketch can "shift" unexpectedly during edits
  - Parent feature changes may cause catastrophic shifts
  - Downstream features may fail unpredictably
```

**Real-world example:**

**Amateur approach:**
```
Draws rectangle, adds one dimension (50mm width)
- Rectangle height: undefined (blue)
- Position: undefined (blue)
- Later edits cause rectangle to shift position
- All features built on this sketch break
```

**Professional approach:**
```
Draws rectangle, fully constrains:
1. Width = 50mm (dimension)
2. Height = 30mm (dimension)
3. Bottom-left corner coincident with origin (constraint)
4. Bottom edge horizontal (constraint)

Result: All geometry BLACK, fully defined
Changes are predictable, model never breaks unexpectedly
```

**Rule:** If you see blue/green lines in your sketch, you're not done. Keep adding constraints/dimensions until everything is black (fully defined).

**Exception:** Sketches for design exploration where you deliberately want flexibility—but these should NEVER be used for final manufacturing models.

### Constraint Strategy

**The Golden Rule: Geometry First, Dimensions Second**

Think of constraints as answering two questions:
1. **What shape?** (Geometric constraints: parallel, perpendicular, tangent, etc.)
2. **What size?** (Dimensional constraints: 50mm, ⌀10mm, 45°, etc.)

**Why this order matters:**
- Geometric constraints are "free" (no specific values, just relationships)
- They reduce degrees of freedom quickly
- They make the sketch more robust (changing one dimension doesn't break relationships)
- Dimensions added last only control size, not relationships

**Step-by-Step Constraint Workflow:**

**Phase 1: Draw Rough Geometry**
```
Draw approximate shape (don't worry about exact sizes yet)
- Rectangle for plate
- Circles for holes
- Lines for edges
Everything will be blue/green (under-defined) - this is OK for now
```

**Phase 2: Apply Geometric Constraints (Define Relationships)**

1. **Horizontal/Vertical** - Align features to coordinate axes
   - Example: "Make bottom edge horizontal" → ensures part aligns with machine axes

2. **Coincident** - Connect endpoints, center points
   - Example: "Rectangle corner coincident with origin" → fixes position

3. **Concentric** - Align holes, shafts, arcs
   - Example: "4 holes concentric with construction circle" → bolt pattern

4. **Parallel/Perpendicular** - Define relationships between lines
   - Example: "Side edge perpendicular to bottom edge" → ensures square corners

5. **Tangent** - Smooth transitions between arcs and lines
   - Example: "Fillet tangent to both edges" → smooth blend

6. **Symmetric** - Mirror features about centerlines
   - Example: "Holes symmetric about vertical centerline" → balanced design

7. **Equal** - Make multiple features identical size
   - Example: "All 4 holes equal diameter" → consistency without specifying size yet

**Phase 3: Add Dimensions (Define Sizes)**

8. **Length/Distance** - Size linear features
   - Example: "Plate width = 100mm"

9. **Radius/Diameter** - Size circular features
   - Example: "Holes = ⌀6.6mm" (M6 clearance)

10. **Angles** - Define non-orthogonal relationships
    - Example: "Bracket angle = 45°"

**Real Example: Sketching a Mounting Plate**

```
Starting point: Empty sketch (everything blue/undefined)

Step 1: Draw rough rectangle, 4 circles inside
Status: All blue (under-defined)

Step 2: Geometric constraints
- Bottom edge → HORIZONTAL
- Left edge → VERTICAL
- Bottom-left corner → COINCIDENT with origin
- 4 holes → SYMMETRIC about both centerlines
- 4 holes → EQUAL diameter
Status: Some geometry now black (partially defined)

Step 3: Dimensions
- Rectangle width → 100mm
- Rectangle height → 80mm
- Hole diameter → 6.6mm
- Hole spacing → 75mm × 55mm
Status: ALL BLACK (fully defined)

Result: Robust sketch that won't break during edits
```

**Pro Tip: Use construction geometry**
```
Instead of dimensioning between holes directly:

❌ Bad: Dimension from hole center to hole center (creates dependency chain)

✓ Good: Create construction rectangle, make holes coincident with corners
  - Dimension the construction rectangle
  - Holes automatically update when rectangle changes
  - More robust, easier to modify
```

### Sketch Origin and Axes

**Always reference the sketch origin strategically:**

```
Manufacturing-Friendly Origin Placement:
┌─────────────────────────────┐
│                             │
│    Part symmetry line → ─┬─ │
│                          │  │
│                          │  │
│    Machining datum    → ─┼─ │ ← Origin at intersection
│    (hole center, edge)   │  │    of critical features
│                          │  │
└─────────────────────────────┘
```

**Good origin choices:**
- Part centerline (for symmetric parts)
- Machining datum (primary locating feature)
- Critical mounting hole center
- Corner of stock material (for nesting efficiency)

**Poor origin choices:**
- Random location in middle of sketch
- Corner of part that will be cut off
- Feature that may be removed in design iterations

### Sketch Hygiene

**Do:**
- Use construction lines for reference geometry (shown as dashed lines)
- Break complex shapes into multiple simple features
- Name sketches descriptively ("mounting_plate_profile", "bolt_pattern")
- Keep one sketch per feature when possible
- Use sketch patterns for repeated features

**Don't:**
- Create unnecessarily complex splines when simple arcs will do
- Over-constrain (adding redundant dimensions)
- Leave dangling sketch geometry
- Mix critical and cosmetic features in same sketch
- Create self-intersecting profiles

## Feature-Based Modeling

### Building Blocks of 3D Parts

Think of features as LEGO blocks for CAD—each one adds or removes material in a specific way. Professional CAD models are built from a logical sequence of features, not random geometry.

**Why feature order matters:**
Your CAD software builds the part step-by-step, like following a recipe. Change an early step, and everything after it updates (or breaks if poorly designed). Understanding features helps you create models that are:
- **Editable:** Change dimensions without breaking the model
- **Logical:** Other people can understand your design intent
- **Manufacturable:** Features map directly to machining operations

### Additive Features

**Extrude**
- Most common feature
- Converts 2D sketch into 3D by extending perpendicular to sketch plane
- Manufacturing consideration: Extrude depth = machining depth (longer = more cycle time)

```
Sketch Profile → [Extrude 25mm] → 3D Boss
     □                                ▄▄▄
                                     ████
```

**Revolve**
- Creates axially symmetric parts
- Perfect for turned components
- Manufacturing consideration: Design for lathe or mill-turn operations

```
Sketch Profile → [Revolve 360°] → Turned Part
     ▐▌                              ●●●
                                    ●   ●
                                     ●●●
```

**Loft**
- Blends between multiple profiles
- Good for streamlined shapes
- Manufacturing consideration: Complex lofts may require multi-axis machining

**Sweep**
- Follows a profile along a path
- Useful for tubes, pipes, complex channels
- Manufacturing consideration: Ensure sweep path is accessible to tooling

### Subtractive Features

**Cut Extrude**
- Removes material
- Represents milling, drilling, boring operations
- Manufacturing consideration: Depth-to-diameter ratio matters (deep pockets are slow/risky)

**Revolve Cut**
- Removes material axially
- Represents turning, grooving, boring
- Manufacturing consideration: Ensure tool can reach without interference

**Hole Feature**
- Specialized feature for drilled/tapped holes
- Includes standard sizes (ANSI, ISO)
- Manufacturing consideration: Use standard drill sizes, tap sizes

**Chamfer**
- Beveled edge (45° typical)
- Removes sharp edges
- Manufacturing consideration: Easier to program than fillets, quick to execute

**Fillet**
- Rounded edge
- Strengthens parts, improves appearance
- Manufacturing consideration: Radius must match available tool sizes

### Pattern Features

**Linear Pattern**
- Repeats features in straight lines
- Perfect for bolt patterns, ventilation holes
- Manufacturing consideration: Aligns with axis of motion = faster machining

**Circular Pattern**
- Repeats features around an axis
- Good for bolt circles, gear teeth
- Manufacturing consideration: May require rotary axis or indexing

**Mirror**
- Reflects features across plane
- Ensures perfect symmetry
- Manufacturing consideration: Consider if part can be flipped in fixture

### Feature Order and Parent-Child Relationships

Features build upon each other, creating a dependency tree:

```
Base Extrude (Sketch1)
  ├─ Fillet1
  ├─ Hole1 (Sketch2)
  │   └─ Hole Pattern1
  └─ Cut Extrude (Sketch3)
      └─ Chamfer1
```

**Critical Principle:** Child features depend on parent features. If you delete or modify a parent, children may fail.

**Best Practices:**
- Place critical features early in the tree
- Place cosmetic features (small fillets, chamfers) late
- Group related features together
- Avoid creating complex interdependencies

### Feature Editing and Suppression

**Edit Feature:** Double-click to change parameters
**Suppress Feature:** Temporarily remove without deleting (useful for analyzing base geometry)
**Rollback Bar:** Move backwards in feature tree to edit earlier features

## File Organization and Naming Conventions

### Project Structure

Organize CAD files for team collaboration and long-term maintenance:

```
Project_Name/
├── CAD/
│   ├── Parts/
│   │   ├── Structural/
│   │   ├── Brackets/
│   │   ├── Hardware/
│   │   └── Custom/
│   ├── Assemblies/
│   │   ├── Subassemblies/
│   │   └── Final_Assembly/
│   ├── Drawings/
│   │   ├── Parts/
│   │   └── Assemblies/
│   └── Templates/
├── CAM/
│   ├── Toolpaths/
│   ├── Setup_Sheets/
│   └── Post_Processed/
├── Documentation/
│   ├── BOM/
│   ├── Specifications/
│   └── Change_Orders/
└── Archive/
    └── Previous_Versions/
```

### Naming Conventions

**Part Files:**
```
[Project]-[Assembly]-[Part]-[Revision].[ext]

Examples:
CNC_Table-Frame-Left_Rail-RevB.sldprt
Plasma_Cutter-Torch_Assy-Nozzle_Cap-RevA.step
Robot_Arm-Gripper-Jaw_Left-RevC.FCStd
```

**Assembly Files:**
```
[Project]-[Assembly_Name]-[Revision].[ext]

Examples:
CNC_Table-Frame_Assembly-RevA.sldasm
Waterjet-Cutting_Head_Assy-RevB.step
```

**Drawing Files:**
```
[Project]-[Part/Assy]-Drawing-[Revision].[ext]

Examples:
CNC_Table-Left_Rail-Drawing-RevB.pdf
Plasma_Cutter-Torch_Assy-Drawing-RevA.dwg
```

### Version Control Strategies

**Revision Levels:**
- **RevA:** Initial release for manufacturing
- **RevB, C, D...:** Sequential changes (document changes in ECO)
- **Proto1, Proto2...:** Prototype iterations (not for production)
- **Dev:** Development/experimental (not released)

**Change Documentation:**
Maintain a change log in each file or external ECO (Engineering Change Order):
```
RevA: Initial release
RevB: Increased hole diameter from 8mm to 10mm per ECO-2024-015
RevC: Added lightening pockets per weight reduction study
```

**File Format Selection:**

| Format | Use Case | Editability | Compatibility |
|--------|----------|-------------|---------------|
| .sldprt, .ipt, .FCStd | Native working files | Full | Software-specific |
| .step, .stp | Neutral 3D exchange | None | Universal |
| .iges, .igs | Legacy 3D exchange | None | Universal (older) |
| .dxf | 2D profiles (plasma/laser/waterjet) | Limited | Universal |
| .dwg | Engineering drawings | Full (AutoCAD) | Near-universal |
| .pdf | Drawing distribution | None | Universal |
| .stl | 3D printing, visualization | None | Universal (mesh only) |

**Best Practice:** Maintain native files for editing, export neutral formats (STEP) for sharing with other CAD systems or CAM software.

## Multi-Body Part Design

### When to Use Multi-Body Modeling

Multi-body parts contain multiple solid bodies within a single part file.

**Good Use Cases:**
1. **Weldments:** Design all components in context, then split for fabrication
2. **Cast/Molded Parts:** Model core and cavity in same file
3. **Assembly-Level Features:** Create cuts or holes that affect multiple parts
4. **Process Planning:** Separate features by manufacturing operation

**Example - Welded Frame:**
```
Single Part File: Frame_Weldment.sldprt
  Body1: Base_Plate
  Body2: Vertical_Post_Left
  Body3: Vertical_Post_Right
  Body4: Top_Rail
  [Assembly feature: weld beads modeled as features]
```

**Advantages:**
- All components stay in perfect alignment
- Shared features (holes through multiple parts) maintain consistency
- Can derive individual part files from bodies
- Faster than assembly for simple structures

**Disadvantages:**
- Can become slow with many bodies
- BOM generation more complex
- Some CAM software prefers separate files

### Deriving Parts from Multi-Body

Most CAD systems allow "Save Bodies" or "Derive Part" to extract individual bodies as separate files:

```
Frame_Weldment.sldprt
  ├─ [Save Body] → Base_Plate.sldprt
  ├─ [Save Body] → Vertical_Post_Left.sldprt
  ├─ [Save Body] → Vertical_Post_Right.sldprt
  └─ [Save Body] → Top_Rail.sldprt
```

Derived parts can then be detailed with drawings, programmed in CAM, and manufactured independently while maintaining design intent from master weldment.

## Part vs. Assembly Modeling

### When to Create a Part

**Single-piece parts:**
- Machined from one piece of stock
- Cast or molded as single item
- Sheet metal part (even if bent—single flat pattern)
- 3D printed object (even if complex)

### When to Create an Assembly

**Multiple components that:**
- Are manufactured separately
- Use different materials
- Can move relative to each other
- Need independent documentation
- Are purchased items (fasteners, bearings, motors)

**Subassemblies:**
Group related parts into subassemblies for:
- Logical organization (motor_mount_assy, control_panel_assy)
- Independent testing/qualification
- Outsourced fabrication (vendor builds subassembly)
- Pattern/reuse (multiple identical subassemblies)

## Design Libraries and Standardization

### Creating Reusable Content

**Part Templates:**
- Start new designs with pre-configured units, material, views
- Include company logo, revision blocks
- Set default tolerance standards

**Feature Libraries:**
- Save commonly used features (bolt patterns, mounting brackets, lightening pockets)
- Insert into new designs with drag-and-drop

**Standard Parts Library:**
- Hardware (screws, nuts, washers, pins)
- Commercial components (bearings, motors, linear guides)
- Company-standard brackets, spacers, fixtures

**Naming Standards:**
```
ISO4762_M8x25_Socket_Head_Cap_Screw.step
SKF_6204_Deep_Groove_Ball_Bearing.step
McMaster_92196A111_Washer.step
```

### Benefits of Standardization

1. **Design Speed:** Don't re-model common parts
2. **Manufacturing Efficiency:** Standard parts = bulk purchasing, interchangeability
3. **Reduced Errors:** Proven designs, correct dimensions
4. **Simplified BOM:** Standard part numbers, vendor codes
5. **Training:** New designers learn consistent methods

## Practical Exercise: Design a Mounting Bracket

### Objective
Create a simple L-bracket demonstrating fundamental CAD techniques.

**Requirements:**
- 100mm x 80mm x 3mm plate (vertical)
- 100mm x 60mm x 3mm plate (horizontal)
- Four M6 mounting holes in vertical plate (80mm x 50mm bolt pattern)
- Two M8 mounting holes in horizontal plate (50mm spacing)
- All holes 10mm from edges
- 5mm fillet at inside corner
- 2mm chamfer on all outer edges

### Step-by-Step Process

**1. Create Vertical Plate Sketch (Front Plane)**
- Rectangle: 100mm x 80mm, centered on origin
- Fully constrain with dimensions
- Name sketch: "vertical_plate_profile"

**2. Extrude Vertical Plate**
- Extrude: 3mm thickness
- Direction: towards you (positive)
- Name feature: "vertical_plate"

**3. Create Horizontal Plate Sketch (Top face of vertical plate)**
- Rectangle: 100mm x 60mm
- Constrain bottom edge coincident with top of vertical plate
- Name sketch: "horizontal_plate_profile"

**4. Extrude Horizontal Plate**
- Extrude: 3mm thickness
- Direction: perpendicular to vertical plate
- Merge result with vertical plate body
- Name feature: "horizontal_plate"

**5. Add Inside Fillet**
- Select inside corner edge
- Fillet radius: 5mm
- Name feature: "corner_fillet"

**6. Create M6 Hole Pattern Sketch (On vertical plate face)**
- Rectangle construction lines: 80mm x 50mm, centered
- Four circles at rectangle corners, diameter 6.6mm (M6 clearance)
- Fully constrain
- Name sketch: "m6_bolt_pattern"

**7. Cut Extrude M6 Holes**
- Through all
- Name feature: "m6_mounting_holes"

**8. Create M8 Hole Pattern Sketch (On horizontal plate face)**
- Two circles, 50mm spacing, centered on plate
- Diameter: 8.8mm (M8 clearance)
- Position 10mm from front edge
- Name sketch: "m8_bolt_pattern"

**9. Cut Extrude M8 Holes**
- Through all
- Name feature: "m8_mounting_holes"

**10. Chamfer All Outer Edges**
- Select all outer edges (avoid inside fillet)
- Chamfer: 2mm x 45°
- Name feature: "edge_chamfers"

**11. Assign Material**
- Material: Aluminum 6061-T6 (or Mild Steel)

**12. Save File**
- Filename: Bracket-L_Shape-100x80-RevA.[ext]

### Verification Checklist

- [ ] All sketches fully constrained (no blue lines)
- [ ] All features named descriptively
- [ ] Feature tree organized logically
- [ ] Material assigned
- [ ] File saved with proper naming convention
- [ ] Can edit any dimension and model updates without errors

## Summary

This section covered the foundational skills for robust CAD modeling:

1. **Sketching:** Fully constrained sketches with strategic origin placement
2. **Features:** Proper use of extrudes, cuts, holes, fillets, chamfers, patterns
3. **Organization:** File structures, naming conventions, version control
4. **Multi-body:** When and how to use multiple bodies in single part
5. **Libraries:** Standardization for efficiency and consistency

Master these fundamentals before moving to advanced parametric techniques in the next section.

***

**Next:** [Section 16.3: Parametric Modeling](section-16.3-parametric-modeling.md)

**Previous:** [Section 16.1: Introduction](section-16.1-introduction.md)
