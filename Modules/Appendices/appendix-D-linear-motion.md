# Appendix D: Linear Motion System Specifications

---

## D.1 Ball Screw Specifications

### D.1.1 Ball Screw Accuracy Grades (ISO 3408-3, DIN 69051)

| Grade | Lead Accuracy (μm/300mm) | Applications | Cost |
|-------|------------------------|--------------|------|
| **C10 (Precision 10)** | ±52 | General industrial, low precision | $ |
| **C7 (Precision 7)** | ±52 | Standard CNC, general machining | $$ |
| **C5 (Precision 5)** | ±23 | Precision CNC, coordinate measuring | $$$ |
| **C3 (Precision 3)** | ±12 | High-precision CNC, grinding machines | $$$$ |
| **C2 (Precision 2)** | ±8 | Ultra-precision machining, inspection equipment | $$$$$ |
| **C1 (Precision 1)** | ±4 | Semiconductor equipment, metrology | $$$$$$ |

**Nomenclature:** Lead error = maximum deviation over 300mm travel length

**Example:** C5 grade ball screw with 2m travel → max cumulative error = 2000/300 × 23 = 153 μm (~0.15mm)

**Recommendation for CNC Gantry:**
- **C7:** Plasma, flame cutting, router (±0.1mm tolerance acceptable)
- **C5:** Milling, waterjet (±0.05mm tolerance required)
- **C3:** Precision milling, engraving, PCB drilling

### D.1.2 Ball Screw Sizing and Nomenclature

**Standard Designation: RM2005-C7**
- **R:** Rolled ball screw (ground = "G")
- **M:** Metric
- **20:** Nominal diameter (mm) of screw shaft
- **05:** Lead (mm) per revolution
- **C7:** Accuracy grade

**Common Diameters and Leads:**

| Designation | Diameter (mm) | Lead (mm) | Critical Speed (RPM) @ 1m | Max Velocity (mm/s) @ 3000 RPM | Typical Use |
|-------------|--------------|----------|--------------------------|-------------------------------|-------------|
| **RM1204** | 12 | 4 | 4500 | 200 | Light duty, Z-axis |
| **RM1605** | 16 | 5 | 3800 | 250 | Small CNC, 3D printer Z |
| **RM2005** | 20 | 5 | 3200 | 250 | Standard CNC X/Y |
| **RM2010** | 20 | 10 | 3200 | 500 | Fast rapids, plasma X/Y |
| **RM2505** | 25 | 5 | 2800 | 250 | Heavy CNC X/Y/Z |
| **RM2510** | 25 | 10 | 2800 | 500 | Heavy CNC, fast rapids |
| **RM3205** | 32 | 5 | 2400 | 250 | Very heavy loads |
| **RM3210** | 32 | 10 | 2400 | 500 | Large gantry X-axis |

**Critical Speed:** Speed at which screw begins to resonate/whip (function of diameter, unsupported length, end fixation).

$$\omega_{crit} = \frac{\pi}{L^2} \sqrt{\frac{E \cdot I}{m}}$$

where:
- $L$ = unsupported length (m)
- $E$ = Young's modulus of steel (210 GPa)
- $I$ = moment of inertia of screw shaft (m⁴)
- $m$ = mass per unit length (kg/m)

**Safety Factor:** Operate below 80% of critical speed to avoid vibration.

### D.1.3 Ball Screw Load Ratings and Life

**Dynamic Load Rating ($C_a$):** Load (in N) at which screw achieves 1 million revolutions (L₁₀ life).

**Life Calculation:**

$$L_{10} = \left(\frac{C_a}{F_a}\right)^3 \text{ (million revolutions)}$$

where:
- $L_{10}$ = rated life (90% of screws survive)
- $C_a$ = dynamic load rating (N)
- $F_a$ = applied axial load (N)

**Convert to hours of operation:**

$$L_{hours} = \frac{L_{10} \times 10^6}{RPM \times 60}$$

**Example: RM2010 ball screw**
- $C_a = 8,500$ N (typical for RM2010)
- Applied load: $F_a = 1,000$ N (gantry + cutting force)
- Operating speed: 1500 RPM average

$$L_{10} = \left(\frac{8500}{1000}\right)^3 = 614 \text{ million revolutions}$$

$$L_{hours} = \frac{614 \times 10^6}{1500 \times 60} = 6,822 \text{ hours}$$

**At 40 hours/week operation → 170 weeks (3.3 years) before replacement**

### D.1.4 Ball Screw Preload Methods

**Purpose of Preload:** Eliminate axial play (backlash), increase stiffness.

**Preload Methods:**

| Method | Description | Stiffness | Backlash | Cost |
|--------|-------------|-----------|----------|------|
| **Single Nut (No Preload)** | Standard nut with internal clearance | Low | 0.05-0.15mm | $ |
| **Double Nut (Spacer Preload)** | Two nuts with shim spacer | Medium | <0.01mm | $$ |
| **Double Nut (Spring Preload)** | Two nuts with compression spring | Medium | <0.01mm, adjustable | $$ |
| **Oversized Ball Preload** | Single nut with larger balls | High | <0.005mm | $$$ |
| **Gothic Arch Preload (Ground)** | Special ball groove geometry | Very High | <0.002mm | $$$$ |

**Recommended Preload:**
- **CNC milling/routing:** 3-8% of dynamic load rating (medium preload)
- **Plasma/waterjet:** 1-3% of dynamic load rating (light preload, lower friction)
- **Grinding/ultra-precision:** 8-12% of dynamic load rating (heavy preload)

**Formula:**
$$F_{preload} = 0.03 \times C_a \text{ to } 0.08 \times C_a$$

### D.1.5 Ball Screw End Fixation

| Fixation Type | Axial Stiffness | Critical Speed | Cost | Applications |
|---------------|----------------|----------------|------|--------------|
| **Free-Free** | Very Low | Low | $ | Not recommended (only for prototyping) |
| **Fixed-Free** | Low | Medium | $ | Short screws (<500mm), low loads |
| **Fixed-Supported** | Medium | Medium-High | $$ | Standard CNC (<1500mm) |
| **Fixed-Fixed** | High | High | $$$ | Long screws (>1500mm), high-speed rapids |

**Fixed End:** BK/BF bearing blocks with angular contact bearings (preloaded), constrained axially and radially.

**Supported End:** FK/FF bearing blocks with deep groove ball bearings, constrained radially only (allows thermal expansion).

**Example Setup for 2m X-Axis:**
- Motor end: BK20 (fixed, locked with locknut)
- Opposite end: FK20 (supported, allows 0.5mm axial float)
- Thermal expansion @ 20°C temp rise: $\Delta L = 2000 \times 11 \times 10^{-6} \times 20 = 0.44$ mm → supported end accommodates without stress

---

## D.2 Linear Guide Rail Specifications

### D.2.1 Linear Guide Types

| Type | Load Direction | Rigidity | Accuracy | Cost | Applications |
|------|---------------|----------|----------|------|--------------|
| **Square Rail (THK HRW, HIWIN HGW)** | Heavy radial/moment | Highest | ±5μm | $$$$ | Heavy milling, large gantry |
| **Standard Rail (THK HRC, HIWIN HGH)** | Moderate all directions | High | ±10μm | $$$ | General CNC, mid-size machines |
| **Compact Rail (THK SRG, HIWIN MGN)** | Light to medium | Medium | ±15μm | $$ | Small CNC, 3D printers |
| **Miniature Rail (THK SSR, HIWIN EGH)** | Light radial only | Low | ±20μm | $ | Pick-place, linear actuators |
| **Cylindrical Rail (SBR)** | Light radial | Low | ±50μm | $ | Budget CNC, not recommended for precision |

**Accuracy Grades:**
- **Normal (N):** ±10-15μm straightness/parallelism over 300mm
- **High (H):** ±5-8μm straightness/parallelism over 300mm
- **Precision (P):** ±3-5μm straightness/parallelism over 300mm
- **Super Precision (SP):** ±2μm straightness/parallelism over 300mm

### D.2.2 Linear Guide Load Ratings

**Static Load Rating ($C_0$):** Maximum static load before permanent deformation (safety factor 3-5 typical).

**Dynamic Load Rating ($C$):** Load at which guide achieves 50 km of travel (L₅₀ life).

**Life Calculation:**

$$L = \left(\frac{f_H f_T f_C f_W C}{P}\right)^3 \times 50 \text{ km}$$

where:
- $f_H$ = hardness factor (1.0 for standard)
- $f_T$ = temperature factor (1.0 for <100°C)
- $f_C$ = contact factor (1.0 for recirculating ball)
- $f_W$ = load factor (1.0-1.5 depending on direction)
- $C$ = dynamic load rating (N)
- $P$ = applied load (N)

**Example: HIWIN HGW25CC (Heavy Square Rail)**
- Dynamic load rating: $C = 60,800$ N
- Applied load (vertical axis with gantry): $P = 5,000$ N
- Load factors: All = 1.0 (conservative)

$$L = \left(\frac{60800}{5000}\right)^3 \times 50 = 9,083 \text{ km}$$

**At 200 mm/s average speed:**
$$L_{hours} = \frac{9,083,000}{0.2 \times 3600} = 12,615 \text{ hours (6.3 years @ 40 hrs/week)}$$

### D.2.3 Common Linear Guide Sizes and Ratings

**Standard Rail (HG-Series, equivalent to THK HRC):**

| Rail Size | Block Type | Dynamic Load (N) | Static Load (N) | Preload Options | Weight/Block (kg) | Typical Axis |
|-----------|-----------|-----------------|----------------|-----------------|------------------|--------------|
| **HGH15CA** | 15mm compact | 12,240 | 17,160 | Z0, ZA, ZB | 0.14 | Small CNC Z-axis |
| **HGH20CA** | 20mm compact | 24,990 | 37,730 | Z0, ZA, ZB | 0.29 | Mid CNC Y/Z-axis |
| **HGH25CA** | 25mm standard | 38,220 | 59,290 | Z0, ZA, ZB | 0.66 | Standard CNC X/Y |
| **HGH30CA** | 30mm standard | 54,930 | 88,200 | Z0, ZA, ZB | 1.08 | Heavy CNC X/Y |
| **HGW35CC** | 35mm heavy | 94,080 | 191,820 | ZA, ZB, ZC | 2.15 | Large gantry X-axis |
| **HGW45CC** | 45mm heavy | 156,960 | 343,350 | ZA, ZB, ZC | 4.22 | Very heavy milling |

**Preload Classes:**
- **Z0:** No preload (light clearance), smooth motion, higher speed
- **ZA:** Light preload, low friction, 3-6% of $C_0$
- **ZB:** Medium preload, standard CNC, 6-10% of $C_0$
- **ZC:** Heavy preload, high rigidity, 10-13% of $C_0$

**Recommendation:** ZA for plasma/waterjet, ZB for milling/routing.

### D.2.4 Linear Guide Mounting and Alignment

**Mounting Bolt Torque (Grade 12.9):**

| Rail Size | Bolt Size | Torque (N·m) | Bolt Pattern Spacing (mm) |
|-----------|----------|-------------|-------------------------|
| 15mm | M4 | 2.5 | 60 |
| 20mm | M5 | 4.5 | 60 |
| 25mm | M6 | 7.5 | 60 |
| 30mm | M8 | 18 | 80 |
| 35mm | M10 | 36 | 80 |
| 45mm | M12 | 62 | 100 |

**Alignment Procedure:**
1. Surface grind or precision machine mounting surface (flatness <0.02mm per 300mm)
2. Clean surfaces with acetone (remove all oil/debris)
3. Apply thin oil film to rail bottom
4. Tighten mounting bolts to 50% torque in sequence from center outward
5. Install blocks, check for smooth motion (no tight spots)
6. Torque bolts to 100% spec
7. Verify running parallelism: <0.02mm over full travel (dial indicator on reference surface)

**Parallelism Between Rails (Dual Rail Axis):**
- **Y-axis (gantry beam):** <0.02mm over full length (critical to prevent binding)
- **X-axis (dual rails on same beam):** <0.01mm over full length

---

## D.3 Rack and Pinion Systems

### D.3.1 Rack Types and Specifications

| Type | Pressure Angle | Accuracy | Backlash | Cost | Applications |
|------|---------------|----------|----------|------|--------------|
| **Standard Spur Gear Rack** | 20° | ±0.1mm/m | 0.1-0.3mm | $ | Budget CNC, large travel low precision |
| **Ground Spur Rack** | 20° | ±0.05mm/m | 0.05-0.1mm | $$ | Standard CNC, long-travel plasma |
| **Helical Rack** | 19.5°-20° helix | ±0.03mm/m | 0.02-0.05mm | $$$ | High-speed CNC, smooth motion |
| **Ball Bearing Rack** | N/A | ±0.02mm/m | <0.01mm | $$$$ | Precision long-travel (rare, specialty) |

**Common Modules (Metric):**
- **M1.5 (1.5mm pitch):** Small CNC, light loads
- **M2.0 (2.0mm pitch):** Mid-size CNC
- **M2.5 (2.5mm pitch):** Standard plasma tables
- **M3.0 (3.0mm pitch):** Heavy routers, large gantry
- **M4.0 (4.0mm pitch):** Industrial large-format

**Module Calculation:**

$$\text{Module (M)} = \frac{\text{Pitch diameter (mm)}}{\text{Number of teeth}}$$

Linear travel per pinion revolution:
$$L = M \times \pi \times N$$

where $N$ = number of pinion teeth.

**Example:** M2.5 module, 20-tooth pinion
$$L = 2.5 \times \pi \times 20 = 157 \text{ mm/rev}$$

### D.3.2 Pinion Selection

**Number of Teeth:** 16-25 teeth typical (trade-off between size and smoothness)

**Recommendations:**
- **16 teeth:** Minimum (small diameter, higher backlash)
- **20 teeth:** Standard (good balance)
- **25 teeth:** Smoother motion, larger diameter, lower torque ripple

**Backlash:** 0.05-0.15mm typical for standard gears. Reduced via:
- Split pinion (two pinions with spring preload)
- Anti-backlash pinion (internal spring mechanism)
- Dual rack (two racks at different heights with opposing pinions)

### D.3.3 Rack and Pinion Mounting

**Rack Mounting:**
- Mount to precision-ground steel channel or extrusion
- Dowel pins every 500mm for alignment (prevents creep)
- Torque mounting bolts to specified value (M6 → 7.5 N·m typical)
- Shim as needed to align pitch line parallel to guide rails (±0.05mm over 1m)

**Pinion Alignment:**
- Pinion-to-rack clearance: 0.1-0.2mm (use feeler gauge)
- Check mesh across full travel (no tight/loose spots)

---

## D.4 Couplings and Shaft Connections

### D.4.1 Flexible Coupling Types

| Type | Misalignment (angular/parallel) | Torsional Stiffness | Backlash | Cost | Applications |
|------|-------------------------------|---------------------|----------|------|--------------|
| **Oldham Coupling** | 1° / 0.5mm | Medium | <0.1° | $ | General motion, moderate precision |
| **Bellows Coupling** | 1° / 0.1mm | High | <0.05° | $$ | Servo/stepper to ball screw (standard) |
| **Beam Coupling** | 3° / 0.25mm | Very High | <0.01° | $$ | Encoder coupling, high precision |
| **Jaw Coupling (Spider)** | 1° / 0.25mm | Low | 0.2° | $ | Light duty, absorbs shock, vibration |
| **Disc Coupling** | 1° / 0.1mm | Very High | <0.01° | $$$ | High-speed, high-torque, precision |

**Recommendation for CNC:**
- **Bellows coupling** for motor-to-ball screw (most common, zero backlash, accommodates slight misalignment)
- **Beam coupling** for encoder mounting (torsionally stiff, electrically isolating)

### D.4.2 Coupling Sizing

**Torque Rating:** Select coupling with torque rating ≥ 2× motor peak torque (safety factor for shock loads, acceleration).

**Bore Sizes:** Must match motor shaft and ball screw diameter. Common:
- Motor shaft: 8mm, 10mm, 12.7mm (1/2"), 14mm
- Ball screw: 10mm, 12mm, 14mm, 16mm

**Clamping Method:**
- **Set screw:** Simple, low cost, can slip under high torque
- **Clamp style:** Higher torque capacity, no shaft damage, requires flat on shaft

**Example:** NEMA 23 (14mm shaft) to RM2010 ball screw (16mm diameter)
- Coupling: Bellows type, 8mm and 10mm bores, clamp style
- Torque rating: 10 N·m (NEMA 23 peak torque = 4 N·m → 2.5× safety factor)

---

## D.5 Lubrication Specifications

### D.5.1 Ball Screw Lubrication

**Lubricant Types:**
- **Lithium grease (NLGI Grade 2):** General purpose, standard CNC
- **Molybdenum disulfide (MoS₂) grease:** High load, slow speed
- **PTFE grease:** Clean environments (medical, food), low lubricity
- **Oil mist system:** High-speed applications (>3000 RPM), automatic

**Lubrication Schedule:**
- **Light duty (plasma, router):** Re-grease every 500 hours
- **Medium duty (milling):** Re-grease every 200 hours
- **Heavy duty (high load, high speed):** Re-grease every 100 hours or oil mist system

**Re-greasing Procedure:**
1. Clean old grease from nut exterior
2. Inject new grease via grease nipple (Zerk fitting)
3. Cycle axis back/forth 10-20 times to distribute grease
4. Wipe excess grease from screw shaft
5. Verify smooth motion (no binding)

### D.5.2 Linear Guide Lubrication

**Automatic Lubrication (Recommended):**
- Single-shot lubricator (refillable cartridge, activates each block pass)
- Centralized lube system (pneumatic pump, distributes to all blocks)

**Manual Lubrication:**
- Oil: ISO VG 32 hydraulic oil (standard)
- Apply 2-3 drops per block via grease nipple
- Frequency: Every 100km of travel or 6 months, whichever first

**Cleaning:** Wipe rails weekly with lint-free cloth + light oil. Remove chips/debris that can score rail/ball raceways.

---

**End of Linear Motion System Specifications Appendix**
