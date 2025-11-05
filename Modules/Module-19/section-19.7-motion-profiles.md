# 19.7 Motion Profiles

## What is a Motion Profile?

**Motion Profile**: The velocity (and acceleration) vs. time curve for a single move.

**Purpose**: Define how system accelerates from rest, maintains velocity, and decelerates to target position while respecting kinematic constraints.

**Profile Types**:
1. **Trapezoidal**: Constant acceleration (simple, widely used)
2. **S-curve**: Jerk-limited (smooth, better for high-speed)
3. **Polynomial**: Higher-order (optimal for specific criteria)
4. **Bang-bang**: Minimum time (aggressive, rarely used in CNC)

## Trapezoidal Velocity Profile

### Profile Structure

**Three Phases**:
1. **Acceleration**: Constant acceleration from 0 to $v_{max}$
2. **Constant Velocity**: Cruise at $v_{max}$
3. **Deceleration**: Constant deceleration from $v_{max}$ to 0

**Velocity vs. Time**:
```
Velocity
   |         ___________  <-- vmax
   |        /           \
   |       /             \
   |      /               \
   |_____/                 \_____
   |____|_____|_____|_____|____|___ Time
      t_a    t_c         t_d
```

Where:
- $t_a$ = acceleration time
- $t_c$ = constant velocity (cruise) time
- $t_d$ = deceleration time
- $v_{max}$ = maximum velocity (cruise velocity)

### Mathematical Formulation

**Given**:
- Distance: $d$ (total move distance)
- Max velocity: $v_{max}$
- Max acceleration: $a_{max}$

**Calculate Acceleration Time**:
$$t_a = \frac{v_{max}}{a_{max}}$$

**Distance During Acceleration**:
$$d_a = \frac{1}{2} a_{max} t_a^2 = \frac{v_{max}^2}{2 a_{max}}$$

**Distance During Deceleration** (assuming same deceleration rate):
$$d_d = d_a = \frac{v_{max}^2}{2 a_{max}}$$

**Distance During Cruise**:
$$d_c = d - d_a - d_d$$

**Cruise Time**:
$$t_c = \frac{d_c}{v_{max}}$$

**Total Time**:
$$T = t_a + t_c + t_d = 2t_a + t_c$$

### Example Calculation

**Given**:
- Distance: $d = 10$ inches
- Max velocity: $v_{max} = 200$ IPM = 3.33 in/s
- Max acceleration: $a_{max} = 100$ in/s²

**Calculate**:
- $t_a = 3.33 / 100 = 0.0333$ s
- $d_a = 3.33^2 / (2 × 100) = 0.0555$ inches
- $d_d = 0.0555$ inches
- $d_c = 10 - 0.0555 - 0.0555 = 9.889$ inches
- $t_c = 9.889 / 3.33 = 2.969$ s
- $T = 0.0333 + 2.969 + 0.0333 = 3.035$ s

**Trajectory**:

| Phase | Time (s) | Velocity (in/s) | Position (in) |
|-------|----------|-----------------|---------------|
| Start | 0.000 | 0.00 | 0.000 |
| Accel | 0.0333 | 3.33 | 0.056 |
| Cruise | 3.002 | 3.33 | 9.944 |
| Decel | 3.035 | 0.00 | 10.000 |

### Short Move (Triangular Profile)

**Problem**: If move distance too short, never reaches $v_{max}$.

**Condition**: $d < \frac{v_{max}^2}{a_{max}}$ (total distance less than accel + decel distance)

**Solution**: **Triangular profile** (accelerate, then immediately decelerate)

**Peak Velocity**:
$$v_{peak} = \sqrt{a_{max} \cdot d}$$

**Example**:
- Distance: $d = 0.5$ inches
- Max acceleration: $a_{max} = 100$ in/s²
- Check: $\frac{v_{max}^2}{a_{max}} = 3.33^2 / 100 = 0.111$ inches
- Since 0.5 > 0.111, **trapezoidal profile OK** (will reach $v_{max}$)

**Short Example**:
- Distance: $d = 0.05$ inches
- Since 0.05 < 0.111, **triangular profile**
- $v_{peak} = \sqrt{100 × 0.05} = 2.24$ in/s (never reaches 3.33 in/s)
- $t_a = 2.24 / 100 = 0.0224$ s
- $T = 2 × t_a = 0.0448$ s

### Advantages and Disadvantages

**Advantages**:
- Simple to compute
- Well-understood
- Minimal computation (real-time friendly)
- Predictable

**Disadvantages**:
- Infinite jerk (instant acceleration change)
- Excites mechanical resonances
- Harsh motion (vibration, noise)
- Poor surface finish in some applications

**When to Use**:
- General-purpose machining
- Robust mechanical systems (stiff, well-damped)
- When cycle time critical (fastest profile type)

## S-Curve (Jerk-Limited) Velocity Profile

### Profile Structure

**Seven Phases**:
1. **Jerk-in** (acceleration increasing)
2. **Constant acceleration**
3. **Jerk-out** (acceleration decreasing to zero)
4. **Constant velocity** (cruise)
5. **Jerk-in** (deceleration starting)
6. **Constant deceleration**
7. **Jerk-out** (deceleration decreasing to zero)

**Velocity vs. Time** (S-curve shape):
```
Velocity
   |           ____________  <-- vmax
   |         /             \
   |        /               \
   |       /                 \
   |     /                     \
   |____/                       \____
   |___|___|___|___|___|___|___|___|___ Time
     t1  t2  t3  t4  t5  t6  t7
```

**Acceleration vs. Time**:
```
Acceleration
   |     _______             <-- amax
   |    /       \
   |___/         \___________
   |                   \___/ <-- deceleration
```

**Jerk vs. Time**:
```
Jerk
   | __                  __
   ||  |                |  |
   ||__|________________|__|___
       |                |
       |________________|
```

### Mathematical Formulation

**Given**:
- Distance: $d$
- Max velocity: $v_{max}$
- Max acceleration: $a_{max}$
- Max jerk: $j_{max}$

**Jerk Phase Duration**:
$$t_j = \frac{a_{max}}{j_{max}}$$

**Acceleration Phase Segments**:
- Jerk-in: $t_1 = t_j$
- Constant acceleration: $t_2$ (calculated)
- Jerk-out: $t_3 = t_j$

**Velocity at End of Jerk-In**:
$$v_1 = \frac{1}{2} j_{max} t_j^2 = \frac{a_{max}^2}{2 j_{max}}$$

**Total Acceleration Phase**:
$$t_a = t_1 + t_2 + t_3 = 2t_j + t_2$$

**Velocity After Acceleration Phase**:
$$v_{max} = v_1 + a_{max} t_2 + v_1 = \frac{a_{max}^2}{j_{max}} + a_{max} t_2$$

Solve for $t_2$:
$$t_2 = \frac{v_{max}}{a_{max}} - \frac{a_{max}}{j_{max}}$$

**Distance During Acceleration**:
$$d_a = \frac{1}{6} j_{max} t_1^3 + v_1 t_2 + \frac{1}{2} a_{max} t_2^2 + v_1 t_2 + \frac{1}{2} a_{max} t_2^2 + \text{(jerk-out contribution)}$$

(Full equation complex; typically computed numerically)

**Simplified** (for symmetric accel/decel):
$$d_a \approx \frac{v_{max}^2}{2a_{max}} + \frac{a_{max}^2}{j_{max}}$$

### Example Calculation

**Given**:
- Distance: $d = 10$ inches
- Max velocity: $v_{max} = 200$ IPM = 3.33 in/s
- Max acceleration: $a_{max} = 100$ in/s²
- Max jerk: $j_{max} = 1000$ in/s³

**Calculate**:
- $t_j = 100 / 1000 = 0.1$ s
- $v_1 = 100^2 / (2 × 1000) = 5.0$ in/s²·s = ... (check units: should be velocity)
- Actually: $v_1 = \frac{1}{2} × 1000 × 0.1^2 = 5$ in/s
- $t_2 = 3.33 / 100 - 100/1000 = 0.0333 - 0.1 = -0.0667$ s **(negative! Problem)**

**Interpretation**: Jerk limit too low; cannot reach $v_{max}$ before jerk phase ends.

**Adjust**: Either increase $j_{max}$ or accept lower peak velocity.

**Revised**: $j_{max} = 5000$ in/s³
- $t_j = 100 / 5000 = 0.02$ s
- $v_1 = 0.5 × 5000 × 0.02^2 = 1.0$ in/s
- $t_2 = 3.33 / 100 - 100/5000 = 0.0333 - 0.02 = 0.0133$ s (OK!)
- $t_a = 2 × 0.02 + 0.0133 = 0.0533$ s

**Distance During Acceleration** (approximate):
$$d_a \approx \frac{3.33^2}{2 × 100} + \frac{100^2}{5000} = 0.0555 + 2.0 = 2.056$$ inches

**Note**: Exact calculation requires numerical integration; controllers compute this iteratively.

### Advantages and Disadvantages

**Advantages**:
- Smooth motion (limited jerk)
- Reduced vibration and resonance excitation
- Better surface finish
- Less mechanical stress (bearings, frame)
- Quieter operation

**Disadvantages**:
- More complex computation (but manageable)
- Slightly longer cycle time (jerk phases add time)
- More parameters to tune ($j_{max}$)

**When to Use**:
- High-speed machining (vibration-sensitive)
- Lightweight/flexible structures
- Better surface finish desired
- Noise reduction important

**Typical Applications**:
- 3D printers (eliminates ringing)
- High-speed routers
- Pick-and-place machines
- Laser cutters

## Polynomial Trajectories

### Concept

**Polynomial Trajectory**: Position as polynomial function of time.

**General Form**:
$$s(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3 + \cdots + a_n t^n$$

**Derivatives**:
- Velocity: $v(t) = \dot{s}(t) = a_1 + 2a_2 t + 3a_3 t^2 + \cdots$
- Acceleration: $a(t) = \ddot{s}(t) = 2a_2 + 6a_3 t + \cdots$
- Jerk: $j(t) = \dddot{s}(t) = 6a_3 + \cdots$

### Cubic Polynomial (3rd Order)

**Application**: Point-to-point move with specified start/end conditions.

**Boundary Conditions**:
- $s(0) = 0$ (start position)
- $s(T) = d$ (end position)
- $v(0) = 0$ (start velocity)
- $v(T) = 0$ (end velocity)

**Polynomial**:
$$s(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3$$

**Solve for Coefficients**:
From boundary conditions:
- $a_0 = 0$
- $a_1 = 0$
- $a_2 = \frac{3d}{T^2}$
- $a_3 = -\frac{2d}{T^3}$

**Result**:
$$s(t) = \frac{3d}{T^2} t^2 - \frac{2d}{T^3} t^3 = d \left( 3\left(\frac{t}{T}\right)^2 - 2\left(\frac{t}{T}\right)^3 \right)$$

**Velocity**:
$$v(t) = \frac{6d}{T^2} t - \frac{6d}{T^3} t^2$$

**Peak Velocity** (at $t = T/2$):
$$v_{peak} = \frac{6d}{T^2} \frac{T}{2} - \frac{6d}{T^3} \frac{T^2}{4} = \frac{3d}{T} - \frac{3d}{2T} = \frac{3d}{2T}$$

**Acceleration**:
$$a(t) = \frac{6d}{T^2} - \frac{12d}{T^3} t$$

**Peak Acceleration** (at $t = 0$ and $t = T$):
$$a_{peak} = \frac{6d}{T^2}$$

**Example**:
- Distance: $d = 10$ inches
- Move time: $T = 3$ seconds
- $v_{peak} = (3 × 10) / (2 × 3) = 5$ in/s
- $a_{peak} = (6 × 10) / 3^2 = 6.67$ in/s²

### Quintic Polynomial (5th Order)

**Boundary Conditions** (more constraints):
- $s(0) = 0$, $s(T) = d$
- $v(0) = 0$, $v(T) = 0$
- $a(0) = 0$, $a(T) = 0$ (smooth start and stop)

**Polynomial**:
$$s(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3 + a_4 t^4 + a_5 t^5$$

**Coefficients** (derived from boundary conditions):
$$s(t) = d \left( 10\left(\frac{t}{T}\right)^3 - 15\left(\frac{t}{T}\right)^4 + 6\left(\frac{t}{T}\right)^5 \right)$$

**Advantage**: Zero acceleration at start and end (even smoother than cubic).

**Peak Velocity** (at $t = T/2$):
$$v_{peak} = \frac{15d}{8T}$$

**Peak Acceleration**:
$$a_{peak} = \frac{30d}{T^2} \text{ (at specific times, not start/end)}$$

**When to Use**:
- Ultra-smooth motion required
- Minimizing jerk
- Synchronizing with other systems (robotics)

## Minimum-Time Trajectories

### Bang-Bang Control

**Concept**: Maximum acceleration, then maximum deceleration (no cruise phase).

**Profile**:
- Accelerate at $a_{max}$ for time $t_a$
- Immediately decelerate at $a_{max}$ for time $t_d = t_a$

**Minimum Time**:
$$T_{min} = 2 \sqrt{\frac{d}{a_{max}}}$$

**Example**:
- Distance: $d = 10$ inches
- Max acceleration: $a_{max} = 100$ in/s²
- $T_{min} = 2 \sqrt{10 / 100} = 2 × 0.316 = 0.632$ seconds

**Compare to Trapezoidal** (with cruise at 200 IPM):
- Trapezoidal time: 3.035 seconds (from earlier example)
- **Bang-bang 4.8× faster** (but exceeds velocity limit!)

**Reality Check**: Must respect velocity limit.
- Peak velocity (bang-bang): $v_{peak} = a_{max} t_a = 100 × 0.316 = 31.6$ in/s = 1896 IPM
- Limit: 200 IPM = 3.33 in/s
- **Cannot use bang-bang** (violates velocity constraint)

**Application**: Very short moves where $v_{max}$ not reached (triangular profile ≈ bang-bang).

### Optimal Time with Constraints

**Problem**: Find fastest trajectory respecting $v_{max}$, $a_{max}$, $j_{max}$.

**Solution**: Typically trapezoidal or S-curve (depending on jerk limit).

**Algorithm**:
1. Assume trapezoidal, check if $v_{max}$ reached
2. If not, triangular profile (minimum time for given $a_{max}$)
3. If jerk limit active, S-curve profile
4. Check all constraints; reduce velocity/acceleration as needed

**Modern CNC Controllers**: Automatically compute near-optimal trajectories using look-ahead and constraint checking.

## Motion Profile Selection

### Application-Based Selection

**High-Speed Machining**:
- **Profile**: S-curve (jerk-limited)
- **Reason**: Smooth motion, reduced vibration, better finish
- **Typical**: $j_{max}$ = 50,000-200,000 in/s³

**Heavy Machining**:
- **Profile**: Trapezoidal (simple)
- **Reason**: Stiff machine, cutting forces dominate, simplicity preferred
- **Typical**: Standard acceleration limits

**Precision Positioning**:
- **Profile**: Polynomial (quintic) or S-curve
- **Reason**: Smooth, no jerks, repeatable
- **Typical**: Slow, controlled moves

**Rapid Positioning**:
- **Profile**: Trapezoidal (maximum speed)
- **Reason**: Speed priority, no cutting
- **Typical**: High $a_{max}$, high $v_{max}$

### Trade-Offs Summary

| Profile | Cycle Time | Smoothness | Complexity | Surface Finish |
|---------|------------|------------|------------|----------------|
| Trapezoidal | Fastest | Harsh | Simple | Good |
| S-curve | Moderate | Smooth | Moderate | Excellent |
| Cubic Poly | Slow | Very Smooth | Moderate | Excellent |
| Quintic Poly | Slowest | Smoothest | Complex | Excellent |

## Velocity Profile Optimization

### Adaptive Feedrate

**Concept**: Adjust feedrate based on cutting conditions.

**Inputs**:
- Cutting force measurement (dynamometer or motor current)
- Surface finish requirements
- Tool wear state

**Algorithm**:
1. Monitor cutting force
2. If force > threshold: Reduce feedrate
3. If force < threshold: Increase feedrate
4. Stay within $v_{max}$ and $a_{max}$

**Example**:
- Programmed feedrate: 100 IPM
- Heavy cut detected: Reduce to 70 IPM (temporary)
- Light cut: Restore to 100 IPM

**Application**: Optimizing cycle time while preventing tool breakage.

### Constant Surface Speed (CSS)

**Lathe Application**: Maintain constant cutting speed at tool edge as diameter changes.

**Formula**:
$$v = \frac{\pi D N}{12}$$

where:
- $v$ = surface speed (SFM)
- $D$ = workpiece diameter (inches)
- $N$ = spindle RPM

**Maintain Constant $v$**: Adjust $N$ as $D$ changes.

**Example**:
- Target surface speed: 300 SFM
- At $D = 4$": $N = (300 × 12) / (\pi × 4) = 286$ RPM
- At $D = 2$": $N = (300 × 12) / (\pi × 2) = 573$ RPM

**G-Code**: G96 (Constant Surface Speed mode)

**Trajectory Planning**: Controller adjusts spindle speed profile synchronized with motion.

## Summary

Motion profiles define velocity vs. time for moves:

**Key Profile Types**:
1. **Trapezoidal**: Simple, fast, harsh (infinite jerk)
2. **S-curve**: Smooth, jerk-limited, best for high-speed
3. **Polynomial**: Very smooth, flexible boundary conditions

**Selection Criteria**:
- **Cycle time**: Trapezoidal fastest
- **Surface finish**: S-curve or polynomial best
- **Mechanical stress**: S-curve reduces wear and vibration

**Modern Controllers**: Automatically generate near-optimal profiles based on constraints.

**Next Steps**:
- Multi-axis coordination (Section 19.8)
- Look-ahead and path blending (Section 19.9)
- Implementation in LinuxCNC/Mach4 (Sections 19.10-19.11)

---

**Next**: [19.8 Multi-Axis Coordination](section-19.8-multi-axis-coordination.md)
