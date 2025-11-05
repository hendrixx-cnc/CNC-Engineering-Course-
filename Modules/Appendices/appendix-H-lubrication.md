# Appendix H: Lubrication Schedules and Specifications

---

## H.1 Linear Motion Lubrication

### H.1.1 Linear Guide Rail Lubrication

**Lubricant Type:** ISO VG 32 hydraulic oil (standard), NLGI Grade 2 lithium grease (enclosed environments)

**Lubrication Schedule:**

| Operating Conditions | Interval | Method |
|---------------------|----------|--------|
| **Clean environment, light duty** | Every 100 km travel or 6 months | Manual (grease nipple, 2-3 drops oil) |
| **Moderate dust, medium duty** | Every 50 km travel or 3 months | Automatic single-shot lubricator |
| **Heavy duty, high speed** | Every 20 km travel or monthly | Centralized auto-lube system |
| **Dirty environment (wood dust, coolant)** | Weekly inspection, lube as needed | Manual + dust covers/bellows |

**Recommended Lubricants:**

| Brand | Product | Type | Viscosity | Applications |
|-------|---------|------|-----------|--------------|
| **Mobil** | DTE 24 | Hydraulic Oil | ISO VG 32 | General linear guides |
| **Shell** | Tellus S2 M 32 | Hydraulic Oil | ISO VG 32 | Standard CNC |
| **THK** | AFE-CA | Grease | NLGI #2 | THK linear guides (OEM spec) |
| **HIWIN** | Lubricant A | Grease | NLGI #2 | HIWIN guides (OEM spec) |
| **Mobilith** | SHC 220 | Synthetic Grease | NLGI #2 | High temp, long life |

### H.1.2 Ball Screw Lubrication

**Lubricant Type:** Lithium-based grease with EP (extreme pressure) additives, NLGI Grade 2

**Re-greasing Procedure:**
1. Clean old grease from nut exterior and screw shaft
2. Inject fresh grease via Zerk fitting (grease gun, 2-3 pumps)
3. Manually cycle axis 10-20 times (distribute grease throughout nut)
4. Wipe excess grease from shaft
5. Verify smooth motion

**Lubrication Schedule:**

| Load Factor | Speed (RPM) | Re-grease Interval (hours) |
|-------------|------------|---------------------------|
| Light (<30% $C_a$) | <1000 | 500 |
| Light (<30% $C_a$) | 1000-2000 | 300 |
| Medium (30-60% $C_a$) | <1000 | 200 |
| Medium (30-60% $C_a$) | 1000-2000 | 100 |
| Heavy (>60% $C_a$) | <1000 | 100 |
| Heavy (>60% $C_a$) | 1000-2000 | 50 (or oil mist system) |

**Oil Mist Systems (High-Speed Applications):**
- Minimum oil flow: 0.01-0.02 cc/min per 100mm screw length
- Oil type: ISO VG 32-68
- Compressed air: 0.3-0.5 MPa (3-5 bar)

**Recommended Greases:**

| Brand | Product | EP Rating | Temp Range (°C) | Applications |
|-------|---------|-----------|---------------|--------------|
| **Mobilux** | EP 2 | High | -20 to +130 | General ball screws |
| **Shell** | Gadus S2 V220 | High | -30 to +120 | Standard CNC |
| **THK** | AFJ-LF | Medium | -40 to +100 | Low-friction, long life |
| **Kluber** | Isoflex NBU 15 | Very High | -40 to +150 | Heavy load, high speed |

---

## H.2 Spindle Bearing Lubrication

### H.2.1 Grease-Lubricated Spindles

**Grease Type:** High-speed bearing grease, NLGI Grade 1.5-2, polyurea or lithium complex base

**Re-greasing Intervals (by DN factor):**

**DN Factor = Bearing bore diameter (mm) × RPM**

| DN Factor | Re-grease Interval |
|-----------|-------------------|
| <300,000 | Every 2000 hours or annually |
| 300,000-500,000 | Every 1000 hours or 6 months |
| 500,000-1,000,000 | Every 500 hours or 3 months |
| >1,000,000 | Oil-mist or oil-air system required |

**Example:** 80mm bore bearing at 10,000 RPM
$$DN = 80 \times 10,000 = 800,000$$
**→ Re-grease every 500 hours (or consider oil-air system for extended life)**

**Recommended Spindle Greases:**

| Brand | Product | Base | Max Speed (DN) | Temp Range (°C) |
|-------|---------|------|---------------|----------------|
| **Kluber** | Isoflex Topas NB 52 | Polyurea | 1,500,000 | -40 to +160 |
| **SKF** | LGMT 2 | Lithium | 500,000 | -40 to +120 |
| **Castrol** | Longtime PD 2 | Lithium Complex | 750,000 | -30 to +140 |
| **Mobil** | Polyrex EM | Polyurea | 1,200,000 | -35 to +180 |

### H.2.2 Oil-Mist and Oil-Air Lubrication

**Oil-Mist System:**
- Continuous mist delivery (air + oil droplets)
- Oil flow: 0.005-0.01 cc/min per bearing
- Air pressure: 0.15-0.3 MPa (1.5-3 bar)
- Suitable for DN <1,500,000

**Oil-Air System:**
- Precise oil + air pulses (programmable intervals)
- Oil flow: 0.01-0.05 cc/min per bearing (adjustable)
- Air pressure: 0.5-0.8 MPa (5-8 bar)
- Suitable for DN >1,000,000 (high-speed spindles up to 40,000 RPM)

**Recommended Oils:**

| Brand | Product | Viscosity (ISO VG) | Max Temp (°C) | Applications |
|-------|---------|-------------------|--------------|--------------|
| **Mobil** | Velocite Oil No. 6 | 10 | 80 | Low-speed spindles |
| **Shell** | Morlina S1 B 10 | 10 | 90 | General spindles |
| **Kluber** | Klüberoil 4 UH1-68 N | 68 | 120 | Medium/high speed |
| **Castrol** | Ilocut EDM 24 | 24 | 100 | High-speed spindles (>20,000 RPM) |

---

## H.3 Rack and Pinion Lubrication

**Lubricant Type:** Open-gear grease (tacky, water-resistant) or spray lubricant

**Lubrication Schedule:**

| Environment | Method | Interval |
|-------------|--------|----------|
| **Indoor, clean** | Spray (PTFE dry lube) | Weekly or 100 km travel |
| **Outdoor, exposed** | Open-gear grease | Weekly or 50 km travel |
| **High load, continuous** | Automatic spray system | Daily or per operating hour |

**Recommended Products:**

| Brand | Product | Type | Applications |
|-------|---------|------|--------------|
| **Mobilgear** | OGL 461 | Open Gear Grease | Heavy-duty racks, outdoor |
| **WD-40** | Specialist Dry Lube | PTFE Spray | Indoor racks, low dust |
| **Kluber** | Barrierta L 55/2 | Spray Grease | Precision racks, moderate load |
| **CRC** | Sta-Lube Open Gear Lube | Aerosol Grease | General racks, easy application |

**Application Procedure:**
1. Clean rack teeth (remove old grease, chips)
2. Apply thin coat of grease to tooth faces (not roots)
3. Cycle axis to distribute lubricant
4. Wipe excess (prevents chip attraction)

---

## H.4 Coolant and Cutting Fluid Maintenance

### H.4.1 Water-Soluble Coolant (Emulsion)

**Concentration:** 5-10% (1:20 to 1:10 dilution) for most machining

**Testing and Maintenance:**

| Parameter | Target Range | Test Method | Frequency |
|-----------|-------------|-------------|-----------|
| **Concentration** | ±1% of target | Refractometer | Daily |
| **pH** | 8.5-9.5 | pH test strips | Daily |
| **Bacteria/Fungi** | <10⁵ CFU/mL | Dip slide test | Weekly |
| **Tramp oil** | <5% | Visual (skim surface) | Daily |

**Coolant Life Extension:**
- Add biocide if bacteria count >10⁶ CFU/mL (foul odor, skin irritation)
- Skim tramp oil daily (prevents anaerobic bacteria growth)
- Top-off with pre-mixed coolant (not concentrate) to maintain concentration
- Full changeout every 3-6 months (or when odor/contamination cannot be controlled)

**Disposal:** Contact local waste management (coolant = hazardous waste in most jurisdictions)

### H.4.2 Straight Cutting Oil (Mineral Oil)

**Viscosity:** ISO VG 15-32 for most CNC operations

**Maintenance:**
- Filter continuously (10 micron nominal filtration)
- Change when dark/cloudy (oxidation, contamination)
- Typical life: 6-12 months with filtration

**Fire Safety:** Flashpoint >200°C typical, but hot chips can ignite oil mist. Use coolant mist collector.

---

## H.5 Pneumatic System Maintenance

### H.5.1 Compressed Air Quality (ISO 8573-1)

**Particulate Class:** 1-7 (Class 1 = <0.1 μm, 0.1 mg/m³ max)
**Water Content:** 1-10 (Class 4 = -40°C pressure dew point typical for CNC)
**Oil Content:** 1-5 (Class 3 = 1 mg/m³ max)

**CNC Recommendation:** Class 4 or better (dew point -40°C, 1 mg/m³ oil, 5 μm particles)

### H.5.2 FRL (Filter-Regulator-Lubricator) Maintenance

**Filter:**
- Check weekly, replace element when pressure drop >0.5 bar
- Drain condensate daily (automatic drain recommended)

**Regulator:**
- Set to 6 bar (0.6 MPa) typical for CNC pneumatics
- Check gauge accuracy annually

**Lubricator:**
- Fill with ISO VG 32 pneumatic oil
- Adjust drip rate: 1 drop per 1000 actuations (visible in sight glass)
- Check weekly

**Note:** Some modern pneumatic components are pre-lubricated and do NOT require FRL lubricator (check manufacturer spec).

---

## H.6 Way Oil (for Sliding Surfaces)

**Applications:** Box ways (Bridgeport-style mills), dovetail slides (older CNC)

**Lubricant Type:** Tacky way oil with stick-slip additives, ISO VG 68-220

**Recommended Products:**

| Brand | Product | Viscosity (ISO VG) | Tackiness | Applications |
|-------|---------|-------------------|-----------|--------------|
| **Mobil** | Vactra Oil No. 2 | 68 | Medium | Horizontal slides |
| **Mobil** | Vactra Oil No. 4 | 220 | High | Vertical slides, heavy load |
| **Shell** | Tonna S3 M 68 | 68 | Medium | General ways |
| **Castrol** | Magna BD 220 | 220 | High | Heavy machine tools |

**Lubrication Schedule:**
- Manual oiling: Before each use (few drops on ways)
- One-shot system: Every 50-100 cycles (adjustable)

---

## H.7 Grease Compatibility Chart

**Mixing Incompatible Greases:** Can cause separation, hardening, or loss of lubricity.

| Lithium | Calcium | Aluminum | Polyurea | Silicone |
|---------|---------|----------|----------|----------|
| **OK** | Caution | Caution | OK | NO |
| Caution | **OK** | NO | Caution | NO |
| Caution | NO | **OK** | NO | NO |
| OK | Caution | NO | **OK** | Caution |
| NO | NO | NO | Caution | **OK** |

**Legend:**
- **OK:** Compatible (can mix)
- **Caution:** Limited compatibility (purge old grease before switching)
- **NO:** Incompatible (flush completely before switching)

**Recommendation:** When changing grease type, purge old grease by cycling axis 50+ times with new grease, then re-grease normally.

---

**End of Lubrication Schedules and Specifications Appendix**
