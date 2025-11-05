# 20.5 Depth of Cut and Width of Cut

## Terminology

**Depth of Cut (DOC)**: Also called Axial Depth of Cut (ADOC)
- The distance the tool plunges into material along its axis
- Vertical engagement in milling
- For endmills: How deep the tool cuts in Z-axis

**Width of Cut (WOC)**: Also called Radial Depth of Cut (RDOC)
- The distance the tool steps over laterally
- Horizontal engagement in milling
- For endmills: How much material engages the tool radially

**Stepover**: WOC expressed as percentage of tool diameter
- Example: 0.100" WOC with 0.500" endmill = 20% stepover

## Depth of Cut Guidelines

### General Recommendations

**Roughing Operations**:
- ADOC: 0.5× to 1.5× tool diameter
- Goal: Maximum material removal
- Deep cuts, light stepover preferred

**Finishing Operations**:
- ADOC: 0.010-0.100" (0.25-2.5mm)
- Goal: Final dimensions and surface finish
- Light cuts in all directions

### By Tool Type

**Square Endmills**:
- Maximum ADOC: Up to 1.5× diameter
- Typical roughing: 0.5-1.0× diameter
- Limited by flute length

**Example**: 1/2" endmill
- Maximum: 0.75" ADOC
- Typical: 0.25-0.50" ADOC

**Ball Endmills**:
- ADOC limited by effective diameter at depth
- Surface finish degrades with deep axial cuts
- Typical: 0.05-0.25× diameter for finishing

**Roughing Endmills** (corn cob):
- Serrated edges reduce cutting forces
- Can handle 2-3× diameter ADOC
- Designed for aggressive roughing

**Face Mills**:
- ADOC typically light: 0.060-0.200" per pass
- Wide coverage (WOC) compensates
- Multiple inserts share load

### By Material

**Aluminum**:
- Can handle deep cuts (1.0-1.5× diameter)
- Low cutting forces
- Excellent chip evacuation needed

**Mild Steel**:
- Moderate: 0.5-1.0× diameter
- Balance between MRR and tool life

**Stainless Steel**:
- Conservative: 0.3-0.6× diameter
- Work hardening concern with heavy cuts
- Reduce ADOC, increase feed per tooth

**Titanium**:
- Light: 0.2-0.5× diameter
- Low thermal conductivity
- Heat builds up quickly in deep cuts

**Cast Iron**:
- Moderate to deep: 0.5-1.2× diameter
- Abrasive but low cutting forces
- Dry cutting preferred

**Hardened Steel (>50 HRC)**:
- Very light: 0.05-0.15× diameter
- Carbide or CBN tools
- Multiple light passes

## Width of Cut Guidelines

### Slotting vs Side Milling

**Full Slotting** (WOC = 100% of diameter):
- Most demanding operation
- Both sides of tool engaged
- Poor chip evacuation
- Reduce feed rate 40-60%
- Avoid if possible

**Side Milling** (WOC < 50% of diameter):
- Preferred approach
- Better chip evacuation
- Lower cutting forces
- Standard feed rates applicable

**High-Speed Machining** (WOC < 20% of diameter):
- Light radial engagement
- Very high feed rates possible (chip thinning)
- Longer tool life
- Faster overall with multiple passes

### Recommended Stepover Percentages

**Roughing**:
- Standard: 40-60% of diameter
- Aggressive (aluminum): 50-75%
- Conservative (hard materials): 25-40%

**Semi-Finishing**:
- 20-40% of diameter
- Balance between MRR and finish

**Finishing**:
- 5-20% of diameter
- Often just 0.010-0.030" radial stock

**Example - 1/2" Endmill**:
- Roughing: 0.200-0.300" WOC (40-60%)
- Semi-finish: 0.100-0.200" WOC (20-40%)
- Finish: 0.025-0.100" WOC (5-20%)

### Climb vs Conventional Milling

**Climb Milling** (down milling):
- Tool rotation matches feed direction
- Chip thickness: thick to thin
- Advantages:
  - Better surface finish
  - Longer tool life
  - Less work hardening
  - Chips evacuate behind tool
- Disadvantages:
  - Requires backlash elimination
  - Can pull workpiece if not secured
  - Higher entry force

**Conventional Milling** (up milling):
- Tool rotation opposes feed direction
- Chip thickness: thin to thick
- Advantages:
  - Works with backlash in machine
  - Pushes work into table
  - Lower entry force
- Disadvantages:
  - Poorer surface finish
  - More work hardening
  - Shorter tool life
  - Chips evacuate toward tool

**Recommendation**: Use climb milling whenever possible (CNC with ballscrews)

## Material Removal Rate Optimization

### MRR Formula

$$MRR = ADOC \times WOC \times F$$

where all dimensions in same units (inches or mm)

**Example**:
- ADOC = 0.200"
- WOC = 0.300"
- F = 40 IPM
$$MRR = 0.200 \times 0.300 \times 40 = 2.4 \text{ in³/min}$$

### Optimization Strategy

**To maximize MRR while minimizing tool wear**:

Priority order for increasing parameters:
1. **Increase ADOC first** (least effect on tool life)
2. **Increase feed rate second** (moderate effect)
3. **Increase WOC third** (significant effect due to engagement angle)
4. **Increase cutting speed last** (greatest effect on tool life)

**Example comparison** - Target MRR = 3.0 in³/min:

**Option A**: ADOC = 0.5", WOC = 0.2", F = 30 IPM
**Option B**: ADOC = 0.2", WOC = 0.5", F = 30 IPM

Both achieve same MRR, but Option A (deep, narrow) produces:
- Lower cutting forces (less radial engagement)
- Better tool life
- Better surface finish (climb milling easier)

**Best practice**: "Deep and narrow" over "shallow and wide"

### Power-Limited Machining

**Maximum MRR from available power**:

$$MRR_{max} = \frac{P \times \eta}{U}$$

where:
- $P$ = spindle power (hp or kW)
- $\eta$ = efficiency (0.70-0.85 typical)
- $U$ = specific cutting energy (hp/(in³/min) or kW/(cm³/s))

**Example**:
3 HP spindle machining 1018 steel:
- U = 0.7 hp/(in³/min)
- η = 0.8
$$MRR_{max} = \frac{3 \times 0.8}{0.7} = 3.4 \text{ in³/min}$$

**Select DOC/WOC/F combination that achieves ~3 in³/min** (safety margin)

## Advanced Strategies

### Trochoidal Milling

**Technique**: Circular tool path with constant light radial engagement

**Parameters**:
- WOC: 5-15% of tool diameter
- ADOC: 1.0-2.0× tool diameter (deeper than conventional)
- Feed rate: 2-4× conventional (chip thinning compensation)

**Advantages**:
- Eliminates full slotting
- Constant tool loading
- Excellent chip evacuation
- Longer tool life (50-200%)
- Can machine full-depth slots efficiently

**Example - 1/2" Endmill**:
- Conventional slotting: ADOC = 0.25", WOC = 0.5", F = 20 IPM (reduced for slot)
- Trochoidal: ADOC = 0.75", WOC = 0.05", F = 60 IPM (much faster!)

**CAM software** generates trochoidal toolpaths automatically

### Adaptive Roughing

**Technique**: CAM varies WOC to maintain constant tool loading

**How it works**:
- Calculates engagement angle at every point
- Adjusts WOC to keep engagement constant
- Feed rate may also vary

**Advantages**:
- Maximum safe MRR throughout toolpath
- No sudden load changes (longer tool life)
- Fewer tool breakages
- 30-60% faster than conventional roughing

**Parameters**:
- Target engagement: 90-120° (vs 180° in slotting)
- ADOC: Aggressive (0.75-1.5× diameter)
- Feed rate: Optimized for target engagement

**Example**:
Pocketing with 1/2" endmill:
- Open area: WOC increases automatically (wider cuts)
- Corners: WOC decreases automatically (prevents overload)
- Constant cutting force maintained

### High-Speed Machining (HSM)

**Philosophy**: Many light passes at very high feed rates

**Parameters**:
- WOC: 5-20% of diameter (very light radial)
- ADOC: 0.25-0.75× diameter (moderate to deep)
- Feed rate: 2-5× conventional (compensate chip thinning)
- Cutting speed: 1.5-2× conventional

**Advantages**:
- Lower cutting forces (despite high feed)
- Better surface finish
- Longer tool life
- Less heat in workpiece (for aluminum)
- Can machine thin walls without deflection

**Requirements**:
- High-speed spindle (>15,000 RPM)
- Rigid machine
- CAM software with HSM toolpaths
- Sharp tools

**Example - Aluminum Part**:
- Conventional: WOC = 0.3", ADOC = 0.3", F = 80 IPM, V = 800 SFM
- HSM: WOC = 0.05", ADOC = 0.5", F = 300 IPM, V = 1200 SFM
- Result: Faster cycle time, better finish, longer tool life

### Dynamic Milling

**Combination of**:
- Trochoidal tool motion
- Adaptive engagement control
- High-speed machining principles

**Result**: Optimal performance across all scenarios

## Depth of Cut in Other Operations

### Turning

**DOC in turning**: Radial depth (amount removed from diameter)

**Roughing**:
- 0.060-0.200" DOC (0.120-0.400" off diameter)
- Limited by rigidity and power

**Finishing**:
- 0.005-0.030" DOC (0.010-0.060" off diameter)
- Surface finish priority

**Example**:
Turning 2.000" diameter to 1.500" (0.500" total):
- Roughing: 4 passes at 0.120" DOC = 0.480" removed
- Finishing: 1 pass at 0.020" DOC = 0.020" removed
- Final diameter: 1.500"

### Drilling

**DOC**: Not typically varied (drill diameter determines)

**Peck depth**: How far drill advances before retracting
- Standard drilling: Full depth, no pecking
- Deep holes (>3× diameter): Peck 0.5-1.0× diameter
- Very deep: Peck 0.25-0.5× diameter

**Example**: 1/4" drill, 2" deep hole
- Hole depth / diameter = 8:1 (deep)
- Peck depth = 0.25" (1× diameter)
- 8 pecks required

### Face Milling

**DOC**: Axial depth per pass

**Roughing**:
- 0.080-0.200" per pass
- Multiple passes to reach depth

**Finishing**:
- 0.020-0.060" per pass
- Often single pass for final dimension

**Large face mills** (>3"):
- Can take heavier DOC (more inserts)
- 0.150-0.300" roughing passes common

## Troubleshooting

### Problem: Tool Deflection / Poor Accuracy

**Symptoms**:
- Dimensions wrong (undersize pockets, oversize bosses)
- Taper in walls
- Poor surface finish on walls

**Likely causes**:
1. WOC too large (excessive side force)
2. Tool overhang too long
3. Feed rate too high

**Solutions**:
- Reduce WOC to 25-40% of diameter
- Reduce tool overhang if possible
- Reduce feed rate 20-30%
- Use larger diameter tool if clearance allows
- Take spring pass (no WOC, just trace final path)

### Problem: Tool Breakage

**Symptoms**: Catastrophic tool failure

**Likely causes**:
1. Full slotting (WOC = 100%)
2. ADOC too large for tool
3. Feed rate too high

**Solutions**:
- Avoid full slotting (use trochoidal or pre-drill)
- Reduce ADOC to 0.5× diameter or less
- Reduce feed rate 40-60%
- Use roughing endmill for heavy cuts

### Problem: Poor Surface Finish

**Symptoms**: Rough walls, chatter marks

**Likely causes**:
1. Too much WOC for finishing
2. Dull tool
3. Vibration

**Solutions**:
- Reduce WOC to 5-15% for finishing
- Replace tool
- Reduce tool overhang
- Change RPM ±15% to avoid resonance

### Problem: Slow Cycle Time

**Symptoms**: Machining takes too long

**Solutions**:
1. Increase ADOC (if not at limit)
2. Increase WOC to 50-60%
3. Increase feed rate (check minimum chip load)
4. Consider adaptive or trochoidal strategies
5. Increase cutting speed (monitor tool life)

### Problem: Excessive Tool Wear

**Symptoms**: Tools dull quickly, frequent changes

**Solutions**:
- Reduce WOC (radial engagement major factor)
- Reduce cutting speed 20-30%
- Ensure climb milling (not conventional)
- Improve coolant flow
- Check for work hardening (stainless)

## Practical Examples

### Example 1: Pocket Roughing in Aluminum

**Setup**:
- Material: 6061 Aluminum
- Pocket: 3" × 3" × 0.75" deep
- Tool: 1/2" 3-flute carbide endmill

**Strategy**: Deep cuts, moderate stepover

**Parameters**:
- ADOC: 0.50" (1× diameter)
- WOC: 0.25" (50% stepover)
- RPM: 6000
- Feed: 180 IPM (f_z = 0.010")

**Toolpath**:
- 2 passes in depth (0.50" + 0.25")
- Spiral entry, climb milling
- ~12 passes across width

**Cycle time**: ~8 minutes

### Example 2: Steel Part Finishing

**Setup**:
- Material: 1018 Steel
- Operation: Finish walls to size
- Stock remaining: 0.030" radial
- Tool: 1/2" 4-flute carbide endmill

**Strategy**: Light finishing passes

**Parameters**:
- ADOC: 0.75" (full depth, one pass)
- WOC: 0.015" radial (single spring pass)
- RPM: 2700
- Feed: 22 IPM (f_z = 0.002")

**Toolpath**:
- Climb milling critical for finish
- Constant Z height
- Two passes: 0.015" + spring pass (0.000")

### Example 3: Slotting Stainless Steel

**Setup**:
- Material: 304 Stainless
- Feature: 0.50" wide × 1.5" deep slot
- Tool: 1/2" 4-flute carbide endmill (coated)

**Problem**: Full slotting required (part geometry)

**Strategy**: Reduce parameters for slotting

**Parameters**:
- ADOC: 0.20" (conservative for slotting)
- WOC: 0.50" (100%, unavoidable)
- RPM: 2000
- Feed: 16 IPM (f_z = 0.002", reduced 50% for slot)

**Toolpath**:
- Plunge in center (or ramp down)
- 8 depth passes (0.20" × 7 + 0.10" final)
- Climb mill on one side, conventional on other (unavoidable in slot)

**Alternative**: Trochoidal slotting
- ADOC: 0.60" (3× deeper!)
- WOC: 0.05" (10%, circular path)
- Feed: 60 IPM (4× faster!)
- Faster overall despite more passes

### Example 4: Face Milling Cast Iron

**Setup**:
- Material: Gray cast iron
- Operation: Face large area (10" × 10")
- Tool: 3" face mill, 6 inserts

**Parameters**:
- ADOC: 0.100" per pass
- WOC: 2.7" (90% of diameter, efficient)
- RPM: 500
- Feed: 24 IPM (f_z = 0.008")

**Toolpath**:
- 4 passes to cover width (with 10% overlap)
- Dry cutting (no coolant)
- ~5 minutes per 0.100" depth

## Summary

**Key principles**:
1. Deep and narrow (high ADOC, low WOC) better than shallow and wide
2. Avoid full slotting when possible (worst case for tool)
3. Finishing requires light WOC (5-20% of diameter)
4. Climb milling preferred over conventional
5. MRR = ADOC × WOC × F (optimize all three)

**Optimization priorities**:
1. Increase ADOC (least tool wear impact)
2. Increase feed rate
3. Increase WOC
4. Increase cutting speed (most tool wear impact)

**Advanced strategies**:
- Trochoidal milling: Constant light engagement, deep cuts
- Adaptive roughing: CAM maintains constant loading
- HSM: Very light WOC, very high feed rates

**Decision framework**:
1. Determine operation type (roughing vs finishing)
2. Select ADOC based on tool size and material
3. Select WOC based on strategy (avoid full slotting)
4. Calculate MRR, check against machine power
5. Adjust parameters based on test cuts
6. Document optimal values for production

---

**Next**: [20.6 Material-Specific Parameters](section-20.6-material-parameters.md)
