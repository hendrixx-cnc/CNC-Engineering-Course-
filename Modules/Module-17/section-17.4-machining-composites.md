# 17.4 Machining Composites - Cutting Mechanics and Tooling

## Composite Machining Challenges

### Unique Characteristics

**Anisotropic Material**:
- Properties vary with fiber direction
- Cutting forces different parallel vs perpendicular to fibers
- Different failure modes in each direction

**Heterogeneous Structure**:
- Two distinct phases (fiber + matrix)
- Different hardness and ductility
- Interface between phases creates challenges

**Abrasive Fibers**:
- Carbon fiber: Hardness 2000-3000 HV (comparable to hardened steel)
- Glass fiber: Hardness 500-600 HV (harder than aluminum)
- Silicon carbide fiber: Hardness 2500 HV
- Rapid tool wear on conventional tooling

**Low Thermal Conductivity**:
- Polymer matrix: 0.2-0.5 W/(m·K)
- Cf. aluminum: 200 W/(m·K) (400× better)
- Heat concentrates at cutting zone → matrix degradation

### Cutting Mechanisms

**Fiber-Dominated Cutting** (parallel to fibers):
- Fibers bend ahead of cutting edge
- Shear failure of fibers
- Matrix supports fibers
- Good surface finish possible

**Matrix-Dominated Cutting** (perpendicular to fibers):
- Matrix cut first
- Fibers exposed and cut individually
- Risk of fiber pullout and delamination
- Rougher surface finish

**Multi-Directional Laminates**:
- Each ply cuts differently
- 0° plies: Longitudinal cutting (smooth)
- 90° plies: Transverse cutting (rough)
- ±45° plies: Intermediate behavior

**Interlaminar Cutting**:
- Cutting between plies
- Weak interface → delamination risk
- Critical during drilling exit and edge trimming

## Defects in Composite Machining

### Delamination

**Definition**: Separation of plies, creating void between layers.

**Types**:

**Entry Delamination** (drilling):
- Drill pushes first ply down
- Bending stress exceeds interlaminar strength
- First ply separates from second ply

**Exit Delamination** (drilling):
- Most common and severe
- Drill breakthrough pushes last ply outward
- Unsupported material peels away

**Edge Delamination** (milling):
- Cutting forces peel plies apart at free edge
- Worse with dull tools
- Climb milling reduces risk

**Mechanisms**:
- Peel stress at ply interface
- Exceeds Mode I fracture toughness
- Propagates if not arrested

**Critical Thrust Force** (drilling):

For zero delamination:
$$F_{crit} = \pi \sqrt{\frac{8 G_{IC} E t^3}{3(1-\nu^2)}}$$

where:
- $G_{IC}$ = Mode I fracture toughness (N/mm)
- $E$ = flexural modulus (MPa)
- $t$ = uncut laminate thickness (mm)
- $\nu$ = Poisson's ratio

**Example** (carbon/epoxy):
- $G_{IC}$ = 0.2 N/mm
- $E$ = 70,000 MPa
- $t$ = 3 mm
- $\nu$ = 0.3
$$F_{crit} = \pi \sqrt{\frac{8 \times 0.2 \times 70000 \times 27}{3 \times 0.91}} = 486 \text{ N (109 lbf)}$$

Exceed this thrust → delamination initiates.

**Prevention**:
- Sharp tools (low cutting forces)
- Backup support (exit side drilling)
- Reduced feed rate
- Compression tooling (milling)

### Fiber Pullout

**Mechanism**:
- Fiber-matrix interface fails
- Fiber pulled from matrix instead of cut
- Leaves protruding fiber and void

**Causes**:
- Dull cutting edge
- Insufficient fiber support (wrong fiber angle)
- Poor fiber-matrix adhesion
- Excessive cutting speed (matrix softens)

**Effect on Quality**:
- Rough surface (protruding fibers)
- Reduced mechanical properties
- Poor cosmetic appearance
- Assembly problems (mating surfaces)

**Prevention**:
- Sharp tools (minimize cutting forces)
- Proper cutting geometry
- Support fibers during cutting (backing)

### Matrix Burning/Melting

**Problem**: Polymer matrix degrades at cutting temperature.

**Typical Matrix Limits**:
- Epoxy: 150-180°C continuous, begins degrading at 200°C
- Polyester: 120°C continuous
- PEEK: 250°C continuous (high-temp thermoplastic)

**Causes**:
- Excessive cutting speed
- Dull tool (friction)
- Insufficient coolant
- Tool rubbing (inadequate clearance)

**Signs**:
- Discoloration (brown/black)
- Burned smell
- Gummy residue on tool
- Surface porosity (matrix vaporized)

**Prevention**:
- Moderate cutting speeds (500-800 SFM typical)
- Sharp tools
- Adequate coolant/air blast
- Proper chip evacuation

### Fuzzing

**Definition**: Loose fiber ends standing up from cut surface.

**Causes**:
- Fiber bending instead of cutting (dull tool)
- Improper fiber orientation relative to cutting direction
- Insufficient tool support angle

**Effect**:
- Poor surface finish
- Reduced mechanical properties
- Difficult to paint/coat
- Handling hazard (fiber splinters)

**Prevention**:
- Sharp tools changed frequently
- Proper tool geometry
- Climb milling preferred
- Abrading/sanding post-machining

### Microcracking

**Definition**: Fine cracks in matrix, not visible to naked eye.

**Detection**: 
- Ultrasonic C-scan
- Microscopic examination
- Dye penetrant

**Causes**:
- Thermal stress (heating/cooling cycles)
- Mechanical stress (excessive cutting forces)
- Impact damage from chip strikes

**Concern**: Reduces mechanical properties, moisture ingress path.

## Tool Materials for Composites

### Diamond Tooling

**Polycrystalline Diamond (PCD)**:

**Structure**: Diamond particles (2-30 μm) sintered onto carbide substrate
- Diamond layer: 0.5-1.0 mm thick
- Carbide backing: Provides toughness

**Properties**:
- Hardness: 8000-10,000 HV (hardest cutting tool material)
- Thermal conductivity: 500-2000 W/(m·K) (excellent heat removal)
- Low friction coefficient: 0.05-0.1
- Abrasion resistance: 100× carbide in composite machining

**Grades**:
- **Coarse grain** (20-30 μm): Toughest, rougher edge, roughing
- **Medium grain** (10 μm): General purpose
- **Fine grain** (2-5 μm): Sharpest edge, best finish, finishing
- **Extra fine** (<2 μm): Finest finish, most brittle

**Tool Life**:
- In carbon fiber: 50-200× longer than carbide
- Example: Carbide drill = 50 holes, PCD drill = 5000+ holes

**Cost**:
- 10-30× carbide cost
- PCD router bit: $200-800 vs $20-50 carbide
- Justified by tool life in production

**Limitations**:
- Cannot cut ferrous metals (carbon diffuses into steel at cutting temp)
- Brittle (sensitive to impact)
- Cannot be resharpened in most cases (brazed tip)

**Applications**:
- Carbon fiber machining (primary choice)
- Fiberglass machining
- Abrasive plastics
- Wood composites (MDF, particleboard)

### Chemical Vapor Deposition (CVD) Diamond

**Structure**: Pure diamond film deposited on carbide substrate
- Diamond layer: 10-30 μm thick
- Smoother than PCD (no grain boundaries)

**Advantages over PCD**:
- Sharper edge (smoother structure)
- Better surface finish
- Lower friction

**Disadvantages**:
- Thinner coating (less total diamond)
- More expensive
- Edge failure if coating breached

**Applications**: Precision finishing of composites

### Solid Carbide

**For Composites**: Uncoated micrograin carbide preferred
- Grain size: 0.5-0.8 μm (fine grain)
- Binder: 6-10% cobalt (tough)

**Advantages**:
- Lower cost than diamond ($20-100 per tool)
- Can be resharpened
- Good for low-volume work

**Disadvantages**:
- Wears rapidly (10-100 holes vs 5000+ for PCD)
- Requires frequent changes

**Coating Not Recommended**:
- TiN, TiAlN coatings wear off quickly in composites
- Coating can delaminate, creating rough edge
- Uncoated carbide performs better

**Application**: 
- Prototyping, low-volume production
- When diamond not justified economically

### High-Speed Steel (HSS)

**Generally Not Recommended** for composites:
- Wears extremely rapidly (5-10 holes typical)
- Softens at temperatures generated in composite cutting
- Poor surface finish

**Exception**: Very low-speed operations (hand drilling, countersinking)

## Tool Geometry for Composites

### Rake Angle

**Positive Rake** (5-15°):
- Slicing action
- Lower cutting forces
- Cleaner cut
- **Preferred for most composite machining**

**Zero to Negative Rake** (0 to -5°):
- Stronger cutting edge (less prone to chipping)
- Used for highly abrasive materials
- Higher cutting forces

**Example**: PCD router bit for carbon fiber
- Rake angle: +10°
- Reduced cutting force vs negative rake
- Cleaner fiber cutting

### Helix Angle

**Standard Helix** (30-35°):
- General purpose
- Good chip evacuation

**High Helix** (45-55°):
- Better chip evacuation
- Shearing cut (reduces force)
- **Recommended for carbon fiber**

**Low Helix** (15-25°):
- Stronger cutting edge
- Used for highly abrasive ceramics
- Not ideal for composites

### Compression Tooling

**Purpose**: Prevent delamination by compressing laminate during cutting.

**Up-Cut/Down-Cut Geometry**:
- Lower section: Up-cut flute (pushes material down)
- Upper section: Down-cut flute (pushes material down)
- Transition: At mid-thickness of material

**Effect**:
- Top surface pushed down
- Bottom surface pushed down
- Laminate compressed in middle → no delamination
- **Critical for through-cutting composites**

**Application**:
- Edge trimming of laminates
- Slotting operations
- Any through-cut where both surfaces critical

**Example**: 1/4" compression end mill for 0.125" carbon fiber
- Lower 0.100": Up-cut geometry
- Upper 0.100": Down-cut geometry
- Transition at 0.062" (mid-thickness)

### Point Angle (Drilling)

**Standard Twist Drill** (118°):
- General purpose metal drilling
- NOT ideal for composites (high thrust force)

**Low Point Angle** (90° or less):
- Reduces thrust force
- Less delamination risk
- **Preferred for composite drilling**

**Brad Point / Spur Point**:
- Outer spurs cut cleanly
- Center point provides guidance
- Excellent for composites
- **Recommended for fiberglass, carbon fiber**

**Step Drill**:
- Multiple diameters on one tool
- Pilots small hole, then enlarges
- Reduces exit delamination
- Excellent for countersinking/counterboring

### Clearance Angle

**Larger Clearance** (10-15°):
- Reduces rubbing
- Important in composites (low thermal conductivity)
- Prevents heat buildup

**Smaller Clearance** (5-7°):
- Stronger edge (for ceramics)
- Not necessary for composites

## Cutting Parameters for Composites

### Cutting Speed (Surface Speed)

**Carbon Fiber**:
- Roughing: 500-800 SFM (150-240 m/min)
- Finishing: 800-1200 SFM (240-370 m/min)
- Diamond tooling: Can run up to 2000 SFM

**Fiberglass**:
- Roughing: 400-700 SFM
- Finishing: 700-1000 SFM

**Aramid (Kevlar)**:
- Very difficult to machine (fibers don't cut, they fray)
- Low speed: 200-400 SFM
- Sharp tools mandatory

**Formula for RPM**:
$$N = \frac{12 \times SFM}{\pi \times D} = \frac{3.82 \times SFM}{D}$$

**Example**: 1/2" PCD endmill in carbon fiber at 800 SFM
$$N = \frac{3.82 \times 800}{0.5} = 6112 \text{ RPM}$$

### Feed Rate

**Feed Per Tooth**: Lower than metals (reduce cutting forces)

| Material | Feed per Tooth | Notes |
|----------|----------------|-------|
| Carbon fiber (PCD) | 0.002-0.006" | Higher for roughing |
| Carbon fiber (carbide) | 0.001-0.004" | Lower to extend life |
| Fiberglass | 0.003-0.008" | Less abrasive than carbon |
| Aramid | 0.001-0.003" | Very low to minimize fraying |

**Feed Rate Calculation**:
$$F = f_z \times Z \times N$$

**Example**: 4-flute PCD tool, 6000 RPM, $f_z$ = 0.004"
$$F = 0.004 \times 4 \times 6000 = 96 \text{ IPM}$$

**Drilling Feed Rates**:
- Carbon fiber: 2-8 IPM
- Fiberglass: 3-10 IPM
- Lower feed → lower thrust force → less delamination

### Depth of Cut

**Roughing**:
- ADOC: 0.050-0.200" (depends on material thickness)
- Full slot width: Avoid when possible (use trochoidal/adaptive)

**Finishing**:
- ADOC: 0.010-0.030"
- RDOC: 0.010-0.040" (light radial)

**Key Principle**: Multiple light passes better than single heavy pass
- Reduces cutting forces
- Minimizes delamination
- Better surface finish
- Longer tool life

**Example Strategy** (0.125" carbon fiber panel):
- Pass 1: 0.100" depth (roughing)
- Pass 2: 0.030" depth (finishing)
Total: Two passes with light finish cut

### Coolant / Lubrication

**Compressed Air**:
- Most common for composites
- Blows chips away
- Some cooling effect
- No mess, no cleanup

**Mist Coolant**:
- Better cooling than air alone
- Vegetable-based oil preferred (5-10% solution)
- Reduces dust
- Cleaner edges

**Flood Coolant**:
- Maximum cooling
- Effective dust suppression
- Water-based (no oil on carbon fiber - contamination risk)
- Matrix absorption concern (especially for honeycomb core)

**Vacuum / Dust Collection**:
- **Mandatory for health and safety**
- Carbon fiber dust carcinogenic (IARC Group 2B)
- HEPA filtration required
- Downdraft table or tool-mounted shroud

**Dry Cutting**:
- Acceptable only with excellent dust collection
- Higher tool wear
- Risk of matrix burning

**Recommendation**: Compressed air + dust collection for most applications

## Drilling Composites

### Drill Selection

**Best Choices**:
1. **PCD brad-point drill**: Sharpest, longest life, best quality
2. **Carbide brad-point**: Good quality, moderate life, lower cost
3. **Carbide twist drill** (90-100° point): Acceptable, frequent changes

**Avoid**:
- Standard HSS twist drills (wear out immediately)
- Step drills in carbon fiber (too much heat)

### Drilling Strategy

**Peck Drilling**:
- Retract frequently (every 0.5-1.0× diameter)
- Clears chips
- Reduces heat buildup
- **Mandatory for deep holes** (depth > 3× diameter)

**Pilot Hole**:
- Drill small pilot (1/4 final diameter)
- Enlarge with final drill
- Reduces thrust force on final pass
- **Significantly reduces exit delamination**

**Example**: 1/2" hole
- Pilot: 1/8" drill
- Final: 1/2" drill
- Thrust force reduced ~60% on final pass

### Backup Support

**Critical for Exit Delamination Prevention**:

**Solid Backup Plate**:
- Place rigid plate under workpiece (wood, aluminum)
- Drill through workpiece into backup
- Backup supports last ply during breakthrough
- **Most effective method**

**Sacrificial Layer**:
- Tape thin aluminum foil or plastic film to exit side
- Provides minimal support
- Better than nothing, not as good as solid backup

**Tape Method**:
- Apply packing tape to exit side
- Helps hold fibers down
- Minimal support
- Quick/easy for field repairs

**Two-Sided Drilling** (best quality):
- Drill from one side until point just breaks through
- Flip workpiece
- Drill from other side, using breakthrough as center
- Both sides are "entry" (no exit delamination)
- Time-consuming but highest quality

## Routing / Milling Composites

### Edge Trimming

**Flush Trim Bit** (bearing-guided):
- Bearing rides on template or finished edge
- Carbide or PCD cutting edge
- Up-cut, down-cut, or compression geometry

**Compression Router**:
- **Ideal for composite laminates**
- Prevents top and bottom surface delamination
- Requires tool length > material thickness

**Tabbed Parts**:
- Leave small tabs connecting part to sheet
- Route all edges leaving tabs
- Remove tabs by hand (sanding, filing)
- Prevents part from shifting during final cut

### Contouring

**Climb Milling** (down-milling):
- Cutting force pushes part onto table
- Cleaner edge (fiber cutting vs pulling)
- **Preferred for composites**
- Requires rigid fixturing

**Conventional Milling** (up-milling):
- Cutting force lifts part from table
- More fiber pullout risk
- Use only if climb milling causes vibration

**Corner Radius**:
- Composites hate sharp internal corners (stress concentration)
- Minimum radius: 2-3× material thickness
- Larger radius reduces stress concentration

### Slotting

**Full Slot Milling** (slot width = tool diameter):
- High radial engagement
- High cutting forces
- Short tool life
- Risk of delamination

**Better: Trochoidal Milling**:
- Small radial engagement (10-20% diameter)
- Circular arc paths overlapping to create slot
- Lower forces, longer tool life
- Smoother edges

**Example**: 0.500" slot with 0.500" endmill
- Traditional: Full slot, RDOC = 0.500"
- Trochoidal: Multiple passes, RDOC = 0.050-0.100" each
- 5-10× longer tool life with trochoidal

## Waterjet and Laser Cutting

### Abrasive Waterjet

**Process**: High-pressure water (40,000-90,000 PSI) + abrasive (garnet) cuts material.

**Advantages for Composites**:
- No heat (cold cutting)
- No delamination
- No tool wear
- Any shape possible
- Cuts thick laminates easily (up to 6"+)

**Disadvantages**:
- Slow (2-10 IPM typical)
- Rough edge (taper, striation marks)
- Expensive equipment ($50,000-300,000)
- Abrasive disposal/mess

**Edge Quality**:
- Kerf taper: 0.002-0.010" per inch thickness
- Surface roughness: Ra 100-300 μin (rougher than machining)
- May require post-machining for precision edges

**Applications**:
- Rough cutting blanks
- Prototyping
- One-off parts
- Thick laminates (>1")

### Laser Cutting

**CO₂ Laser** (10.6 μm wavelength):
- Absorbed well by polymer matrix
- Cuts carbon fiber, fiberglass, aramid
- Heat-affected zone (HAZ): 0.010-0.050"
- Matrix charring/burning

**Fiber Laser** (1.06 μm wavelength):
- Absorbed poorly by most polymers
- Better for metals
- Not ideal for composites

**Advantages**:
- Fast (100-500 IPM)
- Narrow kerf (0.005-0.015")
- No tool wear
- Complex shapes

**Disadvantages**:
- Heat-affected zone (matrix damage)
- Charred edges (cosmetic issue)
- Fiber ends exposed (fuzzing)
- Toxic fumes (polymer pyrolysis products)

**Applications**:
- Thin laminates (<0.125")
- Non-structural parts (cosmetic OK)
- Rapid prototyping
- When edge quality not critical

### Cutting Method Comparison

| Method | Speed | Edge Quality | Delamination Risk | Cost | Best For |
|--------|-------|--------------|-------------------|------|----------|
| CNC Routing (PCD) | Fast | Excellent | Low (if done right) | Medium | Production, precision |
| CNC Routing (carbide) | Fast | Good | Moderate | Low | Low-volume |
| Abrasive Waterjet | Slow | Fair | None | High | Thick, prototypes |
| Laser | Very Fast | Poor (HAZ) | None | High | Thin, non-structural |
| Hand Tools (diamond) | Very Slow | Fair | Moderate | Very Low | Field repairs, one-offs |

## Special Considerations

### Sandwich Structures

**Core Types**:
- Foam (PVC, PU, PMI): Soft, crushes easily
- Honeycomb (aluminum, Nomex): Hollow cells, delicate
- Balsa: Natural wood, grain direction matters

**Challenges**:
- Core crushes under clamping pressure
- Core pulls away from skin (debonding)
- Chip packing in honeycomb cells

**Drilling**:
- Use brad-point drill (prevents walking)
- Low feed rate (prevent crushing)
- Clear chips frequently (peck cycle)
- Solid backup mandatory

**Edge Routing**:
- Compression router essential
- Core exposed at edge → structural weakness
- Edge sealing required after machining

**Facing (Surfacing Core)**:
- Very light depth of cut (0.010-0.020")
- Sharp tools only
- Balsa: Cut with grain when possible

### Honeycomb Core

**Specific Issues**:
- Cells collapse under point loads
- Chips pack into cells (difficult to remove)
- Thin cell walls tear easily

**Potting Compound**:
- Fill cells with epoxy/microsphere mixture
- Cure before drilling
- Provides support during drilling
- Required for fastener holes (prevents pull-through)

**Honeycomb Router Bits**:
- Specialized geometry
- Multiple close-spaced flutes
- Shears cell walls cleanly
- PCD tipped

### Cured vs Uncured

**Green (Uncured) Machining**:
- Composite laid up but not cured
- Soft, easy to cut with conventional tools
- Allows complex features
- Must cure after machining (shrinkage, distortion risk)

**Post-Cure Machining**:
- Composite fully cured (hard)
- Requires diamond tooling
- Accurate final dimensions
- Standard practice for production parts

## Summary

Machining composites requires specialized knowledge:

**Key Principles**:
1. Sharp tools mandatory (dull tools cause delamination)
2. Diamond tooling for production (PCD primary choice)
3. Compression geometry prevents delamination
4. Climb milling preferred
5. Dust collection non-negotiable (health hazard)
6. Backup support for drilling
7. Lower cutting forces than metals (sharp tools, light cuts)

**Tool Life**: 
- PCD: 50-200× carbide
- Carbide: 10-50× HSS
- Justifies diamond tooling cost in production

**Quality Defects**:
- Delamination (most critical)
- Fiber pullout (surface finish)
- Matrix burning (heat damage)
- Fuzzing (loose fibers)

**Next**: Advanced techniques and ceramic machining strategies

---

**Next**: [17.5 Machining Ceramics - Diamond Grinding and Special Processes](section-17.5-machining-ceramics.md)
