# 20.4 Feed Rate Optimization

## Understanding Feed Rate

**Feed Rate (F)**: The velocity at which the tool advances through the workpiece
- Units: Inches per minute (IPM) or millimeters per minute (mm/min)
- Programmed with F word in G-code: `G1 X2.0 F30` (move to X2.0 at 30 IPM)

**Feed rate determines**:
- Surface finish quality (primary factor)
- Chip load per tooth
- Cutting forces
- Material removal rate
- Cycle time

## Feed Per Tooth Concept

**Feed Per Tooth (f_z)**: The distance the tool advances per cutting edge

**This is the fundamental parameter** - most machining data specifies f_z, not feed rate.

**Relationship**:
$$F = f_z \times Z \times N$$

where:
- $F$ = feed rate (IPM or mm/min)
- $f_z$ = feed per tooth (inches or mm)
- $Z$ = number of flutes/teeth
- $N$ = spindle speed (RPM)

**Example 1**:
- 4-flute endmill
- 3000 RPM
- f_z = 0.003"
$$F = 0.003 \times 4 \times 3000 = 36 \text{ IPM}$$

**Example 2**:
- 2-flute endmill (same parameters otherwise)
$$F = 0.003 \times 2 \times 3000 = 18 \text{ IPM}$$

**Key insight**: More flutes = higher feed rate at same chip load

## Reverse Calculation (Feed Rate → Feed Per Tooth)

**When to use**: Given a feed rate, calculate actual chip load

$$f_z = \frac{F}{Z \times N}$$

**Example**:
Running 50 IPM with 3-flute mill at 4000 RPM:
$$f_z = \frac{50}{3 \times 4000} = 0.00417"$$

Check if this is appropriate for material and tool size.

## Recommended Feed Per Tooth Values

### By Material (Carbide Tools)

**Aluminum Alloys**:
- Roughing: 0.008-0.015" per tooth
- Finishing: 0.003-0.006" per tooth
- Note: Can handle high chip loads, excellent machinability

**Mild Steel (1018)**:
- Roughing: 0.005-0.010" per tooth
- Finishing: 0.002-0.004" per tooth

**Alloy Steel (4140)**:
- Roughing: 0.004-0.008" per tooth
- Finishing: 0.001-0.003" per tooth

**Stainless Steel (304)**:
- Roughing: 0.003-0.006" per tooth
- Finishing: 0.001-0.003" per tooth
- Note: Work hardens, avoid rubbing

**Titanium (Ti-6Al-4V)**:
- Roughing: 0.003-0.006" per tooth
- Finishing: 0.001-0.003" per tooth
- Note: Low thermal conductivity, sharp tools critical

**Cast Iron**:
- Roughing: 0.006-0.012" per tooth
- Finishing: 0.003-0.006" per tooth

**Plastics**:
- Roughing: 0.005-0.012" per tooth
- Finishing: 0.002-0.005" per tooth
- Note: Sharp tools to prevent melting

### By Tool Diameter

**General guideline**: Larger tools can handle larger chip loads (more rigid)

**Rule of thumb**: f_z ≈ 0.001-0.002" per 1/8" of diameter

| Tool Diameter | Roughing f_z | Finishing f_z |
|---------------|--------------|---------------|
| 1/8" (3mm) | 0.001-0.002" | 0.0005-0.001" |
| 1/4" (6mm) | 0.003-0.005" | 0.001-0.002" |
| 3/8" (10mm) | 0.004-0.007" | 0.002-0.003" |
| 1/2" (12mm) | 0.005-0.010" | 0.002-0.004" |
| 3/4" (20mm) | 0.007-0.012" | 0.003-0.005" |
| 1" (25mm) | 0.008-0.015" | 0.003-0.006" |

**Adjust down for**:
- Long tool overhang (> 3× diameter)
- Hard materials
- Poor machine rigidity
- Finishing operations

## Surface Finish Relationship

**Theoretical surface roughness**:
$$Ra = \frac{f_z^2}{32 \times r}$$

where:
- $Ra$ = average roughness (inches or μm)
- $f_z$ = feed per tooth
- $r$ = tool nose radius

**Example**:
f_z = 0.010", nose radius = 0.031" (1/32"):
$$Ra = \frac{0.010^2}{32 \times 0.031} = 0.0001" = 100 \text{ μin}$$

**Halving feed per tooth**:
f_z = 0.005":
$$Ra = \frac{0.005^2}{32 \times 0.031} = 0.000025" = 25 \text{ μin (4× smoother)}$$

**Key principle**: Surface finish improves quadratically with reduced feed per tooth

### Surface Finish Guidelines

| Application | Ra (μin) | Ra (μm) | Typical f_z |
|-------------|----------|---------|-------------|
| Rough machining | 200-500 | 5-12 | 0.008-0.015" |
| General machining | 63-125 | 1.6-3.2 | 0.004-0.008" |
| Precision finish | 16-63 | 0.4-1.6 | 0.001-0.003" |
| Mirror finish | 4-16 | 0.1-0.4 | 0.0005-0.001" |

**Achieving better finish**:
1. Reduce feed per tooth (most important)
2. Increase nose radius
3. Sharp tools
4. Higher RPM (more cuts per inch of travel)
5. Rigid setup (minimize vibration)
6. Climb milling (smoother engagement)

## Minimum Chip Load

**Critical concept**: Feed per tooth must be large enough for cutting, not rubbing.

**Minimum chip load**: ~0.0005" (0.01mm)

**Below minimum**:
- Tool rubs instead of cuts
- Rapid wear on tool flank
- Heat buildup
- Poor surface finish
- Potential tool breakage

**Example problem**:
- 4-flute endmill at 10,000 RPM
- Feed rate: 20 IPM
$$f_z = \frac{20}{4 \times 10000} = 0.0005"$$ (at minimum!)

**Better approach**:
- Reduce RPM to 5000
- Same feed rate: 20 IPM
$$f_z = \frac{20}{4 \times 5000} = 0.001"$$ (adequate chip load)

**Key insight**: Sometimes reducing RPM improves results by maintaining proper chip load

## Chip Thinning Effect

**Occurs in**: Light radial engagement (< 25% of tool diameter)

**Phenomenon**: Actual chip thickness is less than programmed feed per tooth

**Formula**:
$$h_{actual} = f_z \times \sqrt{\frac{RDOC}{D}}$$

where:
- $h_{actual}$ = actual average chip thickness
- $RDOC$ = radial depth of cut
- $D$ = tool diameter

**Example**:
- 1/2" endmill
- RDOC = 0.050" (10% of diameter)
- Programmed f_z = 0.004"

$$h_{actual} = 0.004 \times \sqrt{\frac{0.050}{0.5}} = 0.004 \times 0.316 = 0.00126"$$

Chip is 68% thinner than programmed!

**Solution**: Increase feed per tooth to compensate
$$f_z = \frac{0.004}{0.316} = 0.0126"$$

Increase feed rate 3× to maintain effective chip load.

**High-speed machining (HSM)** takes advantage of this:
- Very light radial cuts (5-10% of diameter)
- Very high feed rates (compensate for chip thinning)
- Lower cutting forces (despite high feed rate)
- Longer tool life

## Feed Rate Calculation Examples

### Example 1: Aluminum Pocket Milling

**Setup**:
- Material: 6061 Aluminum
- Tool: 1/2" 3-flute carbide endmill
- Cutting speed: 800 SFM
- Operation: Roughing

**Step 1**: Calculate RPM
$$N = \frac{3.82 \times 800}{0.5} = 6112 \text{ RPM}$$

**Step 2**: Select chip load
- Aluminum roughing: 0.010" per tooth

**Step 3**: Calculate feed rate
$$F = 0.010 \times 3 \times 6112 = 183 \text{ IPM}$$

**G-code**:
```gcode
S6112 M3
F183
G1 X2.0 Y1.0  (Mill at 183 IPM)
```

### Example 2: Steel Finishing

**Setup**:
- Material: 1018 Steel
- Tool: 1/2" 4-flute coated carbide endmill
- Cutting speed: 350 SFM
- Operation: Finishing

**Step 1**: Calculate RPM
$$N = \frac{3.82 \times 350}{0.5} = 2674 \text{ RPM}$$

**Step 2**: Select chip load
- Steel finishing: 0.002" per tooth

**Step 3**: Calculate feed rate
$$F = 0.002 \times 4 \times 2674 = 21 \text{ IPM}$$

### Example 3: Small Tool in Steel

**Setup**:
- Material: 4140 Steel
- Tool: 1/8" 4-flute endmill
- Max RPM: 10,000

**Step 1**: Desired cutting speed = 250 SFM
$$N = \frac{3.82 \times 250}{0.125} = 7640 \text{ RPM}$$ ✓ (within limit)

**Step 2**: Chip load for small tool
- 1/8" diameter: 0.0015" per tooth (conservative)

**Step 3**: Calculate feed rate
$$F = 0.0015 \times 4 \times 7640 = 46 \text{ IPM}$$

**Check minimum chip load**:
- 0.0015" > 0.0005" ✓ (adequate)

### Example 4: Face Milling

**Setup**:
- Material: Cast iron
- Tool: 3" face mill, 6 inserts
- Cutting speed: 400 SFM

**Step 1**: Calculate RPM
$$N = \frac{3.82 \times 400}{3.0} = 509 \text{ RPM}$$

**Step 2**: Chip load
- Cast iron: 0.008" per tooth

**Step 3**: Calculate feed rate
$$F = 0.008 \times 6 \times 509 = 24 \text{ IPM}$$

**Note**: All inserts engaged simultaneously in face milling (different from endmill where engagement varies)

## Adjusting Feed Rates

### Increase Feed When:

**1. Roughing operations**
- Goal: Maximum material removal
- Increase to upper range of chip load recommendations

**2. Aluminum / soft materials**
- Can handle 2-3× higher feeds than steel
- Use aggressive chip loads

**3. Rigid setup**
- Solid fixturing allows higher forces
- Increase 20-30%

**4. Sharp tools**
- New tools can handle higher feeds
- Increase 10-20%

**5. Proper coolant**
- Flood coolant enables higher feeds
- Better chip evacuation

**6. Light radial engagement (HSM)**
- Chip thinning allows 2-5× higher feed rate
- Compensate with formula above

### Reduce Feed When:

**1. Finishing operations**
- Surface finish priority
- Reduce to lower range (often 50% of roughing)

**2. Small tools (< 1/4")**
- Deflection risk
- Reduce 30-50%

**3. Long tool overhang**
- Tool chatter risk
- Reduce 20-40%

**4. Hard materials**
- Titanium, Inconel, hardened steel
- Reduce 30-50% from steel values

**5. Poor fixturing**
- Workpiece movement risk
- Reduce 30-50%

**6. Machine vibration**
- Reduce until chatter stops
- Often 20-40% reduction needed

**7. Tool wear**
- Dull tools need lower feeds
- Reduce 20-30% or change tool

## Feed Rate vs Material Removal Rate

**Material Removal Rate (MRR)**:
$$MRR = DOC \times WOC \times F$$

where:
- $DOC$ = depth of cut (axial)
- $WOC$ = width of cut (radial)
- $F$ = feed rate

**Units**: cubic inches per minute (in³/min) or cm³/min

**Example**:
- DOC = 0.200"
- WOC = 0.400"
- F = 40 IPM
$$MRR = 0.200 \times 0.400 \times 40 = 3.2 \text{ in³/min}$$

**Optimization strategy**:
To increase MRR, prioritize changes in this order:
1. Increase DOC (least effect on tool life)
2. Increase feed rate (moderate effect)
3. Increase cutting speed (greatest effect on tool life)

**Example comparison** (same MRR = 3.2 in³/min):

**Option A**: DOC = 0.1", WOC = 0.4", F = 80 IPM
**Option B**: DOC = 0.4", WOC = 0.4", F = 20 IPM

Both produce 3.2 in³/min, but Option B (deeper, slower) is gentler on tool.

## Adaptive Feed Rate Control

**Modern CAM systems** vary feed rate based on engagement:

**Full slot** (100% engagement):
- Reduce feed 40-60%
- High cutting forces

**50% engagement**:
- Standard feed rate

**Light engagement** (< 25%):
- Increase feed 100-300%
- Chip thinning compensation

**Corners** (direction change):
- Reduce feed 30-50%
- Prevent tool breakage from deceleration forces

**Example program** with adaptive feed:
```gcode
(Adaptive feed rates based on engagement)
G1 X1.0 F80    (Light engagement, high feed)
X2.0 Y1.0 F30  (Full slot, reduced feed)
G2 X3.0 Y0 I0.5 J0 F20  (Arc/corner, further reduced)
```

## Drilling Feed Rates

**Different approach**: Feed per revolution, not feed per tooth

**Formula**:
$$f_r = \frac{F}{N}$$

where $f_r$ = feed per revolution (IPR or mm/rev)

**Recommended feed per revolution**:

| Material | 1/8" drill | 1/4" drill | 1/2" drill | 1" drill |
|----------|-----------|-----------|-----------|----------|
| Aluminum | 0.004 | 0.008 | 0.015 | 0.025 |
| Steel | 0.002 | 0.005 | 0.010 | 0.020 |
| Stainless | 0.001 | 0.003 | 0.006 | 0.012 |
| Cast Iron | 0.003 | 0.006 | 0.012 | 0.020 |

**Example**:
1/4" drill in aluminum, 3000 RPM:
- f_r = 0.008 IPR
$$F = 0.008 \times 3000 = 24 \text{ IPM}$$

**Peck drilling**: Reduce feed rate 10-20% (frequent entry/exit shock)

## Troubleshooting Feed Rate Issues

### Problem: Poor Surface Finish

**Likely cause**: Feed too high

**Solution**:
- Reduce feed per tooth 30-50%
- Increase RPM (more cuts per inch)
- Check tool sharpness
- Verify minimum chip load still maintained

### Problem: Tool Breakage

**Likely cause**: Feed too high (overload)

**Solution**:
- Reduce feed 40-60%
- Check for chip thinning (increase if light engagement)
- Verify adequate spindle torque at RPM

### Problem: Tool Burning / Rapid Wear

**Likely cause**: Feed too low (rubbing)

**Solution**:
- Increase feed rate 50-100%
- Calculate actual chip load (check minimum 0.0005")
- May need to reduce RPM to maintain chip load

### Problem: Vibration / Chatter

**Causes**: Multiple possibilities

**Solutions to try**:
1. Increase feed 20-30% (heavier cut dampens vibration)
2. Decrease feed 20-30% (reduce forces)
3. Change RPM ±15%
4. Reduce DOC/WOC
5. Shorten tool overhang

### Problem: Machine Stalling

**Likely cause**: Feed too high for available power/torque

**Solution**:
- Reduce feed rate 30-50%
- If at low RPM: Reduce DOC (torque-limited)
- If at high RPM: Check spindle power rating

## Feed Rate Optimization Workflow

**Step 1**: Calculate baseline feed rate
- Use material/tool recommendations
- Calculate: F = f_z × Z × N

**Step 2**: Adjust for conditions
- Scale up/down based on factors above
- Check minimum chip load maintained

**Step 3**: Program and test
- Start at 75% of calculated feed
- Monitor sound, vibration, finish

**Step 4**: Optimize
- Gradually increase until:
  - Surface finish degrades, or
  - Vibration occurs, or
  - Machine power limit reached
- Back off 10-15% for production

**Step 5**: Document
- Record optimal parameters
- Note tool life achieved
- Update for future jobs

## Summary

**Key formulas**:
- Feed rate: $F = f_z \times Z \times N$
- Feed per tooth: $f_z = F / (Z \times N)$
- Surface finish: $Ra = f_z^2 / (32 \times r)$
- Chip thinning: $h = f_z \times \sqrt{RDOC/D}$

**Critical principles**:
1. Feed per tooth (chip load) is the fundamental parameter
2. Maintain minimum chip load (0.0005") to avoid rubbing
3. Surface finish improves with lower feed per tooth (quadratic relationship)
4. Compensate for chip thinning in light radial cuts
5. Balance feed rate for tool life, surface finish, and cycle time

**Decision framework**:
1. Select feed per tooth based on material and tool size
2. Calculate feed rate: F = f_z × Z × N
3. Adjust for operation (roughing vs finishing)
4. Compensate for chip thinning if applicable
5. Test and optimize based on results

---

**Next**: [20.5 Depth of Cut and Width of Cut](section-20.5-depth-width-of-cut.md)
