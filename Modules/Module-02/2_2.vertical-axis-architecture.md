# Module 2 – Vertical Axis and Column Assembly

## 2. Vertical Axis Architecture

The architecture of a vertical axis system integrates mechanical, electrical, and control subsystems into a cohesive design that delivers precision vertical motion under gravitational load. This section provides comprehensive specifications, design rationale, and engineering trade-offs for each architectural element.

### 2.1 Travel Range: Determining Working Height

**Design Considerations:**

The Z-axis travel range determines the maximum part height that can be machined and influences nearly every other design parameter. The selection process balances workspace requirements against structural complexity and cost.

**Typical Applications:**

| Application | Travel Range | Rationale |
|-------------|--------------|-----------|
| Sheet metal plasma/laser | 100-150 mm | Limited part thickness, prioritize stiffness |
| General machining | 150-250 mm | Balanced capability for moderate parts |
| Large component machining | 250-400 mm | Heavy industrial, requires robust structure |
| 3D printing (large format) | 400-1000 mm | Tall build volumes, lower cutting forces |

**Structural Scaling:**

As travel increases, structural requirements scale unfavorably:

$$\delta \propto L^3$$

A 2× increase in travel requires 8× the structural moment of inertia to maintain the same deflection specification, typically resulting in 3-4× increase in column cross-section and mass.

**Design Example:**

**Requirement:** Plasma cutting of 25 mm steel plate
- Plate thickness: 25 mm
- Torch standoff: 3-5 mm
- Pierce height: 10 mm above plate
- Clearance for fixturing: 50 mm
- Safety margin: 20 mm

**Calculation:**
$$Travel = 25 + 5 + 10 + 50 + 20 = 110 \text{ mm minimum}$$

**Selected Travel:** 150 mm (provides operational flexibility)

### 2.2 Drive Type Selection: Ball-Screw vs. Belt Drive

**Ball-Screw Drive:**

*Advantages:*
1. High stiffness (minimal elastic deflection under load)
2. Zero backlash (with preload)
3. High positioning resolution
4. Predictable servo response
5. High force capacity (10-50 kN typical)

*Disadvantages:*
1. Higher cost ($200-$800 for precision grades)
2. Critical speed limitations
3. Requires lubrication maintenance
4. Acoustic noise at high speeds

**Engineering Analysis:**

Ball-screw stiffness:
$$k_{screw} = \frac{EA}{L}$$

For Ø20 mm screw, 400 mm length, steel:
$$k_{screw} = \frac{200 \times 10^9 \times \pi \times 0.01^2}{0.4} = 157 \times 10^6 \text{ N/m}$$

This high stiffness (157 N/μm) ensures the drive mechanism does not become the compliance-limiting element.

**Critical Speed:**

The critical rotational speed at which the screw becomes dynamically unstable:

$$n_{cr} = \frac{k \times 10^6 \times d_r}{L^2}$$

Where:
- $k$ = support factor (3.5 for fixed-supported, 4.7 for fixed-free)
- $d_r$ = root diameter (mm)
- $L$ = unsupported length (mm)

For Ø20 mm screw, 400 mm length, fixed-supported:
$$n_{cr} = \frac{3.5 \times 10^6 \times 18}{400^2} = \frac{63 \times 10^6}{160,000} = 393 \text{ rpm}$$

At 5 mm pitch: $v_{max} = 393 \times 0.005 = 1.97$ m/min

**Belt Drive:**

*Advantages:*
1. Lower cost ($50-$150 for complete drive)
2. No critical speed limitations
3. Quiet operation
4. No lubrication requirements
5. High speed capability (10-20 m/min feasible)

*Disadvantages:*
1. Lower stiffness (belt elasticity)
2. Potential backlash from belt stretch
3. Requires tension maintenance
4. Lower force capacity (500-2000 N typical)

**Belt Stiffness Analysis:**

Effective stiffness of tensioned timing belt:
$$k_{belt} = \frac{E_{eff} \cdot A_{belt}}{L_{span}} + \frac{T_{tension}}{elongation}$$

For GT2 belt, 800 mm span, 3000 N tension:
$$k_{belt} \approx 15 \times 10^6 \text{ N/m}$$ (approximately 10× lower than ball-screw)

**Application Guide:**

| Parameter | Choose Ball-Screw | Choose Belt |
|-----------|------------------|-------------|
| Cutting forces | > 500 N | < 200 N |
| Positioning accuracy | < 0.05 mm | 0.05-0.20 mm acceptable |
| Speed requirement | < 10 m/min | > 10 m/min |
| Budget | Premium acceptable | Cost-sensitive |
| Maintenance access | Good | Limited |

**For precision Z-axis applications (plasma, laser, milling):** Ball-screw is strongly preferred due to superior stiffness and accuracy.

### 2.3 Guide System: Linear Rails and Load Distribution

**Rail Selection Criteria:**

1. **Size (Width × Height):**
   Common sizes: MGN12, MGN15, HGR20, HGR25, HGR30
   
   Selection based on load capacity and moment resistance:
   
   | Rail Type | Dynamic Load (kN) | Moment Capacity (N·m) | Application |
   |-----------|-------------------|----------------------|-------------|
   | MGN12 | 1.7 | 12 | Light duty, 3D printing |
   | MGN15 | 2.8 | 24 | Light machining, laser |
   | HGR20 | 4.8 | 65 | Medium machining, plasma |
   | HGR25 | 7.3 | 125 | Heavy machining, milling |
   | HGR30 | 10.8 | 215 | Industrial machining |

2. **Preload Class:**
   - **Z0 (light preload):** 0.02C₀ - General purpose, low friction
   - **ZA (medium preload):** 0.04C₀ - Precision positioning
   - **ZB (heavy preload):** 0.08C₀ - High stiffness, vibration resistance

**Critical Design Parameter: Rail Spacing**

The moment arm provided by wide rail spacing dramatically improves pitching resistance:

$$\theta_{pitch} = \frac{M_{applied}}{k_{moment}}$$

Where moment stiffness:
$$k_{moment} = k_{rail} \times (d_{spacing})^2$$

**Worked Example:**

**Given:**
- Applied cutting force: $F = 400$ N
- Distance from rail centerline to tool tip: $L = 150$ mm
- Applied moment: $M = 400 \times 0.15 = 60$ N·m

**Case 1:** Rail spacing = 80 mm
- Single rail stiffness: $k_{rail} = 500$ N/μm = $5 \times 10^8$ N/m
- Moment stiffness: $k_M = 5 \times 10^8 \times 0.08^2 = 3.2 \times 10^6$ N·m/rad
- Angular deflection: $\theta = 60 / (3.2 \times 10^6) = 18.75 \times 10^{-6}$ rad
- Tip deflection: $\delta = 150 \times 18.75 \times 10^{-6} = 2.8$ μm

**Case 2:** Rail spacing = 120 mm
- Moment stiffness: $k_M = 5 \times 10^8 \times 0.12^2 = 7.2 \times 10^6$ N·m/rad
- Angular deflection: $\theta = 60 / (7.2 \times 10^6) = 8.33 \times 10^{-6}$ rad
- Tip deflection: $\delta = 150 \times 8.33 \times 10^{-6} = 1.25$ μm

**Result:** 50% increase in rail spacing (80→120 mm) reduces angular deflection by 55% and tip deflection by 55%.

**Design Rule:** 
$$d_{spacing} \geq 0.6 \times column\_width$$ (minimum)
$$d_{spacing} \geq 0.8 \times column\_width$$ (preferred)

### 2.4 Motor Orientation: Vertical vs. Horizontal Mounting

**Vertical Mounting (Motor Above Axis):**

*Advantages:*
1. Protected from chips and cutting fluids
2. Simplified cable management (stationary connections)
3. Direct drive possible (no gearbox needed)
4. Natural heat dissipation (convection upward)

*Disadvantages:*
1. Increases overall machine height
2. Adds rotating mass to moving assembly
3. Cable flexing at motor shaft
4. Requires sealed motor connectors

**Horizontal Mounting (Motor on Side):**

*Advantages:*
1. Compact vertical envelope
2. Motor remains stationary (longer life)
3. Fixed electrical connections
4. Easier motor replacement

*Disadvantages:*
1. Requires right-angle gearbox or belt/pulley transmission
2. Additional gear backlash (if gearbox used)
3. More complex mechanical design
4. Chip exposure (requires bellows protection)

**Heat Dissipation Analysis:**

Motor heat generation at 70% duty cycle:
$$Q = (P_{input} - P_{output}) \times duty$$

For 400W rated motor at 70% efficiency:
$$Q = (400 - 280) \times 0.7 = 84 \text{ W continuous}$$

This heat must be dissipated to prevent:
1. Thermal expansion of motor housing
2. Demagnetization of permanent magnets (>120°C risk)
3. Thermal gradient in column structure

**Cooling strategies:**
- Forced air cooling: 10-20 W/(m²·K) heat transfer coefficient
- Required surface area: $A = Q / (h \times \Delta T) = 84 / (15 \times 40) = 0.14$ m²
- Finned motor housing or attached heat sink recommended

**Recommended Configuration:**

For Z-axis travel < 250 mm and spindle mass < 5 kg:
- **Vertical mounting with sealed AC servo motor**
- Use motor brake to prevent gravity drop during power loss
- IP65 rated motor minimum
- Aluminum heat sink attached to motor frame

For Z-axis travel > 250 mm or spindle mass > 5 kg:
- **Horizontal mounting with right-angle gearbox**
- Ratio 3:1 to 5:1 for inertia matching
- Backlash-free gearbox (planetary or harmonic drive)
- Motor remains stationary (extended life)

### 2.5 Counterbalance Systems: Gravitational Force Compensation

**Fundamental Requirement:**

The counterbalance system must provide upward force equal to the weight of all moving components, reducing the motor's workload to only overcoming friction and accelerating mass (without the gravitational bias).

**Net Force Analysis (Unbalanced System):**

$$F_{motor} = ma + F_{friction} + mg \cdot sgn(direction)$$

For upward motion: Motor must lift weight AND accelerate
For downward motion: Motor must brake against falling weight

This asymmetry causes:
1. Servo tuning challenges (different gains needed for up vs. down)
2. Higher RMS motor current (thermal stress)
3. Asymmetric acceleration profiles
4. Increased bearing wear

**Net Force Analysis (Balanced System):**

$$F_{motor} = ma + F_{friction}$$

Gravitational term eliminated! Symmetric performance in both directions.

**Counterbalance Technologies:**

**1. Gas Springs:**

Nitrogen-charged gas springs provide nearly constant force over moderate strokes.

Force characteristic:
$$F(x) = F_0 \left(\frac{V_0}{V_0 - A x}\right)^n$$

Where:
- $F_0$ = initial force
- $V_0$ = initial gas volume
- $A$ = piston area
- $x$ = extension distance
- $n$ = polytropic exponent (≈ 1.2 for nitrogen)

For small displacements ($x << V_0/A$), force is approximately constant.

*Advantages:*
- Compact size
- No external power
- Adjustable force (via pressure)
- Long life (>1 million cycles)

*Disadvantages:*
- Force varies slightly with temperature
- Limited stroke (typically 0.5× compressed length)
- Progressive force characteristic

**Design Example:**

Moving mass: 6 kg → Required force: 58.9 N

Select: Two 300 N gas springs in parallel
- Initial compression: 80% of stroke
- Operating range: 70-90% compression
- Force variation over range: ±5%

**2. Counterweight System:**

Steel weights connected via cable and pulley provide constant gravitational counterforce.

$$F_{counterweight} = m_{weight} \times g$$

*Advantages:*
- Perfectly constant force
- No wear or degradation
- Temperature insensitive
- Simple and reliable

*Disadvantages:*
- Requires vertical space for weight travel
- Cable maintenance (lubrication, inspection)
- Pulley bearing friction
- More complex mechanical design

**Design Consideration:**

Cable routing over pulleys introduces friction:
$$F_{effective} = F_{weight} \times \eta_{pulley}^{n_{pulleys}}$$

For $\eta_{pulley} = 0.98$ (ball bearing pulley), 2 pulleys:
$$F_{effective} = F_{weight} \times 0.98^2 = 0.96 F_{weight}$$

4% force loss → Design for 104% of required counterweight mass.

**3. Constant-Force Springs:**

Tightly coiled springs that unroll to provide constant force.

*Advantages:*
- Compact
- No friction losses
- Long stroke capability

*Disadvantages:*
- Lower force capacity (typically < 50 N)
- Limited to light-duty applications
- Lateral space requirement for spring storage drum

**Tuning Procedure:**

1. Remove all external loads from Z-axis
2. Disable servo drive (free-wheeling mode)
3. Measure force required to move axis at constant velocity
   - Upward force: $F_{up}$
   - Downward force: $F_{down}$
4. Calculate ideal counterbalance force:
   $$F_{ideal} = \frac{F_{up} - F_{down}}{2}$$
5. Adjust counterbalance until $F_{up} \approx F_{down}$ (within ±10%)

**Verification:**
- Command slow velocity profile (50 mm/min) up and down
- Monitor motor current
- Target: <10% current variation between directions

### 2.6 Complete Architecture Summary Table

The following table provides comprehensive specifications for a precision vertical axis suitable for plasma cutting, laser cutting, and light milling applications:

| Component | Specification | Engineering Rationale | Notes |
|-----------|---------------|----------------------|-------|
| **Travel Range** | 150–250 mm | Covers typical plasma plate heights with margin | Increase for thicker materials |
| **Drive Type** | Ball-screw Ø16–25 mm | High stiffness, zero backlash, precision | Ø20 mm most common for medium loads |
| **Screw Pitch** | 5–10 mm | Balances speed and force capability | 5 mm for precision, 10 mm for speed |
| **Critical Speed Margin** | ≥ 30% margin; operate ≤ 80% of $n_{cr}$ | Avoids screw whipping and excessive vibration | Verify with end‑fixity factor and free length |
| **Screw Grade** | C5 or better | Position accuracy ≤ 0.023 mm/300 mm | C7 acceptable for non-precision work |
| **Guide Type** | Two linear rails | Distributed load, moment resistance | Single rail = inadequate moment capacity |
| **Rail Size** | 15–20 mm width | Load capacity 3-7 kN per rail pair | Scale with cutting forces |
| **Rail Spacing** | 80–120 mm | Maximizes moment arm for stiffness | Wider spacing = lower angular deflection |
| **Rail Preload** | Medium (ZA) or Heavy (ZB) | Eliminates play, increases stiffness | ZA for general, ZB for heavy cutting |
| **Motor Orientation** | Vertical (above) or Horizontal (side) | Vertical for chip protection, Horizontal for compactness | Trade-off between protection and height |
| **Motor Type** | AC Servo, 400-750W | Sufficient torque for acceleration + cutting forces | Include brake for gravity holding |
| **Motor Brake** | Electromechanical, 2-5 Nm | Prevents drop during power loss | Critical safety feature |
| **Gearbox** | 3:1 to 5:1 planetary (if used) | Inertia matching, torque multiplication | Backlash-free design required |
| **Counterbalance Type** | Gas spring or counterweight | Eliminates gravitational bias | Gas spring for compactness |
| **Counterbalance Force** | 100-110% of moving mass weight | Slight overbalance compensates friction | Adjustable design preferred |
| **Column Cross-Section** | 100×100 to 150×150 mm RHS | High moment of inertia, low deflection | Steel or aluminum with internal ribs |

### 2.7 Servo Integration and Torque Sizing (with Efficiency)

The servo must overcome gravity, friction, and commanded acceleration. Including screw efficiency $\eta$ and lead $L_{\text{lead}}$:
$$
T_{\text{req}} = \frac{L_{\text{lead}}}{2\pi\,\eta}\Big( m\,a + F_{\text{friction}} + m g \Big)
$$
Reflected linear inertia at the motor shaft is
$$
J_{\text{ref}} = m\left(\frac{L_{\text{lead}}}{2\pi}\right)^{2}, \qquad J_{\text{eq}} = J_m + J_{\text{ref}} + J_{\text{coupling}} + J_{\text{screw}}
$$
Maintain $J_{\text{ref}}/J_m$ between 1:1 and 5:1 for robust tuning.

**Worked Example – 200 mm Z‑Axis:**
Given $m=8$ kg, $L_{\text{lead}}=0.005$ m, $a=2.0\,g$, $F_{\text{friction}}=10$ N, $\eta=0.92$:
$$
T_{\text{req}} = \frac{0.005}{2\pi\cdot 0.92}\Big(8\cdot 2\cdot 9.81 + 10 + 8\cdot 9.81\Big) \approx 0.46\,\text{N·m}
$$
With a 3:1 gearbox, motor torque reduces to ~0.15 N·m (at 3× reflected inertia). Verify thermal limits and add 20–30% margin.

Feedforward improves tracking:
$$
T_{\text{ff}} = J_{\text{eq}}\,\frac{2\pi}{L_{\text{lead}}}\,\ddot{z} + \frac{L_{\text{lead}}}{2\pi\,\eta}\,F_{\text{friction}}(\dot{z})
$$
Tune gains while respecting the natural frequency target (≥5× servo bandwidth).

### 2.8 Brake Sizing and Drop Safety

The holding brake must prevent gravity‑induced motion during power loss:
$$
T_{\text{brake}} \ge \frac{L_{\text{lead}}}{2\pi\,\eta}\,m g \times S_f
$$
with safety factor $S_f$ (typically 1.5–2.5). For $m=8$ kg, $L_{\text{lead}}=5$ mm, $\eta=0.92$, $S_f=2$:
$$
T_{\text{brake}} \ge \frac{0.005}{2\pi\cdot 0.92} (8\cdot 9.81) \times 2 \approx 0.13\,\text{N·m}
$$
Select the next larger standard brake (e.g., 2.5 N·m) to account for wear, contamination, and incline. Add mechanical hard‑stops and soft‑limits; verify weekly during maintenance.

#### 2.8.1 Brake Verification Test (Commissioning)

Purpose: Confirm the holding brake prevents gravity‑induced motion and that no hazardous sag occurs during power loss.

Procedure:
- Jog Z to mid‑stroke; stop motion and engage brake (power ON).
- Disable servo drive power to simulate power loss; observe position with a 0.01 mm dial indicator.
- Re‑enable power; lift 2–3 mm; repeat test 3× to check repeatability.

Acceptance Criteria:
- Sag/displacement ≤ 0.05 mm within 10 s after power removal.
- No sustained downward drift (> 0.05 mm/min) while brake engaged.
- On re‑energizing, inrush current spike is transient; no prolonged overcurrent alarm.

If Fails:
- Increase brake size or adjust brake airgap per manufacturer spec.
- Reduce counterbalance over‑ or under‑bias to minimize net gravity load.
- Inspect screw/nut friction (contamination) and verify brake wiring/voltage.
| **Column Material** | Steel or Aluminum | Steel for stiffness, Aluminum for mass reduction | Consider thermal expansion |
| **Natural Frequency** | ≥ 150 Hz | Ensure > 5× servo bandwidth | Verify with FEA and accelerometer testing |
| **Cable Carrier** | Enclosed drag chain | Protects cables, manages flexing | Size for ≥ 2× cable bend radius |
| **Position Feedback** | Encoder 0.001 mm resolution | Closed-loop control, positioning accuracy | Rotary on motor or linear on axis |
| **Limit Switches** | Mechanical + inductive proximity | Hard limits (crash protection) + soft limits (control) | Dual redundancy for safety |

**Design Integration Notes:**

1. **Electrical Integration:**
   - Motor power cable: Shielded, oil-resistant, 1.5× rated current capacity
   - Encoder cable: Twisted-pair, shielded, separate conduit from power
   - Limit switch wiring: 24V DC logic, optically isolated inputs
   - Emergency stop loop: Hardwired series circuit, NC contacts

2. **Lubrication System:**
   - Ball-screw: Automatic grease injector every 8 hours operation
   - Linear rails: Manual regreasing every 6 months (via zerk fittings)
   - Grease type: NLGI Grade 2, lithium-based, -20°C to +120°C

3. **Thermal Management:**
   - Motor heat sink: Natural convection or forced air
   - Column insulation: Separate motor thermal mass from structure
   - Temperature monitoring: Thermistor on motor winding, shutdown at 130°C

4. **Safety Systems:**
   - Motor brake: Engages on power loss, prevents gravity drop
   - Counterbalance: Sized to prevent free-fall (even if brake fails)
   - Bellows/covers: Protect ball-screw from chip contamination
   - Software limits: Prevent over-travel before hitting hard stops

This comprehensive architecture provides a robust foundation for precision vertical axis performance across diverse CNC applications.

***


---

## References

1. **ISO 14728-1:2017** - Rolling bearings - Linear motion rolling bearings - Dynamic load ratings
2. **THK Linear Motion Systems Catalog** - Z-axis configurations and mounting
3. **Hiwin Linear Guideway Technical Manual** - Vertical axis applications
4. **NSK Linear Guides CAT. No. E728g** - Profile rail systems for vertical mounting
5. **Weck, M. & Brecher, C. (2006).** *Machine Tools 1*. Springer
6. **SKF Linear Motion & Actuation** - Vertical axis design guidelines
