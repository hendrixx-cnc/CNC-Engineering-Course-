# 19.6 Trajectory Planning Fundamentals

## What is Trajectory Planning?

**Trajectory Planning**: The process of generating time-based position, velocity, and acceleration commands that move a machine from one location to another while respecting kinematic and dynamic constraints.

**Distinction**:
- **Path**: Geometric route through space (e.g., line from A to B, arc, spline)
- **Trajectory**: Path + timing (position as function of time: $x(t)$, $y(t)$, $z(t)$)

**Example**:
- **Path**: "Move in straight line from (0,0) to (10,10)"
- **Trajectory**: "At t=0s, position=(0,0); at t=0.5s, position=(5,5); at t=1.0s, position=(10,10)"

**Why Trajectory Planning Matters**:
- Respects machine limits (max velocity, acceleration, jerk)
- Minimizes cycle time (fastest possible while staying within limits)
- Ensures smooth motion (avoids jerks that excite vibration)
- Coordinates multiple axes (maintain tool path accuracy)

## Point-to-Point vs. Continuous Path Motion

### Point-to-Point (PTP) Motion

**Characteristics**:
- Move from start point to end point
- Path between points doesn't matter
- Each axis can move independently at maximum rate
- Used for positioning, tool changes, rapids

**Example**: G0 rapid move
```gcode
G0 X10 Y5 Z2
```

**Behavior**:
- X, Y, Z axes accelerate independently
- Fastest axis arrives first, waits for others
- Actual path is NOT a straight line (unless carefully coordinated)

**Typical Applications**:
- Rapid positioning between cuts
- Tool changes (moving to/from tool changer)
- Probing moves (to/from probe point)

**Advantage**: Fastest possible move (each axis at max speed)

**Disadvantage**: Cannot control actual path taken

### Continuous Path (CP) Motion

**Characteristics**:
- Path is precisely defined (line, arc, spline)
- All axes coordinated to follow path exactly
- Velocity along path may vary
- Used for cutting, contouring

**Example**: G1 linear interpolation
```gcode
G1 X10 Y5 F100
```

**Behavior**:
- Controller calculates X and Y motion to produce straight line
- Velocity along path = 100 IPM (feedrate)
- X and Y velocities continuously adjusted to maintain path

**Typical Applications**:
- Linear cuts (milling, turning)
- Circular interpolation (arcs, holes)
- Complex contours (splines, NURBS)

**Advantage**: Precise path control (geometric accuracy)

**Disadvantage**: Slower than PTP (axes must coordinate)

## Kinematic Constraints

### Velocity Limits

**Maximum Velocity**: Highest speed each axis can sustain.

**Limits Set By**:
1. **Motor speed**: Maximum RPM
2. **Mechanical**: Screw pitch, belt ratio
3. **Control**: Encoder resolution, update rate
4. **Thermal**: Continuous motor current limit

**Example**:
- Motor max speed: 3000 RPM
- Ballscrew pitch: 5 mm/rev (0.2 in/rev)
- Max linear velocity: 3000 × 0.2 = 600 in/min

**Per-Axis Limits**: Each axis may have different max velocity.
- X-axis: 600 IPM
- Y-axis: 500 IPM (longer, heavier)
- Z-axis: 300 IPM (vertical, gravity load)

**Coordinated Motion**: Must slow down to respect all axes.

**Example**: Diagonal move from (0,0) to (10,10) at F600
- Equal X and Y motion
- If X max = 600 IPM, Y max = 500 IPM:
  - Cannot achieve F600 (would require Y = 424 IPM, OK)
  - **Achievable feedrate = 600 IPM** (within limits)

**Example 2**: Diagonal (0,0) to (10,5)
- X motion = 10", Y motion = 5"
- Path length = √(10² + 5²) = 11.18"
- Desired F = 600 IPM
- Required X velocity: (10/11.18) × 600 = 537 IPM (OK)
- Required Y velocity: (5/11.18) × 600 = 268 IPM (OK)
- **Achievable feedrate = 600 IPM**

**Example 3**: Diagonal (0,0) to (10,10) at F800
- Path length = √(10² + 10²) = 14.14"
- Required X velocity: (10/14.14) × 800 = 566 IPM (OK, < 600)
- Required Y velocity: (10/14.14) × 800 = 566 IPM (exceeds 500 max!)
- **Must reduce feedrate**: F = 500 × 14.14/10 = 707 IPM
- Recalculate: X = Y = 500 IPM (at limit)

### Acceleration Limits

**Maximum Acceleration**: Rate of velocity change each axis can achieve.

**Limits Set By**:
1. **Motor torque**: Peak and continuous ratings
2. **Inertia**: Moving mass + load
3. **Mechanical**: Frame rigidity, bearing friction
4. **Control**: Following error limits

**Example**:
- Motor peak torque: 3.0 N·m
- Moving inertia: 0.01 kg·m²
- Max angular acceleration: 3.0 / 0.01 = 300 rad/s²
- Ballscrew pitch: 5 mm/rev = 0.0318 m/rad
- Max linear acceleration: 300 × 0.0318 = 9.54 m/s² ≈ 22,500 in/min² ≈ 375 in/s²

**Typical CNC Accelerations**:
- Hobby/DIY: 50-100 in/s²
- Industrial mill: 150-300 in/s²
- High-speed router: 300-500 in/s²
- Pick-and-place: 1000-3000 in/s²

**Coordinated Acceleration**: Must respect all axes during multi-axis moves.

**Acceleration Distance** (from rest to max velocity):
$$d = \frac{v_{max}^2}{2a_{max}}$$

**Example**:
- Max velocity: 600 IPM = 10 in/s
- Max acceleration: 200 in/s²
- Acceleration distance: 10² / (2 × 200) = 0.25 inches

**Implication**: For moves < 0.5", never reaches max velocity (entirely accel + decel).

### Jerk Limits

**Jerk**: Rate of change of acceleration.

$$j = \frac{da}{dt}$$

**Why Limit Jerk**:
1. **Smooth motion**: Sudden acceleration changes excite vibration
2. **Mechanical stress**: Reduces shock loads on bearings, frame
3. **Following error**: Gradual acceleration changes easier for servo to track
4. **Surface finish**: Smooth motion → better finish

**Unlimited Jerk**: Trapezoidal velocity profile (instant acceleration change)
- Fast cycle time
- Harsh motion (vibration, ringing)

**Limited Jerk**: S-curve velocity profile (smooth acceleration change)
- Slightly slower cycle time
- Smooth motion (better surface finish)

**Typical Jerk Limits**:
- Trapezoidal (no jerk limit): ∞
- Moderate jerk limit: 5,000-10,000 in/s³
- Aggressive jerk limit: 20,000-50,000 in/s³
- High-speed machining: 100,000+ in/s³ (but still limited)

**Trade-off**: Lower jerk limit = smoother motion but longer cycle time.

## Real-Time vs. Pre-Computed Trajectories

### Real-Time Trajectory Generation

**Method**: Controller generates trajectory on-the-fly, synchronized with motion execution.

**Characteristics**:
- Trajectory computed in real-time (every servo cycle, e.g., 1 kHz)
- Can respond to external events (feedhold, feed override)
- Requires fast processor, real-time OS

**Example**: LinuxCNC
- Real-time trajectory planner
- Updates trajectory every 1 ms (1 kHz servo thread)
- Computes position, velocity, acceleration for each axis
- Sends commands to PID loops

**Advantages**:
- Dynamic response (feedhold stops immediately)
- Feed rate override (real-time adjustment)
- Adaptive feed (slow down for heavy cuts)

**Disadvantages**:
- Requires real-time computing (not all systems support)
- Limited look-ahead (computational constraints)

### Pre-Computed Trajectories

**Method**: Entire toolpath trajectory computed before motion begins.

**Characteristics**:
- Trajectory stored in memory (position vs. time table)
- Playback during execution (no real-time computation)
- Can optimize globally (entire path visible)

**Example**: CAM post-processor
- Generates optimized trajectory (considers entire part)
- Outputs G-code + velocity profile
- Controller plays back pre-computed trajectory

**Advantages**:
- Optimal trajectory (global optimization possible)
- Simpler controller (playback only)
- Deterministic (repeatable timing)

**Disadvantages**:
- Cannot respond dynamically (feedhold = stop playback, then resume)
- Large memory for complex parts
- Less flexible

### Hybrid Approach (Common in Modern CNC)

**Method**: Pre-compute short segments, update in real-time.

**Example**:
- Read-ahead buffer: 50-200 G-code blocks
- Compute optimal trajectory for buffered blocks
- Update trajectory as new blocks arrive
- Retain real-time adjustability (feedhold, override)

**Best of Both**: Optimization + dynamic response.

## Interpolation

### Linear Interpolation

**G1 Command**: Move in straight line at specified feedrate.

```gcode
G1 X10 Y5 Z2 F120
```

**Trajectory Generation**:
1. Calculate path length: $L = \sqrt{(X_1-X_0)^2 + (Y_1-Y_0)^2 + (Z_1-Z_0)^2}$
2. Calculate unit direction vector: $\hat{u} = [(X_1-X_0)/L, (Y_1-Y_0)/L, (Z_1-Z_0)/L]$
3. Calculate time duration: $T = L / F$ (feedrate)
4. Generate trajectory: $\vec{r}(t) = \vec{r}_0 + \hat{u} \cdot v(t) \cdot t$

where $v(t)$ = velocity profile (constant or ramped with accel/decel)

**Example**:
- Start: (0, 0, 0)
- End: (10, 5, 0)
- Feedrate: 120 IPM = 2 in/s
- Path length: √(100+25) = 11.18 inches
- Duration: 11.18 / 2 = 5.59 seconds
- X velocity: (10/11.18) × 2 = 1.789 in/s
- Y velocity: (5/11.18) × 2 = 0.894 in/s

**At each servo update** (e.g., 1 ms):
- $t = 0.000$ s: Position = (0.000, 0.000, 0.000)
- $t = 0.001$ s: Position = (0.00179, 0.00089, 0.000)
- $t = 0.002$ s: Position = (0.00358, 0.00179, 0.000)
- ...
- $t = 5.590$ s: Position = (10.000, 5.000, 0.000)

### Circular Interpolation

**G2/G3 Commands**: Move in circular arc.

```gcode
G2 X10 Y10 I5 J0 F100
```

**Parameters**:
- (X, Y): Arc endpoint
- (I, J): Center offset from start point
- F: Feedrate

**Trajectory Generation**:
1. Calculate center: $(X_c, Y_c) = (X_0 + I, Y_0 + J)$
2. Calculate radius: $R = \sqrt{I^2 + J^2}$
3. Calculate start angle: $\theta_0 = \text{atan2}(Y_0 - Y_c, X_0 - X_c)$
4. Calculate end angle: $\theta_1 = \text{atan2}(Y_1 - Y_c, X_1 - X_c)$
5. Calculate arc length: $L = R \cdot |\theta_1 - \theta_0|$
6. Generate trajectory:
   - $\theta(t) = \theta_0 + (\theta_1 - \theta_0) \cdot (s(t) / L)$
   - $X(t) = X_c + R \cos(\theta(t))$
   - $Y(t) = Y_c + R \sin(\theta(t))$

where $s(t)$ = arc distance traveled (from velocity profile)

**Challenge**: Velocity along arc creates centripetal acceleration.

**Centripetal Acceleration**:
$$a_c = \frac{v^2}{R}$$

**Example**:
- Radius: 2 inches
- Feedrate: 200 IPM = 3.33 in/s
- Centripetal acceleration: 3.33² / 2 = 5.56 in/s²

If max acceleration = 200 in/s², this is well within limits.

**Small Radius, High Speed**:
- Radius: 0.1 inches
- Feedrate: 200 IPM = 3.33 in/s
- Centripetal acceleration: 3.33² / 0.1 = 111 in/s² (still OK)

**Very Small Radius**:
- Radius: 0.02 inches
- Feedrate: 200 IPM = 3.33 in/s
- Centripetal acceleration: 3.33² / 0.02 = 556 in/s² (exceeds 200 limit!)

**Controller must reduce feedrate** to respect acceleration limits.

**Allowable velocity** (for given radius and max acceleration):
$$v_{max} = \sqrt{a_{max} \cdot R}$$

Example: $v_{max} = \sqrt{200 \times 0.02} = 2.0$ in/s = 120 IPM

**Automatic Feedrate Reduction**: Modern controllers slow down automatically for tight arcs.

### Helical Interpolation

**Helical Move**: Circular arc in XY plane + linear Z motion.

```gcode
G2 X10 Y10 Z-1 I5 J0 F80
```

**Trajectory**:
- XY: Circular arc (as above)
- Z: Linear interpolation (simultaneous)
- Feedrate: Along 3D helical path

**Application**:
- Thread milling
- Helical hole entry (ramping into hole)
- Spring-like toolpaths

### Spline Interpolation

**Spline**: Smooth curve through multiple points.

**Types**:
- **Cubic spline**: Piecewise cubic polynomials (continuous to 2nd derivative)
- **B-spline**: Basis spline (localized control points)
- **NURBS**: Non-Uniform Rational B-Splines (industry standard in CAD/CAM)

**G-Code Support**:
- **G5**: Cubic spline (limited support)
- **G5.1**: Quadratic B-spline (LinuxCNC)
- **G5.2/G5.3**: NURBS (limited controllers)

**Example** (LinuxCNC G5.1):
```gcode
G5.1 X5 Y2
G5.1 X8 Y6
G5.1 X10 Y4
```

**Advantage**: Smooth curves (no sharp corners), better surface finish.

**Challenge**: More complex interpolation, requires look-ahead for feedrate planning.

## Path Tolerance and Contouring Accuracy

### Path Tolerance

**Definition**: Maximum allowed deviation from programmed path.

**Example**: G1 move from (0,0) to (10,10)
- Ideal: Straight line
- Actual: Servo following errors cause deviation
- Path tolerance: Maximum allowed deviation (e.g., 0.001")

**Factors Affecting Path Accuracy**:
1. **Following error**: Position lag during motion
2. **Corner blending**: Rounding of sharp corners (Section 19.9)
3. **Interpolation resolution**: Time step size
4. **Mechanical compliance**: Frame/screw deflection under load

### Contouring Error

**Definition**: Perpendicular distance from actual position to desired path.

**Example**: Circular arc
- Programmed: Perfect circle, radius = 5.000"
- Actual: Slightly oval due to following errors
- Contouring error: Radial deviation from circle

**Measurement**:
- Circular interpolation test (G2/G3 around circle)
- Measure radius at multiple points
- Maximum deviation = contouring error

**Typical Specifications**:
- Hobby CNC: 0.005-0.010" contouring error
- Industrial CNC: 0.001-0.002" contouring error
- Precision CNC: 0.0001-0.0005" contouring error

**Improvement Methods**:
1. Better servo tuning (reduce following error)
2. Feedforward control (FF1, FF2)
3. Slower feedrates (less dynamic error)
4. Stiffer mechanical construction

## Blending vs. Exact Stop Mode

### Exact Stop Mode

**Behavior**: Axis decelerates to complete stop at each programmed point.

**G-Code**: G61 (Exact Stop Mode)

```gcode
G61
G1 X10 Y0 F100
G1 X10 Y10
G1 X0 Y10
```

**Motion**:
1. Move to (10, 0), **stop completely**
2. Move to (10, 10), **stop completely**
3. Move to (0, 10), **stop completely**

**Advantages**:
- Guaranteed position accuracy at each point
- Predictable (no corner rounding)

**Disadvantages**:
- Slow (stop/start at every point)
- Harsh (acceleration spikes at corners)
- Poor surface finish (start/stop marks)

**When to Use**:
- Probing operations
- Precision positioning
- Tool changes
- When exact final position critical

### Blending Mode (Constant Velocity)

**Behavior**: Axis maintains velocity through programmed points (rounds corners).

**G-Code**: G64 (Blending Mode)

```gcode
G64
G1 X10 Y0 F100
G1 X10 Y10
G1 X0 Y10
```

**Motion**:
1. Move toward (10, 0)
2. **Before reaching (10,0)**, begin transitioning to next move
3. Round corner at (10, 0), never stop
4. Continue through (10, 10) with rounded corner
5. Slow down only at final point (0, 10)

**Advantages**:
- Fast (no stops)
- Smooth motion (no acceleration spikes)
- Better surface finish (continuous motion)

**Disadvantages**:
- Position error at corners (path deviation)
- Requires look-ahead (know next move in advance)

**When to Use**:
- Cutting operations (milling, routing)
- 3D contouring
- Any continuous path where exact corner position not critical

### Blending with Tolerance (G64 P)

**G-Code**: G64 P[tolerance]

```gcode
G64 P0.005
G1 X10 Y0 F100
G1 X10 Y10
```

**Behavior**: Blend corners, but limit path deviation to specified tolerance.

**Example**:
- P0.005: Maximum 0.005" deviation from programmed corner
- Tighter corners: Slow down to stay within tolerance
- Gradual corners: Maintain high speed

**Best of Both**: Speed of blending + controlled accuracy.

**Typical Values**:
- Roughing: P0.010-0.020 (fast, low accuracy needed)
- Finishing: P0.001-0.005 (balance speed and finish)
- Precision: P0.0001-0.001 (slow, high accuracy)

## Summary

Trajectory planning bridges the gap between G-code commands and real-time motion:

**Key Concepts**:
1. **Path vs. Trajectory**: Geometry vs. time-based motion
2. **Kinematic Constraints**: Velocity, acceleration, jerk limits
3. **Interpolation**: Linear, circular, spline motion generation
4. **Blending**: Trade-off between speed and accuracy

**Controller Responsibilities**:
- Generate smooth trajectories respecting all constraints
- Coordinate multiple axes for accurate path following
- Optimize feedrate for minimum cycle time
- Provide real-time adjustability (feed override, feedhold)

**Next Steps**:
- Learn motion profile design (Section 19.7)
- Understand multi-axis coordination (Section 19.8)
- Implement look-ahead and path blending (Section 19.9)

---

**Next**: [19.7 Motion Profiles](section-19.7-motion-profiles.md)
