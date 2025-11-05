# 20.1 Introduction to Feeds and Speeds

## What Are Feeds and Speeds?

**Cutting Parameters**: The numerical values controlling how fast a cutting tool moves and rotates during machining.

**Three Primary Parameters**:

1. **Cutting Speed (V)**: The velocity at which the cutting edge passes through material
   - Measured in surface feet per minute (SFM) or meters per minute (m/min)
   - Determines spindle RPM for given tool diameter

2. **Feed Rate (F)**: The velocity at which the tool advances into the workpiece
   - Measured in inches per minute (IPM) or millimeters per minute (mm/min)
   - Determines thickness of material removed per revolution or per tooth

3. **Depth of Cut (DOC)**: The thickness of material removed in a single pass
   - Axial depth of cut (ADOC): How deep the tool plunges
   - Radial depth of cut (RDOC): How much the tool steps over

## Why Feeds and Speeds Matter

### Tool Life

**Tool wear rate** increases exponentially with cutting speed:

**Taylor Tool Life Equation**:
$$V T^n = C$$

where:
- $V$ = cutting speed
- $T$ = tool life (minutes until dullness)
- $n$ = Taylor exponent (material-dependent, typically 0.2-0.5)
- $C$ = constant for tool/material combination

**Example**:
For 1018 steel with carbide tool, $n$ = 0.25:
- At 400 SFM: Tool life = 60 minutes
- At 500 SFM (+25%): Tool life = 60 × (400/500)⁴ = 25 minutes (-58%)
- At 320 SFM (-20%): Tool life = 60 × (400/320)⁴ = 129 minutes (+115%)

**Key Insight**: Small changes in cutting speed produce large changes in tool life.

### Surface Finish

**Feed per tooth** is the primary factor affecting surface finish:

**Theoretical surface roughness** (Ra):
$$Ra = \frac{f_z^2}{32 r}$$

where:
- $f_z$ = feed per tooth (inches or mm)
- $r$ = tool nose radius

**Example**:
0.010" feed per tooth, 0.031" nose radius:
$$Ra = \frac{0.010^2}{32 \times 0.031} = 0.0001" = 100 \mu\text{in}$$

Halving feed per tooth: Ra = 25 μin (4× smoother)

**Practical surface finish** also depends on:
- Tool sharpness and wear
- Vibration and chatter
- Material properties
- Coolant effectiveness

### Cycle Time

**Material Removal Rate (MRR)**:
$$MRR = DOC \times WOC \times F$$

where:
- $DOC$ = depth of cut
- $WOC$ = width of cut (radial engagement)
- $F$ = feed rate

**Example**:
- DOC = 0.100"
- WOC = 0.500"  
- Feed = 40 IPM
- MRR = 0.100 × 0.500 × 40 = 2.0 cubic inches per minute

To remove 20 cubic inches: Time = 20 / 2.0 = 10 minutes

**Optimization Trade-off**:
- Faster speeds → More MRR but shorter tool life
- Balance tool cost and cycle time for minimum cost per part

### Machine Power and Torque

**Specific Cutting Energy (U)**: Power required to remove unit volume of material

| Material | U (hp/(in³/min)) | U (W/(cm³/s)) |
|----------|------------------|---------------|
| Aluminum 6061 | 0.15-0.25 | 0.7-1.1 |
| Mild Steel 1018 | 0.60-0.80 | 2.7-3.6 |
| Stainless 304 | 1.0-1.5 | 4.5-6.8 |
| Titanium Ti-6Al-4V | 1.2-1.8 | 5.4-8.1 |
| Cast Iron | 0.40-0.60 | 1.8-2.7 |

**Power Required**:
$$P = MRR \times U \times K$$

where $K$ is inefficiency factor (typically 0.7-0.9)

**Example**:
Machining 1018 steel at MRR = 2.0 in³/min:
- $P$ = 2.0 × 0.70 × 0.80 = 1.1 hp at spindle
- Motor power required: 1.1 / 0.75 (efficiency) = 1.5 hp minimum

**Torque at Spindle**:
$$T = \frac{P \times 5252}{RPM}$$

where:
- $T$ = torque (lb-ft)
- $P$ = power (hp)
- RPM = spindle speed

**Example**:
1.1 hp at 2000 RPM:
$$T = \frac{1.1 \times 5252}{2000} = 2.9 \text{ lb-ft}$$

**Machine Limitations**:
- Spindle power curve limits MRR at low RPM (torque limited)
- Maximum spindle power limits MRR at high RPM (power limited)
- Must check both power and torque when selecting parameters

## Historical Context

### Early Manual Machining

**Pre-1900**:
- Belt-driven machines with discrete speeds (step pulleys)
- Feeds and speeds selected by machinist experience
- "Run it until it smokes, then back off a bit"
- No scientific optimization

**Early 20th Century**:
- Frederick W. Taylor (1906): Scientific study of metal cutting
- Developed Taylor Tool Life Equation
- Established optimization principles (minimum cost vs maximum production)
- Machinery's Handbook (1914): First comprehensive speed/feed tables

### CNC Era

**1950s-1970s**:
- Numerical control enables precise, repeatable parameters
- Computer-aided calculations
- Coated carbide tools expand speed ranges

**1980s-Present**:
- CAM software automates parameter selection
- Tool manufacturers provide extensive databases
- High-speed machining strategies
- Adaptive control systems adjust parameters in real-time

## Fundamental Concepts

### Cutting Speed vs Spindle Speed

**Cutting Speed (V)**: The speed at which the cutting edge moves through material (SFM or m/min)
- Independent of tool size
- Material-dependent (aluminum faster than steel)

**Spindle Speed (N)**: Rotational speed of spindle (RPM)
- Depends on tool diameter
- Machine-limited (max RPM varies by spindle)

**Relationship**:
$$N = \frac{12 V}{\pi D} = \frac{3.82 V}{D}$$ (Imperial: SFM, inches, RPM)

$$N = \frac{1000 V}{\pi D} = \frac{318.3 V}{D}$$ (Metric: m/min, mm, RPM)

**Example (Imperial)**:
Machining aluminum (V = 600 SFM) with 1/2" endmill:
$$N = \frac{3.82 \times 600}{0.5} = 4584 \text{ RPM}$$

Same speed with 2" face mill:
$$N = \frac{3.82 \times 600}{2.0} = 1146 \text{ RPM}$$

**Key Insight**: Larger tools run slower RPM for same cutting speed.

### Feed Per Tooth vs Feed Rate

**Feed Per Tooth (f_z)**: Distance tool advances per cutting edge
- Primary specification in machining data
- Typical range: 0.001-0.020" (0.025-0.50 mm)

**Feed Per Revolution (f_r)**: Distance tool advances per spindle revolution
- For single-point tools (turning, boring)
- $f_r = f_z \times Z$ (where $Z$ = number of teeth)

**Feed Rate (F)**: Tool advance speed (IPM or mm/min)
$$F = f_z \times Z \times N$$

**Example**:
4-flute endmill at 3000 RPM with f_z = 0.003":
$$F = 0.003 \times 4 \times 3000 = 36 \text{ IPM}$$

**G-Code Example**:
```gcode
S3000 M3      (Spindle 3000 RPM, CW)
F36           (Feed rate 36 IPM)
G1 X2.0 Y1.0  (Linear move at 36 IPM)
```

### Material Removal Rate

**MRR Calculation**:

**Milling**:
$$MRR = ADOC \times RDOC \times F$$

**Turning**:
$$MRR = DOC \times F \times \pi D$$

**Drilling**:
$$MRR = \frac{\pi D^2}{4} \times F$$

**Units**:
- Imperial: cubic inches per minute (in³/min)
- Metric: cubic centimeters per minute (cm³/min)

**Example - Slot Milling**:
- 1/2" endmill (full slot, RDOC = 0.5")
- ADOC = 0.25"
- Feed = 30 IPM
- MRR = 0.25 × 0.5 × 30 = 3.75 in³/min

### Chip Load (Feed Per Tooth)

**Definition**: The thickness of material removed by each cutting edge.

**Factors Affecting Chip Load**:

**1. Material Hardness**:
- Soft materials (aluminum): Higher chip loads (0.008-0.020")
- Hard materials (titanium, hardened steel): Lower chip loads (0.001-0.004")

**2. Tool Diameter**:
- Larger tools: Higher chip loads (more rigid)
- Smaller tools: Lower chip loads (deflection risk)

**Rule of Thumb**: Chip load ≈ 0.001-0.002" per 1/8" diameter

**3. Number of Flutes**:
- Fewer flutes (2-3): Larger chip loads, better chip evacuation
- More flutes (4-6): Smaller chip loads, smoother finish

**4. Engagement**:
- Full slot: Reduce chip load 25-50%
- Light radial (<25% diameter): Increase chip load (chip thinning effect)

**Minimum Chip Load**:
Below 0.0005", tool may rub instead of cut:
- Rapid wear
- Poor surface finish
- Heat buildup
- Potential tool breakage

**Always maintain minimum chip load**, even if it means reducing RPM.

## Optimization Strategies

### Maximum Production Rate

**Objective**: Remove material as fast as possible.

**Approach**:
1. Select highest cutting speed tool can withstand
2. Maximize DOC and WOC within machine power limits
3. Increase feed rate until surface finish or power limit reached
4. Accept shorter tool life (frequent tool changes acceptable)

**Applications**:
- High-volume production
- Automated tool changers available
- Material cost > labor cost

### Maximum Tool Life

**Objective**: Minimize tool changes and downtime.

**Approach**:
1. Reduce cutting speed 20-30% below maximum
2. Moderate DOC and feed rates
3. Ensure adequate coolant
4. Monitor wear and change tool before failure

**Applications**:
- Unattended machining (lights-out operations)
- Expensive or difficult tool changes
- Critical parts (tool breakage unacceptable)

### Minimum Cost Per Part

**Objective**: Lowest total cost (material + labor + tooling + overhead).

**Cost Per Part**:
$$C_{part} = \frac{t_{cycle}}{60}(C_{labor} + C_{overhead}) + \frac{t_{cycle}}{T_{tool}}C_{tool change}$$

where:
- $t_{cycle}$ = cycle time (minutes)
- $C_{labor}$ = labor rate ($/hour)
- $C_{overhead}$ = machine rate ($/hour)
- $T_{tool}$ = tool life (minutes of cutting)
- $C_{tool change}$ = cost to change tool (tool cost + labor)

**Optimal Cutting Speed** (minimum cost):
$$V_{opt} = V_{max} \left[\frac{1}{n}\left(\frac{C_{tool change}/T_{max}}{C_{labor} + C_{overhead}}\right)\right]^{1/(1-n)}$$

**In Practice**:
- Calculate cost per part at several speeds
- Plot cost vs speed curve
- Select minimum point (often 15-25% below max speed)

### Best Surface Finish

**Objective**: Achieve required surface roughness.

**Approach**:
1. Reduce feed per tooth (primary factor)
2. Use sharp tools with polished cutting edges
3. Increase spindle speed (more cuts per inch of travel)
4. Optimize tool geometry (larger nose radius)
5. Finish passes with minimal RDOC (< 0.020")

**Applications**:
- Cosmetic surfaces
- Sealing surfaces
- Precision fits
- Mating surfaces

## Safety Considerations

### Tool Breakage Hazards

**Causes of Tool Breakage**:
- Excessive feed rate (overload)
- Too much DOC for tool diameter
- Spindle stall (insufficient torque)
- Vibration and chatter
- Workpiece movement (poor fixturing)
- Tool collision (programming error)

**Risks**:
- Flying tool fragments (eye hazard)
- Workpiece damage (scrap part)
- Spindle damage (bent shaft, bearing damage)
- Machine crash

**Prevention**:
- Conservative parameters for first cuts
- Gradual parameter increase (test and verify)
- Monitor spindle load (audible feedback, load meter)
- Proper fixturing and clamping
- Simulation and verification of G-code

### Fire Hazards

**Combustible Materials**:
- Magnesium chips ignite easily (burn at 3100°F)
- Titanium chips pyrophoric when fine
- Composite dust explosive

**Prevention**:
- No water-based coolant on magnesium or titanium
- Mineral oil or approved coolants only
- Regular chip removal (no accumulation)
- Fire extinguisher (Class D for metal fires)

### Chip Hazards

**Sharp Chips**:
- Steel chips cut skin easily
- Long stringy chips wrap around tools (entanglement risk)

**Prevention**:
- Chip breaker geometry on tools
- Proper coolant pressure (break chips)
- Eye protection mandatory
- Gloves for chip removal (machine stopped!)
- Never remove chips by hand while machine running

### Coolant Hazards

**Health Risks**:
- Mist inhalation (respiratory irritation)
- Skin contact (dermatitis)
- Bacterial growth (bio-contamination)

**Prevention**:
- Mist collection system
- Proper coolant maintenance (pH, concentration)
- Skin barrier cream
- Wash hands frequently
- Material Safety Data Sheet (MSDS) review

## Parameter Starting Points

### Quick Reference by Material

| Material | Cutting Speed | Feed per Tooth | Notes |
|----------|---------------|----------------|-------|
| Aluminum 6061 | 600-1200 SFM | 0.005-0.015" | High speed, high feed |
| Brass | 400-800 SFM | 0.003-0.010" | Similar to aluminum |
| Mild Steel 1018 | 200-400 SFM | 0.003-0.008" | Moderate speed |
| Alloy Steel 4140 | 150-300 SFM | 0.002-0.006" | Harder, slower |
| Stainless 304 | 100-200 SFM | 0.002-0.005" | Work hardens, carbide tools |
| Tool Steel (RC 60) | 50-150 SFM | 0.001-0.003" | Very hard, carbide/ceramic |
| Titanium Ti-6Al-4V | 150-250 SFM | 0.002-0.005" | Low speed, sharp tools |
| Cast Iron | 250-500 SFM | 0.004-0.010" | Brittle chips, dry cut |
| Plastics (acrylic) | 500-1000 SFM | 0.003-0.010" | Sharp tools, avoid melt |
| Carbon Fiber | 500-800 SFM | 0.002-0.006" | Diamond tools, dust control |

**Note**: These are conservative starting points for carbide tooling. Adjust based on tool manufacturer data and actual results.

### Depth of Cut Guidelines

**Roughing**:
- ADOC: 0.5-1.5× tool diameter
- RDOC: 0.05-0.20× tool diameter (slotting avoid if possible)
- Goal: Maximum MRR without excessive load

**Finishing**:
- ADOC: 0.010-0.100" (light cut)
- RDOC: 0.010-0.030" (climb mill for best finish)
- Goal: Final dimensions and surface finish

**Example - 1/2" Endmill**:
- Roughing: ADOC = 0.5", RDOC = 0.1" (20% stepover)
- Finishing: ADOC = 0.030", RDOC = 0.015"

## Measurement and Verification

### Measuring Actual Feed Rate

**Method 1: Timed Distance**:
1. Jog to known start position
2. Execute G-code move (known distance)
3. Time with stopwatch
4. Calculate: Feed Rate = Distance / Time (convert to IPM or mm/min)

**Method 2: G-code Display**:
Most CNC controls display actual feed rate in real-time.

**Method 3: Chip Measurement**:
Measure chip thickness and compare to theoretical:
$$f_z = \frac{\text{chip thickness}}{\sin(\text{engagement angle})}$$

### Measuring Spindle Speed

**Tachometer**:
Optical or contact tachometer measures actual RPM.

**Sound Analysis**:
Spindle tone changes with RPM (experienced machinists "hear" speed).

**Strobe Light**:
Mark on spindle, strobe flashes sync with rotation.

**Control Display**:
Modern controls display commanded and actual RPM.

## Common Misconceptions

**Myth 1**: "Faster is always better"
- **Reality**: Faster RPM reduces tool life exponentially. Balance speed and life.

**Myth 2**: "More flutes = better"
- **Reality**: More flutes reduce chip space, risk clogging. 2-3 flutes often best for aluminum.

**Myth 3**: "Cutting oil prevents all problems"
- **Reality**: Poor parameters with coolant still fail. Coolant enhances good parameters.

**Myth 4**: "Speeds and feeds tables are exact"
- **Reality**: Tables are starting points. Adjust for specific machine, tool, and setup.

**Myth 5**: "Big machines need slow speeds"
- **Reality**: Machine rigidity enables higher speeds, not lower. Small machines may need conservative parameters due to flex.

## Learning Path

**Beginner** (Sections 20.1-20.3):
- Understand feed rate, spindle speed, DOC basics
- Calculate RPM from SFM
- Use manufacturer's starting values
- Focus on safe, conservative parameters

**Intermediate** (Sections 20.4-20.7):
- Optimize chip load for material
- Adjust for tool wear and life
- Select appropriate tooling grades
- Interpret tool wear patterns

**Advanced** (Sections 20.8-20.12):
- High-speed machining strategies
- Real-time adaptive control
- Economic optimization
- Troubleshoot complex problems

## Summary

Feeds and speeds are the foundation of successful CNC machining. Proper selection balances tool life, surface finish, cycle time, and cost.

**Key Principles**:
1. Cutting speed primarily affects tool life (exponential relationship)
2. Feed rate primarily affects surface finish (quadratic relationship)
3. MRR = DOC × WOC × F determines production rate
4. Always maintain minimum chip load (avoid rubbing)
5. Tables are starting points - adjust based on results
6. Safety first: conservative parameters until proven

**Next Steps**:
- Learn cutting mechanics (Section 20.2)
- Master RPM calculations (Section 20.3)
- Optimize feed rates (Section 20.4)
- Apply to specific materials (Section 20.6)

---

**Next**: [20.2 Cutting Mechanics and Tool Geometry](section-20.2-cutting-mechanics.md)
