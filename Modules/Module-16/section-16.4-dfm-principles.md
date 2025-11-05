# Section 16.4: Design for Manufacturability (DFM) Principles

## Introduction

Design for Manufacturability (DFM) is the practice of designing parts to be easy, economical, and reliable to manufacture. Good DFM doesn't mean sacrificing performance—it means achieving required performance through the most efficient manufacturing methods. Every design decision has a manufacturing cost: complex geometry requires more machine time, tight tolerances demand precision tooling, and custom features necessitate specialized equipment.

This section establishes universal DFM principles applicable across all CNC processes, with process-specific details covered in Section 16.7.

## The DFM Mindset

**DFM is about asking "how will this be made?" WHILE you design, not after.**

The best DFM engineers mentally simulate the manufacturing process as they add features. They see the cutting tool, the fixturing, the measurement tools—not just the finished geometry.

### Think Like a Machinist

Before finalizing any design, run through these questions:

**1. How will this be made?**

Let's see how this thinking transforms a simple design decision:

**Scenario:** Adding a 20mm deep pocket to a part.

**Amateur Designer:**
- Draws 20mm deep pocket
- Moves on to next feature

**DFM-Aware Designer:**
- "20mm deep pocket... what tool diameter can I use?"
- "If I use 6mm endmill, depth-to-diameter ratio = 20/6 = 3.3× (acceptable)"
- "But 10mm endmill would be more rigid (ratio = 2×), cut faster"
- "Can I widen the pocket to 15mm minimum to allow 10mm tool? Let me check if function allows..."
- [Checks loads, clearances]
- "Yes, can widen to 16mm. Now I can use 10mm tool = faster cutting, better finish, lower cost"

**Time spent thinking: 2 minutes. Cost savings: 30% faster machining.**

***

**2. What can go wrong?**

**Real Example - Thin-Wall Part:**

Designer creates a part with 1.5mm walls in aluminum.

**Questions to ask:**
- "Will thin walls deflect under cutting forces?"
  - YES → Poor dimensional accuracy, surface finish
- "Can walls be thicker?"
  - Check loads: 2.5mm walls provide same strength with safety margin
- "If walls must be thin, what's the mitigation?"
  - Leave extra stock (3mm walls), machine to final 1.5mm in light finishing pass
  - Add temporary support structures (tabs), remove after machining

**Result:** Part actually works, instead of scrapping 10 pieces before figuring out the problem.

***

**3. How can this be simplified?**

**Real Example - Cable Management Bracket:**

**Initial Design:**
- Curved mounting surface (matches curved enclosure perfectly)
- Custom radius: 127mm (exact radius of enclosure)
- Requires 3D ball-endmill surfacing = 45 minutes machine time

**Simplified Design:**
- Flat mounting surface with 3 contact points (edge + 2 bosses)
- Only bosses match curve (small features = fast to machine)
- Contact area 90% same, stress distribution identical (FEA verified)
- Machining time: 8 minutes

**Key insight:** Perfect form-fit isn't always required. Three points define a plane—often enough for mounting.

### The Cost Hierarchy of Manufacturing Features

**Understanding this hierarchy is the SECRET to low-cost design.**

Every feature you add falls somewhere on this cost ladder. DFM is about climbing DOWN the ladder whenever possible.

**From cheapest to most expensive:**

**1. No feature at all (Cost: $0)**
   - Best feature is one you design out entirely
   - **Example:** "Do we really need that lightening pocket? Part is only 50g, weight isn't critical here."
   - **Savings:** If you don't make it, it costs nothing

**2. Standard feature with standard tooling (Cost: 1× baseline)**
   - Drilled hole with standard drill bit
   - Chamfer with standard 45° chamfer mill
   - Square pocket with standard endmill
   - **Example:** ⌀8mm drilled hole (standard 8mm drill bit)
   - **Cost:** Fast, cheap, every shop has these tools

**3. Standard feature with custom size (Cost: 1.5-2×)**
   - Reamed hole to precise diameter (drill, then ream)
   - Tapped hole (drill, tap)
   - **Example:** ⌀8mm hole reamed to ⌀8.00 H7 (precision fit)
   - **Cost:** Extra operation (reaming after drilling), but still standard tools

**4. Custom feature with standard tooling (Cost: 2-3×)**
   - Complex organic pocket (requires long toolpath, multiple passes)
   - Non-standard geometry requiring many tool changes
   - **Example:** Curved pocket with varying depth (sculptured surface)
   - **Cost:** Standard endmill, but LONG cycle time (complex programming, many passes)

**5. Custom feature requiring specialized tooling (Cost: 4-6×)**
   - T-slot (requires T-slot cutter)
   - Dovetail (requires dovetail cutter)
   - Woodruff key seat (requires Woodruff cutter)
   - **Example:** T-slot for workholding clamps
   - **Cost:** Special tool purchase ($50-200), tool setup, limited cutting speeds

**6. Feature requiring multi-axis machining (Cost: 5-10×)**
   - Compound angle holes (3+2 or 5-axis)
   - Complex sculptured surfaces (5-axis continuous)
   - **Example:** Angled hole through curved surface
   - **Cost:** Requires 5-axis machine ($500k+ vs $50k for 3-axis), specialized programming, longer setup

**7. Feature requiring secondary operations (Cost: 3-8×)**
   - Hand deburring (every edge = labor time)
   - Manual polishing
   - Assembly of sub-components
   - **Example:** Mirror-polished surface (machine, then hand-polish for hours)
   - **Cost:** Labor-intensive, non-automated, inconsistent results

**8. Feature requiring outside processing (Cost: 10-20×)**
   - EDM (electrical discharge machining for sharp corners, hard materials)
   - Heat treatment (hardening, stress relief)
   - Special coatings (anodizing, electroplating)
   - **Example:** Sharp internal corner (requires EDM)
   - **Cost:** Ship to vendor, wait in queue, ship back, quality issues = expensive, slow

***

**Real-World Example: Feature Cost Comparison**

Let's design a mounting bracket with 4 holes. Watch how hole spec affects cost:

| Feature Specification | Cost Category | Machining Operation | Time per Part | Cost per Part |
|----------------------|---------------|-------------------|---------------|---------------|
| ⌀8.5mm drilled holes (clearance) | Category 2 | Drill 4 holes | 2 minutes | $5 (baseline) |
| ⌀8.0mm reamed holes (precision) | Category 3 | Drill ⌀7.8 + ream ⌀8.0 | 6 minutes | $12 |
| ⌀8.0mm holes, positioned ±0.01mm | Category 6 | Drill + ream on CNC mill with precision fixturing | 15 minutes | $35 |
| ⌀8.0mm holes, mirror finish inside | Category 7 | Drill + ream + hand-hone each hole | 45 minutes | $95 |

**Same bracket, different hole specs: $5 vs $95 per part (19× cost difference!)**

**Question to ask:** "Does our application really need precision-positioned, mirror-finished holes? Or will clearance holes work?"

**Answer 90% of the time:** Clearance holes work fine.

**DFM Goal:** Keep features in categories 1-3 whenever possible. Categories 4-8 should require written justification (performance data, analysis, or customer spec).

## Universal DFM Principles

### 1. Minimize Part Count

**Every part adds cost:**
- Design time
- Drawing creation
- BOM line item
- Inventory management
- Quality inspection
- Assembly labor
- Potential failure point

**Strategies:**
- Combine multiple parts into single machined piece when practical
- Use common parts across product line
- Eliminate purely cosmetic components
- Consider multi-body design (weldment instead of bolted assembly)

**Example:**
```
Before DFM: Sensor bracket assembly
  - Mounting plate (milled)
  - Vertical riser (milled)
  - Angle bracket (purchased)
  - 6x M4 screws
  - 6x M4 nuts
  Total: 14 parts

After DFM: Single bent sheet metal bracket
  - One part (laser cut + bent)
  Total: 1 part
```

**Result:** 93% reduction in part count, eliminated machining, reduced assembly time.

### 2. Design for Standard Tooling

**Standard tools are:**
- Readily available
- Inexpensive
- Well-documented (feeds, speeds, tool life)
- Stocked by most machine shops

**Common standard tools:**

| Feature | Standard Tool | Sizes |
|---------|---------------|-------|
| Holes | Twist drills | Fractional, metric, number, letter |
| Counterbores | Counterbore tools | Match socket head cap screw sizes |
| Countersinks | 82° or 90° countersinks | Various diameters |
| Threads | Taps (manual/CNC) | Standard thread pitches |
| Pockets | Square endmills | 1/16" to 1" (metric equivalents) |
| Fillets | Ball endmills, radius endmills | Standard radii (1/16", 1/8", 1/4", etc.) |
| Chamfers | Chamfer mills | 45°, 60°, 82°, 90° |

**DFM Rules:**
- **Internal corners:** Radius ≥ smallest available endmill radius (typically 1.5mm / 1/16")
- **Holes:** Use standard drill sizes; avoid fractional millimeters (6.5mm okay, 6.3mm less common)
- **Threads:** Use standard pitches (M6×1.0, not M6×0.9)
- **Fillets:** Use tool radii (3mm, 6mm, 10mm) rather than arbitrary values (3.7mm)

**Poor DFM Example:**
```
Internal pocket with 0.5mm corner radii
→ Requires custom 1mm endmill
→ Tool fragile, expensive, slow cutting
→ High tool wear, frequent breakage
```

**Good DFM Example:**
```
Internal pocket with 1.5mm corner radii
→ Uses standard 3mm endmill
→ Robust tool, fast cutting, long life
→ Low cost, reliable process
```

### 3. Minimize Setups and Operations

**Every time you flip, rotate, or reposition a part, you pay for it.**

Each setup introduces:
- **Setup time:** 10-30 minutes to fixture, probe, indicate part (even if cutting takes 2 minutes!)
- **Datum shift errors:** Every repositioning = new reference, new chance for error
- **Potential misalignment:** Multi-setup tolerances stack up (±0.05mm per setup)
- **Labor cost:** Machinist must manually load, indicate, verify each setup

**Real Cost Example:**

Part requires 3 setups:
- Setup 1: 20 min setup + 5 min machining
- Setup 2: 20 min setup + 3 min machining
- Setup 3: 15 min setup + 2 min machining
- **Total: 55 min setup + 10 min cutting = 65 min total**

Same part redesigned for 1 setup:
- Setup 1: 20 min setup + 12 min machining
- **Total: 32 min**

**Cost savings: 51% reduction in cycle time, just from reducing setups!**

***

**Single-Setup Design Features:**

**✓ All critical features accessible from one direction**
```
Example: Motor mount plate
- All mounting holes drilled from top
- All pockets machined from top
- Bottom surface left as-sawn (doesn't need machining)
Result: 1 setup, part held in vise, done in 15 minutes
```

**✓ Symmetric parts (can flip and maintain datums)**
```
Example: Adapter plate (identical top/bottom)
- Machine top features in Setup 1
- Flip using same fixture, bottom features identical
- No re-indicating needed (symmetric datums)
Result: 2 setups, but second setup takes 2 minutes (fast flip)
```

**✓ Features designed for standard vise/fixture holding**
```
✓ Flat parallel surfaces for vise jaws
✓ Through-holes for fixture pins (repeatable location)
✓ Edges accessible (vise doesn't block tool)

❌ Curved gripping surfaces (custom soft jaws required)
❌ Features on all 6 sides (requires tombstone fixture)
❌ Undercuts that block standard clamping
```

***

**Multi-Setup Considerations (When Unavoidable):**

**Provide locating features for repeatable second-setup alignment:**

**Poor approach:**
```
Setup 1: Machine top features
Setup 2: Flip part, eyeball alignment, clamp, hope for the best
Result: ±0.5mm misalignment between setups
```

**Professional approach:**
```
Setup 1: Machine top features + two precision dowel pin holes
Setup 2: Flip part onto fixture with matching dowel pins
Result: ±0.01mm repeatable alignment between setups
```

**Real Example - Two-Sided Bracket:**

**Design includes:**
- Two ⌀6mm holes on top (Setup 1)
- Precision pocket on bottom (Setup 2)

**How to ensure alignment:**
1. **Setup 1 operations:**
   - Mill top surface (datum A)
   - Drill two ⌀6mm holes with ±0.02mm position tolerance
   - These become alignment features for Setup 2

2. **Setup 2 operations:**
   - Flip part onto fixture with ⌀6mm alignment pins (matching hole pattern)
   - Part now located precisely relative to Setup 1 datums
   - Machine bottom pocket with guaranteed alignment to top holes

**Key principle:** First setup creates precision features that locate second setup.

***

**Example: Milled Block**

**Poor DFM (3 setups = 65 minutes):**
```
Setup 1: Mount in vise (jaws on sides)
  - Top face milling (5 min)
  - Top holes drilled (3 min)
  - Setup time: 20 min

Setup 2: Flip part upside down
  - Bottom face milling (4 min)
  - Bottom holes drilled (2 min)
  - Setup time: 20 min

Setup 3: Stand part on end (90° rotation, custom fixture)
  - Side pockets machined (2 min)
  - Setup time: 15 min

Total: 55 min setup + 16 min cutting = 71 min
Cost at $60/hr shop rate = $71
```

**Good DFM (1 setup = 30 minutes):**
```
Setup 1: Mount in vise (jaws on finished ends)
  - Top face milling (5 min)
  - All holes drilled from top (4 min)
  - Side pockets machined with extended-length endmill (3 min)
  - Bottom face left as-sawn (adequate surface finish)
  - Setup time: 20 min

Total: 20 min setup + 12 min cutting = 32 min
Cost at $60/hr shop rate = $32

Savings: $39 per part (55% cost reduction!)
```

**Design changes that enabled 1-setup:**
- Bottom surface spec changed to "as-sawn" (function allows this)
- Side pocket depth reduced from 25mm to 18mm (allows standard-length tool to reach from top)
- Bottom holes eliminated (redesigned to use through-holes from top with nuts on bottom)

**Key insight:** Small design changes (that don't affect function) = massive manufacturing savings.

### 4. Design for Material Removal Efficiency

**Material removal rate (MRR) drives cycle time:**
```
MRR = Width of Cut × Depth of Cut × Feed Rate
```

**DFM strategies to maximize MRR:**

**Large Pockets:**
- Allow large diameter roughing tools
- Minimize depth (deep pockets require slow, multiple passes)
- Avoid thin floors (can flex, require light cuts)

**Holes:**
- Use drilling instead of milling when possible (faster)
- Through holes faster than blind holes (no dwell, easier chip evacuation)
- Larger holes can use circle milling if no standard drill available

**Thin Walls:**
- Avoid when possible (slow cutting to prevent deflection)
- If required, provide temporary support structures (design to be removed in secondary op)

### 5. Tolerance Only What Matters

**Tolerances cost money:**

| Tolerance Range | Relative Cost | Typical Process |
|-----------------|---------------|-----------------|
| ±0.5 mm | 1× (baseline) | Sawing, plasma cutting |
| ±0.1 mm | 1.5× | Standard milling, turning |
| ±0.05 mm | 2× | Careful milling, ground surfaces |
| ±0.01 mm | 4× | Precision grinding, wire EDM |
| ±0.005 mm | 8× | Cylindrical grinding, lapping |
| ±0.001 mm | 16× | Ultra-precision machining |

**DFM approach:**
- **Identify critical dimensions:** What affects fit, function, safety?
- **Apply appropriate tolerance:** Match process capability to requirement
- **Leave non-critical dimensions as standard tolerance:** Reduces cost, simplifies inspection

**Example: Motor mount plate**
```
Critical dimensions (tight tolerance):
  - Motor bolt pattern: ±0.05 mm (must align with motor)
  - Central shaft hole: +0.02/0 mm (shaft clearance)

Non-critical dimensions (standard tolerance):
  - Overall plate size: ±0.5 mm (cosmetic, no functional impact)
  - Mounting hole positions: ±0.2 mm (slots or clearance holes)
```

**Rule of thumb:** If it doesn't mate with another part or affect performance, it doesn't need a tight tolerance.

### 6. Avoid Undercuts and Re-Entrant Features

**Undercut:** Feature that cannot be accessed without tool interference or part repositioning.

**Common undercuts:**
- Internal threads longer than thread relief allows
- Grooves on inner diameter without through-bore access
- Pockets under overhanging surfaces

**DFM solutions:**
- **Redesign to eliminate:** Extend pocket to edge, remove overhang
- **Split part:** Two-piece design, assemble after machining
- **Accept secondary operation:** Manual deburring, EDM, etc.

**Example:**
```
Poor DFM: T-slot fully enclosed in block
  → Requires specialized broaching or EDM
  → Expensive, slow, specialized equipment

Good DFM: T-slot open on one side
  → Standard T-slot cutter from side entry
  → Fast, inexpensive, standard process
```

### 7. Design for Adequate Rigidity

**Part deflection during machining causes:**
- Dimensional inaccuracy
- Poor surface finish
- Tool breakage
- Scrapped parts

**DFM strategies:**

**Ribs and Gussets:**
```
Thin plate alone: flexible, chatters
Thin plate + ribs: rigid, machines well
```

**Appropriate Wall Thickness:**
```
Minimum wall thickness guidelines:
  Aluminum: 1.5 mm (thin-wall), 3 mm (standard)
  Steel: 2 mm (thin-wall), 5 mm (standard)
  Plastic: 2 mm (thin-wall), 4 mm (standard)
```

**Closed Sections:**
```
Open channel: low torsional rigidity
Closed tube: high torsional rigidity (4×-10× stiffer)
```

**Proper Fixturing Design:**
- Provide clamping surfaces parallel to cutting forces
- Avoid long unsupported spans
- Design-in fixture contact points

### 8. Specify Appropriate Surface Finish

Surface finish impacts both function and cost:

| Finish | Ra (µm) | Process | Relative Cost | Applications |
|--------|---------|---------|---------------|--------------|
| Rough | 6.3-12.5 | As-sawn, plasma cut | 1× | Non-contact surfaces |
| Machined | 1.6-3.2 | Standard milling/turning | 1.5× | General machined parts |
| Fine | 0.8-1.6 | Finish milling, grinding | 3× | Sliding surfaces, seals |
| Precision | 0.2-0.8 | Grinding, honing | 6× | Bearing surfaces, hydraulic seals |
| Mirror | <0.2 | Polishing, lapping | 10×+ | Optical surfaces, mating faces |

**DFM approach:**
- Specify finish only where needed (sealing surfaces, bearing journals, aesthetic faces)
- Leave non-critical surfaces as-machined
- Avoid specifying "mirror finish" unless truly required

### 9. Use Chamfers Instead of Fillets (External Edges)

**External edges:**

**Chamfers:**
- Faster to machine (single-pass with chamfer mill)
- Easier to program
- Removes burrs in same operation
- Good for assembly (lead-in for mating parts)

**Fillets:**
- Require ball endmill or radius tool
- Multiple passes for large radii
- Slower cycle time
- Better for stress concentration reduction

**DFM rule:** Use chamfers for assembly edges, fillets only where stress relief required.

**Internal corners (pockets):**
Always have radius (cannot have sharp corner with rotating tool). Radius = tool radius minimum.

### 10. Design for Inspection and Quality Control

**Inspectable features:**
- Accessible to measurement tools (calipers, micrometers, CMM probes)
- Clear datums for measurement reference
- Critical dimensions easy to verify

**Avoid:**
- Features measurable only with specialized gauges
- Dimensions requiring complex trigonometry to verify
- Internal features impossible to inspect without destructive testing

**DFM aids for inspection:**
- Provide datum surfaces (flat, perpendicular reference planes)
- Include witness marks or measurement reference points
- Design-in gauge access (clearance for probe, caliper jaws)

## DFM Optimization Workflow

### Step 1: Functional Requirements Analysis

Document what the part **must** do:
- Load bearing: What forces, moments, deflection limits?
- Interface: What parts mate with it? What tolerances required?
- Environment: Temperature, corrosion, wear resistance?
- Lifecycle: One-off prototype vs. production quantities?

### Step 2: Initial Design (Function-Focused)

Create design that meets functional requirements without worrying about manufacturing yet.

### Step 3: DFM Review

Systematically review design against DFM principles:

**Checklist:**
- [ ] All internal corners have adequate radii for standard tools?
- [ ] Features accessible from minimal setups?
- [ ] Tolerances appropriate for function (not over-specified)?
- [ ] Materials readily available in required form/size?
- [ ] Surface finish specified only where required?
- [ ] Part can be securely fixtured?
- [ ] No undercuts or features requiring special tooling?
- [ ] Hole sizes match standard drills/reamers?
- [ ] Thread sizes/pitches are standard?

### Step 4: Design Optimization

**Iterate to improve manufacturability:**
- Increase corner radii where possible
- Reduce pocket depths
- Relax non-critical tolerances
- Combine features to reduce setups
- Replace complex geometry with simpler approximations

### Step 5: Manufacturing Process Selection

Choose processes based on:
- Geometry (2D profile → plasma/laser; 3D features → milling)
- Material (plastic → FDM; metal → machining)
- Quantity (prototype → 3D print; production → casting/machining)
- Tolerance (loose → plasma; tight → milling/grinding)
- Surface finish (rough → waterjet; smooth → milling)

### Step 6: Prototype and Refine

- Build physical prototype
- Gather manufacturing feedback
- Measure actual vs. intended results
- Iterate design based on lessons learned

## Practical Example: Bracket Optimization

### Initial Design (Function-Focused)

**Requirements:**
- Supports 50 kg load at 200 mm cantilever
- Mounts to 80/20 extrusion (8mm slot)
- Provides M8 threaded mounting point for payload

**Initial CAD:**
```
- 10mm thick aluminum plate, 80mm × 100mm
- Complex curved reinforcement ribs
- Custom 7.2mm holes for 80/20 mounting (tight fit)
- M8 threaded hole tapped perpendicular to main surface
- Radiused corners (arbitrary 4.7mm radius)
- Polished finish specified on all surfaces
```

**Manufacturing assessment:**
- Curved ribs require 3D surfacing (slow)
- 7.2mm holes require reaming (extra operation)
- Tapped hole orientation difficult to fixture
- 4.7mm radius requires custom tool
- Polished finish adds 200% cost

### DFM-Optimized Design

**Optimizations applied:**

1. **Simplified ribs:** Straight diagonal ribs (2D profile extrude) instead of curved
2. **Standard holes:** 8.5mm clearance holes (standard drill) instead of 7.2mm reamed
3. **Hole orientation:** Thru-holes with nuts instead of tapped holes (easier access)
4. **Standard radius:** 5mm corner radius (standard 10mm ball endmill)
5. **Finish:** As-machined on non-visible surfaces, chamfer edges instead of polish
6. **Material optimization:** FEA shows 8mm plate sufficient; reduce from 10mm

**Results:**
- Machining time: 45 min → 15 min (67% reduction)
- Tool changes: 8 → 4 (simpler program)
- Material cost: 10% reduction (thinner plate)
- Cycle time per part: 3× faster
- **Total cost reduction: 55%**
- Still meets all functional requirements (FEA verified)

### Key DFM Changes Summary

| Aspect | Before DFM | After DFM | Benefit |
|--------|-----------|-----------|---------|
| Ribs | Curved 3D surfaces | Straight 2D extrudes | Simpler toolpaths |
| Holes | 7.2mm reamed | 8.5mm drilled | Eliminated reaming op |
| Threads | Tapped M8 | Through-holes + nuts | Easier fixturing |
| Corners | 4.7mm radius | 5mm radius | Standard tool |
| Finish | Polished | As-machined + chamfer | Eliminated polishing |
| Material | 10mm plate | 8mm plate | Reduced cost, weight |

## Common DFM Mistakes and Solutions

### Mistake 1: Over-Engineering for "Future Flexibility"

**Problem:**
Adding features "just in case" they're needed later increases cost now with uncertain future benefit.

**Solution:**
Design for current requirements. Modern CAD makes revisions easy if needs change.

### Mistake 2: Copying Consumer Product Aesthetics

**Problem:**
Consumer products often use molding/stamping processes that create shapes difficult/expensive to machine.

**Solution:**
Embrace machined aesthetic (clean lines, chamfered edges, visible tooling marks on non-critical surfaces).

### Mistake 3: Ignoring Material Stock Sizes

**Problem:**
Designing 65mm wide part when stock comes in 50mm or 75mm widths wastes material.

**Solution:**
Check material supplier catalogs during design phase; adjust dimensions to minimize waste.

### Mistake 4: Specifying Impossible Tolerances

**Problem:**
Specifying ±0.01mm on large plastic part (plastic moves ±0.5mm with temperature/humidity changes).

**Solution:**
Understand material behavior and process capability; specify tolerances achievable and meaningful.

### Mistake 5: Designing in a Vacuum

**Problem:**
Not consulting with machinists, suppliers, or manufacturing engineers until design is "final."

**Solution:**
Early involvement of manufacturing expertise prevents costly redesigns.

## DFM Resources and Tools

### Software Tools

**DFM Analysis Built into CAD:**
- SolidWorks DFMXpress: Automated DFM checks
- Fusion 360 Manufacture workspace: Toolpath simulation reveals issues
- FreeCAD Path workbench: Visualize machining operations

**Standalone DFM Tools:**
- DFMPro: Comprehensive DFM analysis plugin
- aPriori: Cost estimation and DFM feedback

### Knowledge Resources

**Machinist's Handbooks:**
- Machinery's Handbook (comprehensive reference)
- CNC Machining Handbook (DFM-focused)

**Online Resources:**
- Protolabs Design Tips (free guides for various processes)
- SendCutSend Design Guide (sheet metal DFM)
- Xometry Design Guide (multi-process DFM)

**Supplier Capabilities:**
Most machine shops publish capability charts:
- Minimum feature sizes
- Tolerance capabilities
- Standard materials/stock sizes
- Available tooling

**Use these during design to ensure compatibility.**

## Summary

DFM is not about compromising design quality—it's about achieving required performance through efficient manufacturing methods:

1. **Minimize part count** and complexity
2. **Design for standard tooling** (corner radii, hole sizes, thread pitches)
3. **Minimize setups** (single-setup designs when possible)
4. **Maximize material removal efficiency** (pockets, holes, wall thickness)
5. **Tolerance only critical features** (cost increases exponentially with precision)
6. **Avoid undercuts** and inaccessible features
7. **Design for rigidity** (ribs, appropriate wall thickness)
8. **Specify surface finish** only where needed
9. **Prefer chamfers** over fillets (external edges)
10. **Design for inspection** (accessible, measurable features)

**Next section** covers how to properly specify tolerances and use GD&T to communicate design intent unambiguously.

***

**Next:** [Section 16.5: Tolerancing and GD&T](section-16.5-tolerancing-gdt.md)

**Previous:** [Section 16.3: Parametric Modeling](section-16.3-parametric-modeling.md)
