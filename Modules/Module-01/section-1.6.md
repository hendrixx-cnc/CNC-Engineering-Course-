## 6. Dynamic Behavior and Control-Structure Coupling

### 6.1 The Mechatronic System: Where Mechanical Meets Control

Modern CNC machines are **mechatronic systems**—tightly coupled integrations of mechanical structures, actuators, sensors, and control algorithms. The mechanical compliance and damping directly influence control system performance, while servo forces excite structural dynamics. Understanding this bidirectional coupling is essential for achieving both mechanical and control system design objectives simultaneously.

### 6.2 Equivalent Stiffness of the Complete Drive Train

The positioning accuracy and servo bandwidth are limited by the **total compliance** in the kinematic chain from motor to workpiece. This compliance is a series combination of individual compliances:

$$\frac{1}{k_{eq}} = \frac{1}{k_{rack}} + \frac{1}{k_{gearbox}} + \frac{1}{k_{coupling}} + \frac{1}{k_{mount}} + \frac{1}{k_{frame}}$$

where each $k$ represents the stiffness (N/µm) of:

**$k_{rack}$: Rack-Pinion Tooth Contact Stiffness**
- Hertzian contact between gear teeth: 100–200 N/µm
- Depends on tooth geometry, material properties, contact stress
- Reduced by wear, inadequate lubrication, or misalignment

**$k_{gearbox}$: Planetary Gearbox Stiffness**
- Quality gearboxes with properly preloaded bearings: 300–600 N/µm
- Lost-motion (backlash) reduces effective stiffness under reversals
- Temperature-dependent: stiffness drops 10–20% at elevated temperatures

**$k_{coupling}$: Motor-to-Gearbox Coupling**
- Rigid couplings (steel): 500–1,000 N/µm
- Flexible couplings (elastomeric): 50–200 N/µm (trades stiffness for vibration isolation)

**$k_{mount}$: Rack and Rail Mounting to Frame**
- Often the weakest link in amateur builds
- Proper mounting (bolts every 150mm, torqued to spec): 50–150 N/µm
- Poor mounting (under-torqued, insufficient bolts): 10–30 N/µm

**$k_{frame}$: Frame Structural Compliance**
- Well-designed frames: 200–500 N/µm
- Undersized frames: 50–100 N/µm (dominant compliance)

**Example Calculation:**

Given:
- $k_{rack} = 150$ N/µm
- $k_{gearbox} = 400$ N/µm
- $k_{coupling} = 600$ N/µm
- $k_{mount} = 100$ N/µm
- $k_{frame} = 300$ N/µm

$$\frac{1}{k_{eq}} = \frac{1}{150} + \frac{1}{400} + \frac{1}{600} + \frac{1}{100} + \frac{1}{300}$$

$$= 0.00667 + 0.0025 + 0.00167 + 0.01 + 0.00333 = 0.02417 \text{ µm/N}$$

$$k_{eq} = \frac{1}{0.02417} = 41.4 \text{ N/µm}$$

**Key Observation**: Despite individual components having stiffnesses of 100–600 N/µm, the system stiffness is only 41.4 N/µm—dominated by the mounting compliance (10 N/µm bolt) which contributes 41% of total compliance. This illustrates why **proper mounting is as critical as structural design**.

### 6.3 Damping Ratio and Energy Dissipation

While stiffness determines static deflection and natural frequency, **damping** determines how quickly vibrations decay after excitation. The damping ratio $\zeta$ is:

$$\zeta = \frac{c}{c_{crit}} = \frac{c}{2\sqrt{km}}$$

where:
- $c$ = actual damping coefficient (N·s/m)
- $c_{crit} = 2\sqrt{km}$ = critical damping coefficient
- $k$ = system stiffness (N/m)
- $m$ = effective mass (kg)

**Damping Mechanisms in Machine Structures:**

1. **Material Damping** (Internal friction in crystalline structure)
   - Steel: $\zeta \approx 0.002$–0.005 (very low)
   - Cast iron: $\zeta \approx 0.01$–0.05 (5–10× higher than steel)
   - Aluminum: $\zeta \approx 0.001$–0.003 (very low)
   - **Conclusion**: Material damping alone is insufficient

2. **Structural Damping** (Friction at joints, welds, interfaces)
   - Bolted joints: $\zeta \approx 0.01$–0.03 (moderate)
   - Welded joints: $\zeta \approx 0.005$–0.015 (low to moderate)
   - **Strategy**: Multiple bolted/clamped joints increase total damping

3. **Added Damping** (Engineered dissipation mechanisms)
   - Viscoelastic dampers (3M ISD112): $\zeta \approx 0.05$–0.15 (high)
   - Polymer concrete fill: $\zeta \approx 0.03$–0.08 (moderate to high)
   - Tuned mass dampers: Targeted to specific modes

**Quality Factor and Resonance Amplification:**

At resonance, a lightly-damped system amplifies vibration by:

$$Q = \frac{1}{2\zeta}$$

For welded steel frame with $\zeta = 0.01$:

$$Q = \frac{1}{2 \times 0.01} = 50$$

A 0.01mm excitation at resonant frequency produces **0.50mm vibration amplitude**—destroying precision!

With added damping ($\zeta = 0.10$):

$$Q = \frac{1}{2 \times 0.10} = 5$$

Same excitation produces only 0.05mm—a 10× improvement.

**Design Implication**: Adding damping is as important as adding stiffness. Strategies include:
- Polymer concrete fills in hollow frame sections
- Constrained-layer viscoelastic treatments
- Friction dampers at strategic locations

### 6.4 Servo Bandwidth and Structural Resonance Separation

The servo control bandwidth $f_{servo}$ must remain well below the first structural natural frequency $f_n$ to prevent control-structure interaction. The standard rule:

$$f_{servo} \leq \frac{f_n}{5} \quad \text{to} \quad \frac{f_n}{10}$$

**Physical Reasoning:**

Servo controllers generate command signals (velocity, acceleration) containing **harmonic content** extending to several times the fundamental bandwidth. For a servo with 20 Hz bandwidth, significant energy exists at:
- 20 Hz (fundamental)
- 40 Hz (2nd harmonic)
- 60 Hz (3rd harmonic)
- 80 Hz (4th harmonic)

If $f_n = 100$ Hz, the 4th harmonic (80 Hz) is dangerously close to resonance. With only 5:1 separation:

$$\text{Separation} = \frac{100}{20} = 5:1$$

the 5th harmonic (100 Hz) exactly matches $f_n$, causing instability.

**Safe Design:**

For $f_n = 150$ Hz, limit servo bandwidth to:

$$f_{servo} \leq \frac{150}{5} = 30 \text{ Hz}$$

This provides:
- Fundamental at 30 Hz (5:1 separation)
- 2nd harmonic at 60 Hz (2.5:1)
- 3rd harmonic at 90 Hz (1.67:1)
- 4th harmonic at 120 Hz (1.25:1)
- 5th harmonic at 150 Hz = resonance, but attenuated by filter

**Trade-off**: Higher structural frequency enables higher servo bandwidth, which improves:
- Tracking accuracy during contouring
- Settling time after rapid moves
- Disturbance rejection (cutting forces)

This creates a design incentive to maximize $f_n$ through stiffness/mass optimization.

### 6.5 Control System Implications of Structural Compliance

**Position Loop Stiffness:**

The closed-loop position stiffness (resistance to external disturbance forces) is:

$$k_{closed} = k_{eq} \times (1 + K_p \cdot K_v)$$

where:
- $K_p$ = position loop gain (1/s)
- $K_v$ = velocity loop gain (1/s)
- $k_{eq}$ = mechanical stiffness (N/µm)

For $k_{eq} = 40$ N/µm, $K_p = 50$ /s, $K_v = 200$ /s:

$$k_{closed} = 40 \times (1 + 50 \times 200) = 40 \times 10,001 \approx 400,040 \text{ N/µm}$$

This 10,000× amplification is the power of feedback control—but it requires:
1. Structural resonance well above servo bandwidth
2. Adequate sensor resolution
3. Properly tuned servo gains

**Following Error Under Cutting Load:**

A cutting force $F$ produces following error:

$$e_{following} = \frac{F}{k_{closed}}$$

For 200 N cutting force, $k_{closed} = 400,000$ N/µm:

$$e_{following} = \frac{200}{400,000} = 0.0005 \text{ mm} = 0.5 \text{ µm}$$

Acceptable for most applications. But if poor mechanical design yields $k_{eq} = 5$ N/µm and gains must be reduced due to resonance ($K_p = 10$):

$$k_{closed} = 5 \times (1 + 10 \times 200) = 10,005 \text{ N/µm}$$

$$e_{following} = \frac{200}{10,005} = 0.02 \text{ mm} = 20 \text{ µm}$$

This 40× degradation demonstrates why **mechanical and control design are inseparable**.

***

---

## References

1. **Altintas, Y. (2012).** *Manufacturing Automation* (2nd ed.). Cambridge University Press. - Machine tool dynamics and chatter
2. **Schmitz, T.L. & Smith, K.S. (2019).** *Mechanical Vibrations: Modeling and Measurement*. Springer
3. **Ewins, D.J. (2000).** *Modal Testing: Theory, Practice and Application* (2nd ed.). Research Studies Press
4. **ISO 230-4:2005** - Test code for machine tools - Circular tests for numerically controlled machine tools
5. **Den Hartog, J.P. (1985).** *Mechanical Vibrations*. Dover Publications
6. **Rivin, E.I. (1999).** *Stiffness and Damping in Mechanical Design*. Marcel Dekker
