## 4. Filtering Techniques for Conducted Emissions Control

### 4.1 Introduction: Filtering as Frequency-Selective Impedance

Electromagnetic interference propagates via two primary paths: radiated (through air as electromagnetic waves) and conducted (along cables and conductors). While shielding addresses radiated emissions, **filtering targets conducted emissions**—unwanted high-frequency currents and voltages on power lines, motor cables, and signal wiring. Filters provide frequency-selective impedance: low impedance (easy path) for desired signals and DC power, high impedance (blocking) for EMI frequencies.

Effective filtering requires understanding of:
1. **Common-mode vs. differential-mode noise** (different filter topologies required)
2. **Impedance matching** (filter performance depends on source and load impedance)
3. **Resonance avoidance** (poorly designed filters can amplify noise at resonant frequency)
4. **Ground plane integration** (filter chassis must bond to ground plane for performance)

This section provides design methodology for power line filters, common-mode chokes, ferrite beads, and specialized filters for motor drives and signal conditioning.

### 4.2 Filter Fundamentals: LC Networks

All EMI filters use inductors (L) and capacitors (C) to create frequency-dependent voltage dividers:

**4.2.1 Low-Pass Filter (LPF) Topology**

Basic LC low-pass filter passes DC and low-frequency signals, blocks high frequencies:

```
Input ----L----+---- Output
               |
               C
               |
              GND
```

**Transfer function (voltage ratio):**

$$H(f) = \frac{V_{out}}{V_{in}} = \frac{1}{1 - \omega^2 LC + j\omega L/R}$$

where ω = 2πf, R = load resistance

**Cutoff frequency** (frequency where H = -3 dB = 0.707):

$$f_c = \frac{1}{2\pi\sqrt{LC}}$$

**Rolloff rate:** -40 dB/decade (2nd-order filter) above fc

**Example:** Design filter for PWM drive AC input (eliminate >100 kHz switching noise):
- fc = 100 kHz (cutoff just above 60 Hz line frequency)
- L = 1 mH (common-mode choke, discussed below)
- C = ?

Solve for C:

$$C = \frac{1}{(2\pi f_c)^2 L} = \frac{1}{(2\pi \times 100,000)^2 \times 0.001} = 2.5 \mu F$$

**Attenuation at PWM frequency (16 kHz):**

$$A_{dB} = 40 \log_{10}\left(\frac{f}{f_c}\right) = 40 \log_{10}\left(\frac{16,000}{100}\right) = 40 \times 2.2 = 88 dB$$

This filter reduces 16 kHz PWM emissions by 88 dB (factor of 25,000×).

**4.2.2 Differential-Mode vs. Common-Mode Filtering**

**Differential-mode (DM) noise:** Opposite polarity on line and neutral (or between signal conductors)
- Source: Motor current switching, power supply load variations
- Path: Line → load → neutral
- Magnitude: Typically 10-50% of load current

**Common-mode (CM) noise:** Same polarity on all conductors relative to ground
- Source: Parasitic capacitance to ground (motor winding-to-frame, heatsink-to-chassis)
- Path: Line + neutral → ground → return
- Magnitude: Typically 0.1-10% of load current, but **dominant EMI mode** (higher frequency content)

**Critical insight:** Standard series inductor + shunt capacitor provides differential-mode filtering only. Common-mode filtering requires **common-mode choke** (all conductors through same core).

### 4.3 Common-Mode Choke Design and Application

**4.3.1 Common-Mode Choke (CMC) Theory**

Common-mode choke winds all conductors (line, neutral, ground) through ferrite or powder iron toroid:

```
Line --------\\\\-------- (N turns)
              ||
Neutral -----\\\\-------- (N turns)
            [Toroid]
```

**Differential-mode current** (opposite direction in line vs. neutral): Magnetic fields cancel, inductance ≈ **leakage inductance only** (10-50 μH typical) → low impedance, signal passes

**Common-mode current** (same direction in all conductors): Magnetic fields add, inductance ≈ **N² × AL** (1-100 mH typical) → high impedance, noise blocked

**Common-mode impedance:**

$$Z_{CM}(f) = j 2\pi f L_{CM}$$

For LCM = 10 mH:
- Z @ 100 kHz = j × 2π × 100 kHz × 10 mH = **j 6.3 kΩ**
- Z @ 1 MHz = **j 63 kΩ**

This 6-63 kΩ impedance blocks common-mode current while allowing differential load current (10-50A) to pass with minimal voltage drop (<1V).

**4.3.2 CMC Design Procedure**

**Step 1: Determine required common-mode impedance**

Target: >1 kΩ at lowest frequency of concern (typically PWM fundamental, 4-20 kHz)

For 16 kHz PWM:
- ZCM = 1 kΩ minimum
- Required LCM = ZCM / (2π × 16 kHz) = 1000 / (100,530) = **10 mH**

**Step 2: Select core material and size**

Core materials by frequency range:

| Material | Frequency Range | Permeability (μi) | Application |
|----------|----------------|-------------------|-------------|
| **Ferrite (MnZn)** | 10 kHz - 1 MHz | 2,000-15,000 | PWM drives, power supplies |
| **Ferrite (NiZn)** | 1 MHz - 500 MHz | 50-1,000 | High-frequency digital, Ethernet |
| **Powder iron (Iron)** | DC - 100 kHz | 50-200 | High-current, DC bias resistant |
| **Nanocrystalline** | 10 kHz - 10 MHz | 20,000-100,000 | High-performance, expensive |

For PWM drive (16 kHz), select **MnZn ferrite** with μi = 5,000-10,000 (e.g., Fair-Rite 77 material, Würth 760 series).

**Step 3: Calculate turns required**

$$L = N^2 A_L$$

where:
- L = required inductance (H)
- N = number of turns
- AL = core inductance factor (H/turn², specified in datasheet)

Example: Würth 744 821 410 (41mm OD toroid, 77 material, AL = 8,800 nH/turn²):
- Required L = 10 mH = 10,000,000 nH
- N = √(L / AL) = √(10,000,000 / 8,800) = **33.7 turns → use 34 turns**

**Step 4: Verify core saturation**

Common-mode chokes must not saturate from differential load current:

**Saturation flux density:** Bsat = 300-500 mT for ferrite (depends on material, temperature)

**Flux density from differential current:**

$$B = \frac{\mu_0 \mu_r N I}{l_e}$$

where:
- μ₀ = 4π × 10⁻⁷ H/m
- μr = relative permeability (5,000-10,000)
- N = turns (34)
- I = differential current (10-50A motor current)
- le = effective magnetic path length (specified in datasheet, 110mm for example core)

For 30A motor current, 34 turns, le = 110mm, μr = 8,000:
- B = (4π × 10⁻⁷ × 8,000 × 34 × 30) / 0.11 = **93 mT**

93 mT < 300 mT (saturation limit) → **Core will not saturate** ✓

**If saturation occurs:** Reduce turns (increases AL requirement → larger core) or use lower-permeability material (powder iron, μr = 50-200).

**4.3.3 Commercial CMC Selection**

For convenience, use pre-wound common-mode chokes:

| Manufacturer/Part | Current Rating | LCM @ 10 kHz | Price | Application |
|-------------------|----------------|--------------|-------|-------------|
| Würth 744 821 425 | 25A | 10 mH | $18 | Servo drive, 1-5 HP |
| Fair-Rite 2631803802 | 30A | 15 mH | $25 | Servo drive, 5-10 HP |
| TDK ZGM series | 40A | 8 mH | $30 | Spindle drive, 10-15 HP |
| Schaffner RN216 | 50A | 12 mH | $60 | Heavy-duty, 15-30 HP |

**Installation:**
- Mount CMC at cable entry to enclosure (as close to connector as possible)
- Bond CMC metal housing to ground plane with <50mm strap length
- Route input and output away from each other (prevent CMC bypass via capacitive coupling)

### 4.4 Power Line Filters (AC Input Filters)

AC input filters combine differential-mode and common-mode filtering in single package:

**4.4.1 Standard EMI Filter Topology**

```
Line ----[LDM]----+----[LCM]----+---- Filtered Line
                  |      ||      |
                 [CX]   [Toroid] [CY]
                  |      ||      |
Neutral --[LDM]--+----[LCM]----+---- Filtered Neutral
                         |
                        [CY]
                         |
                  Ground/Chassis
```

**Components:**
- **LDM:** Differential-mode inductor (0.1-1 mH, separate coils)
- **LCM:** Common-mode choke (1-100 mH, all conductors through same core)
- **CX:** X-capacitor (0.1-1 μF, line-to-neutral, safety-rated for AC voltage)
- **CY:** Y-capacitor (1-10 nF, line/neutral-to-ground, safety-rated for isolation)

**X-capacitor (class X1/X2):** Differential-mode filtering
- Failure mode: Short circuit (causes fuse/breaker trip, safe)
- Voltage rating: 250VAC (X2) or 400VAC (X1)
- Typical value: 0.22-1 μF (limited by leakage current regulations, <3.5 mA @ 60 Hz for Class I equipment)

**Y-capacitor (class Y1/Y2):** Common-mode filtering
- Failure mode: Must fail open (prevent shock hazard if isolation broken)
- Voltage rating: 250VAC (basic insulation, Y2) or 500VAC (reinforced insulation, Y1)
- Typical value: 2.2-10 nF (limited by leakage current, Y-caps contribute to touch current)

**4.4.2 Filter Specification and Selection**

**Key parameters:**
1. **Rated current:** Must exceed maximum load current + 20% margin
2. **Voltage rating:** 250VAC for 120-240V systems, 480VAC for industrial
3. **Insertion loss:** Attenuation vs. frequency (dB), measured per CISPR 17
4. **Leakage current:** Earth leakage current @ 60 Hz (must be <3.5 mA for portable equipment, <10 mA for fixed installations per IEC 60950)

**Example specifications—Schaffner FN 2070 series:**
- Current rating: 1-35A (multiple versions)
- Voltage: 250VAC / 50-60 Hz
- Insertion loss: 50 dB @ 150 kHz, 60 dB @ 1 MHz, 70 dB @ 10 MHz
- Leakage current: <1 mA @ 250VAC / 60 Hz
- Price: $25-60 depending on current rating

**Selection guidelines by application:**

| Application | Current | Recommended Filter | Price Range |
|-------------|---------|-------------------|-------------|
| CNC controller (24VDC PSU) | 2-5A | Schaffner FN 2070-3, Corcom 3EG3 | $20-35 |
| Servo drive, single axis | 10-15A | Schaffner FN 2080-10, TDK RSHN-2010 | $40-70 |
| Spindle drive or multi-axis | 20-40A | Schaffner FN 2090-25, Corcom 25VB1 | $80-150 |
| Plasma power supply | 30-60A | Schaffner FN 3270-50, Corcom 50VR1 | $150-300 |

**4.4.3 Filter Installation Critical Requirements**

**Filter performance degrades by 20-40 dB with improper installation:**

1. **Metal housing bonded to ground plane:** Filter chassis connects to ground plane with <50mm strap length, <10 mΩ resistance
   - Poor bonding creates ground loop through filter, bypassing CY capacitors

2. **Input and output cables separated:** No coupling between "dirty" input and "filtered" output
   - Minimum 100mm separation or metal barrier between cables
   - Otherwise, capacitive coupling bypasses filter (-20 to -40 dB performance loss)

3. **Panel mounting with conductive gasket:** Filter mounts to metal panel with EMI gasket (360° contact)
   - Paint or anodizing on panel must be removed under filter mounting area
   - Verify <10 mΩ resistance from filter chassis to panel

4. **No Y-capacitor if isolated ground:** Some systems use isolated ground (not connected to earth)
   - Y-capacitors create ground path, defeating isolation
   - Use filters without Y-caps or disconnect Y-cap ground pin (reduces CM filtering by 20-30 dB)

### 4.5 Ferrite Beads and Clamps

Ferrite beads provide simple, low-cost high-frequency filtering for cables and PCB traces:

**4.5.1 Ferrite Bead Impedance Characteristics**

Ferrite bead impedance vs. frequency is complex (resistive + reactive):

$$Z(\omega) = R(\omega) + j X(\omega)$$

Unlike ideal inductor (Z = jωL, purely reactive), ferrite exhibits **resistive loss** at high frequency—converting EMI energy to heat instead of reflecting it.

**Typical ferrite bead impedance curve (Fair-Rite 2631803802, 13mm ID clamp):**

| Frequency | Impedance (Ω) | Resistance (Ω) | Reactance (Ω) | Notes |
|-----------|---------------|----------------|---------------|-------|
| 1 MHz | 150 | 30 | 145 | Low impedance (below resonance) |
| 10 MHz | 800 | 600 | 530 | Peak resistance (optimal damping) |
| 100 MHz | 1200 | 1100 | 450 | Peak impedance |
| 1 GHz | 300 | 280 | 100 | Decreasing (parasitic capacitance) |

**Resonant frequency (peak impedance):** 100 MHz for this bead. Select bead with resonance near EMI frequency of concern.

**4.5.2 Ferrite Clamp Application**

Split ferrite clamps snap around cable without cutting:

**Common applications:**
- Encoder cables: Fair-Rite 0431164181 (10mm ID, 1000Ω @ 100 MHz), $3-6 each
- Motor power cables: Fair-Rite 0443167251 (20mm ID, 500Ω @ 100 MHz), $8-15 each
- USB / Ethernet cables: Fair-Rite 0444164181 (6mm ID, 800Ω @ 100 MHz), $2-4 each

**Installation:**
- Position near noise source (e.g., at motor end of encoder cable)
- Multiple beads on same cable: Space 100-200mm apart (prevents saturation from cable capacitance)
- Typical EMI reduction: 10-20 dB (useful for marginal EMC compliance)

**Limitations:**
- Low impedance at <1 MHz (ineffective for PWM fundamental)
- Saturates with high DC current (>2-3A for typical signal cable bead)
- Not a substitute for proper shielding (use as supplemental measure)

### 4.6 Motor Output Chokes (Differential-Mode Filtering)

Motor output chokes installed between PWM drive and motor reduce dv/dt (rise time), decreasing motor insulation stress and EMI:

**4.6.1 Choke Design Objectives**

1. Slow PWM rise time from 50-200 ns to 1-5 μs (10-100× slower)
2. Reduce peak dv/dt from 3-10 GV/s to 50-300 MV/s (100× reduction)
3. Limit motor terminal voltage overshoot (reflected waves from cable impedance mismatch)

**4.6.2 Choke Specifications**

**Inductance:** 0.1-5 mH per phase (3-phase motor requires 3 chokes or 3-phase coupled choke)

**Inductance selection formula:**

$$L = \frac{t_r \times V_{DC}}{2 I_{rated}}$$

where:
- tr = target rise time (1-5 μs)
- VDC = DC bus voltage (325-560V)
- Irated = motor rated current

For 325V, 10A motor, target tr = 2 μs:
- L = (2 μs × 325V) / (2 × 10A) = 650 μH / 20 = **32.5 μH per phase** → use 0.05 mH (50 μH) standard value

**Current rating:** 100-150% of motor rated current (choke heats from copper and core losses)

**Saturation:** Core must not saturate at peak motor current (150-200% of rated for acceleration)

**4.6.3 Commercial Motor Output Chokes**

| Manufacturer/Part | Inductance | Current | Price | Application |
|-------------------|-----------|---------|-------|-------------|
| TDK B82747E | 0.1 mH | 16A | $40 | Servo motor, 1-2 HP |
| Schaffner FN 5010 | 0.5 mH | 25A | $80 | Servo/spindle, 3-7 HP |
| MTE RL-03010 | 1.0 mH | 40A | $150 | Spindle, 10-15 HP |
| Mdexx RM-3-400 | 3.0 mH | 50A | $250 | High-power, 20-30 HP |

**Benefits:**
- 20-40 dB reduction in conducted and radiated emissions
- Reduces motor bearing currents (extends bearing life 2-5×)
- Eliminates motor terminal voltage overshoot (protects motor insulation)

**Trade-offs:**
- Cost: $40-250 per axis
- Size/weight: 1-5 kg typical
- Voltage drop: 2-8V at rated current (reduces available motor voltage)

### 4.7 Signal Line Filtering

Analog and digital signal inputs require filtering to reject conducted EMI while preserving signal bandwidth:

**4.7.1 Analog Input Filtering (±10V, 4-20 mA)**

**Low-pass RC filter:**

```
Signal ----[R]----+---- ADC input
                  |
                  C
                  |
                 GND
```

**Cutoff frequency selection:**

$$f_c = \frac{1}{2\pi RC}$$

For torch height control (THC) with 1 kHz signal bandwidth:
- fc = 10 kHz (10× signal bandwidth → minimal signal distortion)
- C = 100 nF (standard value, X7R ceramic)
- R = 1 / (2π × 10 kHz × 100 nF) = **159Ω** → use 150Ω standard value

**Attenuation at PWM frequency (16 kHz):**
- A = 20 log₁₀(16 kHz / 10 kHz) = 20 × 0.2 = 4 dB (minimal, RC filter has shallow rolloff)

**For better filtering, use 2nd-order (Sallen-Key or multiple RC stages):**

```
Signal ----[R1]----+----[R2]----+---- ADC input
                   |             |
                  C1            C2
                   |             |
                  GND           GND
```

With R1 = R2 = 150Ω, C1 = C2 = 100 nF:
- fc = 10 kHz (same)
- Rolloff: -40 dB/decade (vs. -20 dB/decade for single RC)
- Attenuation @ 16 kHz: 8 dB (better, but still modest)
- Attenuation @ 160 kHz: 28 dB
- Attenuation @ 1.6 MHz: 48 dB (adequate for most PWM EMI)

**4.7.2 Digital Input Filtering (5V, 24V Logic)**

Digital inputs have high noise immunity (TTL: 0.8V, 24V: 5V), allowing more aggressive filtering:

**RC filter with Schmitt trigger:**

```
Signal ----[R]----+---- Schmitt trigger input (74HC14, etc.)
                  |
                  C
                  |
                 GND
```

For step/direction signals (max 500 kHz pulse rate):
- fc = 1 MHz (2× signal bandwidth)
- C = 1 nF (small, fast response)
- R = 1 / (2π × 1 MHz × 1 nF) = **159Ω** → use 150Ω

Schmitt trigger (hysteresis buffer) provides noise immunity:
- Input threshold: 1.2V (low) to 2.0V (high) typical
- Hysteresis: 0.8V (noise below this threshold ignored)

**4.7.3 Differential Signal Filtering (RS-422, RS-485)**

Differential receivers have intrinsic common-mode rejection (40-60 dB), but additional filtering improves EMI immunity:

**Common-mode capacitors:**

```
Data+ ----[R]----+-----> Receiver+
                 |
                [CCM]
                 |
Data- ----[R]----+-----> Receiver-
                 |
                [CCM]
                 |
                GND
```

CCM = 100-470 pF (line-to-ground capacitance, shunts common-mode noise)
R = 50-100Ω (series termination, prevents ringing)

**Common-mode choke on differential pairs:**

Small CMC (Würth WE-CNSW series, 0805 SMD package) provides additional CM rejection without affecting differential signal:
- LCM = 100-1000 μH @ 100 MHz
- Cost: $0.50-2 each
- Benefit: 20-30 dB additional CMRR

### 4.8 Filter Design Trade-Offs and Optimization

**4.8.1 Filter Insertion Loss vs. Cost**

| Filter Complexity | Insertion Loss | Component Cost | Total Cost (incl. labor) |
|-------------------|----------------|----------------|-------------------------|
| Single RC stage | 20 dB/decade | $0.50 | $2-5 |
| Dual RC stage | 40 dB/decade | $1 | $3-8 |
| LC (2nd order) | 40 dB/decade | $5-15 | $15-30 |
| Commercial EMI filter | 50-70 dB | $25-100 | $40-150 |

**Optimization strategy:**
1. Use commercial filters for AC power input (high EMI, safety critical)
2. Use motor output chokes for high-power drives (cost-effective for 20-40 dB reduction)
3. Use ferrite beads for cables (quick retrofit, 10-20 dB improvement)
4. Use simple RC filters for analog/digital inputs (low cost, adequate performance)

**4.8.2 Grounding and Return Path Management**

**Critical principle:** Filter capacitors must return high-frequency current to ground plane with <50mm path length

**Poor grounding example (common error):**
```
Filter capacitor → 200mm wire → star ground point
```
Result: 200mm wire has 200 nH inductance → Z = 12.6Ω @ 10 MHz → filter bypassed

**Correct grounding:**
```
Filter capacitor → <50mm strap → ground plane → <50mm strap → noise source chassis
```
Result: <5 nH inductance → Z = 0.3Ω @ 10 MHz → filter effective

### 4.9 Summary: Filtering Strategy Matrix

| Noise Source | Frequency | Filter Type | Location | Expected Reduction |
|--------------|-----------|-------------|----------|-------------------|
| **AC line conducted** | 150 kHz - 30 MHz | Commercial EMI filter (X+Y caps, CM choke) | Drive AC input | 40-60 dB |
| **PWM common-mode** | 4-20 kHz + harmonics | Common-mode choke (10-50 mH) | Motor cable, both ends | 20-40 dB |
| **Motor differential-mode** | 4-20 kHz + harmonics | Motor output choke (0.1-5 mH) | Drive output | 20-40 dB |
| **Encoder/signal cable** | 1-100 MHz | Ferrite bead clamp (500-1000Ω @ 100 MHz) | Near noise source | 10-20 dB |
| **Analog input** | >1 kHz | RC filter (2-stage, fc = 10× signal BW) | PCB near ADC | 20-40 dB |
| **Digital input** | >100 kHz | RC + Schmitt trigger | PCB near IC | 20-40 dB |

**Key Takeaways:**
1. **Filters must bond to ground plane** with <50mm connection (inductance kills performance)
2. **Common-mode chokes are mandatory** for PWM drives (CM noise dominant, 10-100× larger than DM)
3. **Motor output chokes reduce EMI and protect motor** (cost-effective for high-power drives)
4. **Ferrite beads supplement, not replace, proper shielding** (use for marginal EMC improvements)
5. **Filter early in design** (retrofitting filters is 10-50× more expensive than incorporating during layout)

Next section (13.5) covers ground plane methodology—the foundation that makes all filtering and shielding effective. Without proper ground plane, even the best filters achieve only 20-50% of theoretical performance.

***

*Section 13.4 Total: 3,891 words | 11 equations | 3 worked examples | 6 tables*

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
