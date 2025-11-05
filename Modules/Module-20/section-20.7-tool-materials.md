# 20.7 Tool Material Selection

## Overview

Cutting tool materials have evolved dramatically since the early days of machining. Selection depends on workpiece material, cutting conditions, and economic considerations.

**Tool material properties required**:
- **Hardness**: Must be harder than workpiece at cutting temperature
- **Toughness**: Resist fracture from impact and interrupted cuts
- **Wear resistance**: Maintain sharp edge under abrasion
- **Hot hardness**: Retain hardness at elevated temperatures
- **Chemical stability**: Resist diffusion and reaction with workpiece

**Trade-off**: Hardness vs toughness (cannot maximize both simultaneously)

## High-Speed Steel (HSS)

### Composition and Properties

**Typical composition (M2 grade)**:
- Iron base
- 18% Tungsten (or 5% Molybdenum in M42)
- 4% Chromium
- 1% Vanadium
- 0.8% Carbon

**Properties**:
- Hardness: 63-65 HRC
- Fracture toughness: Excellent (best of all tool materials)
- Hot hardness: Retains hardness to ~1000°F (540°C)
- Thermal conductivity: Moderate
- Cost: Low ($5-20 per tool)

### Types of HSS

**M-Series** (Molybdenum-based):
- M2: General purpose (most common)
- M42: Cobalt added (8%), better hot hardness
- M7: High molybdenum (8.75%), general purpose

**T-Series** (Tungsten-based):
- T1, T15: Higher tungsten content
- Better wear resistance, more expensive
- Less common today

**Powder Metallurgy HSS**:
- PM manufacturing process
- Finer, more uniform grain structure
- Better wear resistance and toughness
- 2-3× cost of conventional HSS

### Applications - HSS

**Best for**:
- Drilling (toughness critical)
- Tapping (high torque, shock loads)
- Reamers (long tool life needed)
- Complex form tools (grinding cost high)
- Interrupted cuts (milling slots, keyways)
- Low-speed operations (<200 SFM in steel)
- Hobby/DIY (low cost, can be resharpened)

**Not suitable for**:
- High-speed production (too slow)
- Hard materials (>35 HRC)
- High-temperature alloys

### Cutting Speeds - HSS

Compared to carbide, HSS runs at 50% of speed:

| Material | HSS Speed | Carbide Speed |
|----------|-----------|---------------|
| Aluminum | 200-400 SFM | 600-1200 SFM |
| Mild Steel | 90-120 SFM | 250-500 SFM |
| Stainless | 40-60 SFM | 150-250 SFM |
| Cast Iron | 60-100 SFM | 300-500 SFM |

## Cemented Carbide

### Composition and Properties

**Structure**:
- Tungsten carbide (WC) particles (90-95%)
- Cobalt (Co) binder (5-10%)
- Other carbides (TiC, TaC, NbC) for specific properties

**Manufacturing**:
- Powder metallurgy
- Pressed and sintered at 2500°F
- Very hard ceramic particles in tough metal matrix

**Properties**:
- Hardness: 90-93 HRA (much harder than HSS)
- Hot hardness: Retains hardness to ~1400°F (760°C) uncoated
- Thermal conductivity: Excellent (3× better than HSS)
- Fracture toughness: Good (but less than HSS)
- Cost: Medium ($20-80 per insert/tool)

### ISO Carbide Classification

**C1-C4 Grades** (Steel Cutting):
- **Higher cobalt content** (10-12%)
- **More tough**, less wear-resistant
- For steel (ferrous, non-abrasive)
- Can handle interrupted cuts

**C5-C8 Grades** (Cast Iron / Non-Ferrous):
- **Lower cobalt content** (3-6%)
- **Harder**, more wear-resistant, more brittle
- For cast iron, aluminum, non-ferrous
- Continuous cuts preferred

**ISO Color Code System**:

| Code | Color | Application | Characteristics |
|------|-------|-------------|-----------------|
| P | Blue | Steel, long chips | Tough, less wear-resistant |
| M | Yellow | Stainless steel | Versatile, intermediate properties |
| K | Red | Cast iron, short chips | Hard, wear-resistant, brittle |
| N | Green | Aluminum, non-ferrous | Very hard, for soft materials |
| S | Brown | High-temp alloys (Ti, Inconel) | Heat-resistant, tough |
| H | Grey | Hardened steel (>48 HRC) | Very hard, for hard turning |

**Example**: P20 carbide
- P = Steel cutting
- 20 = Medium toughness/hardness balance (10=very tough, 50=very hard)

### Carbide Grade Selection

**Rough machining / Interrupted cuts**:
- P10-P20 (steel)
- Need toughness to resist fracture
- Accept lower wear resistance

**Finishing / Continuous cuts**:
- P30-P50 (steel)
- Need wear resistance for longer tool life
- Less impact concern

**Cast iron / Aluminum**:
- K10-K20 (interrupted), K30-K40 (continuous)

**Stainless steel**:
- M15-M30 (versatile grades)
- Balance of toughness and wear resistance

## Coated Carbide

### Coating Purpose

**Benefits**:
- 2-10× tool life vs uncoated
- Higher speeds possible (30-100%)
- Reduced friction (lower forces)
- Thermal barrier (protect substrate)
- Chemical barrier (reduce diffusion)

**Structure**:
- Tough carbide substrate
- Hard, wear-resistant coating (2-20 μm thick)
- Best of both: tough core + hard surface

### Coating Methods

**CVD (Chemical Vapor Deposition)**:
- Process temperature: 1800-1900°F (1000°C)
- Coating thickness: 5-20 μm (thicker)
- Better adhesion
- Slightly rounded edge (from high temp)
- Best for: Roughing, interrupted cuts, general machining

**PVD (Physical Vapor Deposition)**:
- Process temperature: 900°F (500°C)
- Coating thickness: 2-5 μm (thinner)
- Sharper edge retained (lower temp)
- Wider variety of coatings possible
- Best for: Finishing, sharp edge required, small tools

### Common Coating Types

**TiN (Titanium Nitride)** - Gold color:
- First-generation coating (1970s)
- Hardness: 2400 HV
- Temperature limit: 1000°F (540°C)
- Cost: Low
- Application: General purpose, good visibility (gold = coated)

**TiCN (Titanium Carbonitride)** - Blue-gray:
- Hardness: 3000 HV (harder than TiN)
- Lower friction than TiN
- Better wear resistance
- Application: Steel machining, roughing

**TiAlN (Titanium Aluminum Nitride)** - Purple-violet:
- Hardness: 3500 HV
- Temperature limit: 1500°F+ (820°C)
- Forms Al₂O₃ barrier layer at high temperature
- Excellent oxidation resistance
- Application: High-speed machining, dry cutting, difficult materials

**AlCrN (Aluminum Chromium Nitride)** - Dark gray:
- Hardness: 3200 HV
- Superior oxidation resistance
- Good for abrasive materials
- Application: Mold making, hard materials

**AlTiN (Aluminum Titanium Nitride)** - Black/violet:
- Hardness: 4000+ HV (very hard)
- Excellent high-temp performance
- Application: High-speed steel machining

**Diamond (DLC - Diamond-Like Carbon)** - Black:
- Extremely low friction
- Very hard
- Application: Aluminum, non-ferrous (not for steel - carbon diffuses)

**Multi-layer Coatings**:
- TiN/TiCN/Al₂O₃ (CVD triple coating)
- Combines benefits: toughness + wear resistance + thermal barrier
- Most advanced coatings are multilayer (5-10+ layers)

### Coating Selection Guide

| Workpiece Material | Recommended Coating |
|--------------------|---------------------|
| Aluminum, brass | Uncoated or ZrN (not TiAlN - buildup risk) |
| Mild steel | TiAlN or TiCN |
| Stainless steel | TiAlN (heat resistance critical) |
| Cast iron | TiCN or uncoated |
| Hardened steel | AlTiN or AlCrN |
| Titanium | TiAlN |
| High-temp alloys | AlTiN or AlCrN |

## Ceramic Tools

### Composition and Properties

**Types**:

**Oxide Ceramics** (Al₂O₃):
- Pure aluminum oxide (white)
- Hardness: 1800-2000 HV
- Very brittle
- Best for: Cast iron finishing, hardened steel

**Silicon Nitride** (Si₃N₄):
- Gray color
- Higher fracture toughness than oxide ceramics
- Best for: Cast iron (interrupted cuts possible)

**SiAlON**:
- Silicon-Aluminum-Oxygen-Nitrogen compound
- Derivative of Si₃N₄
- Enhanced properties
- Best for: High-speed cast iron, heat-resistant alloys

**Whisker-Reinforced Ceramics**:
- SiC whiskers in Al₂O₃ matrix
- 50% higher toughness
- Better performance in steel

**Properties**:
- Hardness: 1800-2200 HV (harder than carbide)
- Hot hardness: Excellent (to 2400°F / 1315°C)
- Chemical stability: Excellent
- Fracture toughness: Poor (very brittle)
- Cost: High ($50-150 per insert)

### Applications - Ceramics

**Best for**:
- High-speed finishing (1000-2500 SFM on cast iron)
- Hardened steel turning (55-65 HRC)
- Continuous cuts (no interruption)
- When tool changes are expensive (long runs)

**Not suitable for**:
- Milling (interrupted cuts cause chipping)
- Low rigidity setups
- When coolant cannot be avoided (thermal shock)

**Cutting Conditions**:
- Very high speeds (2-5× carbide speeds)
- Light DOC (0.030-0.100")
- Dry cutting preferred (no thermal shock)
- Rigid setup mandatory

**Example - Cast Iron Finishing**:
- Ceramic insert
- V = 1500 SFM (vs 400 SFM carbide)
- DOC = 0.050"
- Feed = 0.012 IPR
- Dry cutting
- Mirror finish possible

## Cubic Boron Nitride (CBN)

### Properties

**Second hardest material** (after diamond):
- Hardness: 4500 HV
- Hot hardness: Excellent (to 3000°F / 1650°C)
- Chemically inert to ferrous metals (unlike diamond)
- Cost: Very high ($150-500 per insert)

**Structure**:
- Polycrystalline CBN (PCBN)
- Sintered under extreme pressure/temperature
- Usually bonded to carbide substrate (thin CBN layer)

### Applications - CBN

**Primary use: Hard ferrous materials**:
- Hardened steel (55-70 HRC)
- Chilled cast iron
- Hard facing materials
- High-temp alloys (Inconel, Waspaloy)

**"Hard Turning"** (replaces grinding):
- Finish turn hardened parts after heat treat
- 200-400 SFM in 60 HRC steel
- Ra 16-32 μin achievable
- Eliminates grinding operation (faster, more flexible)

**Benefits vs grinding**:
- Single-point process (simpler)
- Can machine complex shapes
- Faster for small quantities
- No grinding wheel dressing

**Cutting Conditions**:
- V = 200-600 SFM (material dependent)
- DOC = 0.010-0.050" (light)
- Feed = 0.003-0.010 IPR
- Coolant optional (can run dry)

**Tool Life**:
- 10-50× carbide life in hardened steel
- Economical despite high insert cost

### CBN Grades

**Low CBN content** (50-60%):
- More binder, tougher
- For interrupted cuts
- Lower hardness materials (50-55 HRC)

**High CBN content** (85-95%):
- Very hard, more brittle
- Continuous cuts only
- Hardest materials (60+ HRC)

## Polycrystalline Diamond (PCD)

### Properties

**Hardest tool material**:
- Hardness: 8000-10,000 HV
- Thermal conductivity: Highest of all materials (best heat removal)
- Wear resistance: Exceptional (100× carbide in aluminum)
- Cost: Very high ($200-800 per cutter)

**Structure**:
- Synthetic diamond particles sintered together
- Typically brazed as thin layer (0.5mm) on carbide substrate
- Random crystal orientation (unlike natural diamond)

### Applications - PCD

**Primary use: Non-ferrous metals**:
- Aluminum (best choice for production)
- Brass, bronze, copper
- Precious metals

**Also excellent for**:
- Composites (carbon fiber, fiberglass)
- Graphite
- Plastics (abrasive-filled)
- Wood and wood composites

**Cannot machine ferrous metals**:
- Carbon in diamond diffuses into steel at cutting temperature
- Diamond graphitizes (loses structure)
- Tool destroyed rapidly

**Cutting Conditions - Aluminum**:
- V = 1500-4000 SFM (3-5× carbide)
- Standard feed rates
- Extremely long tool life (100-200× carbide)
- High-volume production justifies cost

**Example - Aluminum Production**:
- Part requires 100,000 pieces
- Carbide tool life: 500 parts per edge
- PCD tool life: 50,000+ parts per edge
- Result: 2 PCD tools vs 200 carbide tools needed
- Labor savings >> PCD cost premium

### PCD Forms

**Brazed-tip tools**:
- PCD segment brazed to tool body
- Endmills, drills, routers
- Can be resharpened (diamond grind wheel)

**Insert form**:
- PCD layer on carbide insert
- Indexable (multiple edges)
- Replace when all edges worn

**Solid PCD** (rare):
- Entire cutting edge is diamond
- Very expensive
- Ultra-precision applications

## CVD Diamond Coatings

**Emerging technology**:
- Chemical vapor deposition of diamond film
- Thin coating (5-20 μm) on carbide
- Lower cost than PCD

**Applications**:
- Graphite machining (EDM electrodes)
- Composites
- Ultra-abrasive materials

**Limitations**:
- Coating adhesion challenges
- Cannot be resharpened (coating too thin)

## Tool Material Selection Guide

### By Workpiece Material

**Aluminum**:
- Standard: Uncoated carbide
- Production: PCD (100× life)
- Budget: HSS (hobby use)

**Mild Steel (1018)**:
- Standard: TiAlN coated carbide
- Budget: HSS
- Not recommended: Ceramic (better options exist)

**Alloy Steel (4140)**:
- Annealed: TiAlN or TiCN coated carbide
- Hardened (55-65 HRC): CBN or ceramic

**Stainless Steel**:
- TiAlN coated carbide (mandatory - heat resistance)
- M-grade (versatile grade)

**Titanium**:
- TiAlN or AlCrN coated carbide
- Sharp tools, frequent replacement

**Cast Iron**:
- Roughing: Uncoated or TiCN carbide
- Finishing: Ceramic (high-speed)

**Hardened Steel (>55 HRC)**:
- First choice: CBN (hard turning)
- Alternative: Ceramic
- Budget: Carbide (very slow, light cuts)

**Inconel / High-Temp Alloys**:
- Ceramic or CBN (high-speed)
- Coated carbide (lower speeds)

**Composites (carbon fiber)**:
- First choice: PCD
- Budget: Carbide (short life)

### By Operation Type

**Roughing / Heavy Cuts**:
- Tough grades (P10-P20 for steel)
- CVD coating (better adhesion)
- Larger edge radius (chip breaker)

**Finishing / Light Cuts**:
- Wear-resistant grades (P30-P50 for steel)
- PVD coating (sharper edge)
- Small edge radius or hone

**Interrupted Cuts (Milling)**:
- Toughest grades
- Lower hardness acceptable
- HSS excellent choice for slots, keyways

**Continuous Cuts (Turning)**:
- Harder grades acceptable
- Maximize wear resistance
- Ceramic or CBN for hard materials

**Drilling**:
- HSS preferred (toughness critical)
- Carbide for production (with through-coolant)

**High-Speed Machining**:
- Coated carbide (TiAlN)
- Sharp geometry
- Light cuts, high feeds

## Economic Considerations

### Tool Cost vs Performance

**Cost per cutting edge**:
- HSS: $5-20
- Uncoated carbide: $20-40
- Coated carbide: $30-80
- Ceramic: $50-150
- CBN: $150-500
- PCD: $200-800

**But cost per part is what matters**:

**Example - Aluminum Part (10,000 qty)**:

**Option A: Carbide**
- Tool cost: $40
- Parts per edge: 200
- Edges needed: 50
- Total tool cost: $2,000
- Cost per part: $0.20

**Option B: PCD**
- Tool cost: $600
- Parts per edge: 10,000
- Edges needed: 1
- Total tool cost: $600
- Cost per part: $0.06

**PCD is 70% cheaper per part** despite 15× higher tool cost!

### Decision Framework

**Low-volume** (< 100 parts):
- Use readily available tools (HSS, standard carbide)
- Tool cost matters more than life

**Medium-volume** (100-1,000 parts):
- Coated carbide optimal
- Balance tool cost and life

**High-volume** (> 1,000 parts):
- Optimize cost per part
- Advanced tooling (PCD, CBN) often justified
- Reduced downtime for tool changes

**Difficult materials**:
- May need specialized tooling even for low volume
- Carbide won't work on hardened steel (need CBN)
- Carbon fiber destroys carbide quickly (need PCD)

## Tool Life and Wear

### Typical Tool Life

| Tool Material | Relative Life (Steel) | Relative Life (Aluminum) |
|---------------|----------------------|-------------------------|
| HSS | 1× (baseline) | 1× |
| Uncoated Carbide | 3-5× | 5-10× |
| Coated Carbide | 5-15× | 8-15× |
| Ceramic | 10-30× (hard materials) | N/A |
| CBN | 20-50× (hardened steel) | N/A |
| PCD | N/A (not for ferrous) | 100-200× |

**Factors affecting tool life**:
1. Cutting speed (exponential effect via Taylor equation)
2. Workpiece hardness
3. Coolant effectiveness
4. Tool coating
5. Machine rigidity

### When to Change Tool

**Criteria**:
- Flank wear reaches limit (0.012" roughing, 0.006" finishing)
- Dimensional accuracy lost
- Surface finish degrades
- Cutting forces increase significantly
- Audible change (squealing, chattering)

**Before catastrophic failure**:
- Tool breakage causes scrap
- May damage workpiece, fixture, or machine
- Change tool when wear approaches limit

## Summary

**Tool material selection hierarchy**:

1. **Identify workpiece material and hardness**
2. **Determine operation** (roughing/finishing, continuous/interrupted)
3. **Select appropriate tool material** (use guide above)
4. **Choose specific grade** (toughness vs wear resistance)
5. **Select coating if applicable** (speed/life benefit vs cost)
6. **Verify performance and optimize**

**General recommendations**:
- **Aluminum**: Uncoated carbide or PCD (production)
- **Steel**: TiAlN coated carbide
- **Stainless**: TiAlN coated carbide (mandatory)
- **Cast iron**: Uncoated carbide or ceramic (finishing)
- **Hardened steel**: CBN or ceramic
- **Titanium**: TiAlN coated carbide
- **Composites**: PCD

**Economic principle**:
Optimize cost per part, not tool cost. Advanced tooling (PCD, CBN) often pays for itself in reduced cycle time, longer life, and less downtime.

---

**Next**: [20.8 Coolant and Chip Management](section-20.8-coolant-chip-management.md)
