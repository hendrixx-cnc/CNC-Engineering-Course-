# Appendix B: Standard Hardware Specifications

---

## B.1 Metric Fastener Grades and Properties (ISO 898-1)

### B.1.1 Property Classes

| Grade | Material | Proof Load (MPa) | Tensile Strength (MPa) | Yield Strength (MPa) | Hardness (HB) | Marking |
|-------|----------|-----------------|----------------------|---------------------|--------------|---------|
| **4.6** | Low carbon steel | 225 | 400 | 240 | 114-238 | 4.6 on head |
| **4.8** | Low carbon steel | 310 | 420 | 340 | 114-238 | 4.8 on head |
| **5.8** | Low/medium carbon steel | 380 | 520 | 420 | 147-238 | 5.8 on head |
| **8.8** | Medium carbon steel (quenched) | 600 | 800 | 640 | 238-342 | 8.8 on head |
| **9.8** | Medium carbon steel (quenched) | 650 | 900 | 720 | 269-342 | 9.8 on head |
| **10.9** | Alloy steel (Q&T) | 830 | 1,040 | 940 | 304-361 | 10.9 on head |
| **12.9** | Alloy steel (Q&T, high strength) | 970 | 1,220 | 1,100 | 353-415 | 12.9 on head |

**Notes:**
- First number × 100 = minimum tensile strength (MPa)
- Second number × 10 × first number = proof load (MPa)
- Example: 8.8 → 8×100 = 800 MPa tensile, 8×8×10 = 640 MPa proof load

**Common Applications:**
- **4.6/4.8:** Non-critical fasteners, light-duty brackets, cable management
- **8.8:** Standard structural bolts, machine assembly (most common grade)
- **10.9:** Motor mounts, spindle clamps, high-stress joints
- **12.9:** Critical fasteners requiring maximum strength, preload applications

### B.1.2 Metric Bolt Torque Specifications (Grade 8.8, Lubricated)

**Lubrication condition:** Light oil or anti-seize compound (friction coefficient μ = 0.12-0.15)

| Size | Pitch (mm) | Proof Load (kN) | Torque 75% Proof (N·m) | Torque 85% Proof (N·m) | Clamping Force @ 75% (kN) | Preload Recommended |
|------|-----------|-----------------|----------------------|----------------------|-------------------------|---------------------|
| **M3** | 0.5 | 1.96 | 1.0 | 1.2 | 1.47 | 75% for general use |
| **M4** | 0.7 | 3.54 | 2.1 | 2.5 | 2.66 | 75% for general use |
| **M5** | 0.8 | 5.52 | 3.8 | 4.5 | 4.14 | 75% for general use |
| **M6** | 1.0 | 8.02 | 6.4 | 7.5 | 6.02 | 75% for general use |
| **M8** | 1.25 | 14.2 | 15 | 18 | 10.7 | 85% for critical joints |
| **M10** | 1.5 | 22.6 | 30 | 36 | 17.0 | 85% for critical joints |
| **M12** | 1.75 | 32.7 | 52 | 62 | 24.5 | 85% for critical joints |
| **M16** | 2.0 | 58.6 | 130 | 155 | 44.0 | 85% for critical joints |
| **M20** | 2.5 | 92.0 | 260 | 310 | 69.0 | 85% for critical joints |

**Torque Formula:**
$$T = K \cdot d \cdot F$$

where:
- $T$ = torque (N·m)
- $K$ = nut factor (0.18-0.22 for lubricated, 0.25-0.35 for dry)
- $d$ = nominal diameter (m)
- $F$ = clamping force (N)

**Example Calculation for M8 Bolt:**

Proof load = 14.2 kN, Target preload = 75% = 10.65 kN

$$T = 0.20 \times 0.008 \times 10,650 = 17 \text{ N·m}$$

**Tightening Procedure:**
1. Clean threads, apply light oil or anti-seize
2. Hand-tighten until snug
3. Use calibrated torque wrench, tighten in star pattern (for multiple bolts)
4. Torque to specified value in 2-3 steps (50% → 75% → 100%)
5. Mark bolt head position, verify no rotation after 24 hours (checks for settling)

### B.1.3 Metric Nut Types and Grades

| Type | Grade | Height | Strength | Applications |
|------|-------|--------|----------|--------------|
| **Hex Nut (DIN 934)** | 8, 10 | 0.8×d | Standard | General purpose, most common |
| **Heavy Hex Nut (DIN 6330)** | 10 | 1.0×d | High strength | High-preload joints, vibration |
| **Nylon Insert Lock Nut (DIN 985)** | 8, 10 | 0.8×d + nylon ring | Medium | Prevents loosening, single-use recommended |
| **All-Metal Lock Nut (DIN 980)** | 10 | 1.0×d | High | High-temperature, reusable lock nut |
| **Thin Jam Nut (DIN 439)** | 5, 6 | 0.4×d | Low | Locking second nut, limited space |
| **Square Nut (DIN 557)** | 5, 6 | 0.7×d | Low | Captive nuts, T-slots |

**Lock Nut Comparison:**

| Type | Reusable | Max Temp (°C) | Vibration Resistance | Cost |
|------|----------|--------------|---------------------|------|
| **Nylon Insert** | 3-5 times | 120 | Excellent | $ |
| **All-Metal Prevailing Torque** | 10+ times | 300 | Good | $$ |
| **Split Lock Washer** | Multiple | 200 | Fair | $ |
| **Nord-Lock Wedge Washer** | 100+ times | 300 | Excellent | $$$ |

---

## B.2 Imperial Fastener Grades (SAE/ASTM)

### B.2.1 SAE Bolt Grades

| Grade | Tensile Strength (ksi) | Proof Load (ksi) | Yield Strength (ksi) | Head Markings | Material |
|-------|----------------------|------------------|---------------------|---------------|----------|
| **Grade 2** | 60 | 33 | 57 | No marks | Low/medium carbon steel |
| **Grade 5** | 120 | 85 | 92 | 3 radial lines | Medium carbon steel, quenched |
| **Grade 8** | 150 | 120 | 130 | 6 radial lines | Medium carbon alloy, Q&T |
| **A325** | 120 | 85 | 92 | A325 marking | Structural bolt (buildings, bridges) |
| **A490** | 150 | 120 | 130 | A490 marking | High-strength structural bolt |

**Note:** 1 ksi (kilopound per square inch) = 6.895 MPa

### B.2.2 Imperial Bolt Torque Specifications (Grade 5, Lubricated)

| Size (UNC) | TPI | Torque 75% Proof (lb·ft) | Torque 85% Proof (lb·ft) | Clamping Force @ 75% (lbf) |
|-----------|-----|-------------------------|-------------------------|-------------------------|
| **1/4"-20** | 20 | 8 | 9 | 1,990 |
| **5/16"-18** | 18 | 17 | 19 | 3,150 |
| **3/8"-16** | 16 | 30 | 35 | 4,800 |
| **1/2"-13** | 13 | 75 | 85 | 9,350 |
| **5/8"-11** | 11 | 150 | 170 | 14,750 |
| **3/4"-10** | 10 | 265 | 300 | 21,200 |
| **1"-8** | 8 | 590 | 665 | 37,650 |

---

## B.3 Washer Specifications

### B.3.1 Flat Washer Dimensions (Metric, DIN 125 Form A)

| Bolt Size | Inner Dia (mm) | Outer Dia (mm) | Thickness (mm) | Purpose |
|-----------|---------------|---------------|----------------|---------|
| M3 | 3.2 | 7 | 0.5 | Distribute load, prevent marring |
| M4 | 4.3 | 9 | 0.8 | Distribute load |
| M5 | 5.3 | 10 | 1.0 | Distribute load |
| M6 | 6.4 | 12 | 1.6 | Distribute load |
| M8 | 8.4 | 16 | 1.6 | Distribute load |
| M10 | 10.5 | 20 | 2.0 | Distribute load |
| M12 | 13.0 | 24 | 2.5 | Distribute load |

**Fender Washer (Large OD):** Used when clamping soft materials (wood, plastic) or oversized holes. OD = 3-4× bolt diameter typical.

### B.3.2 Spring Lock Washer (Split Washer)

**Function:** Prevent loosening via spring tension and sharp edges biting into surfaces.

**Limitations:**
- **Not effective under vibration** (studies show no improvement vs. flat washer)
- **Obsolete for critical applications** (replaced by nylon lock nuts, thread lockers)
- **Acceptable for non-critical, low-vibration fasteners**

**Better alternatives:**
- Nylon insert lock nuts (vibration)
- Thread locker (medium strength Loctite 243)
- Safety wire (aircraft/racing applications)
- Nord-Lock washers (high-load, vibration-critical)

### B.3.3 Belleville Spring Washer (Disc Spring)

**Function:** Maintain preload under thermal expansion, creep, or settling.

**Applications:**
- Bearing preload adjustment
- Vibration isolation mounts
- Maintaining bolt tension in joints subject to thermal cycling

**Design Parameters:**
- Load vs. deflection is non-linear (see manufacturer curves)
- Can be stacked in series (more deflection) or parallel (more load)
- Material: Spring steel (65Mn), stainless 301

---

## B.4 Threaded Inserts and Fasteners for Aluminum/Plastic

### B.4.1 Helicoil Thread Inserts

**Purpose:** Create steel threads in soft materials (aluminum, magnesium, plastic).

**Installation:**
1. Drill oversize hole (e.g., 6.6mm for M6 Helicoil)
2. Tap with special STI tap (larger than standard M6 tap)
3. Install Helicoil with installation tool (coiled spring insert)
4. Break off tang with punch

**Advantages:**
- 2-3× stronger than tapped aluminum threads
- Repairable (extract damaged Helicoil, install new one)
- Standard bolts fit (no special hardware)

**Length:** 1.5× to 2.5× bolt diameter recommended for full strength

### B.4.2 Rivnuts (Rivet Nuts, Nutserts)

**Purpose:** Install threaded fastener in sheet metal or thin-walled material.

**Types:**
- **Closed-end (sealed):** Prevents leakage, used in waterproof applications
- **Open-end:** Lower cost, easier installation

**Installation:** Requires rivnut tool (manual or pneumatic). Bolt pulls mandrel, collapsing body to form bulge on backside.

**Load capacity:** 1/3 to 1/2 of standard nut (due to thin wall). Use larger size or multiple rivnuts for high loads.

### B.4.3 PEM Nuts and Standoffs (Self-Clinching)

**Purpose:** Permanent threaded fastener in sheet metal (0.5-3mm thickness).

**Installation:** Press-fit using arbor press or manual tool. Knurls/undercuts bite into parent material and deform to lock in place.

**Advantages:**
- Flush or near-flush on one side
- Very strong (resists pullout better than rivnut)
- Reusable threads

**Common types:**
- S-type nuts (flush on one side)
- SO-type standoffs (spacers between sheets)
- FH-type standoffs (flush head)

---

## B.5 Thread Locking and Sealing

### B.5.1 Thread Locker (Anaerobic Adhesive)

| Type | Strength | Removable | Max Gap Fill | Temp Range | Applications |
|------|----------|-----------|--------------|------------|--------------|
| **Loctite 222 (Purple)** | Low | Hand tools | 0.15mm | -55 to 150°C | Adjustment screws, set screws |
| **Loctite 243 (Blue)** | Medium | Hand tools | 0.15mm | -55 to 150°C | General fasteners, vibration resistance |
| **Loctite 271 (Red)** | High | Heat (250°C) | 0.15mm | -55 to 180°C | Permanent assembly, bearing retaining |
| **Loctite 2701 (Green)** | High (wicking) | Heat | 0.10mm | -55 to 180°C | Pre-assembled fasteners (apply after tightening) |

**Curing:** Anaerobic (cures in absence of air, presence of metal). 24 hours for full cure, handling strength in 10-30 minutes.

**Removal:**
- Low/Medium: Heat to 120°C with heat gun, disassemble
- High: Heat to 250°C (torch), disassemble immediately while hot

### B.5.2 Thread Sealant (PTFE Tape vs. Liquid)

**PTFE Tape (Teflon Tape):**
- Wrap 3-4 turns clockwise (viewing end of fitting)
- Used for NPT pipe threads (water, air, coolant)
- Does NOT provide thread locking (only sealing)

**Liquid Thread Sealant (Pipe Dope):**
- Applied to male threads
- Seals better than tape for tapered threads
- Some formulations include thread locker (check datasheet)

**Hydraulic Fittings (O-ring Face Seal, JIC, SAE):** Do NOT use thread sealant. Seal occurs at mating face (O-ring or cone), not threads. Thread locker OK if anti-seize not required.

---

## B.6 Retaining Rings (Circlips)

### B.6.1 Internal vs. External Retaining Rings

| Type | Function | Installation | Groove Depth |
|------|----------|--------------|--------------|
| **Internal (DIN 472)** | Retain bearing in housing bore | Expand ring, insert into groove | 0.8-1.2mm typical |
| **External (DIN 471)** | Retain bearing on shaft | Compress ring, snap into groove | 0.8-1.2mm typical |

**Material:** Spring steel (1.4310 stainless common), phosphate or zinc-plated carbon steel

**Load Rating:** Axial load capacity 50-80% of groove cross-sectional area × material yield strength. Use shoulder for high loads.

### B.6.2 Spiral Retaining Rings

**Advantages over stamped rings:**
- No ears (flush with shaft/bore)
- 360° contact (no stress concentration)
- Reusable many times

**Disadvantages:**
- Lower load capacity than stamped rings
- Requires special installation/removal tool

---

## B.7 Dowel Pins for Precision Alignment

### B.7.1 Dowel Pin Types

| Type | Tolerance | Hardness | Applications |
|------|-----------|----------|--------------|
| **Standard Tolerance (m6)** | -0.012 to -0.030mm | 58-65 HRC | General precision alignment |
| **Close Tolerance (h7)** | +0.000 to -0.012mm | 58-65 HRC | High-precision jigs, fixtures |
| **Oversize (0.1mm, 0.2mm, 0.5mm)** | Standard | 58-65 HRC | Repair of worn holes |

**Material:** Ground and hardened alloy steel (1.4305 stainless available)

**Sizing:**
- Hole reamed to H7 tolerance (precision reamer required)
- Pin pressed in (1-3 ton press for 6mm × 30mm pin typical)
- Interference fit: 0.010-0.020mm for steel, 0.005-0.015mm for aluminum

**Reaming depth:** Dowel pin length + 5mm minimum (prevents bottoming out)

### B.7.2 Spring Pins (Roll Pins, Slotted Spring Pins)

**Function:** Shear pins, quick-disassembly alignment.

**Installation:** Drive in with hammer or press. Slot compresses, spring force retains pin.

**Advantages:**
- Compensates for hole tolerance (oversized hole OK)
- Removable (vs. solid dowel pin)

**Disadvantages:**
- Lower shear strength than solid dowel pin (30-50% typical)
- Can walk out under vibration without retaining method

---

## B.8 Set Screws (Grub Screws)

### B.8.1 Set Screw Point Types

| Point Type | Best Use | Holding Power | Damage to Shaft |
|------------|----------|---------------|-----------------|
| **Cup Point** | General purpose | ★★★☆☆ | Moderate (indents shaft) |
| **Cone Point** | Permanent assembly | ★★★★★ | High (sharp point mars surface) |
| **Flat Point** | Soft shafts | ★★☆☆☆ | Low (broad area) |
| **Dog Point** | Machined detent | ★★★★☆ | None (seats in drilled hole) |
| **Oval Point** | Delicate shafts | ★★☆☆☆ | Low (rounded contact) |

**Recommendation for CNC:**
- **Shaft collars, pulleys:** Cup point or cone point (most common)
- **Fine-positioning:** Flat point with thread locker
- **Precision:** Dog point (shaft has mating detent hole)

### B.8.2 Torque Specifications for Set Screws

**Grade 45H (Alloy steel, hardened to 45 HRC min):**

| Size | Torque (N·m) | Hex Key Size |
|------|-------------|--------------|
| M3 | 1.0 | 2.0mm |
| M4 | 2.2 | 2.5mm |
| M5 | 4.4 | 3.0mm |
| M6 | 7.5 | 4.0mm |
| M8 | 18 | 5.0mm |
| M10 | 36 | 6.0mm |

**Installation:**
- Clean threads, apply medium-strength thread locker
- Orient setscrews 90° apart (if multiple per collar)
- Torque to spec with hex key (not Allen key ball-end, which reduces torque transfer)

---

## B.9 Specialty Fasteners for CNC

### B.9.1 T-Slot Nuts and Bolts

**Drop-in T-Nuts:**
- Used with aluminum extrusion (80/20, Misumi)
- Insert from end of slot or drop into slot opening
- M5, M6, M8 threads typical
- Ball spring or sliding style

**Flanged T-Nuts (Hammer Head):**
- Rotate 90° after insertion into slot
- Higher load capacity than drop-in
- Requires access to end of slot for installation

**Loading:** Cantilever load on T-slot nut: 100-500 N typical depending on size. Use multiple nuts or longer bolt for high loads.

### B.9.2 Captive Panel Screws

**Quarter-turn fasteners (Dzus, Camloc):**
- Quick-access panels (electronics enclosures, inspection doors)
- 1/4 turn locks, spring-loaded retention
- Low clamping force (use gasket for sealing)

**Thumb screws:**
- Tool-less adjustment
- Knurled head or wing head
- Lower torque capacity (hand-tight only)

### B.9.3 Shoulder Bolts (Shoulder Screws, Stripper Bolts)

**Function:** Precision shaft/pivot with threaded fastening.

**Design:**
- Shoulder: Ground diameter (h7 tolerance), hardened
- Thread: Smaller diameter than shoulder, used for retention only
- Head: Socket head cap screw style

**Applications:**
- Rotating/sliding joints (shoulder acts as bearing surface)
- Precision spacers
- Linkage pivots

**Sizing:** Shoulder diameter clearance fit with mating part (H7/g6 typical). Shoulder length = stack height + 0.5mm clearance.

---

**End of Hardware Specifications Appendix**
