# Section 2.5 – Ball Screws for Vertical Axes

## Overview

Ball screws in vertical applications must transmit both dynamic motion forces and continuous gravitational loads. Critical speed, buckling, thermal expansion, and safety become more significant than in horizontal axes. This section addresses vertical-specific ball screw selection, mounting, and integration.

## Vertical Load Considerations

### Continuous Axial Load

Unlike horizontal axes with primarily dynamic loading, vertical ball screws carry constant axial load:

$$F_{axial} = m \times g + F_{accel} + F_{friction}$$

**Upward motion:**
- All forces add (motor works hardest)
- Maximum load condition for sizing

**Downward motion:**
- Gravity assists, motor brakes
- Potential for backdriving if friction too low

### Load Rating Verification

**Dynamic load capacity:**

$$C_{10} = P \times \left(\frac{L_h}{10^6}\right)^{1/3}$$

Where:
- $C_{10}$ = dynamic load rating (N)
- P = equivalent dynamic load (N)
- $L_h$ = rated life (hours)

**For vertical application:**
$$P = m \times g \times SF$$

Use safety factor SF = 2-3 for continuous gravitational load.

## Critical Speed and Buckling

### Critical Speed for Vertical Mounting

**Fundamental critical speed (first mode):**

$$n_{cr} = \frac{60}{2\pi} \times \sqrt{\frac{k}{\frac{m}{L}}}$$

For vertical axis with fixed-supported ends:

$$n_{cr} \approx 4.73^2 \times \frac{d}{L^2} \times \sqrt{\frac{E}{ρ}}$$

Where:
- d = screw root diameter (mm)
- L = unsupported length (mm)
- E = Young's modulus
- ρ = density

**Design guideline:** Operate below 80% of critical speed to avoid resonance.

### Buckling Analysis

Vertical screws can buckle under compressive load when moving upward:

**Euler buckling load:**

$$P_{cr} = \frac{\pi^2 E I}{(K L)^2}$$

Where:
- E = Young's modulus (200 GPa for steel)
- I = area moment of inertia
- K = effective length factor (0.7 for fixed-supported)
- L = unsupported length

**Design requirement:** $P_{cr}$ > 5 × maximum axial load

### Support Bearing Placement

**Typical configurations:**

1. **Short travel (<500mm):** Fixed-supported (bearings at both ends)
2. **Medium travel (500-1000mm):** Fixed-supported with center support bearing
3. **Long travel (>1000mm):** Multiple support bearings every 500-700mm

**Center support benefits:**
- Reduces effective length by ~50%
- Increases critical speed by 4×
- Prevents buckling under compression

## End Mounting Configurations

### Upper End (Motor Side)

**Fixed bearing (typical):**
- Angular contact bearings (back-to-back)
- Constrains axial and radial motion
- Preloaded for rigidity
- Motor coupled to screw

### Lower End

**Supported bearing:**
- Allows thermal expansion
- Radial constraint only
- Simple bearing or floating support

**Thermal expansion:**

$$\Delta L = \alpha \times L \times \Delta T$$

For 800mm steel screw, 10°C rise:
$$\Delta L = 12 \times 10^{-6} \times 800 \times 10 = 0.096 \text{ mm}$$

Supported bearing allows this expansion without preload loss.

## Nut Mounting

### Direct Mounting to Carriage

Most common configuration:
- Nut bolts directly to carriage plate
- Carriage guided by linear rails
- Screw centerline aligned with carriage

**Alignment tolerance:** ±0.05mm between screw axis and carriage motion axis

### Floating Nut Mount

For systems with potential misalignment:
- Nut mounts in housing with radial clearance
- Allows minor misalignment without binding
- Reduces side loading on nut bearings

**Trade-off:** Slightly reduced stiffness vs. tolerance for imperfect alignment

## Lubrication for Vertical Axes

### Grease Lubrication

**Challenge:** Gravity pulls grease downward, starving upper portions.

**Solution:**
- Initial over-greasing
- Reverse direction running-in (pushes grease upward)
- Periodic re-greasing (more frequent than horizontal)

**Grease selection:**
- NLGI Grade 1 or 2
- Lithium or lithium-complex base
- Operating temp range: -20°C to 120°C

### Oil Lubrication (Preferred for Vertical)

**Recirculating system:**
- Oil pump circulates lubricant through nut
- Gravity return to reservoir
- Consistent lubrication regardless of position

**Advantages:**
- Better heat dissipation
- Continuous fresh lubricant supply
- Longer service life

**Disadvantages:**
- More complex system
- Higher cost
- Requires pump and reservoir

## Safety Features

### Mechanical Brake

Essential for vertical ball screws:

**Brake torque requirement:**

$$T_{brake} = \frac{m \times g \times p}{2\pi \times \eta} \times SF$$

Where:
- p = screw pitch (m)
- η = efficiency (0.9 typical)
- SF = safety factor (2.0 minimum)

**Example:**
- Moving mass: 15 kg
- Pitch: 5mm
- $T_{brake}$ = (15 × 9.81 × 0.005) / (2π × 0.9) × 2.0 = 0.26 N·m

**Brake mounting:**
- Between motor and coupling (most common)
- On screw shaft (requires larger brake)
- Spring-applied, electrically-released (fail-safe)

### Anti-Backlash Nuts

Vertical axes benefit from preloaded nuts:

**Double-nut preload:**
- Two nuts with spring between
- Eliminates backlash
- Prevents "dropping" under reverse load

**Lead accuracy nuts:**
- Single nut with oversized balls and preload spacer
- Lower friction than double-nut
- Better efficiency

## Practical Sizing Example

**Requirements:**
- Z-axis travel: 400mm
- Moving mass: 10 kg
- Maximum acceleration: 1 m/s²
- Design life: 5000 hours

**Load calculation:**

Gravitational: $F_g = 10 \times 9.81 = 98.1$ N
Acceleration: $F_a = 10 \times 1.0 = 10$ N
Total upward: $F_{total} = 98.1 + 10 = 108.1$ N

With SF=2.5: $P = 108.1 \times 2.5 = 270$ N

**Screw selection:**

Candidate: 1605 ball screw (16mm diameter, 5mm pitch)
- Dynamic load rating: C = 2800 N
- Check life: $L = 10^6 \times (2800/270)^3 = 1.16 \times 10^9$ revolutions

At 1000mm/min travel speed:
- Rev/min = 1000/5 = 200 rpm
- Hours = $1.16 \times 10^9 / (200 \times 60) = 96,700$ hours

**Result:** Far exceeds 5000-hour requirement. This screw is adequately sized.

**Critical speed check:**

Unsupported length: 500mm (with center support)
$$n_{cr} \approx 4.73^2 \times \frac{13}{500^2} \times \sqrt{\frac{200000}{7.85}} = 5531 \text{ rpm}$$

Operating speed: 200 rpm (max)
Ratio: 200/5531 = 3.6% (excellent margin)

## Key Takeaways

1. **Vertical ball screws** carry continuous gravitational load, requiring higher capacity ratings
2. **Critical speed** and **buckling** are more critical for vertical than horizontal mounting
3. **Center support bearings** dramatically improve critical speed for longer screws
4. **Fixed-supported** mounting (both ends constrained) standard for vertical axes
5. **Mechanical brakes** mandatory for safety—size for 2× gravitational holding torque
6. **Oil lubrication** preferred over grease for vertical applications
7. **Preloaded nuts** eliminate backlash and prevent dropping
8. **Thermal expansion** must be accommodated with supported bearing at non-motor end
9. **Safety factor 2.5-3×** recommended for continuous gravitational loading
10. **Alignment** between screw and carriage critical to prevent side loading

***

**Next**: [Section 2.6 – Motor and Drive Sizing](section-2.6-motor-drive-sizing.md)

**Previous**: [Section 2.4 – Vertical Linear Guides](section-2.4-vertical-linear-guides.md)
