## 14. Carriage & Bearing Preload Tuning: Optimizing Stiffness, Life, and Friction

### 14.1 The Role of Preload in Linear Bearing Systems

Profile rail linear guides achieve precision through **recirculating ball bearings** that run in precisely ground raceways. The critical design parameter is **preload**—the internal force that eliminates clearance between balls and raceways, providing:

**1. Increased Stiffness**
- Eliminates lost motion from clearance
- Provides linear load-displacement relationship
- Typical stiffness increase: 2–4× vs. zero-preload

**2. Improved Accuracy**
- Eliminates play (backlash) in all directions
- Maintains consistent position under varying loads
- Reduces vibration and chatter

**3. Moment Rigidity**
- Resists angular errors (pitch, yaw, roll)
- Critical for multi-block carriages carrying offset loads

**Trade-offs:**
- **Higher preload** → Higher stiffness, shorter life (increased rolling resistance)
- **Lower preload** → Longer life, lower stiffness, potential for vibration
- **Optimal preload** balances performance requirements with desired service life

### 14.2 Preload Classification System

Manufacturers (THK, HIWIN, NSK) use standardized preload classes:

| Preload Class | Preload Force | Relative Stiffness | Typical Application | Service Life Impact |
|---------------|--------------|-------------------|---------------------|-------------------|
| **Z0** (Light) | ~5% of $C$ | 1.0× (baseline) | High-speed, low-load applications | 1.2–1.5× rated life |
| **Z1** (Medium) | ~10% of $C$ | 1.5–2.0× | General CNC, moderate loads | 1.0× rated life (standard) |
| **Z2** (Heavy) | ~15% of $C$ | 2.0–3.0× | High-stiffness, heavy cutting | 0.6–0.8× rated life |
| **ZA** (Custom) | Specified | Variable | Special applications | Depends on preload level |

where $C$ = dynamic load rating of the bearing block.

**Example**: HGR25 block, $C = 32,760$ N
- Z0: $F_{preload} = 0.05 \times 32,760 = 1,638$ N
- Z1: $F_{preload} = 0.10 \times 32,760 = 3,276$ N
- Z2: $F_{preload} = 0.15 \times 32,760 = 4,914$ N

**Selection Criteria:**

**Use Z0 (Light Preload) when:**
- Axis speed >50 m/min (minimize friction heating)
- Long service life is priority (>10,000 hours)
- Loads are light (<30% of $C$)
- Example: Laser cutting X/Y axes (rapid positioning, low force)

**Use Z1 (Medium Preload) when:**
- General-purpose CNC with moderate loads
- Balanced stiffness and life requirements
- Most common choice for gantry machines
- Example: Plasma/router Y-axis (gantry motion)

**Use Z2 (Heavy Preload) when:**
- High stiffness is critical (precision machining)
- Cutting forces are high (spindle milling)
- Servo bandwidth >20 Hz requires maximum stiffness
- Example: Z-axis with heavy cutting loads

### 14.3 Carriage Configuration: Block Quantity and Spacing

#### **14.3.1 Single vs. Multiple Blocks per Rail**

**Minimum Configuration: 2 Blocks per Carriage**
- Provides line of support (prevents rotation about rail axis)
- Suitable for light loads, short spans
- Stiffness limited by individual block capacity

**Standard Configuration: 4 Blocks per Carriage**
- Two pairs of blocks per rail (front and rear)
- Spacing $S$ between pairs provides moment arm
- Distributes load, increases moment rigidity
- Most common for CNC gantry machines

**Heavy-Duty Configuration: 6+ Blocks per Carriage**
- Three or more pairs per rail
- Used for very long spans (>3 m) or heavy loads
- Diminishing returns beyond 6 blocks (center blocks carry less load)

#### **14.3.2 Block Spacing Optimization**

**Rule of Thumb:**

$$S = 0.6 \text{ to } 0.9 \times L_{axis}$$

where:
- $S$ = spacing between front and rear block pairs
- $L_{axis}$ = total axis travel

**Rationale**: Wider spacing increases moment rigidity but:
- Too wide (>0.9 $L_{axis}$): Blocks approach travel limits, wasted rail length
- Too narrow (<0.6 $L_{axis}$): Insufficient moment arm, poor pitch/yaw rigidity

**Example**: Y-axis, 2,500 mm travel
- Optimal spacing: $S = 0.7 \times 2,500 = 1,750$ mm
- Rail length required: $2,500 + 2 \times 100 \text{ (margin)} + 1,750 \text{ (spacing)} = 4,350$ mm
- Standard rail: 4,500 mm (nearest available length)

**Moment Stiffness Calculation:**

For dual-block carriage with spacing $S$, subjected to moment $M$:

$$k_{moment} = \frac{2 k_{block} S^2}{4}$$

where $k_{block}$ = stiffness of single block in vertical direction (typically 50–150 N/µm).

For HGR25, $k_{block} \approx 100$ N/µm, $S = 300$ mm:

$$k_{moment} = \frac{2 \times 100 \times 300^2}{4} = \frac{1.8 \times 10^{7}}{4} = 4.5 \times 10^{6} \text{ N·mm/rad}$$

### 14.4 Preload Verification and Adjustment

#### **14.4.1 Manual Push-Pull Force Measurement**

**Tool**: Digital fish scale or force gauge (0–200 N capacity, ±1 N accuracy)

**Procedure**:
1. Install bearing blocks on rail (no external load)
2. Attach force gauge to block via hook or threaded hole
3. Pull horizontally at constant slow speed (~10 mm/s)
4. Record peak force (initial breakaway) and sustained force (running)

**Acceptance Criteria** (for HGR20/25):

| Preload Class | Peak Force (N) | Running Force (N) | Assessment |
|---------------|---------------|------------------|------------|
| Z0 | 20–40 | 15–30 | Light, smooth motion |
| Z1 | 50–90 | 35–70 | Moderate resistance |
| Z2 | 100–180 | 70–140 | Firm, substantial resistance |

**Note**: Actual values vary by manufacturer, block size, and lubrication state. Perform test after initial lubrication and 10 full-travel break-in cycles.

#### **14.4.2 Stiffness Measurement via Dial Indicator**

**Setup**:
- Mount carriage rigidly to rail via bearing blocks
- Attach dial indicator (0.001 mm resolution) to carriage, stylus pointing down
- Place indicator stylus on rigid surface (granite plate)

**Test**:
1. Apply known force $F$ (use calibrated weight or load cell) vertically through carriage center
2. Record deflection $\delta$ on indicator
3. Calculate stiffness: $k = F / \delta$

**Example**:
- Applied force: $F = 500$ N (51 kg weight)
- Measured deflection: $\delta = 0.008$ mm
- Stiffness: $k = 500 / 0.008 = 62,500$ N/mm = 62.5 N/µm

**Compare to Manufacturer Specification:**
- HGR25, Z1 preload: $k_{spec} \approx 100$ N/µm (vertical)
- Measured: 62.5 N/µm → **62% of spec** (possible causes: insufficient preload, worn balls, contamination)

**Corrective Actions**:
- Clean and re-lubricate blocks
- Replace blocks if wear limits reached
- Verify proper preload class ordered (check part number)

### 14.5 Rail Pitch and Parallel Axis Configuration

#### **14.5.1 Rail Pitch (Width) Selection**

**Rule**: Rail pitch $W \geq H/2$

where:
- $W$ = distance between parallel rails (center-to-center)
- $H$ = height of structure being supported

**Rationale**: Wider rail spacing increases moment rigidity about roll axis (rotation around axis of travel).

**Example**: Gantry beam, height $H = 180$ mm
- Minimum rail pitch: $W = 180/2 = 90$ mm
- Practical: Use $W = 150$–200 mm for better roll stiffness

**Roll Stiffness:**

For two parallel rails spaced $W$ apart, each with stiffness $k$:

$$k_{roll} = 2 k W^2$$

For HGR25 rails ($k = 100$ N/µm) spaced $W = 150$ mm:

$$k_{roll} = 2 \times 100 \times 150^2 = 4.5 \times 10^{6} \text{ N·mm/rad}$$

#### **14.5.2 Parallelism Tolerance Between Rails**

**Specification**: Rails must be parallel within ±0.02–0.03 mm over full length.

**Effect of Misalignment:**

If rails deviate from parallel by $\delta_{parallel}$ over span $L$:

$$F_{binding} = k_{block} \times \delta_{parallel}$$

For $\delta_{parallel} = 0.05$ mm, $k_{block} = 100$ N/µm:

$$F_{binding} = 100 \times 0.05 = 5,000 \text{ N}$$

**Result**: 5,000 N binding force between rails → excessive wear, potential block failure!

**Mitigation**: Maintain parallelism per Section 12.3.2 (10-step installation procedure).

### 14.6 Lubrication Impact on Preload Performance

#### **14.6.1 Lubrication Regimes**

**Starved Lubrication** (insufficient grease):
- High friction, rapid wear
- Preload effectiveness reduced (balls don't roll smoothly)
- Life reduced to 10–30% of rated

**Optimal Lubrication**:
- Thin film of NLGI #2 lithium grease visible at seals
- Smooth motion, minimal friction
- Full rated life achieved

**Over-Lubrication**:
- Excess grease causes churning, heat generation
- Speed limited due to viscous drag
- Seal failure from pressure buildup

**Recommendation**: Follow manufacturer lubrication schedule (Section 12.7.1): 500–1,000 km or 6 months, 2–3 cc per block.

#### **14.6.2 Temperature Effects**

Elevated temperature reduces grease viscosity and preload force:

**Preload Force vs. Temperature:**
- At 20°C: $F_{preload,nominal}$
- At 60°C: $F_{preload} \approx 0.85 \times F_{preload,nominal}$ (15% reduction)
- At 80°C: $F_{preload} \approx 0.70 \times F_{preload,nominal}$ (30% reduction)

**Design Consideration**: If operating temperature >50°C (e.g., near plasma torch), specify one preload class higher to maintain stiffness.

### 14.7 Preload Adjustment in the Field

Most profile rail blocks have **non-adjustable preload** (set at factory). However, adjustments can be made via:

**Method 1: Shim Adjustment (Parallel Rails)**
- Insert precision shims (0.025–0.050 mm brass) between one rail and mounting surface
- Effect: Increases effective preload by forcing blocks slightly closer together
- **Caution**: Excessive shimming (>0.1 mm) can overload balls, causing premature failure

**Method 2: Block Replacement**
- Replace worn Z1 blocks with new Z2 blocks (higher preload)
- Immediate stiffness increase, no structural changes required
- Cost: $50–150 per block depending on size

**Method 3: Parallel Rail Adjustment**
- Slightly converge rails (narrow pitch by 0.05–0.10 mm at one end)
- Creates wedging effect, increases preload
- **Risk**: Binding if misapplied; requires precise measurement

**Recommendation**: Use Method 2 (block replacement) for predictable, controlled preload increase.

### 14.8 Acceptance Testing and Commissioning

**Test 1: Manual Motion Smoothness**
- [ ] Push carriage by hand through full travel at 10 mm/s
- [ ] Motion feels smooth, no binding or tight spots
- [ ] Preload force consistent (measured with force gauge: ±10% variation)

**Test 2: Stiffness Verification**
- [ ] Apply 500 N vertical load at carriage center
- [ ] Measure deflection with dial indicator
- [ ] Stiffness ≥80% of manufacturer specification

**Test 3: No Audible Noise**
- [ ] Traverse axis at 50% rapid speed (e.g., 20 m/min)
- [ ] No grinding, rumbling, or irregular sounds
- [ ] Only smooth rolling noise acceptable

**Test 4: Temperature Rise**
- [ ] Run axis continuously at 50% rapid speed for 30 minutes
- [ ] Measure bearing block temperature with IR thermometer
- [ ] Temperature rise <20°C above ambient (indicates proper lubrication)

**Test 5: Position Repeatability**
- [ ] Command axis to same position 10 times, measure with 0.001 mm indicator
- [ ] Repeatability (2σ) ≤ 0.010 mm
- [ ] No systematic drift (indicates preload stability)

**Acceptance**: All 5 tests must pass before system released to production.

***


---

## References

1. **ISO 14728-1:2017** - Rolling bearings - Linear motion rolling bearings - Dynamic load ratings
2. **THK Linear Motion Systems General Catalog** - Preload selection and bearing life
3. **Hiwin Mega Preload Series Technical Manual** - Preload adjustment procedures
4. **SKF Linear Motion & Actuation Catalog** - Bearing friction and stiffness data
5. **Harris, T.A. & Kotzalas, M.N. (2006).** *Rolling Bearing Analysis* (5th ed.). CRC Press
6. **NSK Linear Guides Technical Report** - Preload effects on stiffness and life
