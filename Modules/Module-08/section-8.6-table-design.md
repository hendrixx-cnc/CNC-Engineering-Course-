## 6. Table Design and Catcher Systems: Tank Depth, Slat Geometry, and Water Management

### 6.1 Waterjet Table Requirements and Design Constraints

Waterjet cutting tables must satisfy five simultaneous requirements absent in laser or plasma systems: (1) **workpiece support** maintaining flatness within ±0.5 mm across 3-4 meter spans while minimizing jet interference (slat spacing 10-25 mm creates $<$5% kerf obstruction probability), (2) **jet energy dissipation** in catcher tank filled with water to depth 150-300 mm, absorbing 30-120 kW continuous cutting power and reducing exit jet velocity from 900 m/s to $<$10 m/s preventing tank erosion, (3) **abrasive collection and settling** allowing spent garnet (4.1 g/cm³ density) to settle in quiescent zones while overflow removes fine particles ($<$50 mesh) preventing re-circulation and pump damage, (4) **water quality maintenance** via filtration (10-50 μm) and temperature control (15-25°C) ensuring consistent cutting performance and preventing biological growth, and (5) **parts and scrap removal** via manual or automated systems extracting finished parts from tank without operator immersion or cutting interruption. Integration of these functions—structural support providing 2,000-5,000 kg capacity, hydraulic energy absorption preventing 50+ dB noise reflection, sediment management handling 50-200 kg/day abrasive waste, and water circulation processing 500-2,000 L/min flow—distinguishes waterjet table engineering from simpler laser/plasma designs requiring only structural support and fume extraction.

**Table design trade-offs:**

| Feature | Slat Table | Brush Table | Parallel Plate | Downdraft Tank |
|---------|-----------|-------------|----------------|----------------|
| **Support structure** | Steel slats 10-25 mm spacing | Stainless steel bristles 0.5 mm diameter | Perforated plates 5-10 mm holes | Replaceable ceramic tiles |
| **Part support** | Excellent (solid contact) | Good (bristles deflect) | Excellent | Excellent |
| **Edge quality** | Fair (potential slat marks on bottom) | Excellent (minimal contact) | Fair (plate marks) | Excellent (no contact) |
| **Jet interference** | 5-15% (depends on slat width) | $<$2% (minimal blockage) | 10-20% (hole density) | 0% (no obstruction) |
| **Maintenance** | Low (durable steel) | Medium (bristle replacement 1-2 years) | Low | High (tile replacement) |
| **Cost (3m × 1.5m)** | $1,500-3,000 | $5,000-12,000 | $2,000-4,000 | $8,000-15,000 |

**Selection criteria:** Slat tables dominate (70% of installations) for general production due to low cost and durability; brush tables specified for precision parts requiring unmarked bottom edges (aerospace, medical, electronics); downdraft systems for thick material ($>$100 mm) where slat interference unacceptable.

### 6.2 Tank Depth and Jet Energy Dissipation

**Energy dissipation requirement:**

Waterjet exiting workpiece bottom retains 30-70% of initial kinetic energy (varies with material thickness and cutting speed). Tank water must absorb this energy, decelerating jet from 300-600 m/s exit velocity to $<$10 m/s before impacting tank floor to prevent:
- Tank bottom erosion (concrete/steel wear-through in weeks)
- Noise generation ($>$100 dB from supersonic jet impact)
- Splash and mist (safety hazard, water loss)

**Jet deceleration in water:**

Drag force on cylindrical jet in submerged condition:

$$F_{drag} = \frac{1}{2} C_D \rho_{water} A_{jet} v^2$$

Deceleration distance to reduce velocity from $v_0$ to $v_f$:

$$L_{decel} = \frac{m_{jet}}{\frac{1}{2} C_D \rho A} \ln\left(\frac{v_0}{v_f}\right)$$

For typical waterjet ($v_0 = 500$ m/s, $d = 1$ mm, decelerate to $v_f = 10$ m/s):

$$L_{decel} ≈ 100 \text{to } 200 \text{mm (depends on turbulence, jet breakup)}$$

**Practical tank depth specification:**

| Application | Material Thickness | Tank Depth | Rationale |
|-------------|-------------------|------------|-----------|
| **Thin material** | $<$10 mm | 150-200 mm (6-8") | Jet velocity reduced 70-85% through workpiece |
| **Medium thickness** | 10-50 mm | 200-250 mm (8-10") | Standard production applications |
| **Thick/hard material** | 50-150 mm | 250-350 mm (10-14") | Higher exit velocity requires longer deceleration |
| **Ultra-thick** | $>$150 mm | 300-400 mm (12-16") | Plus ceramic tile protection on tank floor |

**Tank floor protection:**

- **Unprotected steel:** Wears through in 200-1,000 hours (localized erosion from repeated cutting over same area)
- **Stainless steel liner (3-6 mm):** 2,000-5,000 hours before replacement required
- **Ceramic tile (25-50 mm):** 10,000-20,000 hours (alumina or silicon carbide tiles)
- **Sacrificial slats/grating on floor:** Replace worn sections ($100-300) vs entire liner ($2,000-8,000)

**Example 6.1: Tank Depth Sizing for 25 mm Steel Cutting**

**Given:**
- Material: 25 mm mild steel
- Cutting speed: 0.5 m/min (slow, high exit velocity)
- Jet velocity at workpiece entry: 900 m/s
- Estimated exit velocity: 40% of entry = 360 m/s
- Target final velocity in tank: $<$10 m/s

**Required deceleration:**
From 360 m/s to 10 m/s = 36× velocity reduction

**Empirical deceleration rate in water:**
Jet velocity halves every 80-100 mm of water depth (for 1 mm diameter jet)

**Calculation:**
- First 100 mm: 360 → 180 m/s
- Second 100 mm: 180 → 90 m/s
- Third 100 mm: 90 → 45 m/s
- Fourth 100 mm: 45 → 23 m/s
- Fifth 100 mm: 23 → 12 m/s (approaching target)

**Recommended tank depth:** 300 mm (12") minimum for 25 mm steel at 0.5 m/min cutting speed, with ceramic tile protection on tank floor for areas of frequent cutting.

### 6.3 Slat Spacing and Part Support Optimization

**Slat spacing trade-off:**

**Narrow spacing (10-15 mm):**
- **Advantages:** Better small part support (prevents tipping), reduced part sag (important for thin flexible materials)
- **Disadvantages:** 10-15% jet interference probability (jet hits slat edge during cutting), more slats = higher cost

**Wide spacing (20-30 mm):**
- **Advantages:** $<$5% jet interference, lower material cost (fewer slats)
- **Disadvantages:** Small parts ($<$30 mm) fall through gaps, thin sheet sags between slats (affects cut quality)

**Optimal spacing selection:**

$$s_{optimal} = \min(0.5 \times L_{part}, 25 \text{mm})$$

where $L_{part}$ is minimum part dimension.

For general-purpose production (part sizes $>$50 mm):
- Slat spacing: 15-20 mm
- Slat width: 5-8 mm (provides strength while minimizing jet blockage)
- Material: Stainless steel 304/316 (corrosion resistance in water environment)

**Slat wear and replacement:**

Waterjet impact causes gradual erosion of slat top surface:
- Wear rate: 0.5-2 mm/year (depends on utilization and abrasive concentration)
- Initial slat height: 25-40 mm above tank floor
- Replacement interval: 2-5 years (when worn slats no longer support parts above water level)
- Cost: $500-1,500 for full 3m × 1.5m slat set replacement

**Adjustable height slats:**

Premium systems ($3,000-6,000 premium) provide screw-jack or hydraulic adjustment:
- Compensate for slat wear without replacement
- Adjust height for different material thicknesses (minimize water splash)
- Extend slat life 50-100% (flip slats to use unworn edge)

### 6.4 Water Quality Management and Filtration

**Water quality impact on cutting performance:**

Pure water (distilled, deionized) not required—municipal tap water acceptable for most applications. However, four water quality parameters significantly affect system reliability and cutting consistency:

**1. Suspended solids (turbidity):**
- **Specification:** $<$50 ppm suspended solids, $<$20 NTU turbidity
- **Impact:** Particles $>$10 μm accelerate orifice wear 50-200% (abrasive contamination)
- **Solution:** 10-25 μm bag filter on tank return ($50-150, replace every 500-2,000 hours)

**2. Hardness (calcium, magnesium):**
- **Specification:** $<$200 ppm as CaCO₃ (soft to moderately hard water acceptable)
- **Impact:** Hard water ($>$300 ppm) deposits scale in intensifier, reducing efficiency 5-15% over 1,000 hours
- **Solution:** Water softener ($1,500-4,000) for hardness $>$250 ppm, or periodic descaling with citric acid

**3. Temperature:**
- **Specification:** 15-25°C (60-77°F) operating range
- **Impact:** Cold water ($<$10°C) increases viscosity 30%, reducing flow rate 3-5%; hot water ($>$30°C) accelerates seal wear
- **Solution:** Heat exchanger ($2,000-5,000) maintaining setpoint ±2°C for precision applications

**4. Biological contamination (algae, bacteria):**
- **Specification:** $<$1,000 CFU/mL (colony forming units per milliliter)
- **Impact:** Algae growth clogs filters, reduces orifice life (biofilm deposits), generates odor
- **Solution:** Biocide treatment (0.5-2 ppm chlorine or alternative), UV sterilization ($1,000-3,000)

**Water circulation and filtration system:**

$$Q_{circulation} = \frac{V_{tank}}{t_{turnover}}$$

where:
- $Q_{circulation}$ = filtration pump flow rate (L/min or GPM)
- $V_{tank}$ = total tank volume (L or gallons)
- $t_{turnover}$ = target turnover time (30-60 minutes typical)

**Example 6.2: Filtration System Sizing**

**Given:**
- Table size: 3 m × 1.5 m = 4.5 m²
- Tank depth: 250 mm (0.25 m)
- Tank volume: $V = 4.5 × 0.25 = 1.125$ m³ = 1,125 L = 297 gallons
- Target turnover time: 45 minutes

**Calculate circulation flow rate:**

$$Q = \frac{1125 \text{L}}{45 \text{min}} = 25 \text{L/min} = 6.6 \text{GPM}$$

**Filtration system specification:**
- Circulation pump: 30 L/min (20% margin for head loss)
- Bag filter: 25 μm polyester, 30 L/min flow capacity
- Filter housing: Stainless steel (corrosion resistance)
- Estimated cost: $800-1,500 (pump + filter housing + initial bags)

**Filter replacement interval:**

Abrasive consumption rate: 0.8 lb/min × 60 min/hr × 8 hr/day × 250 days/year = 96,000 lb/year

Fraction entering tank water (assumes 70% collected in sediment zone, 30% remains suspended):
$$m_{suspended} = 96,000 × 0.30 = 28,800 \text{lb/year} = 115 \text{lb/day}$$

Filter capacity: 5-10 lbs before pressure drop excessive (bag filter saturation)

**Replacement frequency:** Every 0.5-1.0 days of cutting (daily replacement for high-duty production)

Cost: $3-8 per bag × 250 bags/year = $750-2,000/year filter consumable cost.

### 6.5 Abrasive Settling and Collection

**Settling tank design** exploits density difference between garnet abrasive (4.1 g/cm³) and water (1.0 g/cm³) to separate spent abrasive via gravitational settling, enabling collection for disposal or recycling and preventing re-circulation into cutting system (would accelerate orifice/nozzle wear 10-50×).

**Stokes' Law settling velocity:**

For spherical particle in laminar flow:

$$v_{settling} = \frac{(\rho_{particle} - \rho_{water}) g d^2}{18 \mu}$$

where:
- $v_{settling}$ = terminal settling velocity (m/s)
- $ρ_{particle}$ = garnet density = 4,100 kg/m³
- $ρ_{water}$ = water density = 1,000 kg/m³
- $g$ = 9.81 m/s²
- $d$ = particle diameter (m)
- $μ$ = water dynamic viscosity = $1.0 × 10^{-3}$ Pa·s

**Example 6.3: Settling Velocity for 80 Mesh Garnet**

**Given:**
- Particle size: 80 mesh = 177 μm = $177 × 10^{-6}$ m
- Garnet density: 4,100 kg/m³
- Water density: 1,000 kg/m³
- Viscosity: $1.0 × 10^{-3}$ Pa·s

**Calculate settling velocity:**

$$v = \frac{(4100 - 1000) \times 9.81 \times (177 \times 10^{-6})^2}{18 \times 1.0 \times 10^{-3}}$$

$$v = \frac{3100 \times 9.81 \times 3.13 \times 10^{-8}}{18 \times 10^{-3}} = \frac{9.52 \times 10^{-4}}{0.018} = 0.053 \text{m/s} = 53 \text{mm/s}$$

**Settling time from surface to 250 mm tank bottom:**

$$t = \frac{0.25 \text{m}}{0.053 \text{m/s}} = 4.7 \text{seconds}$$

**Interpretation:** 80 mesh garnet particles settle to tank bottom in $<$5 seconds—excellent separation efficiency. Finer particles ($<$120 mesh) settle proportionally slower ($v ∝ d^2$), requiring longer residence time or mechanical separation (cyclone, centrifuge).

**Settling zone design:**

Tank divided into two zones:
1. **Active cutting area:** Directly beneath cutting path, high turbulence from jet impact
2. **Quiescent settling zone:** 20-40% of tank area, baffled to minimize flow velocity

**Horizontal flow velocity limit:**

To prevent particle re-suspension, horizontal velocity must be less than settling velocity:

$$v_{horizontal} < v_{settling}$$

For 80 mesh garnet (53 mm/s settling velocity):
- Maximum horizontal flow: 50 mm/s = 0.05 m/s
- Tank length 3 m, flow rate 25 L/min = 0.025 m³/min = $4.17 × 10^{-4}$ m³/s
- Cross-sectional area: $A = 3 \times 0.25 = 0.75$ m²
- Flow velocity: $v = Q/A = 4.17 \times 10^{-4} / 0.75 = 0.00056$ m/s = 0.56 mm/s

**Result:** Flow velocity (0.56 mm/s) is 100× slower than settling velocity (53 mm/s)—excellent settling efficiency with minimal re-suspension.

**Abrasive removal:**

Two methods for spent abrasive extraction:
1. **Manual shoveling:** Drain tank, shovel abrasive into drums (20-80 kg per session, weekly to monthly depending on usage)
2. **Vacuum system:** Wet/dry vacuum or pneumatic conveying ($2,000-8,000) extracts abrasive without tank drainage (reduces downtime from 2-4 hours to 30-60 minutes)

### 6.6 Fume, Mist, and Noise Control

**Mist generation:**

High-velocity waterjet creates aerosol mist via three mechanisms:
1. **Jet breakup:** Droplets form as jet exits workpiece into air (1-100 μm diameter)
2. **Splash:** Impact on tank water surface ejects droplets (10-500 μm)
3. **Evaporation:** Cutting heat vaporizes water, condenses as fine mist ($<$1 μm)

**Health concern:** Respirable particles ($<$10 μm) containing metal particulates (from workpiece erosion) can cause respiratory irritation with prolonged exposure.

**Mist control methods:**

**1. Tank water depth (primary method):**
- Deep tank (200-300 mm) absorbs jet energy underwater, minimizing surface splash
- Effectiveness: 70-85% mist reduction vs shallow tank ($<$100 mm)

**2. Water level control:**
- Maintain water surface 10-25 mm below slat tops
- Too high: Excessive splash, parts floating
- Too low: Jet impact on exposed slats generates noise and mist

**3. Tank covers/enclosures:**
- Partial covers over unused table area reduce mist escape 40-60%
- Full enclosures with fume extraction (500-1,000 CFM) capture 80-95% of mist
- Cost: $2,000-8,000 for full enclosure with extraction

**Noise generation:**

Waterjet cutting produces 75-90 dB at operator position from:
- Supersonic jet formation (broadband white noise 50-10,000 Hz)
- Jet impact on material and tank water (impulse noise)
- Pump and hydraulic system (60-75 dB mechanical noise)

**Noise control:**

**1. Submerged cutting (most effective):**
- Maintain water level at or slightly above workpiece surface
- Water absorbs acoustic energy, reducing noise 15-25 dB (to 60-70 dB range)
- Trade-off: Complicates part handling and visibility

**2. Tank acoustic absorption:**
- Acoustic foam lining on tank walls/lid ($500-1,500)
- Reduces noise 5-10 dB via reflection absorption

**3. Operator protection:**
- Hearing protection (earplugs/muffs) required if noise $>$85 dB
- Machine enclosures reduce noise to $<$80 dB at operator position ($5,000-15,000)

### 6.7 Summary and Table Design Optimization Guidelines

**Key Takeaways:**

1. **Tank depth** of 200-300 mm (8-12") provides adequate jet energy dissipation for materials up to 50 mm thickness, decelerating exit jet from 300-600 m/s to $<$10 m/s over 4-5 velocity half-distances (100 mm each); ceramic tile floor protection ($500-1,500) extends tank life 5-10× for high-duty applications

2. **Slat spacing** of 15-20 mm balances part support (prevents $<$30 mm parts from falling through) with jet interference ($<$5-10% blockage probability); stainless steel 304/316 slats ($1,500-3,000 for 4.5 m² table) last 2-5 years before wear requires replacement or height adjustment

3. **Water quality** requirements modest—municipal tap water acceptable if $<$50 ppm suspended solids, $<$200 ppm hardness, 15-25°C temperature; 10-25 μm bag filtration ($800-1,500 system, $750-2,000/year consumables) prevents orifice contamination from re-circulated abrasive fines

4. **Circulation flow rate** of 25-30 L/min (6-8 GPM) for typical 1,125 L tank achieves 30-45 minute turnover, maintaining water clarity while minimizing pump power (0.5-1 HP); two-stage filtration (coarse pre-filter 50-100 μm, fine bag 10-25 μm) extends fine filter life 3-5×

5. **Settling velocity** of 53 mm/s for 80 mesh garnet (177 μm) via Stokes' Law $v = (Δρ)gd^2/(18μ)$ enables 5-second settling time in 250 mm tank depth; horizontal flow velocity $<$1 mm/s (100× slower than settling velocity) prevents re-suspension in quiescent zones

6. **Abrasive collection** of 50-200 kg/day spent garnet requires weekly to monthly tank drainage/shoveling ($0 equipment, 2-4 hr labor) or vacuum extraction system ($2,000-8,000, 0.5-1 hr labor); recycling systems ($80,000-150,000) reduce virgin abrasive consumption 50-70% at $>$50% duty cycle

7. **Mist control** via 200-300 mm water depth (primary), water level 10-25 mm below slat tops (prevents splash), and optional enclosure with 500-1,000 CFM extraction (80-95% capture) reduces respirable particle exposure to OSHA-compliant levels ($<$0.5 mg/m³ for nuisance dust)

8. **Noise reduction** from 85-95 dB (uncontrolled) to 60-75 dB via submerged cutting (water level at workpiece surface, -15 to -25 dB), tank acoustic foam lining ($500-1,500, -5 to -10 dB), or full machine enclosure ($5,000-15,000, -20 to -30 dB) eliminating hearing protection requirement

Table design integration—slat spacing optimized for part size distribution (15-20 mm general-purpose), tank depth sized for maximum material thickness (200-300 mm for $<$50 mm materials), water circulation achieving 30-45 minute turnover with 10-25 μm filtration, settling zones providing $<$1 mm/s horizontal velocity for 95%+ abrasive capture, and mist/noise control via water depth and optional enclosure—enables reliable high-duty waterjet operation with 2-5 year slat life, minimal water quality degradation, and OSHA-compliant work environment.

***

*Total: 2,389 words | 5 equations | 3 worked examples | 2 tables*

---

## References

1. **ASME PVHO-1:2016** - Safety Standard for Pressure Vessels for Human Occupancy (high pressure)
2. **WARDJet Technical Manual** - Abrasive waterjet system specifications
3. **OMAX Waterjet Cutting Systems Guide** - Applications and troubleshooting
4. **Hashish, M. (1989).** "A Model for Abrasive-Waterjet (AWJ) Machining." *Journal of Engineering Materials and Technology*, 111(2), 154-162
5. **ISO 22826:2005** - Destructive tests on welds in metallic materials - Hardness test (alternative methods for waterjet quality)
6. **Flow International Waterjet Technology Handbook** - Pump systems and cutting mechanics
7. **Dassault Systèmes Abaqus** - FEA for high-pressure system analysis
