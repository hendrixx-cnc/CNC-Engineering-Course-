# 20.6 Material-Specific Parameters

## Introduction

Different materials have vastly different machining characteristics. This section provides detailed parameter recommendations for common materials encountered in CNC machining.

**Material properties affecting machinability**:
- Hardness (resistance to cutting)
- Thermal conductivity (heat dissipation)
- Work hardening rate (surface hardening during cutting)
- Abrasiveness (tool wear rate)
- Chip formation characteristics

## Aluminum Alloys

### Material Characteristics

**Advantages**:
- Excellent machinability (200% rating vs 1018 steel)
- High thermal conductivity (dissipates heat well)
- Low cutting forces
- Good surface finish achievable
- Non-ferrous (can use PCD tools)

**Challenges**:
- Soft/gummy (can build up on tool edge)
- Long stringy chips (evacuation issues)
- Thermal expansion (dimensional control in precision work)

### Common Aluminum Alloys

**2024 (Aerospace)**:
- Machinability: Good
- Higher strength, lower ductility than 6061
- Slightly more difficult to machine

**6061 (General Purpose)**:
- Machinability: Excellent
- Most common structural aluminum
- Easy to machine, good finish

**7075 (High Strength)**:
- Machinability: Good
- Higher strength than 6061
- Machines similarly to 6061

**Cast Aluminum (A356, 319)**:
- Machinability: Fair to Good
- Contains silicon (abrasive)
- May have porosity
- Reduce speeds 20-30% vs wrought aluminum

### Recommended Parameters - Aluminum

**Cutting Speed**:
- HSS: 200-400 SFM
- Carbide: 600-1200 SFM
- PCD: 1500-4000 SFM (production environments)

**Feed Per Tooth**:
- Roughing: 0.008-0.015"
- Finishing: 0.003-0.006"

**Depth of Cut**:
- Roughing ADOC: 1.0-1.5× diameter
- Roughing WOC: 40-60% stepover
- Finishing: Light passes (0.020-0.060" radial)

**Example - 1/2" Endmill in 6061**:
- V = 900 SFM → N = 6876 RPM
- f_z = 0.010" (roughing)
- Z = 3 flutes (preferred for aluminum)
- F = 0.010 × 3 × 6876 = 206 IPM
- ADOC = 0.50", WOC = 0.25" (50%)
- MRR = 0.50 × 0.25 × 206 = 25.75 in³/min

### Tool Selection - Aluminum

**Endmills**:
- 2-3 flutes preferred (large chip gullets)
- High helix angle (40-50°)
- Polished flutes (reduces buildup)
- Sharp edge geometry
- Uncoated carbide or PCD

**Coatings**:
- Generally NOT recommended (promotes buildup)
- Exception: ZrN (zirconium nitride) works well
- PCD for high-volume production (100× tool life)

**Speeds/Feeds Philosophy**:
- Run fast and aggressive
- High RPM, high feed rates
- Deep ADOC, moderate WOC

### Coolant - Aluminum

**Options**:
1. **Flood coolant** (preferred for production)
   - Water-soluble oil or synthetic
   - Good chip evacuation
   - Prevents buildup

2. **Air blast** (good for hobby/small machines)
   - Clears chips effectively
   - No mess
   - High speeds keep tool cool

3. **Mist coolant** (compromise)
   - Some cooling, good chip clearing

**Never dry**: Aluminum can build up on tool (BUE), poor finish

### Common Issues - Aluminum

**Built-Up Edge (BUE)**:
- Aluminum welding to cutting edge
- **Solution**: Increase cutting speed, improve coolant, use polished tools

**Burrs**:
- Soft material tends to tear at exits
- **Solution**: Sharp tools, climb milling, light final passes, chamfer edges

**Poor Finish**:
- Usually from BUE or chip recutting
- **Solution**: Higher speeds, better chip evacuation, sharp tools

## Steel - Low Carbon (1018, A36, 12L14)

### Material Characteristics

**1018 Cold Rolled**:
- Machinability: 70% rating
- General-purpose mild steel
- Moderate cutting forces
- Good surface finish achievable

**12L14 (Free-Machining)**:
- Machinability: 170% rating (excellent)
- Sulfur added for chip breaking
- Best choice when machinability matters
- Slightly lower strength than 1018

**A36 (Structural)**:
- Machinability: 65% rating
- Hot rolled (scale on surface)
- Variable hardness
- More difficult than 1018

### Recommended Parameters - Mild Steel

**Cutting Speed**:
- HSS: 90-120 SFM
- Uncoated carbide: 250-350 SFM
- Coated carbide: 350-500 SFM

**Feed Per Tooth**:
- Roughing: 0.005-0.010"
- Finishing: 0.002-0.004"

**Depth of Cut**:
- Roughing ADOC: 0.5-1.0× diameter
- Roughing WOC: 40-50% stepover
- Finishing: 0.010-0.030" radial

**Example - 1/2" Coated Carbide in 1018**:
- V = 400 SFM → N = 3056 RPM
- f_z = 0.006" (roughing)
- Z = 4 flutes
- F = 0.006 × 4 × 3056 = 73 IPM
- ADOC = 0.50", WOC = 0.20" (40%)
- MRR = 0.50 × 0.20 × 73 = 7.3 in³/min

### Tool Selection - Mild Steel

**Endmills**:
- 4 flutes standard
- 30-35° helix angle
- TiAlN coating recommended
- Variable pitch reduces chatter

**Coolant**:
- Flood coolant strongly recommended
- Water-soluble oil or synthetic
- Improves tool life 2-3×

### Common Issues - Mild Steel

**Built-Up Edge**:
- Occurs at moderate speeds (100-200 SFM)
- **Solution**: Increase to 350+ SFM with carbide, use coolant

**Work Hardening** (A36, hot rolled):
- Surface harder than core
- **Solution**: Take heavier first cut (get through hardened layer), sharp tools

## Steel - Medium/High Carbon (1045, 4140, 4340)

### Material Characteristics

**1045**:
- Machinability: 60% rating
- Medium carbon (0.45% C)
- Harder than 1018, more wear resistant
- Heat treatable

**4140 (Alloy Steel)**:
- Machinability: 50% rating (annealed), 20-30% (hardened)
- Chromium-molybdenum alloy
- Very common for high-strength parts
- Machines well when annealed (< 28 HRC)

**4340 (High-Strength Alloy)**:
- Machinability: 45% rating
- Nickel-chromium-molybdenum alloy
- Tougher than 4140
- More difficult to machine

### Recommended Parameters - Alloy Steel

**Cutting Speed** (annealed condition):
- HSS: 50-80 SFM
- Uncoated carbide: 150-250 SFM
- Coated carbide: 250-400 SFM

**Feed Per Tooth**:
- Roughing: 0.004-0.008"
- Finishing: 0.001-0.003"

**Depth of Cut**:
- Roughing ADOC: 0.4-0.8× diameter
- Roughing WOC: 30-40% stepover
- More conservative than mild steel

**Example - 1/2" Coated Carbide in 4140 (Annealed)**:
- V = 300 SFM → N = 2292 RPM
- f_z = 0.005" (roughing)
- Z = 4 flutes
- F = 0.005 × 4 × 2292 = 46 IPM
- ADOC = 0.40", WOC = 0.15" (30%)
- MRR = 0.40 × 0.15 × 46 = 2.76 in³/min

### Hardened Steel (> 45 HRC)

**When to machine vs grind**:
- < 55 HRC: Carbide tools possible (difficult)
- 55-65 HRC: CBN or ceramic tools (hard turning)
- > 65 HRC: Grinding typically required

**Hard Turning Parameters** (CBN):
- V = 200-400 SFM
- Feed: 0.003-0.008 IPR
- DOC: 0.010-0.040"
- Light cuts, high precision

**Hard Milling** (65 HRC):
- V = 50-150 SFM
- f_z = 0.001-0.003"
- ADOC: 0.05-0.15× diameter (very light)
- Multiple passes required

## Stainless Steel

### Material Characteristics

**Challenges**:
- Work hardens rapidly during cutting
- Low thermal conductivity (heat concentrates at tool)
- Gummy/stringy chips
- Abrasive (high tool wear)

**Types**:
- **300 series** (304, 316): Austenitic, non-magnetic, most difficult
- **400 series** (416, 430): Martensitic/ferritic, easier to machine
- **17-4 PH**: Precipitation hardened, moderate machinability

### Recommended Parameters - 304 Stainless

**Cutting Speed**:
- HSS: 40-60 SFM
- Uncoated carbide: 100-150 SFM
- Coated carbide (TiAlN): 150-250 SFM

**Feed Per Tooth**:
- Roughing: 0.003-0.006"
- Finishing: 0.001-0.003"
- **Critical**: Must maintain minimum chip load (avoid work hardening)

**Depth of Cut**:
- Roughing ADOC: 0.3-0.6× diameter
- Roughing WOC: 30-40% stepover
- Conservative approach required

**Example - 1/2" TiAlN Coated in 304 SS**:
- V = 180 SFM → N = 1375 RPM
- f_z = 0.004" (roughing)
- Z = 4 flutes
- F = 0.004 × 4 × 1375 = 22 IPM
- ADOC = 0.25", WOC = 0.15" (30%)
- MRR = 0.25 × 0.15 × 22 = 0.83 in³/min

### Tool Selection - Stainless

**Requirements**:
- Sharp tools mandatory
- Positive rake geometry
- TiAlN or AlCrN coating
- Chip breaker geometry

**Strategy**:
- Never dwell (work hardening)
- Constant feed through cut
- Adequate chip load always
- Flood coolant essential

### Common Issues - Stainless

**Rapid Tool Wear**:
- Heat concentration
- **Solution**: Reduce speed 20%, ensure adequate feed, flood coolant

**Work Hardening**:
- Previous cuts harden surface
- **Solution**: Heavier cuts to get below hardened layer, sharp tools, no rubbing

**Poor Finish**:
- Gummy material tears
- **Solution**: Sharp tools, climb milling, adequate coolant

## Titanium Alloys

### Material Characteristics

**Ti-6Al-4V (Grade 5)** - Most Common:
- Machinability: 20% rating (very difficult)
- Low thermal conductivity (5× worse than steel)
- High chemical reactivity with tool materials
- High strength at elevated temperatures
- Springy (elastic deflection during cutting)

**Challenges**:
- Heat concentrates at tool edge
- Tools wear rapidly
- Can catch fire if chips accumulate
- Expensive material (minimize scrap)

### Recommended Parameters - Ti-6Al-4V

**Cutting Speed**:
- HSS: 40-60 SFM (not recommended)
- Uncoated carbide: 150-250 SFM
- Coated carbide: 200-350 SFM

**Feed Per Tooth**:
- Roughing: 0.003-0.006"
- Finishing: 0.001-0.003"
- Adequate chip load critical

**Depth of Cut**:
- Roughing ADOC: 0.2-0.5× diameter (conservative)
- Roughing WOC: 20-40% stepover
- Avoid heavy cuts (heat buildup)

**Example - 1/2" Coated Carbide in Ti-6Al-4V**:
- V = 250 SFM → N = 1910 RPM
- f_z = 0.004" (roughing)
- Z = 4 flutes
- F = 0.004 × 4 × 1910 = 31 IPM
- ADOC = 0.20", WOC = 0.15" (30%)
- MRR = 0.20 × 0.15 × 31 = 0.93 in³/min

### Tool Selection - Titanium

**Requirements**:
- Very sharp tools
- Positive rake geometry
- Carbide substrate (K or M grade)
- TiAlN or AlCrN coating

**Strategy**:
- Sharp tools, replace frequently
- Moderate speeds (not too fast - heat; not too slow - work hardening)
- Adequate feed always
- Copious coolant (flood, high pressure)

### Coolant - Titanium

**Critical for success**:
- Flood coolant mandatory
- High pressure (300+ PSI) if available
- Never dry cut (fire hazard)
- Never water-based (hydrogen embrittlement risk, fire risk)
- Use mineral oil or approved synthetic

### Safety - Titanium

**Fire Hazard**:
- Fine chips can ignite spontaneously
- Burns at 3000°F
- Water accelerates fire
- **Prevention**: Regular chip removal, no accumulation, Class D extinguisher available

## Cast Iron

### Material Characteristics

**Gray Cast Iron**:
- Machinability: Excellent (80-100% rating)
- Brittle chips (easy evacuation)
- Graphite flakes act as lubricant
- Abrasive (carbides in structure)
- Dry cutting preferred

**Ductile/Nodular Iron**:
- Machinability: Good (60-80%)
- More ductile than gray iron
- Stronger but slightly harder to machine

### Recommended Parameters - Gray Cast Iron

**Cutting Speed**:
- HSS: 60-100 SFM
- Uncoated carbide: 300-500 SFM
- Ceramic: 1000-2500 SFM (finishing)

**Feed Per Tooth**:
- Roughing: 0.006-0.012"
- Finishing: 0.003-0.006"
- Can use aggressive feeds

**Depth of Cut**:
- Roughing ADOC: 0.5-1.2× diameter
- Roughing WOC: 40-60% stepover

**Example - 1/2" Carbide in Gray Cast Iron**:
- V = 400 SFM → N = 3056 RPM
- f_z = 0.008" (roughing)
- Z = 4 flutes
- F = 0.008 × 4 × 3056 = 98 IPM
- ADOC = 0.50", WOC = 0.25" (50%)
- MRR = 0.50 × 0.25 × 98 = 12.25 in³/min

### Tool Selection - Cast Iron

**Endmills**:
- Uncoated carbide or ceramic
- 4 flutes standard
- Wear-resistant grade (K grade carbide)

**Coolant**:
- **Dry cutting preferred** (graphite self-lubricates)
- Air blast for chip clearing acceptable
- If coolant used: Light mist only (flood causes thermal shock)

### Common Issues - Cast Iron

**Abrasive Wear**:
- Hard carbides wear tools
- **Solution**: Use harder tool grades (ceramic for finishing), expect shorter tool life than steel

**Hard Spots**:
- White cast iron areas (very hard)
- **Solution**: Reduce speed 30%, sharp tools, carbide required

## Plastics and Composites

### Acrylic (PMMA)

**Characteristics**:
- Easy to machine
- Brittle (chips, not cracks)
- Melts if too slow or dull tools

**Parameters**:
- V = 500-1000 SFM
- f_z = 0.005-0.012"
- Sharp tools, high speed

**Coolant**:
- Air blast or dry
- Coolant optional (prevents melting in deep cuts)

### Delrin (Acetal)

**Characteristics**:
- Excellent machinability
- Tough, slippery
- Machines like aluminum

**Parameters**:
- V = 600-1200 SFM
- f_z = 0.006-0.015"
- Standard carbide tools

### Nylon (Polyamide)

**Characteristics**:
- Soft, gummy
- Absorbs moisture (dimensional changes)
- Builds up on tools

**Parameters**:
- V = 400-800 SFM
- f_z = 0.004-0.010"
- Sharp tools, high rake angles

### Carbon Fiber / Fiberglass Composites

**Characteristics**:
- Extremely abrasive
- Delamination risk
- Health hazard (dust control critical)

**Parameters**:
- V = 400-600 SFM (carbide), 800-1500 SFM (PCD)
- f_z = 0.002-0.006"
- Light ADOC to prevent delamination

**Tool Requirements**:
- PCD (diamond) strongly recommended
- Carbide wears out quickly (20% of life vs aluminum)
- Sharp tools prevent delamination

**Safety**:
- Dust collection mandatory
- Respiratory protection
- Skin/eye protection

## Exotic Alloys (Inconel, Hastelloy)

### Inconel 718

**Characteristics**:
- Machinability: 10% rating (extremely difficult)
- Extreme work hardening
- High strength at temperature
- Retains hardness even when red-hot

**Parameters**:
- V = 50-120 SFM (carbide)
- V = 200-400 SFM (ceramic)
- V = 300-600 SFM (CBN)
- f_z = 0.002-0.005"
- ADOC: 0.1-0.3× diameter (very light)

**Strategy**:
- Ceramic or CBN tools for production
- Extremely sharp carbide for limited runs
- Very rigid setup
- Flood coolant, high pressure
- Expect high tool wear

### Hastelloy C-276

**Similar to Inconel**:
- Extremely difficult
- Work hardens rapidly
- Low speeds, light cuts
- Carbide or ceramic tools

## Material Comparison Table

| Material | Machinability | Cutting Speed (Carbide) | Feed/Tooth | Tool Life | Difficulty |
|----------|---------------|-------------------------|------------|-----------|------------|
| Aluminum 6061 | 200% | 600-1200 SFM | 0.008-0.015" | Excellent | Easy |
| Brass | 300% | 400-800 SFM | 0.005-0.012" | Excellent | Very Easy |
| 1018 Steel | 70% | 250-350 SFM | 0.005-0.010" | Good | Moderate |
| 4140 Steel | 50% | 150-250 SFM | 0.004-0.008" | Moderate | Moderate |
| 304 Stainless | 40% | 100-150 SFM | 0.003-0.006" | Poor | Difficult |
| Ti-6Al-4V | 20% | 150-250 SFM | 0.003-0.006" | Poor | Very Difficult |
| Cast Iron | 80% | 300-500 SFM | 0.006-0.012" | Moderate | Easy |
| Inconel 718 | 10% | 50-120 SFM | 0.002-0.005" | Very Poor | Extremely Difficult |

## Summary

**Key takeaways by material family**:

**Aluminum**: Run fast and aggressive, worry about chip evacuation and buildup

**Mild Steel**: Standard parameters, coated carbide and coolant recommended

**Alloy Steel**: More conservative, sharp tools, adequate coolant critical

**Stainless**: Work hardening major concern, never rub, maintain chip load, sharp tools

**Titanium**: Heat management critical, expensive material demands care, safety concerns

**Cast Iron**: Easy to machine but abrasive, dry cutting preferred

**Plastics**: Sharp tools prevent melting, high speeds, watch for material-specific issues

**Exotics (Inconel)**: Specialized tooling required, expect high costs and slow machining

**General strategy**:
1. Identify material and condition (annealed, hardened, etc.)
2. Start with conservative parameters from this guide
3. Test cut and monitor tool wear, finish, forces
4. Optimize gradually based on results
5. Document successful parameters for future jobs

---

**Next**: [20.7 Tool Material Selection](section-20.7-tool-materials.md)
