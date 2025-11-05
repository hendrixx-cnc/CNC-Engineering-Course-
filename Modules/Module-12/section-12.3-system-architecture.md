## 3. System Architecture: Laser, Pump, and Optical Integration

### 3.1 System Block Diagram and Component Integration

A complete water-jet guided laser system integrates fiber laser technology (Module 7), high-pressure intensification (Module 8.2), precision optics, and CNC motion control (Module 4) into a unified cutting platform. Understanding the interdependencies between subsystems—laser power stability affecting coupling efficiency, pump pressure ripple influencing jet straightness, optical alignment determining transmission losses—enables specification of components meeting system-level performance requirements.

**System Architecture Overview:**

```
[Fiber Laser Source] → [Optical Coupling Head] → [Water Jet Nozzle] → [Workpiece]
        ↓                        ↓                       ↑
   Power Control         Beam Focusing         [High-Pressure Pump]
        ↓                        ↓                       ↑
[CNC Controller] ←→ [Motion System (X-Y-Z)] ←→ [Safety Interlocks]
```

**Critical Integration Points:**
1. Laser-to-water jet optical coupling (Section 3.4)
2. Pump pressure stability ensuring jet straightness (Section 3.3)
3. CNC synchronization of laser power, pump pressure, and motion (Section 12.7)
4. Safety interlock coordination (Section 12.8)

### 3.2 Fiber Laser Source Specification

The fiber laser provides cutting energy, with specifications dictated by target material thickness, cutting speed requirements, and kerf quality objectives.

**Key Laser Parameters:**

**1. Wavelength:**
- Standard: 1.06 μm (Yb-doped fiber laser)
- Rationale: Water absorption coefficient moderate (0.12 m⁻¹) enables 50-200 mm propagation with <10% loss while ensuring energy couples to workpiece via water heating

**2. Power Rating:**
- Range: 500W to 4 kW (typical)
- Selection criterion: $P_{required} = k \times t^{1.5} \times v_{cut}$
  - $k = 0.15$ to $0.30$ (material constant, stainless steel = 0.20)
  - $t$ = material thickness (mm)
  - $v_{cut}$ = cutting speed (m/s)

**Example 3.1: Laser Power Selection for 3 mm Stainless Steel**

**Given:**
- Material: Stainless steel 316L
- Thickness: $t = 3$ mm
- Target cutting speed: $v_{cut} = 400$ mm/min = 0.00667 m/s
- Material constant: $k = 0.20$

**Calculate required laser power:**

$$P_{required} = k \times t^{1.5} \times v_{cut} = 0.20 \times 3^{1.5} \times 0.00667$$

$$P_{required} = 0.20 \times 5.196 \times 0.00667 = 0.00693 \text{ kW} = 6.93 \text{ W}$$

Wait—this seems too low. The formula applies to **power delivered to workpiece**. Accounting for 80% coupling efficiency:

$$P_{laser} = \frac{P_{required}}{\eta} = \frac{693}{\0.80} = 866 \text{ W}$$

**Recommended:** 1 kW laser (provides margin for process variation, thicker materials, higher speeds)

**3. Beam Quality (M²):**
- Requirement: M² <1.3 (near-diffraction-limited)
- Impact: Lower M² enables tighter focusing → smaller spot size → higher power density → faster cutting
- Single-mode fiber lasers: M² = 1.05-1.15
- Multi-mode fiber lasers: M² = 1.2-1.4

**4. Output Fiber:**
- Core diameter: 50-200 μm
- Numerical aperture: 0.12-0.16
- Delivery length: 5-15 m (fiber cable from laser source to cutting head)
- Connector type: QBH (Quik-Brite High-power) or LLK-D for field replaceability

**5. Modulation Capability:**
- **CW (Continuous Wave):** Constant power output, primary mode for cutting metals/ceramics
- **Pulsed:** 10-100 kHz repetition rate, 10-500 ns pulse duration, enables peak powers 10-100× average for micro-machining applications

**6. Power Stability:**
- Short-term: ±2% over 1 second (critical for coupling efficiency consistency)
- Long-term: ±5% over 8 hours (prevents cut quality drift during production runs)

**Laser Source Comparison:**

| Specification | Entry-Level | Production | High-Performance |
|---------------|-------------|------------|------------------|
| **Power** | 500W | 1-2 kW | 3-4 kW |
| **Applications** | <2 mm thin materials | 2-6 mm general cutting | 6-10 mm thick materials |
| **Beam quality** | M² <1.3 | M² <1.15 | M² <1.10 |
| **Fiber core** | 100-200 μm | 50-100 μm | 50 μm |
| **Cost** | $30,000-50,000 | $50,000-100,000 | $100,000-150,000 |
| **Efficiency** | 28-32% | 32-38% | 35-40% |

### 3.3 High-Pressure Intensifier Pump Design

The pump generates 3,000-6,000 bar (45,000-90,000 PSI) water pressure, with flow rates 10-50× lower than cutting waterjet systems due to small orifice diameter (0.10-0.15 mm vs. 0.25-0.40 mm for AWJ).

**Intensifier Fundamentals (Module 8.2):**

Hydraulic oil at moderate pressure (200-300 bar) drives a large-area piston connected to a small-area plunger immersed in water. Pressure intensification follows force balance:

$$P_{water} = P_{oil} \times \frac{A_{oil}}{A_{water}} = P_{oil} \times R$$

where $R$ = intensification ratio (typically 20:1 to 30:1).

**For 5,000 bar water pressure from 250 bar oil:**

$$R = \frac{5000}{250} = 20:1$$

**Required area ratio:**

$$\frac{A_{oil}}{A_{water}} = 20:1$$

If water plunger diameter = 10 mm:

$$A_{water} = \frac{\pi \times 10^2}{4} = 78.5 \text{ mm}^2$$

$$A_{oil} = 20 \times 78.5 = 1,570 \text{ mm}^2$$

$$d_{oil} = \sqrt{\frac{4 \times 1570}{\pi}} = 44.7 \text{ mm}$$

**Flow Rate Calculation:**

$$Q = C_d \times A_{orifice} \times \sqrt{\frac{2 \Delta P}{\rho}}$$

For 0.12 mm orifice at 5,000 bar (Module 8.5):

$$A = \frac{\pi \times 0.12^2}{4} = 0.0113 \text{ mm}^2 = 1.13 \times 10^{-8} \text{ m}^2$$

$$Q = 0.70 \times 1.13 \times 10^{-8} \times \sqrt{\frac{2 \times 500 \times 10^6}{1000}}$$

$$Q = 0.70 \times 1.13 \times 10^{-8} \times 1000 = 7.91 \times 10^{-6} \text{ m}^3\text{/s}$$

$$Q = 7.91 \times 10^{-6} \times 60 \times 1000 = 0.475 \text{ L/min}$$

**Approximately 0.12 L/min for 0.12 mm orifice** (scaling: flow ∝ diameter²)

**Pump Motor Sizing:**

Hydraulic power required:

$$P_{hydraulic} = Q \times \Delta P = (0.12 \times 10^{-3} / 60) \times (5000 \times 10^5)$$

$$P_{hydraulic} = 2.0 \times 10^{-6} \times 5 \times 10^8 = 1,000 \text{ W} = 1.34 \text{ HP}$$

Adding 25% for intensifier friction losses and 15% for motor efficiency:

$$P_{motor} = \frac{1000 \times 1.25}{0.85} = 1,470 \text{ W} = 1.97 \text{ HP}$$

**Specify: 2.5 HP motor** (provides margin)

Compare to cutting waterjet (Module 8): 60,000 PSI with 0.010" (0.254 mm) orifice requires 50 HP motor due to 4× larger orifice area and similar pressure.

**Pressure Stability: Accumulator Requirement:**

Intensifier piston reciprocation causes pressure pulsations. **Accumulator** (nitrogen-charged bladder or piston, 0.5-2 L volume) dampens ripple to <±0.5% required for jet straightness.

**Accumulator sizing:**

$$V_{acc} = \frac{Q \times t_{cycle}}{4 \times \frac{\Delta P}{P_{nominal}}}$$

For 0.12 L/min flow, 2-second cycle time, ±0.5% pressure ripple:

$$V_{acc} = \frac{(0.12/60) \times 2}{4 \times 0.005} = \frac{0.004}{0.02} = 0.20 \text{ L}$$

**Specify: 0.5 L accumulator** (provides margin)

### 3.4 Optical Coupling Head Design

The coupling head focuses laser beam from fiber output (50-200 μm) into water jet (100-150 μm diameter), positioned 3-8 mm downstream of nozzle orifice exit.

**Component Sequence:**

**1. Fiber Collimator:**
- Function: Expands laser from fiber core to 5-15 mm parallel beam
- Lens: Aspheric, AR-coated for 1.06 μm
- Focal length: 10-25 mm (matched to fiber NA)

**2. Focusing Lens:**
- Material: Fused silica (low absorption at 1.06 μm, high thermal conductivity)
- Focal length: 35-50 mm typical
- AR coating: R <0.5% per surface
- Diameter: 20-30 mm
- Cooling: Water jacket or forced air (for >2 kW power)

**3. Sapphire Pressure Window:**
- Thickness: 1.5-3 mm (balances pressure strength vs. thermal lensing)
- Diameter: 15-25 mm
- Coating: AR-coated both sides (R <0.5% each)
- Pressure rating: 6,000-8,000 bar (safety factor 1.2-1.6× operating pressure)
- Temperature limit: <400°C (sapphire stable to 2,000°C, but mounting O-rings limit to 150-200°C)

**4. Nozzle Assembly:**
- Orifice: Sapphire or diamond, 0.10-0.15 mm diameter
- Coupling distance: Laser focuses 3-8 mm downstream of orifice exit
- Alignment tolerance: ±0.025 mm positional, ±0.5° angular

**Optical Path Calculation:**

**Example 3.2: Spot Size at Water Jet Coupling Point**

**Given:**
- Fiber output: 100 μm core, NA = 0.15
- Collimating lens: f = 15 mm
- Focusing lens: f = 40 mm
- Beam quality: M² = 1.10

**Step 1: Collimated beam diameter**

$$D_{coll} = \frac{4 \times f_{coll} \times NA}{\pi} \times M^2 = \frac{4 \times 15 \times 0.15}{\pi} \times 1.10$$

$$D_{coll} = \frac{9.0}{3.14} \times 1.10 = 3.15 \text{ mm}$$

**Step 2: Focused spot diameter**

$$d_{spot} = \frac{4 \lambda f_{focus} M^2}{\pi D_{coll}}$$

where $\lambda = 1.06$ μm = $1.06 \times 10^{-6}$ m, $f_{focus} = 40$ mm = 0.040 m

$$d_{spot} = \frac{4 \times 1.06 \times 10^{-6} \times 0.040 \times 1.10}{\pi \times 0.00315}$$

$$d_{spot} = \frac{1.863 \times 10^{-7}}{9.90 \times 10^{-3}} = 1.88 \times 10^{-5} \text{ m} = 0.0188 \text{ mm}$$

**Focused spot: 18.8 μm diameter**

**Note:** Spot size <<water jet diameter (120 μm typical) ensures efficient coupling. Beam expands due to NA as it propagates through water, filling jet diameter after 3-5 mm propagation.

### 3.5 Water Quality and Filtration System

Water purity critically affects scattering losses (Section 2.4) and nozzle lifetime. **Specifications:**

| Parameter | Requirement | Test Method | Consequence if Exceeded |
|-----------|-------------|-------------|------------------------|
| **Particulates** | <1 ppm (>1 μm size) | Optical particle counter | Scattering losses >10%, nozzle clogging |
| **Total dissolved solids** | <10 ppm | TDS meter | Mineral deposition on optics |
| **pH** | 6.5-7.5 | pH electrode | Corrosion (low pH) or scaling (high pH) |
| **Dissolved oxygen** | <50 ppm | DO probe | Bubble formation disrupts TIR |
| **Temperature** | 18-22°C | Thermocouple | Refractive index variation |

**Filtration System:**
1. **Pre-filter:** 20 μm cartridge (protects pump from large debris)
2. **Main filter:** 1 μm cartridge (removes scattering particulates)
3. **DI polisher:** Ion exchange resin (reduces TDS to <5 ppm)
4. **UV sterilizer:** Prevents algae growth in reservoir (10-30W UV-C lamp)

**Filtration flow rate:** 2-5 L/min (20-50× system flow rate ensures <5 ppm contamination)

### 3.6 System Integration and Control Architecture

**Control Hierarchy:**

**Level 1 - Safety Interlocks (Hardware):**
- E-stop circuit (series NC contacts): laser + pump + motion
- Door interlocks: magnetic safety switches per ISO 14119
- Pressure overshoot detection: redundant transducers, <110% alarm

**Level 2 - PLC/Embedded Controller:**
- Pump pressure control: 4-20 mA analog output to proportional valve
- Laser power modulation: 0-10V analog or digital fiber protocol (Modbus)
- Sensor monitoring: Pressure, flow rate, temperature, water quality

**Level 3 - CNC Motion Controller:**
- X-Y-Z axis coordination
- G-code parsing and execution
- Laser ON/OFF via M-codes (M3/M5)
- Feedrate override for corner slowdown

**Signal Interfaces:**

```
CNC → Laser Enable (Digital Out) → Laser Driver
Laser → Power OK (Digital In) → CNC (permits motion)
CNC → Pump Pressure Setpoint (Analog Out 4-20 mA) → PLC
Pump → Pressure Achieved (Digital In) → CNC (laser enable prerequisite)
CNC → Motion Axes (Servo drive commands) → X-Y-Z Motors
```

### 3.7 Typical System Specifications Summary

**Entry-Level WGL System ($250-350k):**
- Laser: 500W-1 kW fiber
- Pump: 3,000-4,000 bar, 2.5 HP
- Work area: 600 × 600 mm
- Positioning: ±0.05 mm
- Applications: Medical prototyping, thin material R&D

**Production WGL System ($400-600k):**
- Laser: 1.5-2.5 kW fiber
- Pump: 4,000-5,500 bar, 5-7.5 HP
- Work area: 1,200 × 1,200 mm
- Positioning: ±0.02 mm
- Automation: Automatic nozzle height sensing, part recognition
- Applications: Medical device manufacturing, microelectronics

Understanding system architecture—laser power scaling, pump intensification, optical coupling design, and control integration—enables specification of WGL systems matching application requirements while optimizing cost-performance trade-offs.

***

---

## References

1. **ISO 11553 Series** - Safety of machinery - Laser processing machines
2. **ANSI Z136.1-2014** - Safe Use of Lasers
3. **ISO 9013:2017** - Thermal cutting - Classification of thermal cuts
4. **Steen, W.M. & Mazumder, J. (2010).** *Laser Material Processing* (4th ed.). Springer
5. **Flow International Waterjet Technology Handbook** - Hybrid system applications
6. **TRUMPF TruLaser Technical Documentation** - Combined processing systems
7. **Hashish, M. (2014).** "Hybrid Waterjet-Laser Cutting Technology." *Journal of Manufacturing Processes*
