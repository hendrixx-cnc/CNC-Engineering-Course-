# Module 2 – Vertical Axis and Column Assembly

## 1. Z-Axis Design Philosophy

The vertical axis (Z-axis) presents unique engineering challenges fundamentally different from horizontal motion axes. While horizontal axes operate in a relatively neutral gravitational field and benefit from distributed loads, the vertical axis must continuously resist gravity, manage large cantilever moments, and overcome the dynamic challenges of moving masses in opposition to gravitational acceleration. The design philosophy for vertical axis systems integrates structural mechanics, dynamic stability theory, mass-energy management, and thermal compensation into a coherent framework that delivers precision, responsiveness, and reliability.

### 1.1 Mass & Inertia Management: The Foundation of Dynamic Performance

#### Fundamental Challenge

Every kilogram of mass moving on the Z-axis requires continuous energy input to resist gravity and demands proportionally higher motor torque for acceleration. The moment of inertia about the drive screw axis scales with the square of the radial distance, making compact designs critical.

#### Design Principles

1. Minimum Mass Design:
   - Use topology optimization to remove non-structural material
   - Employ high-strength aluminum alloys (7075-T6, yield ~500 MPa) instead of steel where possible
   - Consider magnesium alloys (AZ91D) for ultra-lightweight applications (density 1.8 g/cm³ vs 2.7 g/cm³ for Al)
   - Use hollow-core composite structures (carbon fiber/epoxy) for ultimate mass reduction

2. Gravitational Energy Management:
   The potential energy change during vertical motion:
   $$\Delta E_p = m g \Delta z$$
   
   For a 5 kg spindle assembly moving 200 mm:
   $$\Delta E_p = 5 \times 9.81 \times 0.2 = 9.81 \text{ J}$$
   
   This energy must be supplied (upward motion) or dissipated (downward motion) by the drive system.

3. Counterbalance Strategy:
   A properly implemented counterbalance system:
   - Reduces motor RMS torque by ~50-70%
   - Eliminates gravitational bias in the servo control loop
   - Enables symmetric acceleration profiles
   - Reduces thermal load on motor and amplifier
   - Extends bearing and drive component life

#### Counterbalance Force Calculation

For a moving mass $m$ with center of gravity at distance $L_{cg}$ from the column mounting plane:

$$F_{cb} = m g \cos(\theta)$$

Where $\theta$ is the machine tilt angle (typically 0° for vertical machines).

For adjustable counterbalance using gas springs:
$$F_{gas}(x) = F_0 + k_{gas}(x - x_0)$$

Where:
- $F_0$ = initial preload force
- $k_{gas}$ = gas spring stiffness (typically 0.5-2.0 N/mm)
- $x$ = displacement from neutral position
- $x_0$ = initial compressed length

#### Design Example

Moving mass: 8 kg (spindle + mounting plate + carriage)
Required counterbalance force: $F = 8 \times 9.81 = 78.5$ N

Using two gas springs in parallel:
- Individual spring force: 39.3 N
- Select standard 400 N gas spring compressed to ~10% extension
- Mounting geometry ensures force vector alignment within ±5° over full travel

4. Moment of Inertia Minimization:
   For a rotating drive screw, the reflected inertia is critical:
   
   $$J_{total} = J_{motor} + J_{coupling} + J_{screw} + \frac{m_{carriage}}{(2\pi/p)^2}$$
   
   Where $p$ is the screw pitch (m/revolution).
   
   For a 5 mm pitch screw:
   $$J_{reflected} = \frac{m}{(2\pi/0.005)^2} = m \times 6.33 \times 10^{-7}$$
   
   An 8 kg carriage reflects as: $J = 5.06 \times 10^{-6}$ kg·m²
   
   This is typically 10-50× the motor rotor inertia, dominating system dynamics.

### 1.2 Column Stiffness: Structural Optimization for Precision

Engineering Objective:
The column structure must provide a rigid reference frame that maintains rail parallelism and minimizes deflection under cutting forces. Unlike horizontal gantry beams that can be designed as simply-supported structures, vertical columns typically function as cantilevers with concentrated loads at the free end.

Cantilever Mechanics:

For a cantilever beam with length $L$, Young's modulus $E$, and second moment of area $I$, subjected to tip load $F$:

$$\delta_{tip} = \frac{F L^3}{3 E I}$$

Critical Insight: Deflection scales with the *cube* of length and inversely with moment of area. Doubling column height increases deflection by 8×, while doubling cross-sectional depth increases stiffness by ~8× (for rectangular sections).

Design Strategy:

1. Maximize Second Moment of Area:
   For rectangular hollow section (external dimensions $b × h$, wall thickness $t$):
   
   $$I_x = \frac{b h^3}{12} - \frac{(b-2t)(h-2t)^3}{12}$$
   
   For a 150×150×8 mm square tube:
   $$I_x = \frac{150 \times 150^3}{12} - \frac{134 \times 134^3}{12} = 42.19 \times 10^{6} - 26.98 \times 10^{6}$$
   $$I_x = 15.21 \times 10^{6} \text{ mm}^4 = 1.52 \times 10^{-5} \text{ m}^4$$

2. Material Selection:
   Common materials for column structures:
   
   | Material | E (GPa) | Density (kg/m³) | $E/\rho$ | Cost multiplier |
   |----------|---------|----------------|----------|----------------|
   | Mild steel | 200 | 7850 | 25.5 | 1.0× |
   | Cast iron | 120 | 7200 | 16.7 | 0.8× |
   | Aluminum 6061 | 69 | 2700 | 25.6 | 3.5× |
   | Steel + ribs | 200 | 7850 | 25.5 | 1.4× |
   
   Key Insight: While aluminum has lower absolute stiffness, its specific stiffness (E/ρ) matches steel. For vertical axes where mass reduction is critical, ribbed aluminum columns offer excellent performance.

3. Internal Ribbing and Stiffening:
   Strategic placement of internal ribs increases $I$ without proportional mass increase:
   
   - Longitudinal ribs at extreme fibers (corners)
   - Transverse bulkheads every 150-250 mm
   - Diagonal bracing in high-stress regions
   
   FEA-optimized designs achieve 30-50% stiffness increase with only 15-20% mass penalty.

4. Deflection Specification:
   Industry practice for precision machines:
   
   $$\delta_{max} = \frac{L}{10,000} \text{ to } \frac{L}{20,000}$$
   
   For 500 mm cantilever:
   $$\delta_{max} = 0.025 \text{ to } 0.05 \text{ mm}$$

Worked Example: Column Sizing

Requirements:
- Cantilever length: $L = 400$ mm
- Maximum cutting force: $F = 500$ N (conservative)
- Material: Steel ($E = 200$ GPa)
- Allowable deflection: $\delta_{max} = 0.03$ mm

Solution:

Required moment of inertia:
$$I_{req} = \frac{F L^3}{3 E \delta_{max}} = \frac{500 \times 0.4^3}{3 \times 200 \times 10^9 \times 0.00003}$$

$$I_{req} = \frac{32}{18 \times 10^6} = 1.78 \times 10^{-6} \text{ m}^4 = 1.78 \times 10^6 \text{ mm}^4$$

For square hollow section, approximating $I \approx \frac{b^3 t}{3}$ (thin-wall):
$$b^3 t \approx 5.33 \times 10^6$$

Trying $b = 120$ mm, $t = 8$ mm:
$$120^3 \times 8 = 13.8 \times 10^6 \text{ mm}^4$$ (adequate)

Selected section: 120×120×8 mm steel RHS
- Mass per meter: 28.3 kg/m
- Actual $I_x = 3.52 \times 10^6$ mm⁴ (provides 2× safety factor)

### 1.3 Symmetry & Thermal Behaviour: Compensating Environmental Effects

Thermal Expansion Challenge:
Vertical columns experience thermal gradients from:
1. Motor heat dissipation (30-100 W continuous)
2. Ambient temperature variations (±5°C typical)
3. Process heat (cutting/welding operations)
4. Solar loading (through enclosure panels)

Thermal Expansion Coefficient:
For steel: $\alpha = 11.7 \times 10^{-6}$ /°C

A 500 mm column experiencing 10°C differential:
$$\Delta L = \alpha L \Delta T = 11.7 \times 10^{-6} \times 500 \times 10 = 0.0585 \text{ mm}$$

This 58 μm error exceeds precision requirements!

Design Solutions:

1. Symmetric Cross-Sections:
   Using square or circular hollow sections ensures uniform thermal expansion in all radial directions. Asymmetric sections (C-channel, I-beam) create differential expansion leading to bending.

2. Thermal Symmetry:
   - Mount motors on centerline or use paired motors
   - Insulate motor from column structure
   - Use thermal breaks at mounting interfaces
   - Employ forced air circulation within hollow column

3. Material Selection:
   Materials with low thermal expansion coefficients:
   
   | Material | α (10⁻⁶/°C) | Relative expansion |
   |----------|-------------|-------------------|
   | Steel | 11.7 | 1.00× |
   | Aluminum | 23.6 | 2.02× |
   | Cast iron | 10.8 | 0.92× |
   | Invar 36 | 1.3 | 0.11× |
   | Carbon fiber | 0.5 to -1.0 | 0.04× |
   
   Practical Approach: Use steel or cast iron for primary structure, with carbon fiber composite in extreme precision applications.

4. Active Compensation:
   Modern CNC controllers implement thermal compensation:
   
   $$Z_{corrected} = Z_{commanded} + K_{thermal}(T - T_{ref})$$
   
   Where $K_{thermal}$ is determined through calibration cycles.

### 1.4 Vibration & Resonance: Dynamic Stability Requirements

Fundamental Principle:
The natural frequency of the Z-axis structure must be significantly higher than the servo control bandwidth to prevent control-structure interaction and ensure stable operation.

Natural Frequency Calculation:

For cantilever column modeled as spring-mass system:
$$f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m}}$$

Where the spring constant for cantilever:
$$k = \frac{3EI}{L^3}$$

Combined expression:
$$f_n = \frac{1}{2\pi}\sqrt{\frac{3EI}{mL^3}}$$

Design Rule:
$$f_n \geq 5 \times f_{servo} \text{ (minimum)}$$
$$f_n \geq 10 \times f_{servo} \text{ (preferred)}$$

For typical servo bandwidth of 30 Hz:
$$f_n \geq 150 \text{ Hz (minimum)}$$
$$f_n \geq 300 \text{ Hz (preferred)}$$

Worked Example:

Given:
- Column: 120×120×8 mm steel RHS
- Length: $L = 400$ mm
- Moving mass: $m = 8$ kg
- $E = 200$ GPa
- $I = 3.52 \times 10^{-6}$ m⁴

Calculate natural frequency:

$$k = \frac{3 \times 200 \times 10^9 \times 3.52 \times 10^{-6}}{0.4^3} = \frac{2.112 \times 10^6}{0.064} = 33.0 \times 10^6 \text{ N/m}$$

$$f_n = \frac{1}{2\pi}\sqrt{\frac{33.0 \times 10^6}{8}} = \frac{1}{6.283}\sqrt{4.125 \times 10^6}$$

$$f_n = \frac{2031}{6.283} = 323 \text{ Hz}$$

Result: This design achieves $f_n = 323$ Hz, providing 10.8× margin over 30 Hz servo bandwidth (excellent).

Resonance Mitigation Strategies:

1. **Structural Damping:**
   - Use cast iron (damping ratio ξ ≈ 0.02-0.05) instead of steel (ξ ≈ 0.001-0.002)
   - Add constrained-layer damping treatments
   - Use polymer-composite hybrid structures

2. **Modal Analysis:**
   Perform FEA to identify all modes below 500 Hz:
   - 1st mode: Typically Z-axis bending
   - 2nd mode: Torsion about column axis
   - 3rd mode: X-Y rocking of carriage
   
   Ensure all modes satisfy $f_i > 5 f_{servo}$

3. **Active Damping:**
   Modern servo drives implement notch filters and low-pass filters to suppress resonances:
   
   Notch filter transfer function:
   $$H(s) = \frac{s^2 + 2\zeta_z \omega_n s + \omega_n^2}{s^2 + 2\zeta_p \omega_n s + \omega_n^2}$$
   
   Tuned to structural resonant frequency with high attenuation.

### 1.5 Serviceability: Design for Maintenance and Adjustment

**Critical Insight:**
The most precisely designed vertical axis will degrade over time without proper maintenance access. Bearing preload adjustment, rail replacement, and alignment verification must be possible without complete machine disassembly.

**Design Requirements:**

1. **Bearing Access:**
   - Removable covers at bearing mounting locations
   - Jack-screw provisions for preload adjustment
   - Clearance for bearing puller tools
   - Documented preload values (typically 4-8% of dynamic load rating)

2. **Rail Replacement:**
   - Rails should be removable without disturbing column structure
   - Use dowel pins for repeatable rail positioning
   - Provide access for precision height gauge measurements
   - Design for single-rail replacement (if paired rails used)

3. **Screw Alignment:**
   - Shim packs at bearing mounts
   - Slotted mounting holes (±1.0 mm adjustment)
   - Dial indicator access points
   - Alignment specification: ≤0.02 mm TIR over full travel

4. **Counterbalance Adjustment:**
   - External force adjustment (gas spring pressure or weight stack)
   - Test procedure: Measure motor current at mid-stroke with zero external load
   - Target: ≤10% variation from ideal balance current

5. **Cable Management:**
   - Use cable carriers (drag chains) sized for 2× bend radius of largest cable
   - Provide strain relief at moving carriage
   - Route away from chip zones
   - Allow for future additions (extra 30% capacity)

**Maintenance Schedule:**

| Component | Interval | Procedure |
|-----------|----------|-----------|
| Rail preload | 6 months | Verify bearing preload, adjust if needed |
| Screw lubrication | 3 months | Re-grease ball nut via zerk fitting |
| Counterbalance | 12 months | Verify force ±10%, adjust gas spring pressure |
| Rail parallelism | 12 months | Height gauge measurement, shim if needed |
| Resonance check | 12 months | Accelerometer test, update notch filters |

***

## 1.6 Integrated Design Philosophy Summary

The design of precision vertical axes requires simultaneous optimization of multiple competing objectives:

1. **Minimize moving mass** → Reduced motor torque, faster acceleration
2. **Maximize structural stiffness** → Dimensional stability under load
3. **Ensure thermal symmetry** → Minimize position errors from temperature
4. **Achieve high natural frequency** → Stable servo control without resonance
5. **Enable maintenance access** → Long-term precision retention

**Design Workflow:**

```
1. Define performance requirements (travel, speed, cutting forces)
2. Calculate required column stiffness → Select cross-section
3. Estimate moving mass → Design counterbalance system
4. Verify natural frequency > 5× servo bandwidth
5. Perform thermal FEA → Verify symmetric expansion
6. Design maintenance access features
7. Prototype and measure → Iterate
```

The successful vertical axis represents a balanced compromise where no single parameter is over-optimized at the expense of overall system performance. The following sections provide detailed implementation guidance for each subsystem.

***


---

## References

1. **ISO 13849-1:2015** - Safety of machinery - Safety-related parts of control systems
2. **EN 60204-1:2018** - Safety of machinery - Electrical equipment - General requirements
3. **ANSI/NFPA 79-2021** - Electrical Standard for Industrial Machinery
4. **Mayr Antriebstechnik Safety Brake Catalog** - Spring-applied brake sizing and selection
5. **Warner Electric Brake Catalog** - Electromagnetic and spring-set brake specifications
6. **Slocum, A.H. (1992).** *Precision Machine Design*. SME. - Gravity compensation systems
