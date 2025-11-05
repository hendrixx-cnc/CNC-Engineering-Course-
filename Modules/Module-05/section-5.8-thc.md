# Module 5 – Plasma Cutting Systems

## 5.8 Torch Height Control (THC)

THC keeps the torch standoff (arc length) in its optimum window during cutting by regulating Z based on arc voltage. The key enablers are: (1) a calibrated relation between arc voltage and standoff, (2) robust signal conditioning to reject noise/EMI, and (3) a gated, well‑tuned control loop that avoids “diving” at kerf transitions and over surface defects.

### 5.8.1 Arc Voltage vs. Standoff (Calibration)

Over a small operating window, the arc voltage is approximately affine with effective arc length \(L\):
$$
V(L) \approx E_{arc}\, L + V_0
\quad \Rightarrow \quad \frac{dV}{dL} \approx E_{arc}\; (>0)
$$
where \(E_{arc}\) (V/mm) depends on gas, current, and constriction (typical 15–35 V/mm; see Section 5.2). Calibration establishes \(dV/dL\) and the setpoint \(V_{set}\) for the desired standoff.

Calibration procedure (at cutting current/gas):
1) Jog Z to a safe standoff above the plate; enable pilot, then transfer to cutting arc on scrap.
2) Execute a slow straight move (e.g., 300 mm/min) while stepping Z by ±0.2 mm about the nominal standoff; log \(V\) and \(L\).
3) Fit \(V\) vs. \(L\) in the linear region to obtain \(dV/dL\) and intercept \(V_0\).
4) Choose \(V_{set} = V(L_{opt})\) for target standoff \(L_{opt}\).

Notes:
- Recalibrate when changing gas/current/nozzle, or if voltage drift >5% is observed.
- Height mapping (probing or capacitive sensor) can pre‑compensate plate waviness so the THC works on small residuals.

### 5.8.2 Signal Conditioning and Anti‑Noise Measures

Sources: HF start, PWM drive switching, arc instability over kerf edges, EMI/ground loops. Use a combination of electrical design (shielded cabling, proper grounding per Module 13) and digital filtering.

Filters (discrete‑time, sample period \(T_s\)):
- First‑order IIR low‑pass: \(y[k]= \alpha y[k{-}1] + (1{-}\alpha) x[k]\), \(\alpha = e^{-2\pi f_c T_s}\)
- Second‑order low‑pass (biquad) for steeper roll‑off; cutoff \(f_c\) 5–15 Hz
- Median filter (3–5 samples) to reject spikes; optional notch at a known vibration mode (e.g., 120 Hz)

Guidelines:
- Choose \(f_c\) high enough (\(\sim\)5–10 Hz) to follow slow Z corrections but low enough to attenuate arc noise.
- Synchronize sampling with the motion controller; avoid aliasing of PWM/EMI.
- Clamp “Arc OK” before closing the loop; gate THC by feedrate (e.g., enable only above 50% cut speed).

### 5.8.3 THC Control Loop

Define voltage error \(e_V = V_{set} - V\). Convert to height error using the calibration slope \(dV/dL\):
$$
e_L = \frac{e_V}{dV/dL} = e_V \cdot \frac{dL}{dV}
$$
A PI controller in height coordinates (mm) generates a Z correction:
$$
\Delta L_{cmd}(t) = K_p \, e_L(t) + K_i \int e_L(t)\, dt
$$
Discretized with period $T_s$: $\Delta L_{cmd}[k] = K_p e_L[k] + K_i T_s \sum e_L$. Convert to Z velocity/position commands subject to rate/saturation limits:
- Rate limit $|\dot{L}| \le r_{max}$ to prevent dive on holes/kerf
- Deadband on $e_V$ (e.g., ±0.5–1.0 V) to avoid chatter
- Anti‑dive: detect sudden $V$ rise (kerf crossing) → freeze THC for a dwell time
- Gating: THC active only when Arc OK, feed > threshold, and not during corners/pierces

Tuning recipe:
1) Start with \(K_i=0\); increase \(K_p\) until a clean response without oscillation (target 1–2 s settling to ±0.1 mm).
2) Add a small \(K_i\) to remove steady offset (integrator windup protected with clamp or back‑calc).
3) Verify with step disturbances (holes, plate warp) and high‑speed segments.

### 5.8.4 Worked Examples

#### Example 1 – Voltage–Height Calibration and Correction
Calibration yields \(dV/dL = 25\,\text{V/mm}\). THC measures \(V=132\,\text{V}\) while \(V_{set}=130\,\text{V}\) → \(e_V=-2\,\text{V}\) (arc is long). Height error \(e_L = -2/25 = -0.08\,\text{mm}\). With \(K_p = 0.8\), command \(\Delta L_{cmd} = -0.064\,\text{mm}\) (move down); integrator trims residual.

#### Example 2 – Filter and Loop Trade‑off
Sample \(x[k]\) at 200 Hz. Choose first‑order low‑pass with \(f_c=10\,\text{Hz}\) → \(\alpha = e^{-2\pi (10) (1/200)} \approx 0.73\). Noise at >50 Hz is attenuated >10 dB while loop lag \(\approx 16\,\text{ms}\). Increase \(K_p\) modestly to compensate; verify no oscillation with a 120 Hz notch if a mechanical mode is excited.

### 5.8.5 Acceptance & Commissioning

- Calibration repeatability: two runs give \(dV/dL\) within ±10% and \(V_{set}\) within ±2 V
- Enable gating: THC active only above configured feed and with Arc OK asserted
- Step disturbance over scrap hole: no dive; recovery to ±0.1 mm within 1.5 s
- Ruler test (alternating narrow/wide cuts): kerf and dross within recipe; no corner over‑correction
- EMI robustness: no controller resets/glitches during HF start; voltage signal within expected RMS noise band

Commissioning record should capture: calibration plot (\(V\)–\(L\)), chosen \(K_p, K_i\), filter settings, gating thresholds, and acceptance results.


---

## References

1. **AWS C5.1:2018** - Recommended Practices for Plasma Arc Cutting
2. **Hypertherm Powermax Series Technical Manual** - Plasma system specifications
3. **ISO 9013:2017** - Thermal cutting - Classification of thermal cuts - Geometrical product specification
4. **NFPA 51B:2019** - Standard for Fire Prevention During Welding, Cutting, and Other Hot Work
5. **Paton, B.E. (1962).** *Plasma Arc Welding*. Consultants Bureau
6. **Miller Electric Plasma Cutting Guide** - Applications and troubleshooting
7. **Lincoln Electric Plasma Cutting Handbook** - Process fundamentals
