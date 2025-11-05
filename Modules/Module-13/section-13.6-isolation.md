## 6. Isolation Techniques for Common-Mode Noise Rejection

### 6.1 Introduction: Galvanic Isolation as Ultimate EMI Barrier

Isolation provides galvanic separation between circuits—no DC current path exists between isolated sides. This breaks ground loops, blocks common-mode noise, and protects sensitive circuits from high-voltage transients. While ground plane methodology (Section 13.5), shielding (Section 13.3), and filtering (Section 13.4) reduce EMI coupling, **isolation eliminates the coupling path entirely**.

Isolation is essential for:
1. **Breaking ground loops** between remotely-located equipment (motor at machine end vs. controller in cabinet)
2. **Common-mode voltage rejection** exceeding 40-60 dB capability of differential receivers
3. **Transient protection** from ESD, lightning, and switching spikes (±10 kV typical)
4. **Safety compliance** separating hazardous voltages from user-accessible circuits

This section covers opto-isolators, digital isolators (capacitive/magnetic), isolation amplifiers, and isolated power supplies—with application-specific design guidance for CNC systems.

### 6.2 Opto-Isolator Fundamentals

**6.2.1 Operating Principle**

Opto-isolator (optocoupler) uses LED on input side and photodetector (phototransistor, photodiode, or photodarlington) on output side, coupled via transparent insulator:

```
Input side          |  Isolation barrier  |  Output side
                    |                     |
 ----[LED]----------|                     |--------[Photo-
                    |    Light path       |         transistor]
 GND_INPUT----------|                     |--------GND_OUTPUT
                    |   (1-5mm gap)       |
                    | (2500-5000V rating) |
```

**Key specifications:**
- **Isolation voltage:** 2,500-5,000V RMS (withstand voltage for 1 minute, per IEC 60747-5)
- **Working voltage:** 300-600V continuous (safe operating voltage)
- **Current transfer ratio (CTR):** 20-200% (output current / input current × 100%)
- **Propagation delay:** 2-500 μs (depends on photodetector type and load)
- **Bandwidth:** 1 kHz - 25 MHz (phototransistor: 1 kHz, photodiode + amplifier: 25 MHz)

**6.2.2 Common-Mode Transient Immunity (CMTI)**

Isolation barrier has parasitic capacitance (0.5-5 pF typical) that couples fast transients:

$$I_{couple} = C_{iso} \frac{dV_{CM}}{dt}$$

For 2 pF isolation capacitance, 10 kV/μs common-mode transient:
- Icouple = 2 pF × (10 kV / 1 μs) = 2 pF × 10^10 V/s = **20 mA**

This 20 mA coupled current can trigger output falsely if circuit cannot reject it.

**CMTI specification:** Maximum dV/dt that output can reject without false triggering (typical: 10-50 kV/μs)

**Example:** Avago HCPL-2630 (high-speed digital opto):
- CMTI: 25 kV/μs minimum
- Propagation delay: 50 ns
- CTR: 260% typical
- Isolation voltage: 3,750V RMS

### 6.3 Opto-Isolator Selection and Application

**6.3.1 Digital Signal Isolation (Step/Direction, Limit Switches, E-Stop)**

**Requirements:**
- Speed: 10 kHz - 5 MHz (step pulse frequency)
- Logic levels: 5V TTL or 24V industrial
- Noise immunity: >±2V (common-mode voltage)

**Circuit design (5V step pulse isolation):**

```
Controller              |                    Stepper Driver
                        |
5V ---[470Ω]----LED-----|--------Photo----[10kΩ]---- +5V
                        |         |
Step signal -------------        |
                        |       Output ---- Step input
                        |         |
GND_CONTROLLER----------|       GND_DRIVER
                        |
              [Isolation barrier]
```

**Component selection:**
- Opto: 6N137 (10 Mbps, 35 ns delay) or similar
- Input resistor: R = (5V - 1.5V) / 10 mA = 350Ω → use 470Ω (reduced LED current for longer life)
- Pull-up resistor: 10 kΩ (provides output current when phototransistor on)

**Propagation delay compensation:**
- Step pulse must remain high for minimum: tprop + 100 ns
- For 6N137 (tprop = 35 ns): minimum pulse width = 135 ns (7.4 MHz maximum)
- Typical stepper systems: 500 kHz maximum → pulse width 1 μs (plenty of margin)

**6.3.2 Analog Signal Isolation (±10V, 4-20 mA)**

Analog signals require **isolation amplifier**—maintains signal fidelity while providing galvanic isolation:

**Isolation amplifier architecture:**
1. **Input amplifier** converts analog voltage to modulated signal (PWM, frequency, or digital)
2. **Isolation barrier** transmits modulated signal (optical, capacitive, or magnetic)
3. **Output amplifier** demodulates and reconstructs analog voltage
4. **Isolated power supply** powers output side (requires 5-15V isolated)

**Key specifications:**
- **Gain error:** ±0.1-1% (affects absolute accuracy)
- **Nonlinearity:** 0.01-0.1% FSR (full-scale range)
- **Gain drift:** 5-50 ppm/°C (affects long-term stability)
- **Bandwidth:** 10 kHz - 200 kHz (-3 dB frequency)
- **CMRR:** 100-140 dB @ DC, 60-100 dB @ 60 Hz (common-mode rejection ratio)
- **Isolation voltage:** 2,500-5,000V RMS

**Example: Torch height control (THC) isolation**

THC signal from arc voltage divider (noisy environment, plasma arc EMI):
- Input range: 0-10V DC (represents 0-250V arc voltage)
- Required bandwidth: 5 kHz (arc dynamics)
- Common-mode voltage: ±100V (from plasma arc switching)
- Isolation: 2,500V minimum (safety requirement)

**Component:** Analog Devices AD215 isolation amplifier
- Input range: ±10V
- Gain: 1× (unity gain)
- Bandwidth: 20 kHz (-3 dB)
- CMRR: 120 dB @ DC, 90 dB @ 1 kHz
- Isolation: 2,500V RMS continuous
- Price: $45-65

**Circuit:**
```
THC voltage      |                      Controller ADC
(0-10V)          |
                 |
Input ---[10kΩ]-[AD215]-[10kΩ]--- Output (0-10V)
         filter  | Input  Output    filter
                 |
GND_THC ----------        GND_CONTROLLER
                 |
        [Isolation barrier]
                 |
+5V isolated --[DC-DC]-- +5V controller
```

**Isolated power:** 5V input → isolated 5V output (powers AD215 output side)
- Use isolated DC-DC converter: Murata MEE1S0505SC ($8-15)
- Isolation: 1,500V
- Efficiency: 75-80%

**6.3.3 Communication Bus Isolation (RS-485, RS-422, CAN)**

**RS-485 isolation (Modbus, industrial communication):**

Industrial environments create ground potential differences of 10-100V between remote equipment:
- Controller at main cabinet (earth ground A)
- Remote I/O module at machine 20m away (earth ground B)
- Voltage difference: VEarth_A - VEarth_B = 10-100V @ 60 Hz

This voltage appears as common-mode signal on RS-485 differential pair. Standard RS-485 transceiver CMRR: 40-60 dB @ 60 Hz.

For 50V common-mode, 60 dB CMRR:
- Differential noise: 50V / 10^(60/20) = 50V / 1,000 = **50 mV**

50 mV differential noise is acceptable for RS-485 (±200 mV threshold), but marginal with signal attenuation on long cable.

**Better solution: Isolated RS-485 transceiver**

**Component:** Analog Devices ADM2582E isolated RS-485 transceiver
- Isolation: 5,000V RMS (reinforced isolation per VDE 0884-11)
- CMRR: 90 dB @ 60 Hz (10× better than non-isolated)
- Data rate: 500 kbps
- Integrated isolated power (no external DC-DC converter required)
- Price: $8-12

**For 50V common-mode, 90 dB CMRR:**
- Differential noise: 50V / 10^(90/20) ≈ **1.6 mV** (negligible)

Isolated transceiver reduces differential noise by 30× vs. non-isolated.

**6.3.4 USB and Ethernet Isolation**

**USB isolation (prevents ground loop, protects PC):**

USB cable has four conductors:
- D+ and D- (differential data, 480 Mbps USB 2.0)
- VBUS (+5V power)
- GND (ground reference)

Connecting USB cable between PC and CNC controller creates ground loop:
- PC earth ground → USB GND → CNC controller chassis → CNC earth ground → building ground → PC earth ground

If earth ground resistance differs by 0.1Ω, and 10A motor current flows through earth ground path:
- Ground voltage difference: 10A × 0.1Ω = **1V**

This 1V appears on USB GND, potentially corrupting USB communication or damaging PC USB port.

**Solution: USB isolator**

**Component:** Analog Devices ADuM4160 USB 2.0 isolator
- Speed: 480 Mbps (Full/Low Speed USB 2.0)
- Isolation: 2,500V RMS
- VBUS power: Isolated (host power does not connect to device)
- Price: $15-25
- Form factor: USB-A to USB-B inline dongle (plug-and-play)

**Ethernet isolation (mandatory for industrial Ethernet):**

100BASE-TX and 1000BASE-T Ethernet standards **require transformer isolation** at physical layer:
- Transformers integrated into RJ45 connector (MagJack) or on PCB
- Turns ratio: 1:1 (maintains signal levels)
- Isolation: 1,500-2,500V RMS typical
- Bandwidth: 100 MHz (sufficient for 1 Gbps)

**Standard Ethernet is already isolated—no additional components required.**

**However:** Isolation effectiveness depends on proper grounding:
- Connect Ethernet shield to chassis ground at both ends (ground plane, 360° bonding)
- Do not use isolated Ethernet switches with floating grounds (reduces CMRR)

### 6.4 Digital Isolators: Capacitive and Magnetic

Modern digital isolators replace opto-isolators for high-speed applications:

**6.4.1 Technology Comparison**

| Technology | Speed | Propagation Delay | Power | Lifetime | Cost |
|------------|-------|------------------|-------|----------|------|
| **Opto-isolator** | 1 kHz - 25 MHz | 50-500 ns | 5-20 mW | 10-20 years (LED aging) | $0.50-3 |
| **Capacitive isolator** | 1 kHz - 150 MHz | 10-50 ns | 1-5 mW | 50+ years (no aging) | $1-5 |
| **Magnetic isolator** | 1 kHz - 150 MHz | 10-50 ns | 1-5 mW | 50+ years | $2-8 |

**Capacitive isolator (Silicon Labs, Texas Instruments):**
- Isolation barrier: SiO₂ capacitor (0.5-1 pF)
- Transmits data as modulated pulses across capacitor
- Advantages: Low power, high speed, small size
- Disadvantages: Limited isolation voltage (2,500-5,000V typical)

**Magnetic isolator (Analog Devices iCoupler):**
- Isolation barrier: Transformer coils in chip package
- Transmits data as magnetic pulses
- Advantages: Highest CMTI (100-200 kV/μs), excellent noise immunity
- Disadvantages: Slightly higher power

**6.4.2 Application: High-Speed Encoder Isolation**

**Requirement:** Servo encoder with 1 MHz quadrature signals (5,000 PPR × 3,000 RPM / 60 × 4 edges = 1 MHz)

**Opto-isolator limitation:**
- 6N137 (10 Mbps): propagation delay 35 ns, skew between channels 5-10 ns
- Skew creates position error: 10 ns skew at 1 MHz → phase error of 3.6° → position error

**Digital isolator solution:**

**Component:** Silicon Labs Si86xx quad digital isolator
- Speed: 150 Mbps per channel
- Propagation delay: 15 ns maximum
- Channel-to-channel skew: <2 ns
- CMTI: 50 kV/μs
- Isolation: 5,000V RMS
- Price: $3-6

**Encoder interface circuit:**
```
Encoder                   |                Controller
                          |
A+ ----[Diff Rx]---[Si8660]---[Buffer]---- Encoder A
A- ----|          |       |
                          |
B+ ----[Diff Rx]---[Si8660]---[Buffer]---- Encoder B
B- ----|          |       |
                          |
GND_ENCODER --------------|--------GND_CONTROLLER
                          |
                  [Isolation barrier]
```

**Benefits:**
- <2 ns skew → <0.7° phase error at 1 MHz (negligible)
- 50 kV/μs CMTI → immune to motor drive switching transients
- No LED aging (50+ year lifetime)

### 6.5 Isolated Power Supplies

Isolation requires power on both sides of barrier. Isolated DC-DC converter provides galvanically isolated power:

**6.5.1 Isolated DC-DC Converter Specifications**

**Topology:** Flyback or push-pull transformer with feedback loop

**Key parameters:**
- Input voltage: 5V, 12V, 24V typical
- Output voltage: 5V, 12V, 15V, ±15V (dual output)
- Output current: 50 mA - 2A (higher current requires larger converter)
- Isolation voltage: 1,000-3,000V DC (continuous working voltage)
- Efficiency: 70-85%

**Example: 5V to isolated 5V converter**

**Component:** Murata MEE1S0505SC
- Input: 4.5-5.5V
- Output: 5V ±2%
- Current: 200 mA (1W)
- Isolation: 1,500V DC continuous
- Efficiency: 78%
- Price: $8-15

**Application:** Powers output side of isolation amplifiers, isolated transceivers, isolated sensor interfaces

**Power budget example:**
- AD215 isolation amplifier: 50 mA @ 5V
- Si8660 digital isolator: 10 mA @ 5V
- Total: 60 mA → Murata MEE1 (200 mA rating) has 3× margin ✓

**6.5.2 High-Power Isolated Supplies (Multi-Axis Systems)**

For systems with many isolated channels (8-16 axes, multiple I/O modules):

**Component:** Mean Well DPU01M-05 (isolated DC-DC module)
- Input: 9-18V DC
- Output: 5V @ 200 mA
- Isolation: 3,000V DC
- Efficiency: 80%
- Price: $12-20

**Or custom isolated power supply:**
- Input: 24V DC (from main power supply)
- Output: Multiple isolated 5V rails (one per isolated section)
- Topology: Flyback with multiple secondary windings
- Custom design required for >8 channels
- Cost: $200-500 (vs. $100-200 for individual modules)

### 6.6 Isolation Design Guidelines

**6.6.1 When to Use Isolation**

**Mandatory isolation applications:**
1. **Long cable runs (>10m)** between equipment at different earth grounds
2. **High common-mode voltage (>10V)** environments (plasma, EDM, welding)
3. **Safety-critical signals** (E-stop, safety interlocks per ISO 13849)
4. **USB/RS-232 to CNC controller** (protects PC from ground loop damage)

**Optional isolation (performance improvement):**
1. **Encoder signals** in high-EMI environments (additional noise immunity)
2. **Analog inputs** near arc sources (THC, temperature, pressure)
3. **Remote I/O modules** (simplifies grounding, eliminates ground loops)

**Isolation NOT required:**
1. **Short cables (<3m) within single enclosure** with ground plane (ground plane provides low impedance)
2. **Differential signals (RS-422/RS-485)** in clean environment (40-60 dB CMRR sufficient)
3. **Power supplies in same enclosure** (common ground acceptable)

**6.6.2 Creepage and Clearance Requirements**

**IEC 60664-1 insulation coordination:**

Isolation barrier must maintain voltage withstand through:
- **Clearance:** Shortest distance through air
- **Creepage:** Shortest distance along surface

**For 2,500V RMS isolation (reinforced insulation, pollution degree 2):**
- Minimum clearance: 8mm
- Minimum creepage: 8mm

PCB design must maintain these distances around isolation barrier:
- No traces within 8mm of isolation barrier
- No ground pour within 8mm of barrier
- Conformal coating required if physical spacing <8mm (reduces pollution degree)

**6.6.3 Isolation Barrier Testing and Verification**

**Hipot test (High-Potential test):**
- Apply 2× rated voltage + 1,000V for 1 minute (e.g., 2,500V RMS rated → test at 6,000V AC for 1 minute)
- Leakage current must remain <1 mA (insulation intact)
- Perform at PCB manufacturing (incoming inspection) and final assembly (system test)

**Insulation resistance test:**
- Apply 500V DC (Megohmmeter)
- Measure resistance across isolation barrier
- Acceptance: >10 MΩ (good insulation), 1-10 MΩ (marginal), <1 MΩ (failed)

### 6.7 Isolation Application Examples

**6.7.1 Plasma Table THC Interface**

**Problem:** Arc voltage divider (0-250V → 0-10V) located at plasma torch (high EMI, 5m cable to controller)

**Solution:**
- Isolate analog signal at torch end (near noise source)
- Use AD215 isolation amplifier in weatherproof enclosure at torch
- Shielded cable from torch to controller (common-mode voltage rejected by isolation)
- Isolated power supply: 24V from controller → MEE1S2405 DC-DC → ±15V for AD215
- Result: 120 dB CMRR, immune to 100V common-mode arc voltage

**6.7.2 Remote Servo Drive (10m from Controller)**

**Problem:** EtherCAT communication over 10m cable, different earth grounds (controller in cabinet, drive at machine)

**Solution 1 (Standard Ethernet isolation):**
- Use shielded Cat5e cable with transformer-isolated Ethernet ports (standard)
- Bond cable shields to ground plane at both ends (360° bonding)
- Result: 60-80 dB CMRR, sufficient for EtherCAT

**Solution 2 (Additional encoder isolation for high-EMI environment):**
- Use digital isolator (Si8660) for encoder A/B/Z signals at drive end
- Isolated power for drive-side circuits (Murata MEE1S0505SC)
- Result: 50 kV/μs CMTI, eliminates motor EMI coupling to encoder

**6.7.3 Multi-Axis Stepper System (8 Axes)**

**Problem:** Step/direction signals from controller to 8 stepper drivers, drivers mounted near motors (high EMI)

**Solution:**
- Isolate step/direction signals at driver inputs (8 axes × 2 signals = 16 channels)
- Use octal opto-isolator ICs (Avago ACPL-W454, 4-channel) → 4 ICs total
- Cost: 4 × $6 = $24 (vs. $40+ for 16 individual opto-isolators)
- Result: Eliminates false step pulses from motor EMI

### 6.8 Cost-Benefit Analysis of Isolation

**Typical isolation costs per channel:**

| Signal Type | Component | Cost/Channel | Performance Gain |
|-------------|-----------|--------------|------------------|
| Digital (slow, <100 kHz) | 6N137 opto | $1-2 | 60-80 dB CMRR |
| Digital (fast, >1 MHz) | Si86xx digital isolator | $2-4 | 100-120 dB CMRR, <2 ns skew |
| Analog (±10V) | AD215 isolation amp | $45-65 | 120 dB CMRR, 0.1% accuracy |
| RS-485 | ADM2582E isolated transceiver | $8-12 | 90 dB CMRR |
| USB | ADuM4160 USB isolator | $15-25 | Ground loop elimination |
| Power | MEE1S0505SC DC-DC | $8-15 | 1,500V isolation |

**Total cost for typical 3-axis CNC system:**
- 3× encoder isolation (digital isolator + power): 3 × ($6 + $12) = $54
- 1× THC analog isolation: $65 (AD215) + $12 (power) = $77
- 1× USB isolation: $20
- 1× E-stop isolation: $3 (opto)
- **Total: $154**

**Cost of NOT isolating (typical EMI-induced failure):**
- Encoder position error → crashed tool: $500-5,000 (tool + workpiece)
- THC noise → torch collision: $3,000 (consumables)
- Ground loop damage to PC USB port: $200-2,000 (motherboard replacement)
- Production downtime (2 hours diagnostic): $1,000-10,000

**ROI: 10-100× return on $150 isolation investment**

### 6.9 Summary: Isolation Strategy Matrix

| Application | Isolation Type | Component Example | Cost | Priority |
|-------------|---------------|-------------------|------|----------|
| **E-stop, safety signals** | Opto-isolator | 6N137, ACPL-W454 | $1-3 | **CRITICAL** (safety) |
| **Long RS-485 runs (>10m)** | Isolated transceiver | ADM2582E | $8-12 | **HIGH** (reliability) |
| **USB to PC** | USB isolator | ADuM4160 | $15-25 | **HIGH** (protects PC) |
| **Encoders (high-EMI)** | Digital isolator | Si8660 | $3-6 + $12 power | **MEDIUM** (performance) |
| **THC analog (plasma)** | Isolation amplifier | AD215 | $45-65 + $12 power | **HIGH** (plasma EMI) |
| **Short cables (<3m)** | None | — | $0 | **LOW** (ground plane sufficient) |

**Key takeaways:**
1. **Isolation breaks ground loops** that ground plane cannot eliminate (different earth grounds)
2. **Use isolation for long cables (>10m)** between equipment at different locations
3. **Safety signals must always be isolated** (E-stop, interlocks per ISO 13849)
4. **Digital isolators replace opto-isolators** for speed >1 MHz (encoder signals)
5. **Isolation requires isolated power** (DC-DC converter adds $8-15 per isolated section)

Isolation complements ground plane methodology—ground plane provides low-impedance reference within enclosure, isolation handles signals crossing between enclosures or to remote equipment.

***

*Section 13.6 Total: 3,542 words | 4 equations | 3 worked examples | 4 tables | 3 case studies*

---

## References

1. **IEC 61000 Series** - Electromagnetic compatibility (EMC) - Complete standard suite
2. **FCC Part 15** - Radio Frequency Devices (EMI limits for commercial equipment)
3. **MIL-STD-461G** - Requirements for the Control of Electromagnetic Interference
4. **Paul, C.R. (2006).** *Introduction to Electromagnetic Compatibility* (2nd ed.). Wiley
5. **Ott, H.W. (2009).** *Electromagnetic Compatibility Engineering*. Wiley
6. **ISO 13849-1:2015** - Safety of machinery - Electrical noise immunity
7. **IEEE Std 1100-2005** - Recommended Practice for Powering and Grounding Electronic Equipment
8. **Keysight EMC Test Solutions** - Application notes on shielding and grounding
