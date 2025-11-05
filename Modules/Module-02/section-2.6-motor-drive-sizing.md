# Section 2.6 – Motor and Drive Sizing

## Overview

Motor sizing for vertical axes must account for continuous gravitational torque, acceleration forces, and friction—all while maintaining adequate thermal margins. This section presents systematic motor selection methodology specific to Z-axis applications, including torque calculations, inertia matching, and servo tuning considerations.

## Torque Requirements

### Gravitational Torque (Continuous)

The motor must supply continuous torque to resist gravity:

$$T_{gravity} = \frac{m \times g \times p}{2\pi \times \eta}$$

Where:
- m = moving mass (kg)
- g = 9.81 m/s²
- p = ball screw pitch (m)
- η = ball screw efficiency (0.90-0.95 typical)

**Example:**
- Moving mass: 12 kg
- Pitch: 5mm = 0.005 m
- Efficiency: 0.90

$$T_g = \frac{12 \times 9.81 \times 0.005}{2\pi \times 0.90} = \frac{0.589}{5.65} = 0.104 \text{ N·m}$$

### Acceleration Torque (Dynamic)

Torque required for acceleration:

$$T_{accel} = \frac{m \times a \times p}{2\pi \times \eta} + J_{total} \times \alpha$$

Where:
- a = linear acceleration (m/s²)
- $J_{total}$ = total system inertia (kg·m²)
- α = angular acceleration (rad/s²)

**Relationship:** $\alpha = \frac{2\pi \times a}{p}$

**Example (continued):**
- Acceleration: 2 m/s²
- System inertia: $8 \times 10^{-6}$ kg·m²

Linear component:
$$T_{linear} = \frac{12 \times 2 \times 0.005}{2\pi \times 0.90} = 0.021 \text{ N·m}$$

Rotational component:
$$\alpha = \frac{2\pi \times 2}{0.005} = 2513 \text{ rad/s}^2$$
$$T_{rotational} = 8 \times 10^{-6} \times 2513 = 0.020 \text{ N·m}$$

$$T_{accel} = 0.021 + 0.020 = 0.041 \text{ N·m}$$

### Friction Torque

Friction from linear guides and seals:

$$T_{friction} = \frac{\mu \times F_{normal} \times p}{2\pi}$$

Typically 5-15% of gravitational torque for well-lubricated systems.

**Simplified:** $T_{friction} \approx 0.10 \times T_{gravity}$

**Example:** $T_{friction} = 0.10 \times 0.104 = 0.010$ N·m

### Total Torque Requirements

**Moving upward (maximum):**
$$T_{up} = T_{gravity} + T_{accel} + T_{friction}$$
$$T_{up} = 0.104 + 0.041 + 0.010 = 0.155 \text{ N·m}$$

**Moving downward:**
$$T_{down} = -T_{gravity} + T_{accel} + T_{friction}$$
$$T_{down} = -0.104 + 0.041 + 0.010 = -0.053 \text{ N·m}$$

(Negative indicates motor brakes instead of drives)

**With counterbalance (ideal):**
$$T_{up,balanced} = T_{accel} + T_{friction} = 0.051 \text{ N·m}$$
$$T_{down,balanced} = T_{accel} + T_{friction} = 0.051 \text{ N·m}$$

**Benefit:** Symmetric torque requirements, 67% reduction in peak torque.

## Motor Selection

### Continuous Torque Rating

Motor must handle RMS torque over duty cycle:

**Without counterbalance:**

$$T_{RMS} = \sqrt{\frac{T_{gravity}^2 \times t_{total} + T_{peak}^2 \times t_{accel}}{t_{cycle}}}$$

**With counterbalance:**

$$T_{RMS} = \sqrt{\frac{T_{accel}^2 \times t_{accel}}{t_{cycle}}}$$

**Example duty cycle:**
- Cycle time: 10 seconds
- Acceleration time: 1 second
- Constant velocity: 8 seconds
- Deceleration: 1 second

Without counterbalance:
$$T_{RMS} = \sqrt{\frac{0.104^2 \times 10 + 0.155^2 \times 1}{10}} = 0.111 \text{ N·m}$$

With counterbalance:
$$T_{RMS} = \sqrt{\frac{0.051^2 \times 2}{10}} = 0.023 \text{ N·m}$$

**Result:** Counterbalancing reduces RMS torque by 79%.

### Peak Torque Capability

Motor must provide peak torque for acceleration:

$$T_{peak} \geq T_{up} \times SF$$

Safety factor: SF = 1.5-2.0 typical

**Example:** $T_{peak,required} = 0.155 \times 1.5 = 0.233$ N·m

### Motor Selection Example

**Requirements:**
- RMS torque: 0.111 N·m (without counterbalance) or 0.023 N·m (with)
- Peak torque: 0.233 N·m
- Speed requirement: 1000 mm/min = 200 RPM (5mm pitch)

**NEMA 23 servo motor candidate:**
- Continuous torque: 0.32 N·m
- Peak torque: 0.96 N·m
- Rated speed: 3000 RPM
- Rotor inertia: $3.0 \times 10^{-6}$ kg·m²

**Verification:**
- Continuous: 0.32 > 0.111 ✓ (margin: 188%)
- Peak: 0.96 > 0.233 ✓ (margin: 312%)
- Speed: 3000 > 200 ✓ (adequate)

**Conclusion:** NEMA 23 adequate without counterbalance, significantly oversized with counterbalance. Could downsize to NEMA 17 with counterbalancing.

## Inertia Matching

### System Inertia Calculation

**Total reflected inertia:**

$$J_{total} = J_{motor} + J_{coupling} + J_{screw} + J_{reflected}$$

**Reflected load inertia:**

$$J_{reflected} = \frac{m}{(2\pi/p)^2}$$

**Example:**
- Moving mass: 12 kg
- Pitch: 5mm

$$J_{reflected} = \frac{12}{(2\pi/0.005)^2} = \frac{12}{1,579,137} = 7.60 \times 10^{-6} \text{ kg·m}^2$$

**Inertia ratio:**

$$IR = \frac{J_{reflected}}{J_{motor}} = \frac{7.60 \times 10^{-6}}{3.0 \times 10^{-6}} = 2.53:1$$

**Optimal range:** 1:1 to 3:1

**Result:** Inertia ratio is within optimal range for good servo response.

### Improving Inertia Ratio

If inertia ratio too high (>5:1):

**Option 1: Reduce moving mass**
- Lightweight materials
- Structural optimization
- Most beneficial overall

**Option 2: Increase ball screw pitch**
- Reduces reflected inertia (squared relationship)
- Trade-off: Lower resolution, higher gravitational torque

**Option 3: Larger motor**
- Higher rotor inertia
- More expensive, heavier

## Drive Sizing

### Drive Current Requirements

**Peak current:**

$$I_{peak} = \frac{T_{peak}}{K_t}$$

Where $K_t$ = motor torque constant (N·m/A)

**RMS current:**

$$I_{RMS} = \frac{T_{RMS}}{K_t}$$

**Example:**
- Motor $K_t = 0.12$ N·m/A
- Peak torque: 0.233 N·m
- RMS torque: 0.111 N·m

$$I_{peak} = \frac{0.233}{0.12} = 1.94 \text{ A}$$
$$I_{RMS} = \frac{0.111}{0.12} = 0.93 \text{ A}$$

**Drive selection:**
- Peak capability: >2× peak current = 3.9 A
- Continuous rating: >1.5× RMS current = 1.4 A

**Typical NEMA 23 servo drive:** 5A peak, 2.5A continuous (adequate)

### Voltage Requirements

**Peak voltage at maximum speed:**

$$V_{peak} = K_e \times \omega_{max} + I_{peak} \times R$$

Where:
- $K_e$ = back-EMF constant (V/(rad/s))
- $\omega_{max}$ = maximum angular velocity
- R = winding resistance

**For most servo systems:** 24-48V DC bus adequate for speeds <3000 RPM

## Servo Tuning for Vertical Axes

### Challenge: Gravitational Bias

Without counterbalance, the servo sees asymmetric loading:
- Upward motion: Motor works hard
- Downward motion: Gravity assists

**Effect on tuning:**
- Standard PID gains may cause overshoot in down direction
- Underdamped response when changing direction
- Difficult to achieve crisp acceleration profiles

### Tuning with Counterbalance

Properly balanced system eliminates gravitational bias:
- Symmetric response in both directions
- Standard tuning procedures apply
- Better overall performance

**Recommendation:** Always implement counterbalancing before final servo tuning.

### Feed-Forward Compensation

For systems without perfect counterbalance:

**Gravity feed-forward:**

$$FF_{gravity} = T_{gravity} \times \text{sign}(velocity)$$

Add to commanded torque to cancel gravitational bias.

**Implementation:** Available in advanced servo drives (e.g., LinuxCNC HAL, industrial drives)

### Typical Tuning Parameters

**PID gains (starting point):**
- Proportional: $K_p = 100-500$ (depending on inertia ratio)
- Integral: $K_i = 1-10$ (start low, increase to eliminate steady-state error)
- Derivative: $K_d = 0.1-1.0$ (damping)

**Feed-forward:**
- Velocity FF: 0.8-1.0 (for smooth motion)
- Acceleration FF: 0.5-0.9 (reduces lag during accel)

**Tuning sequence:**
1. Set all gains to zero
2. Increase $K_p$ until stable oscillation
3. Back off $K_p$ by 50%
4. Add $K_d$ for damping
5. Add small $K_i$ to eliminate offset
6. Add velocity and acceleration FF for smooth motion
7. Verify response in both directions

## Mechanical Brake Sizing

### Holding Torque Requirement

Brake must prevent motion on power loss:

$$T_{brake} = T_{gravity} \times SF_{brake}$$

Safety factor: 2.0 minimum, 3.0 recommended for critical applications

**Example:**
$$T_{brake} = 0.104 \times 3.0 = 0.31 \text{ N·m}$$

### Brake Types

**Spring-applied, electrically-released:**
- Fail-safe (engages on power loss)
- Most common for servo motors
- Integrated or external mounting

**Electromagnetic holding brake:**
- Requires continuous power to engage
- Not suitable as safety brake
- Used for positioning hold only

### Brake Integration

**Motor-mounted brake (preferred):**
- Compact package
- Direct shaft mounting
- Brake between motor and coupling

**Shaft-mounted brake:**
- External to motor
- Larger brake capacity available
- More complex installation

## Practical Example: Complete System

**Machine specifications:**
- Z-axis travel: 500mm
- Moving mass: 15 kg (spindle + carriage)
- Maximum cutting force: 1000 N
- Required acceleration: 1.5 m/s²
- Maximum speed: 1500 mm/min

**Ball screw selection:** 2005 (20mm dia, 5mm pitch)

**Counterbalance:** Gas spring, 147 N (balances 15kg mass)

**Torque calculations:**

Gravitational (before counterbalance): 
$$T_g = \frac{15 \times 9.81 \times 0.005}{2\pi \times 0.90} = 0.130 \text{ N·m}$$

Gravitational (after counterbalance): ~0 N·m (balanced)

Acceleration:
$$T_{accel} = \frac{15 \times 1.5 \times 0.005}{2\pi \times 0.90} + J \times \alpha = 0.020 + 0.025 = 0.045 \text{ N·m}$$

Total required (with counterbalance): 0.050 N·m

**Motor selection:** NEMA 23, 0.6 N·m rated torque
- Margin: 0.6 / 0.05 = 12× (excellent)
- Inertia ratio: 2.1:1 (optimal)

**Drive selection:** 5A peak, 48V bus

**Brake sizing:** 0.130 × 3 = 0.39 N·m minimum
- Selected: 0.5 N·m motor-integrated brake

## Key Takeaways

1. **Gravitational torque** dominates vertical axis motor sizing
2. **Counterbalancing** reduces motor torque requirements by 50-70%
3. **RMS torque** determines thermal capacity; peak torque determines acceleration capability
4. **Inertia ratio** should be 1:1 to 3:1 for optimal servo response
5. **Drive sizing** must accommodate peak current with margin
6. **Servo tuning** simplified dramatically with proper counterbalancing
7. **Mechanical brakes** mandatory with 2-3× safety factor on holding torque
8. **Feed-forward compensation** can improve performance when perfect balance impractical
9. **Motor selection** with counterbalance allows downsizing by one NEMA size typically
10. **System approach:** Design counterbalance first, then size motor for dynamic loads only

***

**Next**: [Section 2.7 – Thermal Management](section-2.7-thermal-management.md)

**Previous**: [Section 2.5 – Ball Screws for Vertical Axes](section-2.5-ball-screw-vertical.md)
