# Section 15.3 – Motion Commands

## Overview

Motion commands are the foundation of CNC programming, translating geometric paths into coordinated axis movements. The four primary motion modes—rapid positioning (G00), linear interpolation (G01), and circular interpolation (G02/G03)—enable the creation of virtually any 2D or 3D toolpath.

This section provides comprehensive coverage of motion command syntax, trajectory planning, feed rate control, and the mathematical principles underlying linear and circular interpolation.

## G00 – Rapid Positioning

### Function

**G00** commands the machine to move all specified axes simultaneously to the endpoint at maximum traverse speed. This is a **non-cutting move** used for positioning between operations.

**Syntax:**
```gcode
G00 X__ Y__ Z__ A__ B__ C__
```

**Example:**
```gcode
G00 X50.0 Y25.0 Z10.0    (Rapid to position, Z safe above work)
```

### Characteristics

**Multi-axis coordination:**
- All axes move simultaneously
- Each axis travels at its maximum speed
- Motion follows a straight line in machine coordinates
- **Not guaranteed** to follow a straight line in work coordinates when rotary axes are involved

**Speed:**
- Rapid rate set by machine parameters (typically 500-2000 IPM / 12000-50000 mm/min)
- Independent of F-word (feed rate)
- Limited by machine acceleration and servo performance

**Safety considerations:**
- **Never use G00 with tool in contact** with workpiece
- Always retract Z-axis before rapid XY moves
- Check clearances for fixtures, clamps, part edges
- Use safe Z heights appropriate to setup

### Trajectory Planning

The path taken during G00 depends on the controller:

**Type 1: Simultaneous arrival (ideal line)**
- All axes reach endpoint at the same time
- Follows a straight line in space
- Most common on modern CNC controls

**Type 2: Independent axis (dog-leg)**
- Each axis completes at different times
- Fastest axis arrives first, path is not straight
- Common on older controls or when axes have very different speeds

**Example comparison:**

```gcode
G00 X100 Y100    (From origin)
```

**Simultaneous arrival:** Diagonal line from (0,0) to (100,100)
**Independent axis:** L-shaped path if X-axis faster than Y-axis

**Best practice:** Never rely on G00 path shape. Always position with adequate clearance.

### Safe Retract Strategy

Standard practice for safe rapids:

```gcode
G01 Z-10.0 F100        (Cutting at depth)
G00 Z5.0               (Retract Z to safe height)
G00 X100.0 Y50.0       (Rapid XY to next position)
G00 Z-8.0              (Rapid down to near-depth)
G01 Z-10.0 F100        (Feed to cutting depth)
```

This sequence ensures:
1. Z-axis clears workpiece before XY rapid
2. No collision with fixtures or clamps
3. Controlled feed for final approach

## G01 – Linear Interpolation

### Function

**G01** commands coordinated linear motion of all specified axes at a controlled feed rate. This is the primary **cutting move** for straight-line toolpaths.

**Syntax:**
```gcode
G01 X__ Y__ Z__ A__ B__ C__ F__
```

**Example:**
```gcode
G01 X50.0 Y25.0 Z-5.0 F500    (Linear cut to endpoint at 500 units/min)
```

### Characteristics

**Coordinated motion:**
- All axes move in synchronization
- Motion follows a straight line in Cartesian space
- Feed rate applies to the resultant velocity vector
- Arrival at endpoint is simultaneous for all axes

**Feed rate:**
- Specified by F-word in units per minute (G94 mode)
- Remains modal until changed
- Must be set before or with first G01 command
- Applies to subsequent G01 moves until changed

### Feed Rate Calculation

The feed rate F specifies the velocity of the **tool tip** along the programmed path, not individual axis speeds.

**For linear motion, resultant feed rate:**

$$F_{resultant} = \sqrt{(v_X)^2 + (v_Y)^2 + (v_Z)^2}$$

Where $v_X$, $v_Y$, $v_Z$ are individual axis velocities.

**Example:**

```gcode
G01 X10.0 Y0 F100    (Move 10mm in X at 100 mm/min)
```

- Time = Distance / Feed = 10 / 100 = 0.1 minutes = 6 seconds
- $v_X$ = 100 mm/min, $v_Y$ = 0

```gcode
G01 X10.0 Y10.0 F100    (Move diagonally at 100 mm/min resultant)
```

- Path length = $\sqrt{10^2 + 10^2}$ = 14.14 mm
- Time = 14.14 / 100 = 0.1414 minutes = 8.49 seconds
- $v_X$ = 70.71 mm/min, $v_Y$ = 70.71 mm/min
- Resultant = $\sqrt{70.71^2 + 70.71^2}$ = 100 mm/min

The controller automatically calculates individual axis speeds to maintain the programmed feed rate along the path.

### Multi-Axis Linear Motion

G01 supports coordinated motion of any combination of axes:

**XY plane cutting:**
```gcode
G01 X50.0 Y25.0 F500    (2-axis move)
```

**3-axis contouring:**
```gcode
G01 X50.0 Y25.0 Z-5.0 F500    (3-axis move)
```

**4-axis indexed:**
```gcode
G01 X50.0 A90.0 F300    (Linear + rotary)
```

**5-axis simultaneous:**
```gcode
G01 X50.0 Y25.0 Z-5.0 A45.0 B30.0 F200    (All 5 axes)
```

### Incremental vs. Absolute

G01 respects the current distance mode (G90/G91):

**Absolute mode (G90):**
```gcode
G90                     (Absolute mode)
G01 X10.0 Y10.0 F100    (Move to X=10, Y=10)
G01 X20.0 Y20.0         (Move to X=20, Y=20)
```

**Incremental mode (G91):**
```gcode
G91                     (Incremental mode)
G01 X10.0 Y10.0 F100    (Move +10 in X, +10 in Y from current)
G01 X10.0 Y10.0         (Move another +10 in X, +10 in Y)
```

**Mixed mode (some controls):**
```gcode
G90 G91.1               (Absolute distance, incremental arc centers)
G01 X20.0 Y20.0         (Absolute coordinate)
```

## G02 and G03 – Circular Interpolation

### Function

**G02** (clockwise) and **G03** (counterclockwise) command circular or helical motion at controlled feed rate. Essential for arcs, radii, and circular pockets.

**Syntax (center format):**
```gcode
G02 X__ Y__ I__ J__ F__    (CW arc with center offset)
G03 X__ Y__ I__ J__ F__    (CCW arc with center offset)
```

**Syntax (radius format):**
```gcode
G02 X__ Y__ R__ F__    (CW arc with radius)
G03 X__ Y__ R__ F__    (CCW arc with radius)
```

### Direction Convention

The direction (CW vs. CCW) is defined by viewing the plane from the **positive axis** perpendicular to the plane:

**G17 (XY plane):** View from +Z looking down
- G02 = clockwise
- G03 = counterclockwise

**G18 (XZ plane):** View from +Y looking left
**G19 (YZ plane):** View from +X looking right

### Center Format (I, J, K)

The arc center is specified as an **offset from the start point**, not an absolute coordinate.

**Parameters:**
- **I**: Offset from start X to arc center X
- **J**: Offset from start Y to arc center Y
- **K**: Offset from start Z to arc center Z (helical)

**Example:**

```gcode
G90 G17                    (Absolute mode, XY plane)
G00 X0 Y0                  (Start position)
G01 X10.0 Y0 F500          (Move to arc start)
G02 X10.0 Y20.0 I0 J10.0   (CW arc, center at X10 Y10)
```

**Calculation:**
- Start point: (10, 0)
- End point: (10, 20)
- Center offset: I=0, J=10
- Arc center: (10+0, 0+10) = (10, 10)
- Radius: 10 units
- Arc: 180° semicircle from bottom to top

**Visual:**
```
        End (10,20)
           |
    -------C------- Center (10,10)
           |
       Start (10,0)
```

### Radius Format (R)

Simpler syntax using radius directly:

```gcode
G02 X10.0 Y20.0 R10.0 F500    (CW arc with radius 10)
```

**Advantages:**
- Easier to read and understand
- No offset calculation required
- Common for simple arcs

**Limitations:**
- Ambiguous for arcs > 180° (two possible arcs)
- Cannot describe a full circle (start = end)

**Radius sign convention:**
- **R positive**: Arc ≤ 180° (minor arc)
- **R negative**: Arc > 180° (major arc)

**Example:**

```gcode
G00 X0 Y0
G02 X10.0 Y10.0 R10.0    (90° arc, minor)
```

vs.

```gcode
G00 X0 Y0
G02 X10.0 Y10.0 R-10.0   (270° arc, major)
```

### Arc Validation

The controller validates arc geometry before execution. Common errors:

**Radius mismatch:**
```gcode
G00 X0 Y0
G02 X20.0 Y0 I5.0 J0    (ERROR: Start radius ≠ end radius)
```

- Start radius: $\sqrt{5^2 + 0^2}$ = 5
- End radius: $\sqrt{(5-20)^2 + 0^2}$ = 15
- **Mismatch:** Controller rejects or alarms

**Tolerance:** Most controls allow small discrepancies (0.001-0.01mm) due to rounding.

### Helical Interpolation

Adding a Z-component creates a helical path:

```gcode
G17                         (XY plane for arc)
G00 X10.0 Y0 Z0
G02 X10.0 Y0 Z-10.0 I-10.0 J0 F500    (Helical CW, full circle descending 10mm)
```

**Applications:**
- Thread milling
- Circular pockets with depth
- Spiral ramps into material

**Feed rate applies to the 3D helix length:**

$$L_{helix} = \sqrt{L_{arc}^2 + \Delta Z^2}$$

### Full Circle

A full 360° circle requires **I, J, K format** (not R):

```gcode
G00 X10.0 Y0
G02 X10.0 Y0 I-10.0 J0 F500    (Full circle, center at origin)
```

- Start point: (10, 0)
- End point: (10, 0) – same as start
- Center offset: I=-10, J=0
- Arc center: (10-10, 0+0) = (0, 0)
- Radius: 10 units

### Arc Feed Rate

Feed rate applies to the arc **circumference**, not radius:

```gcode
G02 X10.0 Y10.0 I5.0 J0 F500
```

The tool moves along the arc path at 500 units/min, automatically adjusting individual axis speeds for circular motion.

**Calculation example:**

Arc length = $r \times \theta$ (radians)

For 90° arc with radius 10mm:
- Arc length = 10 × (π/2) = 15.71 mm
- At F500 mm/min: Time = 15.71 / 500 = 0.0314 min = 1.88 seconds

## Plane Selection

### G17, G18, G19

Circular interpolation requires a plane selection:

| Code | Plane | Arc Axes | Perpendicular Axis |
|------|-------|----------|--------------------|
| **G17** | XY | X, Y (I, J) | Z |
| **G18** | XZ | X, Z (I, K) | Y |
| **G19** | YZ | Y, Z (J, K) | Z |

**Example G17 (default):**
```gcode
G17                        (XY plane)
G02 X10 Y10 I5 J0 F500     (Arc in XY, I and J offsets)
```

**Example G18:**
```gcode
G18                        (XZ plane)
G02 X10 Z-5 I5 K0 F500     (Arc in XZ, I and K offsets)
```

**Example G19:**
```gcode
G19                        (YZ plane)
G02 Y10 Z-5 J5 K0 F500     (Arc in YZ, J and K offsets)
```

**Default:** Most controls default to G17 at startup.

## Feed Rate Modes

### G94 – Feed Per Minute (Default)

Feed rate specifies tool velocity in units per minute:

```gcode
G94                        (Feed per minute mode)
G01 X100.0 F500            (500 mm/min or IPM)
```

**Characteristics:**
- Most common mode
- Feed rate independent of spindle speed
- Consistent for both linear and circular motion

### G95 – Feed Per Revolution

Feed rate specifies tool advance per spindle revolution:

```gcode
G95                        (Feed per revolution mode)
S1000 M03                  (1000 RPM)
G01 X100.0 F0.1            (0.1 mm per revolution = 100 mm/min)
```

**Effective feed rate:**

$$F_{effective} = F_{per\_rev} \times S_{RPM}$$

**Applications:**
- Threading
- Turning operations
- Constant chip load regardless of diameter

### G93 – Inverse Time Feed

Feed rate specifies the inverse of the time for the move:

```gcode
G93                        (Inverse time mode)
G01 X100.0 F10.0           (Move completes in 1/10 = 0.1 minutes)
```

**Characteristics:**
- F-word must be specified for every move
- Used in some CAM post-processors for 5-axis
- Ensures predictable move completion time

## Motion Control Modes

### G61 – Exact Stop Mode

The machine comes to a complete stop at each endpoint:

```gcode
G61                        (Exact stop mode)
G01 X10 Y10 F500
G01 X20 Y10
G01 X20 Y20
```

Each corner is a full deceleration to zero, then acceleration to next move.

**Characteristics:**
- Guarantees corner accuracy
- Slower cycle time due to decel/accel
- Use for precise corners, inspection points

### G64 – Continuous Path Mode

The machine blends motion between blocks without stopping:

```gcode
G64 P0.01                  (Continuous mode, 0.01mm path tolerance)
G01 X10 Y10 F500
G01 X20 Y10
G01 X20 Y20
```

**Characteristics:**
- Maintains velocity through corners (path blending)
- Faster cycle times
- May round corners slightly (within tolerance P value)
- Default mode on most modern controls

**Tolerance parameter:**
- **P value**: Maximum deviation from programmed path
- Smaller P = tighter corners, slower speed
- Larger P = smoother motion, higher speed

### G64 P0 – Maximum Speed Blending

```gcode
G64 P0                     (Maximum blending, no path tolerance limit)
```

Use for non-critical contouring where speed is prioritized over corner accuracy.

## Practical Examples

### Example 1: Simple Rectangle

```gcode
G21 G90 G17 G94            (Metric, absolute, XY plane, feed/min)
G54                        (Work offset 1)
T01 M06                    (12mm end mill)
G43 H01                    (Tool length offset)
S2000 M03                  (Spindle on)

G00 X0 Y0 Z5.0             (Rapid to start, safe Z)
G01 Z-5.0 F100             (Plunge to depth)
G01 X50.0 Y0 F500          (Side 1)
G01 X50.0 Y25.0            (Side 2)
G01 X0 Y25.0               (Side 3)
G01 X0 Y0                  (Side 4, close rectangle)
G01 Z5.0 F100              (Retract)

M05                        (Spindle off)
M30                        (Program end)
```

### Example 2: Arc-Corner Rectangle

```gcode
G21 G90 G17 G94
G54
T01 M06
G43 H01
S2000 M03

G00 X5.0 Y0 Z5.0           (Start 5mm in from corner)
G01 Z-5.0 F100             (Plunge)
G01 X45.0 Y0 F500          (Side 1)
G03 X50.0 Y5.0 R5.0        (Corner 1, radius 5)
G01 X50.0 Y20.0            (Side 2)
G03 X45.0 Y25.0 R5.0       (Corner 2)
G01 X5.0 Y25.0             (Side 3)
G03 X0 Y20.0 R5.0          (Corner 3)
G01 X0 Y5.0                (Side 4)
G03 X5.0 Y0 R5.0           (Corner 4, close)
G01 Z5.0 F100              (Retract)

M05
M30
```

### Example 3: Circular Pocket (Helical Entry)

```gcode
G21 G90 G17 G94
G54
T01 M06                    (12mm end mill)
G43 H01
S2000 M03

(Approach center)
G00 X25.0 Y25.0 Z5.0       (Center of 50mm diameter pocket)
G01 Z0 F100                (Touch surface)

(Helical ramp entry)
G02 X25.0 Y25.0 Z-10.0 I-5.0 J0 F300    (Helix down 10mm, radius 5mm)

(Circular cuts at depth, spiraling outward)
G02 X25.0 Y25.0 I-10.0 J0 F500          (Circle radius 10mm)
G02 X25.0 Y25.0 I-15.0 J0               (Circle radius 15mm)
G02 X25.0 Y25.0 I-20.0 J0               (Circle radius 20mm)
G02 X25.0 Y25.0 I-23.0 J0               (Circle radius 23mm, finish)

(Retract)
G00 Z5.0

M05
M30
```

## Troubleshooting Motion Commands

### Common Errors

**1. Feed rate not defined:**
```gcode
G01 X10 Y10    (ERROR if no F-word previously set)
```
**Solution:** Always initialize F-word before first G01.

**2. Arc radius mismatch:**
```gcode
G02 X10 Y10 I3 J2    (May alarm if start/end radius differ)
```
**Solution:** Verify geometry, check CAM output, adjust tolerance.

**3. Wrong plane selection:**
```gcode
G17                  (XY plane)
G02 X10 Z10 I5 K0    (ERROR: Using X and Z in XY plane)
```
**Solution:** Switch to G18 for XZ arcs.

**4. Full circle with R format:**
```gcode
G02 X10 Y0 R10       (ERROR: Start = end, ambiguous)
```
**Solution:** Use I, J, K format for 360° arcs.

### Debugging Techniques

1. **Simulation:** Visualize toolpath in CAM or verifier
2. **Dry run:** Execute with feed override at 0% or in air above part
3. **Single block:** Step through program one line at a time
4. **Arc validation:** Calculate start/end radius manually to verify

## Key Takeaways

1. **G00** is for rapid, non-cutting moves; **G01** is for linear cutting moves
2. **Feed rate** (F-word) controls G01 velocity and is modal
3. **G02/G03** create circular arcs; direction depends on plane and viewpoint
4. **I, J, K** specify arc center as offset from start; **R** specifies radius
5. **Plane selection** (G17/G18/G19) determines which axes participate in arcs
6. **Helical interpolation** combines circular motion with linear Z movement
7. **G64** enables path blending for smooth, fast contouring
8. **Always validate** arc geometry and feed rates before running

***

**Next**: [Section 15.4 – Coordinate Systems](section-15.4-coordinate-systems.md)

**Previous**: [Section 15.2 – G-Code Structure](section-15.2-gcode-structure.md)
