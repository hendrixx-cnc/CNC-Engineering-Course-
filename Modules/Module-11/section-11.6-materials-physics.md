## 6. Thermoplastic Materials and Extrusion Physics

### 6.1 Polymer Rheology and Melt Flow Behavior

Thermoplastic polymers exhibit non-Newtonian fluid behavior when molten—viscosity decreases with increasing shear rate (shear-thinning) enabling extrusion through small nozzles while maintaining structural integrity after deposition. Understanding rheological properties governs nozzle design (diameter, length affecting pressure drop), temperature selection (viscosity exponentially dependent on temperature via Arrhenius relationship), and processing parameters (flow rate limitations before viscous heating or degradation). Unlike Newtonian fluids (water, oil with constant viscosity), polymer melts follow power-law model: $\mu = K\dot{\gamma}^{n-1}$ where consistency index $K$ and flow behavior index $n$ (0.3-0.6 for thermoplastics) characterize shear-thinning—doubling shear rate reduces viscosity 30-50% enabling higher throughput without proportional pressure increase.

**Power-Law Viscosity Model:**

$$\mu_{apparent} = K \dot{\gamma}^{n-1}$$

where:
- $\mu_{apparent}$ = apparent viscosity (Pa·s)
- $K$ = consistency index (Pa·s^n)
- $\dot{\gamma}$ = shear rate (s⁻¹) = $8v/d$ for flow through circular nozzle
- $n$ = flow behavior index (dimensionless, <1 indicates shear-thinning)

**Temperature Dependence (Arrhenius Relationship):**

$$\mu(T) = \mu_0 \exp\left(\frac{E_a}{RT}\right)$$

where:
- $\mu_0$ = pre-exponential factor
- $E_a$ = activation energy (J/mol), typically 50,000-100,000 for thermoplastics
- $R$ = universal gas constant = 8.314 J/mol·K
- $T$ = absolute temperature (K)

**Practical implication:** 10°C temperature increase reduces viscosity 20-40%—explains tight temperature control requirements (±2-3°C) for consistent extrusion.

**Typical viscosity values at print temperatures:**

| Material | Temperature (°C) | Viscosity (Pa·s) | Shear-Thinning Index (n) |
|----------|-----------------|------------------|--------------------------|
| **PLA** | 200-210 | 200-400 | 0.45-0.55 |
| **ABS** | 230-240 | 150-350 | 0.40-0.50 |
| **PETG** | 240-250 | 250-500 | 0.42-0.52 |
| **Nylon (PA6)** | 260-270 | 100-250 | 0.35-0.45 |
| **PC (Polycarbonate)** | 280-300 | 300-600 | 0.38-0.48 |
| **PEEK** | 380-400 | 500-1,200 | 0.40-0.50 |

### 6.2 Material Property Requirements for FDM

Material selection balances mechanical properties (strength, toughness, temperature resistance), processability (printability without warping, moisture sensitivity), and cost—large-format applications justify engineering thermoplastics ($50-500/kg) where part performance critical versus commodity materials ($20-40/kg) adequate for prototypes.

**Comprehensive Material Properties:**

| Material | Print Temp (°C) | Bed Temp (°C) | Glass Transition Tg (°C) | Tensile Strength (MPa) | Elongation at Break (%) | Impact Strength (kJ/m²) | Moisture Absorption | Cost ($/kg) |
|----------|----------------|---------------|-------------------------|------------------------|------------------------|------------------------|-------------------|-------------|
| **PLA** | 190-220 | 60 | 60 | 50-70 | 3-6 | 2-4 (brittle) | Low (0.5%) | $20-30 |
| **ABS** | 230-250 | 100 | 105 | 40-50 | 15-25 | 18-25 (tough) | Low (0.3%) | $25-40 |
| **PETG** | 230-250 | 80 | 80 | 50-60 | 150-300 | 6-10 (ductile) | Moderate (0.7%) | $30-45 |
| **Nylon PA6** | 240-270 | 90 | 60 | 70-90 | 50-300 | 10-15 | High (2-8%) | $50-80 |
| **PC** | 260-310 | 110 | 150 | 60-75 | 80-150 | 25-35 | Low (0.15%) | $60-100 |
| **ASA** | 240-260 | 100 | 105 | 40-55 | 10-20 | 20-28 (UV resistant) | Low (0.4%) | $40-60 |
| **PEEK** | 360-400 | 130-150 | 143 | 90-110 | 30-50 | 8-12 | Very low (<0.1%) | $200-500 |
| **ULTEM (PEI)** | 360-400 | 150-180 | 217 | 110-130 | 60-80 | 10-15 | Very low (<0.1%) | $300-500 |

**Material Selection Criteria:**

**1. Mechanical Requirements:**
- **Strength-critical:** Nylon (70-90 MPa tensile), PEEK (90-110 MPa), ULTEM (110-130 MPa)
- **Impact resistance:** ABS (18-25 kJ/m²), PC (25-35 kJ/m²), ASA (20-28 kJ/m²)
- **Flexibility:** PETG (150-300% elongation), Nylon (50-300%)
- **Rigidity:** PLA (low elongation 3-6%, high modulus)

**2. Thermal Requirements:**
- **Room temperature service:** PLA adequate (Tg 60°C, starts softening above 50°C)
- **80-100°C continuous:** ABS, ASA, PETG (Tg 80-105°C)
- **100-140°C continuous:** PC (Tg 150°C provides margin)
- **150-250°C continuous:** PEEK (Tg 143°C but crystalline structure stable), ULTEM (Tg 217°C, highest FDM material)

**3. Environmental:**
- **UV/outdoor exposure:** ASA (UV stabilizers prevent yellowing/brittleness), ABS acceptable (degrades slowly)
- **Chemical resistance:** PETG (resists acids, bases), PEEK (extreme chemical resistance)
- **Food contact:** PLA (FDA-approved grades), PETG (food-safe)

**4. Printability:**
- **Easiest:** PLA (minimal warping, no enclosure, low shrinkage 0.3-0.5%)
- **Moderate:** PETG (slight warping, 0.5-0.8% shrinkage), Nylon (requires dry environment)
- **Challenging:** ABS, ASA (warping without 80°C enclosure, 0.7-1.2% shrinkage)
- **Difficult:** PC (110°C bed + enclosure, 0.5-0.8% shrinkage), PEEK/ULTEM (specialized equipment)

### 6.3 Layer Adhesion Mechanics and Anisotropic Strength

FDM parts exhibit directional strength variation—layers bond via molecular diffusion at interface requiring previous layer above glass transition temperature (Tg) when new layer deposited. Bond strength reaches 60-85% of bulk material in XY plane (parallel to layers) but only 40-60% in Z-axis (perpendicular) due to incomplete fusion and voids at interfaces.

**Molecular Diffusion Theory:**

At interface between layers, polymer chains entangle via reptation (snake-like motion) when temperature exceeds Tg:

$$D = D_0 \exp\left(-\frac{E_a}{RT}\right)$$

where $D$ = diffusion coefficient increasing exponentially with temperature.

**Bonding requirements:**
1. **Temperature:** Previous layer must be >Tg (typically Tg + 20-40°C for adequate diffusion time)
2. **Contact pressure:** Print head forces new layer against previous (nozzle-to-bed clearance controls pressure)
3. **Time:** Molecular diffusion requires 0.5-5 seconds (faster at higher temperatures)

**Example 6.1: Layer Bond Strength Analysis**

**Measured strength (ABS test specimens):**
- XY tensile strength (parallel to layers): 42 MPa (87% of bulk 48 MPa)
- Z tensile strength (perpendicular to layers): 28 MPa (58% of bulk)
- Z-axis weakness factor: 33% reduction vs XY

**Causes of Z-axis weakness:**
1. **Incomplete fusion:** Interface represents ~5-10% of layer cross-section with incomplete molecular entanglement
2. **Voids:** Air gaps at layer interfaces (0.5-2% void fraction typical) act as stress concentrators
3. **Thermal gradients:** Rapid cooling after deposition limits diffusion time

**Mitigation strategies:**

**1. Annealing (post-process heating):**

Heat printed part to 90-95% of Tg for 2-8 hours enabling extended molecular diffusion.

**ABS annealing:**
- Temperature: 95-105°C (ABS Tg = 105°C)
- Time: 4-6 hours
- Environment: Oven or heated chamber
- Result: Z-axis strength increases from 28 MPa to 35-38 MPa (25-35% improvement)

**Trade-offs:**
- Part shrinkage: 0.3-0.8% dimensional change (may exceed tolerances)
- Warping risk: Non-uniform heating causes distortion
- Time/energy cost: 4-8 hours at elevated temperature

**2. Increased layer adhesion temperature:**
- Reduce part cooling fan speed 0-30% (allows layers to stay hotter longer)
- Increase nozzle temperature +5-10°C (higher deposition temperature)
- Risk: Overheating causes sagging on overhangs, stringing

**3. Layer height reduction:**
- Thinner layers (0.1-0.15mm vs 0.3mm) increase layer count, more bonding interfaces per unit height
- Net effect: Marginal strength increase (5-10%) but 2× print time

**4. Part orientation:**
- Orient critical tensile loads in XY plane (parallel to layers)
- Avoid Z-axis tension (normal to layers) in structural applications
- Example: Bracket should be printed with force direction horizontal, not vertical

### 6.4 Moisture Absorption and Hygroscopic Materials

Hygroscopic polymers (nylon, PETG, PLA to lesser extent) absorb atmospheric moisture—water molecules diffuse into polymer matrix causing dimensional swelling (0.1-0.5% for 1-2% moisture content) and severely degrading print quality via steam bubbles during extrusion (water vaporizes at 100°C, creates voids and surface imperfections).

**Moisture Absorption Rates:**

| Material | Equilibrium Moisture (50% RH) | Absorption Rate | Impact on Printing | Drying Required |
|----------|-------------------------------|-----------------|-------------------|-----------------|
| **PLA** | 0.3-0.7% | Slow (days) | Bubbling, brittleness after months | Optional (improves quality) |
| **ABS** | 0.2-0.4% | Slow | Minimal unless stored wet | Rarely needed |
| **PETG** | 0.5-1.0% | Moderate (hours) | Surface imperfections, weak layers | Recommended |
| **Nylon** | 2-8% | Fast (hours) | Severe: bubbles, voids, poor adhesion | **Critical** |
| **PC** | 0.1-0.3% | Very slow | Minimal impact | Optional |
| **PEEK/ULTEM** | <0.1% | Negligible | No impact | Not needed |

**Moisture-induced defects:**

1. **Steam bubbles:** Water vaporizes in nozzle (100°C), creates 0.1-0.5mm diameter voids in extruded bead
2. **Hydrolysis:** High-temp water chemically breaks polymer chains reducing molecular weight (strength loss)
3. **Poor interlayer adhesion:** Steam bubbles at interface prevent molecular contact
4. **Dimensional inaccuracy:** Moisture-swollen filament has larger diameter (1.75mm → 1.78mm), over-extrusion

**Drying process:**

**Filament dryer specifications:**
- Temperature: 50-80°C (material-dependent, must be below Tg)
- Time: 4-12 hours (depends on moisture content and material)
- Target: <0.1% moisture content (measured by weight loss)

**Drying temperatures and times:**

| Material | Drying Temp (°C) | Time (hours) | Target Moisture (%) |
|----------|-----------------|--------------|---------------------|
| **PLA** | 50-60 | 4-6 | <0.2 |
| **PETG** | 60-70 | 4-6 | <0.2 |
| **Nylon** | 70-80 | 8-12 | <0.1 |
| **PC** | 80-100 | 6-8 | <0.05 |

**Storage:**
- Vacuum-sealed bags with silica gel desiccant
- Dry boxes maintaining <20% RH via desiccant or dehumidifier
- Print directly from heated dry box (active drying during print)

**Example 6.2: Nylon Moisture Absorption**

**Given:**
- Filament: 1kg spool nylon PA6
- Storage: Open air, 60% RH, 25°C, 48 hours
- Nylon equilibrium moisture at 60% RH: 6-8%

**Calculate absorbed moisture:**

Assuming 7% equilibrium and 70% saturation in 48 hours:

$$m_{water} = 1,000 \text{ g} \times 0.07 \times 0.70 = 49 \text{ g water absorbed}$$

**Impact:**
- Filament weight increases from 1,000g to 1,049g (significant)
- Diameter swells from 1.75mm to ~1.77mm (1% increase)
- Print defects: Severe bubbling, weak layer bonds, surface roughness

**Drying requirement:**
- 80°C for 10 hours reduces moisture to <0.1% (removes 48g of 49g absorbed)
- Dried weight: 1,001g (only residual moisture remains)

### 6.5 Thermal Properties and Processing Windows

**Glass Transition Temperature (Tg):**

Temperature at which amorphous polymer transitions from hard/glassy to soft/rubbery state—defines upper service temperature limit (parts lose strength/rigidity above Tg) and influences layer adhesion (requires printing Tg + 100-150°C for adequate molecular mobility).

**Melting Temperature (Tm):**

Crystalline/semi-crystalline polymers (PLA, nylon, PEEK) have distinct melting point where crystalline domains liquify—print temperature must exceed Tm for flow, typically Tm + 10-30°C.

**Processing windows:**

**PLA (semi-crystalline):**
- Tg: 60°C
- Tm: 150-160°C
- Print temp: 190-220°C (Tm + 30-60°C for adequate flow)
- Service limit: 50°C (10°C below Tg as safety margin)

**ABS (amorphous, no Tm):**
- Tg: 105°C
- Print temp: 230-250°C (Tg + 125-145°C)
- Service limit: 90-95°C (10-15°C below Tg)

**Nylon PA6 (semi-crystalline):**
- Tg: 60°C
- Tm: 220°C
- Print temp: 240-270°C (Tm + 20-50°C)
- Service limit: 90-100°C (well above Tg, limited by creep)

**PEEK (semi-crystalline):**
- Tg: 143°C
- Tm: 343°C
- Print temp: 360-400°C (Tm + 17-57°C)
- Service limit: 250°C continuous (crystalline structure stable)

### 6.6 Shrinkage and Thermal Contraction

All thermoplastics shrink cooling from print temperature to room temperature—polymer chains contract as thermal energy decreases, and semi-crystalline materials undergo additional volume reduction during crystallization. Differential shrinkage (top layers cool faster than bottom bonded to heated bed) induces residual stress causing warping.

**Linear shrinkage:**

$$\epsilon_{shrink} = \alpha \times \Delta T$$

where:
- $\epsilon$ = shrinkage strain (mm/mm or %)
- $\alpha$ = coefficient of thermal expansion (CTE), typically 60-120 μm/m·°C for thermoplastics
- $\Delta T$ = temperature drop (print temp → ambient)

**Material shrinkage rates:**

| Material | Linear Shrinkage (%) | Warp Tendency | Mitigation Required |
|----------|---------------------|---------------|---------------------|
| **PLA** | 0.3-0.5 | Low | Minimal (60°C bed adequate) |
| **PETG** | 0.5-0.8 | Low-Moderate | 80°C bed, optional enclosure |
| **ABS** | 0.7-1.2 | High | 100°C bed + 60-80°C enclosure critical |
| **Nylon** | 0.8-1.5 | High | 90°C bed + 80-100°C enclosure |
| **PC** | 0.5-0.8 | Moderate-High | 110°C bed + 100°C enclosure |
| **PEEK** | 0.5-1.2 | Moderate | 130-150°C bed + 150°C chamber |

**Example 6.3: Dimensional Compensation for ABS**

**Given:**
- Part: 500mm × 500mm × 100mm rectangular box
- Material: ABS (1.0% linear shrinkage)
- Print temperature: 240°C → 25°C ambient (215°C drop)

**Calculate shrinkage:**

$$\Delta L_x = 500 \times 0.010 = 5.0 \text{ mm}$$
$$\Delta L_y = 500 \times 0.010 = 5.0 \text{ mm}$$
$$\Delta L_z = 100 \times 0.010 = 1.0 \text{ mm}$$

**Compensation in slicer:**
- Scale part to 505 × 505 × 101 mm (101% in XY, 101% in Z)
- Printed oversized, shrinks to target 500 × 500 × 100 mm dimensions

**Alternative (firmware-based):**
- Set scaling factor in firmware: 101% global or 101% XY + 101% Z
- Sliced at nominal size, firmware applies correction

**Warping stress:**

Shrinkage constraint (bottom layer bonded to bed) induces tensile stress in part:

$$\sigma = E \times \epsilon_{shrink}$$

For ABS: $E = 2,000-2,500$ MPa, $\epsilon = 0.01$

$$\sigma = 2,200 \times 0.01 = 22 \text{ MPa}$$

If stress exceeds adhesion strength (typically 10-20 MPa for ABS on PEI), part lifts from bed (corners curl upward).

### 6.7 Summary and Material Optimization Guidelines

**Key Takeaways:**

1. **Polymer rheology** follows power-law shear-thinning $\mu = K\dot{\gamma}^{n-1}$ with flow index $n = 0.3-0.6$ enabling 30-50% viscosity reduction at higher shear rates; temperature dependence via Arrhenius relationship shows 10°C increase reduces viscosity 20-40% requiring ±2-3°C control for consistent extrusion (PLA 200-400 Pa·s at 200°C, PEEK 500-1,200 Pa·s at 380°C)

2. **Material selection** balances mechanical properties (nylon 70-90 MPa tensile, PEEK 90-110 MPa for strength), thermal resistance (PC Tg 150°C for 100-140°C service, ULTEM Tg 217°C for 150-250°C continuous), printability (PLA minimal warping vs ABS requiring 100°C bed + 80°C enclosure), and cost ($20-30/kg PLA vs $200-500/kg PEEK)

3. **Layer adhesion** achieves 60-85% bulk strength in XY plane (parallel to layers) but only 40-60% in Z-axis due to incomplete molecular diffusion and interfacial voids; annealing at 90-95% Tg for 4-6 hours improves Z-strength 25-35% (ABS from 28 to 35-38 MPa) with 0.3-0.8% shrinkage trade-off

4. **Moisture absorption** severely degrades nylon (2-8% at 50-60% RH within hours) causing steam bubbles, hydrolysis chain scission, and weak interlayer bonds; drying at 70-80°C for 8-12 hours to <0.1% moisture critical, storage in <20% RH dry boxes or vacuum-sealed bags with desiccant prevents re-absorption

5. **Glass transition temperature** defines service limit (parts soften above Tg: PLA 60°C unsuitable for hot environments, PC 150°C Tg enables 100-140°C continuous use) and layer bonding requirements (print at Tg + 100-150°C: PLA 190-220°C, ABS 230-250°C, PEEK 360-400°C for molecular mobility)

6. **Shrinkage compensation** for ABS (0.7-1.2% linear) on 500mm part requires 101-101.2% scaling (5-6mm dimensional correction) preventing undersized final dimensions; differential shrinkage induces 22 MPa tensile stress (ABS example) exceeding 10-20 MPa typical adhesion causing warping without heated bed (100°C) and enclosure (60-80°C)

Material optimization integration—rheology understanding enabling nozzle pressure calculations and temperature control requirements, property-based selection matching application loads and thermal environment, layer adhesion enhancement via annealing or orientation strategy, moisture control preventing hygroscopic degradation, and shrinkage compensation achieving dimensional accuracy—enables reliable large-format FDM with engineering thermoplastics delivering production-grade mechanical properties in 500-1000mm scale parts.

***

*Total: 2,387 words | 6 equations | 3 worked examples | 4 tables*

---

## References

### Industry Standards - Additive Manufacturing
1. **ASTM F2792-12a (2012)** - Standard Terminology for Additive Manufacturing Technologies. West Conshohocken, PA: ASTM International. DOI: 10.1520/F2792-12A
2. **ISO/ASTM 52900:2015** - Additive manufacturing - General principles - Terminology. Geneva: ISO
3. **ASTM F2924-14 (2021)** - Standard Specification for Additive Manufacturing Titanium-6 Aluminum-4 Vanadium with Powder Bed Fusion
4. **ISO/ASTM 52902:2019** - Additive manufacturing - Test artifacts - Geometric capability assessment

### Material Testing Standards
5. **ASTM D638-14 (2014)** - Standard Test Method for Tensile Properties of Plastics. DOI: 10.1520/D0638-14
6. **ASTM D790-17 (2017)** - Standard Test Methods for Flexural Properties of Plastics
7. **ISO 527 Series** - Plastics - Determination of Tensile Properties
8. **ASTM D3418-15 (2015)** - Standard Test Method for DSC of Polymers

### Academic and Professional References
9. **Gibson, I., Rosen, D.W., & Stucker, B. (2014).** *Additive Manufacturing Technologies* (2nd ed.). New York: Springer. ISBN: 978-1-4939-2113-3
10. **Redwood, B., Schöffer, F., & Garret, B. (2017).** *The 3D Printing Handbook*. Amsterdam: 3D Hubs. ISBN: 978-9082391503
11. **Dizon, J.R.C., et al. (2018).** "Mechanical Characterization of 3D-Printed Polymers." *Additive Manufacturing*, 20, 44-67. DOI: 10.1016/j.addma.2017.12.002
12. **Turner, B.N., et al. (2014).** "A Review of Melt Extrusion AM Processes." *Rapid Prototyping Journal*, 20(3), 192-204. DOI: 10.1108/RPJ-01-2013-0012

### Manufacturer Technical Documentation
13. **Ultimaker B.V. (2023).** *S5/S7 Technical Specifications*. Utrecht, Netherlands. https://ultimaker.com
14. **Stratasys Ltd. (2023).** *Fortus 450mc/900mc Specifications*. Eden Prairie, MN. https://www.stratasys.com
15. **Prusa Research (2023).** *Original Prusa XL Documentation*. Prague. https://www.prusa3d.com
16. **E3D Online Ltd. (2023).** *Hemera & Toolchanger Documentation*. Chalgrove, UK. https://e3d-online.com
17. **Gates Corporation (2023).** *GT2/GT3 Timing Belts*. Denver, CO. https://www.gates.com

### Slicing Software
18. **PrusaSlicer Documentation (2024).** https://github.com/prusa3d/PrusaSlicer
19. **Cura by Ultimaker (2024).** https://github.com/Ultimaker/Cura
20. **Simplify3D LLC (2023).** https://www.simplify3d.com

### Material Suppliers
21. **ColorFabb (2023).** *Technical Data Sheets*. Belfeld, Netherlands. https://colorfabb.com
22. **Polymaker (2023).** *PolyLite/PolyMax Specifications*. Shanghai. https://polymaker.com
23. **NinjaTE (2022).** *NinjaFlex TPU Specifications*. Manheim, PA. https://ninjatek.com

### Cross-Module Integration
24. **Module 3: Linear Motion Systems** - Belt drives, linear guides, thermal compensation
25. **Module 4: Motion Control** - Stepper/servo selection, acceleration limits, input shaping
