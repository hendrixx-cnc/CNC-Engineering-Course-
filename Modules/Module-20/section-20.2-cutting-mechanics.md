# 20.2 Cutting Mechanics and Tool Geometry

## Chip Formation Process

### Orthogonal Cutting Model

**Simplified 2D Model**: Single cutting edge perpendicular to cutting direction.

**Cutting Zones**:

**Zone 1 - Primary Shear Zone**:
- Material deforms plastically ahead of tool
- Chip forms by shearing along shear plane
- Angle φ (phi) = shear angle

**Zone 2 - Secondary Shear Zone**:
- Friction between chip and tool rake face
- Additional heat generation
- Affects chip curl and evacuation

**Zone 3 - Tertiary Zone**:
- Rubbing between tool flank and workpiece
- Generates finished surface
- Wear on tool flank face

### Shear Plane Angle

**Merchant's Equation**:
$$\phi = 45° + \frac{\alpha}{2} - \frac{\beta}{2}$$

where:
- φ = shear angle
- α (alpha) = rake angle (tool geometry)
- β (beta) = friction angle at tool-chip interface

**Key Insight**: Higher rake angle → higher shear angle → less deformation → lower cutting forces and heat.

**Example**:
- Rake angle α = 10°
- Friction angle β = 30° (typical for steel)
- φ = 45° + 5° - 15° = 35°

Lower friction (better lubrication): β = 20°
- φ = 45° + 5° - 10° = 40° (less deformation, easier cutting)

### Chip Types

**Continuous Chip**:
- Smooth, ribbon-like chip
- Ductile materials (low carbon steel, aluminum)
- Sharp tool, high speed, positive rake
- Good surface finish
- Problem: Long chips tangle

**Discontinuous Chip**:
- Segmented, broken chips
- Brittle materials (cast iron, brass)
- Low speed, negative rake, or built-up edge
- Poor surface finish
- Advantage: Easy chip removal

**Continuous with Built-Up Edge (BUE)**:
- Material welds to cutting edge
- Periodic detachment degrades finish
- Occurs at moderate speeds with steel
- Eliminated by increasing speed or better lubrication

**Serrated/Segmented Chip**:
- Saw-tooth appearance
- High-strength materials (titanium, Inconel)
- Adiabatic shear bands (localized heating and softening)
- Cyclic cutting forces (vibration risk)

### Cutting Force Components

**Three Force Components**:

**1. Primary Cutting Force (F_c)**:
- Direction of cutting velocity
- Largest component (60-80% of total)
- Determines power requirement

**2. Thrust Force (F_t)**:
- Perpendicular to cutting direction, in feed direction
- Causes tool deflection
- 20-40% of F_c

**3. Radial Force (F_r)**:
- Perpendicular to cutting direction and feed
- Relevant in milling (pushes away from center)
- 10-30% of F_c

**Force Measurement**:
Dynamometers measure forces during machining tests.

**Typical Values** (turning 1018 steel, 0.020" DOC, 0.010" feed):
- F_c ≈ 300 lb
- F_t ≈ 100 lb
- F_r ≈ 50 lb

### Specific Cutting Force

**Definition**: Cutting force per unit area of uncut chip.

$$k_s = \frac{F_c}{A_{chip}} = \frac{F_c}{DOC \times f}$$

**Typical Values**:

| Material | k_s (kpsi) | k_s (N/mm²) |
|----------|------------|-------------|
| Aluminum 6061 | 50-80 | 345-550 |
| Brass | 80-120 | 550-825 |
| Mild Steel 1018 | 150-250 | 1035-1725 |
| Alloy Steel 4140 | 250-400 | 1725-2760 |
| Stainless 304 | 300-450 | 2070-3100 |
| Titanium Ti-6Al-4V | 350-500 | 2415-3450 |
| Cast Iron | 100-180 | 690-1240 |

**Force Prediction**:
$$F_c = k_s \times DOC \times f$$

**Example**:
Turning 4140 steel, DOC = 0.100", feed = 0.008":
$$F_c = 300,000 \text{ psi} \times 0.100 \times 0.008 = 240 \text{ lb}$$

**Power Required**:
$$P = \frac{F_c \times V}{33,000}$$

where V is cutting speed (FPM), P in horsepower.

At 400 FPM:
$$P = \frac{240 \times 400}{33,000} = 2.9 \text{ hp}$$

### Chip Thickness and Width

**Uncut Chip Thickness (h)**:
In turning: h = feed per revolution

In milling: h varies with engagement angle θ:
$$h = f_z \sin\theta$$

**Maximum chip thickness** (90° engagement):
$$h_{max} = f_z$$

**Average chip thickness** (full slot, 180° engagement):
$$h_{avg} = f_z \times \frac{2}{\pi} \approx 0.64 f_z$$

**Chip Thinning Effect**:
In light radial cuts (< 25% diameter), chip thins:
$$h_{avg} = f_z \sqrt{\frac{RDOC}{D}}$$

**Example**:
1/2" endmill, RDOC = 0.050" (10%), f_z = 0.004":
$$h_{avg} = 0.004 \sqrt{\frac{0.050}{0.5}} = 0.004 \times 0.316 = 0.00126"$$

Chip is 68% thinner! Must increase f_z to maintain cutting action:
$$f_z = \frac{0.004}{0.316} = 0.0126"$$ (increase feed rate 3×)

## Tool Geometry

### Single-Point Tool Angles

**Rake Angle (α)**:
- Angle of tool face relative to workpiece surface
- Positive rake: Slopes away from cutting edge (easier cutting, weaker edge)
- Negative rake: Slopes toward cutting edge (stronger edge, higher forces)

**Typical Rake Angles**:
- Aluminum: +10° to +20° (soft, ductile)
- Steel: +5° to +15°
- Cast iron: 0° to +10° (brittle)
- Hardened steel: 0° to -5° (edge strength critical)

**Effect on Forces**:
10° increase in rake angle reduces cutting forces ~15-20%.

**Clearance Angle (γ)**:
- Angle between tool flank and workpiece
- Prevents rubbing behind cutting edge
- Typical: 5-10°

**Inclination Angle (λ)**:
- Angle of cutting edge relative to horizontal
- Controls chip flow direction
- Positive: Chips flow toward workpiece (turning away from tailstock)
- Negative: Chips flow away from workpiece

**End Cutting Edge Angle (ECEA)**:
- Reduces friction on trailing edge
- Typical: 5-15°

### Milling Tool Geometry

**Helix Angle**:
- Spiral of flutes around endmill
- 30-35° standard
- 40-50° high helix (aluminum, soft materials - better chip evacuation)
- 10-20° slow helix (cast iron, hardened steel - stronger edge)

**Radial Rake**:
- Rake angle viewed from front of tool
- Affects cutting forces

**Axial Rake**:
- Rake angle along helix
- Related to helix angle

**Relief Angle**:
- Clearance behind cutting edge
- Prevents rubbing on circumference

**Core Diameter**:
- Diameter of endmill body (excluding flutes)
- Larger core = more rigid tool (less deflection)

**Example - Endmill Selection**:
- Aluminum: 3-flute, 40° helix, large core, polished flutes
- Steel: 4-flute, 30° helix, variable pitch (chatter resistance)
- Titanium: 4-flute, 30° helix, sharp edge geometry, slow helix

### Number of Flutes

**Trade-offs**:

**Fewer Flutes (2-3)**:
- Larger chip gullets (better evacuation)
- Higher feed per tooth possible
- Faster feed rates at same RPM
- Less likely to clog
- Best for aluminum, deep slotting

**More Flutes (4-6+)**:
- Smoother cutting (more cuts per revolution)
- Better surface finish
- Lower chip load per tooth required
- Requires adequate chip clearance
- Best for steel, finishing operations

**Example**:
1/2" endmill at 3000 RPM, f_z = 0.003":
- 2-flute: F = 0.003 × 2 × 3000 = 18 IPM
- 4-flute: F = 0.003 × 4 × 3000 = 36 IPM (2× faster)

But 2-flute can handle higher f_z (larger gullets):
- 2-flute at f_z = 0.006": F = 36 IPM (same feed, less load per tooth)

### Tool Nose Radius

**Effect on Surface Finish**:
$$Ra = \frac{f^2}{32 r}$$

**Example**:
Feed = 0.010 IPR, nose radius = 1/32" (0.031"):
$$Ra = \frac{0.010^2}{32 \times 0.031} = 0.0001" = 100 \mu\text{in}$$

Doubling nose radius to 1/16":
$$Ra = \frac{0.010^2}{32 \times 0.0625} = 50 \mu\text{in (2× smoother)}$$

**Trade-off**:
- Larger radius: Better finish but higher cutting forces (more contact area)
- Smaller radius: Lower forces but rougher finish

**Typical Radii**:
- Roughing: 0.015-0.031" (sharp, low forces)
- Finishing: 0.031-0.062" (smoother finish)
- Precision finishing: 0.062-0.125" (mirror finish possible)

### Chip Breakers

**Purpose**: Break long, continuous chips into manageable segments.

**Mechanisms**:
- Groove on rake face causes chip to curl tightly
- Chip curls back and contacts workpiece or tool
- Stress concentration fractures chip

**Types**:
- Form-ground: Groove machined into insert
- Clamped: Separate chip breaker plate
- Geometry-based: Positive/negative lands, steps

**Selection**:
- Aggressive (deep groove): Heavy cuts, soft materials
- Moderate: General purpose
- Light (shallow groove): Finishing cuts, hard materials

**Without Chip Breaker**:
Long, stringy chips (hazardous, tangle, poor chip evacuation).

**With Chip Breaker**:
Short, 'C' or '6' shaped chips (safe, easy removal).

## Temperature Distribution

### Heat Sources

**Primary Shear Zone**: 60-80% of total heat
- Plastic deformation of material
- Proportional to shear force and shear velocity

**Secondary Shear Zone**: 20-30% of total heat
- Friction between chip and rake face
- Higher at low speeds (more contact time)

**Tertiary Zone**: 5-10% of total heat
- Friction between flank and workpiece
- Increases with tool wear

**Total Heat Generated**:
$$Q = F_c \times V \times J$$

where J = mechanical equivalent of heat (1 BTU = 778 ft-lb)

**Example**:
F_c = 250 lb, V = 400 FPM:
$$Q = \frac{250 \times 400}{778} = 128 \text{ BTU/min}$$

### Temperature Distribution

**Chip**: Carries away 60-80% of heat
- Higher speeds → more heat in chip (less contact time)
- Coolant on chip very effective

**Tool**: Absorbs 10-20% of heat
- Carbide conducts heat well (distributes along tool)
- Coating reduces heat transfer to substrate

**Workpiece**: Absorbs 10-20% of heat
- Low speeds → more heat in workpiece (longer contact)
- Thermal expansion affects precision

**Typical Cutting Temperatures**:

| Material | Temperature (°F) | Temperature (°C) |
|----------|------------------|------------------|
| Aluminum | 400-600 | 200-315 |
| Brass | 500-700 | 260-370 |
| Mild Steel | 800-1200 | 425-650 |
| Stainless Steel | 1000-1400 | 540-760 |
| Titanium | 1200-1600 | 650-870 |
| Inconel | 1400-1800 | 760-980 |

**Tool Material Limits**:
- HSS: 1000-1100°F (540-595°C) - loses hardness
- Uncoated carbide: 1400-1600°F (760-870°C)
- Coated carbide: 1800-2000°F (980-1095°C)
- Ceramic: 2200-2800°F (1200-1540°C)
- CBN: 2700-3300°F (1480-1815°C)

### Coolant Effects

**Functions of Coolant**:
1. **Cooling**: Removes heat from cutting zone
2. **Lubrication**: Reduces friction (secondary shear zone)
3. **Chip Flushing**: Evacuates chips from cut
4. **Corrosion Prevention**: Protects machine and workpiece

**Temperature Reduction**:
Flood coolant reduces cutting temperature 200-400°F compared to dry cutting.

**Effect on Tool Life**:
Reducing temperature from 1200°F to 1000°F can double tool life (due to exponential wear relationship).

**Thermal Shock**:
Intermittent cuts with coolant cause thermal cycling:
- Tool heats in cut
- Rapid cooling when exiting cut
- Cracking at cutting edge (comb cracks)

**Solution**: Flood coolant (continuous) or no coolant (consistent temperature).

## Tool Wear Mechanisms

### Abrasive Wear

**Mechanism**: Hard particles in workpiece scrape material from tool.

**Typical in**:
- Cast iron (hard carbides)
- Composites (glass or carbon fibers)
- Sand castings (sand inclusions)

**Wear Pattern**: Uniform wear on flank face

**Reduction Strategies**:
- Harder tool material (carbide > HSS)
- Reduce cutting speed
- Increase feed (less contact per cut)

### Adhesive Wear

**Mechanism**: Workpiece material welds to tool, tears away tool material when chip separates.

**Typical in**:
- Soft, ductile metals (aluminum, copper)
- Insufficient coolant/lubrication

**Wear Pattern**: Built-up edge (BUE) on rake face

**Reduction Strategies**:
- Increase cutting speed (less time for welding)
- Improve lubrication
- Coated tools (TiN, TiAlN reduce adhesion)

### Diffusion Wear

**Mechanism**: Atoms from tool diffuse into workpiece (or vice versa) at high temperatures.

**Typical in**:
- High-speed cutting of steel
- High temperatures (> 1400°F)

**Wear Pattern**: Crater wear on rake face

**Reduction Strategies**:
- Reduce cutting speed (lower temperature)
- Coated carbide (diffusion barrier)
- Ceramic or CBN tools (more stable at high temp)

### Oxidation Wear

**Mechanism**: Oxygen reacts with tool material at high temperatures, forming weak oxide layer.

**Typical in**:
- High-speed dry cutting
- Elevated temperatures (> 1500°F)

**Wear Pattern**: Flank wear, notching at depth of cut line

**Reduction Strategies**:
- Reduce cutting speed
- Use inert atmosphere (difficult in practice)
- Coatings (aluminum oxide protects)

### Thermal Cracking

**Mechanism**: Cyclic heating/cooling causes thermal stresses, cracks form perpendicular to cutting edge.

**Typical in**:
- Interrupted cuts (milling, facing)
- Flood coolant with intermittent cuts

**Wear Pattern**: Comb cracks perpendicular to edge

**Reduction Strategies**:
- Mist coolant or dry cutting (avoid thermal shock)
- Tougher tool grade (less brittle)
- Reduce cutting speed

### Mechanical Fracture

**Mechanism**: Excessive cutting forces or impact loads exceed tool strength.

**Typical in**:
- Aggressive cuts (too much DOC or feed)
- Chatter and vibration
- Interrupted cuts with hard inclusions

**Wear Pattern**: Chipping or complete edge failure

**Reduction Strategies**:
- Reduce DOC and feed
- More rigid setup (minimize vibration)
- Tougher tool grade (higher fracture toughness)

## Tool Life Criteria

### Flank Wear (VB)

**Measurement**: Width of wear land on tool flank.

**ISO Standard Tool Life**:
- Roughing: VB = 0.3 mm (0.012")
- Finishing: VB = 0.15 mm (0.006")

**Measurement Method**:
Toolmaker's microscope or optical comparator.

**Typical Progression**:
- Initial rapid wear (break-in, 0-2 minutes)
- Steady-state wear (linear, 2-30 minutes typical)
- Accelerated wear (exponential, end of life)

**Tool change** at beginning of accelerated wear phase.

### Crater Wear (KT)

**Measurement**: Depth of crater on rake face.

**Acceptable Limit**: KT = 0.06 + 0.3 × tool thickness (mm)

**Example**:
1/4" (6.35 mm) thick insert:
KT_max = 0.06 + 0.3 × 6.35 = 2.0 mm (0.080")

### Other Criteria

**Dimensional Accuracy**:
When workpiece size drifts out of tolerance, change tool.

**Surface Finish**:
When finish exceeds specification, change tool.

**Cutting Force**:
Dull tool shows 50-100% increase in forces.

**Audible**:
Experienced machinists hear when tool dulls (pitch changes, squealing).

### Taylor Tool Life Equation (Revisited)

$$V T^n = C$$

Rearranged to solve for tool life:
$$T = \left(\frac{C}{V}\right)^{1/n}$$

**Extended Form** (includes feed and DOC):
$$V T^n f^m DOC^p = C$$

where:
- $m$ ≈ 0.5-0.8 (feed exponent)
- $p$ ≈ 0.3-0.5 (DOC exponent)

**Key Insight**: Cutting speed has greatest effect on tool life (highest exponent when in VT^n form).

**Example Effect of Doubling Parameters**:
- 2× speed: Tool life × 0.06-0.25 (drastically reduced)
- 2× feed: Tool life × 0.4-0.6 (moderately reduced)
- 2× DOC: Tool life × 0.5-0.7 (moderately reduced)

**Strategy**: Increase feed and DOC before increasing speed (less impact on tool life).

## Machinability

### Definition

**Machinability**: Relative ease of machining a material, considering:
- Tool life
- Cutting forces
- Surface finish
- Chip formation

### Machinability Ratings

**AISI B1112 Steel = 100% (Reference)**

**Relative Machinability**:

| Material | Rating | Interpretation |
|----------|--------|----------------|
| Free-machining brass | 300 | 3× easier than B1112 |
| Aluminum 6061-T6 | 200 | 2× easier |
| AISI B1112 (reference) | 100 | Baseline |
| AISI 1018 steel | 70 | 30% more difficult |
| AISI 4140 steel | 50 | 2× more difficult |
| Stainless 304 | 40 | 2.5× more difficult |
| Titanium Ti-6Al-4V | 20 | 5× more difficult |
| Inconel 718 | 10 | 10× more difficult |

**Interpretation**:
Rating ≈ relative tool life at same cutting parameters.

**Example**:
Cutting 4140 at 200 SFM gives 30-minute tool life.
Same tool on aluminum 6061 at 200 SFM: ~60 minutes (2× longer).

### Factors Affecting Machinability

**Material Properties**:
- **Hardness**: Harder materials more difficult
- **Ductility**: Very ductile materials gum up (aluminum), very brittle chip poorly (cast iron)
- **Thermal conductivity**: Low conductivity (stainless, titanium) concentrates heat at tool
- **Work hardening**: Stainless hardens rapidly during cutting

**Microstructure**:
- **Grain size**: Finer grains → smoother surface but higher forces
- **Phase distribution**: Ferrite + pearlite in steel machines well
- **Inclusions**: Sulfides (MnS) improve machinability (free-machining grades)

**Additives**:
- **Lead** (Pb): Lubricates, breaks chips (banned in many regions)
- **Sulfur** (S): Forms MnS inclusions (B1112 has 0.16-0.23% S)
- **Phosphorus** (P): Increases brittleness, aids chip breaking

## Cutting Tool Materials

### High-Speed Steel (HSS)

**Composition**: Iron with 4% Cr, 18% W (or Mo), 1% V, 0.7% C (typical M2 grade)

**Properties**:
- Hardness: 63-65 HRC
- Toughness: Excellent (high fracture toughness)
- Temperature limit: 1000°F (540°C)
- Cost: Low ($5-20 per tool)

**Applications**:
- Drilling (flexibility important)
- Tapping (toughness critical)
- Low-speed operations
- Interrupted cuts
- DIY/hobby (low cost, regrindable)

**Speed Limitations**:
HSS limited to 50-200 SFM in steel (carbide 3-10× faster).

### Carbide

**Composition**: Tungsten carbide (WC) grains bonded with cobalt (Co).

**Grades**:
- **C1-C4**: More cobalt (10-15%), tougher, lower hardness (for steel)
- **C5-C8**: Less cobalt (3-6%), harder, more brittle (for cast iron, non-ferrous)

**Properties**:
- Hardness: 90-93 HRA (harder than HSS)
- Temperature limit: 1600°F (870°C) uncoated, 1800°F+ coated
- Thermal conductivity: 10× higher than HSS (better heat removal)
- Cost: Medium ($20-80 per insert)

**ISO Classifications**:
- **P (Blue)**: Steel
- **M (Yellow)**: Stainless steel (versatile)
- **K (Red)**: Cast iron, non-ferrous
- **N (Green)**: Aluminum, non-ferrous
- **S (Brown)**: High-temperature alloys (Inconel, Titanium)
- **H (Grey)**: Hardened steel (> 45 HRC)

**Example**: P20 carbide
- P = steel machining
- 20 = moderate toughness/hardness balance

### Coated Carbide

**Coating Methods**:
- **CVD** (Chemical Vapor Deposition): 1000°C, thicker coatings (5-20 μm)
- **PVD** (Physical Vapor Deposition): 500°C, thinner coatings (2-5 μm), sharper edge

**Common Coatings**:

**TiN (Titanium Nitride)** - Gold color:
- First generation coating
- Hardness: 2400 HV
- Temp limit: 1000°F (540°C)
- General purpose

**TiCN (Titanium Carbonitride)** - Blue-gray:
- Harder than TiN (3000 HV)
- Better wear resistance
- Steel machining

**TiAlN (Titanium Aluminum Nitride)** - Purple-violet:
- Excellent high-temp stability (1500°F+)
- Forms Al₂O₃ barrier at high temp
- High-speed machining, dry cutting

**AlCrN (Aluminum Chromium Nitride)** - Gray:
- Superior oxidation resistance
- Hard coatings, mold making

**Multilayer Coatings**:
TiN/TiCN/Al₂O₃ - combines benefits of each layer.

**Benefits**:
- 2-10× tool life vs uncoated
- Higher speeds possible (50-100% increase)
- Dry machining capable

### Ceramics

**Composition**: Aluminum oxide (Al₂O₃) with additives.

**Types**:
- **Oxide ceramics** (Al₂O₃): White, for cast iron and hardened steel
- **Silicon nitride** (Si₃N₄): Gray, for cast iron (higher toughness)
- **SiAlON**: Si-Al-O-N solid solution (Si₃N₄ derivative)

**Properties**:
- Hardness: 1800-2000 HV (harder than carbide)
- Temperature limit: 2400°F (1315°C)
- Toughness: Low (brittle)
- Chemical stability: Excellent

**Applications**:
- High-speed finishing (2000+ SFM on cast iron)
- Hardened steel (55-65 HRC)
- No coolant (thermal shock risk)

**Limitations**:
- Brittle (no interrupted cuts)
- Expensive ($50-150 per insert)
- Requires rigid setup

### Cubic Boron Nitride (CBN)

**Composition**: Cubic form of boron nitride (second hardest material after diamond).

**Properties**:
- Hardness: 4500 HV (approaching diamond)
- Temperature limit: 3000°F (1650°C)
- Chemically inert (doesn't react with ferrous metals)
- Cost: Very high ($150-500 per insert)

**Applications**:
- Hardened steel (55-70 HRC)
- Hard turning (replaces grinding)
- Aerospace alloys (Inconel, Waspaloy)
- Long tool life in hard materials (10-50× carbide)

**Form**:
- Solid CBN: All CBN (rare, expensive)
- Tipped CBN: Thin CBN layer on carbide substrate (common)

### Polycrystalline Diamond (PCD)

**Composition**: Synthetic diamond particles sintered under high pressure/temperature.

**Properties**:
- Hardness: 8000-10,000 HV (hardest tool material)
- Thermal conductivity: Highest (better heat removal than any other material)
- Toughness: Moderate (better than ceramic, worse than carbide)
- Cost: Very high ($200-800 per cutter)

**Applications**:
- Non-ferrous metals (aluminum, brass, copper)
- Composites (carbon fiber, fiberglass)
- Plastics and wood
- Ultra-long tool life (100× carbide in aluminum)

**Limitations**:
- **Cannot machine ferrous metals** (iron/steel) - carbon diffuses into steel at cutting temperature
- Expensive
- Sensitive to shock loads

**Forms**:
- Tipped tools: PCD brazed to carbide
- Solid PCD: Entire cutting edge is diamond (rare, expensive)
- CVD diamond: Thin film coating (emerging)

### Material Selection Guide

**Low-speed (<200 SFM), Interrupted Cuts, Toughness Required**:
→ HSS

**General Machining Steel (200-600 SFM)**:
→ Coated carbide (TiAlN)

**High-Speed Finishing Cast Iron (1000-2000+ SFM)**:
→ Ceramic (Si₃N₄)

**Hardened Steel (55-65 HRC)**:
→ CBN

**High-Volume Aluminum Production**:
→ PCD

**Composites, Non-Ferrous**:
→ PCD or solid carbide (uncoated)

## Summary

Understanding cutting mechanics enables intelligent selection of feeds, speeds, and tool geometry:

**Key Principles**:
1. Chip formation involves shear deformation and friction
2. Cutting forces scale with chip area (DOC × feed)
3. Temperature increases exponentially with speed
4. Tool wear results from abrasion, adhesion, diffusion, oxidation, and cracking
5. Tool material must match workpiece and cutting conditions

**Practical Applications**:
- Calculate forces to check machine/fixture capability
- Predict power requirements
- Select tool geometry for material (rake angle, helix, flutes)
- Choose tool material based on speed and workpiece
- Recognize wear patterns to optimize parameters

**Next Steps**:
Understanding mechanics provides foundation for:
- Calculating optimal cutting speeds (Section 20.3)
- Optimizing feed rates (Section 20.4)
- Troubleshooting problems (Section 20.9)

---

**Next**: [20.3 Cutting Speed and Spindle RPM Calculations](section-20.3-cutting-speed.md)
