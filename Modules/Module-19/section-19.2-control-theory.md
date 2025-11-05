# 19.2 Control System Theory

## Introduction to Control Theory

Control theory provides the mathematical foundation for understanding and designing feedback control systems. While you can tune PID controllers by trial and error, understanding control theory enables:

- **Predictable Results**: Anticipate system behavior before implementation
- **Systematic Design**: Calculate gains mathematically instead of guessing
- **Troubleshooting**: Diagnose problems by analyzing frequency response
- **Optimization**: Design controllers for specific performance criteria

**Balance**: This section provides enough theory to be useful without requiring advanced mathematics. Focus on concepts and practical application.

## Transfer Functions

### Definition

A **transfer function** describes the input-output relationship of a linear time-invariant (LTI) system in the frequency domain.

**Mathematical Definition**:
$$G(s) = \frac{Y(s)}{U(s)}$$

where:
- $s$ = complex frequency variable (Laplace domain)
- $Y(s)$ = output (Laplace transform)
- $U(s)$ = input (Laplace transform)
- $G(s)$ = transfer function

**Physical Meaning**: How much output you get for a given input, as a function of frequency.

### Laplace Transform Basics

The **Laplace transform** converts time-domain functions to frequency domain:

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t) e^{-st} dt$$

**Common Transforms**:
| Time Domain | Laplace Domain |
|-------------|----------------|
| $\delta(t)$ (impulse) | $1$ |
| $u(t)$ (step) | $\frac{1}{s}$ |
| $e^{-at}$ | $\frac{1}{s+a}$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$ |
| $\frac{df}{dt}$ (derivative) | $sF(s)$ |
| $\int f dt$ (integral) | $\frac{F(s)}{s}$ |

**Why Useful**: Differential equations in time domain → algebraic equations in Laplace domain (easier to solve).

**Example**:
Time domain: $\ddot{x} + 2\zeta\omega_n\dot{x} + \omega_n^2 x = u$

Laplace domain: $s^2 X(s) + 2\zeta\omega_n s X(s) + \omega_n^2 X(s) = U(s)$

Transfer function: $G(s) = \frac{X(s)}{U(s)} = \frac{1}{s^2 + 2\zeta\omega_n s + \omega_n^2}$

### First-Order System

**General Form**:
$$G(s) = \frac{K}{\tau s + 1}$$

where:
- $K$ = DC gain (steady-state gain)
- $\tau$ = time constant

**Time Domain (Step Response)**:
$$y(t) = K(1 - e^{-t/\tau})$$

**Characteristics**:
- **Rise time**: $t_r \approx 2.2\tau$ (10% to 90%)
- **Settling time** (2%): $t_s \approx 4\tau$
- **Time constant** $\tau$: Time to reach 63% of final value

**Example**: RC Low-Pass Filter
- $V_{in}(s) \to G(s) \to V_{out}(s)$
- $G(s) = \frac{1}{RC \cdot s + 1}$
- Time constant: $\tau = RC$

**CNC Example**: Servo motor velocity response
- Command step in voltage → motor accelerates to final velocity
- $G(s) = \frac{K_t}{J s + b}$ ≈ first-order system
- $K_t$ = torque constant, $J$ = inertia, $b$ = viscous damping

### Second-Order System

**General Form**:
$$G(s) = \frac{K\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

where:
- $K$ = DC gain
- $\omega_n$ = natural frequency (rad/s)
- $\zeta$ = damping ratio (dimensionless)

**Physical Meaning**: Mass-spring-damper system
- Mass ($m$) → inertia
- Spring ($k$) → stiffness
- Damper ($c$) → friction/damping

$$\omega_n = \sqrt{\frac{k}{m}}, \quad \zeta = \frac{c}{2\sqrt{km}}$$

**CNC Interpretation**:
- Moving mass: gantry, table, spindle head
- Spring: mechanical compliance (frame, screws, couplings)
- Damper: friction, viscous damping in ways

### Damping Ratio Effects

**Underdamped** ($\zeta < 1$):
- Oscillatory response
- Overshoot present
- Settling time moderate

**Critical Damping** ($\zeta = 1$):
- Fastest response without overshoot
- No oscillation
- Optimal for many applications

**Overdamped** ($\zeta > 1$):
- Slow, sluggish response
- No overshoot
- Long settling time

**Percent Overshoot**:
$$\text{PO} = e^{-\frac{\zeta\pi}{\sqrt{1-\zeta^2}}} \times 100\%$$

**Examples**:
| $\zeta$ | Overshoot | Application |
|---------|-----------|-------------|
| 0.3 | 37% | Too oscillatory for CNC |
| 0.5 | 16% | Acceptable for rapids |
| 0.707 | 4.3% | Common CNC target |
| 0.9 | 0.2% | Precision positioning |
| 1.0 | 0% | Critically damped |

**Typical CNC Target**: $\zeta = 0.7-0.9$ (slight underdamping, fast response, minimal overshoot)

### Block Diagrams

**Basic Feedback Loop**:

```
        +     E(s)          U(s)          Y(s)
R(s) ──>○──> Controller ──> Plant ──────> Output
        -      C(s)          G(s)     |
        ↑                              |
        └──────── Feedback ────────────┘
                  H(s)
```

**Closed-Loop Transfer Function**:
$$T(s) = \frac{Y(s)}{R(s)} = \frac{C(s)G(s)}{1 + C(s)G(s)H(s)}$$

**Unity Feedback** ($H(s) = 1$):
$$T(s) = \frac{C(s)G(s)}{1 + C(s)G(s)}$$

**Example**: Proportional controller ($C(s) = K_P$), first-order plant ($G(s) = \frac{1}{\tau s + 1}$)

$$T(s) = \frac{K_P \cdot \frac{1}{\tau s + 1}}{1 + K_P \cdot \frac{1}{\tau s + 1}} = \frac{K_P}{\tau s + 1 + K_P}$$

**Effect of Increasing $K_P$**:
- DC gain: $\frac{K_P}{1+K_P} \to 1$ as $K_P \to \infty$
- Time constant: $\frac{\tau}{1+K_P} \to 0$ (faster response)

## Frequency Response

### Definition

**Frequency response**: System output when input is sinusoid at various frequencies.

**Sinusoidal Input**: $u(t) = A \sin(\omega t)$

**Steady-State Output**: $y(t) = |G(j\omega)| \cdot A \sin(\omega t + \angle G(j\omega))$

where:
- $|G(j\omega)|$ = magnitude (gain at frequency $\omega$)
- $\angle G(j\omega)$ = phase shift at frequency $\omega$

**Key Concept**: Replace $s$ with $j\omega$ in transfer function to get frequency response.

$$G(j\omega) = G(s)\bigg|_{s=j\omega}$$

### Bode Plots

**Bode plot**: Graphical representation of frequency response
- **Magnitude plot**: $20\log_{10}|G(j\omega)|$ (dB) vs. frequency (log scale)
- **Phase plot**: $\angle G(j\omega)$ (degrees) vs. frequency (log scale)

**Why Bode Plots**:
- Visualize system response across frequency spectrum
- Identify bandwidth, resonances, phase lag
- Design and analyze controllers
- Assess stability margins

### Bandwidth

**Definition**: Frequency at which closed-loop gain drops to -3 dB below DC value.

$$|T(j\omega_{BW})| = \frac{|T(j0)|}{\sqrt{2}} = 0.707 \times |T(j0)|$$

**Physical Meaning**: Maximum frequency of input commands system can follow accurately.

**Example**:
- System bandwidth: 50 Hz
- Sinusoidal position command at 10 Hz: System follows accurately (<3 dB attenuation)
- Sinusoidal position command at 100 Hz: System cannot follow (>10 dB attenuation)

**CNC Context**:
- Higher bandwidth → can follow rapid direction changes (corners, curves)
- Typical CNC servo bandwidth: 20-100 Hz
- High-performance systems: 100-200 Hz

### Gain Margin and Phase Margin

**Stability Margins**: Measure of "how far" from instability the closed-loop system is.

**Gain Margin (GM)**:
- Additional gain that can be added before system becomes unstable
- Measured at frequency where phase = -180° (phase crossover frequency)

$$\text{GM} = -20\log_{10}|L(j\omega_{pc})|_{dB} \text{ at } \angle L(j\omega_{pc}) = -180°$$

**Phase Margin (PM)**:
- Additional phase lag system can tolerate before instability
- Measured at frequency where magnitude = 0 dB (gain crossover frequency)

$$\text{PM} = 180° + \angle L(j\omega_{gc}) \text{ at } |L(j\omega_{gc})|_{dB} = 0$$

**Typical Specifications**:
- **Gain Margin**: >6 dB (factor of 2)
- **Phase Margin**: 30-60° (45° common target)

**Phase Margin vs Damping Ratio** (approximation):
$$\zeta \approx \frac{\text{PM}}{100}$$

Examples:
- PM = 30° → $\zeta \approx 0.3$ (37% overshoot)
- PM = 45° → $\zeta \approx 0.45$ (20% overshoot)
- PM = 60° → $\zeta \approx 0.6$ (10% overshoot)

## Summary

Control system theory provides the foundation for systematic servo tuning:

**Key Concepts**:
1. **Transfer functions**: Mathematical models of system dynamics
2. **Frequency response**: How system responds to different frequencies
3. **Bode plots**: Visualize gain and phase vs. frequency
4. **Stability margins**: Quantify "distance" from instability

**Practical Application**:
- Higher $K_P$: Increases bandwidth, reduces phase margin
- Add $K_I$: Eliminates steady-state error, reduces phase margin
- Add $K_D$: Increases phase margin, extends bandwidth

**Next Steps**:
- Apply theory to PID tuning methods (Section 19.4)
- Learn systematic tuning procedures
- Implement in real systems (Sections 19.10-19.11)

---

**Next**: [19.3 PID Control Fundamentals](section-19.3-pid-fundamentals.md)
