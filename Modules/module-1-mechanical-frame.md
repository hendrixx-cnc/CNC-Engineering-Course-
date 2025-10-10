# Module 1 – Mechanical Frame & Structure

## 1. Introduction to Professional CNC Machine Design

Modern CNC routers, plasma tables, and laser cutters share a common mechanical DNA. They are elastic structures driven by feedback-controlled motors and subject to dynamic loads and thermal gradients. Professional design ensures that every deflection, expansion, or vibration remains predictable, reversible, and bounded within the resolution of the control system. Four fundamental design principles:

- **Deterministic Geometry:** Each axis references a single, traceable datum.
- **Stiffness Hierarchy:** Subassemblies must be stiffer than those they carry.
- **Thermal Symmetry:** Arrange materials symmetrically so expansions cancel and twist is eliminated.
- **Serviceability and Scalability:** Precision comes from adjustability.

---

## 2. System Architecture

Most gantry-style machines have three orthogonal motion groups:

| Axis | Range (mm) | Drive | Structural role |
|------|------------|-------|----------------|
| Y (long) | ≈ 2,500 | Dual helical rack & pinion | Moves gantry across table |
| X (cross) | ≈ 1,250 | Helical rack & pinion | Moves head along gantry |
| Z (vertical) | ≈ 150 | Ball-screw (Ø16 mm, 5 mm lead) | Positions the tool |

Example: Hendrixx design uses Mod 1.25 helical racks, 15° helix angle, 40-tooth pinions, 10:1 planetary gearboxes, 750W AC servos.

---

## 3. Why Use Helical Rack & Pinion

- Maintains 2–3 teeth in contact for continuous force transfer.
- ~20–25% higher load capacity than spur racks.
- Reduces acoustic noise by 10–15 dB.
- Eliminates backlash by spring-preloaded split pinions or torque-biasing dual servos.

---

## 4. Core Equations for Structural Behaviour

### 4.1 Linear Deflection of a Simply Supported Beam

Maximum mid-span deflection:

$$
\delta = \frac{5 w L^4}{384 E I}
$$

Where:
- $w$ = load per unit length
- $L$ = span
- $E$ = modulus of elasticity
- $I$ = second moment of area

---

### 4.2 Critical Speed of a Ball-Screw

$$
n_{cr} = \frac{4.76 \times 10^6 \cdot k \cdot d_s}{L^2}
$$

- $d_s$ = screw diameter (mm)
- $L$ = free length (mm)
- $k$ = end-fixity factor ($\approx$ 2.23 for fixed–simple supports)

---

### 4.3 Thermal Expansion

$$
\Delta L = \alpha L \Delta T
$$

- $\alpha$ = coefficient of thermal expansion

---

### 4.4 Resonant Frequency

$$
f_n = \frac{1}{2\pi} \sqrt{\frac{k}{m}}
$$

- $k$ = stiffness
- $m$ = mass

---

## 5. Universal Frame Requirements

Required moment of inertia for a maximum allowable deflection $\delta_{max}$:

$$
I_{req} = \frac{384 E \delta_{max}}{5 w L^4}
$$

---

| Feature         | Universal requirement            | Hendrixx example                  |
|-----------------|---------------------------------|-----------------------------------|
| Frame material  | Welded steel tube or cast iron  | 5 × 5 × 3/16 in A36 steel         |
| Rail/rack seats | Machined CRS flatbars           | Epoxy-bedded, edge-stitched CRS   |
| Gantry beam     | High $I_{xx}$ / low mass        | 45 × 180 mm 6061-T6 extrusion     |
| Support spacing | ≤ 400 mm                        | Six cross-members at ~400 mm      |
| Natural freq.   | > 100 Hz                        | Verified via FEA modal analysis   |

---

## 6. Dynamic Behaviour and Control Coupling

### 6.1 Equivalent Stiffness of Drive Train

$$
\frac{1}{k_{eq}} = \frac{1}{k_{rack}} + \frac{1}{k_{gearbox}} + \frac{1}{k_{frame}}
$$

### 6.2 Damping Ratio

$$
\zeta = \frac{c}{2 \sqrt{k m}}
$$

### 6.3 Servo Bandwidth

$$
f_{servo} \leq \frac{f_n}{5}
$$

---

## 7. Thermal Management

- Shade and ventilate both sides equally.
- Bond frame thermally to floor through steel pads.
- Execute a 5min warm-up traverse to equalise temperatures.

---

## 8. Measurement and Verification Framework

| Parameter             | Instrument                       | Target            |
|-----------------------|----------------------------------|-------------------|
| Frame flatness        | Dial indicator or laser          | ≤ 0.05 mm/m       |
| Rail parallelism      | Bridge gauge                     | ≤ 0.03 mm         |
| Rack run-out          | Optical microscope / indicator   | ≤ 0.02 mm         |
| Thermal drift (10°C)  | Dial at tool tip                 | ≤ 0.05 mm         |
| Vibration amplitude   | Accelerometer                    | ≤ 0.1g @ 60 Hz    |
| Backlash (closed loop)| Laser interferometer             | ≤ 0.02 mm         |

---

## 9. Epoxy-Bedded Flatbar System

- Design: Bars milled off-frame, jack screws for adjustability.
- Alignment: Indicator straightness ±0.02 mm, parallelism ±0.03 mm.
- Epoxy: Steel-filled, jack screws maintain alignment during curing.
- Edge stitch welding: Alternating sides, controlled temperature.

---

## 10. Material Science & Structural Selection

### 10.1 Material Properties

Specific stiffness: $E/\rho$

### 10.2 Sizing Members

Use beam-deflection rule:

$$
\delta_{max} = T_{pos}/2
$$

### 10.3 Vibration and Damping

First-mode frequency for a beam:

$$
f_1 \approx \frac{1.875^2}{2\pi L^2} \sqrt{\frac{E I}{\rho A}}
$$

---

## 11. Welding Strategy & Thermal Management

Longitudinal shrinkage:

$$
\Delta L \approx k \frac{b L}{t} \quad \text{where } k \approx 0.001-0.0015
$$

Angular distortion:

$$
\theta \approx \frac{3 \Delta L}{2 h}
$$

---

## 12. Linear Motion & Drive Foundations

- Rails: 35 mm profile rail, four blocks per axis.
- Helical racks: Module 1.25, helix angle 15–20°.
- Pinions: 40 teeth, hardened.
- Gearboxes: 10:1 planetary.
- Servo motors: 750W (Y), 400W (Z).
- Z-axis screw: Ø16 mm, 5 mm lead.

---

## 13. Gantry Beam Design

- Use closed box section for torsional stiffness.
- Precision end-plates, dowel pins, M10 bolts.
- Counter-balance: Adjust mass distribution.

---

## 14. Carriage & Bearing Preload Tuning

- Preload classes (Z0/Z1/Z2) for translation stiffness.
- Key sizing rules: Rail pitch $W \geq H/2$, Carriage spacing $S$ = 60–90% axis stroke.

---

## 15. Conclusion

A CNC machine’s mechanical performance results from equations executed in steel, aluminium, and epoxy. By calculating, measuring, and verifying each step, builders can scale designs confidently.

---

**References and cross-links are preserved.**