# Module 5 – Plasma Cutting Systems

## 5.2 Plasma Physics & Arc Theory

This section introduces the essential physics underpinning the plasma cutting arc: how the arc is initiated (gas breakdown), how it sustains (energy balance and conductivity), and how its properties (temperature, current density, heat flux) relate to practical cutting performance (pierce reliability, kerf shape, speed limits).

### 5.2.1 Gas Breakdown and Paschen’s Law (Arc Initiation)

An electric arc begins when the neutral process gas (air, N₂, H35, etc.) becomes sufficiently ionized to conduct. The breakdown voltage for a uniform field between parallel plates at pressure \(p\) and gap \(d\) is modeled by Paschen’s law:
$$
V_b = \frac{B\,p\,d}{\ln(A\,p\,d) - \ln\!\left[\ln\!\left(1+\frac{1}{\gamma_{se}}\right)\right]}
$$
where $A, B$ are gas-specific Townsend coefficients and $\gamma_{se}$ is the effective secondary electron emission coefficient of the cathode. Typical values (air, near 1 bar): $A\approx 112~\text{(1/(Pa}\cdot\text{m))}$, $B\approx 2737~\text{V/(Pa}\cdot\text{m)}$, $\gamma_{se}\sim 0.01$–0.1. In torches, a pilot arc (HF/HV or blow-back start) locally reduces the effective gap and raises the local electric field to force breakdown at controlled locations.

Practical implications:
- Higher pressure or larger gap increases $p d$ and thus $V_b$ until the Paschen minimum is passed.
- Electrode/cathode conditioning ($\gamma_{se}$) strongly influences start reliability.
- HF start couples a high-frequency field to seed electrons; blow-back start creates a transient micro-gap to trigger breakdown without RF emissions.

### 5.2.2 Arc Column, Energy Balance, and Temperature

After initiation, the arc forms a constricted, highly conductive plasma column. Power delivered is \(P=V I\). A fraction \(\eta\) of this power couples thermally into the workpiece and kerf; the remainder is lost to radiation and convective transport.
$$
q'' \approx \frac{\eta \, V I}{A_{spot}}
$$
where \(q''\) is incident heat flux and \(A_{spot}\) is the effective arc spot area on the work. Typical cutting arcs reach core temperatures \(T \sim 10{,}000\text{–}20{,}000\,\text{K}\), enabling rapid melting/vaporization and ejecting molten metal with the assist gas jet. Torch design (nozzle orifice and gas swirl) constricts the arc to increase current density and heat flux.

Rule-of-thumb parameters (atmospheric air plasma, industrial torches):
- Current \(I\): 30–200 A (handheld), up to 400+ A (mechanized)
- Arc voltage \(V\): 90–180 V (depends on length and gas)
- Thermal coupling \(\eta\): 0.25–0.45 (material/process dependent)
- Spot diameter: 0.8–2.0 mm (nozzle/orifice dependent)

### 5.2.3 Conductivity, Current Density, and Arc Constriction

The plasma’s electrical conductivity \(\sigma\) increases strongly with temperature. In atmospheric-pressure arcs used for cutting, \(\sigma\) typically reaches \(5\times10^4\) to \(1\times10^5\,\text{S/m}\). Current density \(J\) in the constricted core can exceed \(10^7\,\text{A/m}^2\), producing strong electromagnetic pinching that further constricts the arc (self-magnetic effect). Nozzle design and gas swirl stabilize this constriction; excessive erosion or incorrect gas settings reduce constriction, lowering heat flux and cut quality.

Design levers:
- Smaller nozzle orifice → higher current density (within thermal limits of nozzle/cathode)
- Optimized gas swirl → stabilizes arc attachment and reduces wander
- Correct standoff → maintains voltage and effective arc length in the designed window

### 5.2.4 Ionization, Transport, and Arc Voltage–Length Relation

Ionization fraction and transport set the plasma’s macroscopic conductivity. A simple equilibrium indicator is the Saha relation (monatomic gas):
$$
\frac{n_e n_i}{n_0} = \left(\frac{2\pi m_e k T}{h^2}\right)^{3/2}\! \frac{2 g_i}{g_0}\; e^{-E_i/(kT)}
$$
where \(n_e, n_i, n_0\) are electron/ion/neutral number densities, \(g_i,g_0\) are statistical weights, and \(E_i\) is first ionization energy. Although cutting arcs are not perfectly equilibrated, this shows why \(T\sim10\text{–}20\,\text{kK}\) produces large ionization fractions.

Electron transport links microphysics to conductivity:
$$
\lambda = \frac{1}{\sqrt{2}\,\pi d^2 n},\quad \nu \approx \frac{\bar{v}}{\lambda},\quad \mu_e = \frac{e}{m_e \nu},\quad \sigma = n_e e \mu_e
$$
with $\lambda$ mean free path, $\nu$ collision frequency, $\bar{v}$ thermal speed, $\mu_e$ mobility. Higher $T$ (larger $n_e$, $\mu_e$) raises $\sigma$, reducing arc resistivity.

Arc voltage scales with effective length \(L\) and near-electrode falls:
$$
V \approx E_{arc}\, L + V_{cath} + V_{an}
$$
where \(E_{arc}\) (V/mm) depends on gas, current, and constriction. Torch standoff primarily modifies \(L\) and thus \(V\); too large a standoff → higher \(V\), unstable attachment, poor cut quality.

### 5.2.5 Worked Examples

#### Example 1 – Paschen Breakdown in Air (Pilot Gap)

Given air at $p = 1.0\,\text{bar} = 1.01\times10^5\,\text{Pa}$ and a pilot gap $d = 0.25\,\text{mm} = 2.5\times10^{-4}\,\text{m}$, $\gamma_{se}=0.05$, $A=112\,\text{(1/(Pa}\cdot\text{m))}$, $B=2737\,\text{V/(Pa}\cdot\text{m)}$. Compute $V_b$.

Compute $p d = 1.01\times10^5 \times 2.5\times10^{-4} = 25.25\,\text{Pa}\cdot\text{m}$.
$\ln(A p d) = \ln(112\times25.25) = \ln(2828) = 7.946$.
$\ln(1+1/\gamma_{se}) = \ln(1+20) = \ln(21) = 3.045$ → $\ln[\ln(1+1/\gamma_{se})] = \ln(3.045) = 1.113$.
Denominator: $7.946 - 1.113 = 6.833$.
Numerator: $B p d = 2737\times25.25 = 69{,}083\,\text{V}$.
Thus $V_b \approx 69{,}083 / 6.833 = 10{,}114\,\text{V}$ (≈10 kV). HF/HV pilot circuits readily provide this; blow‑back designs reduce effective $d$ to lower $V_b$ without RF.

#### Example 2 – Heat Flux to Workpiece (Order of Magnitude)

Mechanized torch at \(I=120\,\text{A}\), \(V=140\,\text{V}\) → \(P=16.8\,\text{kW}\). Assume \(\eta=0.35\), spot diameter 1.2 mm → \(A_{spot}=\pi (0.6\times10^{-3})^2 = 1.13\times10^{-6}\,\text{m}^2\).
$$
q'' = \frac{0.35\times16.8\times10^3}{1.13\times10^{-6}} \approx 5.2\times10^{9}\,\text{W/m}^2
$$
This gigawatt‑per‑square‑meter heat flux supports high cutting speeds; reductions in \(\eta\) or increased spot size lower \(q''\), degrading kerf quality and increasing dross.

#### Example 3 – Energy per Unit Length and Cut Speed

For a given material/thickness, a recipe may require energy per unit length \(E'\) to ensure full penetration. With \(V=120\,\text{V}\), \(I=100\,\text{A}\) and target \(E' = 1500\,\text{J/mm}\):
$$
v_{cut} = \frac{V I}{E'} = \frac{12{,}000\,\text{W}}{1500\,\text{J/mm}} = 8\,\text{mm/s} = 0.48\,\text{m/min}
$$
Increasing current or improving \(\eta\) allows higher \(v_{cut}\); excessive speed lowers \(E'\), causing bevel/dross.

#### Example 4 – Arc Voltage vs. Standoff (Effect on Power)

If \(E_{arc} = 30\,\text{V/mm}\) (gas/nozzle dependent) and standoff increases \(\Delta L = 0.5\,\text{mm}\), arc voltage rises by \(\Delta V \approx 15\,\text{V}\). At \(I=120\,\text{A}\), added power \(\Delta P = I \Delta V = 1.8\,\text{kW}\) mostly heats the arc/torch, not the kerf, degrading efficiency; maintain correct standoff.

### 5.2.6 Acceptance Checklist (Physics Tie‑ins)
- Start reliability: Pilot arc breakdown margin verified across expected \(p d\) variation (gas pressure ±10%, standoff ±0.2 mm)
- Thermal coupling: \(\eta\) within process window for material thickness; cut energy per unit length meets recipe
- Constriction: Nozzle/orifice condition and gas swirl verified for stable, centered arc (no wander), correct standoff voltage

### 5.2.7 Typical Parameters by Gas (Guidance)

Indicative values at cutting conditions (ballpark – tune per torch/vendor data):
- Air: \(\sigma \sim 5\times10^4\,\text{S/m}\) at \(T\sim 12\text{–}16\,\text{kK}\); \(E_{arc} \sim 25\text{–}35\,\text{V/mm}\)
- Nitrogen (N₂): \(\sigma \sim 6\times10^4\,\text{S/m}\); \(E_{arc} \sim 20\text{–}30\,\text{V/mm}\)
- Oxygen (O₂): \(\sigma \sim 4\times10^4\,\text{S/m}\); \(E_{arc} \sim 20\text{–}30\,\text{V/mm}\)
- Argon/Hydrogen (e.g., H35): \(\sigma \sim 8\times10^4\,\text{S/m}\); \(E_{arc} \sim 15\text{–}25\,\text{V/mm}\)

Higher \(\sigma\) and lower \(E_{arc}\) (at a given current) generally imply lower voltage for the same standoff, reducing waste heat in the arc/torch and improving thermal efficiency at the kerf.

### 5.2.8 Commissioning & Safety Cross‑Links

- Verify pilot start window: gas pressure, standoff, and HF (or blow‑back) settings achieve breakdown with margin (reference Paschen analysis).
- Set standoff control (height control) to maintain arc voltage setpoint \(V\) consistent with target \(L\) and \(E_{arc}\).
- Interlocks: HF start inhibit near sensitive electronics; ensure grounding/shielding per Module 4; confirm gas flow/pressure interlocks before arc enable.

***
Notes: Values are indicative; use OEM torch data where available. For detailed EMI/EMC constraints during HF start and PWM drive emissions, see Module 13.

***
Cross‑References: Module 4 (Controller/Drive requirements for HF start emissions and interlocks); Module 1 (Thermal expansion considerations under plasma process heat);

---

## References

1. **AWS C5.1:2018** - Recommended Practices for Plasma Arc Cutting
2. **Hypertherm Powermax Series Technical Manual** - Plasma system specifications
3. **ISO 9013:2017** - Thermal cutting - Classification of thermal cuts - Geometrical product specification
4. **NFPA 51B:2019** - Standard for Fire Prevention During Welding, Cutting, and Other Hot Work
5. **Paton, B.E. (1962).** *Plasma Arc Welding*. Consultants Bureau
6. **Miller Electric Plasma Cutting Guide** - Applications and troubleshooting
7. **Lincoln Electric Plasma Cutting Handbook** - Process fundamentals
