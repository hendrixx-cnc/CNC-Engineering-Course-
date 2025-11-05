# Appendix G: Safety and Regulatory Standards

---

## G.1 Machine Safety Standards

### G.1.1 International Safety Standards

| Standard | Region | Scope | Key Requirements |
|----------|--------|-------|------------------|
| **ISO 12100** | International | Machinery safety (general) | Risk assessment, hazard elimination hierarchy |
| **ISO 13849-1** | International | Safety-related control systems | Safety categories (B, 1, 2, 3, 4), SIL ratings |
| **ISO 13850** | International | Emergency stop function | E-stop button specs, circuit design |
| **IEC 60204-1** | International | Electrical equipment of machines | Wiring colors, voltage levels, control circuits |
| **ANSI B11.0** | USA | General machine safety | Guards, interlocks, operator training |
| **NFPA 79** | USA | Electrical standard for industrial machinery | Panel wiring, grounding, short-circuit protection |
| **CE Marking** | EU | Product safety directives | LVD, EMC, Machinery Directive compliance |

### G.1.2 Risk Assessment (ISO 12100)

**Hierarchy of Risk Reduction:**
1. **Inherent Safe Design:** Eliminate hazard (e.g., use 24V instead of 230V for controls)
2. **Engineering Controls:** Guards, interlocks, light curtains
3. **Information for Use:** Warning labels, training, procedures
4. **PPE (Last Resort):** Safety glasses, gloves, hearing protection

**Risk Matrix:**

| Severity → | Minor Injury | Moderate Injury | Serious Injury | Fatal |
|------------|-------------|-----------------|----------------|-------|
| **Frequent** | Medium | High | Very High | Very High |
| **Probable** | Low | Medium | High | Very High |
| **Occasional** | Low | Low | Medium | High |
| **Rare** | Negligible | Low | Low | Medium |

**Example Hazards for CNC Machines:**
- **Rotating spindle:** Severity = Serious/Fatal, Probability = Occasional → **High Risk** (requires interlock guard)
- **Moving gantry:** Severity = Moderate, Probability = Rare → **Low Risk** (requires warning labels, awareness)

---

## G.2 Machine Guarding Requirements

### G.2.1 Guard Types (ANSI B11.19)

| Type | Description | Advantages | Disadvantages | Applications |
|------|-------------|------------|---------------|--------------|
| **Fixed Guard** | Permanent barrier (bolted panels) | Simple, reliable | Limits access for setup | Full enclosures, chip guards |
| **Interlocked Guard** | Opens, stops machine via switch | Allows access, automatic protection | More complex, can be defeated | Access doors, spindle enclosure |
| **Adjustable Guard** | Position adjusted for operation | Flexible for different parts | Requires operator setup | Blade guards, chip shields |
| **Self-Adjusting** | Opens/closes with workpiece | Automatic, no adjustment | Limited applications | Table saw blade guards |

**Interlocking Safety Switch Requirements:**
- **Type 1 (coded):** Switch mechanically linked to guard, cannot be easily defeated
- **Type 2 (magnetic):** Non-contact switch, higher security (coded magnets)
- **Type 3 (RFID):** Unique coded transponder, highest security
- **Type 4 (trapped key):** Physical key locks guard, key required to start machine

**Recommendation for CNC:** Type 1 or 2 interlocked switches on all access doors, wired to safety relay (dual-channel monitoring).

### G.2.2 Safety Distances (ISO 13855)

**Reach-Over Distance (top of guard to hazard):**

$$D = K \times T + C$$

where:
- $D$ = minimum distance (mm)
- $K$ = approach speed (1600 mm/s hand, 2000 mm/s body)
- $T$ = stopping time of machine (s)
- $C$ = penetration depth (8mm minimum)

**Example:** CNC with 0.5s stopping time (E-stop circuit + axis deceleration)
$$D = 1600 \times 0.5 + 8 = 808 \text{ mm}$$

**Guard height must be ≥808mm above hazard, or hazard must stop within 0.5s**

**Reach-Through Distance (opening size to hazard):**

| Opening Size (mm) | Minimum Distance to Hazard (mm) |
|------------------|-------------------------------|
| <4 | 0 (finger cannot pass) |
| 4-6 | 35 |
| 6-8 | 50 |
| 8-10 | 80 |
| 10-12 | 100 |
| 20-30 | 180 |
| 30-40 | 230 |

**Example:** Chip tray vent holes (10mm diameter) → hazard (spindle) must be ≥100mm from opening.

---

## G.3 Electrical Safety Standards

### G.3.1 Voltage Isolation and Clearances (IEC 60204-1)

**Minimum Clearance (Air Gap) Between Conductors:**

| Voltage | Clearance (mm) | Creepage (mm) |
|---------|---------------|--------------|
| **24V DC (SELV)** | 1.5 | 2.5 |
| **50V AC / 120V DC** | 3.0 | 5.0 |
| **230V AC** | 5.5 | 8.0 |
| **400V AC** | 8.0 | 10.0 |

**Clearance:** Shortest distance through air between conductors
**Creepage:** Shortest distance along surface of insulation

**Example:** 230V AC terminal block → adjacent terminals must be ≥5.5mm apart (air), with ≥8mm surface distance.

### G.3.2 LOTO (Lock-Out Tag-Out) Procedures (OSHA 1910.147)

**Purpose:** Prevent unexpected machine startup during maintenance.

**Procedure:**
1. **Notify** affected personnel of shutdown
2. **Shut down** machine normally (controlled stop)
3. **Isolate** energy (open main disconnect, circuit breaker)
4. **Lock** disconnect in "off" position (padlock on breaker handle)
5. **Tag** disconnect ("Do Not Operate - Maintenance in Progress")
6. **Verify** zero energy (test start button, measure voltage with multimeter)
7. **Release stored energy** (discharge capacitors, bleed hydraulics, lower raised components)

**Lock Types:**
- Single-person lockout: One lock per person working
- Group lockout: Multiple locks on hasp (each worker has own lock, all must remove for re-energization)

**Tag Requirements:**
- Durable material (plastic-coated cardstock)
- Text: "DANGER - DO NOT OPERATE" or "OUT OF SERVICE"
- Name, date, reason for lockout

---

## G.4 Personal Protective Equipment (PPE)

### G.4.1 Minimum PPE for CNC Operations

| PPE | Standard | Protection | Required For |
|-----|----------|------------|--------------|
| **Safety Glasses** | ANSI Z87.1 | Impact, flying chips | All CNC operations (mandatory) |
| **Hearing Protection** | ANSI S3.19 | Noise >85 dB | Router, milling, plasma cutting |
| **Gloves** | ANSI/ISEA 105 | Cut resistance, abrasion | Material handling (NOT during machine operation) |
| **Steel-Toe Boots** | ASTM F2413 | Compression, impact | Heavy material handling, large machines |
| **Respirator** | NIOSH 42 CFR 84 | Dust, fumes | Wood routing, composite machining, plasma fume |

**Warning:** Never wear gloves during machine operation (risk of entanglement). Remove jewelry, tie back long hair, avoid loose clothing.

### G.4.2 Noise Levels and Hearing Protection

**Permissible Noise Exposure (OSHA 1910.95):**

| Noise Level (dBA) | Max Duration/Day |
|------------------|------------------|
| 90 | 8 hours |
| 95 | 4 hours |
| 100 | 2 hours |
| 105 | 1 hour |
| 110 | 30 minutes |
| 115 | 15 minutes or less |

**Typical CNC Machine Noise:**
- Small router (24,000 RPM): 95-105 dBA → **hearing protection required**
- Milling machine (6,000 RPM): 80-90 dBA → **hearing protection recommended**
- Plasma cutter (arc): 90-100 dBA → **hearing protection required**

**Hearing Protection Ratings:**
- **Foam earplugs:** NRR 29-33 dB (highest rating, correct insertion critical)
- **Reusable earplugs:** NRR 25-27 dB (more comfortable, lower cost over time)
- **Earmuffs:** NRR 22-31 dB (easy to use, works with safety glasses)
- **Electronic earmuffs:** NRR 22-24 dB (amplifies speech, blocks loud noise)

**Effective Noise Reduction:**
$$\text{Effective NRR} = \frac{\text{Rated NRR} - 7}{2}$$

Example: NRR 30 earplugs → Effective reduction = (30-7)/2 = 11.5 dB

---

## G.5 Fire Safety

### G.5.1 Fire Extinguisher Types (NFPA 10)

| Class | Fuel Type | Extinguisher | Color | CNC Applications |
|-------|-----------|--------------|-------|------------------|
| **A** | Ordinary combustibles (wood, paper, plastic) | Water, foam | Green | Wood routing, plastic machining |
| **B** | Flammable liquids (oil, coolant, solvents) | CO₂, dry chemical | Red | Coolant fires, hydraulic leaks |
| **C** | Electrical equipment | CO₂, dry chemical | Blue | Electrical panel, motor fires |
| **D** | Combustible metals (Mg, Ti, Al powder) | Dry powder (special) | Yellow | Metal dust from grinding |

**Recommendation for CNC Shop:**
- **ABC dry chemical extinguisher** (10 lb minimum) mounted near machine exit
- Inspect monthly (pressure gauge in green zone)
- Replace/recharge every 6 years or after use

**Combustible Dust Hazard:**
- Wood dust, aluminum chips, composite fibers can ignite if suspended in air
- Clean dust daily (vacuum, not compressed air which suspends dust)
- Ground metal chip bins (prevent static spark)

### G.5.2 Coolant Fire Risks

**Coolant Types and Flashpoint:**

| Coolant Type | Flashpoint (°C) | Fire Risk | Precautions |
|--------------|----------------|-----------|-------------|
| **Water-based emulsion** | >100 | Very Low | Monitor bacteria growth (mold, odor) |
| **Synthetic coolant** | >120 | Low | Change when contaminated |
| **Soluble oil (mineral)** | 200-250 | Low-Medium | Keep away from open flame |
| **Straight cutting oil** | 150-200 | Medium | Hot chip accumulation can ignite, clean regularly |

**Fire Prevention:**
- Clean chips from coolant tank weekly (prevent hotspots, bacterial growth)
- Use coolant mist collector (reduces airborne oil, improves visibility)
- Keep spindle clean (chip buildup + high RPM = heat + friction fire risk)

---

## G.6 Material-Specific Safety

### G.6.1 Wood and Composites

**Hazards:**
- **Dust inhalation:** Hardwood dust is IARC Group 1 carcinogen (nasal cancer risk)
- **Fire:** Fine dust suspended in air is explosive (minimum ignition energy ~10 mJ)

**Safety Measures:**
- Dust collection: Minimum 400 CFM per machine, <0.5 micron filtration
- Respirator: N95 minimum (P100 for very fine dust like MDF)
- Grounding: Metal ducting bonded to ground (prevent static ignition)

### G.6.2 Metals

**Hazards:**
- **Sharp chips:** Lacerations from handling swarf
- **Metal fumes:** Zinc (galvanized), lead (brass/bronze), cadmium (rare)
- **Reactive metals:** Magnesium, titanium (fire risk if chips overheat)

**Safety Measures:**
- Gloves for chip handling (cut-resistant, ANSI Level A4 minimum)
- Fume extraction for zinc/brass (local exhaust ventilation)
- Magnesium/titanium: Use flood coolant (prevent chip ignition), Class D extinguisher nearby

### G.6.3 Plastics

**Hazards:**
- **Fumes:** PVC releases HCl (hydrochloric acid vapor), acrylic releases methyl methacrylate (MMA)
- **Static:** Acrylic builds static charge → chip/dust attraction

**Safety Measures:**
- Ventilation: 100 CFM minimum for enclosed area
- Avoid PVC if possible (corrosive fumes damage machine, health hazard)
- Anti-static spray or grounding for acrylic (reduce chip adhesion)

---

## G.7 Laser Safety (Fiber/CO₂ Laser Systems)

### G.7.1 Laser Classification (IEC 60825-1)

| Class | Power | Hazard | Control Measures |
|-------|-------|--------|------------------|
| **1** | <0.39 mW | Safe (enclosed) | None (fully enclosed laser cutter) |
| **1M** | <0.5 mW CW | Safe without optics | Do not use magnifiers/telescopes |
| **2** | <1 mW visible | Blink reflex protects | Avoid staring |
| **3R** | <5 mW | Eye hazard if direct | Laser warning signs, training |
| **3B** | <500 mW | Serious eye/skin hazard | Interlocked enclosure, laser goggles |
| **4** | >500 mW | Fire + diffuse reflection hazard | Full enclosure, interlocks, training, goggles |

**Fiber Laser (1064 nm):** Class 4 (enclosed machine = Class 1 system)

**Safety Requirements for Class 4 (Enclosed):**
- Interlocked doors (laser shuts off when opened)
- Emergency stop accessible from operator position
- Laser warning labels (Class 4 on interior, Class 1 on exterior if fully enclosed)
- Laser safety officer (LSO) designated if multiple lasers

### G.7.2 Laser Safety Eyewear

**Optical Density (OD) Required:**

$$OD = \log_{10}\left(\frac{P_{incident}}{P_{MPE}}\right)$$

where:
- $P_{incident}$ = incident laser power (W)
- $P_{MPE}$ = maximum permeable exposure (W/cm²)

**Example:** 100W fiber laser (1064 nm), beam diameter 5mm
- $P_{incident} = 100$ W / $(0.25 \text{ cm})^2 / \pi = 5093$ W/cm²
- $P_{MPE}$ = 0.005 W/cm² (for 1064 nm, 10s exposure)
- $OD = \log_{10}(5093 / 0.005) = 6.0$

**Goggles required: OD 6+ at 1064 nm wavelength**

**Caution:** Standard safety glasses do NOT protect against lasers. Use laser-specific eyewear with correct OD and wavelength.

---

## G.8 Confined Space and Enclosure Safety

### G.8.1 Confined Space Definition (OSHA 1910.146)

**Criteria:**
1. Large enough for worker to enter and perform work
2. Limited means of entry/exit
3. Not designed for continuous occupancy

**Example:** Large CNC enclosure (>2m³) requiring internal maintenance = **confined space**

**Hazards:**
- Oxygen deficiency (<19.5% O₂) or enrichment (>23.5% O₂)
- Flammable atmosphere (coolant vapor, dust)
- Toxic atmosphere (plasma fume, oil mist)

### G.8.2 Permit-Required Confined Space (PRCS)

**Additional Hazards Requiring Permit:**
- Engulfment risk (chips, coolant)
- Internal configuration causing entrapment
- Serious safety/health hazard

**Entry Procedure:**
1. Atmospheric testing (O₂, flammable gas, CO, H₂S)
2. Ventilation (forced air, 100+ CFM)
3. Entry permit (signed by supervisor)
4. Attendant outside (communication, rescue)
5. Retrieval equipment (harness, winch)

**Recommendation:** For large CNC enclosures, treat as PRCS if entry required during operation (e.g., waterjet tank maintenance).

---

**End of Safety and Regulatory Standards Appendix**
