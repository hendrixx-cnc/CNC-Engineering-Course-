# Appendix C: Motor and Drive Sizing

---

## C.1 Stepper Motor Specifications

### C.1.1 NEMA Stepper Motor Frame Sizes

| NEMA Size | Flange (mm) | Length Range (mm) | Shaft Dia (mm) | Typical Torque Range (N·m) | Applications |
|-----------|-------------|------------------|---------------|--------------------------|--------------|
| **NEMA 11** | 28 × 28 | 30-51 | 5 | 0.08-0.15 | Small 3D printers, light actuators |
| **NEMA 14** | 35 × 35 | 30-48 | 5 | 0.15-0.30 | Compact CNC, extruders |
| **NEMA 17** | 42 × 42 | 34-60 | 5 | 0.26-0.65 | 3D printers, desktop CNC, pick-place |
| **NEMA 23** | 57 × 57 | 56-112 | 6.35 or 8 | 0.9-3.0 | Mid-size CNC, plasma tables, routers |
| **NEMA 34** | 86 × 86 | 80-156 | 12.7 or 14 | 4.0-12.0 | Heavy CNC, large gantry systems |
| **NEMA 42** | 110 × 110 | 114-201 | 19 | 12.0-30.0 | Industrial CNC, high-inertia loads |

**Note:** NEMA = National Electrical Manufacturers Association. Number indicates mounting hole spacing in inches × 10 (NEMA 23 = 2.3" spacing).

### C.1.2 Stepper Motor Wiring Configurations

**Bipolar (4-wire):**
- One winding per phase (2 phases total)
- Requires H-bridge driver (reverses current direction)
- Higher torque than unipolar (full coil energized)
- Most common for CNC applications

**Unipolar (6-wire or 8-wire):**
- Center-tapped windings
- Simpler driver (just switches, no H-bridge)
- Lower torque (only half coil energized at a time)
- Obsolete for modern CNC (bipolar preferred)

**Bipolar-Series vs. Bipolar-Parallel (8-wire motors):**
- **Series:** Higher inductance → better low-speed torque, lower top speed
- **Parallel:** Lower inductance → better high-speed torque, higher top speed
- **Rule of thumb:** Series for direct drive, parallel for 2:1+ reduction gearboxes

### C.1.3 Stepper Motor Torque-Speed Curves

**Key Parameters:**
- **Holding Torque ($T_H$):** Maximum torque at 0 RPM (standstill)
- **Pull-out Torque ($T_{PO}$):** Maximum torque before stalling at given speed
- **Pull-in Torque ($T_{PI}$):** Maximum starting torque without ramping
- **Resonance Region:** 100-200 full steps/sec typical (causes vibration/stalling)

**Torque vs. Speed Relationship:**

At low speeds (0-500 RPM):
$$T \approx T_H \left(1 - \frac{\omega}{3000}\right)$$

At high speeds (500+ RPM):
$$T \approx \frac{K_v \cdot V_{supply}}{\omega}$$

where:
- $T$ = available torque (N·m)
- $T_H$ = holding torque (N·m)
- $\omega$ = rotor speed (RPM)
- $K_v$ = motor voltage constant
- $V_{supply}$ = driver supply voltage (V)

**Example Torque Curve (NEMA 23, 3.0 N·m holding torque, 48V supply):**

| Speed (RPM) | Available Torque (N·m) | % of Holding Torque |
|-------------|----------------------|---------------------|
| 0 | 3.00 | 100% |
| 100 | 2.85 | 95% |
| 300 | 2.50 | 83% |
| 600 | 1.80 | 60% |
| 1000 | 1.20 | 40% |
| 1500 | 0.75 | 25% |
| 2000 | 0.50 | 17% |
| 3000 | 0.25 | 8% |

**Increasing High-Speed Torque:**
1. **Increase supply voltage** (most effective): 48V → 72V typically doubles torque at 1500 RPM
2. **Use low-inductance motors:** Reduces L/R time constant, faster current rise
3. **Microstepping with higher current:** 1/8 or 1/16 microstepping smooths motion
4. **Gearbox reduction:** Trade speed for torque (2:1 reduction = 2× torque, 0.5× speed)

---

## C.2 Servo Motor Specifications

### C.2.1 Servo vs. Stepper Comparison

| Characteristic | Stepper Motor | Servo Motor |
|----------------|---------------|-------------|
| **Control type** | Open-loop (no feedback) | Closed-loop (encoder feedback) |
| **Positioning accuracy** | ±0.05° (1/4 step) typical | ±0.001° with high-res encoder |
| **Torque at high speed** | Poor (drops rapidly) | Excellent (flat to rated speed) |
| **Holding torque** | Full torque at standstill | Zero torque at standstill (unless energized) |
| **Overload behavior** | Stalls (loses position) | Faults/shuts down (maintains position tracking) |
| **Efficiency** | 40-60% (always energized) | 80-95% (energized on demand) |
| **Cost** | $ | $$-$$$ |
| **Noise** | Moderate (resonance) | Low (smooth motion) |
| **Best for** | Low cost, open-loop OK | High performance, critical positioning |

### C.2.2 AC Servo Motor Frame Sizes (Standard)

| Frame Size (mm) | Rated Power (W) | Cont. Torque (N·m) | Peak Torque (N·m) | Rated Speed (RPM) | Applications |
|-----------------|----------------|-------------------|------------------|------------------|--------------|
| **40** | 50-100 | 0.16-0.32 | 0.48-0.95 | 3000 | Ultra-compact automation |
| **60** | 100-400 | 0.32-1.27 | 0.95-3.82 | 3000 | Pick-place, light CNC |
| **80** | 400-750 | 1.27-2.39 | 3.82-7.16 | 3000 | Small/mid CNC axes |
| **110** | 750-1500 | 2.39-4.77 | 7.16-14.3 | 3000 | Mid-size CNC, mill axes |
| **130** | 1500-2000 | 4.77-6.37 | 14.3-19.1 | 3000 | Large CNC, high-load axes |
| **180** | 3000-5000 | 9.55-15.9 | 28.6-47.7 | 3000 | Heavy industrial CNC |

**Continuous vs. Peak Torque:**
- **Continuous (rated) torque:** Can run indefinitely without overheating
- **Peak torque:** Available for short bursts (1-2 seconds typical), acceleration/deceleration
- **Duty cycle:** Peak torque limited by thermal constraints (motor winding temperature)

**Encoder Resolution:**
- **Standard:** 2500 PPR (pulses per revolution) → 10,000 counts/rev with quadrature
- **High-resolution:** 10,000-20,000 PPR → 40,000-80,000 counts/rev
- **Absolute encoders:** Retain position when powered off (battery-backed or multi-turn)

### C.2.3 Servo Motor Torque-Speed Curves

**Typical AC Servo Characteristics:**
- Flat torque from 0 to rated speed (3000 RPM typical)
- Constant power above rated speed (torque inversely proportional to speed)
- Peak torque = 3× continuous torque (thermal limit)

**Torque Curve Regions:**

$$
T(\omega) = 
\begin{cases}
T_{cont} & \omega \leq \omega_{rated} \text{ (constant torque region)} \\
\frac{P_{rated}}{\omega} & \omega > \omega_{rated} \text{ (constant power region)}
\end{cases}
$$

where:
- $T_{cont}$ = continuous rated torque (N·m)
- $\omega_{rated}$ = rated speed (rad/s or RPM)
- $P_{rated}$ = rated power (W)

**Example: 1.5 kW, 4.77 N·m servo (rated speed 3000 RPM):**

| Speed (RPM) | Continuous Torque (N·m) | Peak Torque (N·m) | Power (W) |
|-------------|------------------------|------------------|-----------|
| 0 | 4.77 | 14.3 | 0 |
| 1000 | 4.77 | 14.3 | 500 |
| 3000 | 4.77 (rated) | 14.3 | 1500 (rated) |
| 4500 | 3.18 | 9.5 | 1500 |
| 6000 | 2.39 | 7.2 | 1500 |

---

## C.3 Motor Sizing Calculations

### C.3.1 Required Torque Calculation

**Linear Axis (Ball Screw Drive):**

$$T_{motor} = \frac{F \cdot p}{2\pi \eta} + T_{friction} + T_{inertia}$$

where:
- $T_{motor}$ = motor torque required (N·m)
- $F$ = cutting force or load force (N)
- $p$ = ball screw lead (m/rev)
- $\eta$ = efficiency (0.90-0.95 for ball screws)
- $T_{friction}$ = friction torque (guide rails, seals)
- $T_{inertia}$ = torque to accelerate load

**Inertia Torque (Acceleration):**

$$T_{inertia} = J_{total} \cdot \alpha$$

where:
- $J_{total}$ = total reflected inertia (kg·m²)
- $\alpha$ = angular acceleration (rad/s²)

**Reflected Inertia (Linear Load to Motor Shaft):**

$$J_{reflected} = m \cdot \left(\frac{p}{2\pi}\right)^2$$

where:
- $m$ = moving mass (kg)
- $p$ = screw lead (m/rev)

**Example: NEMA 23 stepper sizing for plasma table X-axis**

Given:
- Moving mass: $m = 15$ kg (gantry assembly)
- Ball screw lead: $p = 0.010$ m/rev (10mm/rev, RM2005)
- Cutting force: $F = 50$ N (plasma drag force)
- Max velocity: $v = 200$ mm/s = 0.2 m/s
- Acceleration time: $t = 0.5$ s
- Efficiency: $\eta = 0.90$

**Step 1: Screw speed at max velocity**

$$\omega = \frac{v}{p} = \frac{0.2}{0.010} = 20 \text{ rev/s} = 1200 \text{ RPM}$$

**Step 2: Reflected inertia**

$$J_{reflected} = 15 \times \left(\frac{0.010}{2\pi}\right)^2 = 3.8 \times 10^{-5} \text{ kg·m}^2$$

Motor rotor inertia (NEMA 23): $J_{motor} = 1.2 \times 10^{-4}$ kg·m²

$$J_{total} = J_{motor} + J_{reflected} = 1.58 \times 10^{-4} \text{ kg·m}^2$$

**Step 3: Angular acceleration**

$$\alpha = \frac{\omega}{t} = \frac{20 \times 2\pi}{0.5} = 251 \text{ rad/s}^2$$

**Step 4: Torque components**

Load torque:
$$T_{load} = \frac{50 \times 0.010}{2\pi \times 0.90} = 0.088 \text{ N·m}$$

Inertia torque:
$$T_{inertia} = 1.58 \times 10^{-4} \times 251 = 0.040 \text{ N·m}$$

Friction torque (estimate 10% of load):
$$T_{friction} = 0.010 \text{ N·m}$$

**Total torque required:**
$$T_{required} = 0.088 + 0.040 + 0.010 = 0.138 \text{ N·m}$$

**At 1200 RPM, NEMA 23 (3.0 N·m holding torque, 48V) provides ~1.2 N·m → 8.7× safety factor (adequate)**

### C.3.2 Motor Sizing for Rotary Axis (4th Axis, Spindle Indexer)

**Torque Required:**

$$T = J_{load} \cdot \alpha + T_{friction} + T_{cutting}$$

**Load Inertia (Solid Cylinder):**

$$J = \frac{1}{2} m r^2$$

**Example: Rotary table for indexing**

Given:
- Chuck + part mass: $m = 10$ kg
- Effective radius: $r = 0.1$ m
- Acceleration time: $t = 1$ s to 60 RPM
- Cutting torque: $T_{cutting} = 5$ N·m (milling force × radius)

Load inertia:
$$J_{load} = \frac{1}{2} \times 10 \times 0.1^2 = 0.05 \text{ kg·m}^2$$

Angular acceleration:
$$\alpha = \frac{60 \times 2\pi / 60}{1} = 6.28 \text{ rad/s}^2$$

Inertia torque:
$$T_{inertia} = 0.05 \times 6.28 = 0.314 \text{ N·m}$$

Friction (bearing + worm gear, assume 20%):
$$T_{friction} = 1.0 \text{ N·m}$$

**Total:**
$$T_{required} = 0.314 + 1.0 + 5.0 = 6.3 \text{ N·m}$$

**With 10:1 worm gear (η = 0.50 efficiency):**
$$T_{motor} = \frac{6.3}{10 \times 0.50} = 1.26 \text{ N·m}$$

**NEMA 23 with 3.0 N·m holding torque provides 2.4× margin**

---

## C.4 Stepper Motor Driver Selection

### C.4.1 Driver Voltage and Current Ratings

**Voltage Selection:**
- **24V:** Small steppers (NEMA 17), low speed (<500 RPM)
- **48V:** NEMA 23, medium speed (1000-1500 RPM) - **most common for CNC**
- **72-80V:** NEMA 34, high speed (2000+ RPM), high-inductance motors

**Rule of Thumb:** Driver voltage = 20-30× motor rated voltage

Example: Motor rated 3.0V, 3.0A → use 48-72V driver

**Current Rating:** Driver continuous current ≥ 1.2× motor rated current (for microstepping overhead)

### C.4.2 Microstepping Settings

| Microstep Resolution | Steps/Rev (1.8° motor) | Resolution | Smoothness | Torque Loss | Typical Use |
|---------------------|----------------------|------------|------------|-------------|-------------|
| **Full Step** | 200 | Lowest | Rough, resonance | 0% | Obsolete for CNC |
| **Half Step** | 400 | Low | Better | ~5% | Low-precision applications |
| **1/4 Step** | 800 | Medium | Good | ~10% | General CNC (direct drive) |
| **1/8 Step** | 1600 | High | Smooth | ~15% | Standard CNC setting |
| **1/16 Step** | 3200 | Very High | Very smooth | ~20% | High precision, low speed |
| **1/32 Step** | 6400 | Ultra High | Smoothest | ~25% | Ultra-precision, very low speed |

**Recommendation:**
- **1/8 microstepping** for most CNC (good balance of resolution and torque)
- **1/16 or 1/32** for very low-speed applications (Z-axis fine positioning)
- **1/4 microstepping** for high-speed/high-torque axes (rapids)

### C.4.3 Common Stepper Drivers

| Driver Model | Voltage Range | Current/Axis | Axes | Microstepping | Interface | Price |
|--------------|--------------|--------------|------|---------------|-----------|-------|
| **DM542** | 20-50V DC | 1.0-4.2A | 1 | 1/2 to 1/128 | Step/Dir | $ |
| **DM860H** | 24-80V DC | 2.4-7.2A | 1 | 1/2 to 1/128 | Step/Dir | $$ |
| **Leadshine DM856** | 24-80V AC | 2.0-5.6A | 1 | 1/2 to 1/128 | Step/Dir + RS232 | $$ |
| **Gecko G203V** | 18-80V DC | 0-7.0A | 1 | 1/10 (unique) | Step/Dir | $$$ |
| **ClearPath SDSK** | 48-75V DC | 13A peak | 1 | Servo (encoder) | Step/Dir | $$$$ |

---

## C.5 Servo Drive Selection

### C.5.1 Servo Drive Types

**Pulse/Direction Input (Step/Dir):**
- Acts like stepper driver (accepts pulse train from motion controller)
- Closed-loop internally (encoder feedback to drive)
- Easiest retrofit for stepper-based systems
- Limited tuning capability

**Analog Velocity Input (±10V):**
- Voltage proportional to speed
- Common on older CNC controls
- Requires separate controller for position loop

**Digital Fieldbus (EtherCAT, CANopen, Modbus):**
- High-speed networked communication
- Advanced tuning and diagnostics
- Synchronized multi-axis motion
- Required for complex path planning

### C.5.2 Servo Drive Sizing

**Drive Continuous Current:** Must meet or exceed motor continuous current rating.

**Drive Peak Current:** Must provide motor peak current for acceleration/deceleration (typically 3× continuous).

**Bus Voltage:** Common DC bus voltages:
- **48V DC:** Small servos (<400W)
- **300-340V DC:** Standard (200-240V AC rectified) - **most common**
- **550-680V DC:** High power (380-480V AC rectified)

**Regenerative Braking:**
- Energy returned during deceleration charges DC bus
- **Brake resistor** dissipates excess energy if bus voltage rises too high
- Size resistor for duty cycle: $P_{brake} = \frac{1}{2} J \omega^2 / t_{decel}$ averaged over cycle time

### C.5.3 Servo Tuning Parameters

**PID Gains (Position Loop):**
- **$K_p$ (Proportional):** Higher = stiffer, faster response, more oscillation/overshoot
- **$K_i$ (Integral):** Eliminates steady-state error, can cause instability if too high
- **$K_d$ (Derivative):** Dampens oscillation, reduces overshoot

**Typical starting values (requires tuning per application):**
- $K_p = 100$ (position gain)
- $K_i = 5$ (eliminate droop under load)
- $K_d = 10$ (damping)

**Tuning procedure (Ziegler-Nichols method):**
1. Set $K_i = 0$, $K_d = 0$
2. Increase $K_p$ until sustained oscillation occurs → note critical gain $K_c$
3. Set $K_p = 0.6 \times K_c$
4. Set $K_i = 1.2 \times K_c / T_c$ (where $T_c$ = oscillation period)
5. Set $K_d = 0.075 \times K_c \times T_c$
6. Fine-tune by observing step response

---

## C.6 VFD (Variable Frequency Drive) for Spindle Motors

### C.6.1 VFD Sizing

**Power Rating:** VFD continuous kW ≥ motor nameplate kW

**Overload Capacity:**
- **110% continuous:** General purpose
- **150% for 60s:** Heavy duty (frequent start/stop, high inertia loads)

**Example:** 2.2 kW spindle motor → minimum 2.2 kW VFD, recommend 3.0 kW VFD for margin

### C.6.2 VFD Control Modes

| Mode | Description | Best For | Torque at Low Speed |
|------|-------------|----------|---------------------|
| **V/Hz (Scalar)** | Voltage proportional to frequency | Constant-torque loads, simple spindles | Poor (<30 Hz) |
| **Sensorless Vector** | Estimates rotor position/flux | Improved low-speed torque, variable loads | Good (>5 Hz) |
| **Closed-Loop Vector** | Encoder feedback | Constant torque to 0 Hz, precision speed | Excellent (0 Hz) |

**CNC Spindle Recommendation:** Sensorless vector (good performance, no encoder cost)

### C.6.3 VFD Input/Output Parameters

**Input:**
- Single-phase 230V AC (up to 2.2 kW typical)
- Three-phase 230V or 400V AC (3 kW and above)
- **Derating:** 3-phase VFD run on single-phase input must be derated 50% (e.g., 4 kW VFD → 2 kW max on 1-phase input)

**Output:**
- Three-phase AC, variable frequency (0-400 Hz typical)
- PWM waveform (carrier frequency 4-16 kHz adjustable)
- **Do NOT use motor overload relays on output** (VFD has internal protection)

**Control Signals:**
- **Speed reference:** 0-10V analog, 4-20mA, or Modbus/RS485
- **Run/Stop:** Digital input (24V or dry contact)
- **Fault output:** Relay output for E-stop circuit integration

**Example VFD Wiring (2.2 kW spindle, Huanyang-style VFD):**
- Terminals R, S, T: 230V AC single-phase input (or 3-phase)
- Terminals U, V, W: 3-phase output to spindle motor
- Terminals DCM, VI: 0-10V speed reference from CNC controller
- Terminals DCM, FOR: Run command (close to start spindle)
- Terminals DCM, REV: Reverse command (rarely used for CNC)

---

**End of Motor and Drive Sizing Appendix**
