## 2. Physical Principles: Optical Waveguiding in Water Jets

### 2.1 Total Internal Reflection Physics

Total internal reflection (TIR) forms the physical basis for water-jet guided laser technology, enabling a liquid column to function as an optical waveguide despite its cylindrical geometry, microscopic diameter (0.1-0.2 mm), and exposure to atmospheric conditions. Understanding the optical physics governing TIR, coupling efficiency, and power transmission losses enables quantitative prediction of system performance and optimization of nozzle design, laser beam parameters, and water jet stability.

**Refractive Index and Light Propagation:**

Light propagates at different velocities in different media according to the material's refractive index:

$$n = \frac{c}{v}$$

where:
- $n$ = refractive index (dimensionless)
- $c$ = speed of light in vacuum = 299,792,458 m/s
- $v$ = speed of light in medium (m/s)

**Refractive indices at 1.06 μm wavelength (fiber laser):**
- Water: $n_1 = 1.330$ (pure DI water at 20°C)
- Air: $n_2 = 1.000$ (standard atmospheric pressure)
- Fused silica (optical fiber): $n = 1.450$
- Sapphire (nozzle orifice): $n = 1.760$

When light crosses an interface from higher to lower refractive index medium (water to air), Snell's law governs refraction:

$$n_1 \sin(\theta_1) = n_2 \sin(\theta_2)$$

As incident angle $\theta_1$ increases, refracted angle $\theta_2$ approaches 90° (ray emerges parallel to interface). At the **critical angle** $\theta_c$, $\theta_2 = 90°$:

$$\sin(\theta_c) = \frac{n_2}{n_1} = \frac{1.000}{1.330} = 0.7519$$

$$\theta_c = \arcsin(0.7519) = 48.75°$$

For incident angles **exceeding 48.75°**, Snell's law predicts $\sin(\theta_2) > 1$, physically impossible—no refracted ray exists, 100% of light reflects back into water. This is **total internal reflection**.

**Example 2.1: TIR Verification for Fiber Laser Beam**

**Given:**
- Laser beam propagating in water jet at 55° from surface normal
- Water refractive index: $n_1 = 1.330$
- Air refractive index: $n_2 = 1.000$

**Determine:** Does TIR occur?

**Solution:**

Critical angle: $\theta_c = 48.75°$

Incident angle: $\theta_1 = 55°$

Since $\theta_1 = 55° > \theta_c = 48.75°$, **total internal reflection occurs**.

**Verify using Snell's law:**

$$\sin(\theta_2) = \frac{n_1}{n_2} \sin(\theta_1) = \frac{1.330}{1.000} \sin(55°) = 1.330 \times 0.8192 = 1.089$$

Since $\sin(\theta_2) > 1$ (impossible), no refracted ray exists—**confirms TIR**.

### 2.2 Numerical Aperture and Acceptance Cone

The **numerical aperture (NA)** quantifies the light-gathering capability of an optical waveguide—the maximum cone half-angle of incident light that will propagate via total internal reflection.

**Derivation:**

Consider a ray entering the water jet at angle $\theta_{input}$ from the jet axis. For this ray to propagate via TIR after reflecting from the water-air boundary, the incident angle at the boundary must exceed $\theta_c$.

Geometric analysis yields:

$$NA = n_{core} \sin(\theta_{accept}) = \sqrt{n_{core}^2 - n_{cladding}^2}$$

For water jet (core) in air (cladding):

$$NA = \sqrt{1.330^2 - 1.000^2} = \sqrt{1.769 - 1.000} = \sqrt{0.769} = 0.877$$

The acceptance half-angle:

$$\theta_{accept} = \arcsin\left(\frac{NA}{n_{air}}\right) = \arcsin\left(\frac{0.877}{1.000}\right) = 61.3°$$

**Full acceptance cone:** $2 \times 61.3° = 122.6°$

**Comparison to Conventional Optical Fiber:**

| Waveguide Type | Core Index | Cladding Index | NA | Acceptance Angle |
|----------------|------------|----------------|-----|------------------|
| **Single-mode fiber** | 1.465 | 1.450 | 0.14 | 8.0° half-angle |
| **Multi-mode fiber** | 1.470 | 1.450 | 0.22 | 12.7° half-angle |
| **Water jet in air** | 1.330 | 1.000 | 0.88 | 61.3° half-angle |

The water jet's extraordinarily high NA (0.88 vs. 0.14-0.22 for glass fiber) enables efficient coupling from fiber lasers with typical beam divergence 5-15° full angle—well within the 122.6° acceptance cone.

**Example 2.2: Coupling Efficiency from Fiber Laser Output**

**Given:**
- Fiber laser output: 100 μm core diameter, NA = 0.15, 2 kW power
- Output beam divergence: $\theta_{divergence} = 2 \times \arcsin(0.15) = 17.3°$ full angle
- Water jet NA = 0.877, acceptance cone = 122.6°

**Determine:** What fraction of laser power couples into water jet (geometric consideration only)?

**Solution:**

Laser beam divergence (17.3°) << water jet acceptance (122.6°)

**Geometric coupling efficiency:** Nearly 100% of rays within laser divergence cone satisfy TIR condition in water jet.

**Actual coupling efficiency:** 75-85% in practice (losses from Fresnel reflection at coupling interface, beam alignment errors, jet surface ripples)

### 2.3 Fresnel Reflection Losses

When laser light enters the water jet from air (or from focusing optics), **Fresnel reflection** occurs at the interface—a portion of incident power reflects rather than transmits, reducing coupling efficiency.

**Fresnel Reflection Coefficient (Normal Incidence):**

$$R = \left(\frac{n_1 - n_2}{n_1 + n_2}\right)^2$$

**For air-to-water interface:**

$$R = \left(\frac{1.000 - 1.330}{1.000 + 1.330}\right)^2 = \left(\frac{-0.330}{2.330}\right)^2 = 0.0201 = 2.01\%$$

**2.01% of incident laser power reflects** at the air-water interface, reducing transmitted power to 97.99%.

**Anti-Reflection (AR) Coating:**

Sapphire pressure windows in optical coupling heads typically feature AR coatings optimized for 1.06 μm wavelength, reducing reflection to <0.5% per surface:

$$R_{AR} < 0.005 \quad (0.5\%)$$

For coupling head with sapphire window (2 surfaces: air-to-sapphire, sapphire-to-water):

**Total transmission:** $T = (1 - R_1) \times (1 - R_2) = 0.995 \times 0.995 = 0.990 = 99.0\%$

### 2.4 Scattering and Absorption Losses in Water

As laser light propagates through the water jet, two mechanisms cause power attenuation: **absorption** (photon energy converts to heat in water molecules) and **scattering** (light deflects from propagation direction due to particulates, dissolved gases, or density fluctuations).

**Beer-Lambert Law:**

$$P(L) = P_0 \times e^{-\alpha L}$$

where:
- $P(L)$ = power after propagation distance $L$
- $P_0$ = initial power
- $\alpha$ = attenuation coefficient (m⁻¹)
- $L$ = propagation length (m)

**Attenuation Coefficient Components:**

$$\alpha = \alpha_{absorption} + \alpha_{scattering}$$

**At 1.06 μm wavelength in pure water:**
- Absorption: $\alpha_{abs} = 0.12$ m⁻¹ (water molecules absorb infrared)
- Scattering (pure DI water): $\alpha_{scat} = 0.02$ m⁻¹ (density fluctuations)
- **Total:** $\alpha = 0.14$ m⁻¹

**For practical WGL systems (filtered tap water, <1 ppm particulates):**
- Total attenuation: $\alpha = 0.3$ to $0.8$ m⁻¹ (higher due to residual particulates)

**Example 2.3: Power Loss Over 100 mm Jet Length**

**Given:**
- Initial laser power: $P_0 = 2,000$ W (coupled into jet)
- Jet length from nozzle to workpiece: $L = 100$ mm = 0.10 m
- Attenuation coefficient: $\alpha = 0.5$ m⁻¹ (typical for filtered water)

**Calculate power reaching workpiece:**

$$P(L) = P_0 \times e^{-\alpha L} = 2000 \times e^{-0.5 \times 0.10}$$

$$P(L) = 2000 \times e^{-0.05} = 2000 \times 0.9512 = 1,902 \text{ W}$$

**Power loss:** $2000 - 1902 = 98$ W (4.9% over 100 mm)

**Interpretation:** Short jet length (<100 mm standoff) minimizes scattering losses. Longer standoffs (>200 mm) incur 10-15% losses, reducing cutting effectiveness.

### 2.5 Jet Stability and Straightness Requirements

For efficient TIR propagation, the water jet must remain straight within angular tolerance—jet curvature or vibration causes ray angles to exceed the critical angle locally, breaking TIR and losing laser power.

**Jet Straightness Criterion:**

$$\theta_{deviation} < \theta_c - \theta_{beam,max}$$

where:
- $\theta_{deviation}$ = maximum angular deviation of jet from straight line
- $\theta_c = 48.75°$ (critical angle)
- $\theta_{beam,max}$ = maximum ray angle in beam (half of divergence angle)

For typical fiber laser with 10° full-angle divergence:

$$\theta_{beam,max} = 5°$$

**Required jet straightness:**

$$\theta_{deviation} < 48.75° - 5° = 43.75°$$

**In practice:** Jet straightness maintained to **<0.5°** over coupling length (3-10 mm) ensures margin for TIR even with high-divergence input beams.

**Factors Affecting Jet Stability:**
1. **Pressure ripple:** <±0.5% required (accumulator dampens intensifier pulsations)
2. **Nozzle orifice quality:** Ra <0.1 μm surface finish prevents turbulence nucleation
3. **Dissolved gas content:** <50 ppm prevents cavitation bubbles disrupting flow
4. **Water temperature stability:** ±2°C (thermal expansion affects refractive index and jet diameter)

**Jet Coherence Length:**

The distance over which water jet remains straight and cylindrical before breakup:

$$L_{coherent} = K \times d_{orifice}$$

where:
- $K = 800$ to $1,200$ for pure waterjet (no abrasive)
- $d_{orifice}$ = nozzle diameter (mm)

**For 0.12 mm orifice:**

$$L_{coherent} = 1000 \times 0.12 = 120 \text{ mm}$$

WGL systems operate at standoff distances 5-50 mm, well within coherence length, ensuring stable optical waveguide.

### 2.6 Power Density and Thermal Effects

Laser power absorbed in water (2-5% of beam power) generates heat, raising water temperature and potentially causing thermal lensing (refractive index change) or vapor bubble formation.

**Heat Generation:**

$$\dot{Q} = P_{laser} \times f_{absorbed}$$

where $f_{absorbed} = 0.02$ to $0.05$ (2-5% absorption over 50-100 mm path length)

For 2 kW laser:

$$\dot{Q} = 2000 \times 0.03 = 60 \text{ W}$$

**Temperature Rise in Water Flow:**

$$\Delta T = \frac{\dot{Q}}{\dot{m} \times c_p}$$

where:
- $\dot{Q}$ = heat load (W)
- $\dot{m}$ = mass flow rate (kg/s)
- $c_p$ = specific heat of water = 4,186 J/(kg·K)

**Example 2.4: Water Temperature Rise Calculation**

**Given:**
- Laser power: 2 kW
- Absorbed fraction: 3%
- Water flow rate: 0.15 L/min = 0.0025 kg/s
- Specific heat: 4,186 J/(kg·K)

**Calculate temperature rise:**

Heat load: $\dot{Q} = 2000 \times 0.03 = 60$ W

$$\Delta T = \frac{60}{0.0025 \times 4186} = \frac{60}{10.47} = 5.7 \text{ K}$$

**Temperature rise: 5.7°C**

**Interpretation:** Modest temperature rise (<10°C) acceptable—does not cause significant refractive index change ($\Delta n < 0.001$) or boiling (water exits nozzle at 900 m/s, insufficient residence time for heat diffusion).

### 2.7 Coupling Efficiency: Combined Loss Analysis

**Total transmission efficiency** from laser fiber output to workpiece:

$$\eta_{total} = \eta_{Fresnel} \times \eta_{scattering} \times \eta_{alignment}$$

**Typical Values:**

1. **Fresnel transmission (AR-coated optics):** $\eta_{Fresnel} = 0.99$ (99%)

2. **Scattering transmission (100 mm jet):** $\eta_{scattering} = e^{-0.5 \times 0.10} = 0.95$ (95%)

3. **Alignment efficiency (geometric coupling):** $\eta_{alignment} = 0.85$ (85%, accounts for beam-to-jet centering errors, jet diameter variations, surface ripples)

**Combined efficiency:**

$$\eta_{total} = 0.99 \times 0.95 \times 0.85 = 0.80 = 80\%$$

**Typical WGL systems achieve 75-85% coupling efficiency**—for 2 kW laser source, 1.5-1.7 kW reaches workpiece.

**Loss Budget Summary:**

| Loss Mechanism | Typical Loss | Cumulative Efficiency |
|----------------|--------------|----------------------|
| Initial laser power | 0% | 100% (2,000 W) |
| Fresnel reflection (AR-coated) | 1% | 99% (1,980 W) |
| Scattering (100 mm jet) | 5% | 94% (1,881 W) |
| Alignment/coupling errors | 15% | 80% (1,600 W) |
| **Final power at workpiece** | **20% total loss** | **80% (1,600 W)** |

### 2.8 Design Implications

Understanding optical physics enables quantitative optimization:

1. **Minimize standoff distance:** Use 5-20 mm typical (vs. 50-100 mm possible) → reduces scattering losses from 10-15% to 2-5%

2. **Maintain jet straightness:** Pressure stability <±0.5%, nozzle surface finish Ra <0.1 μm → ensures TIR margin >40°

3. **Water purity critical:** Filter to <1 ppm particulates, degas to <50 ppm dissolved gases → reduces scattering coefficient from 0.8 to 0.3 m⁻¹

4. **AR coatings essential:** Uncoated sapphire window loses 7-8% per surface (14-16% total for 2 surfaces), AR coating reduces to 1% total

5. **Flow rate balances cooling vs. efficiency:** Higher flow (>0.20 L/min) improves cooling but requires larger orifice (reduces jet velocity, compromises cutting performance); optimal 0.10-0.15 L/min

Mastery of TIR physics, numerical aperture, Fresnel losses, and scattering mechanisms enables prediction of coupling efficiency (75-85% achievable) and identification of loss mechanisms for optimization—foundational to specifying laser power requirements and nozzle design parameters covered in subsequent sections.

***

---

## References

1. **ISO 11553 Series** - Safety of machinery - Laser processing machines
2. **ANSI Z136.1-2014** - Safe Use of Lasers
3. **ISO 9013:2017** - Thermal cutting - Classification of thermal cuts
4. **Steen, W.M. & Mazumder, J. (2010).** *Laser Material Processing* (4th ed.). Springer
5. **Flow International Waterjet Technology Handbook** - Hybrid system applications
6. **TRUMPF TruLaser Technical Documentation** - Combined processing systems
7. **Hashish, M. (2014).** "Hybrid Waterjet-Laser Cutting Technology." *Journal of Manufacturing Processes*
