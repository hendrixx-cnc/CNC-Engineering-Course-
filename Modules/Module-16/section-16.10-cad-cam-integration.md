# Section 16.10: CAD-CAM Integration

## Introduction

The transition from CAD design to CAM (Computer-Aided Manufacturing) programming is a critical handoff point. Well-prepared CAD models import cleanly into CAM software, enabling efficient toolpath generation. Poorly prepared models cause errors, require manual fixes, and waste programming time. This section covers best practices for preparing CAD models for CAM, common pitfalls, and optimization strategies.

## Understanding the CAD-CAM Workflow

### The Complete Pipeline

```
CAD Model → Export → Import to CAM → Setup → Toolpath Generation → Simulation → Post-Processing → G-code → CNC Machine
```

**CAD responsibilities:**
- Accurate geometry
- Proper file format
- Feature organization
- Stock definition
- Coordinate system establishment

**CAM responsibilities:**
- Tool selection
- Toolpath strategies
- Feeds and speeds
- Operation sequencing
- G-code generation

**Overlap zone (CAD can help CAM):**
- Feature recognition geometry
- Work coordinate setup
- Stock modeling
- Fixture clearance zones

## CAD Model Preparation for CAM

### Geometry Quality

**Clean, valid solid models:**
```
✓ Closed, watertight solids (no gaps, missing faces)
✓ No self-intersecting surfaces
✓ No duplicate/overlapping geometry
✓ Proper face normals (consistent inside/outside)
✗ Surface models (CAM needs solids for volume calculations)
✗ Sketch geometry mixed with 3D solids
✗ Construction geometry left visible
```

**CAD cleanup checklist:**
- [ ] Delete construction geometry before export
- [ ] Verify solid model (not surface) using CAD validation tools
- [ ] Check for small sliver faces (merge or remove)
- [ ] Ensure all features properly merged/subtracted

### Feature Recognition

**CAM software recognizes standard features:**
- Holes (through, blind, countersunk, counterbored)
- Pockets (rectangular, irregular)
- Bosses (raised features)
- Slots
- Faces (planar surfaces to mill)

**Design features CAM can recognize:**

**Holes:**
```
Simple cylindrical holes:
  ✓ Single diameter (or stepped diameters)
  ✓ Blind or through
  ✓ Perpendicular to face
```

**Pockets:**
```
Enclosed perimeter:
  ✓ Clear floor
  ✓ Defined depth
  ✓ Radiused internal corners
  ✓ No undercuts
```

**Faces:**
```
Planar surfaces to machine:
  ✓ Flat, bounded regions
  ✓ Accessible to tool without interference
```

**Design to aid feature recognition:**
```
✓ Use CAD hole features (not extruded cuts) — CAM recognizes as drill operations
✓ Create pockets as distinct features (not complex boolean operations)
✓ Separate features for different operations (rough pocket, finish walls separately)
```

### Coordinate Systems and Work Offsets

**Work Coordinate System (WCS):**
- Origin point (X0, Y0, Z0)
- Axis orientation (X, Y, Z directions)
- Matches machine setup and fixturing

**CAD should define WCS matching manufacturing setup:**

**Example 1: Vise-mounted part**
```
Origin: Top-left corner of stock
  X+ → Right
  Y+ → Away from operator
  Z+ → Up from top face

Rationale:
  - Easy to locate with edge finder
  - Matches common machine convention
  - Positive Z moves tool up (safe)
```

**Example 2: Part on fixture plate**
```
Origin: Center of locating hole
  (CAM references hole center, not corner)

Datum features:
  - Locating pin in center hole (X, Y, rotation reference)
  - Part bottom surface on fixture plate (Z reference)
```

**CAD approach:**
- Create coordinate system in CAD at intended WCS origin
- Export geometry with this origin
- CAM imports with correct zero point

### Stock Definition

**Stock = raw material before machining**

**CAD can model stock:**
```
1. Create stock body (separate from part)
   - Rectangular bounding box
   - Cylindrical bar (for turning)
   - Actual stock shape (casting, forging)

2. Position part within stock
   - Leave machining allowance on all machined faces
   - Show as-received surfaces (no machining needed)

3. Export both part AND stock to CAM
```

**Stock modeling benefits:**
- CAM calculates material removal volume
- Toolpath avoids air cutting (faster cycle time)
- Simulation shows stock removal (visualize machining sequence)

**Example: Milled block from plate stock**
```
Stock: 100 × 100 × 25 mm aluminum plate
Part: 95 × 95 × 20 mm (machined all faces)
Stock allowance: 2.5 mm on X, Y sides; 5 mm on top face; bottom face as-received

CAD model:
  - Part body: final dimensions
  - Stock body: 100 × 100 × 25 mm block positioned around part
  - Export both to CAM
```

### Multi-Setup Models

**Parts requiring multiple setups:**

**Approach 1: Single CAD file with setup features**
```
CAD file contains:
  - Final part geometry
  - Datum features (locating holes, surfaces for Setup 2)
  - Notes indicating which features machined in which setup
```

**Approach 2: Separate CAD files per setup**
```
Part_Setup1.step: Geometry as appears after Setup 1 (includes stock for Setup 2)
Part_Setup2.step: Final geometry

CAM workflow:
  - Import Part_Setup1 → program Setup 1 operations
  - Import Part_Setup2 → program Setup 2 operations (using Setup 1 geometry as stock)
```

**Datum establishment for Setup 2:**
```
Setup 1: Create precision locating holes, datum surfaces
Setup 2: Reference these features in CAM for work offset
```

## File Formats for CAM

### 3D Model Formats

**STEP (.step, .stp):**
```
Advantages:
  ✓ Industry standard (ISO 10303)
  ✓ Preserves solid model data
  ✓ Cross-platform compatibility
  ✓ Supports assemblies
  ✓ Retains feature information (some CAM systems)

Best for: Most CAM workflows (milling, turning)
```

**IGES (.iges, .igs):**
```
Advantages:
  ✓ Widely compatible

Disadvantages:
  ✗ Older standard
  ✗ Less reliable than STEP (translation errors common)
  ✗ May lose feature data

Use: Only if CAM system doesn't support STEP (rare)
```

**Native CAD formats:**
```
SolidWorks (.sldprt), Inventor (.ipt), Fusion 360 (.f3d)

Advantages:
  ✓ No translation (if CAM supports native format)
  ✓ Full feature tree available (advanced CAM feature recognition)

Disadvantages:
  ✗ CAM system must support specific CAD format
  ✗ Version compatibility issues

Best for: Integrated CAD/CAM (Fusion 360, SolidWorks CAM)
```

### 2D Profile Formats

**DXF (.dxf) / DWG (.dwg):**
```
Use: 2D cutting operations (plasma, laser, waterjet, wire EDM)

Export from CAD:
  - Flatten 3D part to 2D profile
  - OR create sketch of cut profile
  - Export as DXF

CAM import:
  - Recognizes lines, arcs, circles, splines
  - Generates cutting toolpaths from profile geometry
```

**SVG (.svg):**
```
Use: Some laser cutters, hobbyist CAM software

Less common in industrial applications
```

### Mesh Formats (Avoid for CAM)

**STL (.stl):**
```
Disadvantages for CAM:
  ✗ Faceted (approximation of curves)
  ✗ No dimensional accuracy
  ✗ CAM must triangulate → poor toolpaths

Use ONLY for:
  ✓ 3D printing
  ✓ Visualization

DO NOT use for milling, turning, cutting CAM programs
```

## CAM Software Feature Recognition

### Automatic Feature Recognition

**CAM systems with feature recognition:**
- Autodesk Fusion 360
- Mastercam
- GibbsCAM
- SolidCAM
- Tebis

**How it works:**
```
1. Import CAD model (STEP or native)
2. CAM analyzes geometry
3. Identifies features:
   - Holes (drill candidates)
   - Pockets (2D/3D milling candidates)
   - Faces (face milling candidates)
4. Suggests appropriate toolpaths
5. Operator reviews, accepts, modifies
```

**Example recognition:**
```
CAD model: Block with 6 holes, 2 pockets, top face

CAM recognizes:
  - 6 holes → "Spot drill + drill operations recommended"
  - 2 pockets → "2D adaptive clearing recommended"
  - Top face → "Face milling recommended"

Operator:
  - Accepts hole operations
  - Modifies pocket strategy (wants roughing + finishing passes)
  - Accepts face milling
```

**Design to maximize recognition:**
- Use standard hole features in CAD (not Boolean cuts)
- Create pockets with clear boundaries
- Separate features for different machining strategies

### Manual Feature Selection

**CAM without automatic recognition:**
- Operator manually selects faces, edges, profiles
- Defines operations (2D contour, pocket, drill, etc.)
- More time-consuming but full control

**CAD can still help:**
- Clear, simple geometry
- Features separated into distinct faces/bodies
- Named features or layers (some CAM systems can filter by name/layer)

## Common CAD-to-CAM Issues and Solutions

### Issue 1: Missing or Invalid Geometry

**Symptoms in CAM:**
- Import fails or gives errors
- Geometry appears incomplete
- Toolpath generation fails

**Root causes:**
- Surface model instead of solid
- Open edges (non-watertight)
- Corrupt CAD file

**Solutions:**
```
In CAD:
  ✓ Validate solid model (CAD checker tool)
  ✓ Export as STEP (most reliable translation)
  ✓ Simplify complex features if causing export issues

In CAM:
  ✓ Increase import tolerance (if allowed)
  ✓ Use "heal" or "repair" tools
  ✓ Manually rebuild problem features
```

### Issue 2: Incorrect Units

**Symptoms:**
- Part appears 25.4× too large or too small
- Dimensions don't match drawing

**Root cause:**
- CAD model in mm, CAM interprets as inches (or vice versa)

**Solutions:**
```
In CAD:
  ✓ Verify model units before export (File properties)
  ✓ Include units in filename: "Part_mm.step" or "Part_inch.step"

In CAM:
  ✓ Check import units dialog
  ✓ Measure known dimension after import to verify
```

### Issue 3: Complex Geometry Slows CAM

**Symptoms:**
- CAM software slow or crashes
- Toolpath calculation takes hours

**Root causes:**
- Excessive detail (small fillets, chamfers everywhere)
- Complex splines/surfaces
- High-polygon count imported from mesh

**Solutions:**
```
In CAD:
  ✓ Simplify non-critical features (remove tiny fillets)
  ✓ Use "defeaturing" tools (remove cosmetic details)
  ✓ Create separate "CAM model" (simplified version)

Example:
  Design model: 50 fillets, engraved logo, fine knurling
  CAM model: Essential geometry only (critical dimensions, machined features)
```

### Issue 4: Feature Not Recognized

**Symptoms:**
- CAM doesn't auto-detect holes, pockets
- Must manually program every feature

**Root cause:**
- Feature geometry doesn't match CAM expectations
  (e.g., angled hole, non-cylindrical pocket)

**Solutions:**
```
In CAD:
  ✓ Use standard feature types (hole wizard, not extruded cuts)
  ✓ Keep features perpendicular to setup face when possible
  ✓ Simplify pocket geometry (avoid complex multi-level pockets)

In CAM:
  ✓ Manually define features CAM doesn't recognize
  ✓ Adjust recognition settings (tolerances, angle limits)
```

### Issue 5: Coordinate System Mismatch

**Symptoms:**
- Part appears rotated or offset in CAM
- Toolpaths in wrong location

**Root cause:**
- CAD origin ≠ CAM work offset expectation
- Axis orientation mismatch

**Solutions:**
```
In CAD:
  ✓ Define explicit coordinate system at machining origin
  ✓ Export from this coordinate system
  ✓ Document origin location on drawing

In CAM:
  ✓ Redefine WCS to match CAD intent
  ✓ Translate/rotate geometry after import if needed
  ✓ Verify setup before toolpath generation
```

## Optimizing CAD Models for Efficient CAM Programming

### 1. Organize Features by Operation

**Group similar features:**
```
All through-holes on top face:
  - CAM can pattern drill operation
  - Faster programming

Mixed features scattered:
  - CAM must program each individually
  - Slower, error-prone
```

**CAD approach:**
- Linear or circular patterns for repeated features
- Consistent feature types (all holes same depth if possible)

### 2. Minimize Setups

**Design features accessible from single direction:**
```
✓ All critical machining from top face
✓ Bottom face as-received or rough-machined only

✗ Critical features on top, sides, bottom
  → Multiple setups, longer CAM programming time
```

**If multiple setups required:**
- Provide locating features (dowel pin holes)
- Document setup sequence on drawing
- Consider separate CAD files per setup

### 3. Use Standard Tool Sizes

**CAD model with standard corner radii:**
```
Internal corner radii: 1.5 mm, 3 mm, 6 mm (match common tool sizes)

CAM benefits:
  ✓ Uses standard tools already in library
  ✓ Faster programming (no custom tool creation)
  ✓ Lower tooling cost (standard endmills readily available)
```

**CAD model with arbitrary radii:**
```
Internal corner radii: 2.3 mm, 4.7 mm, 5.9 mm

CAM challenges:
  ✗ Requires custom tool definition
  ✗ May need special-order tooling
  ✗ Slows programming
```

### 4. Provide Stock Models

**Include stock body in export:**
```
CAM benefits:
  ✓ Automatic stock-to-part calculation
  ✓ Optimized roughing toolpaths (removes only necessary material)
  ✓ Simulation shows actual material removal
```

**Without stock model:**
```
CAM must:
  - Manually define bounding box
  - Conservative toolpaths (assumes more stock)
  - Longer cycle times (unnecessary air cutting)
```

### 5. Name Features Logically

**Named features (if CAM supports):**
```
CAD feature names:
  - Mounting_Holes_M6
  - Main_Pocket
  - Datum_A_Face
  - Thread_M8x1.25

CAM import:
  - Can filter/select features by name
  - Organize operations logically
  - Easier to review program
```

## Integrated CAD/CAM Systems

### All-in-One Platforms

**Autodesk Fusion 360:**
```
Integrated CAD + CAM in same environment:
  ✓ No export/import (seamless transition)
  ✓ Full parametric history available to CAM
  ✓ Changes in CAD auto-update CAM (with warnings)

Workflow:
  1. Design in CAD workspace
  2. Switch to Manufacture workspace (same file)
  3. Define setups, operations directly on CAD model
  4. Generate toolpaths
  5. Simulate
  6. Post-process to G-code
```

**SolidWorks CAM (CAMWorks):**
```
CAM plugin for SolidWorks:
  ✓ Works directly on SolidWorks files
  ✓ Feature recognition from native feature tree
  ✓ Parametric CAM (dimensions change → toolpaths update)
```

**Mastercam for SolidWorks:**
```
Integrated CAM for SolidWorks users:
  ✓ Reads native SolidWorks files
  ✓ Associates to SolidWorks features
  ✓ Separate Mastercam license required
```

### Advantages of Integrated Systems

**Single file workflow:**
- No export/import steps
- Reduced file management
- CAD changes trigger CAM review (warnings if toolpaths affected)

**Full feature access:**
- CAM sees entire parametric history
- Better feature recognition
- Can suppress features for CAM (without affecting design)

**Associativity:**
- Change CAD dimension → CAM toolpaths update automatically (or flag for review)
- Ensures CAM always matches current design

### Standalone CAM Systems

**Separate CAM software:**
```
Examples:
  - Mastercam (standalone)
  - GibbsCAM
  - Edgecam
  - BobCAD-CAM

Workflow:
  1. Design in any CAD (SolidWorks, Fusion, FreeCAD, etc.)
  2. Export neutral format (STEP)
  3. Import to CAM system
  4. Program operations
  5. Generate G-code
```

**Advantages:**
- Choose best CAD for design, best CAM for programming
- Powerful CAM features (5-axis, advanced toolpath strategies)
- Independent updates (CAD and CAM software on separate release cycles)

**Disadvantages:**
- Extra import/export step
- No automatic update if CAD changes
- Must manually re-import revised models

## Verification and Simulation

### CAM Simulation

**Verifying toolpaths before machining:**
```
CAM simulation shows:
  ✓ Tool removing material from stock
  ✓ Finished part dimensions
  ✓ Potential collisions (tool holder, fixtures)
  ✓ Gouges or uncut areas

Check:
  - Does simulated part match CAD model?
  - Any missed features?
  - Any over-cutting (crashes)?
  - Tool holder clearance?
```

**CAD role in simulation:**
- Provide accurate stock model (simulation starts here)
- Model fixtures, clamps if possible (check clearances)

### Post-Simulation Review

**Compare simulation result to CAD:**
```
Overlay simulated part on original CAD:
  ✓ Perfect match → Toolpaths correct
  ✗ Differences → Review toolpath issues

Common issues caught:
  - Uncut material (tool too large, no clearance)
  - Over-cut (tool compensated wrong direction)
  - Missing operations
```

## Summary

Efficient CAD-to-CAM integration requires thoughtful CAD model preparation:

**CAD Model Quality:**
- Clean, valid solid models (no gaps, overlaps)
- Organized features (by operation, accessibility)
- Proper coordinate systems (match setup)

**File Formats:**
- STEP (preferred for 3D machining)
- DXF (2D cutting)
- Native formats (integrated CAD/CAM)

**Feature Recognition:**
- Design standard features (holes, pockets)
- Use CAD feature tools (not Boolean operations)
- Simplify geometry (remove unnecessary complexity)

**Stock Definition:**
- Model stock body
- Export with part
- Enables optimized toolpaths

**Common Issues:**
- Invalid geometry: Validate before export
- Unit mismatches: Document units clearly
- Complex geometry: Simplify CAM models
- Coordinate mismatches: Define explicit WCS

**Integrated vs. Standalone CAM:**
- Integrated: Seamless, associative, single file
- Standalone: Flexible, powerful, extra import step

**Verification:**
- Simulate toolpaths in CAM
- Compare result to CAD model
- Catch errors before machining

**Next section** covers advanced CAD techniques including simulation, topology optimization, and cutting-edge design methods.

***

**Next:** [Section 16.11: Advanced Techniques](section-16.11-advanced-techniques.md)

**Previous:** [Section 16.9: Documentation and Drawings](section-16.9-documentation-drawings.md)
