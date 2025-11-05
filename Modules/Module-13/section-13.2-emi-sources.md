## 2. EMI Sources and Characterization in Motion Control Systems

### 2.1 Introduction to Noise Source Identification

Effective EMC design begins with identifying and characterizing electromagnetic interference sources within CNC and robotic systems. Unlike external interference (radio transmitters, lightning, nearby equipment), internal EMI sources are deterministic and controllable through proper design. Understanding source characteristics—frequency spectrum, amplitude, rise time, repetition rate—enables selection of appropriate mitigation strategies before problems manifest as system failures.

**Primary EMI Categories in Motion Control:**
1. **Switching power electronics**: PWM motor drives, DC-DC converters, rectified power supplies
2. **Arc discharge sources**: Plasma cutting, spindle motor commutation, electrical discharge machining (EDM)
3. **High-speed digital circuits**: Microcontrollers, FPGA clock distribution, communication buses
4. **Magnetic field generators**: Transformers, relay coils, solenoid valves, motor windings

This section provides quantitative analysis methods for each source category, enabling prediction of coupling mechanisms and specification of mitigation requirements.

### 2.2 PWM Motor Drive Emissions: Dominant EMI Source

Pulse-width modulation (PWM) drives for servo motors and spindles represent the largest single EMI source in CNC systems. Modern drives switch 10-100A at 4-20 kHz (industrial servo) or 30-100 kHz (permanent magnet brushless) with rise times of 50-200 ns, generating broadband emissions from fundamental frequency to >100 MHz.

**2.2.1 PWM Switching Waveform Analysis**

Typical servo drive configuration:
- DC bus voltage: 325V (240VAC rectified) or 560V (480VAC rectified)
- Output current: 5-50A RMS per phase
- PWM frequency: 4-20 kHz (industrial), 8-16 kHz most common
- Switching device: IGBT (Insulated Gate Bipolar Transistor)
- Rise/fall time: 50-200 ns (depends on gate drive and IGBT rating)

**Fourier Analysis of PWM Spectrum:**

Ideal square wave with 50% duty cycle contains only odd harmonics:

$$v(t) = \frac{4V_{DC}}{\pi} \sum_{n=1,3,5...}^{\infty} \frac{1}{n} \sin(2\pi n f_{PWM} t)$$

For 16 kHz PWM at 325V DC bus:
- Fundamental (16 kHz): 414V peak (4 × 325 / π)
- 3rd harmonic (48 kHz): 138V peak (414V / 3)
- 5th harmonic (80 kHz): 83V peak
- 7th harmonic (112 kHz): 59V peak
- Higher harmonics decrease as 1/n

**Real-World PWM Spectrum with Finite Rise Time:**

Finite rise time (tr) adds high-frequency components beyond ideal square wave. Spectral amplitude rolls off above corner frequency:

$$f_{corner} = \frac{0.35}{t_r}$$

For tr = 100 ns:
- fcorner = 0.35 / (100 × 10⁻⁹) = 3.5 MHz

Above 3.5 MHz, spectrum decreases at -20 dB/decade (first-order rolloff) to approximately -40 dB/decade (due to parasitic capacitance and inductance).

**Measured PWM Drive Spectrum (16 kHz, 100 ns rise time, 325VDC):**

| Frequency | Voltage Amplitude (dBV) | Voltage Amplitude (V peak) | Notes |
|-----------|-------------------------|---------------------------|-------|
| 16 kHz (fundamental) | 52 dBV | 400V | Near theoretical ideal |
| 48 kHz (3rd) | 42 dBV | 126V | -10 dB from fundamental |
| 80 kHz (5th) | 38 dBV | 79V | -14 dB |
| 160 kHz (10th) | 32 dBV | 40V | -20 dB |
| 1 MHz | 18 dBV | 8V | -34 dB, above corner frequency |
| 10 MHz | -2 dBV | 0.8V | -54 dB, still sufficient to corrupt signals |
| 100 MHz | -22 dBV | 0.08V | -74 dB |

Even at 10 MHz (54 dB below fundamental), 0.8V emissions can corrupt 5V digital signals or saturate high-gain analog inputs if coupled via poor grounding or unshielded cables.

**2.2.2 Common-Mode vs. Differential-Mode Currents**

PWM drives generate both differential-mode (motor phase currents) and common-mode (capacitive coupling to ground) currents:

**Differential-Mode Current:**
- Motor phase current: 5-50A RMS
- Frequency: PWM fundamental and harmonics
- Path: Drive output → motor winding → return
- Mitigation: Differential-mode chokes (Section 13.4)

**Common-Mode Current (Dominant EMI):**

Parasitic capacitance between motor windings and motor frame couples high-frequency PWM voltage to ground:

$$I_{CM} = C_{parasitic} \frac{dV_{CM}}{dt}$$

Typical motor parasitic capacitance: 100-500 pF per phase (larger motors higher)

For 325V PWM with 100 ns rise time:
- dV/dt = 325V / 100ns = 3.25 GV/s
- CCM = 300 pF (typical 3-phase servo motor)
- ICM = 300 pF × 3.25 GV/s = **0.975A peak common-mode current**

This ~1A common-mode current flows through motor cable shield (if present), motor frame, machine structure, and ground return path—creating ground potential differences and radiating from cable if unshielded.

**Common-mode current path:**
1. Drive DC bus capacitor → motor cable parasitic capacitance
2. Motor frame → machine structure → earth ground
3. Earth ground → drive chassis → DC bus return

**Critical insight:** Common-mode current is 10-100× smaller amplitude than differential motor current (1A vs. 10-50A), but more problematic because:
- Higher frequency content (MHz range vs. kHz motor current)
- Flows through uncontrolled paths (ground structure, cable shields)
- Creates voltage drops across ground impedances (causes signal corruption)
- Radiates efficiently from cables acting as antennas (compliance failures)

### 2.3 Switching Power Supply Emissions

DC-DC converters and switch-mode power supplies (SMPS) for 5V, 12V, 24V, and 48V rails generate high-frequency emissions from 50 kHz to 5 MHz.

**Typical Buck Converter (Step-Down) Topology:**
- Input voltage: 24-48VDC (from rectified AC or battery)
- Output voltage: 3.3V, 5V, 12V, 24V
- Switching frequency: 50-500 kHz (higher for compact design)
- Output current: 1-50A
- Switching device: MOSFET (50-200V rating)

**Switching Transient Analysis:**

High-side MOSFET switches input voltage to inductor at fsw (e.g., 200 kHz), creating square wave with amplitude equal to input voltage.

For 48V input, 200 kHz switching, 50 ns rise time:
- dV/dt = 48V / 50ns = 0.96 GV/s
- PCB trace parasitic capacitance to ground: 10-50 pF
- Common-mode current: ICM = 30 pF × 0.96 GV/s = **28.8 mA**

**Conducted Emissions on Input Power Lines:**

SMPS draws pulsed current from input supply, creating voltage ripple on power distribution:

$$\Delta V = I_{pulse} \cdot Z_{line}(f)$$

For 10A output at 80% efficiency (12.5A input average), with 20% ripple current:
- Ipulse = 12.5A × 0.2 = 2.5A peak-to-peak at 200 kHz
- Power line impedance at 200 kHz: 0.5-2Ω typical (wire inductance dominant)
- Voltage ripple: ΔV = 2.5A × 1Ω = 2.5V at 200 kHz

This 2.5V ripple propagates to all devices on shared power bus, potentially corrupting analog references and digital logic thresholds.

**Mitigation Preview (Detailed Section 13.4):**
- Input line filter (LC filter with X and Y capacitors): -40 dB at switching frequency
- Output capacitors (low-ESR electrolytic + ceramic): <50 mV output ripple
- Shielded enclosure for converter module: -30 to -60 dB radiated emission reduction

### 2.4 Plasma Arc and High-Voltage Arc Sources

Plasma cutting torches, EDM spark gaps, and spindle motor brush commutation generate extremely broadband EMI from DC to >1 GHz via electrical arc discharge.

**2.4.1 Plasma Cutting Arc Characteristics**

Plasma arc parameters (typical CNC plasma table):
- Arc voltage: 100-250V DC (depends on material, gas, current)
- Arc current: 20-200A (thickness-dependent)
- Arc initiation: 5-15 kV high-frequency (HF) start pulse, 10-50 μs duration
- Arc re-ignition rate: 100-400 kHz (arc instability, electrode wear)
- Torch cable length: 3-10m (acts as antenna)

**Arc Noise Spectrum:**

Plasma arc exhibits white noise characteristic from DC to 500 MHz, with peak energy at 100-400 kHz (arc instability frequency):

| Frequency Band | Measured Emission Level | Source Mechanism |
|----------------|------------------------|------------------|
| DC - 10 kHz | 40-60 dBμV/m @ 3m | Arc current fundamental |
| 10-100 kHz | 60-80 dBμV/m @ 3m | Arc modulation, power supply switching |
| 100 kHz - 1 MHz | 80-100 dBμV/m @ 3m | Arc instability (dominant) |
| 1-10 MHz | 60-80 dBμV/m @ 3m | High-frequency components, cable resonance |
| 10-100 MHz | 40-60 dBμV/m @ 3m | Radiated from torch cable |
| 100-500 MHz | 20-40 dBμV/m @ 3m | Residual broadband |

**dBμV/m to Voltage Conversion:**

Field strength at 3m distance with 1m antenna (torch cable) approximation:

$$E (V/m) = 10^{(dB\mu V/m - 120)/20}$$

For 100 dBμV/m at 3m:
- E = 10^((100 - 120)/20) = 10^(-1) = 0.1 V/m
- Voltage induced in 1m cable: V ≈ 0.1V/m × 1m = 0.1V

However, torch cable carries arc current (20-200A) with AC component at arc instability frequency (100-400 kHz). Magnetic field couples into adjacent cables:

**Example Calculation:** 100A arc with 10% AC ripple at 200 kHz, 5m torch cable parallel to 3m encoder cable at 100mm separation:

Using mutual inductance formula for parallel conductors:

$$M = \frac{\mu_0 \ell}{\pi} \ln\left(\frac{d}{r}\right)$$

where:
- μ₀ = 4π × 10⁻⁷ H/m
- ℓ = 3m (overlap length, shorter of two cables)
- d = 0.1m (separation)
- r = 0.002m (wire radius, ~12 AWG)

$$M = \frac{4\pi \times 10^{-7} \times 3}{\pi} \ln\left(\frac{0.1}{0.002}\right) = 1.2 \times 10^{-6} \times \ln(50) = 4.7 \mu H$$

Induced voltage from 10A AC ripple at 200 kHz (dI/dt = 10A × 2π × 200 kHz = 12.6 MA/s):

$$V_{induced} = M \frac{dI}{dt} = 4.7 \times 10^{-6} \times 12.6 \times 10^6 = 59V$$

**59V spike induced into encoder cable**—far exceeding 5V logic levels, guaranteed to corrupt position data or damage encoder inputs.

**Mitigation requirements for plasma systems:**
- Torch cable separation: >200mm minimum from signal cables
- Shielded twisted-pair for all signals: -40 to -60 dB coupling reduction
- Common-mode chokes on torch leads: -20 to -40 dB emission reduction
- Metal enclosure for controller: -40 to -80 dB shielding effectiveness

### 2.5 High-Speed Digital Circuit Emissions

Microcontroller clocks, FPGA I/O toggling, and communication buses (SPI, USB, Ethernet) generate harmonics extending to 100 MHz - 1 GHz.

**2.5.1 Clock Signal Harmonics**

Microcontroller or FPGA clock with frequency fclk and rise time tr generates harmonics:

$$f_{max} \approx \frac{0.5}{t_r}$$

For 100 MHz STM32 microcontroller clock with 2 ns rise time:
- fmax = 0.5 / 2ns = 250 MHz (significant harmonic content extends to this frequency)

**Clock signal power spectrum:**
- Fundamental: 100 MHz
- Harmonics present at: 200, 300, 400, 500 MHz, etc.
- Amplitude decreases -20 dB/decade above corner frequency

**PCB trace radiation efficiency:**

PCB trace with length ℓ radiates efficiently when length approaches λ/10 (quarter-wave dipole):

$$\lambda = \frac{c}{f \sqrt{\epsilon_r}}$$

For FR4 PCB (εr ≈ 4.5):
- λ at 100 MHz = 3×10⁸ / (100×10⁶ × √4.5) = 1.41m
- λ/10 = 141mm

Clock traces >141mm length radiate 100 MHz clock directly. For 250 MHz harmonic:
- λ/10 = 56mm (very common trace length)

**Mitigation:**
- Minimize clock trace length: <20mm from oscillator to IC
- Ground plane directly under clock traces: -20 to -40 dB radiation reduction
- Series termination resistor: Slow rise time to 5-10 ns (reduces fmax to 50-100 MHz)
- Spread-spectrum clocking: Distributes energy across ±1-2% bandwidth (10-20 dB peak reduction)

**2.5.2 Differential Communication Bus Emissions**

RS-485, CAN bus, and Ethernet use differential signaling with common-mode currents generated by timing skew and amplitude imbalance:

**Common-mode voltage from differential skew:**

$$V_{CM} = \frac{V_{diff}}{2} \times \frac{t_{skew}}{t_r}$$

For RS-485 with 5V differential, 1 ns skew, 10 ns rise time:
- VCM = (5V / 2) × (1ns / 10ns) = 0.25V common-mode

This 0.25V common-mode couples to chassis ground via cable shield capacitance, generating common-mode current.

**Ethernet (100BASE-TX) emissions:**

100 Mbps Ethernet uses 125 MHz clock (4B/5B encoding) with differential signaling:
- Fundamental: 125 MHz
- Harmonics: 250, 375, 500 MHz extending to 1 GHz
- Radiated emissions without shielded cable: 60-80 dBμV/m @ 3m (exceeds FCC/CE limits)

**Requirement:** Shielded Cat5e/Cat6 Ethernet cable with 360° shield bonding at both ends mandatory for EMC compliance.

### 2.6 Transformer and Relay Magnetic Field Emissions

Power transformers (50/60 Hz), high-frequency switch-mode transformers (50-500 kHz), and relay/solenoid coils generate strong magnetic fields that induce voltages in nearby conductors.

**2.6.1 50/60 Hz Power Transformer Fields**

Large power transformers (2-20 kVA for CNC systems) generate magnetic fields at line frequency:

**Magnetic field strength near transformer:**

$$H = \frac{N I}{2\pi r}$$

where:
- N = winding turns (primary, typically 100-500 turns)
- I = magnetizing current (0.5-2A for 5 kVA transformer)
- r = distance from transformer core

For 500 turns, 1A magnetizing current, 0.2m distance:
- H = (500 × 1) / (2π × 0.2) = 398 A/m
- B = μ₀H = 4π × 10⁻⁷ × 398 = 0.5 mT (5 Gauss)

**Induced voltage in nearby cable loop:**

For signal cable forming 0.5m × 0.3m loop (0.15 m² area) at 0.2m from transformer:

$$V_{induced} = -\frac{d\Phi}{dt} = -A B \omega$$

where ω = 2πf = 2π × 60 Hz = 377 rad/s:
- Vinduced = 0.15 m² × 0.5 mT × 377 = 28 mV RMS at 60 Hz

28 mV is generally acceptable for digital signals, but problematic for high-resolution analog inputs (16-bit ADC with 10V range has LSB = 150 μV).

**Mitigation:**
- Physical separation: >500mm between transformer and signal cables
- Magnetic shielding: Mu-metal or steel enclosure around transformer (-20 to -40 dB)
- Twisted-pair cables: Mutual cancellation reduces loop area >100× (28 mV → <0.3 mV)

**2.6.2 Relay and Solenoid Transients**

Relay coil de-energization generates high-voltage spike via inductive kickback:

$$V_{spike} = -L \frac{dI}{dt}$$

For 100 mH relay coil with 100 mA coil current switching off in 10 μs:
- dI/dt = 0.1A / 10μs = 10,000 A/s
- Vspike = 100 mH × 10,000 = **1,000V spike**

Without suppression (flyback diode, snubber), this 1kV spike radiates strongly and couples into nearby circuits.

**Standard mitigation:** Flyback diode (1N4007 or equivalent) across relay coil clamps voltage to 0.7V, eliminating spike.

### 2.7 Measurement and Characterization Techniques

**2.7.1 Time-Domain Measurement with Oscilloscope**

Oscilloscope captures transient waveforms for rise time, amplitude, and repetition rate analysis:

**Key specifications:**
- Bandwidth: 5× highest frequency of interest (e.g., 500 MHz scope for 100 MHz signals)
- Sample rate: 10× bandwidth minimum (5 GS/s for 500 MHz scope)
- Differential probe: For measuring common-mode vs. differential signals

**Measurement setup for PWM drive noise:**
1. Channel 1: Motor phase voltage (100:1 high-voltage probe, 400V range)
2. Channel 2: Encoder signal (10:1 probe, 10V range)
3. Trigger: CH1 PWM edge
4. Capture: Single-shot to observe noise coupling during PWM transition

**2.7.2 Frequency-Domain Analysis with Spectrum Analyzer**

Spectrum analyzer displays frequency content from 9 kHz to 3+ GHz:

**Detector modes:**
- **Peak detector:** Captures maximum amplitude (required for EMC pre-compliance)
- **Average detector:** Averages over time (understates peak emissions)
- **Quasi-peak detector:** Weighted average (used in CISPR standards, approximates human perception)

**Typical measurement setup:**
- Frequency span: 9 kHz - 1 GHz (conducted) or 30 MHz - 6 GHz (radiated)
- Resolution bandwidth (RBW): 9 kHz (CISPR 11), 120 kHz (FCC Part 15)
- Detector: Peak for pre-compliance, quasi-peak for final compliance

**Example measurement—PWM drive conducted emissions:**
1. Insert LISN (Line Impedance Stabilization Network) between AC source and drive
2. Connect spectrum analyzer to LISN 50Ω output
3. Scan 150 kHz - 30 MHz with 9 kHz RBW, peak detector
4. Compare measured spectrum to CISPR 11 Class A limit (79 dBμV at 150 kHz, decreasing to 73 dBμV at 30 MHz)

**2.7.3 Near-Field Probe Troubleshooting**

Near-field probes (H-field magnetic loop, E-field monopole) identify local emission sources on PCBs and cables:

**H-field probe:** Small loop (10-30mm diameter) responds to magnetic fields from current-carrying conductors
- Use near: PWM output traces, motor cables, switch-mode converter inductors
- Peak response indicates high dI/dt source

**E-field probe:** Short monopole antenna (10-50mm) responds to electric fields from high-voltage nodes
- Use near: PWM DC bus capacitors, MOSFET drain nodes, high-voltage power supplies
- Peak response indicates high dV/dt source

**Technique:** Sweep probe over PCB surface while monitoring spectrum analyzer at frequency of interest (e.g., 16 kHz PWM fundamental). Peak amplitude identifies noise source location.

### 2.8 EMI Source Prioritization Matrix

Not all EMI sources require equal mitigation effort. Prioritize based on:
1. **Emission amplitude** (higher voltage/current = more severe)
2. **Frequency range** (higher frequency = more difficult to control)
3. **Coupling efficiency** (unshielded cables, large loop areas = worse)
4. **Victim sensitivity** (analog signals, high-speed digital = more susceptible)

**Prioritized Source List for Typical CNC System:**

| Source | Frequency Range | Typical Amplitude | Coupling Mechanism | Priority | Mitigation Cost |
|--------|----------------|-------------------|-------------------|----------|----------------|
| **PWM motor drive** | 4-20 kHz + harmonics to 10 MHz | 325V, 10-50A | Magnetic induction, common-mode current | **HIGHEST** | $50-300/axis |
| **Plasma arc** | DC to 500 MHz | 100-250V, 20-200A | Magnetic induction, radiation | **HIGHEST** | $200-1,000 |
| **SMPS (control power)** | 50-500 kHz + harmonics | 24-48V, 1-50A | Conducted emissions, magnetic coupling | **HIGH** | $50-200 |
| **Ethernet/USB** | 100-125 MHz + harmonics | 2-5V differential | Common-mode radiation | **MEDIUM** | $10-50/cable |
| **Microcontroller clock** | 10-100 MHz + harmonics | 3.3V, <100 mA | PCB trace radiation | **MEDIUM** | $0-20 (design) |
| **Power transformer (50/60 Hz)** | 60 Hz + harmonics | 120-240V, 5-50A | Magnetic induction (low frequency) | **LOW** | $20-100 |
| **Relay/solenoid** | Transient (1-10 kHz) | 1000V spike (unsuppressed) | Magnetic transient | **LOW** | $0.50-2 (diode) |

### 2.9 Conducted vs. Radiated Emissions

**Conducted Emissions (150 kHz - 30 MHz):**
- Propagate via power lines, signal cables, ground conductors
- Measured at equipment AC input using LISN
- Dominant below 30 MHz (wavelength >10m, cables not efficient radiators)
- Mitigation: Line filters, common-mode chokes, ground plane

**Radiated Emissions (30 MHz - 1 GHz):**
- Propagate through air as electromagnetic waves
- Measured at 3m or 10m distance in anechoic chamber or open area test site (OATS)
- Dominant above 30 MHz (wavelength <10m, cables act as antennas)
- Mitigation: Metal enclosure, cable shielding, aperture control

**Critical frequency: 30 MHz (λ = 10m)**
- Below 30 MHz: Conducted emissions dominate (filter power lines and I/O cables)
- Above 30 MHz: Radiated emissions dominate (shield enclosure and cables)

### 2.10 Summary: EMI Source Identification Methodology

Systematic approach to EMI source identification:

**Step 1: Inventory all switching sources** (PWM drives, SMPS, arcs, clocks)
**Step 2: Calculate fundamental frequencies and harmonics** (extend to 10× fundamental or fmax = 0.5/tr)
**Step 3: Measure time-domain waveforms** (oscilloscope: rise time, amplitude, repetition rate)
**Step 4: Measure frequency-domain spectrum** (spectrum analyzer: identify dominant frequencies)
**Step 5: Use near-field probes** (locate specific sources on PCBs and cables)
**Step 6: Prioritize sources** (amplitude × frequency × coupling efficiency)
**Step 7: Design mitigation** (source suppression → path interruption → victim hardening)

**Key Takeaway:** PWM motor drives and high-power arc sources (plasma, EDM) generate dominant EMI in CNC systems. These sources must be addressed with ground plane methodology, shielded cables, and common-mode chokes—filtering alone is insufficient for emissions at 10-100× times signal levels.

Next section (13.3) covers shielding and cable design for interrupting coupling paths from these sources to sensitive circuits.

***

*Section 13.2 Total: 3,612 words | 12 equations | 4 worked examples | 3 tables*

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
