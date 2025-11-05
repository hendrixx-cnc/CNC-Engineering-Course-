# Section 16.3: Parametric Modeling

## Introduction

**Parametric modeling is like writing a smart program for your part instead of just drawing it.**

Imagine two designers both create a 100mm × 50mm bracket with 4 mounting holes:

**Designer A (Static Model):**
- Hard-codes every dimension
- Change bracket size → manually move every hole, edge, fillet
- Takes 30 minutes to resize
- High chance of errors (forgetting to update something)

**Designer B (Parametric Model):**
- Defines: `bracket_width = 100mm`, holes automatically positioned relative to edges
- Change `bracket_width = 120mm` → entire model updates instantly
- Takes 5 seconds to resize
- Zero errors (relationships enforce design intent)

**This isn't just about speed—it's about:**
- **Design exploration:** Try 10 sizes in 1 minute instead of 5 hours
- **Part families:** One model = many sizes (small/medium/large brackets)
- **Optimization:** Rapidly iterate based on analysis/testing
- **Manufacturing flexibility:** Adjust to available stock sizes instantly

**The secret:** You're not drawing geometry—you're encoding **design logic** that generates geometry.

## Understanding Design Intent

### What is Design Intent?

Design intent is the underlying logic that defines **why** your part is shaped the way it is, not just **what** it looks like.

**Example: Mounting Bracket**

**Poor Design (No Intent):**
```
- Hole1: diameter = 8mm, center at X=25, Y=25
- Hole2: diameter = 8mm, center at X=75, Y=25
```
If you change the bracket width from 100mm to 120mm, the holes stay at X=25 and X=75—no longer properly positioned.

**Good Design (With Intent):**
```
- Hole1: diameter = bolt_size, center at distance = edge_margin from left edge
- Hole2: diameter = bolt_size, center at distance = edge_margin from right edge
- Constraint: holes remain concentric with Y-axis centerline
```
Now changing bracket width automatically repositions holes correctly because the design intent (holes near edges, centered vertically) is encoded.

### Capturing Design Intent

**Ask yourself:**
- What dimensions are fixed (driven by standards, purchased parts)?
- What dimensions are variable (adapt to design changes)?
- What relationships must be maintained (symmetry, alignment, clearances)?
- What features drive other features (primary locating features)?

## Parameters and Variables

**Think of parameters as the "control panel" for your part.**

Instead of hunting through sketches to change a dimension, you adjust one value and the entire model updates.

### Global Parameters

Global parameters (also called "equations" or "variables") define values that can be used throughout your model.

**Real-World Scenario:**

You're designing a custom enclosure. Client says "make it bigger" after you've finished.

**Without Parameters (Pain):**
- Open 8 different sketches
- Change 24 individual dimensions
- Hope you didn't miss any
- Time: 20 minutes
- Risk: High (easy to miss something)

**With Parameters (Easy):**
- Change `enclosure_length = 300 mm` to `enclosure_length = 350 mm`
- Model regenerates automatically
- Time: 10 seconds
- Risk: Zero (relationships enforce consistency)

**Syntax varies by CAD system:**
```
FreeCAD:        bracket_width = 100 mm
SolidWorks:     "bracket_width" = 100
Fusion 360:     bracket_width = 100 mm
Inventor:       bracket_width = 100 mm
```

### Common Parameter Types

**1. Dimensional Parameters (The Foundation)**

These are your basic measurements—the "source of truth" for sizes.

```
plate_length = 200 mm
plate_width = 100 mm
plate_thickness = 3 mm
hole_diameter = 8 mm
edge_margin = 10 mm
```

**When to Use:**
- Primary dimensions that might change
- Values controlled by standards (bolt sizes, stock material)
- Customer-specified dimensions

**2. Derived Parameters (The Smart Ones)**

These calculate automatically based on other parameters.

```
hole_spacing = plate_length - (2 * edge_margin)
plate_area = plate_length * plate_width
bolt_clearance = hole_diameter + 0.5 mm
```

**Real Example - Mounting Plate:**
```
plate_length = 200 mm            ← You control this
edge_margin = 10 mm              ← You control this
hole_spacing = plate_length - (2 * edge_margin)    ← Calculates automatically = 180mm

Change plate_length to 250mm → hole_spacing becomes 230mm (no manual calculation!)
```

**3. Conditional Parameters (The Decision Makers)**

These parameters make decisions based on logic.

```
fillet_radius = if(plate_thickness < 5 mm, 2 mm, 5 mm)
min_wall_thickness = max(3 mm, plate_thickness * 2)
```

**Real Example - Material-Dependent Thread Depth:**
```
# Tapped holes need different depths in different materials
thread_depth = if(material == "Aluminum",
                  bolt_diameter * 1.5,     ← Aluminum: 1.5× diameter
                  bolt_diameter * 1.0)     ← Steel: 1.0× diameter

M8 bolt in aluminum → 12mm thread depth
M8 bolt in steel → 8mm thread depth
(Model automatically adjusts when you change material parameter!)
```

**4. Material-Based Parameters (The Physical Properties)**

```
density_steel = 7850 kg/m³
weight = volume * density_steel
```

**Real Example - Weight Calculation:**
```
# Automatic weight calculation for cost estimation
material = "Aluminum_6061"
density = 2700 kg/m³              ← Aluminum density
volume = (calculated by CAD)      ← CAD automatically computes volume

weight_kg = (volume / 1000000) * (density / 1000)
weight_lbs = weight_kg * 2.205

material_cost_per_kg = 8.50
estimated_material_cost = weight_kg * material_cost_per_kg
```

Change material to steel → density becomes 7850 kg/m³ → weight and cost recalculate instantly!

### Parameter Organization

**Poor Organization (Chaos):**
```
d1 = 200
w = 100
t = 3
h = 8
m = 10
```
**Problem:** What does "d1" mean? What's "m"? Impossible to maintain.

***

**Good Organization (Clear & Maintainable):**
```
# ============================================
# PLATE DIMENSIONS
# ============================================
plate_length = 200 mm
plate_width = 100 mm
plate_thickness = 3 mm

# ============================================
# HOLE PATTERN
# ============================================
hole_diameter = 8 mm          # M8 clearance
hole_count = 4
hole_spacing_x = 150 mm
hole_spacing_y = 75 mm
edge_margin = 10 mm           # Minimum distance from edge

# ============================================
# MANUFACTURING FEATURES
# ============================================
fillet_radius = 5 mm          # Internal corners
chamfer_size = 2 mm           # External edges (deburring)
min_wall_thickness = 3 mm     # Structural minimum

# ============================================
# DERIVED CALCULATIONS (Auto-Update)
# ============================================
actual_hole_spacing_x = plate_length - (2 * edge_margin)
actual_hole_spacing_y = plate_width - (2 * edge_margin)
plate_weight_kg = (plate_length * plate_width * plate_thickness / 1000000) * (density / 1000)
```

**Benefits:**
- ✓ Anyone can understand at a glance
- ✓ Easy to find what you need to change
- ✓ Comments explain context
- ✓ Grouped logically

### Naming Best Practices

| ❌ Bad Name | ✓ Good Name | Why Good is Better |
|------------|-------------|-------------------|
| `dia1` | `mounting_hole_clearance_M8` | Describes purpose, size, and bolt type |
| `L` | `base_plate_length` | Clear which length (base vs cover vs bracket) |
| `offset` | `hole_edge_margin` | Specifies what's being offset |
| `r` | `corner_fillet_radius` | Indicates location and feature type |
| `x` | `motor_bolt_spacing_horizontal` | Describes purpose and direction |

**Pro Tip:** Use names that will make sense to you 6 months from now (or to a coworker who has to edit your model).

## Linking Dimensions to Parameters

**This is where the magic happens—connecting your sketches to the parameter "control panel."**

### Direct Parameter References

Instead of entering numeric values in sketches, reference parameters:

**Before (Hard-Coded):**
```
Rectangle: 200 x 100
```
**Problem:** Change size → must manually edit sketch, find dimension, change value, repeat for every sketch that uses this size.

***

**After (Parametric):**
```
Rectangle: plate_length x plate_width
```
**Benefit:** Change size → change ONE parameter (`plate_length`), ALL sketches using it update automatically!

**Step-by-Step: Converting Hard-Coded to Parametric**

**Scenario:** You've drawn a mounting plate with hard-coded 200mm × 100mm rectangle.

**Step 1: Define Parameter**
```
Open Parameters/Equations panel
Add: plate_length = 200 mm
Add: plate_width = 100 mm
```

**Step 2: Link Sketch Dimension**
```
Double-click the "200" dimension in sketch
Delete "200"
Type: plate_length
Press Enter
```

Dimension now shows "plate_length" instead of "200mm"—it's LINKED!

**Step 3: Test It**
```
Change parameter: plate_length = 250 mm
Watch sketch update automatically to 250mm
```

**Before vs After:**

| Task | Hard-Coded | Parametric |
|------|-----------|-----------|
| Initial setup | 2 minutes | 5 minutes (define parameters) |
| First size change | 10 minutes (edit 6 sketches) | 10 seconds (change 1 parameter) |
| Second size change | 10 minutes | 10 seconds |
| Third size change | 10 minutes | 10 seconds |
| **Total time after 3 changes** | **32 minutes** | **5 min 30 sec** |

**Parametric pays for itself FAST.**

### Equations in Dimensions

Most CAD systems allow equations directly in dimension fields—you don't even need to create a named parameter!

**Real Examples:**

```
Extrude depth: plate_thickness * 2
  ↳ Boss height is always double the plate thickness

Hole position: plate_length / 2
  ↳ Hole stays centered even when plate length changes

Pattern spacing: (plate_length - 2 * edge_margin) / (hole_count - 1)
  ↳ Holes evenly distributed between margins, regardless of plate size
```

**Practical Example - Motor Mount Hole Pattern:**

```
# Parameters defined:
plate_length = 200 mm
edge_margin = 15 mm
hole_count = 4

# In sketch, dimension hole #2 position from hole #1:
Horizontal distance = (plate_length - 2 * edge_margin) / (hole_count - 1)
                    = (200 - 30) / 3
                    = 56.67 mm

# Change plate to 300mm:
New spacing = (300 - 30) / 3 = 90 mm
(All 4 holes redistribute automatically!)
```

**Pro Tip:** Use equations for **derived** values, named parameters for **primary** values you change often.

### Master Sketch Technique

**This is the "foundation blueprint" approach—one sketch controls everything.**

A master sketch contains critical parameters and reference geometry that drives multiple features.

**Why Use Master Sketches?**
- **Single source of truth** for complex geometry (bolt patterns, mounting interfaces)
- **Change once, update everywhere**
- **Prevents dimension drift** (when multiple features slowly get out of sync)

**Example: Bolt Pattern Master Sketch**

**Scenario:** Designing adapter plate for a motor with 4-hole mounting pattern.

**Master_Sketch (on reference plane):**
```
Construction rectangle: mounting_width x mounting_height
  ↳ Represents motor flange outline

Four construction points at rectangle corners
  ↳ Exact bolt hole locations

Construction circle: bolt_circle_diameter
  ↳ Reference for circular bolt pattern (if needed)

Reference dimensions ALL parametric:
  - mounting_width = 80 mm
  - mounting_height = 80 mm
  - bolt_circle_diameter = 113 mm
```

**Features driven by master sketch:**
```
Feature 1: Hole Pattern
  - Projects from 4 construction points in master sketch
  - Diameter = mounting_hole_clearance

Feature 2: Mounting Boss
  - Extrudes around bolt_circle from master sketch
  - Adds material for structural support

Feature 3: Clearance Pocket
  - Offsets from construction rectangle in master sketch
  - Creates recess for motor flange

Feature 4: Alignment Pin Holes
  - References midpoints of construction rectangle sides
```

**The Payoff:**

Motor manufacturer updates bolt pattern from 80mm × 80mm to 90mm × 90mm:

**Without Master Sketch:**
- Edit 4 hole positions individually
- Adjust boss diameter manually
- Recalculate clearance pocket
- Reposition alignment pins
- Time: 30+ minutes
- Risk: Holes misaligned, parts don't fit

**With Master Sketch:**
- Change: `mounting_width = 90 mm`, `mounting_height = 90 mm`
- ALL features update in perfect alignment
- Time: 10 seconds
- Risk: Zero

**Master Sketch Best Practice:**

✓ **Use construction geometry** (doesn't create physical features, just references)
✓ **Keep it simple** (only critical layout geometry)
✓ **Fully constrain** (black sketch—no uncertainty)
✓ **Name clearly** ("Motor_Interface_Master" not "Sketch017")

❌ **Don't overload** with unrelated geometry
❌ **Don't use for non-critical features** (cosmetic details don't need master sketch)

## Design Tables and Configurations

### Creating Part Families

Design tables (also called "configurations" or "family tables") allow one model to represent multiple size variations.

**Example: Standard Bracket Sizes**

| Configuration | plate_length | plate_width | plate_thickness | hole_diameter |
|---------------|--------------|-------------|-----------------|---------------|
| Small         | 100 mm       | 80 mm       | 3 mm            | 6 mm          |
| Medium        | 150 mm       | 120 mm      | 5 mm            | 8 mm          |
| Large         | 200 mm       | 160 mm      | 6 mm            | 10 mm         |
| XLarge        | 250 mm       | 200 mm      | 8 mm            | 12 mm         |

**Single CAD file contains all four variants**—select configuration when inserting into assembly or generating drawings.

### Configuration-Specific Features

Suppress or enable features based on configuration:

```
Configuration: Light_Duty
  - Lightening_Pockets: SUPPRESSED
  - Reinforcement_Ribs: SUPPRESSED

Configuration: Heavy_Duty
  - Lightening_Pockets: SUPPRESSED
  - Reinforcement_Ribs: ACTIVE

Configuration: Weight_Optimized
  - Lightening_Pockets: ACTIVE
  - Reinforcement_Ribs: SUPPRESSED
```

### Bill of Materials Impact

Configurations affect BOM generation:
- Each configuration can have unique part number
- Shared configurations reduce inventory (one drawing, multiple sizes)
- CAM programs can reference specific configuration

## Relationships and Constraints

### Geometric Relationships

**Symmetry:**
```
Feature1 and Feature2: Symmetric about vertical centerline
```
Ensures balanced design, simplifies machining (can use part centerline as datum).

**Concentric:**
```
Hole_Center and Boss_Center: Concentric
```
Maintains alignment through design changes.

**Tangent:**
```
Fillet and Adjacent_Surfaces: Tangent
```
Ensures smooth transitions, critical for flow paths, stress distribution.

**Parallel/Perpendicular:**
```
Mounting_Face and Reference_Datum: Perpendicular
```
Captures manufacturing setup requirements.

### Algebraic Relationships

**Ratios:**
```
hole_diameter = shaft_diameter * 1.05    # 5% clearance
wall_thickness = hole_diameter * 1.5      # Strength requirement
```

**Summations:**
```
total_length = section1_length + section2_length + section3_length
```

**Conditionals:**
```
thread_depth = if(material == "Aluminum", nominal_diameter * 1.5, nominal_diameter * 1.0)
```

### Inter-Part Relationships (Top-Down Design)

In assemblies, parts can reference each other:

```
Assembly: Motor_Mount
  Part: Base_Plate
    mounting_hole_spacing = Motor.bolt_pattern_spacing
    base_width = Motor.flange_width + 2 * clearance

  Part: Cover_Plate
    cover_width = Base_Plate.base_width    # Matches base plate
    cover_length = Base_Plate.base_length
```

**Caution:** Excessive inter-part references can make assemblies fragile. Use sparingly for truly dependent features.

## Advanced Parametric Techniques

### Suppression Equations

Automatically suppress/unsupppress features based on parameters:

```
Suppression equation for Lightening_Pockets:
  plate_thickness > 5 mm AND weight_optimization == TRUE
```

Feature appears only when both conditions met.

### Derived Patterns

Pattern count or spacing driven by overall dimensions:

```
Rib_Count = floor(plate_length / rib_spacing)
```

As plate gets longer, rib count automatically increases to maintain spacing.

### Linked External Files

Reference external parameter files (Excel, CSV, text):

**parameters.csv:**
```
parameter,value,unit
plate_length,200,mm
plate_width,100,mm
bolt_size,M8,
```

CAD model imports parameters from file. Entire product line updates when file changes.

**Use case:** Customer-specific variants, automated design generation.

### Parametric Curves and Splines

Define curves mathematically:

```
Spiral cam profile:
  radius(θ) = base_radius + (pitch * θ / 360°)
  x = radius * cos(θ)
  y = radius * sin(θ)
```

**Applications:** Cam profiles, turbine blades, custom spring geometry.

## Practical Parametric Design: Configurable Motor Mount

### Design Requirements

Create a parametric motor mount that adapts to different NEMA stepper motor sizes:
- NEMA 17: 42mm body, M3 mounting holes, 31mm bolt spacing
- NEMA 23: 56mm body, M5 mounting holes, 47.14mm bolt spacing
- NEMA 34: 86mm body, M6 mounting holes, 69.6mm bolt spacing

Additional requirements:
- Base plate extends 15mm beyond motor body on all sides
- Mounting holes for base plate: 10mm from corners
- Central shaft clearance hole: motor shaft diameter + 2mm
- Plate thickness: 6mm for NEMA 17/23, 8mm for NEMA 34

### Parameter Definition

```
# Motor Parameters (Configuration-Specific)
motor_body_size = 42 mm           # NEMA 17
motor_bolt_spacing = 31 mm
motor_mounting_hole = 3.3 mm      # M3 clearance
motor_shaft_diameter = 5 mm

# Derived Parameters
base_plate_size = motor_body_size + 2 * 15 mm
base_hole_edge_distance = 10 mm
shaft_clearance_diameter = motor_shaft_diameter + 2 mm

# Conditional Parameter
plate_thickness = if(motor_body_size > 60 mm, 8 mm, 6 mm)
```

### Modeling Steps

**1. Create Configuration Table**

| Config   | motor_body_size | motor_bolt_spacing | motor_mounting_hole | motor_shaft_diameter |
|----------|-----------------|--------------------|--------------------|----------------------|
| NEMA_17  | 42              | 31                 | 3.3                | 5                    |
| NEMA_23  | 56              | 47.14              | 5.3                | 6.35                 |
| NEMA_34  | 86              | 69.6               | 6.6                | 14                   |

**2. Base Plate Sketch**
```
Square: base_plate_size x base_plate_size
Centered on origin
```

**3. Extrude Base Plate**
```
Depth: plate_thickness
```

**4. Motor Mounting Hole Pattern Sketch**
```
Construction square: motor_bolt_spacing x motor_bolt_spacing
Centered on origin
Four circles at square corners
Diameter: motor_mounting_hole
```

**5. Central Shaft Clearance**
```
Circle: diameter = shaft_clearance_diameter
Centered on origin
```

**6. Base Mounting Holes**
```
Construction square:
  (base_plate_size - 2 * base_hole_edge_distance) x
  (base_plate_size - 2 * base_hole_edge_distance)
Four circles at corners
Diameter: 6.6 mm (M6 clearance for base mounting)
```

**7. Cut Holes**
```
Through all
```

**8. Chamfer Edges**
```
All outer edges: 2mm x 45°
```

### Testing Configurations

Switch between NEMA_17, NEMA_23, NEMA_34 configurations:
- All holes reposition correctly
- Base plate resizes appropriately
- Thickness changes for NEMA_34
- All clearances maintained

### Manufacturing Benefits

- **One CAD file** = Three product variants
- **One drawing** (with configuration table) = Simplified documentation
- **CAM program** can reference configurations = Automated toolpath generation
- **Design changes** propagate to all sizes = Reduced engineering time

## Design for Change: Building Robust Parametric Models

### Anticipating Modifications

**Ask during initial design:**
- Which dimensions might change based on customer requirements?
- What features might be added or removed later?
- How might manufacturing process change affect design?

**Build flexibility early:**
```
# Instead of hard-coding:
hole_depth = 20 mm

# Use ratio that adapts:
hole_depth = plate_thickness * 3
```

### Preventing Over-Constraint

**Symptoms of over-constraint:**
- Cannot change dimensions without errors
- Features constantly failing
- Sketch becomes over-defined

**Solutions:**
- Use construction geometry for reference, not multiple dimensions
- Let parameters drive multiple features instead of independent dimensions
- Leverage symmetry constraints instead of individual dimensions

### Parent-Child Management

**Minimize dependencies:**
- Critical features first (locating features, primary datums)
- Independent features when possible
- Group related features
- Cosmetic features last (fillets, chamfers)

**Reorder features** if child features fail when editing parent.

## Parametric Modeling for Different Manufacturing Processes

### Sheet Metal (Plasma/Laser/Waterjet)

**Key Parameters:**
```
material_thickness = 3 mm
kerf_width = 0.5 mm              # Process-dependent
min_feature_size = kerf_width * 3
bend_radius = material_thickness * 1.5    # For bending operations
hole_to_edge = material_thickness * 2     # Minimum distance
```

**Flat pattern parameters:**
```
bend_allowance = (π/2) * (bend_radius + k_factor * material_thickness)
developed_length = flat1_length + flat2_length + bend_allowance
```

### Milling

**Key Parameters:**
```
smallest_tool_diameter = 3 mm
min_internal_radius = smallest_tool_diameter / 2
pocket_depth_max = smallest_tool_diameter * 3    # Depth-to-diameter ratio
wall_thickness_min = material_thickness / 3
```

**Feature constraints:**
```
fillet_radius >= min_internal_radius
pocket_depth <= pocket_depth_max
```

### Turning

**Key Parameters:**
```
bar_stock_diameter = 25 mm
max_part_diameter = bar_stock_diameter - 1 mm    # Stock allowance
min_wall_thickness = 2 mm
thread_depth = thread_nominal_diameter * 1.5     # Aluminum
groove_width = tool_width + 0.2 mm               # Tool clearance
```

### 3D Printing (FDM)

**Key Parameters:**
```
nozzle_diameter = 0.4 mm
layer_height = 0.2 mm
min_wall_thickness = nozzle_diameter * 2
max_overhang_angle = 45°                         # Without support
bridge_max_span = 10 mm
hole_compensation = -0.2 mm                      # Holes print small
```

**Feature validation:**
```
if wall_thickness < min_wall_thickness:
    warning("Wall too thin for reliable printing")
```

## Summary

Parametric modeling transforms CAD from static geometry into intelligent, adaptable designs:

1. **Capture Design Intent:** Encode the "why" behind your geometry
2. **Use Parameters:** Global variables drive dimensions throughout the model
3. **Create Relationships:** Geometric and algebraic constraints maintain design logic
4. **Build Configurations:** One model, multiple variants
5. **Design for Change:** Anticipate modifications, build flexibility early
6. **Process-Specific Parameters:** Tailor parametric approach to manufacturing method

**Next level:** Apply these parametric techniques while implementing DFM principles in Section 16.4.

***

**Next:** [Section 16.4: Design for Manufacturability Principles](section-16.4-dfm-principles.md)

**Previous:** [Section 16.2: CAD Fundamentals](section-16.2-cad-fundamentals.md)
