# Appendix E: Electrical Standards and Wiring

---

## E.1 Wire Sizing and Current Ratings

### E.1.1 AWG (American Wire Gauge) Current Ratings

**Copper Wire, 60°C Insulation (NEC Table 310.16), Chassis Wiring:**

| AWG Size | Diameter (mm) | Resistance (Ω/km) | Max Current (A) @ 60°C | Typical CNC Use |
|----------|--------------|------------------|---------------------|----------------|
| **24** | 0.511 | 84.2 | 3.5 | Signal wires, limit switches, encoder |
| **22** | 0.644 | 53.0 | 5 | Control signals, relay coils, sensors |
| **20** | 0.812 | 33.3 | 7.5 | Limit switches, low-current 24V DC |
| **18** | 1.024 | 20.9 | 10 | 24V DC power distribution, steppers (short runs) |
| **16** | 1.291 | 13.2 | 13 | Motor power (NEMA 17), 24V supplies |
| **14** | 1.628 | 8.28 | 20 | Motor power (NEMA 23), 48V supplies |
| **12** | 2.053 | 5.21 | 25 | Heavy motor power (NEMA 34), VFD output |
| **10** | 2.588 | 3.28 | 40 | Main power feeds, spindle motor |
| **8** | 3.264 | 2.06 | 55 | Large spindle VFD input/output |

**Note:** For power transmission, derate by 80% for continuous duty (e.g., 14 AWG → 16A continuous max).

**90°C Insulation (THHN, THWN):** Multiply current rating by 1.3× (e.g., 14 AWG → 26A @ 90°C).

### E.1.2 Metric Wire Sizing (IEC 60228)

| Cross-Section (mm²) | Diameter (mm) | Resistance (Ω/km) | Max Current (A) @ 70°C | AWG Equivalent |
|--------------------|--------------|------------------|---------------------|----------------|
| **0.5** | 0.80 | 39.0 | 3 | ~24 AWG |
| **0.75** | 0.98 | 26.0 | 6 | ~22 AWG |
| **1.0** | 1.13 | 19.5 | 10 | ~20 AWG |
| **1.5** | 1.38 | 13.3 | 15 | ~18 AWG |
| **2.5** | 1.78 | 7.98 | 21 | ~14 AWG |
| **4.0** | 2.26 | 4.95 | 28 | ~12 AWG |
| **6.0** | 2.76 | 3.30 | 36 | ~10 AWG |
| **10.0** | 3.57 | 1.95 | 50 | ~8 AWG |

### E.1.3 Voltage Drop Calculation

**Formula:**

$$V_{drop} = \frac{2 \times I \times L \times R}{1000}$$

where:
- $V_{drop}$ = voltage drop (V)
- $I$ = current (A)
- $L$ = one-way length (m)
- $R$ = resistance (Ω/km) from tables above
- Factor of 2 accounts for return path

**Example:** 10A load, 20m cable run (one-way), 14 AWG copper

$$V_{drop} = \frac{2 \times 10 \times 20 \times 8.28}{1000} = 3.3 \text{ V}$$

**On 48V system: 3.3V / 48V = 6.9% drop (borderline acceptable)**
**On 24V system: 3.3V / 24V = 13.8% drop (excessive, use 12 AWG)**

**Maximum Recommended Voltage Drop:**
- **Power circuits (motors, VFD):** 3% max (2% preferred)
- **Control circuits (24V DC logic):** 5% max
- **Signal circuits (encoders, analog):** 1% max (minimize noise)

---

## E.2 Electrical Standards and Codes

### E.2.1 Voltage Classifications (IEC 60449, NEC)

| Voltage Range | Classification | Insulation Requirements | Typical CNC Applications |
|---------------|---------------|------------------------|-------------------------|
| **<50V AC, <120V DC** | Extra-Low Voltage (ELV) | Basic insulation | 24V DC control, 48V stepper supplies |
| **50-1000V AC, 120-1500V DC** | Low Voltage (LV) | Double insulation or grounding | 115V/230V AC mains, spindle motors |
| **>1000V AC, >1500V DC** | High Voltage (HV) | Special isolation, qualified personnel | Rare in CNC (plasma arc, EDM) |

**SELV (Safety Extra-Low Voltage):** ≤50V AC / ≤120V DC with isolation from mains (transformer). Safe to touch under normal conditions.

**Example:** 24V DC control circuit powered by isolated 230V→24V transformer = SELV (safe).

### E.2.2 IP (Ingress Protection) Ratings (IEC 60529)

**Format: IP XY**
- X = Solid particle protection (0-6)
- Y = Liquid ingress protection (0-9)

| Rating | Solid Protection | Liquid Protection | CNC Applications |
|--------|-----------------|------------------|------------------|
| **IP20** | >12.5mm (finger) | None | Indoor electronics enclosure (standard) |
| **IP54** | Dust protected | Splash-proof | Machine control cabinet (light industrial) |
| **IP65** | Dust-tight | Water jet proof | Outdoor enclosures, washdown areas |
| **IP67** | Dust-tight | Immersion 1m | Sensors in cutting zone (waterjet, coolant) |

**Recommendation:**
- **Main control cabinet:** IP54 minimum (keep dust out, survive accidental liquid splash)
- **Pendant/HMI:** IP65 (operator handling, coolant splash)
- **Limit switches in cutting zone:** IP67 (continuous coolant exposure)

### E.2.3 UL, CE, and Safety Certifications

**UL (Underwriters Laboratories - North America):**
- UL 508A: Industrial Control Panels
- UL 61010-1: Electrical Equipment for Measurement, Control, Laboratory Use

**CE Marking (European Conformity):**
- Low Voltage Directive (LVD) 2014/35/EU: 50-1000V AC equipment safety
- EMC Directive 2014/30/EU: Electromagnetic compatibility
- Machinery Directive 2006/42/EC: Machine safety (includes E-stop, interlocks)

**CSA (Canadian Standards Association):**
- CSA C22.2 No. 142: Process Control Equipment

**Recommendation for DIY/Small Production:**
- Use UL-listed components (power supplies, circuit breakers, contactors)
- Follow NEC/IEC wiring practices
- CE marking not required for single machines (own use), but recommended for sale in EU

---

## E.3 Power Distribution and Protection

### E.3.1 Circuit Breaker Selection

**Thermal-Magnetic Circuit Breakers:**

| Rating (A) | Trip Curve | Magnetic Trip (A) | Applications |
|-----------|-----------|------------------|--------------|
| **C-Curve (Standard)** | 5-10× | 50-100A @ 10A breaker | General CNC circuits, motors |
| **D-Curve (Motor)** | 10-20× | 100-200A @ 10A breaker | Inductive loads, VFD input, high inrush |

**Sizing:**
- **Continuous load:** Breaker rating ≥ 1.25× max continuous current
- **Motor circuits:** Breaker rating = 2.5× motor full-load current (FLC) typical

**Example:** 2.2 kW spindle motor, 230V single-phase
- FLC = 2200W / 230V / 0.85 PF = 11.2A
- Breaker: 11.2 × 2.5 = 28A → use 30A D-curve breaker

### E.3.2 Residual Current Device (RCD) / GFCI

**Purpose:** Detect ground fault (leakage current), trip to prevent electrocution.

**Types:**
- **Type AC:** Detects AC fault current (standard, lowest cost)
- **Type A:** Detects AC + pulsating DC (VFD compatible)
- **Type B:** Detects AC + DC (high-frequency drives, medical)

**Trip Current:**
- **30 mA:** Personnel protection (required on circuits with portable equipment, operator contact)
- **100-300 mA:** Fire protection (main panel)

**Recommendation for CNC:**
- **30 mA Type A RCD** on operator circuits (pendant, HMI, 115V outlets)
- VFDs may cause nuisance tripping with RCD (use Type A or B, or isolate VFD on separate circuit without RCD)

### E.3.3 Fuses vs. Circuit Breakers

| Device | Response Time | Reusability | Cost | Best For |
|--------|--------------|-------------|------|----------|
| **Fast-Blow Fuse** | <0.001s | Single-use | $ | Semiconductor protection (drivers, PSU) |
| **Slow-Blow (Time-Delay) Fuse** | 0.1-10s | Single-use | $ | Motor circuits (tolerates inrush) |
| **Circuit Breaker** | 0.01-1s | Reusable | $$ | Panel distribution, easy reset |

**Fuse Sizing:**
- **Electronics (PSU, drivers):** 1.5× max continuous current, fast-blow
- **Motors (VFD, steppers):** 2.0× FLC, slow-blow

---

## E.4 Grounding and Shielding

### E.4.1 Grounding Schemes

**Single-Point Ground (Star Ground):**
- All grounds connect to one central point (typically main panel ground bus)
- Prevents ground loops (multiple return paths causing noise)
- **Recommended for CNC controls**

**Multi-Point Ground:**
- Grounds connected at multiple locations (chassis, cabinet, earth)
- Lower impedance at high frequencies
- Used for RF/EMI shielding (enclosure bonding)

**Grounding Conductor Sizing (NEC):**

| Circuit Breaker Size (A) | Minimum Ground Wire (AWG) |
|-------------------------|--------------------------|
| 15-20 | 14 |
| 30 | 10 |
| 40-60 | 10 |
| 100 | 8 |
| 200 | 6 |

**Grounding Recommendations:**
- Motor frame ground: Same gauge as power conductors
- Chassis ground: 14 AWG minimum to earth ground (green/yellow wire)
- VFD PE (protective earth): Same gauge as input power, <0.1Ω to cabinet ground

### E.4.2 Shielded Cable and Grounding

**Shield Types:**
- **Foil shield (aluminum polyester):** 85-90% coverage, lightweight, low cost
- **Braided shield (tinned copper):** 90-98% coverage, flexible, higher cost
- **Spiral/serve shield:** 80-85% coverage, very flexible, low coverage

**Shield Grounding:**
- **Single-end grounding:** Shield grounded at source (driver) only, prevents ground loops
- **Both-ends grounding:** Shield grounded at both source and load, better for high-frequency EMI (>1 MHz)

**CNC Signal Recommendations:**
- **Encoder cables:** Shielded twisted-pair, shield grounded at driver end only
- **Stepper/servo motor cables:** Shielded, both ends grounded (motor frame + driver PE)
- **Analog signals (0-10V, ±10V):** Shielded twisted-pair, single-end ground, differential if possible
- **Limit switches:** Unshielded OK for short runs (<3m), shielded for long runs or high-noise environments

### E.4.3 Cable Routing and Separation

**Separation Distances (IEC 61800-3):**

| Cable Type | Separation from Power Cables (cm) |
|------------|----------------------------------|
| **Low-voltage power (<50V DC, signal)** | 30 cm minimum |
| **Shielded signal (encoder, analog)** | 15 cm minimum |
| **Motor power cables (unshielded)** | 50 cm from signal cables |
| **High-frequency VFD output** | 100 cm from sensitive signals |

**Cable Tray/Routing:**
- Separate trays for power and signal (or metal divider in same tray)
- Cross power/signal cables at 90° (minimize coupling)
- Avoid running cables parallel for >1m

---

## E.5 Control Voltage Standards

### E.5.1 Common Control Voltages

| Voltage | Type | Typical Use | Safety | Distribution |
|---------|------|-------------|--------|--------------|
| **24V DC** | Extra-low | Logic, PLC I/O, relays, sensors | Touch-safe | Standard industrial |
| **24V AC** | Extra-low | Older PLCs, some sensors | Touch-safe | Less common (legacy) |
| **12V DC** | Extra-low | Cooling fans, LED indicators | Touch-safe | Automotive-style |
| **5V DC** | Extra-low | TTL logic, microcontrollers | Touch-safe | Modern electronics |
| **3.3V DC** | Extra-low | Modern microcontrollers, FPGA | Touch-safe | High-speed digital |

**CNC Standard:** 24V DC (most common, compatible with industrial components)

### E.5.2 24V DC Power Supply Sizing

**Formula:**

$$P_{PSU} = \sum P_{devices} \times 1.3 \text{ (safety factor)}$$

**Example CNC System:**
- PLC/controller: 5W
- HMI touchscreen: 15W
- Limit switches (10×): 2W total
- Relay coils (5×): 10W total
- Cooling fans (3×): 12W total
- LED indicators: 3W total

$$P_{total} = (5 + 15 + 2 + 10 + 12 + 3) \times 1.3 = 61 \text{ W}$$

**Select 100W (24V, 4.2A) power supply for margin**

**Inrush Current:** PSU should handle 5-10× rated current for 10-100ms (capacitor charging). Most modern PSUs handle this automatically.

---

## E.6 Connectors and Terminations

### E.6.1 Industrial Connector Standards

| Connector Type | Pins | Current/Pin (A) | IP Rating | Mating Cycles | Applications |
|---------------|------|---------------|-----------|---------------|--------------|
| **M12 (A-coded, 5-pin)** | 3-5 | 4 | IP67 | 500 | Sensors, encoders, actuators |
| **M12 (B-coded, 5-pin)** | 5 | 4 | IP67 | 500 | Profibus, DeviceNet fieldbus |
| **M8 (3-pin)** | 3 | 2 | IP67 | 500 | Compact sensors, proximity switches |
| **M23 (12-pin)** | 12-19 | 3-5 | IP67 | 500 | Multi-signal (motor power + encoder) |
| **Han (Harting)** | 10-108 | 10-16 | IP65 | 500 | Heavy-duty motor, panel interconnect |
| **D-Sub (DB9, DB25)** | 9, 25 | 1-5 | IP20 | 100 | Parallel port (obsolete), RS232/422 |
| **RJ45 (8P8C)** | 8 | 1.5 | IP20 | 1000+ | Ethernet, Modbus RTU (not recommended for motor cables) |

**Recommendation:**
- **Limit switches, sensors:** M12 or M8 (field-installable, waterproof)
- **Stepper/servo motors:** Pre-wired cables with specific connectors (vendor-supplied) or terminal blocks
- **Control cabinet interconnect:** Phoenix Contact PCB terminal blocks or Wago lever-lock connectors

### E.6.2 Wire Termination Methods

**Crimp Terminals (Ferrules):**
- Twin ferrules for two wires in one terminal block hole
- Insulated ferrules (color-coded: 0.5mm² = white, 1.0mm² = red, 2.5mm² = blue)
- Requires crimping tool (ratcheting recommended for consistent crimp quality)

**Solder:**
- Acceptable for low-vibration environments
- **NOT recommended** for terminal blocks (solder creeps, connection loosens over time)
- OK for PCB connections, low-current signal wires

**Wire Nuts (Twist-On Connectors):**
- **NOT suitable for CNC** (vibration loosens, not industrial-rated)
- Use Wago lever-lock connectors instead (tool-less, vibration-proof, reusable)

**Terminal Block Torque Specifications:**

| Wire Gauge (AWG) | Terminal Screw Size | Torque (N·m) |
|-----------------|-------------------|-------------|
| 24-22 | M2.5 | 0.4 |
| 20-18 | M3 | 0.6 |
| 16-14 | M3.5 | 0.8 |
| 12-10 | M4 | 1.2 |

**Use calibrated torque screwdriver** to prevent under/over-tightening (common failure mode).

---

## E.7 Emergency Stop (E-Stop) Circuits

### E.7.1 E-Stop Requirements (ISO 13850, IEC 60204-1)

**E-Stop Button:**
- Red mushroom head, yellow background
- Latching (stays pressed until manually reset)
- Break-before-make contacts (NC contact opens before any NO contact closes)

**E-Stop Circuit:**
- Hardwired (not through software)
- Series circuit (all E-stop buttons in series)
- Redundancy: Dual-channel (two independent circuits)
- Monitoring: Safety relay monitors both channels for faults

**Categories (ISO 13849-1):**
- **Category 0:** Uncontrolled stop (power removed immediately)
- **Category 1:** Controlled stop (controlled deceleration, then power removed)

**CNC Recommendation:** Category 0 (immediate power cut to motors, close spindle contactor)

### E.7.2 Safety Relay Selection

**Function:**
- Monitors E-stop circuit for faults (contact welding, wire short)
- Provides redundant outputs (typically 2 or 4 safety outputs)
- Self-testing (checks own operation on each cycle)

**Safety Integrity Level (SIL):**
- **SIL 1:** 10⁻⁵ to 10⁻⁶ failures/hour (basic automation)
- **SIL 2:** 10⁻⁶ to 10⁻⁷ failures/hour (standard industrial)
- **SIL 3:** 10⁻⁷ to 10⁻⁸ failures/hour (critical safety, large machines)

**CNC Recommendation:** SIL 2 safety relay (Pilz PNOZ, Phoenix Contact PSR series)

**E-Stop Circuit Example:**

```
E-Stop 1 (NC) ----[====]----+
                            |
E-Stop 2 (NC) ----[====]----+---> Safety Relay Channel A
                            |
                            +---> Safety Relay Channel B

Safety Relay Outputs:
- Output 1 (NO) -> Motor enable (all axes)
- Output 2 (NO) -> Spindle contactor coil
- Output 3 (NC) -> Fault indicator (light/buzzer)
```

---

**End of Electrical Standards and Wiring Appendix**
