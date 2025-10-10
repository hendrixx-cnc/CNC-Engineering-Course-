# Module 2 – Vertical Axis and Column Assembly

## 1. Z-Axis Design Philosophy

- **Mass & Inertia Management:** Reduce moving mass, use counterbalance.
- **Column Stiffness:** High second moment of area, minimize deflection.
- **Symmetry & Thermal Behaviour:** Use symmetrical cross sections.
- **Vibration & Resonance:** First resonance $>$ 5–10× servo loop bandwidth.
- **Serviceability:** Access for adjustment and maintenance.

---

## 2. Vertical Axis Architecture

| Component      | Typical Specification         | Notes                                      |
|----------------|------------------------------|---------------------------------------------|
| Travel         | 150–250 mm                   | Determines working height                   |
| Drive type     | Ball-screw (Ø16–25 mm) or belt | Ball-screws for high stiffness, belts for cost |
| Guide          | Two linear rails (15–20 mm)  | Wide spacing for moment arm                 |
| Motor orient.  | Vertical/horizontal          | Vertical above chips, horizontal compact    |
| Counterbalance | Gas spring / counterweight   | Matches static load                         |

---

## 3. Core Equations for Column Behaviour

### 3.1 Cantilever Beam Deflection

$$
\delta_B = \frac{F L^3}{3 E I}
$$

Required moment of inertia for $\delta_{max}$:

$$
I_{req} = \frac{3 E \delta_{max}}{F L^3}
$$

---

### 3.2 Natural (Resonant) Frequency

Spring–mass system with $k = 3 E I / L^3$, mass $m$:

$$
f_n = \frac{1}{2\pi} \sqrt{\frac{3 E I}{m L^3}}
$$

---

### 3.3 Ball-Screw Critical Speed

$$
n_{cr} = \frac{4.76 \times 10^6 \cdot k \cdot d_s}{L^2}
$$

---

### 3.4 Servo Resonance Criterion

$$
f_n \geq 5 \times f_{servo}
$$

---

## 4. Universal Column Requirements

| Feature         | Universal requirement                | Example implementation                           |
|-----------------|-------------------------------------|--------------------------------------------------|
| Cross section   | High second moment of area          | 150 × 150 × 8 mm steel tube with internal ribs   |
| Guide spacing   | Wide relative to column depth        | Rails 120 mm apart                               |
| Screw alignment | Parallel to rail datum ≤ 0.03 mm    | Machined or shimmed mounting pads                |
| Counterbalance  | Force within ±10% of head weight    | Two 250 N gas springs                            |
| Natural freq.   | ≥ 5× servo bandwidth (>150 Hz)      | 1st mode ≈ 180 Hz (FEA verified)                 |
| Access          | Replace guides, adjust preload      | Removable rear cover, jack-screw mount           |

---

## 5. Example Application – Designing a 200 mm Travel Z-Axis

- Column size: Use the cantilever deflection formula.
- Natural frequency: Calculate for required stability.
- Ball-screw: Select for speed and critical RPM.
- Counterbalance: Use gas springs to match head weight.
- Servo and gearbox: Size for inertia and resonance.

---

## 6. Verification & Maintenance Checklist

| Parameter                     | Instrument              | Acceptance criterion      |
|-------------------------------|-------------------------|--------------------------|
| Column deflection (400 N)     | Dial indicator          | ≤ 0.02 mm                |
| Rail parallelism              | Height gauge            | ≤ 0.03 mm variation      |
| Screw alignment               | Dial indicator          | Misalignment ≤ 0.02 mm   |
| Natural frequency             | Accelerometer           | ≥ 150 Hz                 |
| Counterbalance force          | Force gauge             | ±10% of head weight      |
| Backlash                      | Laser interferometer    | ≤ 0.02 mm                |

---

## 7. Design Rule

Ensure static deflection under max cutting force is less than half the positioning tolerance. Natural frequency should meet resonance criterion.

---

## 8. Cross References & Further Reading

- Module 1 – Mechanical Frame & Structure
- Module 3 – Servo Motor Selection & Control
- Module 6 – Spindle Systems
- Module 13 – EMI and EMC
- Appendix & Glossary

---

