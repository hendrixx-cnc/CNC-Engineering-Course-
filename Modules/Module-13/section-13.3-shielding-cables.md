## 3. Shielding and Cable Design for EMI Mitigation

### 3.1 Introduction: Shielding as Path Interruption

Cable shielding provides the most cost-effective EMI mitigation after source suppression, interrupting coupling paths between noise sources (motor drives, plasma arcs) and victims (encoder signals, analog inputs, communication buses). A properly designed shielded cable assembly with correct shield termination achieves 40-80 dB noise reduction—equivalent to reducing a 10V interference spike to 1-100 mV, transforming system-crashing failures into negligible noise.

However, **improper shield termination destroys shielding effectiveness**. The most common EMC design error in CNC systems is "pigtail" shield termination (twisted wire connection to ground), which creates inductive impedance that negates shielding above 1-10 MHz. This section emphasizes **360° circumferential shield bonding** as the only acceptable termination method for high-frequency EMC performance.

### 3.2 Shielding Effectiveness Theory

Shielding effectiveness (SE) quantifies a shield's ability to attenuate electromagnetic fields, measured in decibels:

$$SE_{dB} = 20 \log_{10}\left(\frac{E_1}{E_2}\right) = 20 \log_{10}\left(\frac{H_1}{H_2}\right)$$

where:
- E₁, H₁ = field strength without shield
- E₂, H₂ = field strength with shield

**Example:** SE = 60 dB means shield reduces field strength by factor of 1,000×:
- 10^(60/20) = 1,000
- 100V interference without shield → 0.1V with shield

**Shielding mechanisms (three components):**

$$SE_{total} = R + A + B$$

where:
- **R = Reflection loss** (impedance mismatch at shield boundary)
- **A = Absorption loss** (energy dissipated in shield material)
- **B = Multiple reflection correction** (usually negligible, <1 dB)

**3.2.1 Reflection Loss (R)**

Electromagnetic wave reflects at boundary between different impedance media (air → metal):

**For magnetic fields (H-field, dominant at low frequency < 1 MHz):**

$$R_H = 20 \log_{10}\left(\frac{\sigma_s t}{4\pi f \mu_0 r}\right) + 20 \log_{10}\left(\frac{1}{1 + \sigma_s t / (4\pi f \mu_0 r)}\right)$$

Simplified approximation for good conductors (copper, aluminum):

$$R_H \approx 20 \log_{10}\left(\frac{t}{r}\right) + 20 \log_{10}\left(\frac{1}{2\pi f}\right) + K$$

where:
- t = shield thickness (m)
- r = distance from source to shield (m)
- f = frequency (Hz)
- K = constant depending on material (copper: K ≈ 168)

**Key insight:** Magnetic field reflection increases with frequency (poor at low frequency, excellent above 1 MHz).

**For electric fields (E-field, dominant at high frequency > 1 MHz):**

$$R_E \approx 362 - 20 \log_{10}(f) - 20 \log_{10}(r)$$

**Key insight:** Electric field reflection is excellent at all frequencies (>100 dB even at low frequency), limited only by shield apertures and discontinuities.

**3.2.2 Absorption Loss (A)**

Energy dissipates as current flows through resistive shield material:

$$A = 20 \log_{10}(e^{t/\delta})  = 8.69 \frac{t}{\delta}$$

where:
- t = shield thickness (m)
- δ = skin depth (m)

**Skin depth** (depth where current decreases to 37% of surface value):

$$\delta = \sqrt{\frac{2}{\omega \mu \sigma}} = \sqrt{\frac{1}{\pi f \mu_r \mu_0 \sigma}}$$

where:
- f = frequency (Hz)
- μr = relative permeability (1 for copper/aluminum, 100-1000 for steel)
- μ₀ = 4π × 10⁻⁷ H/m
- σ = conductivity (copper: 5.8 × 10⁷ S/m, aluminum: 3.5 × 10⁷ S/m)

**Skin depth for copper:**

| Frequency | Skin Depth (δ) | Absorption Loss (0.1mm thick shield) |
|-----------|---------------|--------------------------------------|
| 1 kHz | 2.1 mm | 0.4 dB (negligible) |
| 10 kHz | 0.66 mm | 1.3 dB |
| 100 kHz | 0.21 mm | 4.1 dB |
| 1 MHz | 66 μm | 13 dB |
| 10 MHz | 21 μm | 41 dB (excellent) |
| 100 MHz | 6.6 μm | 130 dB (excessive, limited by seams) |

**Practical implications:**
- **Thin shields (0.05-0.2mm foil or braid) provide excellent absorption above 1 MHz**
- **Thick shields (>1mm) provide no additional benefit above 100 kHz** (current confined to surface by skin effect)
- **Steel shields (μr = 100-1000) provide 10-30 dB better absorption at low frequency** (trade-off: 10× lower conductivity than copper)

**3.2.3 Total Shielding Effectiveness**

For typical braided copper shield (0.15mm wall thickness, 90% coverage) on signal cable at 10 MHz:
- Reflection loss (H-field): R ≈ 40 dB
- Absorption loss: A = 8.69 × (0.15mm / 0.021mm) ≈ 62 dB
- **Total SE ≈ 102 dB** (theoretical)

**However, practical SE is limited by:**
- **Braid coverage gaps:** 90% coverage reduces SE to ~40-50 dB
- **Seam and termination resistance:** Poor bonding reduces SE to 20-30 dB
- **Pigtail termination inductance:** Reduces SE to 0-10 dB above 10 MHz

**Critical takeaway:** Shield material provides >60 dB theoretical SE, but termination quality determines actual performance (0-80 dB range).

### 3.3 Cable Shield Types and Construction

**3.3.1 Braided Shield**

Woven mesh of bare copper or tinned copper strands (16-48 strands per carrier, 4-24 carriers):

**Advantages:**
- High flexibility (withstands repeated flexing)
- Good coverage: 85-95% typical
- Low DC resistance: 5-20 mΩ/m
- Mechanical strength for termination

**Disadvantages:**
- Coverage gaps reduce SE at high frequency (>100 MHz)
- More expensive than foil ($5-15/meter vs. $2-5/meter)

**Typical specifications:**
- Belden 9841 (RS-485 cable): 85% tinned copper braid, 2-pair 22 AWG
- Alpha Wire 6412 (Servo encoder): 90% tinned copper braid, 4-pair 24 AWG
- Lapp Ölflex 540 (Motor power): 90% copper braid, 4×6mm² conductors

**3.3.2 Foil Shield (Aluminum-Polyester Laminate)**

Aluminum foil (6-50 μm thickness) laminated to polyester film (12-25 μm) with drain wire:

**Advantages:**
- 100% coverage (no gaps)
- Excellent SE at high frequency: 60-100 dB above 10 MHz
- Low cost: $2-5/meter
- Lightweight

**Disadvantages:**
- Poor flexibility (tears with repeated bending)
- Requires drain wire for termination (foil too thin to solder)
- Difficult 360° bonding (requires conductive tape or backshell)

**Typical applications:**
- Fixed installation (non-flexing cables)
- Ethernet (Cat5e/Cat6/Cat7): Foil shield standard
- Multi-pair control cables

**3.3.3 Combination Braid + Foil (Dual Shield)**

Foil shield under braided shield, combines advantages of both:

**Advantages:**
- 100% coverage from foil (high-frequency SE)
- Mechanical termination via braid (easy 360° bonding)
- Excellent SE across full spectrum: 60-80 dB from 10 kHz to 1 GHz

**Disadvantages:**
- Higher cost: $10-30/meter
- Larger diameter (reduced flexibility)

**Typical applications:**
- Premium servo encoder cables (Hirose, Phoenix Contact)
- Medical/aerospace (EMI-critical applications)
- Plasma/EDM signal cables

**3.3.4 Spiral/Serve Shield**

Helically wrapped tinned copper wires (not woven):

**Advantages:**
- Very high flexibility (constant-flex applications)
- Easy termination (individual wires)

**Disadvantages:**
- Low coverage: 60-75% typical
- Poor SE: 20-40 dB (gaps allow field penetration)
- Not recommended for EMI-critical applications

**Selection summary:**

| Shield Type | Coverage | SE @ 10 MHz | Flexibility | Cost | Best Application |
|-------------|----------|-------------|-------------|------|------------------|
| **Braided (90%)** | 85-95% | 40-60 dB | Excellent | $5-15/m | General-purpose, motor power |
| **Foil (100%)** | 100% | 60-100 dB | Poor | $2-5/m | Fixed installation, Ethernet |
| **Braid + Foil** | 100% | 60-80 dB | Good | $10-30/m | Servo encoders, plasma signals |
| **Spiral (60%)** | 60-75% | 20-40 dB | Excellent | $8-20/m | Constant-flex (avoid if possible) |

### 3.4 The Critical Importance of 360° Shield Bonding

**3.4.1 Why Pigtail Termination Fails**

"Pigtail" termination connects shield to ground via twisted wire (10-100mm length):

```
Cable shield ----+
                 |
         [Pigtail wire 50mm]
                 |
            Ground plane
```

**Problem:** Pigtail wire has inductance:

$$L_{wire} \approx 20 \text{ nH/cm} \times \text{length (cm)}$$

For 50mm (5cm) pigtail:
- L = 20 nH/cm × 5cm = 100 nH

**Impedance at high frequency:**

$$Z_L = 2\pi f L$$

| Frequency | Pigtail Impedance (100 nH) | Voltage Drop (1A common-mode) |
|-----------|----------------------------|-------------------------------|
| 1 MHz | 0.63Ω | 0.63V |
| 10 MHz | 6.3Ω | 6.3V |
| 100 MHz | 63Ω | 63V |

At 10 MHz, 1A common-mode current (typical from PWM drive) creates **6.3V ground potential difference** across pigtail—negating all shielding benefit. The shield becomes ineffective at precisely the frequencies where EMI is most severe.

**Measured shielding effectiveness with pigtail:**
- 1 kHz: 40 dB (DC resistance dominant, ~10 mΩ)
- 100 kHz: 35 dB (inductance starting to dominate)
- 1 MHz: 20 dB (inductive reactance > resistance)
- 10 MHz: **5 dB** (pigtail inductance destroys shielding)
- 100 MHz: **0 dB** (no shielding)

**3.4.2 360° Shield Bonding Theory**

360° circumferential bonding connects entire shield perimeter to ground plane or connector backshell:

```
Cable shield ---(360° contact)---+
                                  |
                             Ground plane
```

**Advantages:**
- **Ultra-low inductance:** L ≈ 1-10 nH (100× better than pigtail)
- **Parallel current paths:** Circumferential contact provides hundreds of parallel paths
- **Uniform field termination:** No discontinuities for fields to penetrate

**Inductance of 360° bond vs. pigtail:**

| Termination Method | Inductance | Z @ 10 MHz | Z @ 100 MHz |
|--------------------|-----------|------------|-------------|
| Pigtail (50mm) | 100 nH | 6.3Ω | 63Ω |
| Pigtail (10mm) | 20 nH | 1.3Ω | 13Ω |
| **360° bond (backshell)** | **5 nH** | **0.3Ω** | **3Ω** |
| **360° bond (EMI gasket)** | **2 nH** | **0.13Ω** | **1.3Ω** |

**Measured shielding effectiveness with 360° bonding:**
- 1 kHz: 40 dB
- 100 kHz: 45 dB
- 1 MHz: 50 dB
- 10 MHz: **55 dB** (vs. 5 dB for pigtail)
- 100 MHz: **60 dB** (vs. 0 dB for pigtail)

**360° bonding maintains >50 dB SE across entire frequency range**, providing consistent protection from PWM drives (4-20 kHz), plasma arcs (100 kHz - 1 MHz), and digital circuits (10-100 MHz).

### 3.5 Practical 360° Shield Termination Methods

**3.5.1 Circular Connector Backshell (Best Practice)**

Metal backshell (nickel-plated aluminum or EMI-grade zinc) with compression gland:

**Components:**
- Circular connector body (D-sub, M12, M23): Provides signal pin termination
- EMI backshell: Threads onto connector, surrounds cable
- Compression gland: Conductive gasket compresses against cable shield
- Ground plane attachment: Backshell bonds to panel with conductive gasket

**Assembly procedure:**
1. Strip cable jacket to expose 15-25mm of braid (do not damage braid)
2. Fold braid back over cable jacket
3. Slide backshell over folded braid
4. Tighten compression gland (torque: 0.5-2 N⋅m depending on size)
5. Mount connector to metal panel with conductive gasket
6. Verify <10 mΩ resistance from cable shield to panel

**Commercial examples:**
- ITT Cannon KJB series (D-sub backshells): $15-40 each
- Amphenol C091 series (Circular MIL-DTL-38999): $30-100 each
- Phoenix Contact SACC-DSI-MS (M12/M23): $20-60 each

**3.5.2 Cable Gland with EMI Gasket (Panel Entry)**

For cables without connectors entering enclosure:

**Components:**
- Metal cable gland (PG, M, or NPT thread): Brass or nickel-plated steel
- EMI gasket (conductive elastomer or wire mesh): Compresses between gland and cable shield
- Lock nut and washer: Secures gland to panel

**Assembly procedure:**
1. Pass cable through gland body (gland not yet tightened)
2. Strip jacket to expose 25-40mm of braid
3. Fold braid back over gland compression ring
4. Insert EMI gasket between braid and gland
5. Tighten gland compression nut (fold braid tightly against gasket)
6. Thread gland through panel hole
7. Secure with lock nut and washer (metal washer, 4-8 N⋅m torque)
8. Verify <10 mΩ resistance from cable shield to panel

**Commercial examples:**
- Lapp Skintop MS-M (EMI cable gland): $8-25 each
- Jacob 50.620 PA (Cable gland with EMI gasket): $10-30 each
- Heyco EMI/RFI cable gland: $12-35 each

**3.5.3 Conductive Tape Method (Emergency/Low-Cost)**

For prototyping or emergency repairs when proper connectors unavailable:

**Materials:**
- 3M 1183 or 1345 copper foil tape with conductive adhesive ($40-80/roll)
- Alternatively: Chomerics CHO-SEAL 1298 conductive fabric tape ($60-120/roll)

**Procedure:**
1. Strip cable jacket to expose 30-50mm of braid
2. Fan out braid strands radially (create umbrella shape)
3. Wrap conductive tape around fanned braid and ground plane surface (50mm overlap minimum)
4. Apply pressure to ensure adhesive contact (use non-conductive tape over conductive tape for strain relief)
5. Verify <50 mΩ resistance from shield to ground plane (higher than backshell, but acceptable)

**Limitations:**
- Lower reliability (adhesive degrades over time, especially with heat cycling)
- Moderate SE: 40-50 dB (vs. 60+ dB for backshell)
- Not suitable for vibration environments
- Use only for fixed installations or temporary testing

### 3.6 Shield Bonding at Both Ends vs. One End

**Historical guidance (pre-1990s, obsolete for high-frequency systems):**
- "Ground shield at one end only to prevent ground loops"

**Modern guidance (IEC 61000-5-2, mandatory for >100 kHz):**
- "Bond shield at both ends with 360° circumferential connection"

**Why both-end bonding is mandatory:**

1. **Ground loops are not created by shield bonding** (they exist due to multiple ground return paths through chassis, earth ground, etc.)—shield bonding to low-impedance ground plane prevents voltage differences from driving circulating current

2. **Single-end bonding fails at high frequency:** Shield-to-ground capacitance (50-100 pF/m) provides low-impedance path at RF frequencies, creating unbonded end:
   - At 10 MHz: Zcap = 1/(2π × 10 MHz × 100 pF) = **160Ω** (high impedance, poor shielding)
   - Unbonded end becomes "antenna feedpoint," radiating instead of shielding

3. **Both-end 360° bonding creates transmission line:** Shield becomes coaxial structure with controlled impedance, preventing resonances and maintaining low ground impedance across full frequency range

**Correct practice:**
- **Bond shield at both ends with 360° circumferential connection**
- **Ground plane at both ends must be part of same low-impedance plane** (not separate isolated grounds)
- **If legitimate concern about ground loops exists** (very rare with proper ground plane design), use common-mode choke on cable (Section 13.4) instead of leaving shield unbonded

**Exception (single-end bonding acceptable):**
- Analog instrumentation cables carrying <1 kHz signals with >1 MΩ source impedance
- These systems don't generate/receive high-frequency EMI
- Not applicable to CNC systems with PWM drives and digital communication

### 3.7 Twisted Pair vs. Twisted Shielded Pair

**3.7.1 Twisted Pair (Unshielded)**

Conductors twisted together (10-50 twists/meter depending on wire gauge):

**Noise rejection mechanism:** Magnetic field couples equal voltage into both conductors (common-mode). Differential receiver rejects common-mode:

$$V_{noise,diff} = V_{noise,CM} \times \text{Imbalance}$$

For 1V common-mode noise with 1% conductor length imbalance:
- Vnoise,diff = 1V × 0.01 = 10 mV (differential noise)

**Common-mode rejection ratio (CMRR):**
- 40 dB typical for twisted pair (100:1 rejection)
- 60 dB typical for precision-matched twisted pair
- Limited by: conductor length mismatch, capacitance imbalance, receiver input balance

**Limitations:**
- No protection against electric field (capacitive) coupling
- No protection against direct current injection (e.g., ESD strike to cable)
- CMRR degrades at high frequency (>1 MHz) due to parasitic capacitance asymmetry

**Best application:**
- RS-485, CAN bus in low-EMI environment (no plasma, short cable runs <10m)
- Low-cost sensor signals (thermocouples, RTDs) where shielding cost is prohibitive

**3.7.2 Twisted Shielded Pair (STP)**

Twisted pair surrounded by shield (foil or braid):

**Advantages over unshielded twisted pair:**
- **Shield blocks electric field coupling:** 40-80 dB additional rejection
- **Shield diverts ESD and transient currents:** Protects conductors from direct strikes
- **Shield provides defined return path:** Reduces crosstalk between multiple pairs in same cable

**Specification example—Encoder cable (Hirose HRQ series):**
- Conductors: 4-pair 24 AWG tinned copper, twisted 30 twists/meter
- Insulation: Foamed polyethylene (low capacitance, 15 pF/m/pair)
- Shield: 90% tinned copper braid
- Jacket: PUR (polyurethane, oil-resistant, flexible)
- Capacitance: 45 pF/m (conductor-to-conductor), 100 pF/m (conductor-to-shield)
- Cost: $18-30/meter

**Critical point:** Shield must be properly terminated (360° bonding at both ends) to realize full EMI rejection. Twisted shielded pair with pigtail termination performs worse than unshielded twisted pair due to shield-induced ground loops.

### 3.8 Cable Routing and Segregation

Physical separation provides additional EMI reduction beyond shielding:

**3.8.1 Segregation Guidelines**

| Cable Type | Voltage/Current | Minimum Separation from Signal Cables |
|------------|-----------------|--------------------------------------|
| AC power (120-240V, <10A) | 120-240V | 100mm (unshielded), 50mm (shielded) |
| DC power (<60V, <10A) | 12-48V | 50mm (unshielded), 25mm (shielded) |
| **Motor power (PWM drive)** | **325-560VDC bus, 10-50A** | **300mm (unshielded), 150mm (shielded)** |
| Plasma torch power | 100-250V, 20-200A | **500mm (no exceptions, too high EMI)** |
| Servo encoder (differential) | 5V | — (victim, reference) |
| Analog signals (±10V) | ±10V | — (victim, reference) |
| Ethernet, USB | 2-5V differential | 50mm from motor power |

**3.8.2 Crossing Angles**

When cable crossing is unavoidable (limited space in cable chain):
- **Cross at 90° angle** (minimizes mutual inductance coupling)
- **Never run parallel >100mm** (even with shielding, residual coupling accumulates)
- **Use barrier** (metal or conductive plastic) to separate motor and signal cables in same tray

**Mutual inductance reduction with 90° crossing:**
- Parallel run (worst case): 100% coupling
- 45° crossing: ~50% coupling
- **90° crossing: <10% coupling** (20 dB improvement)

### 3.9 Motor Power Cable Shielding

Motor power cables present special challenge:
- High current: 5-50A per phase (3 phases = 15-150A total)
- High voltage: 325-560VDC bus (PWM switching)
- High dI/dt: 100-500 A/μs during PWM transitions
- Length: 1-10m typical (cable acts as antenna)

**Motor cable construction:**

**Option 1: Shielded motor cable (preferred for EMI-critical systems)**
- Conductors: 3 or 4 core (U, V, W phases + PE ground)
- Size: 1.5-16mm² (12-6 AWG) depending on motor current
- Shield: Tinned copper braid 85-90% coverage
- Jacket: PVC or PUR
- Examples: Lapp Ölflex 540, igus Chainflex CF9

**Cost:** $15-40/meter (vs. $5-12/meter unshielded)
**EMI reduction:** 40-60 dB conducted emissions, 20-40 dB radiated emissions

**Option 2: Unshielded motor cable + common-mode choke (cost-effective alternative)**
- Standard 3-4 core motor cable: $5-12/meter
- Common-mode choke at drive end (all 3 phases + PE through ferrite core): $50-200
- **EMI reduction:** 20-40 dB conducted emissions, 10-20 dB radiated emissions
- **Trade-off:** Lower performance than shielded cable, but much lower cost for long runs (>10m)

**Shield termination for motor cables:**
- **Drive end:** 360° bonding to drive chassis via cable gland or backshell
- **Motor end:** 360° bonding to motor frame via cable gland
- **Both ends must bond to ground plane** (drive and motor chassis bonded to machine ground plane)

### 3.10 Special Considerations for Long Cables (>3m)

Long cables exhibit transmission line behavior at high frequencies, requiring additional considerations:

**3.10.1 Cable Capacitance Effects**

Motor cable capacitance (conductor-to-shield) loads PWM drive output:

$$C_{total} = C_{per-meter} \times \text{Length}$$

Typical motor cable: 150-250 pF/m (conductor-to-shield)

For 10m motor cable at 200 pF/m:
- Ctotal = 200 pF/m × 10m = 2000 pF = 2 nF

**Charging current during PWM transition:**

$$I_{charge} = C \frac{dV}{dt}$$

For 325V, 100 ns rise time:
- Icharge = 2 nF × (325V / 100 ns) = **6.5A peak charging current**

This 6.5A adds to motor current during each PWM transition (16 kHz = 32,000 transitions/second), increasing drive losses and EMI.

**Drive derating:** Most PWM drives specify maximum cable length (20-50m typical) before output current must be derated or output choke added.

**3.10.2 Resonance and Reflected Waves**

Cable characteristic impedance (Z₀) interacts with motor impedance, creating reflections:

$$Z_0 = \sqrt{\frac{L}{C}}$$

For typical motor cable (L = 0.5 μH/m, C = 200 pF/m):
- Z₀ = √(0.5 μH / 200 pF) = 50Ω

If motor impedance ≠ 50Ω at high frequency (typical motor is 5-20Ω), reflections occur, creating voltage overshoot at motor terminals:

$$V_{peak} = V_{drive} \times \left(1 + \frac{Z_0 - Z_{motor}}{Z_0 + Z_{motor}}\right)$$

For 325V drive, 50Ω cable, 10Ω motor:
- Vpeak = 325V × (1 + (50 - 10)/(50 + 10)) = 325V × 1.67 = **542V at motor terminals**

This 542V overvoltage stresses motor insulation and increases EMI.

**Mitigation:** Install motor choke (low-pass filter) or use PWM drive with controlled rise time (slowed to 1-2 μs, eliminating reflections but increasing switching losses).

### 3.11 Signal Cable Specifications for CNC Applications

**3.11.1 Servo Encoder Cables (High Priority)**

**Requirements:**
- Differential signals (RS-422): 5V logic, 1-10 MHz signal rate (2000-5000 count/rev encoders at 3000 RPM)
- Low capacitance: <50 pF/m (reduces signal distortion)
- Excellent shielding: >60 dB SE (nearby motor cables generate severe EMI)
- Flexible: >10 million flex cycles (cable chain in motion)

**Recommended cable:**
- Lapp Unitronic LI2YCY (TP) or equivalent
- 2-4 twisted pair, 22-24 AWG
- Tinned copper braid 90% + foil shield (dual shield)
- PUR jacket (oil-resistant)
- Cost: $12-25/meter

**3.11.2 Analog Cables (Torch Height, Spindle Speed, Temperature)**

**Requirements:**
- Low noise: ±10V signals with 12-16 bit ADC (2.4-0.15 mV resolution)
- Shield against capacitive and magnetic coupling
- Twisted pair (differential or pseudo-differential with shield as return)

**Recommended cable:**
- Belden 8761 (1-pair 22 AWG shielded) or multi-pair equivalent
- Foil + 90% braid shield
- Cost: $3-8/meter

**3.11.3 Stepper Motor Step/Direction Cables**

**Requirements:**
- 5V TTL or 24V differential signals
- Moderate frequency: 10-500 kHz step pulse rate
- Length: 1-5m typical

**Recommended cable:**
- Belden 9842 (2-pair 22 AWG shielded) or equivalent
- Tinned copper braid 85-90%
- Cost: $5-12/meter

**3.11.4 Ethernet (EtherCAT, Modbus TCP) Cables**

**Requirements:**
- 100BASE-TX or 1000BASE-T: 100-125 MHz differential signaling
- Impedance controlled: 100Ω ±15% (standard Cat5e/Cat6)
- Shield mandatory for industrial environment

**Recommended cable:**
- Cat5e or Cat6 STP (Shielded Twisted Pair), not UTP
- Foil shield + drain wire or braid shield
- Examples: Belden 7923A (Cat5e STP), Lapp Etherline Cat6 (2170339)
- Cost: $3-10/meter

**360° shield bonding:** Use shielded RJ45 connectors with metal body bonded to ground plane, or M12 X-coded connectors (industrial Ethernet standard with integrated EMI gasket).

### 3.12 Cable Shield Measurement and Verification

**3.12.1 DC Resistance Test (Shield Continuity)**

Measure shield resistance from one end to other (cable disconnected from equipment):

**Acceptable values:**
- <100 mΩ for <10m cable
- <20 mΩ/m as general guideline

**If resistance >100 mΩ:** Shield damage (broken braid strands), poor termination, or corrosion. Investigate and repair.

**3.12.2 Shield-to-Ground Impedance Test (Termination Quality)**

Measure impedance from cable shield to ground plane at 10 MHz using LCR meter or impedance analyzer:

**Acceptable values:**
- <1Ω for 360° bonding with backshell/cable gland
- <10Ω for conductive tape method

**If impedance >10Ω:** Poor 360° contact, pigtail termination, or corroded connection. Rework termination.

**3.12.3 Shielding Effectiveness Measurement (Lab Test)**

For critical applications, measure SE using injection clamp method:
1. Inject RF signal into cable shield at one end (signal generator + current injection clamp)
2. Measure coupled signal on inner conductor (oscilloscope or spectrum analyzer)
3. Calculate SE = 20 log₁₀(Vinject / Vcouple)

**Expected SE with proper 360° bonding:**
- 40-50 dB for braided shield (85-90% coverage)
- 60-80 dB for braid + foil dual shield
- 0-20 dB for pigtail termination (confirms poor practice)

### 3.13 Summary: Shielding Design Checklist

**Cable Selection:**
- [ ] Use shielded twisted pair (STP) for all signals in EMI-critical systems
- [ ] Select braided shield (≥85% coverage) for flexibility or braid+foil for maximum SE
- [ ] Specify motor power cable with shield for plasma/high-EMI systems

**Shield Termination (CRITICAL):**
- [ ] Implement 360° circumferential bonding at both ends (never pigtail)
- [ ] Use circular connector backshells or EMI cable glands (preferred methods)
- [ ] Verify <10 mΩ DC resistance from shield to ground plane at each termination
- [ ] Verify <1Ω impedance at 10 MHz (confirms proper 360° contact)

**Cable Routing:**
- [ ] Maintain ≥150mm separation between motor power and signal cables
- [ ] Cross cables at 90° when parallel routing unavoidable
- [ ] Segregate plasma torch cables by ≥500mm (extreme EMI source)

**Ground Plane Integration:**
- [ ] Bond cable shields to ground plane (not isolated star point)
- [ ] Bond drive chassis, motor frame, and enclosure to same ground plane
- [ ] Ensure ground plane impedance <10 mΩ DC, <1Ω at 10 MHz (see Section 13.5)

**Verification:**
- [ ] Measure shield continuity: <100 mΩ end-to-end
- [ ] Measure shield-to-ground impedance: <1Ω at 10 MHz
- [ ] Test system with oscilloscope: encoder signals <50 mV noise, analog inputs <10 mV noise

Proper shielding with 360° bonding provides 40-80 dB EMI reduction—transforming unreliable, intermittent systems into stable production machines. The cost difference between proper shielded cables and poor termination is $100-500 for typical CNC system, while the cost of EMI-induced failures is $10,000-100,000. This is the highest return-on-investment EMC measure after ground plane implementation.

***

*Section 13.3 Total: 4,283 words | 14 equations | 5 worked examples | 7 tables*

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
