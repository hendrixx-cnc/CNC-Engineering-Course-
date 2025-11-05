# 19.9 Look-Ahead and Path Blending

## The Look-Ahead Problem

**Sequential G-Code Processing** (naive approach):
1. Execute Line 1 completely
2. Stop at end of Line 1
3. Read Line 2
4. Execute Line 2
5. Repeat...

**Problem**: Stop-and-go motion
- Slow (acceleration/deceleration at every line)
- Harsh (jerky motion)
- Poor surface finish (start/stop marks)

**Solution**: **Look-Ahead** - read multiple lines ahead, plan smooth continuous motion.

### Why Look-Ahead is Necessary

**Example G-Code** (square profile):
```gcode
N10 G1 X10 Y0 F100
N20 G1 X10 Y10
N30 G1 X0 Y10
N40 G1 X0 Y0
```

**Without Look-Ahead**:
- Accelerate to F100, move to (10,0), **decelerate to stop**
- **Stop completely** at corner
- Accelerate to F100, move to (10,10), **decelerate to stop**
- Repeat for each corner
- **Total time**: ~4× longer due to stops

**With Look-Ahead**:
- Read all 4 lines before starting
- Plan continuous motion through corners
- Never stop (except at final point)
- **Total time**: Much faster, smooth motion

## Look-Ahead Buffer

### Buffer Structure

**Read-Ahead Buffer**: Queue of upcoming G-code blocks.

**Typical Size**: 50-200 blocks (depends on controller memory and computational power)

**Example**:
- Controller at Line N50
- Buffer contains: N51, N52, ..., N150
- As N50 completes, N51 moves to execution, N151 added to buffer

### Buffer Benefits

**1. Corner Planning**:
- Know next move direction before reaching corner
- Calculate optimal corner velocity (blend vs. stop)

**2. Velocity Optimization**:
- Look ahead for tight corners, slow arcs
- Preemptively reduce velocity
- Avoid sudden decelerations

**3. Smooth Acceleration Profiles**:
- Plan acceleration/deceleration across multiple moves
- Smoother than per-move planning

**4. Constraint Checking**:
- Check upcoming moves for axis limits
- Adjust velocity proactively

### Computational Challenge

**Real-Time Constraint**: Must plan trajectory faster than execution.

**Example**:
- Feedrate: 100 IPM = 1.67 in/s
- Line length: 0.1 inches
- Execution time: 0.1 / 1.67 = 0.06 seconds
- **Planner must process line in <0.06 seconds**

**Short Lines** (common in CAM output):
- 1000+ lines per second typical
- Requires efficient algorithms (linear time, not exponential)

**Modern Controllers**: Dedicated trajectory planning processor/thread.

## Corner Blending Strategies

### Exact Stop (No Blending)

**G61 Mode**: Decelerate to complete stop at each programmed point.

**Motion**:
```
Velocity
   |  /\    /\    /\
   | /  \  /  \  /  \
   |/    \/    \/    \
   |__________________ Time
     P1    P2    P3
```

**Advantages**:
- Exact position at every point
- Predictable
- Simple

**Disadvantages**:
- Slow (stops at every point)
- Jerky motion
- Poor surface finish (start/stop marks)

### Continuous Blending (G64)

**G64 Mode**: Maintain velocity through corners by rounding.

**Motion**:
```
Velocity
   |    _______________
   |   /               \
   |  /                 \
   | /                   \
   |/                     \
   |_______________________ Time
        (smooth curve)
```

**Path Deviation**: Actual path rounds corners (doesn't pass through exact programmed points).

**Advantage**: Fast, smooth motion.

**Disadvantage**: Position error at corners.

### Tolerance-Based Blending (G64 P)

**G64 P[tolerance]**: Blend corners with maximum allowed path deviation.

**Example**:
```gcode
G64 P0.005  ; Max 0.005" path deviation
G1 X10 Y0 F100
G1 X10 Y10
```

**Algorithm**:
1. Calculate corner angle
2. Determine blend radius for given tolerance
3. Slow down if necessary to stay within tolerance

**Balance**: Speed (large blend radius) vs. Accuracy (small blend radius).

## Corner Velocity Calculation

### Geometric Analysis

**Two-Line Corner**:
- Line 1: Direction $\vec{u}_1$
- Line 2: Direction $\vec{u}_2$
- Corner angle: $\theta = \cos^{-1}(\vec{u}_1 \cdot \vec{u}_2)$

**Corner Velocity** (for given blend tolerance):

**Sharp Corner** ($\theta$ near 90°):
- Requires low velocity (high direction change)
- Large centripetal acceleration

**Gradual Corner** ($\theta$ near 180°):
- Can maintain high velocity (slight direction change)
- Small centripetal acceleration

### Blend Radius and Tolerance

**Blend Arc**: Circular arc connecting two lines tangentially.

**Chord Tolerance** (path deviation):
$$P = r(1 - \cos(\theta/2))$$

where:
- $P$ = chord tolerance (max path deviation)
- $r$ = blend radius
- $\theta$ = corner angle

**Solve for Blend Radius**:
$$r = \frac{P}{1 - \cos(\theta/2)}$$

**Example**:
- Corner angle: $\theta = 90°$
- Tolerance: $P = 0.010$ inches
- Blend radius: $r = 0.010 / (1 - \cos(45°)) = 0.010 / 0.293 = 0.034$ inches

### Maximum Corner Velocity

**Centripetal Acceleration Constraint**:
$$a_c = \frac{v^2}{r} \leq a_{max}$$

**Maximum Velocity**:
$$v_{max} = \sqrt{a_{max} \cdot r}$$

**Example**:
- Blend radius: $r = 0.034$ inches
- Max acceleration: $a_{max} = 200$ in/s²
- $v_{max} = \sqrt{200 \times 0.034} = 2.61$ in/s = 156 IPM

**Controller Action**: If programmed F = 200 IPM, reduce to 156 IPM for this corner.

### Axis Acceleration Constraints

**Additional Check**: Individual axis accelerations during corner.

**Example** (90° XY corner):
- Approaching along +X
- Exiting along +Y
- At corner apex: $v_X$ decreasing, $v_Y$ increasing
- Peak acceleration: Both axes at $a_{max}$ simultaneously?

**Vector Sum**:
$$\vec{a}_{total} = [a_X, a_Y]$$
$$|\vec{a}_{total}| = \sqrt{a_X^2 + a_Y^2}$$

**For 90° corner**: $|\vec{a}_{total}| = \sqrt{2} \cdot a_{max}$ (if both axes at limit)

**Solution**: Reduce corner velocity to keep $|\vec{a}_{total}| \leq a_{max}$.

## Velocity Planning Along Path

### Look-Ahead Velocity Profiling

**Forward Pass** (look ahead from start):
1. Start at programmed feedrate F
2. For each upcoming corner:
   - Calculate max corner velocity $v_{corner}$
   - If $v_{corner} < v_{current}$: Begin decelerating
   - Calculate deceleration distance: $d = \frac{v_{current}^2 - v_{corner}^2}{2a_{max}}$
3. Propagate constraints forward

**Backward Pass** (look back from end):
1. Start from final point (v = 0 or final feedrate)
2. For each previous segment:
   - Calculate max velocity (considering next segment constraint)
   - Acceleration distance: $d = \frac{v_{next}^2}{2a_{max}}$
3. Propagate constraints backward

**Optimal Profile**: Minimum of forward and backward passes.

### Example Velocity Profile

**Scenario**: Three lines forming two 90° corners

```gcode
G64 P0.005
G1 X10 Y0 F200
G1 X10 Y10
G1 X0 Y10
```

**Calculate Corner Velocities**:
- Corner 1 (10,0): $v_{c1} = 150$ IPM (from blend radius calculation)
- Corner 2 (10,10): $v_{c2} = 150$ IPM

**Velocity Profile**:
```
Velocity (IPM)
200 |    ___________
    |   /           \
150 |__/             \___
    |                    \
  0 |____________________\__
    0   X10   X10Y10   X0Y10
```

**Motion**:
1. Accelerate to 200 IPM
2. Decelerate approaching Corner 1, reaching 150 IPM
3. Blend through Corner 1 at 150 IPM
4. Accelerate back to 200 IPM
5. Decelerate approaching Corner 2
6. Blend through Corner 2 at 150 IPM
7. Decelerate to stop at final point

**Smooth, continuous motion** with no complete stops.

## Path Tolerance and Accuracy

### Tolerance Specification

**Typical Values**:
- **Roughing**: P = 0.010-0.050" (fast, low accuracy)
- **Finishing**: P = 0.001-0.005" (balanced)
- **Precision**: P = 0.0001-0.001" (slow, high accuracy)

**Trade-Off**: Tighter tolerance = slower corners = longer cycle time.

**Example**:
- With P = 0.010": Corner velocity = 200 IPM
- With P = 0.001": Corner velocity = 80 IPM
- **2.5× slower** for 10× tighter tolerance

### Adaptive Tolerance

**Concept**: Vary tolerance based on operation.

**Example Strategy**:
- Roughing passes: Loose tolerance (P = 0.020")
- Semi-finishing: Medium (P = 0.005")
- Finishing pass: Tight (P = 0.001")

**G-Code**:
```gcode
; Roughing
G64 P0.020
(roughing toolpath)

; Finishing
G64 P0.001
(finishing toolpath)
```

**Benefit**: Optimize cycle time while achieving required final accuracy.

## Acceleration Limiting

### Jerk-Limited Acceleration

**Problem**: Instantaneous acceleration changes (trapezoidal profile) cause vibration.

**Solution**: Limit jerk (rate of acceleration change).

**S-Curve Profile** (covered in Section 19.7):
- Smooth acceleration transitions
- Requires look-ahead to plan jerk-limited ramps

**Look-Ahead for Jerk**:
- Calculate jerk-limited acceleration distance
- Ensure sufficient distance available before corner
- If not, reduce velocity earlier

### Coordinated Acceleration

**Multi-Axis Constraint**: All axes must respect acceleration limits.

**Example** (diagonal move with corner):
- X and Y accelerating simultaneously
- Combined acceleration vector: $\vec{a} = [a_X, a_Y]$
- Constraint: $|\vec{a}| \leq a_{max}$ (for each axis)

**Look-Ahead Planner**: Calculate required axis accelerations for path, reduce feedrate if any axis limit exceeded.

## CAM Integration

### G-Code Post-Processing

**CAM Software**: Generates toolpath geometry.

**Post-Processor**: Converts geometry to G-code.

**Post-Processor Responsibilities**:
1. Set appropriate G64 mode and tolerance
2. Insert feedrate changes for tight corners
3. Break complex curves into linear segments
4. Optimize move order for efficiency

**Example** (CAM Output):
```gcode
G64 P0.002  ; Tight tolerance for finishing
G1 X0 Y0 Z0.1 F100
G1 X0.1 Y0
G1 X0.2 Y0.005
G1 X0.3 Y0.015
; ... (many short line segments approximating curve)
```

**CNC Controller**: Blends these short segments into smooth motion.

### Line Segment Length

**Tolerance vs. Segment Length**:
- Finer segments (0.001" long): Smoother curves, more processing
- Coarser segments (0.010" long): Faster processing, chord error

**Typical CAM Output**:
- Roughing: 0.010-0.050" segments
- Finishing: 0.001-0.010" segments
- High-precision: 0.0001-0.001" segments

**Controller Challenge**: Process thousands of short segments per second.

**Modern Controllers** (e.g., LinuxCNC):
- Can handle 10,000+ segments/second with look-ahead
- Real-time trajectory planning (1 kHz servo loop)

## Feedhold and Feed Override

### Feedhold (Stop in Place)

**Function**: Pause motion immediately while maintaining control.

**Implementation with Look-Ahead**:
1. Feedhold button pressed
2. Controller initiates deceleration (at $a_{max}$)
3. Motion stops smoothly
4. Position maintained (servos still active)
5. Resume: Accelerate back to programmed feedrate

**Challenge**: Look-ahead buffer contains future moves.

**Solution**: Controller tracks current position in buffer, resumes from correct point.

### Feed Rate Override

**Function**: Adjust feedrate in real-time (e.g., 50%-150% of programmed F).

**Example**:
- Programmed: F100
- Override: 120%
- Actual: F120

**Implementation**:
- Controller scales velocity profile by override factor
- Look-ahead planner recomputes constraints in real-time
- Smooth transition (ramp from old feedrate to new)

**Challenge**: Recompute corner velocities, acceleration profiles on-the-fly.

**Modern Controllers**: Handle override changes seamlessly (background recomputation).

## Advanced Blending Techniques

### Biarc Blending

**Biarc**: Two circular arcs (tangent to each other and to incoming/outgoing lines).

**Advantage**: Smoother than single circular arc (better approximation of optimal path).

**Application**: High-precision contouring (better than simple circular blend).

**Complexity**: More computation; not common in standard CNC controllers.

### Spline Blending

**Cubic Spline**: Smooth curve (continuous to 2nd derivative).

**Blending**: Fit spline through multiple consecutive points.

**Example**:
```gcode
G1 X1 Y0
G1 X2 Y1
G1 X3 Y1.5
G1 X4 Y1.8
```

**Spline Blend**: Single smooth curve through all 4 points (instead of 3 separate blends).

**Advantage**: Optimal smoothness, fewer acceleration changes.

**Challenge**: Requires advanced look-ahead (multiple moves at once).

**Support**: LinuxCNC (G5.1 cubic spline), limited in other controllers.

### NURBS Interpolation

**NURBS** (Non-Uniform Rational B-Splines): Industry-standard CAD curve representation.

**Direct NURBS G-Code** (G5.2/G5.3):
- CAM outputs NURBS parameters directly
- Controller interpolates NURBS in real-time
- No line segment approximation needed

**Advantage**: Perfect curve fidelity, minimal G-code size.

**Disadvantage**: Complex interpolation, limited controller support.

**Status**: Emerging technology (not widely supported yet).

## Performance Benchmarking

### Cycle Time Comparison

**Test Part**: Square with rounded corners (4 corners, 10" sides)

**Exact Stop Mode (G61)**:
- Stop at each corner: 4 stops
- Acceleration time: 0.5 s per stop
- Total stop time: 4 × 0.5 × 2 = 4 seconds (accel + decel)
- Cutting time: 40 / (100 IPM) × 60 = 24 seconds
- **Total: 28 seconds**

**Blending Mode (G64)**:
- No complete stops
- Corner velocity: 80 IPM (from blend calculation)
- Decel/accel time: ~0.2 s per corner
- Total transition time: 4 × 0.2 = 0.8 seconds
- Cutting time: ~24 seconds (varies with velocity profile)
- **Total: ~25 seconds**

**Savings**: 3 seconds (11% reduction) for this simple part.

**Complex Part** (hundreds of corners):
- Savings can be 30-50% with blending.

### Surface Finish Comparison

**Exact Stop**:
- Visible start/stop marks at corners
- Scalloping from deceleration/acceleration
- Rougher finish (Ra = 100-200 μin typical)

**Blending**:
- Smooth continuous motion
- No start/stop marks
- Better finish (Ra = 50-100 μin typical)
- May have slight corner rounding (within tolerance)

## Summary

Look-ahead and path blending are essential for high-performance CNC:

**Key Concepts**:
1. **Look-Ahead Buffer**: Read multiple blocks ahead, plan smooth continuous motion
2. **Corner Blending**: Round corners to maintain velocity (G64 mode)
3. **Tolerance-Based Blending**: Balance speed and accuracy (G64 P)
4. **Velocity Planning**: Compute optimal feedrate considering all upcoming constraints

**Benefits**:
- **30-50% faster** cycle times (vs. exact stop)
- **Better surface finish** (no start/stop marks)
- **Smoother motion** (less vibration, mechanical stress)

**Trade-Offs**:
- Path deviation at corners (controlled by tolerance)
- More complex controller (computational requirements)
- Tuning needed (tolerance selection)

**Modern CNC Controllers**: Implement sophisticated look-ahead and blending automatically (LinuxCNC, Mach4, industrial controllers).

**Next Steps**:
- Implement in LinuxCNC (Section 19.10)
- Implement in Mach4 (Section 19.11)
- Troubleshooting and optimization (Section 19.12)

---

**Next**: [19.10 Implementation in LinuxCNC](section-19.10-linuxcnc.md)
