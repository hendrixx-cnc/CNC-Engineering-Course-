## 4. Power Supply Design & Sizing: Electrical Fundamentals for Plasma Arc Generation

### 4.1 Power Supply Architecture and DC Output Requirements

Plasma cutting power supplies convert 230V single-phase or 480V three-phase AC mains to regulated DC output (typically 140–180 VDC open-circuit voltage, dropping to 80–120 VDC under load). The DC output maintains arc stability—AC arcs extinguish twice per cycle at zero-crossing, unsuitable for precision cutting. Modern inverter-based supplies operate at 20–100 kHz switching frequencies, achieving:

- **Compact size:** 1/5 the weight of traditional transformer-rectifier designs
- **High efficiency:** 85–92% (vs. 60–70% for linear supplies)
- **Precise current regulation:** ±2% setpoint accuracy via feedback control
- **Fast transient response:** Arc re-ignition after pierce in <10 ms

**Simplified Power Supply Block Diagram:**

```
AC Mains → Rectifier → DC Bus (320–680 VDC) → Inverter (IGBT bridge)
→ HF Transformer → Rectifier/Filter → DC Output (80–180 VDC)
                                          ↓
                                   Current Feedback
```

The inverter section modulates pulse width (PWM) to regulate output current, compensating for arc impedance changes as torch height varies or material thickness changes.

### 4.2 Amperage Rating and Material Thickness Capacity

The fundamental parameter defining a plasma power supply is its **maximum output current** (amperage), which determines the maximum material thickness that can be reliably cut. The relationship between current and cut capacity follows empirical scaling laws derived from energy balance:

**Rule of Thumb (Mild Steel):**

$$t_{\text{max}} = \frac{I_{\text{rated}}}{4} \quad \text{(mm)}$$

where $I_{\text{rated}}$ is the power supply current rating in amperes.

**Example 4.1: Maximum Cut Thickness for Common Power Supplies**

| Amperage Rating | Max Thickness (Steel) | Typical Application |
|----------------|----------------------|---------------------|
| 30 A | 8 mm (5/16") | Sheet metal, HVAC duct |
| 45 A | 11 mm (7/16") | Light structural, auto body |
| 60 A | 15 mm (5/8") | General fabrication, brackets |
| 85 A | 21 mm (7/8") | Heavy structural, trailer frames |
| 125 A | 31 mm (1-1/4") | Thick plate, mining equipment |

**Material Derating Factors:**

The above values apply to mild steel (1018, A36). Other materials require derating due to higher thermal conductivity or melting point:

- **Stainless steel (304/316):** 0.75× steel capacity (higher thermal conductivity dissipates heat)
- **Aluminum:** 0.50× steel capacity (high thermal conductivity, low melting point creates wide kerf)
- **Cast iron:** 0.60× steel capacity (graphite inclusions reduce arc efficiency)

**Example 4.2: Aluminum Cut Capacity Calculation**

**Given:** 85 A power supply
**Find:** Maximum aluminum thickness

**Solution:**

$$t_{\text{steel}} = \frac{85}{4} = 21.25 \text{ mm}$$

$$t_{\text{aluminum}} = 0.50 \times 21.25 = 10.6 \text{ mm}$$

**Answer:** 10–11 mm maximum aluminum thickness with 85 A supply.

### 4.3 Duty Cycle: Thermal Limits and Continuous Operation

Power supplies dissipate heat in inverter switching devices (IGBTs), transformer core losses, and output rectifier diodes. The **duty cycle** specifies the percentage of a 10-minute period the supply can operate at rated current without exceeding internal temperature limits (typically 85°C junction temperature for IGBTs).

**Duty Cycle Definition:**

$$\text{Duty Cycle} = \frac{t_{\text{on}}}{t_{\text{on}} + t_{\text{off}}} \times 100\%$$

where $t_{\text{on}}$ is arc-on time and $t_{\text{off}}$ is cooling time within a 10-minute window.

**Standard Duty Cycle Ratings:**

| Current (% of Max) | Typical Duty Cycle | Interpretation |
|-------------------|-------------------|----------------|
| 100% (85 A on 85 A unit) | 35–50% | 3.5–5 min cutting, 6.5–5 min cooling per 10 min |
| 80% (68 A on 85 A unit) | 60–70% | 6–7 min cutting, 4–3 min cooling |
| 60% (51 A on 85 A unit) | 100% | Continuous operation indefinitely |

**Thermal Power Dissipation:**

Power supply losses scale approximately with output current squared:

$$P_{\text{loss}} = P_{\text{fixed}} + k \cdot I^2$$

where:
- $P_{\text{fixed}}$ = no-load losses (transformer magnetization, control circuits): 20–50 W
- $k$ = resistance coefficient (IGBT on-state resistance, diode forward drop): 0.01–0.03 Ω
- $I$ = output current (A)

**Example 4.3: Duty Cycle Calculation from Thermal Limits**

**Given:**
- 85 A power supply rated for 40% duty cycle at maximum current
- Cutting operation requires 3 minutes of continuous arc-on time per part

**Find:** Can the supply handle back-to-back parts without cooldown?

**Solution:**

At 40% duty cycle, arc-on time per 10 minutes:

$$t_{\text{on,max}} = 0.40 \times 10 = 4 \text{ minutes}$$

Required cooling time between parts:

$$t_{\text{off}} = \frac{t_{\text{on}} \times (1 - DC)}{DC} = \frac{3 \times (1 - 0.40)}{0.40} = 4.5 \text{ minutes}$$

**Answer:** No—must wait 4.5 minutes between parts, or reduce current to 60% of rated (51 A) for 100% duty cycle.

### 4.4 Open-Circuit Voltage (OCV) and Arc Starting Energy

The **open-circuit voltage (OCV)** is the voltage present at the torch terminals before arc ignition. High OCV (150–180 VDC) ensures reliable arc starting, especially with contaminated workpieces (rust, paint, mill scale). Once the arc establishes, voltage drops to the **operating voltage** (80–120 VDC), determined by arc length and current.

**Arc Voltage vs. Current Characteristic:**

Plasma arcs exhibit a **negative resistance characteristic**—as current increases, voltage decreases slightly due to increased ionization reducing arc impedance:

$$V_{\text{arc}} = V_0 - k \cdot I$$

where:
- $V_0$ = intercept voltage (~120–140 V)
- $k$ = slope coefficient (0.3–0.8 V/A)
- $I$ = arc current (A)

**Example:** For a 60 A arc with $V_0 = 130$ V and $k = 0.5$ V/A:

$$V_{\text{arc}} = 130 - 0.5 \times 60 = 100 \text{ V}$$

**Arc Starting Methods:**

1. **High-Frequency (HF) Starting:**
   Applies 5–10 kV RF burst (2–5 MHz) between electrode and nozzle, ionizing gas to initiate arc. Advantages: non-contact (no nozzle wear), reliable. Disadvantages: EMI noise interferes with CNC electronics if not shielded.

2. **Contact Starting (Pilot Arc):**
   Electrode contacts nozzle momentarily, creating pilot arc, then retracts to transfer arc to workpiece. Advantages: No HF EMI. Disadvantages: Nozzle wear, slower starting (~100 ms vs. 10 ms for HF).

**HF Suppression Requirements:**

HF starting generates broadband EMI from 100 kHz to 10 MHz, coupling into:
- Encoder cables → position errors
- Limit switch wiring → false triggers
- USB/Ethernet → communication dropouts

**Mitigation:**
- Shielded torch cable with drain wire grounded at power supply chassis
- Ferrite cores (Fair-Rite 43 or 61 material) on all signal cables within 3 m of torch
- Separate star-point grounding: plasma ground ≠ CNC ground (connect at single earth point only)

### 4.5 Input Power Requirements and Electrical Service Sizing

Input power requirements determine breaker sizing, wire gauge, and whether single-phase or three-phase service is needed.

**Input Power Calculation:**

$$P_{\text{input}} = \frac{V_{\text{arc}} \times I_{\text{arc}}}{\eta}$$

where $\eta$ is power supply efficiency (0.85–0.92 for inverter types).

**Example 4.4: Breaker and Wire Sizing for 85 A Plasma Supply**

**Given:**
- Arc voltage: 105 V
- Arc current: 85 A
- Efficiency: 88%
- Input: 230V single-phase

**Calculate Input Current:**

$$P_{\text{input}} = \frac{105 \times 85}{0.88} = 10,142 \text{ W}$$

$$I_{\text{input}} = \frac{10,142}{230} = 44.1 \text{ A}$$

**Breaker Sizing (NEC 80% Rule):**

$$I_{\text{breaker}} = \frac{44.1}{0.80} = 55.1 \text{ A} \rightarrow \text{use 60 A breaker}$$

**Wire Sizing (75°C THHN, NEC Table 310.16):**

For 44.1 A continuous load: **6 AWG copper** (rated 65 A at 75°C)

**Voltage Drop Check (3% max for branch circuits):**

For 15 m (50 ft) cable run:

$$V_{\text{drop}} = 2 \times I \times R_{\text{wire}} \times L = 2 \times 44.1 \times 0.00131 \times 15 = 1.73 \text{ V}$$

$$\% \text{drop} = \frac{1.73}{230} \times 100\% = 0.75\% \quad \text{(acceptable)}$$

**Three-Phase Input Advantages:**

For high-amperage supplies (>85 A), three-phase input (208V or 480V) reduces input current per phase by √3, enabling smaller wire gauge and balanced loading:

$$I_{\text{input,3ph}} = \frac{P_{\text{input}}}{\sqrt{3} \times V_{\text{line}}}$$

### 4.6 Power Supply Selection Criteria

Selecting the optimal power supply involves balancing current capacity, duty cycle, and budget:

**Decision Matrix:**

| Material Thickness Range | Recommended Amperage | Duty Cycle Requirement | Price Range (USD) |
|-------------------------|---------------------|------------------------|-------------------|
| ≤6 mm (sheet metal) | 30–45 A | 50% (intermittent) | $500–$1,500 |
| 6–12 mm (light fabrication) | 45–60 A | 60% (frequent cuts) | $1,500–$3,000 |
| 12–20 mm (structural) | 60–85 A | 80% (production) | $3,000–$6,000 |
| 20–30 mm (heavy plate) | 85–125 A | 100% (continuous) | $6,000–$12,000 |

**Additional Features to Consider:**

- **Post-flow timer:** Continues gas flow 5–30 seconds after arc-off to cool consumables, extending life 2–3×
- **Arc force control:** Adjusts arc stiffness (energy density) for thick vs. thin materials
- **CNC interface:** Relay outputs for arc-on/arc-OK status; analog input for remote current adjustment
- **Automatic gas pressure compensation:** Adjusts output current to maintain arc stability as compressed air pressure varies

### 4.7 Integration with CNC Control Systems

The power supply interfaces with the CNC controller via digital and analog I/O:

**Required Control Signals:**

1. **Torch On (Input to PSU):** Digital input (24V or dry contact) from CNC initiates arc. Typically connected to M3/M4 spindle-on output in LinuxCNC or equivalent.

2. **Arc OK / Arc Transfer (Output from PSU):** Digital output (relay or open-collector) signals successful arc transfer to workpiece. CNC reads this to confirm cut start before motion; if arc-OK fails, abort and alarm.

3. **Divided Voltage (Output from PSU):** Analog voltage (0–10V or 0–5V) proportional to arc voltage, scaled 50:1 or 100:1. Used by THC (Torch Height Control) to maintain constant arc length via Z-axis feedback.

**Wiring Example (LinuxCNC):**

```
CNC Motion.spindle-on → Power Supply "Torch On" input
Power Supply "Arc OK" → CNC Motion.digital-in-00 (enable motion only when true)
Power Supply "Divided Voltage" → CNC Mesa 7i76 Analog Input 0 (THC feedback)
```

**Safety Interlocks:**

- Arc-OK timeout: If arc does not transfer within 3 seconds of torch-on command, fault and retract torch (prevents consumable burnout)
- Emergency stop integration: E-stop must disconnect torch-on signal and disable HF starting circuitry

### 4.8 Summary and Best Practices

**Key Takeaways:**

1. **Amperage determines cut capacity:** 4:1 rule for steel (divide amperage by 4 to get max mm). Derate for aluminum (0.5×) and stainless (0.75×).

2. **Duty cycle limits production rate:** Operating at 60% of rated current achieves 100% duty cycle for continuous use; full current limited to 35–50% duty cycle.

3. **Input power sizing critical:** Use NEC 80% rule for breaker sizing; check voltage drop over cable runs; three-phase reduces wire gauge for high-current units.

4. **EMI suppression essential:** HF starting generates broadband noise—shield torch cable, use ferrite cores on CNC signals, separate plasma and control grounds.

5. **CNC integration requires three signals:** Torch-on (CNC→PSU), Arc-OK (PSU→CNC), Divided voltage (PSU→THC for height control).

Proper power supply selection and integration ensures reliable arc starting, optimal cut quality, and long consumable life while preventing electrical issues from disrupting CNC operation.

***

---

## References

1. **AWS C5.1:2018** - Recommended Practices for Plasma Arc Cutting
2. **Hypertherm Powermax Series Technical Manual** - Plasma system specifications
3. **ISO 9013:2017** - Thermal cutting - Classification of thermal cuts - Geometrical product specification
4. **NFPA 51B:2019** - Standard for Fire Prevention During Welding, Cutting, and Other Hot Work
5. **Paton, B.E. (1962).** *Plasma Arc Welding*. Consultants Bureau
6. **Miller Electric Plasma Cutting Guide** - Applications and troubleshooting
7. **Lincoln Electric Plasma Cutting Handbook** - Process fundamentals
