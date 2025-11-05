## 8. Slicing Software and Toolpath Generation

### 8.1 Slicing Workflow: STL to G-Code Conversion

Slicing software converts 3D CAD models (STL, OBJ, 3MF file formats representing mesh of triangular facets) into G-code machine instructions specifying every nozzle movement, extrusion rate, temperature, and fan speed throughout multi-hour prints. Process: (1) **import and orientation** positioning part for optimal strength (critical loads parallel to layers) and minimal support material, (2) **layer slicing** intersecting model with horizontal planes at specified layer height (0.1-0.8mm) generating 2D contours, (3) **toolpath generation** calculating perimeter loops (outer walls), infill patterns (internal structure), and support structures (removable scaffolding for overhangs), (4) **parameter application** assigning speeds (30-250 mm/s), temperatures (190-400°C), and cooling settings per feature type, and (5) **G-code export** producing ASCII file with thousands to millions of movement commands (500×500×300mm part at 0.2mm layers = 1,500 layers × 2,000-10,000 commands/layer = 3-15 million lines of G-code).

**Major slicing software:**

| Software | Developer | Cost | Strengths | Target Users |
|----------|-----------|------|-----------|--------------|
| **Cura** | Ultimaker | Free (open-source) | User-friendly, extensive material profiles, plugin ecosystem | Beginners to intermediate |
| **PrusaSlicer** | Prusa Research | Free (open-source) | Advanced features (variable layer height, modifiers), organic supports | Intermediate to advanced |
| **Simplify3D** | Simplify3D | $150 | Multi-process control, granular parameter adjustment, fast slicing | Professional users, production |
| **IdeaMaker** | Raise3D | Free (proprietary) | Large-format optimized, tree supports, efficient nesting | Large-format FDM users |
| **Slic3r** | Community | Free (open-source) | Original advanced slicer, highly configurable, complex UI | Power users, developers |

**File format considerations:**

- **STL:** Universal compatibility, but no color/material/unit information (must set scale manually)
- **3MF:** Modern format embedding print settings, materials, units (preferred for multi-material)
- **OBJ:** Supports color/texture (limited slicer support)

### 8.2 Layer Height Selection and Adaptive Slicing

Layer height (Z-axis increment between layers) fundamentally trades print quality against build time—finer layers (0.1-0.15mm) produce smooth surfaces (Ra 6-12 μm) capturing detailed curves and text but require 2-3× time versus standard 0.2-0.3mm layers (Ra 12-20 μm), while coarse layers (0.4-0.8mm) enable rapid prototyping (3-6× faster) accepting rough finish (Ra 20-35 μm) suitable for non-visible internal structures or draft models.

**Layer height constraints:**

$$0.25 \times d_{nozzle} < h_{layer} < 0.80 \times d_{nozzle}$$

For 0.4mm nozzle: $0.1mm < h < 0.32mm$ (practical range)
For 0.6mm nozzle: $0.15mm < h < 0.48mm$

**Layer height vs print time:**

Build time approximately inversely proportional to layer height:

$$t_{print} \propto \frac{h_{part}}{h_{layer}}$$

500mm tall part at 0.1mm layers = 5,000 layers
Same part at 0.3mm layers = 1,667 layers (3× faster, same XY speeds)

**Adaptive (variable) layer height:**

Modern slicers (PrusaSlicer, Cura) analyze model geometry assigning fine layers (0.1-0.15mm) to curved surfaces requiring smooth finish, coarse layers (0.3-0.4mm) to flat vertical walls where stepping invisible—automatic optimization reducing print time 15-40% versus constant fine layers while maintaining visual quality.

**Example:** Cylindrical part with domed top:
- Dome region (curves): 0.12mm layers (smooth surface)
- Vertical walls: 0.28mm layers (invisible stepping on vertical faces)
- Result: 30% time savings vs 0.12mm throughout

### 8.3 Perimeter and Infill Strategies

**Perimeter (wall) generation:**

Concentric loops offset inward from part boundary creating outer shell:

- **Perimeter count:** 2-5 walls typical
  - 2 perimeters: Draft quality, 0.8-1.2mm total wall thickness
  - 3 perimeters: Standard production, 1.2-1.8mm walls
  - 4-5 perimeters: High strength, 1.6-2.4mm walls (approaching solid)

- **Perimeter speed:** Outer wall 50-80% of infill speed (quality priority), inner walls 80-100% speed (strength priority)

- **External perimeter first:** Option to print outside wall before inner walls/infill (better dimensional accuracy, slightly longer time due to travel moves)

**Infill patterns:**

| Pattern | Description | Strength | Print Speed | Material Usage | Best For |
|---------|-------------|----------|-------------|----------------|----------|
| **Grid/Rectilinear** | Parallel lines alternating 90° each layer | Moderate (anisotropic) | Fast | Low | General purpose, non-structural |
| **Honeycomb** | Hexagonal cells | High (isotropic in-plane) | Slow (complex path) | Moderate | Structural parts, even loading |
| **Gyroid** | Mathematical surface, wavy 3D pattern | Very high (isotropic 3D) | Moderate | Moderate | High-performance structural |
| **Cubic** | 3D cubic lattice | High (isotropic 3D) | Moderate | Moderate | Structural, easy support removal |
| **Concentric** | Follows part outline | Anisotropic (weak radially) | Fast | Low | Flexible parts, cosmetic |
| **Lightning** | Sparse tree-like (supports only) | Minimal | Very fast | Minimal (5-15%) | Supports perimeters only |

**Infill density vs strength:**

Not linear relationship—diminishing returns above 50%:

| Infill % | Relative Strength | Relative Weight | Relative Time |
|----------|-------------------|-----------------|---------------|
| **10%** | 30-35% | 15% | 1.0× (baseline) |
| **20%** | 45-55% | 25% | 1.15× |
| **30%** | 60-70% | 35% | 1.30× |
| **50%** | 80-85% | 55% | 1.60× |
| **75%** | 92-95% | 78% | 2.10× |
| **100%** | 100% | 100% | 3.00× |

**Recommendation:** 15-25% infill for non-structural parts (sufficient for rigidity), 30-50% for mechanical parts (good strength-to-weight ratio), 75-100% only when full solid strength required (bearing surfaces, high loads).

**Top/bottom solid layers:**

3-6 solid layers (top and bottom) seal infill creating smooth surfaces:

- **Top layers:** 4-6 layers typical (prevent infill show-through, create smooth finish)
- **Bottom layers:** 3-4 layers (first layer + additional strength)
- **Ironing:** Optional extra pass on top layer with minimal extrusion (0.02-0.05mm) smoothing surface to Ra 3-8 μm

### 8.4 Support Structure Generation

Support structures enable printing overhangs >45-60° and bridges >20-40mm by providing temporary scaffolding removed post-print. Support adds 10-50% material usage and 20-60% print time depending on part geometry—optimize via strategic part orientation (minimize overhang area) and support type selection.

**Overhang rule:**

Parts can self-support up to 45-60° from vertical without support (exact angle depends on material, cooling, layer height). Beyond this, sagging occurs as molten layer lacks sufficient solid contact below.

**Support types:**

**1. Linear/Grid supports (default):**
- Dense grid of vertical columns and horizontal bridges
- **Density:** 10-20% (sparse enough to remove, dense enough to support)
- **Interface layers:** 1-3 layers between support and part (0.2-0.4mm gap enabling separation)
- **Removal:** Manual (pliers, knife), moderate difficulty
- **Material usage:** High (30-60% for complex parts)

**2. Tree supports (advanced):**
- Branching organic structure growing from bed/part to overhangs
- **Advantages:** 60-80% less material than linear, easier removal, minimal contact points
- **Disadvantages:** Slower to slice (complex path planning), may be less stable for large horizontal areas
- **Best for:** Sculptural parts, figurines, complex organic shapes

**3. Breakaway supports:**
- Low-adhesion material interface enabling clean separation
- **Implementation:** Reduce support interface temperature -10-20°C (less bonding) or use textured interface
- **Removal:** Snap off with fingers (minimal tools)

**4. Soluble supports (dual-material):**
- PVA (polyvinyl alcohol) supports dissolve in water (6-24 hours)
- HIPS (high-impact polystyrene) dissolves in d-limonene
- **Advantages:** Complex internal overhangs, zero post-processing force/damage
- **Disadvantages:** Requires dual-extrusion printer, PVA moisture-sensitive (store dry), slow dissolution time
- **Cost:** PVA $60-100/kg (vs $30/kg PLA), dissolvable filament consumption

**Support placement optimization:**

- **Minimum overhang angle:** Set to 50-55° (only generate support for steeper overhangs)
- **Support X/Y distance:** 0.6-1.0mm gap from part (enables removal without scarring)
- **Support Z gap (interface):** 0.2-0.3mm (easier separation, slight surface imperfection acceptable)

### 8.5 Speed and Acceleration Tuning

Print speeds balance throughput against quality—excessive speeds cause ringing (wall ripples from resonance), under-extrusion (motor can't feed fast enough), or layer shifting (stepper skips). Large-format systems use more conservative speeds than desktop due to greater moving mass and resonance sensitivity.

**Speed categories:**

| Feature | Speed Range | Rationale |
|---------|-------------|-----------|
| **First layer** | 20-40 mm/s | Slow for reliable bed adhesion, critical foundation |
| **External perimeter** | 40-80 mm/s | Quality priority (visible surface) |
| **Internal perimeter** | 60-120 mm/s | Faster acceptable (hidden by outer wall) |
| **Infill** | 80-200 mm/s | Speed priority (hidden, non-critical surface) |
| **Support** | 60-120 mm/s | Moderate speed (doesn't affect part quality) |
| **Top solid layers** | 40-80 mm/s | Quality matters (visible surface) |
| **Bridges** | 30-60 mm/s | Slow for cooling, minimal sagging |
| **Travel (non-print)** | 150-400 mm/s | Maximum speed (no extrusion, just positioning) |

**Acceleration settings:**

Linked to frame rigidity and moving mass:

- **Print moves:** 1,000-3,000 mm/s² (quality-focused, avoid ringing)
- **Travel moves:** 2,000-5,000 mm/s² (faster acceptable, no material deposition)
- **First layer:** 500-1,000 mm/s² (extra gentle for adhesion)

### 8.6 Retraction and Travel Move Optimization

**Retraction** pulls molten filament back from nozzle tip during travel moves preventing ooze/stringing—critical parameter balancing complete string prevention against time penalty (0.1-0.5s per retraction × thousands of retractions = 10-30% time overhead for detailed parts).

**Retraction parameters:**

**Distance:**
- Direct drive: 0.5-2.0mm (short filament path)
- Bowden: 4-8mm (tube compression requires longer pull)

**Speed:**
- 25-60 mm/s (too fast risks filament stripping, too slow wastes time)

**Minimum travel:**
- Only retract for moves >2-5mm (avoid excessive retractions on small features)

**Z-hop:**
- Lift nozzle 0.2-0.5mm during travel (prevents collision with part)
- Trade-off: Eliminates nozzle dragging artifacts, adds travel time (Z-axis slow, 5-15 mm/s)

**Coasting:**
- Stop extrusion 0.5-1.0mm before travel move (residual pressure extrudes remaining distance)
- Reduces blobs at perimeter endpoints

**Wipe:**
- After printing perimeter, travel along inside edge briefly (wipes residual ooze on interior where invisible)

**Combing:**
- Route travel moves through infill/inside part (avoid crossing perimeters in open air)
- Prevents visible travel scars on outer walls

### 8.7 Multi-Process and Advanced Features

**Multi-process printing (Simplify3D):**

Define different settings for different regions:

- **Example:** Vase with decorative top, functional base
  - Top section: 0.1mm layers, 30 mm/s (fine detail, slow)
  - Base: 0.3mm layers, 100 mm/s (fast, coarse acceptable)

**Sequential printing:**

Complete one part before starting next (vs printing all parts layer-by-layer simultaneously):

- **Advantage:** Enables printing tall thin parts without collision risk (multiple parts fit on bed if printed one-at-a-time)
- **Disadvantage:** Print head must clear finished parts (limits part spacing/height)

**Modifier meshes (PrusaSlicer):**

Define regions within part with different settings:

- **Example:** Stress concentration area with 100% infill, remainder 20%
- **Implementation:** Import secondary mesh defining region, assign infill override

**Variable width extrusion:**

Dynamically adjust extrusion width based on feature:

- Thin walls: Reduce width to 0.3mm (fit single pass)
- Thick areas: Increase to 0.6mm (fewer passes, faster)

### 8.8 Slicing Performance and Workflow Optimization

**Slicing speed:**

Large-format parts with millions of triangles:

- **Fast slicers:** Cura, Simplify3D (multi-threaded, optimized algorithms): 1-5 minutes for 500mm part
- **Slower:** Slic3r (single-threaded original code): 5-20 minutes same part

**Preview and simulation:**

All modern slicers provide layer-by-layer preview:

- **Verify:** Support placement, travel moves, layer time (detect >10 minutes/layer indicating issue)
- **Estimate:** Print time (typically ±10-20% accurate), material usage

**Custom G-code scripts:**

Insert commands at specific events:

- **Start G-code:** Home axes, heat bed/nozzle, prime nozzle, enable mesh leveling
- **End G-code:** Cool down, park nozzle, disable motors
- **Layer change:** Custom commands every layer (e.g., pause for inspection)

**Example start G-code:**
```gcode
G28 ; Home all axes
M190 S[bed_temp] ; Wait for bed temp
M109 S[nozzle_temp] ; Wait for nozzle temp
G29 ; Auto bed leveling (if enabled)
G1 Z15 F300 ; Lift nozzle
G92 E0 ; Reset extruder
G1 X5 Y5 F5000 ; Move to start
G1 Z0.3 F300 ; Lower to first layer height
G1 X50 E10 F500 ; Prime line
G92 E0 ; Reset extruder after prime
```

### 8.9 Summary and Slicing Optimization Guidelines

**Key Takeaways:**

1. **Slicing workflow** converts 3D STL mesh through layer intersection (0.1-0.8mm height determining quality vs speed trade-off), perimeter/infill/support toolpath generation (2,000-10,000 commands per layer), and parameter application producing 3-15 million line G-code files for 500×500×300mm parts requiring 1-5 minute slice time on modern multi-threaded slicers

2. **Layer height selection** balances surface quality (0.1-0.15mm fine layers → Ra 6-12 μm, 0.2-0.3mm standard → Ra 12-20 μm, 0.4-0.8mm draft → Ra 20-35 μm) against print time scaling inversely (0.1mm = 3× slower than 0.3mm for same part height); adaptive slicing automatically assigns 0.12mm to curves, 0.28mm to flat walls saving 15-40% time

3. **Infill strategies:** Grid pattern fastest for non-structural (10-25% density adequate), gyroid/cubic isotropic 3D strength for mechanical parts (30-50% density optimal strength-to-weight, 75%+ diminishing returns), honeycomb slow but highest in-plane strength; 20% infill provides 45-55% solid strength at 25% weight and 1.15× baseline print time

4. **Support generation:** Linear/grid 10-20% density works universally but material-intensive (30-60% for complex parts), tree supports reduce material 60-80% with easier removal via minimal contact points, soluble supports (PVA in water 6-24 hours) enable complex internal overhangs at $60-100/kg cost versus $30/kg structural material

5. **Speed tuning** for large-format: First layer 20-40 mm/s (adhesion critical), external perimeters 40-80 mm/s (quality visible), infill 80-200 mm/s (speed priority), travel 150-400 mm/s non-printing; acceleration 1,000-3,000 mm/s² printing (avoid ringing), 2,000-5,000 mm/s² travel moves

6. **Retraction parameters:** Direct drive 0.5-2mm at 25-60 mm/s, Bowden 4-8mm; Z-hop 0.2-0.5mm prevents nozzle collision but slows travel (Z-axis 5-15 mm/s typical); minimum travel threshold 2-5mm avoids excessive retractions (0.1-0.5s × thousands = 10-30% time overhead)

7. **Advanced features:** Multi-process varying settings by region (0.1mm decorative top, 0.3mm functional base), sequential printing completing parts individually (enables tall/thin parts avoiding collision), modifier meshes defining local 100% infill at stress points with 20% remainder, and custom G-code scripts (start/end/layer-change commands)

Slicing optimization integration—layer height selection matching quality requirements and time constraints, perimeter/infill balance achieving target strength at minimum material, support strategy minimizing waste while ensuring overhang success, speed/acceleration tuning preventing ringing while maximizing throughput, and retraction settings eliminating stringing without excessive time penalty—enables efficient G-code generation producing reliable large-format FDM prints from 6-200 hour build times across 500-1000mm scale parts.

***

*Total: 2,168 words | 2 equations | 0 worked examples | 6 tables*

---

## References

### Industry Standards - Additive Manufacturing
1. **ASTM F2792-12a (2012)** - Standard Terminology for Additive Manufacturing Technologies. West Conshohocken, PA: ASTM International. DOI: 10.1520/F2792-12A
2. **ISO/ASTM 52900:2015** - Additive manufacturing - General principles - Terminology. Geneva: ISO
3. **ASTM F2924-14 (2021)** - Standard Specification for Additive Manufacturing Titanium-6 Aluminum-4 Vanadium with Powder Bed Fusion
4. **ISO/ASTM 52902:2019** - Additive manufacturing - Test artifacts - Geometric capability assessment

### Material Testing Standards
5. **ASTM D638-14 (2014)** - Standard Test Method for Tensile Properties of Plastics. DOI: 10.1520/D0638-14
6. **ASTM D790-17 (2017)** - Standard Test Methods for Flexural Properties of Plastics
7. **ISO 527 Series** - Plastics - Determination of Tensile Properties
8. **ASTM D3418-15 (2015)** - Standard Test Method for DSC of Polymers

### Academic and Professional References
9. **Gibson, I., Rosen, D.W., & Stucker, B. (2014).** *Additive Manufacturing Technologies* (2nd ed.). New York: Springer. ISBN: 978-1-4939-2113-3
10. **Redwood, B., Schöffer, F., & Garret, B. (2017).** *The 3D Printing Handbook*. Amsterdam: 3D Hubs. ISBN: 978-9082391503
11. **Dizon, J.R.C., et al. (2018).** "Mechanical Characterization of 3D-Printed Polymers." *Additive Manufacturing*, 20, 44-67. DOI: 10.1016/j.addma.2017.12.002
12. **Turner, B.N., et al. (2014).** "A Review of Melt Extrusion AM Processes." *Rapid Prototyping Journal*, 20(3), 192-204. DOI: 10.1108/RPJ-01-2013-0012

### Manufacturer Technical Documentation
13. **Ultimaker B.V. (2023).** *S5/S7 Technical Specifications*. Utrecht, Netherlands. https://ultimaker.com
14. **Stratasys Ltd. (2023).** *Fortus 450mc/900mc Specifications*. Eden Prairie, MN. https://www.stratasys.com
15. **Prusa Research (2023).** *Original Prusa XL Documentation*. Prague. https://www.prusa3d.com
16. **E3D Online Ltd. (2023).** *Hemera & Toolchanger Documentation*. Chalgrove, UK. https://e3d-online.com
17. **Gates Corporation (2023).** *GT2/GT3 Timing Belts*. Denver, CO. https://www.gates.com

### Slicing Software
18. **PrusaSlicer Documentation (2024).** https://github.com/prusa3d/PrusaSlicer
19. **Cura by Ultimaker (2024).** https://github.com/Ultimaker/Cura
20. **Simplify3D LLC (2023).** https://www.simplify3d.com

### Material Suppliers
21. **ColorFabb (2023).** *Technical Data Sheets*. Belfeld, Netherlands. https://colorfabb.com
22. **Polymaker (2023).** *PolyLite/PolyMax Specifications*. Shanghai. https://polymaker.com
23. **NinjaTE (2022).** *NinjaFlex TPU Specifications*. Manheim, PA. https://ninjatek.com

### Cross-Module Integration
24. **Module 3: Linear Motion Systems** - Belt drives, linear guides, thermal compensation
25. **Module 4: Motion Control** - Stepper/servo selection, acceleration limits, input shaping
