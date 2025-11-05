# Section 16.8: Assembly Design

## Introduction

Most mechanical systems consist of multiple parts working together. Assembly design in CAD involves not just modeling individual components, but defining how they fit, move, and interact. Good assembly design ensures parts can be manufactured individually, assembled efficiently, and serviced when needed. This section covers assembly modeling strategies, design for assembly (DFA) principles, and best practices for creating robust, manufacturable assemblies.

## Assembly Modeling Approaches

### Bottom-Up Design

**Process:**
1. Design individual parts independently
2. Create assembly file
3. Insert parts into assembly
4. Apply mates/constraints to position parts

**Advantages:**
- Parts can be designed and detailed independently
- Multiple designers can work in parallel
- Parts can be reused in different assemblies
- Part files remain independent (easier file management)

**Disadvantages:**
- Interface dimensions must be coordinated manually
- Changes to one part may not propagate to mating parts
- Risk of mismatched interfaces

**Best for:**
- Standard parts (bolts, bearings, purchased components)
- Modular designs with well-defined interfaces
- Large teams working on subsystems

**Example workflow:**
```
1. Design motor mount plate (separate file)
2. Design motor bracket (separate file)
3. Download motor CAD model (vendor)
4. Create assembly file
5. Insert all parts
6. Apply mates to align mounting holes
7. Check for interference
```

### Top-Down Design

**Process:**
1. Create assembly file first
2. Create skeleton sketch with critical interfaces
3. Design parts in context of assembly
4. Parts reference assembly geometry or other parts

**Advantages:**
- Interface dimensions automatically coordinated
- Changes propagate to all affected parts
- Parts designed to fit perfectly from the start
- Visualize whole system during design

**Disadvantages:**
- Complex file dependencies (external references)
- Cannot easily reuse parts in other assemblies
- File management more difficult
- Circular references can cause errors

**Best for:**
- Custom designs with many interfaces
- Single designer projects
- Designs where fit is critical
- Weldments and fabricated structures

**Example workflow:**
```
1. Create assembly file
2. Create master skeleton sketch:
   - Motor mounting face
   - Shaft centerline
   - Bolt pattern locations
3. Create motor mount part in assembly (references skeleton)
4. Create bracket in assembly (references motor mount and skeleton)
5. Parts automatically align because they share references
```

### Middle-Out (Hybrid) Approach

**Process:**
- Define key interface parts first (top-down)
- Add standard/purchased parts (bottom-up)
- Create detail parts referencing interface parts (hybrid)

**Advantages:**
- Balances control with flexibility
- Critical interfaces coordinated
- Non-critical parts independent

**Best for:**
- Most real-world projects
- Teams with mix of custom and standard parts

## Mates and Constraints

### Common Mate Types

**Coincident:**
```
Aligns two faces or planes flush together

Example: Mounting plate bottom surface coincident with base surface
```

**Concentric:**
```
Aligns two cylindrical or circular features on same axis

Example: Shaft concentric with bearing inner race
```

**Distance:**
```
Maintains specific distance between features

Example: Spacer maintaining 10mm gap between two plates
```

**Parallel:**
```
Keeps two planes or axes parallel (but not coincident)

Example: Top plate parallel to bottom plate in multi-level structure
```

**Perpendicular:**
```
Maintains 90° relationship between features

Example: Vertical post perpendicular to base plate
```

**Angle:**
```
Maintains specific angle between features

Example: Bracket at 45° angle to mounting surface
```

**Tangent:**
```
Maintains tangent relationship between surfaces

Example: Belt tangent to pulleys
```

### Mate Strategy

**Best practices:**

**1. Constrain incrementally:**
```
Each part has 6 degrees of freedom (DOF):
  3 translations (X, Y, Z)
  3 rotations (about X, Y, Z)

Apply mates to remove DOF until fully constrained (0 DOF remaining)
```

**2. Use geometric mates before distance mates:**
```
Good sequence:
  1. Coincident (align primary surfaces)
  2. Concentric (align holes/shafts)
  3. Distance (set specific spacing)

Poor sequence:
  1. Distance, distance, distance → over-constrained, conflicts
```

**3. Avoid redundant mates:**
```
Over-constrained assembly = mate conflicts = unstable model

Example of redundancy:
  - Part already located with 3 mates (fully constrained)
  - Adding 4th mate creates conflict if dimensions don't perfectly match
```

**4. Ground primary component:**
```
"Ground" or "fix" one part as reference (usually base plate, frame)
All other parts mate relative to grounded part or previously constrained parts
```

## Design for Assembly (DFA) Principles

### Minimize Part Count

**Every additional part increases:**
- Design time (CAD modeling, drawings, revisions)
- Manufacturing cost (setup, inspection, handling)
- Inventory complexity (storage, tracking, stock-outs)
- Assembly labor (pick, orient, fasten)
- Potential failure points (joints, fasteners)
- Service difficulty (disassembly, part replacement)

**Real-World Cost Impact:**

**Rule of thumb:** Each additional part adds $3-8 in total cost (design + manufacturing + assembly + inventory).

| Cost Factor | Per Additional Part | 10-Part Assembly | 50-Part Assembly |
|-------------|---------------------|------------------|------------------|
| Design/Documentation | $50-150 (one-time) | $500-1,500 | $2,500-7,500 |
| Manufacturing setup | $2-5/part | $20-50/unit | $100-250/unit |
| Assembly labor | $1-3/part | $10-30/unit | $50-150/unit |
| **Total per unit** | **$3-8** | **$30-80** | **$150-400** |

**Strategies to Reduce Part Count:**

**Example 1: Combine Parts (Motor Bracket)**

**Amateur Design (bolted construction):**
- Base plate: 1 part, $15
- 2× L-brackets: 2 parts, $12 each = $24
- 8× M6 screws: $0.50 each = $4
- Assembly time: 12 minutes @ $30/hr = $6
- **Total: 11 parts, $49 per assembly**

**Professional Design (single bent bracket):**
- One-piece sheet metal bracket (laser cut + brake press)
- Material + cutting: $8
- Bending: $3
- **Total: 1 part, $11 per assembly**

**Savings: $38 per assembly (78% cost reduction) + 10 fewer parts to manage!**

**Example 2: Integral Features (Shaft Assembly)**

**Before (separate components):**
```
- Shaft: ⌀20mm × 150mm, $8
- Collar: ⌀20mm ID × ⌀30mm OD × 10mm, $6
- M6 setscrew: $0.75
- Assembly time: 3 minutes @ $30/hr = $1.50
Total: 3 pieces, $16.25
```

**After (machined shoulder):**
```
- Shaft with machined shoulder: ⌀20mm × 150mm with ⌀30mm × 10mm shoulder
- Material + machining: $12
Total: 1 piece, $12
```

**Savings: $4.25 per assembly (26%) + eliminates setscrew loosening failure mode**

**Example 3: Welded Frame Assembly**

**Bolted Frame (amateur approach):**
- 12 aluminum extrusion pieces: 12 × $8 = $96
- 48 corner brackets: 48 × $2 = $96
- 96 M6 screws: 96 × $0.40 = $38.40
- Assembly time: 2 hours @ $30/hr = $60
- **Total: 156 pieces, $290.40 per frame**

**Welded Frame (professional approach):**
- 12 aluminum extrusion pieces: 12 × $8 = $96
- Welding: 24 joints × $3/joint = $72
- **Total: 12 pieces (1 welded assembly), $168 per frame**

**Savings: $122.40 per frame (42% cost reduction) + eliminates 144 fasteners!**

**Part Count Decision Matrix:**

| Separate Parts? | Integrated Part? | Choose When... |
|-----------------|------------------|----------------|
| ✓ Bolted bracket (easy disassembly) | ✓ Welded/bent bracket (permanent) | Field service required? Bolted. One-time assembly? Integrated. |
| ✓ Shaft + collar (adjustable position) | ✓ Machined shoulder (fixed) | Position needs adjustment? Collar. Fixed position? Shoulder. |
| ✓ Multi-part (different materials) | ✓ Single-part | Need steel shaft in aluminum housing? Separate. Same material? Integrate. |

**When NOT to reduce part count:**
- Serviceability required (must replace worn components)
- Different materials needed (heat resistance, wear resistance)
- Adjustment needed (collars, spacers for position tuning)
- Manufacturing cost of integrated part > sum of separate parts

### Design for Ease of Assembly

**Self-Aligning Features:**
```
Chamfers on shafts and holes:
  - Lead-in for easier insertion
  - 0.5 mm × 45° chamfer typical

Tapered dowel pins:
  - Self-center as they insert
  - Pull parts into alignment
```

**Minimize Orientations:**
```
Assemble all parts from one direction (top-down assembly)
  - Gravity assists
  - Simpler fixturing
  - Faster assembly

Avoid: Assembly requiring flipping part multiple times
```

**Snap-Fits and Captive Hardware:**
```
Snap-fit features:
  - No separate fasteners
  - One-hand assembly
  - Common in plastic parts

Captive screws:
  - Screw stays in part (can't fall out or get lost)
  - Spring or snap ring retains screw
```

**Symmetry:**
```
Symmetric parts can be installed in any orientation
  - Reduces assembly errors
  - Faster assembly (no need to check orientation)

Example: Square plate with symmetric hole pattern
  - Can be rotated 90° and still fits
```

**Keying and Poka-Yoke (Error-Proofing):**
```
Asymmetric features prevent incorrect assembly

Examples:
  - Connector with one pin larger (can only plug in one way)
  - Mounting holes on offset pattern (part only fits one orientation)
  - Chamfer on one corner (visual indicator of correct orientation)
```

### Standardization

**Use common fasteners across assembly:**
```
Good: All M6 socket head cap screws (one tool size, bulk purchase)
Poor: M4, M5, M6, M8 screws mixed (multiple tools, small quantity purchases)
```

**Standard part libraries:**
```
Bearings: Select from standard sizes (6000, 6200, 6300 series)
Belts/pulleys: Standard pitches (GT2, HTD, etc.)
Linear guides: Standard rail sizes (15mm, 20mm, 25mm)
Motors: NEMA standard sizes
```

## Fastener Selection and Design

### Common Fastener Types

**Socket Head Cap Screw (SHCS):**
```
Advantages:
  - High strength
  - Compact head (flush or below surface)
  - Allen key drive (common, reliable)

Applications:
  - Structural connections
  - Where low-profile head needed
```

**Button Head Cap Screw:**
```
Advantages:
  - Lower profile than SHCS
  - Rounded head (aesthetics, safety)

Applications:
  - User-facing surfaces
  - Where very low profile desired
```

**Flat Head Socket Screw:**
```
Advantages:
  - Countersunk (fully flush surface)
  - Clean appearance

Applications:
  - Sliding surfaces
  - Where absolutely flush surface required

Disadvantage:
  - Requires countersink (extra machining operation)
```

**Hex Head Bolt:**
```
Advantages:
  - High torque capacity (larger wrench contact)
  - Inexpensive

Applications:
  - Heavy structural joints
  - High-torque applications

Disadvantage:
  - Large head (requires clearance)
```

**Set Screw:**
```
Advantages:
  - Flush or recessed (no protrusion)
  - Locks components on shafts

Applications:
  - Collars, pulleys on shafts
  - Locating pins

Types:
  - Cup point (most common, mars shaft slightly)
  - Flat point (doesn't mar shaft)
  - Cone point (high friction)
```

### Fastener Sizing and Specification

**Hole clearances:**

| Screw Size | Close Clearance | Normal Clearance | Loose Clearance |
|------------|------------------|------------------|-----------------|
| M3 | 3.2 mm | 3.4 mm | 3.6 mm |
| M4 | 4.3 mm | 4.5 mm | 4.8 mm |
| M5 | 5.3 mm | 5.5 mm | 5.8 mm |
| M6 | 6.4 mm | 6.6 mm | 7.0 mm |
| M8 | 8.4 mm | 9.0 mm | 10.0 mm |
| M10 | 10.5 mm | 11.0 mm | 12.0 mm |

**CAD approach:**
```
Parameters:
  screw_size = "M6"
  clearance_type = "normal"

  If screw_size == "M6" AND clearance_type == "normal":
    hole_diameter = 6.6 mm
```

**Thread engagement:**
```
Minimum thread engagement:

Steel into steel: 1× nominal diameter
  M6 screw → 6 mm min engagement

Aluminum into aluminum: 1.5× nominal diameter
  M6 screw → 9 mm min engagement

Plastic: 2× nominal diameter (or use threaded insert)
  M6 screw → 12 mm engagement OR heat-set insert
```

**Counterbore dimensions:**

| Screw Size | Socket Head Cap Screw | Button Head |
|------------|------------------------|-------------|
| M3 | ⌀6 mm × 3 mm deep | ⌀5.5 mm × 2 mm |
| M4 | ⌀7.5 mm × 4 mm deep | ⌀7 mm × 2.5 mm |
| M5 | ⌀9.5 mm × 5 mm deep | ⌀8.5 mm × 3 mm |
| M6 | ⌀11 mm × 6 mm deep | ⌀10 mm × 3.5 mm |
| M8 | ⌀14 mm × 8 mm deep | ⌀13 mm × 4.5 mm |

**Countersink dimensions (flat head screws):**
```
Countersink angle: 90° or 82° (match screw)
Diameter: Screw head diameter + 0.5 mm clearance

M6 flat head: ⌀12 mm countersink × 82° angle
```

### CAD Modeling of Fasteners

**Simplified representation (recommended):**
```
Model:
  - Clearance hole in parts
  - Cosmetic screw in assembly (simplified cylinder)

Don't model:
  - Threads (complex geometry, slows CAD)
  - Exact head geometry

Benefits:
  - Faster model performance
  - Easier to swap fastener sizes
  - Drawings show simplified holes (easier to dimension)
```

**Fastener libraries:**
```
Most CAD systems include:
  - Standard fastener libraries (ANSI, ISO)
  - Automatic hole creation
  - BOM generation with part numbers

Example: SolidWorks Toolbox, Fusion 360 Insert > McMaster-Carr
```

## Interference Detection

### Checking for Collisions

**Interference check tools in CAD:**
```
Detect overlapping geometry:
  - Parts occupying same physical space
  - Impossible to assemble as designed

Process:
  1. Select all parts in assembly (or specific subset)
  2. Run interference detection
  3. Review report (volume of interference, location)
  4. Fix design (adjust dimensions, clearances)
```

**Clearance check:**
```
Verify minimum spacing between parts:
  - Ensure tool access for fastener installation
  - Provide clearance for thermal expansion
  - Allow for tolerance stack-up

Example:
  Minimum clearance: 2 mm between all non-mating parts
  If clearance < 2 mm → Warning, review design
```

### Dynamic Interference (Motion Studies)

**For assemblies with moving parts:**
```
Simulate motion through full range of travel
Check for:
  - Parts colliding during movement
  - Cable/wire interference
  - Adequate clearance throughout motion

Example: Robot arm
  - Simulate all joint rotations
  - Check arm doesn't collide with base, obstacles
  - Verify end effector workspace
```

## Subassemblies

### When to Create Subassemblies

**Logical grouping:**
```
Subassembly when:
  - Parts assembled together as unit
  - Unit can be tested independently
  - Simplifies top-level assembly
  - Parts always used together

Examples:
  - Motor + mounting bracket + coupling = motor_mount_assembly
  - PCB + standoffs + enclosure = electronics_module
  - Bearing + shaft + spacers = shaft_assembly
```

### Subassembly Structure

**Hierarchical organization:**
```
Top_Level_Assembly
├─ Frame_Subassembly
│  ├─ Base_Plate
│  ├─ Vertical_Posts (4x)
│  └─ Top_Plate
├─ Motion_System_Subassembly
│  ├─ Linear_Rails (2x)
│  ├─ Carriages (2x)
│  └─ Mounting_Blocks (4x)
├─ Drive_System_Subassembly
│  ├─ Motor
│  ├─ Motor_Bracket
│  ├─ Coupling
│  └─ Leadscrew
└─ Hardware
   ├─ M6_SHCS (24x)
   ├─ M6_Washers (24x)
   └─ M6_Nuts (24x)
```

**Benefits:**
- Each subassembly can be assigned to different team member
- Subassemblies can be performance-tested independently
- Simplified BOM structure
- Easier assembly instructions (build subassemblies first, then combine)

## Bill of Materials (BOM)

### BOM Structure

**Indented BOM:**
```
1. Main_Assembly
   1.1 Frame_Subassembly
       1.1.1 Base_Plate (1x)
       1.1.2 Vertical_Post (4x)
       1.1.3 Top_Plate (1x)
       1.1.4 M6×20 SHCS (16x)
   1.2 Motor_Mount_Subassembly
       1.2.1 Motor_Bracket (1x)
       1.2.2 NEMA_23_Motor (1x) [PURCHASED]
       1.2.3 M5×16 SHCS (4x)
   1.3 Hardware_Kit
       1.3.1 M6_Washer (16x)
       1.3.2 M6_Locknut (16x)
```

**Flat BOM (for purchasing):**
```
Part Number | Description | Qty | Source | Unit Cost | Total
------------|-------------|-----|--------|-----------|------
BP-001 | Base Plate | 1 | In-house | $15.00 | $15.00
VP-002 | Vertical Post | 4 | In-house | $8.00 | $32.00
TP-003 | Top Plate | 1 | In-house | $12.00 | $12.00
MB-004 | Motor Bracket | 1 | In-house | $6.00 | $6.00
MOT-NEMA23 | NEMA 23 Stepper | 1 | Vendor A | $45.00 | $45.00
M6x20-SHCS | M6×20 Socket Cap | 16 | McMaster | $0.25 | $4.00
M5x16-SHCS | M5×16 Socket Cap | 4 | McMaster | $0.18 | $0.72
...
TOTAL | | | | | $114.72
```

### BOM Management in CAD

**Automatic BOM generation:**
```
CAD systems can auto-generate BOM from assembly:
  - Part names
  - Quantities (counts instances)
  - Custom properties (material, finish, source)
  - Mass/weight
```

**Custom properties to include:**
```
Part-level properties:
  - Part number (unique ID)
  - Description
  - Material
  - Finish/coating
  - Source (in-house, purchased, vendor name)
  - Unit cost
  - Lead time

Assembly-level:
  - Assembly number
  - Revision
  - Designer
  - Date
```

**BOM export formats:**
```
- Excel (.xlsx) - Most common, easy editing/sharing
- CSV - Universal import to ERP/MRP systems
- PDF - Distribution to suppliers, assembly technicians
```

## Assembly Documentation

### Exploded Views

**Purpose:**
- Show how parts fit together
- Assembly/disassembly instructions
- Service manuals

**Creating exploded views in CAD:**
1. Create new configuration/state ("exploded")
2. Move parts outward along logical assembly paths
3. Add "explosion lines" showing part relationships
4. Render with part balloons (number each part)

### Assembly Instructions

**Step-by-step documentation:**
```
Step 1: Attach vertical posts to base plate
  - Parts: Base plate (1), Vertical posts (4), M6×20 SHCS (16)
  - Tools: 5mm Allen key
  - Torque: 8 Nm
  - Image: Exploded view showing bolt locations

Step 2: Install motor mount subassembly
  - Parts: Motor mount subassembly (preassembled)
  - Parts: M6×25 SHCS (4)
  - Tools: 5mm Allen key
  - Torque: 10 Nm
  - Image: Motor mount positioned on frame
...
```

**CAD-generated assembly instructions:**
- Fusion 360: Animate assembly sequence
- SolidWorks: Composer (dedicated assembly instruction tool)
- Manual: Screenshots of each assembly step

## Practical Example: Linear Actuator Assembly

### Design Requirements

**System:** Linear actuator for CNC application

**Components needed:**
- Frame structure
- Linear guides (2x rails)
- Carriage plate
- Leadscrew and nut
- Motor mount and motor
- Coupling
- Hardware

### Assembly Design Process

**Step 1: Define interfaces (top-down)**
```
Master skeleton sketch:
  - Rail mounting surface (datum A)
  - Rail spacing (200 mm)
  - Carriage travel (300 mm stroke)
  - Motor mounting location
```

**Step 2: Design frame (in-context)**
```
Frame_Base_Plate:
  - References skeleton rail spacing
  - Mounting holes for rails (M5 tapped, 50 mm spacing)
  - Motor mounting face

Frame_End_Plates (2x):
  - Mount to base plate
  - Support leadscrew bearings
```

**Step 3: Add purchased parts (bottom-up)**
```
Insert from libraries:
  - Linear rails (HGH20, 400 mm length)
  - Linear carriages (HGH20CA)
  - Leadscrew (1605, 350 mm)
  - Ballnut (1605)
  - NEMA 23 motor
  - Flexible coupling (8mm to 16mm)
  - Bearings (6004-2RS for leadscrew support)
```

**Step 4: Design custom parts (in-context)**
```
Carriage_Plate:
  - Mounting holes match linear carriage bolt pattern (references carriage)
  - Ballnut pocket (references ballnut dimensions)
  - Payload mounting holes (50×50 mm pattern)

Motor_Mount_Bracket:
  - References motor bolt pattern
  - Positions motor axis concentric with leadscrew
  - Mounts to frame end plate
```

**Step 5: Add hardware**
```
From fastener library:
  - M5×12 SHCS (16x) - Rail mounting
  - M4×12 SHCS (8x) - Carriage mounting
  - M5×20 SHCS (4x) - Motor mounting
  - M6×20 SHCS (8x) - End plate mounting
```

**Step 6: Verify and document**
```
Interference check: Pass (no collisions)
Motion study: Carriage travels full 300 mm stroke, no interference
BOM generated: 45 line items total
Exploded view created
Assembly instructions: 8 steps
```

### DFA Review

**Optimizations applied:**
```
✓ All fasteners: M4, M5, M6 (3 sizes only, 2 hex keys)
✓ Assembly direction: All from top (gravity-assisted)
✓ Subassemblies: Motor + bracket preassembled and tested
✓ Alignment features: Dowel pins locate end plates to base
✓ Standard parts: Rails, bearings, hardware all off-the-shelf
```

## Summary

Effective assembly design requires planning beyond individual part geometry:

**Assembly Modeling:**
- Bottom-up: Independent parts, later assembled (flexible)
- Top-down: Parts designed in assembly context (coordinated interfaces)
- Hybrid: Best of both approaches

**DFA Principles:**
1. Minimize part count (combine, integrate, weld/bond)
2. Design for ease of assembly (self-aligning, one-direction, snap-fits)
3. Standardize fasteners and parts
4. Use keying and poka-yoke (error-proofing)

**Fasteners:**
- Select appropriate types (SHCS, button head, flat head)
- Specify correct clearances and engagement
- Use simplified models in CAD (performance)

**Verification:**
- Interference detection (static)
- Motion studies (dynamic)
- BOM accuracy (purchasing, costing)

**Documentation:**
- Exploded views
- Assembly instructions
- BOM (indented and flat formats)

**Next section** covers how to generate engineering drawings and technical documentation from CAD models.

***

**Next:** [Section 16.9: Documentation and Engineering Drawings](section-16.9-documentation-drawings.md)

**Previous:** [Section 16.7: Process-Specific Design](section-16.7-process-specific-design.md)
