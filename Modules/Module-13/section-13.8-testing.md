## 8. EMC Testing and Measurement

### 8.1 Introduction: Pre-Compliance Testing Strategy

EMC compliance testing at accredited laboratories costs $10,000-30,000 per iteration (conducted emissions, radiated emissions, immunity testing). **Failing first test requires design modifications and complete retest**—doubling or tripling certification costs and delaying product launch by 2-6 months. Pre-compliance testing using affordable bench equipment ($1,000-10,000) identifies problems early, enabling fixes before expensive lab testing.

**Testing hierarchy:**
1. **Design-phase prediction:** Calculate expected emissions using equations (Sections 13.2, 13.3)
2. **Benchtop pre-compliance:** Spectrum analyzer, near-field probes, current probes ($1,000-10,000 equipment)
3. **Pre-compliance lab:** Test house with full equipment but relaxed procedures ($2,000-5,000)
4. **Full compliance testing:** Accredited lab (NVLAP, A2LA) with report for regulatory submission ($10,000-30,000)

This section covers benchtop pre-compliance testing—affordable, iterative testing during development.

### 8.2 Required Test Equipment

**8.2.1 Spectrum Analyzer**

Measures frequency-domain emissions (amplitude vs. frequency):

**Minimum specifications:**
- Frequency range: 9 kHz - 1 GHz (covers conducted 150 kHz - 30 MHz and radiated 30 MHz - 1 GHz)
- Resolution bandwidth (RBW): 9 kHz, 120 kHz (per CISPR 16-1-1)
- Detector modes: Peak, quasi-peak, average
- Display: Waterfall or spectrogram (tracks intermittent emissions)

**Equipment options:**

| Equipment | Frequency Range | RBW | Price | Application |
|-----------|----------------|-----|-------|-------------|
| **TinySA Ultra** | 100 kHz - 6 GHz | 10 kHz - 850 kHz | $130 | Budget pre-compliance |
| **Siglent SSA3021X** | 9 kHz - 2.1 GHz | 10 Hz - 1 MHz | $1,500 | Excellent pre-compliance |
| **Rigol DSA815-TG** | 9 kHz - 1.5 GHz | 10 Hz - 1 MHz | $2,000 | Tracking generator included |
| **Keysight N9320B** | 9 kHz - 3 GHz | 1 Hz - 3 MHz | $6,000 | Professional pre-compliance |

**Recommendation:** Siglent SSA3021X ($1,500) provides best value—covers required frequency range, CISPR-compliant RBW, peak detector.

**8.2.2 Near-Field Probes**

Locate emission sources on PCBs and cables:

**H-field probe** (magnetic, loop antenna):
- Detects current flow (motor cables, PWM output traces, power supply inductors)
- Construction: 10-30mm diameter wire loop
- Response: Proportional to dI/dt (sensitive to high-frequency transients)

**E-field probe** (electric, monopole antenna):
- Detects voltage (high-impedance nodes, capacitors, MOSFETs)
- Construction: 10-50mm monopole rod
- Response: Proportional to dV/dt

**Commercial sets:**
- Beehive Electronics 100 series ($400-800): H and E field probes, 10 MHz - 3 GHz
- Tekbox TBPS01 ($200): Budget H-field and E-field set
- DIY option ($20): 10mm wire loop + 20mm monopole, SMA connector

**8.2.3 Current Probe**

Measures common-mode current on cables (non-invasive clamp):

**Specifications:**
- Frequency range: 10 kHz - 100 MHz
- Transfer impedance: 1-10 Ω (converts current to voltage for spectrum analyzer)
- Clamp diameter: 10-50mm (must fit around cable)

**Example:** Fischer Custom Communications F-33-1 ($800)
- Frequency: 10 kHz - 230 MHz
- Transfer impedance: 5Ω @ 10 MHz
- Clamp: 13mm diameter

**Interpretation:** Spectrum analyzer reading 60 dBμV at 16 kHz:
- Voltage: 10^((60-120)/20) = 0.001V = 1 mV
- Current: 1 mV / 5Ω = **0.2 mA common-mode current**

**8.2.4 Line Impedance Stabilization Network (LISN)**

Measures conducted emissions on AC power lines:

**Function:**
- Provides defined 50Ω impedance for equipment under test (EUT)
- Blocks external noise from AC mains (isolates DUT emissions from grid)
- Couples emissions to spectrum analyzer

**Specifications:**
- Frequency range: 150 kHz - 30 MHz (per CISPR 16-1-2)
- Impedance: 50Ω || 5 μH + 1 μF (standard LISN network)
- Current rating: 10-16A typical

**Cost:** $500-2,000 (Tekbox TBLC08, $600; Com-Power LI-125A, $1,200)

### 8.3 Conducted Emissions Testing

**8.3.1 Test Setup**

```
AC Mains ----[LISN]----[Equipment Under Test]
               |
               | (50Ω RF output)
               |
          [Spectrum Analyzer]
```

**Procedure:**
1. Connect EUT AC input to LISN output
2. Connect LISN 50Ω port to spectrum analyzer via coaxial cable
3. Set spectrum analyzer:
   - Frequency span: 150 kHz - 30 MHz
   - RBW: 9 kHz (CISPR 16-1-1)
   - Detector: Peak (pre-compliance) or Quasi-Peak (compliance)
   - Sweep time: 50-100 seconds (slow sweep for QP detector)
4. Operate EUT at maximum load (motors running, full power)
5. Capture spectrum, compare to limits

**8.3.2 CISPR 11 Class A Limits (Industrial Equipment)**

| Frequency Range | Quasi-Peak Limit (dBμV) | Average Limit (dBμV) |
|-----------------|------------------------|----------------------|
| 150 kHz - 500 kHz | 79 | 66 |
| 500 kHz - 5 MHz | 73 | 60 |
| 5 MHz - 30 MHz | 73 | 60 |

**FCC Part 15 Class A Limits (similar to CISPR 11):**
- 0.15 - 0.5 MHz: 79 dBμV quasi-peak
- 0.5 - 30 MHz: 73 dBμV quasi-peak

**Example measurement:**
- 16 kHz PWM fundamental: Measured 68 dBμV (pk), Limit 79 dBμV → **Pass** (11 dB margin)
- 1 MHz PWM harmonic: Measured 76 dBμV (pk), Limit 73 dBμV → **Fail** (3 dB over)

**Corrective action:** Add common-mode choke on motor cable (20-30 dB reduction expected) → retest → 76 - 25 = 51 dBμV → Pass with 22 dB margin.

### 8.4 Radiated Emissions Testing (Pre-Compliance)

**8.4.1 Test Setup (Simplified)**

Full compliance requires anechoic chamber or open-area test site (OATS). Pre-compliance uses simplified setup:

```
[Equipment Under Test] <-- 1-3m --> [Broadband Antenna] --> [Spectrum Analyzer]
```

**Antenna options:**
- 30 MHz - 200 MHz: Biconical antenna or log-periodic dipole array (LPDA)
- 200 MHz - 1 GHz: LPDA or horn antenna
- Budget: DIY dipole antennas at spot frequencies (150 MHz, 450 MHz, 900 MHz)

**Procedure:**
1. Position EUT on non-conductive table (wood or plastic, height 0.8m)
2. Place antenna 1m from EUT (3m for full compliance, 1m for pre-compliance sensitivity)
3. Set spectrum analyzer:
   - Frequency span: 30 MHz - 1 GHz
   - RBW: 120 kHz (CISPR 16-1-1)
   - Detector: Peak
4. Sweep antenna height 1-4m (finds maximum emission)
5. Rotate EUT 0-360° (finds worst-case orientation)
6. Capture peak spectrum, compare to limits

**8.4.2 CISPR 11 Class A Radiated Limits (@ 10m distance)**

| Frequency Range | Quasi-Peak Limit (dBμV/m) |
|-----------------|---------------------------|
| 30 MHz - 230 MHz | 40 |
| 230 MHz - 1 GHz | 47 |

**Distance correction factor:**

Measurements at 1m or 3m must be corrected to 10m equivalent:

$$E_{10m} = E_{measured} - 20\log_{10}\left(\frac{10}{d_{measured}}\right)$$

For measurement at 1m:
- E₁₀m = E₁m - 20 log₁₀(10/1) = E₁m - 20 dB

**Example:** Measured 65 dBμV/m @ 1m, 150 MHz
- E₁₀m = 65 - 20 = 45 dBμV/m
- Limit: 40 dBμV/m
- **Fail (5 dB over)** → Add ferrite beads to cables or improve enclosure shielding

### 8.5 Near-Field Probe Troubleshooting

**8.5.1 Emission Source Localization**

**Procedure:**
1. Connect near-field probe to spectrum analyzer
2. Set analyzer to frequency of interest (e.g., 16 kHz PWM fundamental or harmonic)
3. Sweep probe over PCB surface, cables, and enclosure seams
4. Identify location of maximum amplitude (emission source)

**Example: Locating PWM drive emission**

System fails radiated emissions at 48 kHz (3rd harmonic of 16 kHz PWM):
- Sweep H-field probe over servo drive PCB
- Peak amplitude at MOSFET drain node (high dI/dt during switching)
- Peak amplitude at motor output connector (unfiltered cable)

**Corrective actions:**
- Add snubber across MOSFET drain-source (RC: 10Ω + 1nF, reduces dV/dt)
- Install common-mode choke on motor cable at connector (10 mH, blocks 48 kHz)

**8.5.2 Shielding Effectiveness Verification**

Use near-field probe to verify enclosure shielding:

**Procedure:**
1. Place probe inside enclosure near emission source (e.g., 10mm from PWM drive)
2. Measure amplitude at frequency of concern (e.g., 100 MHz)
3. Close enclosure, install gaskets and panels
4. Repeat measurement with probe outside enclosure (same distance from source)
5. Calculate SE: SE = Inside level (dBμV) - Outside level (dBμV)

**Example:**
- Inside: 80 dBμV @ 100 MHz
- Outside (closed enclosure): 20 dBμV @ 100 MHz
- **SE = 80 - 20 = 60 dB** ✓ (meets target)

**If SE <40 dB:**
- Check gasket compression (insufficient contact resistance)
- Check apertures >15mm (ventilation, display cutout)
- Check cable shield bonding (pigtail termination creates leakage)

### 8.6 Current Probe Cable Emissions Measurement

**8.6.1 Common-Mode Current Measurement**

Clamp current probe around cable (all conductors together):

**Procedure:**
1. Clamp probe around motor cable 200mm from drive (standard measurement point)
2. Connect probe to spectrum analyzer
3. Measure current spectrum (probe transfer impedance converts current → voltage)
4. Compare to limits or baseline

**Typical common-mode currents:**
- PWM motor cable (unfiltered): 100-500 mA @ 16 kHz, 10-50 mA @ 1 MHz
- PWM motor cable (with CMC): 10-50 mA @ 16 kHz, 1-5 mA @ 1 MHz (10× reduction)
- Ethernet cable (shielded, proper grounding): <1 mA @ 100 MHz

**8.6.2 Cable Resonance Detection**

Long cables (>3m) resonate at frequencies where length = λ/2:

$$f_{resonance} = \frac{c}{2 L \sqrt{\epsilon_r}}$$

For 5m motor cable (εr ≈ 2 for cable insulation):
- f = 3×10⁸ / (2 × 5 × √2) = **21 MHz**

Expect peak common-mode current at 21 MHz (cable acts as half-wave dipole antenna).

**Mitigation:** Install ferrite bead clamp at resonant frequency (fair-rite material 43 for 10-100 MHz).

### 8.7 Immunity Testing (Advanced Pre-Compliance)

**8.7.1 ESD Testing**

Electrostatic discharge (IEC 61000-4-2) tests equipment response to 2-15 kV ESD strikes:

**Simplified ESD test:**
- Use commercial ESD gun (Keytek, Noiseken: $2,000-5,000) or piezo lighter (±10 kV, $5)
- Strike exposed metal surfaces (connectors, enclosure)
- Test levels: ±2 kV contact, ±4 kV air discharge (IEC 61000-4-2 Level 2)
- Acceptance: No resets, errors, or damage

**Common ESD failures:**
- Controller resets: Poor ground plane impedance (transient couples to power supply)
- Encoder position loss: ESD couples into unshielded encoder cable
- USB disconnection: ESD strike to enclosure couples to USB ground

**Mitigation:**
- Ground plane with <10 mΩ impedance (Section 13.5)
- TVS diodes on all I/O (PESD5V0L1BA, $0.20 each)
- 360° shield bonding on all cables

**8.7.2 Conducted Immunity Testing (Burst, Surge)**

Electrical fast transient (EFT/burst, IEC 61000-4-4) and surge (IEC 61000-4-5) test power line immunity:

**Simplified test:**
- Use EFT/burst generator (Noiseken INS-5020, $8,000-15,000) or
- DIY: Relay switching inductive load (simulates <1 kV transients)

**Test levels:**
- EFT/burst: 2 kV, 5 kHz repetition rate (Level 3 for industrial)
- Surge: 1-2 kV line-line, 2-4 kV line-ground (Level 3)

**Mitigation:**
- MOV (metal oxide varistor) on AC input (275V RMS for 240VAC, Littelfuse V275LA4P)
- EMI filter with X and Y capacitors (Section 13.4.4)

### 8.8 Measurement Uncertainty and Margin

Pre-compliance measurements have ±3-6 dB uncertainty:
- Antenna calibration: ±2 dB
- Cable loss: ±1 dB
- Spectrum analyzer accuracy: ±1 dB
- Ambient noise floor: ±1-3 dB (depends on environment)

**Design margin guideline:** Target 6-10 dB below limit during pre-compliance
- Pre-compliance: Measured 63 dBμV, Limit 73 dBμV → 10 dB margin → Good
- Compliance lab: Expect 63 ±3 dB = 60-66 dBμV → Still passes with 7+ dB margin

**If margin <6 dB during pre-compliance, risk failing compliance test.**

### 8.9 Pre-Compliance Test Report Template

Document all testing for design review and compliance lab preparation:

**Report sections:**
1. **Equipment Under Test (EUT) description:** Model, serial, configuration
2. **Test setup:** Photos, equipment list, calibration dates
3. **Test conditions:** AC input voltage, load conditions, ambient temperature
4. **Conducted emissions:** Spectrum plots with limit lines, worst-case frequencies
5. **Radiated emissions:** Spectrum plots, antenna orientation, EUT rotation
6. **Immunity:** ESD test points, pass/fail criteria, observed behavior
7. **Conclusions:** Pass/fail vs. limits, margin analysis, recommended improvements

**Example conclusion:**
- Conducted emissions: Pass, 8 dB margin at worst-case frequency (1 MHz)
- Radiated emissions: Fail, 5 dB over limit at 48 kHz (3rd PWM harmonic)
- **Recommendation:** Add common-mode choke on motor cable, retest

### 8.10 Summary: Pre-Compliance Testing Strategy

**Testing phases:**

**Phase 1: Benchtop (weekly during development)**
- Spectrum analyzer + near-field probes ($2,000 equipment)
- Identify emission sources, verify shielding and filtering
- Cost: $0 (internal), Time: 1-2 hours
- **Goal:** Catch problems early, iterate quickly

**Phase 2: Pre-compliance lab (before final design)**
- Test house with full compliance setup but relaxed procedures
- Conducted + radiated emissions scan (no full report)
- Cost: $2,000-5,000, Time: 4-8 hours
- **Goal:** Predict compliance lab results, identify remaining issues

**Phase 3: Full compliance (final product)**
- Accredited lab (NVLAP, A2LA, TÜV, UL)
- Conducted emissions, radiated emissions, immunity (full test plan)
- Cost: $10,000-30,000, Time: 2-5 days + 2-4 week report
- **Goal:** Certification for regulatory submission (FCC, CE marking)

**ROI of pre-compliance testing:**
- Pre-compliance equipment: $1,000-10,000
- Benchtop testing time: 20-40 hours over development (1 engineer @ $50/hr = $1,000-2,000 labor)
- **Total pre-compliance cost: $2,000-12,000**

**Cost of skipping pre-compliance:**
- Compliance test failure (50% probability without pre-compliance testing)
- Redesign cost: $20,000-100,000 (engineering, PCB respins, enclosure mods)
- Retest cost: $10,000-30,000 (second compliance lab visit)
- Schedule delay: 2-6 months (market launch delayed, lost revenue)
- **Total failure cost: $30,000-130,000+**

**Pre-compliance testing ROI: 5-20× return**

***

*Section 13.8 Total: 2,712 words | 3 equations | 5 worked examples | 3 tables*

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
