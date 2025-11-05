# 19.8 Multi-Axis Coordination

## The Coordination Challenge

**Single-Axis Motion**: Straightforward—move one axis from point A to point B.

**Multi-Axis Motion**: Complex—multiple axes must move simultaneously in coordinated fashion to:
- Follow precise geometric path (lines, arcs, surfaces)
- Maintain programmed feedrate along path
- Arrive at target position simultaneously
- Respect individual axis constraints

**Example Problem**: Move from (0,0) to (10,5) in straight line
- If X and Y move independently at max speed:
  - X reaches 10 at t₁
  - Y reaches 5 at t₂ (where t₂ ≠ t₁)
  - Actual path is NOT straight line!

**Solution**: **Coordinate** X and Y motion so they reach target simultaneously while maintaining geometric path.

## Synchronized Motion Basics

### Time Synchronization

**Principle**: All axes complete move in same total time.

**Algorithm**:
1. Calculate path length: $L = \sqrt{\Delta X^2 + \Delta Y^2 + \Delta Z^2}$
2. Determine move time: $T = L / F$ (where F = programmed feedrate)
3. Calculate individual axis velocities:
   - $v_X = \Delta X / T$
   - $v_Y = \Delta Y / T$
   - $v_Z = \Delta Z / T$
4. Generate synchronized motion profiles

**Example**:
- Start: (0, 0, 0)
- End: (10, 5, 2)
- Feedrate: F = 120 IPM = 2 in/s
- Path length: $L = \sqrt{10^2 + 5^2 + 2^2} = \sqrt{129} = 11.36$ inches
- Move time: $T = 11.36 / 2 = 5.68$ seconds
- Axis velocities:
  - $v_X = 10 / 5.68 = 1.76$ in/s
  - $v_Y = 5 / 5.68 = 0.88$ in/s
  - $v_Z = 2 / 5.68 = 0.35$ in/s

**Verification**: $\sqrt{v_X^2 + v_Y^2 + v_Z^2} = \sqrt{1.76^2 + 0.88^2 + 0.35^2} = 2.0$ in/s ✓

### Velocity Vector Coordination

**Tool Center Point (TCP) Velocity**: Velocity along programmed path.

$$\vec{v}_{TCP} = \frac{d\vec{r}}{dt}$$

where $\vec{r}(t) = [X(t), Y(t), Z(t)]$ = position vector

**Components**:
$$\vec{v}_{TCP} = [v_X, v_Y, v_Z]$$

**Magnitude** (feedrate):
$$|\vec{v}_{TCP}| = \sqrt{v_X^2 + v_Y^2 + v_Z^2} = F$$

**Controller Responsibility**: Continuously adjust individual axis velocities to maintain:
1. $|\vec{v}_{TCP}| = F$ (constant feedrate along path)
2. Direction along programmed path

## Linear Interpolation (Multi-Axis)

### Three-Axis Linear Move

**G-Code**:
```gcode
G1 X10 Y5 Z-2 F150
```

**Trajectory Generation** (each servo cycle):

**Step 1**: Calculate unit direction vector
$$\hat{u} = \frac{[\Delta X, \Delta Y, \Delta Z]}{L} = \frac{[10, 5, -2]}{11.36} = [0.880, 0.440, -0.176]$$

**Step 2**: Calculate distance traveled (from velocity profile)
- At time $t$, total distance along path: $s(t)$ (from motion profile)

**Step 3**: Calculate individual axis positions
$$X(t) = X_0 + \hat{u}_X \cdot s(t)$$
$$Y(t) = Y_0 + \hat{u}_Y \cdot s(t)$$
$$Z(t) = Z_0 + \hat{u}_Z \cdot s(t)$$

**Example** (at t = 2 seconds, s(t) = 4.0 inches):
- $X(2) = 0 + 0.880 \times 4.0 = 3.52$ inches
- $Y(2) = 0 + 0.440 \times 4.0 = 1.76$ inches
- $Z(2) = 0 + (-0.176) \times 4.0 = -0.70$ inches

**Position commands sent to each axis PID loop every servo cycle** (e.g., 1 ms).

### Feedrate Along Path

**Programmed Feedrate**: F = 150 IPM (in this example)

**Actual TCP Velocity** (instantaneous):
$$v_{TCP}(t) = \frac{ds(t)}{dt}$$

**During Acceleration**:
- $v_{TCP}$ increases from 0 to F (ramping up)
- Individual axis velocities increase proportionally

**During Cruise**:
- $v_{TCP} = F$ (constant)
- Individual axis velocities constant

**During Deceleration**:
- $v_{TCP}$ decreases from F to 0
- Individual axis velocities decrease proportionally

**Key Point**: Ratio of axis velocities remains constant (maintains straight line path).

## Circular Interpolation (Multi-Axis)

### Two-Axis Circular Motion (XY Plane)

**G-Code**:
```gcode
G2 X10 Y10 I5 J0 F100
```

**Parameters**:
- Current position: (X₀, Y₀)
- Target: (X₁, Y₁) = (10, 10)
- Center offset: (I, J) = (5, 0)
- Arc center: $(X_c, Y_c) = (X_0 + I, Y_0 + J)$

**Trajectory Generation**:

**Step 1**: Calculate arc parameters
- Radius: $R = \sqrt{I^2 + J^2}$
- Start angle: $\theta_0 = \text{atan2}(Y_0 - Y_c, X_0 - X_c)$
- End angle: $\theta_1 = \text{atan2}(Y_1 - Y_c, X_1 - X_c)$
- Arc length: $L = R |\theta_1 - \theta_0|$

**Step 2**: Calculate instantaneous angle
$$\theta(t) = \theta_0 + \frac{s(t)}{R}$$

where $s(t)$ = arc distance traveled

**Step 3**: Calculate X, Y positions
$$X(t) = X_c + R \cos(\theta(t))$$
$$Y(t) = Y_c + R \sin(\theta(t))$$

**Step 4**: Calculate velocities (derivatives)
$$v_X(t) = -R \sin(\theta(t)) \cdot \frac{d\theta}{dt}$$
$$v_Y(t) = R \cos(\theta(t)) \cdot \frac{d\theta}{dt}$$

where $\frac{d\theta}{dt} = \frac{v_{TCP}(t)}{R}$ (angular velocity)

### Centripetal Acceleration Constraint

**Problem**: Circular motion creates centripetal acceleration.

$$a_c = \frac{v^2}{R}$$

**Example**:
- Radius: R = 2 inches
- Feedrate: F = 200 IPM = 3.33 in/s
- Centripetal acceleration: $a_c = 3.33^2 / 2 = 5.55$ in/s²

**If $a_c > a_{max}$**: Controller must reduce feedrate.

**Maximum Allowable Feedrate**:
$$v_{max} = \sqrt{a_{max} \cdot R}$$

**Example** (small radius):
- Radius: R = 0.1 inches
- Max acceleration: $a_{max} = 200$ in/s²
- $v_{max} = \sqrt{200 \times 0.1} = 4.47$ in/s = 268 IPM

If programmed F = 400 IPM, controller automatically reduces to 268 IPM for this arc.

**Feedrate Override for Arcs**: Modern controllers automatically compute this; programmer doesn't need to manually adjust F for every arc radius.

### Helical Interpolation (3-Axis Circular)

**G-Code**:
```gcode
G2 X10 Y10 Z-5 I5 J0 F100
```

**Motion**:
- XY plane: Circular arc
- Z axis: Simultaneous linear motion

**Trajectory**:
$$X(t) = X_c + R \cos(\theta(t))$$
$$Y(t) = Y_c + R \sin(\theta(t))$$
$$Z(t) = Z_0 + \frac{\Delta Z}{L_{arc}} \cdot s(t)$$

where:
- $L_{arc}$ = arc length in XY plane
- $s(t)$ = distance traveled along arc

**Feedrate**: Along 3D helical path (not just XY arc)

$$L_{total} = \sqrt{L_{arc}^2 + \Delta Z^2}$$

**Application**: Thread milling, helical entry into holes.

## Tool Center Point (TCP) Control

### TCP Definition

**Tool Center Point**: The effective point of the tool (e.g., tip of end mill, center of ball on CMM probe).

**CNC Context**: Control TCP position, not machine coordinate position.

**Why TCP Control Matters**:
- Tool length varies (different tools, tool wear)
- Work offset (part location on table)
- Rotary axes (A, B, C) change TCP location relative to machine coordinates

### Tool Length Compensation (TLC)

**Problem**: Different tools have different lengths.

**Solution**: Define tool length offset; controller adjusts Z position.

**G-Code**:
```gcode
G43 H1 Z0.5   ; Activate tool length comp, use offset H1
```

**Controller Calculation**:
$$Z_{machine} = Z_{programmed} + \text{ToolOffset}[H1]$$

**Example**:
- Programmed Z = 0.5" (above part surface)
- Tool offset H1 = -3.5" (tool length)
- Machine Z = 0.5 + (-3.5) = -3.0" (absolute machine position)

**TCP Position**: 0.5" above part surface (regardless of tool length)

### Multi-Axis TCP (5-Axis Machining)

**5-Axis Configuration**: X, Y, Z (linear) + A, B (rotary)

**Challenge**: Rotary axis motion changes TCP position.

**Example**: Tilt B-axis by 10°
- Tool tip position changes in X and Z
- Must coordinate X, Z motion to keep TCP stationary during B rotation

**Forward Kinematics**: Calculate TCP position from joint (axis) positions
$$\vec{r}_{TCP} = f(X, Y, Z, A, B)$$

**Inverse Kinematics**: Calculate required joint positions for desired TCP position
$$[X, Y, Z, A, B] = f^{-1}(\vec{r}_{TCP}, \text{orientation})$$

**Controller Responsibility**: Solve inverse kinematics in real-time; coordinate all 5 axes.

**Complexity**: Non-trivial mathematics; requires 5-axis controller (not all CNC controllers support).

## Coordinated Motion Constraints

### Individual Axis Limits

**Each Axis Has Limits**:
- Maximum velocity: $v_{max,i}$
- Maximum acceleration: $a_{max,i}$
- Maximum jerk: $j_{max,i}$

**Coordinated Motion**: Must respect ALL axis limits simultaneously.

### Velocity Constraint Checking

**Given**: Desired feedrate F along path

**Required Axis Velocities**:
$$v_i = F \cdot \frac{\Delta r_i}{L}$$

where:
- $\Delta r_i$ = motion distance for axis $i$
- $L$ = path length

**Constraint Check**:
$$|v_i| \leq v_{max,i} \text{ for all } i$$

**If Violated**: Reduce F to maximum allowable value.

**Maximum Allowable F**:
$$F_{max} = \min_i \left( v_{max,i} \cdot \frac{L}{|\Delta r_i|} \right)$$

**Example**:
- Move: ΔX = 10", ΔY = 10", ΔZ = 5"
- Path length: $L = \sqrt{10^2 + 10^2 + 5^2} = 15$ inches
- Programmed F = 600 IPM = 10 in/s
- Axis limits:
  - $v_{max,X}$ = 600 IPM = 10 in/s
  - $v_{max,Y}$ = 500 IPM = 8.33 in/s
  - $v_{max,Z}$ = 300 IPM = 5 in/s

**Required Velocities**:
- $v_X = 10 \times (10/15) = 6.67$ in/s (OK, < 10)
- $v_Y = 10 \times (10/15) = 6.67$ in/s (OK, < 8.33)
- $v_Z = 10 \times (5/15) = 3.33$ in/s (OK, < 5)

**All constraints satisfied**: F = 600 IPM achievable.

**Example 2** (constraint violated):
- Move: ΔX = 10", ΔY = 10", ΔZ = 10"
- Path length: $L = 17.32$ inches
- Programmed F = 800 IPM = 13.33 in/s
- Required $v_Z = 13.33 \times (10/17.32) = 7.70$ in/s **(exceeds 5 in/s limit!)**

**Maximum Allowable F**:
$$F_{max} = 5.0 \times \frac{17.32}{10} = 8.66 \text{ in/s} = 520 \text{ IPM}$$

Controller automatically reduces F to 520 IPM.

### Acceleration Constraint Checking

**Similar Process**: Check that required axis accelerations don't exceed limits.

**During Velocity Change**: Each axis accelerates proportionally.

$$a_i = \frac{a_{TCP} \cdot \Delta r_i}{L}$$

where $a_{TCP}$ = acceleration along path

**Constraint**:
$$|a_i| \leq a_{max,i} \text{ for all } i$$

**If Violated**: Reduce $a_{TCP}$ (slower ramp-up/down).

## Contouring Accuracy

### Path Following Error

**Ideal**: Tool follows programmed path exactly

**Reality**: Following errors cause deviation from path

**Contouring Error**: Perpendicular distance from actual TCP to ideal path

### Sources of Contouring Error

1. **Individual Axis Following Errors**:
   - Each axis lags command by small amount
   - Combined effect: TCP deviates from path

2. **Servo Tuning Mismatch**:
   - X-axis responds faster than Y-axis
   - Path distortion (even if following errors small)

3. **Acceleration/Deceleration**:
   - Transient errors during speed changes
   - Worse at corners (large acceleration)

4. **Mechanical Compliance**:
   - Cutting forces deflect tool
   - Direction-dependent (different X vs. Y stiffness)

### Reducing Contouring Error

**Method 1: Better Servo Tuning**
- Minimize individual following errors (PID + feedforward)
- Match response of all axes (similar bandwidth)

**Method 2: Cross-Coupling Control**
- Measure contouring error directly
- Apply correction to maintain path accuracy
- More complex, not common in standard CNC controllers

**Method 3: Slower Feedrates**
- Reduces dynamic errors (acceleration-dependent)
- Trade-off: Longer cycle time

**Method 4: Mechanical Improvements**
- Stiffer frame (reduce compliance)
- Better bearings (reduce friction variation)
- Balanced axes (similar inertia, friction)

### Circular Test (Contouring Accuracy Check)

**Procedure**:
1. Mount dial indicator or probe
2. Program circular interpolation (e.g., 4" diameter circle)
3. Measure actual radius at multiple points
4. Deviation from nominal = contouring error

**Example Results**:
- Nominal radius: 2.000"
- Measured: 1.998" to 2.003" (variation = 0.005")
- **Contouring error: ±0.0025" (radial)**

**Typical Specifications**:
- Hobby CNC: ±0.005-0.010"
- Industrial CNC: ±0.001-0.002"
- Precision CNC: ±0.0001-0.0005"

## Gantry Synchronization (Dual-Motor Axis)

### The Gantry Problem

**Dual-Motor Gantry** (common on plasma tables, large routers):
- Two motors drive same axis (e.g., left and right side of Y-axis gantry)
- Motors must stay perfectly synchronized
- Mismatch causes gantry to rack (skew)

**Consequences of Racking**:
- Binding (mechanical stress)
- Loss of accuracy
- Premature wear
- Possible motor stall

### Independent Motor Control

**Approach 1**: Treat as separate axes (e.g., Y1 and Y2)

**G-Code Coordination**:
```gcode
G1 Y10 ; Both Y1 and Y2 commanded to move 10"
```

**Problem**: If one motor lags (even slightly), gantry racks.

**Example**:
- Y1 position: 10.002"
- Y2 position: 9.998"
- **Racking error: 0.004"** (across gantry width)

### Slaving (Simple Synchronization)

**Approach 2**: One motor is "master", other is "slave"

**Configuration**:
- Y1 = master (receives position commands from controller)
- Y2 = slave (copies Y1 commands)

**Problem**: Still no correction if slave lags (open-loop slaving)

### Cross-Coupling Control (Active Synchronization)

**Approach 3**: Feedback from both motors, cross-coupling controller

**Algorithm**:
1. Measure positions: $y_1$, $y_2$
2. Calculate average: $y_{avg} = (y_1 + y_2) / 2$
3. Calculate sync error: $e_{sync} = y_1 - y_2$
4. Commands:
   - $u_1 = \text{PID}(r - y_1) - K_{sync} \cdot e_{sync}$
   - $u_2 = \text{PID}(r - y_2) + K_{sync} \cdot e_{sync}$

**Effect**:
- If Motor 1 leads: Reduce $u_1$, increase $u_2$ → synchronize
- If Motor 2 leads: Increase $u_1$, reduce $u_2$ → synchronize

**Tuning $K_{sync}$**:
- Start: $K_{sync} = 0.1 \times K_P$
- Increase until $|e_{sync}| < 0.001$"
- Too high: Instability (motors fight each other)

**LinuxCNC**: `gantrykins` kinematics module handles this automatically.

## Summary

Multi-axis coordination ensures all axes work together to follow programmed path:

**Key Concepts**:
1. **Time Synchronization**: All axes complete move simultaneously
2. **Velocity Coordination**: Individual axis velocities maintain path direction
3. **Constraint Checking**: Respect individual axis limits (velocity, acceleration)
4. **Contouring Accuracy**: Minimize perpendicular deviation from path

**Interpolation Types**:
- **Linear**: Straight lines (3+ axes coordinated)
- **Circular**: Arcs (2-3 axes, centripetal acceleration constrained)
- **Helical**: 3D spiral (circular + linear combined)

**Advanced Topics**:
- **TCP Control**: Account for tool length, rotary axes
- **Gantry Sync**: Dual-motor coordination (cross-coupling)

**Next Steps**:
- Look-ahead and path blending (Section 19.9)
- Implementation in LinuxCNC (Section 19.10)
- Implementation in Mach4 (Section 19.11)

---

**Next**: [19.9 Look-Ahead and Path Blending](section-19.9-look-ahead-blending.md)
