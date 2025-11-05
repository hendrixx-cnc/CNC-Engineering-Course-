# Appendix P: Engineering Mathematics for CNC Design

---

## P.1 Fundamentals: Units and Dimensional Analysis

### P.1.1 SI Base Units

| Quantity | Unit | Symbol |
|----------|------|--------|
| Length | meter | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric Current | ampere | A |
| Temperature | kelvin | K |
| Amount of Substance | mole | mol |
| Luminous Intensity | candela | cd |

### P.1.2 Common Derived Units

| Quantity | Unit | Symbol | Formula | SI Base |
|----------|------|--------|---------|---------|
| Force | newton | N | F = ma | kg·m/s² |
| Pressure/Stress | pascal | Pa | P = F/A | kg/(m·s²) or N/m² |
| Energy/Work | joule | J | W = Fd | kg·m²/s² or N·m |
| Power | watt | W | P = E/t | kg·m²/s³ or J/s |
| Frequency | hertz | Hz | f = 1/T | s⁻¹ |
| Torque | newton-meter | N·m | τ = F×r | kg·m²/s² |
| Angle | radian | rad | θ = s/r | dimensionless |

### P.1.3 Dimensional Analysis

**Rule:** All terms in equation must have same dimensions.

**Example:** Beam deflection equation
$$\delta = \frac{F L^3}{3 E I}$$

Dimensional check:
- Left side: $[\delta] = \text{m}$ (length)
- Right side: $\frac{[\text{N}] \cdot [\text{m}]^3}{[\text{Pa}] \cdot [\text{m}]^4} = \frac{\text{kg·m/s}^2 \cdot \text{m}^3}{(\text{kg/(m·s}^2)) \cdot \text{m}^4} = \frac{\text{m}^4}{\text{m}^3} = \text{m}$ ✓

---

## P.2 Algebra and Equation Manipulation

### P.2.1 Linear Equations

**Standard form:** $ax + b = 0$

**Solution:** $x = -\frac{b}{a}$

**Example:** Motor sizing requires torque $T = J \alpha$ where $J = 0.05$ kg·m², $\alpha = 100$ rad/s². Find $T$:
$$T = 0.05 \times 100 = 5 \text{ N·m}$$

### P.2.2 Quadratic Equations

**Standard form:** $ax^2 + bx + c = 0$

**Quadratic formula:**
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Example:** Critical speed of ball screw: $N_{\text{crit}}^2 - 200N_{\text{crit}} - 10000 = 0$

$$N = \frac{200 \pm \sqrt{200^2 - 4(1)(-10000)}}{2(1)} = \frac{200 \pm \sqrt{80000}}{2} = \frac{200 \pm 283}{2}$$

Positive solution: $N = 241.5$ RPM

### P.2.3 Simultaneous Linear Equations

**Matrix form:** $\mathbf{Ax} = \mathbf{b}$

**Example:** Force balance on gantry
$$\begin{cases}
F_1 + F_2 = 1000 \text{ N} \\
2F_1 + F_2 = 1500 \text{ N}
\end{cases}$$

Substitution method:
- From equation 1: $F_2 = 1000 - F_1$
- Substitute into equation 2: $2F_1 + (1000 - F_1) = 1500$
- Solve: $F_1 = 500$ N, $F_2 = 500$ N

### P.2.4 Exponential and Logarithmic Equations

**Exponential decay:** $y = y_0 e^{-kt}$

**Example:** Vibration amplitude decay (damping):
$$A(t) = A_0 e^{-\zeta \omega_n t}$$

where $\zeta$ = damping ratio, $\omega_n$ = natural frequency (rad/s)

**Logarithm rules:**
- $\log(ab) = \log a + \log b$
- $\log(a/b) = \log a - \log b$
- $\log(a^n) = n \log a$
- $\log_b(b^x) = x$

**Example:** Bearing life calculation involves cube root:
$$L_{10} = \left(\frac{C}{P}\right)^3 \text{ (million revolutions)}$$

Taking log: $\log L_{10} = 3 \log(C/P)$

---

## P.3 Trigonometry

### P.3.1 Basic Trigonometric Functions

**Right triangle definitions:**
$$\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}}, \quad \cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}}, \quad \tan \theta = \frac{\text{opposite}}{\text{adjacent}}$$

**Pythagorean identity:**
$$\sin^2 \theta + \cos^2 \theta = 1$$

**Angle sum formulas:**
$$\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$$
$$\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$$

### P.3.2 Inverse Trigonometric Functions

$$\theta = \arcsin(x), \quad \theta = \arccos(x), \quad \theta = \arctan(x)$$

**Example:** Gantry beam angle from deflection
$$\theta = \arctan\left(\frac{\delta}{L}\right) = \arctan\left(\frac{0.5 \text{ mm}}{1000 \text{ mm}}\right) = 0.0005 \text{ rad} = 0.029°$$

### P.3.3 Angle Conversions

$$\text{radians} = \text{degrees} \times \frac{\pi}{180}$$
$$\text{degrees} = \text{radians} \times \frac{180}{\pi}$$

**Example:** Stepper motor 1.8° step
$$1.8° = 1.8 \times \frac{\pi}{180} = 0.0314 \text{ rad}$$

Steps per revolution: $360° / 1.8° = 200$ steps

### P.3.4 Practical CNC Applications

**Arc interpolation (G02/G03):**

Given start point $(x_1, y_1)$, end point $(x_2, y_2)$, radius $R$:

Center offset from start:
$$I = \pm \sqrt{R^2 - d^2/4}, \quad J = \pm \sqrt{R^2 - d^2/4}$$

where $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$

---

## P.4 Vectors and Vector Operations

### P.4.1 Vector Notation

**2D vector:** $\mathbf{v} = \begin{bmatrix} v_x \\ v_y \end{bmatrix}$ or $\mathbf{v} = v_x \mathbf{i} + v_y \mathbf{j}$

**3D vector:** $\mathbf{v} = \begin{bmatrix} v_x \\ v_y \\ v_z \end{bmatrix}$ or $\mathbf{v} = v_x \mathbf{i} + v_y \mathbf{j} + v_z \mathbf{k}$

### P.4.2 Vector Magnitude

$$|\mathbf{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2}$$

**Example:** Gantry velocity components $v_x = 10$ m/min, $v_y = 15$ m/min

Resultant velocity:
$$|\mathbf{v}| = \sqrt{10^2 + 15^2} = \sqrt{325} = 18.03 \text{ m/min}$$

### P.4.3 Dot Product (Scalar Product)

$$\mathbf{a} \cdot \mathbf{b} = a_x b_x + a_y b_y + a_z b_z = |\mathbf{a}||\mathbf{b}| \cos \theta$$

**Applications:**
- Work: $W = \mathbf{F} \cdot \mathbf{d}$
- Power: $P = \mathbf{F} \cdot \mathbf{v}$
- Angle between vectors: $\theta = \arccos\left(\frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}\right)$

**Example:** Cutting force $\mathbf{F} = (100, 50, 30)$ N, tool displacement $\mathbf{d} = (0, 0, -5)$ mm

Work done:
$$W = \mathbf{F} \cdot \mathbf{d} = 100(0) + 50(0) + 30(-5) = -150 \text{ N·mm} = -0.15 \text{ J}$$

### P.4.4 Cross Product (Vector Product)

$$\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix} = (a_y b_z - a_z b_y)\mathbf{i} - (a_x b_z - a_z b_x)\mathbf{j} + (a_x b_y - a_y b_x)\mathbf{k}$$

**Magnitude:** $|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}| \sin \theta$

**Applications:**
- Torque: $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$
- Angular momentum: $\mathbf{L} = \mathbf{r} \times \mathbf{p}$

**Example:** Force $\mathbf{F} = (0, 100, 0)$ N at position $\mathbf{r} = (0.5, 0, 0)$ m

Torque about origin:
$$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 0.5 & 0 & 0 \\ 0 & 100 & 0 \end{vmatrix} = (0, 0, 50) \text{ N·m}$$

Torque magnitude: 50 N·m about Z-axis

---

## P.5 Calculus: Differentiation

### P.5.1 Basic Derivatives

| Function $f(x)$ | Derivative $f'(x)$ |
|----------------|-------------------|
| $c$ (constant) | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $1/x$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |

### P.5.2 Differentiation Rules

**Sum/Difference:** $(f \pm g)' = f' \pm g'$

**Product rule:** $(fg)' = f'g + fg'$

**Quotient rule:** $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$

**Chain rule:** $\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$

### P.5.3 Applications in CNC

**Velocity from position:**
$$v(t) = \frac{dx}{dt}$$

**Acceleration from velocity:**
$$a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$

**Example:** Position profile during trapezoidal move:

Acceleration phase: $x(t) = \frac{1}{2}at^2$

Velocity: $v(t) = \frac{dx}{dt} = at$

Acceleration: $a(t) = \frac{dv}{dt} = a$ (constant)

**Instantaneous power:**
$$P = \frac{dE}{dt}$$

For motor: $P = \tau \omega$ where $\omega = \frac{d\theta}{dt}$ (angular velocity)

### P.5.4 Optimization (Finding Maxima/Minima)

Set $f'(x) = 0$ and solve for $x$.

**Second derivative test:**
- $f''(x) > 0$: minimum
- $f''(x) < 0$: maximum

**Example:** Minimize deflection by optimizing beam shape

For rectangular beam: $I = \frac{bh^3}{12}$

Given constant area $A = bh$, find $h$ maximizing $I$:

$b = A/h$, so $I = \frac{Ah^2}{12}$

$\frac{dI}{dh} = \frac{Ah}{6} = 0$ → No finite maximum (increase $h$, decrease $b$)

Practical constraint: buckling limits $h/b$ ratio

---

## P.6 Calculus: Integration

### P.6.1 Basic Integrals

| Function $f(x)$ | Integral $\int f(x) dx$ |
|----------------|------------------------|
| $x^n$ | $\frac{x^{n+1}}{n+1} + C$ (n ≠ -1) |
| $1/x$ | $\ln|x| + C$ |
| $e^x$ | $e^x + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |

### P.6.2 Definite Integrals

$$\int_a^b f(x) dx = F(b) - F(a)$$

where $F(x)$ is antiderivative of $f(x)$

### P.6.3 Applications in CNC

**Distance from velocity:**
$$s = \int_0^t v(t) dt$$

**Velocity from acceleration:**
$$v = \int_0^t a(t) dt$$

**Example:** Trapezoidal velocity profile

Constant acceleration $a = 2$ m/s² for $t = 3$ s:

$$v(t) = \int_0^3 a \, dt = at \Big|_0^3 = 2(3) = 6 \text{ m/s}$$

Distance during acceleration:
$$s = \int_0^3 v(t) dt = \int_0^3 2t \, dt = t^2 \Big|_0^3 = 9 \text{ m}$$

**Work from force:**
$$W = \int_0^d F(x) dx$$

**Average value:**
$$f_{\text{avg}} = \frac{1}{b-a} \int_a^b f(x) dx$$

**Example:** Average motor torque over acceleration

$$\tau_{\text{avg}} = \frac{1}{T} \int_0^T \tau(t) dt$$

---

## P.7 Differential Equations for Dynamic Systems

### P.7.1 First-Order Linear ODE

**Standard form:** $\frac{dy}{dt} + p(t)y = q(t)$

**Solution method:** Integrating factor $\mu(t) = e^{\int p(t) dt}$

**Example:** RC circuit (similar to motor thermal model)

$$\frac{dT}{dt} + \frac{T}{\tau} = \frac{P}{\tau}$$

where $T$ = temperature rise, $\tau$ = thermal time constant, $P$ = power dissipation

Solution: $T(t) = P\left(1 - e^{-t/\tau}\right)$ (heating from ambient)

### P.7.2 Second-Order Linear ODE (Vibration)

**Standard form:** $m\frac{d^2x}{dt^2} + c\frac{dx}{dt} + kx = F(t)$

**Natural frequency:** $\omega_n = \sqrt{\frac{k}{m}}$ rad/s

**Damping ratio:** $\zeta = \frac{c}{2\sqrt{km}}$

**Solutions:**

1. **Underdamped ($\zeta < 1$):** Oscillatory
   $$x(t) = Ae^{-\zeta \omega_n t} \cos(\omega_d t + \phi)$$
   where $\omega_d = \omega_n \sqrt{1 - \zeta^2}$ (damped frequency)

2. **Critically damped ($\zeta = 1$):** Fastest return without overshoot
   $$x(t) = (A + Bt)e^{-\omega_n t}$$

3. **Overdamped ($\zeta > 1$):** Slow return, no oscillation
   $$x(t) = Ae^{-(\zeta - \sqrt{\zeta^2-1})\omega_n t} + Be^{-(\zeta + \sqrt{\zeta^2-1})\omega_n t}$$

**Example:** Gantry vibration after step input

Given: $m = 50$ kg, $k = 100,000$ N/m, $c = 500$ N·s/m

$$\omega_n = \sqrt{\frac{100000}{50}} = 44.7 \text{ rad/s} = 7.1 \text{ Hz}$$

$$\zeta = \frac{500}{2\sqrt{50 \times 100000}} = 0.35$$

System is underdamped → will oscillate at:
$$f_d = \frac{\omega_d}{2\pi} = \frac{44.7\sqrt{1-0.35^2}}{2\pi} = 6.6 \text{ Hz}$$

---

## P.8 Matrix Algebra

### P.8.1 Matrix Operations

**Addition:** $\mathbf{C} = \mathbf{A} + \mathbf{B}$ where $c_{ij} = a_{ij} + b_{ij}$

**Multiplication:** $\mathbf{C} = \mathbf{A} \mathbf{B}$ where $c_{ij} = \sum_k a_{ik}b_{kj}$

**Transpose:** $\mathbf{A}^T$ where $(A^T)_{ij} = A_{ji}$

**Inverse:** $\mathbf{A}^{-1}$ where $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$

**2×2 inverse:**
$$\mathbf{A}^{-1} = \frac{1}{\det \mathbf{A}} \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix}$$

where $\det \mathbf{A} = a_{11}a_{22} - a_{12}a_{21}$

### P.8.2 Rotation Matrices

**2D rotation by angle $\theta$:**
$$\mathbf{R}(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

**3D rotation about Z-axis:**
$$\mathbf{R}_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

**Example:** Rotating coordinate system for angled tool approach

Point $(x, y) = (10, 0)$ mm rotated by $\theta = 45°$:

$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos 45° & -\sin 45° \\ \sin 45° & \cos 45° \end{bmatrix} \begin{bmatrix} 10 \\ 0 \end{bmatrix} = \begin{bmatrix} 7.07 \\ 7.07 \end{bmatrix} \text{ mm}$$

### P.8.3 Transformation Matrices (Homogeneous Coordinates)

**Translation + Rotation in 2D:**
$$\mathbf{T} = \begin{bmatrix} \cos\theta & -\sin\theta & t_x \\ \sin\theta & \cos\theta & t_y \\ 0 & 0 & 1 \end{bmatrix}$$

**Point transformation:**
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \mathbf{T} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

**Application:** G-code coordinate transforms (G54-G59 work offsets, G68 rotation)

---

## P.9 Statics and Force Analysis

### P.9.1 Newton's Laws

**First Law:** Object at rest stays at rest unless acted upon by force (inertia)

**Second Law:** $\mathbf{F} = m\mathbf{a}$

**Third Law:** Action-reaction pairs (equal magnitude, opposite direction)

### P.9.2 Equilibrium Conditions

**Static equilibrium:**
$$\sum \mathbf{F} = 0 \quad \text{(no net force)}$$
$$\sum \boldsymbol{\tau} = 0 \quad \text{(no net torque)}$$

**2D equilibrium (3 equations):**
$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_z = 0$$

**3D equilibrium (6 equations):**
$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum F_z = 0$$
$$\sum M_x = 0, \quad \sum M_y = 0, \quad \sum M_z = 0$$

### P.9.3 Free Body Diagrams (FBD)

**Procedure:**
1. Isolate body/component
2. Show all external forces (gravity, reactions, applied loads)
3. Choose coordinate system
4. Apply equilibrium equations

**Example:** Simply supported beam with center load

Given: Beam length $L = 1$ m, load $F = 1000$ N at center

FBD: Reactions $R_A$ and $R_B$ at ends

Equilibrium:
- $\sum F_y = R_A + R_B - F = 0$
- $\sum M_A = R_B \cdot L - F \cdot (L/2) = 0$

Solve: $R_B = F/2 = 500$ N, $R_A = 500$ N (symmetry)

### P.9.4 Truss Analysis (Method of Joints)

For each joint in equilibrium:
$$\sum F_x = 0, \quad \sum F_y = 0$$

**Sign convention:** Tension (+), Compression (-)

**Example:** Simple triangular truss supporting gantry beam

---

## P.10 Dynamics and Kinematics

### P.10.1 Linear Motion Equations

**Constant acceleration:**
$$v = v_0 + at$$
$$s = v_0 t + \frac{1}{2}at^2$$
$$v^2 = v_0^2 + 2as$$

**Example:** CNC rapid move (G00)

Acceleration phase: $a = 2$ m/s², time $t_1 = 1$ s

Final velocity: $v = 0 + 2(1) = 2$ m/s

Distance: $s = 0 + \frac{1}{2}(2)(1)^2 = 1$ m

### P.10.2 Rotational Motion Equations

**Angular displacement:** $\theta$ (rad)

**Angular velocity:** $\omega = \frac{d\theta}{dt}$ (rad/s)

**Angular acceleration:** $\alpha = \frac{d\omega}{dt}$ (rad/s²)

**Constant angular acceleration:**
$$\omega = \omega_0 + \alpha t$$
$$\theta = \omega_0 t + \frac{1}{2}\alpha t^2$$
$$\omega^2 = \omega_0^2 + 2\alpha \theta$$

**Relationship to linear motion:**
$$v = r\omega, \quad a_{\text{tangential}} = r\alpha, \quad a_{\text{centripetal}} = \frac{v^2}{r} = r\omega^2$$

**Example:** Spindle acceleration

From rest to $N = 3000$ RPM in $t = 0.5$ s:

$$\omega = \frac{2\pi N}{60} = \frac{2\pi(3000)}{60} = 314 \text{ rad/s}$$

$$\alpha = \frac{\omega - 0}{t} = \frac{314}{0.5} = 628 \text{ rad/s}^2$$

### P.10.3 Newton's Second Law for Rotation

$$\tau = I \alpha$$

where $I$ = moment of inertia (kg·m²), $\alpha$ = angular acceleration (rad/s²)

**Moment of inertia (common shapes):**

| Shape | Axis | Moment of Inertia |
|-------|------|-------------------|
| Solid cylinder | Central axis | $I = \frac{1}{2}mR^2$ |
| Hollow cylinder | Central axis | $I = \frac{1}{2}m(R_o^2 + R_i^2)$ |
| Solid sphere | Diameter | $I = \frac{2}{5}mR^2$ |
| Thin rod | Center, perpendicular | $I = \frac{1}{12}mL^2$ |
| Point mass | Distance $r$ | $I = mr^2$ |

**Example:** Motor torque for spindle acceleration

Spindle: $m = 5$ kg, $R = 0.05$ m (solid cylinder approximation)

$$I = \frac{1}{2}(5)(0.05)^2 = 0.00625 \text{ kg·m}^2$$

From previous example: $\alpha = 628$ rad/s²

Required torque: $\tau = I\alpha = 0.00625 \times 628 = 3.93$ N·m

### P.10.4 Work-Energy Theorem

$$W = \Delta KE = \frac{1}{2}m(v_f^2 - v_i^2)$$

**Rotational kinetic energy:**
$$KE_{\text{rot}} = \frac{1}{2}I\omega^2$$

**Example:** Energy to accelerate servo motor + ball screw

Motor rotor: $I_m = 0.001$ kg·m², final speed $\omega_m = 3000$ RPM = 314 rad/s

Ball screw: $I_s = 0.005$ kg·m², coupled 1:1

Total inertia (reflected to motor): $I_{\text{total}} = 0.001 + 0.005 = 0.006$ kg·m²

Energy required:
$$E = \frac{1}{2}(0.006)(314)^2 = 296 \text{ J}$$

If accelerated in 0.5 s: $P_{\text{avg}} = 296 / 0.5 = 592$ W

---

## P.11 Mechanics of Materials

### P.11.1 Stress and Strain

**Normal stress:** $\sigma = \frac{F}{A}$ (Pa or N/m²)

**Shear stress:** $\tau = \frac{F}{A}$ (Pa or N/m²)

**Normal strain:** $\epsilon = \frac{\Delta L}{L_0}$ (dimensionless or %)

**Shear strain:** $\gamma = \frac{\Delta x}{h}$ (rad, dimensionless)

**Hooke's Law (elastic region):**
$$\sigma = E \epsilon$$

where $E$ = Young's modulus (Pa)

**Example:** Steel rod under tension

$F = 10,000$ N, $A = 100$ mm², $L_0 = 500$ mm, $E = 200$ GPa

$$\sigma = \frac{10000}{100 \times 10^{-6}} = 100 \times 10^6 \text{ Pa} = 100 \text{ MPa}$$

$$\epsilon = \frac{\sigma}{E} = \frac{100 \times 10^6}{200 \times 10^9} = 0.0005 = 0.05\%$$

$$\Delta L = \epsilon L_0 = 0.0005 \times 500 = 0.25 \text{ mm}$$

### P.11.2 Bending Stress

**Flexure formula:**
$$\sigma = \frac{My}{I}$$

where:
- $M$ = bending moment (N·m)
- $y$ = distance from neutral axis (m)
- $I$ = second moment of area (m⁴)

**Maximum stress (at outer fiber):**
$$\sigma_{\max} = \frac{Mc}{I} = \frac{M}{S}$$

where $S = I/c$ = section modulus (m³)

**Example:** Gantry beam (rectangular cross-section)

$M = 500$ N·m, $b = 100$ mm, $h = 200$ mm

$$I = \frac{bh^3}{12} = \frac{0.1 \times 0.2^3}{12} = 6.67 \times 10^{-5} \text{ m}^4$$

$$c = h/2 = 0.1 \text{ m}$$

$$\sigma_{\max} = \frac{500 \times 0.1}{6.67 \times 10^{-5}} = 75 \times 10^6 \text{ Pa} = 75 \text{ MPa}$$

### P.11.3 Beam Deflection

**Cantilever beam (end load):**
$$\delta = \frac{FL^3}{3EI}$$

**Simply supported beam (center load):**
$$\delta = \frac{FL^3}{48EI}$$

**Example:** Z-axis spindle head deflection (cantilever)

$F = 1000$ N, $L = 0.5$ m, $E = 200$ GPa, $I = 6.67 \times 10^{-5}$ m⁴

$$\delta = \frac{1000 \times 0.5^3}{3 \times 200 \times 10^9 \times 6.67 \times 10^{-5}} = 0.000313 \text{ m} = 0.313 \text{ mm}$$

### P.11.4 Torsional Stress and Deflection

**Shear stress:**
$$\tau = \frac{Tr}{J}$$

where:
- $T$ = torque (N·m)
- $r$ = radius (m)
- $J$ = polar moment of inertia (m⁴)

**Solid circular shaft:** $J = \frac{\pi d^4}{32}$

**Hollow circular shaft:** $J = \frac{\pi (d_o^4 - d_i^4)}{32}$

**Angle of twist:**
$$\phi = \frac{TL}{GJ}$$

where $G$ = shear modulus (Pa)

**Example:** Ball screw torsional stiffness

$d = 40$ mm, $L = 1$ m, $G = 80$ GPa (steel)

$$J = \frac{\pi (0.04)^4}{32} = 2.51 \times 10^{-7} \text{ m}^4$$

Torque $T = 50$ N·m:

$$\phi = \frac{50 \times 1}{80 \times 10^9 \times 2.51 \times 10^{-7}} = 0.00249 \text{ rad} = 0.143°$$

---

## P.12 Heat Transfer

### P.12.1 Conduction (Fourier's Law)

$$Q = -kA\frac{dT}{dx}$$

**Steady-state through wall:**
$$Q = \frac{kA\Delta T}{L}$$

where:
- $Q$ = heat transfer rate (W)
- $k$ = thermal conductivity (W/(m·K))
- $A$ = area (m²)
- $\Delta T$ = temperature difference (K)
- $L$ = thickness (m)

**Thermal resistance:** $R_{\text{thermal}} = \frac{L}{kA}$ (K/W)

**Example:** Motor cooling through aluminum housing

$k = 205$ W/(m·K), $A = 0.01$ m², $L = 5$ mm, $\Delta T = 50$ K

$$Q = \frac{205 \times 0.01 \times 50}{0.005} = 20,500 \text{ W}$$

### P.12.2 Convection (Newton's Law of Cooling)

$$Q = hA(T_s - T_\infty)$$

where:
- $h$ = convection coefficient (W/(m²·K))
- $T_s$ = surface temperature (K)
- $T_\infty$ = fluid temperature (K)

**Typical values:**
- Natural air: $h = 5-25$ W/(m²·K)
- Forced air: $h = 10-200$ W/(m²·K)
- Water: $h = 500-10,000$ W/(m²·K)

### P.12.3 Radiation (Stefan-Boltzmann Law)

$$Q = \epsilon \sigma A(T_s^4 - T_\text{surr}^4)$$

where:
- $\epsilon$ = emissivity (0-1)
- $\sigma = 5.67 \times 10^{-8}$ W/(m²·K⁴) (Stefan-Boltzmann constant)
- $T$ in Kelvin (absolute temperature)

---

## P.13 Control Systems Mathematics

### P.13.1 Transfer Functions (Laplace Domain)

**Laplace transform:**
$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t)e^{-st} dt$$

**Common transforms:**

| Time Domain | Laplace Domain |
|-------------|----------------|
| $\delta(t)$ (impulse) | $1$ |
| $u(t)$ (step) | $\frac{1}{s}$ |
| $e^{-at}$ | $\frac{1}{s+a}$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$ |
| $\cos(\omega t)$ | $\frac{s}{s^2 + \omega^2}$ |

**Differentiation:** $\mathcal{L}\{\frac{df}{dt}\} = sF(s) - f(0)$

**Integration:** $\mathcal{L}\{\int_0^t f(\tau)d\tau\} = \frac{F(s)}{s}$

### P.13.2 PID Controller

**Time domain:**
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau)d\tau + K_d \frac{de}{dt}$$

**Laplace domain:**
$$U(s) = \left(K_p + \frac{K_i}{s} + K_d s\right)E(s)$$

**Transfer function:**
$$G_c(s) = K_p + \frac{K_i}{s} + K_d s = \frac{K_d s^2 + K_p s + K_i}{s}$$

**Gains:**
- $K_p$: Proportional gain (immediate response to error)
- $K_i$: Integral gain (eliminates steady-state error)
- $K_d$: Derivative gain (damping, anticipates error)

### P.13.3 First-Order System

**Transfer function:**
$$G(s) = \frac{K}{\tau s + 1}$$

**Step response:**
$$y(t) = K(1 - e^{-t/\tau})$$

where $\tau$ = time constant (63.2% of final value at $t = \tau$)

### P.13.4 Second-Order System

**Transfer function:**
$$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

**Step response characteristics:**
- Rise time: $t_r \approx \frac{1.8}{\omega_n}$ (underdamped)
- Settling time: $t_s \approx \frac{4}{\zeta\omega_n}$ (2% criterion)
- Peak overshoot: $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ (underdamped)

---

## P.14 Statistics and Uncertainty

### P.14.1 Mean and Standard Deviation

**Mean (average):**
$$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$$

**Standard deviation:**
$$\sigma = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2}$$

**Example:** Measuring part dimension 10 times:
Data: 50.01, 50.03, 49.98, 50.02, 50.00, 50.01, 49.99, 50.02, 50.00, 50.01 mm

$$\bar{x} = \frac{500.07}{10} = 50.007 \text{ mm}$$

$$\sigma = 0.015 \text{ mm}$$

### P.14.2 Error Propagation

**Addition/Subtraction:**
$$\sigma_z^2 = \sigma_x^2 + \sigma_y^2$$

**Multiplication/Division:**
$$\left(\frac{\sigma_z}{z}\right)^2 = \left(\frac{\sigma_x}{x}\right)^2 + \left(\frac{\sigma_y}{y}\right)^2$$

**General function $z = f(x, y)$:**
$$\sigma_z^2 = \left(\frac{\partial f}{\partial x}\right)^2\sigma_x^2 + \left(\frac{\partial f}{\partial y}\right)^2\sigma_y^2$$

---

## P.15 Fourier Analysis (Frequency Domain)

### P.15.1 Fourier Series

Periodic signal $f(t)$ with period $T$:

$$f(t) = a_0 + \sum_{n=1}^\infty \left[a_n \cos\left(\frac{2\pi nt}{T}\right) + b_n \sin\left(\frac{2\pi nt}{T}\right)\right]$$

**Coefficients:**
$$a_0 = \frac{1}{T}\int_0^T f(t)dt$$
$$a_n = \frac{2}{T}\int_0^T f(t)\cos\left(\frac{2\pi nt}{T}\right)dt$$
$$b_n = \frac{2}{T}\int_0^T f(t)\sin\left(\frac{2\pi nt}{T}\right)dt$$

### P.15.2 Frequency Analysis Applications

**Vibration analysis:** Decompose vibration signal into frequency components

**Modal testing:** Identify natural frequencies and mode shapes

**Chatter detection:** Monitor cutting forces in frequency domain

---

**End of Engineering Mathematics Appendix**
