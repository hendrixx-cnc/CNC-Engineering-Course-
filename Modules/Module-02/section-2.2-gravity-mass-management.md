# Section 2.2 – Gravity and Mass Management

## Overview

Gravity is the defining challenge of vertical axis design. Every kilogram of moving mass creates a constant 9.81 N downward force that the motor must resist continuously. This section presents systematic approaches to mass reduction, counterbalancing, and inertia management that transform vertical axis performance from adequate to exceptional.

## The Gravitational Challenge

### Continuous Energy Demand

Unlike horizontal axes where motors work only during acceleration, vertical axes require continuous torque output:

**Potential energy during vertical motion:**

$$\Delta E_p = m \cdot g \cdot \Delta z$$

Where:
- m = moving mass (kg)
- g = gravitational acceleration (9.81 m/s²)
- Δz = vertical displacement (m)

**Example calculation:**

For a 10 kg spindle assembly moving 300 mm:

$$\Delta E_p = 10 \times 9.81 \times 0.3 = 29.43 \text{ J}$$

**Moving upward:** Motor supplies 29.43 J + kinetic energy + friction losses

**Moving downward:** Motor must dissipate 29.43 J - kinetic energy extraction

### Asymmetric Performance

Without counterbalancing, vertical axes exhibit asymmetric behavior:

**Upward acceleration:**
$$T_{motor} = (F_{accel} + F_{gravity} + F_{friction}) \times r_{lead}$$

**Downward acceleration:**
$$T_{motor} = (F_{accel} - F_{gravity} + F_{friction}) \times r_{lead}$$

Where:
- $F_{accel} = m \times a$ (acceleration force)
- $F_{gravity} = m \times g$ (gravitational force)
- $F_{friction}$ (bearing and screw friction)
- $r_{lead}$ (ball screw lead radius)

**Result:** Different acceleration capabilities in each direction, servo tuning compromises, increased thermal load.

### Holding Torque Requirement

Even when stationary, the motor must supply holding torque:

$$T_{hold} = \frac{m \cdot g \cdot p}{2\pi \eta}$$

Where:
- p = ball screw pitch (m)
- η = screw efficiency (typically 0.90-0.95)

**Example:**

10 kg mass, 5 mm pitch, 90% efficiency:

$$T_{hold} = \frac{10 \times 9.81 \times 0.005}{2\pi \times 0.90} = 0.087 \text{ N·m}$$

This continuous load generates heat and contributes to thermal drift.

## Mass Reduction Strategies

### Material Selection

**High-strength aluminum alloys:**

| Alloy | Yield Strength (MPa) | Density (g/cm³) | Strength-to-Weight Ratio |
|-------|---------------------|-----------------|--------------------------|
| **6061-T6** | 275 | 2.70 | 102 |
| **7075-T6** | 505 | 2.81 | 180 |
| **7068-T6** | 550 | 2.85 | 193 |

**Comparison to steel:**
- Steel 4140: 415 MPa yield, 7.85 g/cm³, ratio = 53
- Aluminum 7075-T6 provides 3.4× better strength-to-weight ratio

**Application:**
- Use 6061-T6 for general carriage structures (easier to machine)
- Use 7075-T6 for highly stressed components (spindle mounts, bearing blocks)
- Reserve 7068-T6 for ultimate performance (expensive, limited availability)

**Magnesium alloys (specialized applications):**

| Alloy | Yield Strength (MPa) | Density (g/cm³) | Strength-to-Weight Ratio |
|-------|---------------------|-----------------|--------------------------|
| **AZ91D** | 160 | 1.81 | 88 |
| **WE43** | 200 | 1.84 | 109 |

**Advantages:**
- 33% lighter than aluminum for same volume
- Excellent vibration damping
- Good machinability

**Disadvantages:**
- Lower stiffness (E = 45 GPa vs 70 GPa for aluminum)
- Fire hazard during machining (requires proper precautions)
- Higher cost
- Galvanic corrosion concerns with steel fasteners

### Topology Optimization

Modern CAD/FEA software enables topology optimization to remove non-structural material:

**Process:**
1. Define design space and loads
2. Specify mass reduction target (e.g., 30%)
3. Run iterative FEA optimization
4. Generate organic structure concentrating material where needed
5. CAM organic geometry or simplify for conventional machining

**Results:**
- 30-50% mass reduction with same stiffness
- Complex organic shapes (best for additive manufacturing or 5-axis milling)
- Improved structural efficiency

**Practical approach for conventional machining:**
- Start with topology-optimized design
- Simplify to machinable geometry (pockets, webs, lightening holes)
- Verify with FEA that simplification maintains stiffness

### Hollow Core Structures

Replace solid sections with hollow profiles:

**Weight savings example:**

Solid aluminum plate: 150mm × 150mm × 25mm = 1.52 kg

Hollow section with 6mm walls:
- Outer: 150mm × 150mm × 25mm = 1.52 kg
- Remove: 138mm × 138mm × 13mm = 0.68 kg
- **Net weight: 0.84 kg (45% reduction)**

Stiffness (bending):
- Solid: I = 19.5 × 10⁴ mm⁴
- Hollow: I = 15.8 × 10⁴ mm⁴ (19% reduction)

**Efficiency improvement:**
- Weight reduced 45%
- Stiffness reduced 19%
- Stiffness-to-weight ratio improved 46%

### Component Integration

Combine multiple parts into single machined components:

**Example: Spindle mount with bearing blocks**

**Separate components:**
- Spindle mount plate: 2.5 kg
- Two bearing blocks: 0.8 kg each
- Fasteners: 0.2 kg
- Total: 4.3 kg

**Integrated design:**
- Single machining from billet
- Bearing bores machined in-situ
- Ribbed structure for stiffness
- Total: 2.8 kg (35% reduction)

**Benefits:**
- Weight reduction
- Improved alignment (no fastener stack-up)
- Reduced assembly time
- Increased stiffness (no joint compliance)

## Counterbalancing Systems

### Gas Spring Counterbalance

**Principle:** Compressed gas provides constant force over travel range.

**Gas spring characteristics:**

$$F(x) = F_0 \left(\frac{V_0}{V_0 - A \cdot x}\right)^n$$

Where:
- $F_0$ = initial force at x=0
- $V_0$ = initial gas volume
- A = piston area
- x = extension distance
- n = polytropic index (≈1.3 for typical gas springs)

**Simplified approximation:**

For travel << gas spring stroke (typical case):

$$F(x) \approx F_0 + k_{gas} \cdot x$$

Where $k_{gas}$ = spring rate (typically 0.5-2.0 N/mm)

**Design procedure:**

1. **Calculate required force:**
   $$F_{required} = m \cdot g = \text{moving mass} \times 9.81$$

2. **Select gas spring(s):**
   - Standard sizes: 50N, 100N, 200N, 400N, 600N, 1000N
   - For precise balance, use multiple springs in parallel
   - Example: 78N required → Use two 40N springs

3. **Mounting geometry:**
   - Ensure force vector aligns with Z-axis (±5° max deviation)
   - Mounting point moves with carriage
   - Fixed anchor point on column

4. **Adjustment:**
   - Some gas springs have adjustable end fittings (±10mm travel)
   - Fine-tune balance by adjusting mounting position
   - Verify force balance across full travel range

**Example system:**

Moving mass: 8 kg
Required force: 78.5 N

Gas spring selection:
- Two Stabilus Lift-O-Mat 40N springs in parallel
- Stroke: 100mm (Z-axis travel: 250mm, spring extends ~80mm)
- Mounting angle: 3° from vertical (force loss <0.2%)
- Spring rate: 0.8 N/mm each
- Force variation over 80mm: ±3.2N (4% of total force)

**Advantages:**
- Simple installation
- No external power required
- Low friction
- Compact

**Disadvantages:**
- Force variation over stroke (typically ±5-10%)
- Fixed balance (difficult to adjust for different spindles)
- Temperature sensitivity (force changes ~0.3%/°C)

### Weight-Cable Counterbalance

**Principle:** Hanging weight connected via cables and pulleys provides constant gravitational force.

**Force relationship:**

$$F_{counterweight} = m_{weight} \cdot g$$

For direct 1:1 cable arrangement:
$$m_{weight} = m_{moving\\_mass}$$

**Mechanical advantage:**

Using pulleys, the counterweight mass can be reduced:

For 2:1 mechanical advantage (cable doubled back):
$$m_{weight} = \frac{m_{moving\\_mass}}{2}$$

**Design considerations:**

1. **Cable selection:**
   - Stainless steel aircraft cable (7×19 construction typical)
   - Diameter: 2-4mm for most applications
   - Working load: 5× static load minimum safety factor
   - Low-friction UHMW or Delrin pulleys

2. **Pulley arrangement:**
   ```
   Column top
       |
   [Pulley 1] ← Fixed to column
       |
       ├──Cable to carriage
       |
   [Pulley 2] ← On carriage
       |
   [Counterweight] ← Hangs in column cavity
   ```

3. **Counterweight design:**
   - Steel plates (easy to add/remove for adjustment)
   - Enclosure prevents cable fouling
   - Limit stops at top and bottom of travel

4. **Cable tensioning:**
   - Turnbuckle or adjustable fastener for fine-tuning
   - Tension should eliminate slack without preloading carriage

**Advantages:**
- Constant force over full travel (no spring rate)
- Easy to adjust (add/remove weight plates)
- No temperature sensitivity
- Works with any moving mass

**Disadvantages:**
- Requires space inside column for weight travel
- More complex installation
- Cable stretch over time (minimal with steel cable)
- Requires periodic inspection

**Example system:**

Moving mass: 15 kg
Counterweight: 15 kg (steel plates)
Cable: 3mm stainless steel 7×19, 480 kg breaking strength
Pulleys: 50mm diameter, sealed ball bearing
Mechanical advantage: 1:1 (direct connection)

Safety factor: 480 kg / (15 kg × 9.81 N/kg) = 3.3× (acceptable for static load with inspection)

### Pneumatic Counterbalance

**Principle:** Compressed air cylinder provides adjustable force.

**Force calculation:**

$$F_{cylinder} = P \cdot A_{piston}$$

Where:
- P = air pressure (Pa or psi)
- $A_{piston}$ = piston area (m² or in²)

**Example:**

Cylinder bore: 50mm (area = 1963 mm² = 3.04 in²)
Air pressure: 90 psi (6.2 bar)
Force: 3.04 in² × 90 psi = **274 lbs (1218 N)**

**Design procedure:**

1. **Select cylinder size** based on required force and available pressure
2. **Install pressure regulator** for fine-tuning balance
3. **Mount cylinder** with rod connected to carriage, body to column
4. **Adjust pressure** to achieve balance

**Advantages:**
- Easily adjustable (change air pressure)
- Constant force over stroke
- Can adapt to different spindle weights quickly

**Disadvantages:**
- Requires compressed air supply
- Air leaks over time (requires periodic adjustment)
- Friction in cylinder (typically 5-10% of force)
- More complex installation

**Application:**

Best for machines with:
- Multiple spindle configurations
- Frequent spindle changes
- Available compressed air infrastructure
- Need for remote adjustment capability

### Hydraulic Counterbalance

**Principle:** Hydraulic cylinder with accumulator maintains constant pressure.

**System components:**
- Hydraulic cylinder (typically 32-80mm bore)
- Bladder accumulator (maintains pressure)
- Pressure relief valve (safety)
- Check valve (prevents pressure loss)
- Fill port (for adjustment)

**Advantages:**
- Very constant force (hydraulic fluid incompressible)
- Highest load capacity
- No air compressor required
- Self-contained system

**Disadvantages:**
- Most expensive option
- Requires hydraulic expertise for installation
- Potential for leaks
- Heavier system weight

**Application:**

Best for:
- Very heavy spindles (>30 kg)
- High-precision requirements
- Industrial/production machines
- Where hydraulic power already available

## Counterbalance Design Example

### System Requirements

**Machine specifications:**
- Z-axis travel: 400mm
- Moving mass: 12 kg (spindle + carriage)
- Required force: 12 × 9.81 = 117.7 N
- Balance target: ±5% (111.8 - 123.6 N acceptable)

### Solution: Dual Gas Spring System

**Gas spring selection:**

Two Stabilus Lift-O-Mat 60N springs in parallel:
- Individual force: 60N at mid-stroke
- Combined force: 120N
- Spring rate: 1.0 N/mm per spring
- Stroke: 150mm (adequate for 400mm Z-travel with linkage)

**Mounting geometry:**

```
Column (fixed)
    |
    |  [Spring 1]
    |    /
    |   /  ← 5° angle
    |  /
    |─●  Carriage mounting point
    |  \
    |   \  ← 5° angle
    |    \
    |  [Spring 2]
    |
```

Springs mount at ±5° from vertical:
- Vertical force component: 120N × cos(5°) = 119.5N
- Horizontal forces cancel (symmetric arrangement)

**Force variation calculation:**

Over 400mm Z-travel, each spring extends ~130mm:
- Spring rate: 1.0 N/mm
- Force increase: 130mm × 1.0 N/mm = 130N total (both springs)
- Initial force: 120N at mid-stroke
- Final force: 120N + (130N × 0.5 from mid to end) = 185N

**Correction:** Use spring mounting linkage to create near-constant force:

With proper linkage geometry (effective lever arm changes):
- Force variation reduced to ±8N (±6.7% of nominal)
- Within acceptable ±5% target with fine-tuning

**Adjustment procedure:**

1. Install springs with adjustable mounting brackets
2. Position carriage at mid-travel
3. Release motor (with brake engaged for safety)
4. Adjust spring mounting position until carriage self-supports
5. Verify balance at top and bottom of travel
6. Fine-tune mounting position to minimize variation
7. Lock adjustment and verify security

## Moment of Inertia Management

### Reflected Inertia

Moving mass reflects to the motor shaft as rotational inertia:

$$J_{reflected} = \frac{m_{load}}{(2\pi / p)^2}$$

Where:
- $m_{load}$ = linear moving mass (kg)
- p = ball screw pitch (m/rev)

**Example:**

Moving mass: 10 kg
Ball screw pitch: 5mm = 0.005 m/rev

$$J_{reflected} = \frac{10}{(2\pi / 0.005)^2} = \frac{10}{(1256.6)^2} = 6.33 \times 10^{-6} \text{ kg·m}^2$$

**Comparison to motor inertia:**

Typical NEMA 23 servo motor: $J_{motor} = 3 \times 10^{-6}$ kg·m²

Inertia ratio: $\frac{J_{reflected}}{J_{motor}} = \frac{6.33}{3} = 2.1:1$

**Servo tuning implications:**

Ideal inertia ratio: 1:1 to 3:1
- Lower ratio: Responsive, may resonate
- Higher ratio: Stable, reduced bandwidth
- Above 10:1: Difficult to tune, sluggish response

### Optimizing Inertia Ratio

**Option 1: Increase ball screw pitch**

Changing from 5mm to 10mm pitch:

$$J_{reflected} = \frac{10}{(2\pi / 0.010)^2} = 1.58 \times 10^{-6} \text{ kg·m}^2$$

Inertia ratio: 1.58 / 3 = 0.53:1 (excellent)

Trade-off: Higher pitch reduces resolution and increases gravitational torque demand.

**Option 2: Larger motor**

Select NEMA 34 motor with $J_{motor} = 1 \times 10^{-5}$ kg·m²

Inertia ratio: 6.33 / 10 = 0.63:1 (excellent)

Trade-off: Larger motor adds weight, cost, and may not fit package.

**Option 3: Reduce moving mass**

Reduce mass from 10 kg to 6 kg through design optimization:

$$J_{reflected} = \frac{6}{(1256.6)^2} = 3.80 \times 10^{-6} \text{ kg·m}^2$$

Inertia ratio: 3.80 / 3 = 1.27:1 (ideal)

Trade-off: Requires careful design for stiffness.

**Recommended approach:**
- Start with mass reduction (always beneficial)
- Select motor with appropriate inertia for expected load
- Choose ball screw pitch for balance between resolution and inertia
- Use counterbalancing to reduce gravitational torque demand

## Practical Implementation

### Mass Budget Worksheet

Create a mass budget for your Z-axis:

| Component | Material | Volume (cm³) | Density (g/cm³) | Mass (kg) |
|-----------|----------|--------------|-----------------|-----------|
| Spindle | Steel/Al | - | - | 3.50 |
| Spindle mount | Al 6061 | 250 | 2.70 | 0.68 |
| Linear rail blocks (4×) | Steel | - | - | 0.80 |
| Ball nut housing | Al 6061 | 120 | 2.70 | 0.32 |
| Carriage plate | Al 6061 | 180 | 2.70 | 0.49 |
| Wiring bundle | Copper/PVC | - | - | 0.40 |
| **Total moving mass** | | | | **6.19 kg** |

**Target: Reduce to <5 kg**

Optimization opportunities:
- Use 7075-T6 for spindle mount (save 0.08 kg, higher strength)
- Hollow carriage plate (save 0.22 kg)
- Integrated spindle mount + ball nut housing (save 0.15 kg)
- **Optimized mass: 4.74 kg (23% reduction)**

### Counterbalance Sizing

**Required force:**
$$F = 4.74 \times 9.81 = 46.5 \text{ N}$$

**Gas spring selection:**
- Two 25N gas springs in parallel = 50N total
- Force tolerance: ±2.5N over travel
- Within ±5% target (acceptable)

**Alternative: Single 50N spring**
- Simpler installation
- Similar performance

## Key Takeaways

1. **Gravity creates continuous torque demand** that dominates vertical axis motor sizing
2. **Counterbalancing is essential** for performance, efficiency, and component life
3. **Mass reduction** through material selection and design optimization provides compounding benefits
4. **Inertia ratio** between load and motor should be 1:1 to 3:1 for optimal servo tuning
5. **Gas springs** provide simple, effective counterbalancing for most applications
6. **Weight-cable systems** offer constant force and easy adjustment
7. **Pneumatic/hydraulic systems** best for heavy loads or variable configurations
8. **Mass budget** worksheet ensures systematic optimization
9. **Safety margins** required for all counterbalance systems (2× minimum)

***

**Next**: [Section 2.3 – Column Structural Design](section-2.3-column-structural-design.md)

**Previous**: [Section 2.1 – Introduction](section-2.1-introduction.md)

---

## References

1. **Budynas, R.G. & Nisbett, J.K. (2020).** *Shigley's Mechanical Engineering Design* (11th ed.). McGraw-Hill. - Spring design and energy storage
2. **Associated Spring Raymond Handbook** - Gas spring specifications and selection
3. **Stabilus Gas Spring Engineering Manual** - Gas spring sizing and mounting
4. **Bansbach Easylift Gas Springs Technical Guide** - Gas spring characteristics and applications
5. **ISO 4126-1:2013** - Safety devices for protection against excessive pressure - Safety valves
6. **Machinery's Handbook (31st Edition, 2020).** Industrial Press. - Spring calculations
