## 4. Drives & Amplifiers

### 4.1 Stepper Drives

Stepper drives convert low-level step/dir commands into regulated phase currents for 2-phase hybrid stepper motors. Modern chopper drives implement current-mode control with microstepping to linearize torque and reduce vibration.

**Electrical Model and Current Regulation**

Each phase behaves approximately as an RL winding with back-EMF proportional to speed:
$$
V_{bus} = R I + L \frac{dI}{dt} + E_{bemf}, \qquad E_{bemf} = K_e \, \omega
$$
The electrical time constant is $\tau = L/R$. To achieve rated current at higher speeds, select bus voltage $V_{bus}$ such that $V_{bus} - E_{bemf}$ maintains sufficient di/dt:
$$
\frac{dI}{dt} = \frac{V_{bus} - E_{bemf} - R I}{L}
$$

Rule of thumb: choose $V_{bus} \approx 10\text{–}20 \times$ the phase rated voltage to overcome inductance and preserve torque at speed (within drive limits).

**Microstepping and Torque Ripple**

Ideal microstepping commands sinusoidal phase currents:
$$
I_A = I_{max} \sin \theta, \qquad I_B = I_{max} \cos \theta
$$
Torque ripple arises from detent torque and current nonlinearity; 8–16× microstepping typically reduces audible resonance without materially increasing static holding torque.

**Mid-Band Resonance and Damping**

Closed-loop damping methods:
- Increase microstep resolution, enable drive’s anti-resonance feature
- Add mechanical inertia (flywheel) or elastomer coupler
- Use closed-loop stepper (encoder + position loop) when trajectory demands

**Torque–Speed Envelope**

Available torque decreases with speed due to $E_{bemf}$ and limited di/dt. Manufacturers provide curves; approximate with an exponential decay over electrical time constants. Ensure application torque + margin stays below curve across duty cycle.

**Worked Example – Stepper Bus Voltage**

NEMA 23: $R=1.2\,\Omega$, $L=3.0\,$mH, $I_{rated}=3.0$ A, $K_e=0.03$ V·s/rad. Target speed 1,200 rpm (125.7 rad/s). Back-EMF $E=3.77$ V. Choose $V_{bus} = 48$ V → maximum di/dt at zero current ~16 kA/s. Adequate margin to track microstep current up to target speed.

**Mechanical Resonance and Mid‑Band Instability**

The rotor and load form a second‑order system driven by discrete microstep excitations. A simplified small‑signal model around an operating speed $\omega_0$ is:
$$
J_{eq} \ddot{\theta} + B_{eq} \, \dot{\theta} + k_{\text{syn}} (\theta - \theta_{cmd}) = T_{dist}
$$
where $J_{eq}$ is reflected inertia, $B_{eq}$ viscous damping, and $k_{\text{syn}}$ the synchronous stiffness (proportional to holding torque and microstep current linearity). Mid‑band resonance occurs when excitation harmonics intersect the natural frequency:
$$
f_n = \frac{1}{2\pi} \sqrt{\frac{k_{\text{syn}}}{J_{eq}}}
$$
Design levers: increase $J_{eq}$ (inertia), increase $B_{eq}$ (damping), or increase $k_{\text{syn}}$ (current linearity, higher holding torque) to shift/attenuate the resonance.

**Step Loss Budget and Margin**

Define step loss margin at speed $\omega$:
$$
M_{\text{step}}(\omega) = \frac{T_{avail}(\omega) - T_{load}(\omega)}{T_{load}(\omega)}
$$
Require $M_{\text{step}} \ge 0.3$ (30%) over the duty trajectory to ensure immunity to disturbances.

**Worked Example – Resonance Damping Sizing**

Given $J_{eq} = 1.6\times10^{-4}$ kg·m², $T_{hold}=2.0$ N·m, microstepping linearity → $k_{\text{syn}} \approx T_{hold}/\theta_s$ with $\theta_s = 1$ step = $2\pi/200$ rad → $k_{\text{syn}} = 2.0/(2\pi/200) = 63.7$ N·m/rad.
Natural frequency: $f_n = (1/2\pi) \sqrt{k_{\text{syn}}/J_{eq}} = 100.3$ Hz (≈ 6,018 rpm 1× mechanical). Add elastomer coupler that contributes $B_{eq}=0.004$ N·m·s/rad; damping ratio $\zeta = B_{eq}/(2\sqrt{J_{eq}k_{\text{syn}}}) = 0.25$ → mid‑band oscillations suppressed; acceptance: no step loss in 0–120 rps sweep.

**PWM Ripple – Numeric Check**

Given $L=3$ mH, $V_{bus}=48$ V, $E_{bemf}=4$ V at target speed, PWM 30 kHz ($T_{PWM}=33.3\,\mu$s), duty $D=0.5$:
$$
\Delta I \approx \frac{(48-4)\,0.5\,33.3\times10^{-6}}{3\times10^{-3}} = 0.245 \; \text{A}
$$
For $I_{ref}=3$ A, ripple ≈ 8.2% (<10% target) → acceptable. If ripple >10%, increase PWM frequency or switch to mixed/slow decay.

**Torque–Speed Relationship (Approximate Derivation)**

Assuming sinusoidal current control with electrical time constant $\tau=L/R$, current magnitude tracks the command with first‑order lag:
$$
|I(j\omega)| \approx \frac{I_0}{\sqrt{1+(\omega \tau)^2}}
$$
With $T \approx K_t I$, the available torque decays similarly with speed; identify $\omega_c\approx 1/\tau$ and compare against catalog curves to validate motor/drive selection.

**Worked Example – Torque–Speed Validation vs. Catalog**

Motor datasheet (NEMA 23): $T_0=2.2$ N·m at 0 rpm, knee at 900 rpm with 48 V drive; our model with $\tau=2.5$ ms gives $\omega_c=400$ rad/s (≈ 3,820 rpm). At 1,200 rpm (125.7 rad/s):
$$
\frac{T(\omega)}{T_0} \approx \frac{1}{\sqrt{1+(\omega/\omega_c)^2}} = \frac{1}{\sqrt{1+(126/400)^2}} = 0.95
$$
Predicted torque = 2.1 N·m vs. catalog 1.9 N·m (≈10% optimistic). Apply a correction factor 0.9 to account for current ripple and detent torque; selection remains acceptable with ≥20% margin over 0.8 N·m requirement.

### 4.2 Servo Drives

Servo drives regulate motor current (torque) with a high-bandwidth inner loop and close velocity/position loops in cascaded fashion. Modern AC servos use three-phase inverters with field-oriented control (FOC).

**FOC Essentials**

Clarke–Park transforms map three-phase currents to rotating dq axes:
\begin{align*}
\begin{bmatrix} i_\alpha \\ i_\beta \end{bmatrix} &= \mathbf{T}_{Clarke} \begin{bmatrix} i_A \\ i_B \\ i_C \end{bmatrix}, \\
\begin{bmatrix} i_d \\ i_q \end{bmatrix} &= \mathbf{R}(-\theta_e) \begin{bmatrix} i_\alpha \\ i_\beta \end{bmatrix}
\end{align*}
Torque is predominantly from $i_q$: $T \approx K_t \, i_q$. Current controllers (PI) regulate $i_d, i_q$; outer loops command $i_q$ to meet velocity/position demands.

**Cascaded Loop Tuning**

- Current loop bandwidth: 2–5 kHz (limited by PWM switching and sampling)
- Velocity loop: 100–300 Hz
- Position loop: 20–100 Hz

General rule: bandwidths separated by ~5–10× for robustness. Verify phase/gain margins with frequency response tools provided by the drive vendor.

**Encoder/Resolver Interfaces and Safety (STO)**

Drives accept incremental (A/B/Z), absolute (BiSS, EnDat), or resolver signals. Safety torque off (STO) inputs disable gate drive to achieve SIL2/PLd stopping without removing mains power.

**Worked Example – Current Loop Bandwidth**

Motor: $L_s=1.2$ mH, $R_s=0.8\,\Omega$, $K_t=0.9$ N·m/A. With PWM 20 kHz, sampling 10 kHz, choose current PI to achieve ~2 kHz crossover (approximate). Validate via injected sine sweep; ensure <10% phase ripple at crossover.

**Inverter Topology, Dead‑Time, and Current Sensing**

Three‑phase inverters (two‑level NPC) modulate phase voltages with PWM. Dead‑time $t_d$ prevents shoot‑through but distorts phase voltage:
$$
\Delta V_{dt} \approx \frac{2 t_d}{T_{PWM}} V_{bus} \operatorname{sgn}(i_{phase})
$$
Compensate via dead‑time insertion tables or model‑based correction. Current sensing options: shunt resistors (low cost), Hall sensors (isolation), fluxgate CT (high accuracy). Sample synchronously near the middle of PWM on‑time to minimize switching noise.

**Discrete Implementation Notes**

With sampling $T_s$, implement Tustin (bilinear) transform for PI:
$$
C_i(z) = K_{pi} + K_{ii} \frac{T_s}{2} \frac{1+z^{-1}}{1-z^{-1}}
$$
Anti‑windup back‑calculation:
$$
\dot{x}_i = K_{ii} e + K_{aw} (u - u_{sat})
$$
Choose $K_{aw} \approx 1/T_i$ to limit integrator during saturation.

**Notch Filter Placement (Structural Mode)**

If Module 1 identified a structural mode at $f_s=120$ Hz, configure velocity‑loop notch:
$$
H_n(s) = \frac{s^2 + 2\zeta_z \omega_s s + \omega_s^2}{s^2 + 2\zeta_p \omega_s s + \omega_s^2}
$$
with $\omega_s=2\pi f_s$, choose $\zeta_z \approx 0.1$, $\zeta_p \approx 0.01$ so the notch removes energy near $f_s$ with minimal phase penalty elsewhere. Validate via swept‑sine.

**Worked Example – Velocity Loop Phase Margin**

Assume current loop is 10× faster than velocity loop (stiff torque source). Plant $G_v(s)=K_t/(J_{eq}s)$ with $J_{eq}=7.5\times10^{-4}$ kg·m², $K_t=0.9$ N·m/A. Controller $C_v(s)=K_{pv}+K_{iv}/s$ with $K_{pv}=1.0$ A·s/rad, $K_{iv}=240$ A/rad.

Open‑loop $L(s)=C_v(s)G_v(s) = \frac{K_t}{J_{eq}} \left( \frac{K_{pv}}{s} + \frac{K_{iv}}{s^2} \right)$. Crossover near $\omega_v \approx 1200$ rad/s (by design). Phase at $\omega_v$:
$$
\angle L(j\omega_v) \approx \tan^{-1}\!\left(\frac{K_{iv}/\omega_v}{K_{pv}}\right) - 90^\circ \approx \tan^{-1}(0.2) - 90^\circ = -78.7^\circ
$$
Phase margin ≈ $180^\circ - 78.7^\circ = 101^\circ$ (conservative upper bound; measured PM typically 50–70° once sampling, delays, and current‑loop dynamics are included). Verify in drive bode tool; adjust $K_{pv},K_{iv}$ to target 55–60° PM.

**Worked Example – Dead‑Time Error Estimate**

$V_{bus}=80$ V, $f_{PWM}=20$ kHz ($T_{PWM}=50\,\mu$s), $t_d=800$ ns. $\Delta V_{dt} \approx 2\cdot0.8/50 \times 80 = 2.56$ V (3.2%). Enable dead‑time compensation table → measured THD in phase current drops from 7.5% to 2.1% at 2 A RMS.

**Velocity and Position Loop Synthesis**

Velocity plant $G_v(s)=K_t/(J_{eq}s)$ → place zero at origin (PI) and choose $\omega_v$ with 5–10× separation from current loop. Position loop $C_p(s)=K_p(1+1/(T_i s))$ preferred when friction or gravity bias requires integral action; otherwise, P with feedforward minimizes overshoot.

### 4.3 Drive Sizing (Peak/Continuous, Bus, Braking)

Select drive ratings from mechanical demand (Module 3):
$$
I_{peak} \ge \frac{T_{peak}}{K_t}, \qquad I_{cont} \ge \frac{T_{RMS}}{K_t}
$$
Bus voltage targets electrical speed margin: $V_{bus} \gtrsim E_{bemf,max} + R I_{max} + L \, (dI/dt)_{req}$.

Regeneration during decel stores energy in the DC link capacitor; size braking resistor $R_b$ for power $P_{regen}$ and allowable duty:
$$
P_{regen} \approx J_{eq} \, \omega \, \dot{\omega}, \qquad R_b = \frac{(V_{trip}^2 - V_{bus}^2)}{P_{regen}}
$$
Confirm resistor thermal time constant supports the decel profile.

**RMS Current/Power from Motion Profile**

Given torque profile $T(t)$ over cycle time $T_c$, compute RMS:
$$
T_{RMS} = \sqrt{\frac{1}{T_c} \int_0^{T_c} T^2(t)\, dt}, \qquad I_{RMS} = \frac{T_{RMS}}{K_t}
$$
Use $I_{RMS}$ to verify continuous current and heatsink thermal limits.

**DC Link Capacitor Sizing (Ripple)**

Rectified supply ripple (single‑phase) approximation:
$$
\Delta V \approx \frac{I_{load}}{C \cdot 2 f_{line}}
$$
Braking energy absorption peak ripple (short interval $\Delta t$):
$$
\Delta V \approx \frac{I_{regen}\, \Delta t}{C}
$$
Choose capacitor bank to keep $\Delta V$ within drive trip margin (e.g., <10% of $V_{bus}$) and meet ripple current ratings.

**Worked Example – RMS Sizing from Profile**

Cycle: accelerate 0→1.5 m/s in 0.15 s at 1.2 kN on 10 mm lead ($T=\tfrac{F p}{2\pi \eta}=2.08$ N·m), hold 2 s at 0.4 N·m friction, decel symmetric. Compute
$$
T_{RMS} = \sqrt{\frac{2(0.15)\, (2.08)^2 + 2.0\, (0.4)^2}{2.3}} = 0.94 \; \text{N·m}
$$
With $K_t=0.9$ N·m/A → $I_{RMS}=1.04$ A: a 5 A continuous drive has ample thermal margin.

**Braking Duty – Acceptance Table (Guide)**

| Decel Energy (J) | Duration (s) | Avg Power (W) | Resistor Rating Guidance |
|---:|---:|---:|---|
| 200 | 1.0 | 200 | ≥200 W cont., ≥2× for 1 s pulses |
| 600 | 0.5 | 1200 | ≥200 W cont., ≥6× for 0.5 s (vendor pulse chart) |
| 1200 | 1.0 | 1200 | ≥300 W cont., ≥5× for 1 s; consider longer decel |
| 2500 | 2.0 | 1250 | Split resistors, verify enclosure cooling, consider regen drive |

### 4.4 Commissioning & Tuning

**Procedure:**
1.  **Mechanical Check**: Ensure free motion without binding; verify feedback polarity.
2.  **Auto-Identification**: Use drive's built-in tools to estimate motor parameters (R, L, inertia).
3.  **Tune Loops**: Sequentially tune the current loop (PI), then velocity loop (PI), then position loop (P/PI + feedforward).
4.  **Feedforward**: Enable friction and inertia feedforward; configure integrator anti-windup limits.
5.  **Resonance Handling**: Use notch filters to suppress structural modes identified in Module 1; verify with chirp/step response tests.
6.  **Safety Tests**: Verify STO, overcurrent, overspeed, and following error limits function correctly.

**Acceptance Criteria**

- Current loop: command square wave; <10% current ripple at rated current; crossover within target (±10%).
- Velocity loop: 50% speed step; settling <50 ms, overshoot <10%.
- Position loop: 10 mm step; settling <25 ms, overshoot <5%, steady‑state error <1 encoder count.
- Following error during S‑curve profile: <25% of tolerance budget (e.g., <5 µm if tolerance = 20 µm).
- Safety: STO reaction <20 ms; E‑stop end‑to‑end <200 ms.

**Troubleshooting Guide (Quick Reference)**

- High current ripple at low speed → switch to mixed/slow decay (stepper) or retune current PI (servo); check current sensor bandwidth.
- Audible grind at mid‑speeds (stepper) → enable anti‑resonance, increase microstep, add inertia/damping.
- Overshoot/oscillation (servo) → reduce velocity loop gain or add lead filter; verify current loop separation ≥5×.
- Overvoltage trips on decel → increase braking resistor power or duty rating; add DC link capacitance; lengthen decel ramp.

### 4.5 Safety & STO Integration

Servo drives with SIL2/PLd provide dual‑channel STO (Safe Torque Off). Typical wiring:
- Dual inputs STO_A and STO_B from safety relay contacts (force‑guided), 24 V DC logic. Both channels must be high for the drive to enable.
- E‑stop loop opens both channels → drive power stage disabled within specified reaction time.

Design requirements:
- Category 3 architecture: redundant channels, monitored by safety relay
- STO reaction time: ≤20 ms; total machine stopping <200 ms (see Section 6)
- Periodic proof testing: monthly STO functional test

STO Commissioning Procedure:
1) With axis enabled and holding position, open STO_A only → drive faults with “STO channel discrepancy” within 20 ms.
2) Reset, then open both STO_A and STO_B → torque off within reaction time; axis coasts; no uncontrolled restart on re‑close.
3) Log reaction time with scope (drive ready → STO low → current zero). Acceptance: ≤20 ms.

### 4.6 Commissioning Matrix (Acceptance)

| Test | Procedure | Acceptance |
|---|---|---|
| Current loop verification | Inject square‑wave current command at 10% rated; observe ripple | <10% ripple; no saturations |
| Velocity step | 50% speed step; log response | Settling <50 ms; overshoot <10% |
| Position step | 10 mm step; measure error | Settling <25 ms; SS error <1 count |
| Following error budget | S‑curve move at max feed | <25% of tolerance budget |
| Structural notch | Sweep 50–300 Hz | Peak suppression >12 dB at mode freq |
| STO reaction | Open both STO channels | ≤20 ms drive reaction; <200 ms system stop |
| Regen trip | Hard decel from max speed | No DC bus over‑voltage with resistor engaged |

---

## References

1. **ISO 230-2:2014** - Test code for machine tools - Positioning accuracy
2. **ISO 13849-1:2015** - Safety of machinery - Safety-related control systems
3. **Franklin, G.F., Powell, J.D., & Emami-Naeini, A. (2014).** *Feedback Control of Dynamic Systems* (7th ed.). Pearson
4. **Ogata, K. (2009).** *Modern Control Engineering* (5th ed.). Pearson
5. **LinuxCNC Integrator's Manual** (linuxcnc.org) - CNC control configuration
6. **Mach4 CNC Controller** (machsupport.com) - Software documentation
7. **FANUC CNC Series Technical Manuals** - Industrial controller specifications
8. **IEC 61000 Series** - Electromagnetic compatibility (EMC) standards
