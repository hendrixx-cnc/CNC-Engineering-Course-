## 5. Beam Delivery and Optics: Fiber Coupling, Collimation, and Focusing Systems

### 5.1 Process Fiber: Power Transmission from Source to Cutting Head

The process fiber (also called delivery fiber or transport fiber) transmits laser output from source to cutting head via flexible fiber optic cable, enabling simplified machine design compared to rigid mirror-arm beam delivery required for CO₂ lasers. Process fiber selection balances power handling capability (avoiding optical damage), beam quality preservation (maintaining M² through fiber bends), and focusing performance (core diameter determines minimum achievable spot size).

**Process Fiber Construction:**

1. **Core:** Step-index multimode fiber (50-600 μm diameter) made from ultra-pure fused silica (OH content <1 ppm)
2. **Cladding:** Low-index polymer or fluorine-doped silica (125-1,000 μm diameter)
3. **Buffer:** Acrylate or polyimide protective coating
4. **Jacket:** Armored cable with stainless steel monocoil or Kevlar reinforcement

**Numerical Aperture (NA):**

The fiber NA defines maximum acceptance angle for light:

$$NA = \sin(\theta_{max}) = \sqrt{n_{core}^2 - n_{clad}^2}$$

where:
- $θ_{max}$ = half-angle of acceptance cone
- $n_{core}$ = core refractive index (typically 1.46 for silica)
- $n_{clad}$ = cladding refractive index (1.45 for typical fiber, giving NA = 0.12-0.22)

**Typical values:** NA = 0.12 for premium cutting fibers (tight spot capability), NA = 0.22 for high-power fibers (relaxed coupling tolerance).

### 5.2 Power Density Limits and Fiber Damage Mechanisms

**Optical Damage Threshold:**

Maximum safe power density in fiber core:

$$I_{max} = \frac{I_{damage}}{SF}$$

where:
- $I_{max}$ = maximum operating intensity (kW/mm²)
- $I_{damage}$ = damage threshold (100-200 kW/mm² for bulk silica, 50-100 kW/mm² at fiber endface)
- $SF$ = safety factor (typically 2-3×)

**Power density in fiber:**

$$I_{fiber} = \frac{4P}{\pi d_{core}^2}$$

**Example 5.1: Process Fiber Sizing for 6 kW Laser**

**Given:**
- Laser power: $P = 6,000$ W
- Damage threshold (endface): $I_{damage} = 80$ kW/mm²
- Safety factor: $SF = 2.5$
- Operating limit: $I_{max} = 80 / 2.5 = 32$ kW/mm²

**Calculate minimum core diameter:**

$$d_{core} = \sqrt{\frac{4P}{\pi I_{max}}} = \sqrt{\frac{4 \times 6000}{\pi \times 32,000}} = \sqrt{\frac{24,000}{100,531}} = \sqrt{0.239} = 0.489 \text{ mm}$$

**Selection:** Use 500 μm or 600 μm core diameter (standard sizes).
- 500 μm: $I = 30.6$ kW/mm² (96% of limit, tight margin)
- 600 μm: $I = 21.2$ kW/mm² (66% of limit, recommended for reliability)

**Fiber length and transmission loss:**

Attenuation in ultra-pure silica fiber at 1,070 nm:

$$P_{out} = P_{in} \cdot \exp(-\alpha \cdot L)$$

where $α = 0.5-1.5$ dB/km (negligible for typical 5-15 m cable length).

**Example:** 10 m fiber at 1 dB/km: Loss = 0.01 dB = 0.23% (99.8% transmission)

**Bend radius limits:**

Minimum bend radius to prevent loss and mode distortion:
- Static bend: $R_{min} = 10 \times d_{core}$ (5 mm for 500 μm fiber)
- Dynamic bend (moving axis): $R_{min} = 20 \times d_{core}$ (10 mm for 500 μm fiber)

Violating minimum bend radius causes:
- Increased loss (light leaking into cladding)
- M² degradation (mode coupling between fundamental and higher-order modes)
- Stress-induced fiber fracture after 10,000-100,000 cycles

### 5.3 Collimator Design and Function

The collimator converts diverging fiber output into parallel beam suitable for focusing lens input. Located at cutting head inlet, the collimator determines collimated beam diameter $D$ which in turn affects focused spot size.

**Collimator Equation:**

$$D_{collimated} = 2 f_{coll} \cdot NA_{fiber}$$

where:
- $D_{collimated}$ = collimated beam diameter (mm)
- $f_{coll}$ = collimator focal length (typically 50-200 mm)
- $NA_{fiber}$ = numerical aperture of process fiber

**Example 5.2: Collimated Beam Diameter Calculation**

**Given:**
- Process fiber: 200 μm core, NA = 0.15
- Collimator focal length: $f_{coll} = 125$ mm

**Calculate collimated beam diameter:**

$$D = 2 \times 125 \times 0.15 = 37.5 \text{ mm}$$

**Analysis:** Larger collimator focal length produces larger collimated beam diameter, which enables smaller focused spot (Equation 5.5) but requires correspondingly larger focusing lens aperture (increased cost and aberrations).

**Collimator Types:**

1. **Achromatic doublet:** Two-element lens correcting chromatic aberration (focal shift with wavelength)
   - Advantage: Maintains focus over ±5 nm wavelength drift
   - Disadvantage: Higher cost ($200-600 vs. $50-150 for singlet)

2. **Aspheric singlet:** Single lens with non-spherical surface profile
   - Advantage: Low cost, compact
   - Disadvantage: Wavelength-dependent focus (acceptable for fiber lasers with <0.5 nm linewidth)

3. **Reflective collimator (off-axis parabola):**
   - Advantage: No chromatic aberration, handles >10 kW power
   - Disadvantage: Bulky, alignment-sensitive, expensive ($1,000-3,000)

### 5.4 Focusing Optics: Lens Selection and Spot Size Calculation

**Focused Spot Diameter:**

The diffraction-limited focused spot diameter:

$$d_{spot} = \frac{4 \lambda f M^2}{\pi D}$$

where:
- $d_{spot}$ = spot diameter at 1/e² intensity (μm)
- $λ$ = wavelength (1.07 μm for fiber laser)
- $f$ = focusing lens focal length (mm)
- $M^2$ = beam quality factor (1.05-1.3 for fiber lasers)
- $D$ = collimated beam diameter (mm)

**f-number relationship:**

$$f/\# = \frac{f}{D}$$

Lower f-number (shorter focal length or larger beam) produces smaller spot but shorter working distance and depth of focus.

**Example 5.3: Spot Size vs. Focal Length Trade-off**

**Given:**
- Wavelength: $λ = 1.07$ μm
- Beam quality: $M^2 = 1.15$
- Collimated diameter: $D = 30$ mm
- Compare $f = 100$ mm vs. $f = 200$ mm lenses

**Calculate spot diameters:**

For $f = 100$ mm:
$$d_{spot} = \frac{4 \times 1.07 \times 100 \times 1.15}{\pi \times 30} = \frac{492.2}{94.25} = 5.2 \text{ μm (theoretical)}$$

For $f = 200$ mm:
$$d_{spot} = \frac{4 \times 1.07 \times 200 \times 1.15}{\pi \times 30} = \frac{984.4}{94.25} = 10.4 \text{ μm (theoretical)}$$

**Trade-off analysis:**
- $f = 100$ mm: Smaller spot (2× higher power density), shorter working distance (less collision clearance), shorter depth of focus (tighter height tolerance)
- $f = 200$ mm: Larger spot (lower power density), longer working distance (better for thick material and spatter protection), longer depth of focus

**Practical cutting spot sizes:** Add 3-5× to theoretical values due to:
- Focal position offset (focus set 1-3 mm into material for through-cutting)
- Thermal blooming from plasma and vapor
- Aberrations in lens system
- Protective window contamination

Typical practical spots: 100-150 μm for thin material (<3 mm), 200-300 μm for thick material (>10 mm).

### 5.5 Depth of Focus and Rayleigh Length

**Rayleigh Length:**

Distance over which focused beam remains within √2 of minimum diameter:

$$z_R = \frac{\pi d_{spot}^2}{4 \lambda M^2}$$

**Depth of focus (DOF):**

$$DOF = 2 z_R = \frac{\pi d_{spot}^2}{2 \lambda M^2}$$

**Example 5.4: Depth of Focus Calculation**

**Given:**
- Theoretical spot: $d_{spot} = 10$ μm
- Wavelength: $λ = 1.07$ μm
- Beam quality: $M^2 = 1.15$

**Calculate depth of focus:**

$$DOF = \frac{\pi \times (10)^2}{2 \times 1.07 \times 1.15} = \frac{314.16}{2.46} = 127.7 \text{ μm} = 0.13 \text{ mm}$$

**Practical implications:**
- Tight focus (10 μm spot) requires height control within ±0.06 mm to maintain <10% power density variation
- Looser focus (50 μm spot) provides 25× longer DOF (3.2 mm), relaxing height control to ±1.5 mm

For cutting through-thickness material, focal position typically set at 30-60% of material thickness (e.g., 2 mm into 5 mm plate) to balance top and bottom edge quality.

### 5.6 Lens Materials and Coatings

**Lens Substrate Materials:**

| Material | Transmission @ 1.07 μm | Thermal Conductivity (W/m·K) | Cost Factor | Application |
|----------|------------------------|-------------------------------|-------------|-------------|
| **Fused silica** | >99.5% | 1.4 | 1× | Standard <6 kW systems |
| **BK7 glass** | >99% | 1.1 | 0.5× | Economy <3 kW systems |
| **Zinc selenide (ZnSe)** | >99.5% | 18 | 3× | High-power >10 kW (better thermal dissipation) |
| **Sapphire** | >99% | 25 | 5× | Ultra-high-power >15 kW, protective windows |

**Anti-Reflection (AR) Coatings:**

Multi-layer dielectric coatings reduce surface reflection from 4% (uncoated) to <0.2% (AR-coated) at 1,070 nm wavelength.

**Reflection loss for two surfaces (lens front and back):**

Without AR coating: Loss = $1 - (0.96)^2 = 7.8\%$
With AR coating: Loss = $1 - (0.998)^2 = 0.4\%$

For 6 kW laser, uncoated lens absorbs ~470 W vs. 24 W for AR-coated lens—absorbed power causes thermal lensing (focal shift) and eventually catastrophic damage.

**Coating durability:**

- Ion-assisted deposition (IAD): Hard, durable, resists contamination
- Evaporated coatings: Lower cost, more susceptible to moisture and spatter damage
- V-coat (single wavelength): >99.8% transmission at 1,070 nm, degrades ±20 nm off-peak
- Broadband: 99-99.5% transmission over 1,030-1,100 nm, robust to wavelength drift

### 5.7 Protective Windows and Contamination Management

**Function:**

Protective window (also called cover glass or debris shield) seals optical pathway from fume, spatter, and assist gas pressure, while transmitting laser beam with minimal loss. Located at cutting head nozzle interface, 10-50 mm from workpiece.

**Specifications:**

- Material: Fused silica or sapphire, 3-6 mm thickness
- Coating: AR-coated both sides (>99.5% transmission)
- Mounting: O-ring seal with positive gas pressure (prevents fume infiltration)
- Replacement interval: 200-2,000 hours depending on material, cutting parameters, and gas selection

**Contamination Effects:**

Spatter or fume deposition on protective window causes:
1. **Absorption heating:** Localized hot spots reaching 200-400°C
2. **Thermal lensing:** Focal position shifts 0.5-2 mm (degrades cut quality)
3. **Thermal stress fracture:** Window cracks from thermal gradient (sudden failure)

**Contamination rate factors:**
- Oxygen cutting of mild steel: High spatter, window life 200-500 hours
- Nitrogen cutting of stainless: Moderate spatter, window life 500-1,000 hours
- Nitrogen cutting of aluminum: Low spatter, window life 1,000-2,000 hours

**Monitoring and replacement:**

- Visual inspection every 50-100 operating hours
- Replace when visible contamination covers >5% of aperture
- Emergency replacement: Keep 2-3 spare windows on-site ($50-200 each)

### 5.8 Optical Alignment and Beam Centering

**Alignment Requirements:**

Laser beam must remain centered in collimator, focusing lens, and nozzle orifice within ±0.1-0.2 mm throughout cutting head motion. Misalignment causes:
- Asymmetric kerf (one side burned, other incomplete)
- Nozzle spatter accumulation (beam clips nozzle edge)
- Reduced power transmission (vignetting losses)

**Alignment Procedure:**

1. **Initial optical axis definition:**
   - Install alignment laser or visible pointer coaxial with process fiber
   - Mark beam center at collimator, lens, and nozzle locations

2. **Collimator adjustment:**
   - Three-axis kinematic mount (X, Y translation; tip/tilt)
   - Center fiber output on collimator aperture using burn paper 1 m downstream

3. **Focusing lens centering:**
   - Adjust lens mount to center collimated beam
   - Verify circular spot at focus using burn paper or CCD camera

4. **Nozzle centering verification:**
   - Pierce test on thin material (0.5-1 mm) at low power
   - Inspect hole symmetry; adjust if oval or offset
   - Acceptance: <0.1 mm eccentricity for precision cutting

**Thermal drift compensation:**

Optical mounts expand with temperature change (aluminum: 23 μm/m/°C). For cutting heads with 200 mm optical path at ±10°C ambient variation:
$$\Delta L = 200 \times 23 \times 10^{-6} \times 10 = 0.046 \text{ mm}$$

High-precision systems use invar (1.2 μm/m/°C) or carbon fiber mounts to minimize thermal drift.

### 5.9 Summary and Design Guidelines

**Key Takeaways:**

1. **Process fiber core diameter** must limit power density below 30-50 kW/mm² (safety factor 2-3× from 80-100 kW/mm² damage threshold); 6 kW laser requires ≥500 μm core for safe operation

2. **Collimated beam diameter** $D = 2 f_{coll} \cdot NA$ scales with collimator focal length and fiber NA; typical 125 mm collimator with NA = 0.15 fiber produces 37.5 mm beam diameter

3. **Focused spot diameter** $d_{spot} = 4\lambda f M^2 / (\pi D)$ decreases with shorter focal length or larger collimated beam; typical 100-200 mm focal lengths produce 5-10 μm theoretical spots (multiply by 3-5× for practical cutting spot)

4. **Depth of focus** $DOF = \pi d_{spot}^2 / (2\lambda M^2)$ requires tight height control for small spots: 10 μm spot demands ±0.06 mm tolerance, 50 μm spot relaxes to ±1.5 mm

5. **Lens material and AR coatings** critical for thermal management: uncoated fused silica absorbs 7.8% (470 W for 6 kW laser) causing thermal lensing, while AR-coated lens absorbs <0.5% (30 W) maintaining stable focus

6. **Protective window contamination** from spatter deposits causes absorption heating, thermal lensing (0.5-2 mm focal shift), and thermal fracture; replacement interval 200-2,000 hours depending on material and process

7. **Optical alignment** requires beam centering within ±0.1-0.2 mm in collimator, lens, and nozzle using kinematic mounts; misalignment >0.3 mm causes asymmetric cuts, nozzle damage, and power loss

8. **Bend radius limits** for process fiber prevent mode distortion: static bends >10× core diameter (5 mm for 500 μm fiber), dynamic bends >20× core diameter to achieve 100,000+ cycle lifetime

Proper beam delivery system design balances fiber power handling, focusing performance (spot size and working distance), and optical protection (windows, coatings, alignment stability) to achieve reliable high-quality cutting with maximum component lifetime and minimal maintenance intervention.

***

*Total: 1,920 words | 10 equations | 4 worked examples | 1 table*

---

## References

1. **ISO 11553 Series** - Safety of machinery - Laser processing machines
2. **ANSI Z136.1-2014** - Safe Use of Lasers
3. **IEC 60825-1:2014** - Safety of laser products - Equipment classification
4. **Steen, W.M. & Mazumder, J. (2010).** *Laser Material Processing* (4th ed.). Springer
5. **IPG Photonics Fiber Laser Systems Manual** - Industrial laser specifications
6. **Trumpf Laser Technology Handbook** - Laser cutting and welding applications
7. **ISO 9013:2017** - Thermal cutting - Classification of thermal cuts
8. **OSHA Technical Manual Section III: Chapter 6** - Laser Hazards
