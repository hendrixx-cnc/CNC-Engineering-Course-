# Section 15.6 – Canned Cycles

## Overview

Canned cycles are single-block commands that execute complex, repetitive machining operations automatically. Instead of programming every motion explicitly, a canned cycle condenses drilling, tapping, boring, and pocketing operations into one line of code with parameters.

This section covers the standard canned cycles (G81-G89), their parameters, return modes, and practical applications for efficient CNC programming.

## Canned Cycle Fundamentals

### Purpose and Benefits

**Without canned cycles:**
```gcode
G00 X10 Y10 Z5.0           (Position above hole 1)
G01 Z-20.0 F100            (Drill to depth)
G00 Z5.0                   (Retract)
G00 X20 Y10                (Position above hole 2)
G01 Z-20.0 F100            (Drill to depth)
G00 Z5.0                   (Retract)
(... repeat for every hole ...)
```

**With canned cycles:**
```gcode
G81 X10 Y10 Z-20.0 R5.0 F100    (Drill hole 1)
X20 Y10                         (Drill hole 2)
X30 Y10                         (Drill hole 3)
G80                             (Cancel cycle)
```

**Benefits:**
- **Reduced code length**: 1-2 lines per hole vs. 5-10 lines
- **Fewer errors**: Standardized motion sequence
- **Easier editing**: Change depth or feed once, affects all holes
- **Better readability**: Intent is clear from G-code number

### Common Parameters

All canned cycles use a standard set of parameters:

| Parameter | Meaning | Units |
|-----------|---------|-------|
| **X, Y** | Hole position (in current work offset) | Distance |
| **Z** | Depth of operation (absolute or incremental) | Distance |
| **R** | Retract plane (safe height above surface) | Distance |
| **Q** | Peck increment (for peck drilling) | Distance |
| **P** | Dwell time at bottom of hole | Seconds or milliseconds |
| **F** | Feed rate for drilling/boring | Units/min |

### Canned Cycle Sequence

Standard motion sequence for most cycles:

1. **Rapid (G00) to XY position** at current Z height
2. **Rapid (G00) to R plane** (retract height)
3. **Feed (G01) operation** specific to cycle type
4. **Action at depth** (dwell, stop, reverse)
5. **Retract** to R plane or initial Z (depending on return mode)
6. **Repeat** for next XY position

### Modal Behavior

Canned cycles are **modal** – once activated, they repeat at each new XY position:

```gcode
G81 X10 Y10 Z-20 R5.0 F100    (Activate cycle, drill hole 1)
X20 Y10                        (Drill hole 2 with same parameters)
X30 Y10                        (Drill hole 3)
Y20                            (Drill hole 4 at X30 Y20)
G80                            (Cancel cycle)
```

### G80 – Cancel Canned Cycle

**G80** cancels active canned cycle:

```gcode
G80                            (Cancel canned cycle mode)
```

After G80, XY moves do not trigger drilling operations.

**Best practice:** Always cancel canned cycles before resuming normal programming.

## Return Modes

### G98 – Return to Initial Z

**G98** returns the tool to the Z height before the cycle started:

```gcode
G00 Z10.0                      (Start at Z=10)
G98 G81 X10 Y10 Z-20 R5.0 F100 (Drill, return to Z=10)
X20 Y10                        (Drill, return to Z=10)
```

**Motion:**
1. Rapid to X10 Y10 at Z=10
2. Rapid to R plane (Z=5)
3. Feed to depth (Z=-20)
4. Rapid back to **Z=10 (initial level)**
5. Rapid to X20 Y10 at Z=10
6. Repeat cycle

**Use when:**
- Holes are far apart
- Obstacles between holes (clamps, risers)
- Maximum clearance needed

### G99 – Return to R Plane

**G99** returns the tool to the R plane only:

```gcode
G00 Z10.0                      (Start at Z=10)
G99 G81 X10 Y10 Z-20 R5.0 F100 (Drill, return to R=5)
X20 Y10                        (Drill, return to R=5)
```

**Motion:**
1. Rapid to X10 Y10 at Z=10
2. Rapid to R plane (Z=5)
3. Feed to depth (Z=-20)
4. Rapid back to **Z=5 (R plane)**
5. Rapid to X20 Y10 at Z=5
6. Repeat cycle

**Use when:**
- Holes are close together
- No obstacles between holes
- Faster cycle time (less Z travel)

**Default:** Most controls default to G99 (R-plane return).

## Standard Drilling Cycles

### G81 – Drilling Cycle (Simple)

Basic drilling cycle with feed in, rapid out:

```gcode
G81 X__ Y__ Z__ R__ F__
```

**Sequence:**
1. Rapid to XY at current Z
2. Rapid to R plane
3. Feed to Z depth
4. Rapid out to R plane (G99) or initial Z (G98)

**Example:**
```gcode
G00 Z10.0                      (Initial Z)
G99 G81 X10 Y10 Z-20 R5.0 F100 (Drill to -20mm depth)
X20 Y10                        (Drill second hole)
X30 Y10                        (Drill third hole)
G80                            (Cancel)
```

**Applications:**
- Through holes in thin material
- Spotting for larger drills
- Pilot holes

**Limitations:**
- No chip breaking (can pack chips in deep holes)
- Full-depth feed (may overload small drills)

### G82 – Drilling Cycle with Dwell

Drilling with dwell at bottom for chip breaking and hole finish:

```gcode
G82 X__ Y__ Z__ R__ P__ F__
```

**Additional parameter:**
- **P**: Dwell time at depth (seconds or milliseconds, control-dependent)

**Sequence:**
1. Rapid to XY at current Z
2. Rapid to R plane
3. Feed to Z depth
4. **Dwell for P seconds**
5. Rapid out

**Example:**
```gcode
G99 G82 X10 Y10 Z-20 R5.0 P1.0 F100    (Drill with 1-second dwell)
X20 Y10
G80
```

**Applications:**
- Flat-bottom holes
- Breaking stringy chips (aluminum, brass)
- Improved hole finish
- Chamfering hole exit

**Dwell time selection:**
- **Chip breaking**: 0.5-1.0 seconds
- **Finish improvement**: 1.0-2.0 seconds
- **Too long**: Wastes time, may work-harden material

### G83 – Peck Drilling Cycle

Deep hole drilling with periodic retraction for chip clearing:

```gcode
G83 X__ Y__ Z__ R__ Q__ F__
```

**Additional parameter:**
- **Q**: Peck increment (depth to drill before retract)

**Sequence (each peck):**
1. Rapid to XY at current Z (first peck only)
2. Rapid to R plane (first peck only)
3. Feed down Q distance (or to Z depth, whichever is less)
4. **Rapid retract to R plane (full retract)**
5. Rapid back to 0.1mm above previous depth
6. Repeat until Z depth reached
7. Rapid out

**Example:**
```gcode
G99 G83 X10 Y10 Z-50 R5.0 Q10.0 F80    (Drill 50mm deep, 10mm pecks)
X20 Y10
G80
```

**Motion detail for Q10, Z-50:**
- Peck 1: Feed to -10, rapid to R5.0, rapid to -9.9
- Peck 2: Feed to -20, rapid to R5.0, rapid to -19.9
- Peck 3: Feed to -30, rapid to R5.0, rapid to -29.9
- Peck 4: Feed to -40, rapid to R5.0, rapid to -39.9
- Peck 5: Feed to -50, rapid out

**Applications:**
- Deep holes (depth > 3× diameter)
- Difficult-to-machine materials
- Prevents chip packing and tool breakage

**Q value selection:**

$$Q = (1.5 \text{ to } 3) \times D$$

Where D = drill diameter

- **Aluminum, soft materials**: Q = 3D
- **Steel, hard materials**: Q = 1.5-2D
- **Very deep holes**: Start with 2D, reduce if problems

### G73 – High-Speed Peck Drilling

Similar to G83 but with **partial retract** for chip breaking:

```gcode
G73 X__ Y__ Z__ R__ Q__ F__
```

**Sequence (each peck):**
1. Feed down Q distance
2. **Rapid retract 0.5-1.0mm (partial retract)**
3. Repeat until Z depth reached
4. Rapid out to R plane

**Difference from G83:**
- G83: Full retract to R plane (slow, thorough chip clearing)
- G73: Partial retract (fast, chip breaking only)

**Applications:**
- Holes 3-8× diameter deep
- Cast iron (short chips)
- High-speed drilling
- When full retract is unnecessary

**Example:**
```gcode
G99 G73 X10 Y10 Z-30 R5.0 Q8.0 F150    (Fast peck, 30mm deep)
```

## Tapping Cycles

### G84 – Tapping Cycle (Synchronized)

Rigid tapping with synchronized spindle and Z-axis:

```gcode
G84 X__ Y__ Z__ R__ F__
```

**Feed rate calculation:**

$$F = S \times P$$

Where:
- F = feed rate (mm/min or IPM)
- S = spindle speed (RPM)
- P = thread pitch (mm or inches per thread)

**Sequence:**
1. Rapid to XY at current Z
2. Rapid to R plane
3. **Spindle on CW (M03)**
4. Feed to Z depth (synchronized)
5. **Spindle reverse CCW (M04)**
6. Feed out to R plane (synchronized)
7. **Spindle CW (M03)**

**Example (M6×1.0 thread):**
```gcode
S500 M03                       (500 RPM)
G99 G84 X10 Y10 Z-20 R5.0 F500 (F = 500 RPM × 1.0 mm/rev)
X20 Y10
G80
M05
```

**For inch threads:**
```gcode
S400 M03                       (400 RPM)
G99 G84 X1.0 Y1.0 Z-0.75 R0.2 F100    (1/4-20: F = 400 × 0.05 = 20 IPM)
```

Where 1/20 = 0.05 inches per thread

**Requirements:**
- Rigid tapping capability (encoder feedback)
- Proper feed rate calculation
- Tapping head or tension/compression holder (for floating taps)

**Applications:**
- Through holes and blind holes
- Consistent thread depth
- Faster than hand tapping

### G74 – Left-Hand Tapping (Counter-boring)

Tapping cycle for left-hand threads or counter-boring:

```gcode
G74 X__ Y__ Z__ R__ F__
```

**Sequence:**
- Same as G84, but starts with **M04 (CCW)** and reverses to **M03 (CW)**

**Applications:**
- Left-hand threads
- Reverse boring
- Counter-boring operations

### G84.2/G84.3 – Tapping with Peck (Control-Dependent)

Some controls support peck tapping for chip breaking:

```gcode
G84.2 X__ Y__ Z__ R__ Q__ F__
```

**Sequence:**
- Feed-tap Q distance
- Reverse spindle briefly
- Forward spindle
- Continue until depth

**Not universally supported** – check control manual.

## Boring Cycles

### G85 – Boring Cycle (Feed In, Feed Out)

Simple boring with feed in and feed out:

```gcode
G85 X__ Y__ Z__ R__ F__
```

**Sequence:**
1. Rapid to XY at current Z
2. Rapid to R plane
3. Feed to Z depth
4. **Feed out to R plane** (no rapid)

**Applications:**
- Precision holes requiring good finish on exit
- Boring bars sensitive to rapid retract
- When chip evacuation during retract is needed

**Example:**
```gcode
G99 G85 X50 Y50 Z-25 R5.0 F80    (Bore hole, feed in and out)
```

### G86 – Boring Cycle (Feed In, Spindle Stop, Rapid Out)

Boring with spindle stop at depth before rapid retract:

```gcode
G86 X__ Y__ Z__ R__ F__
```

**Sequence:**
1. Rapid to XY at current Z
2. Rapid to R plane
3. Feed to Z depth
4. **Spindle stop (M05)**
5. Rapid out to R plane
6. **Spindle start (M03)**

**Applications:**
- Avoiding tool marks on hole finish
- Boring bars that deflect under cutting forces
- Precision bore diameter control

**Limitation:** Slower due to spindle stop/start

### G87 – Back Boring Cycle

Advanced boring cycle for interrupted cuts (not universally supported):

```gcode
G87 X__ Y__ Z__ R__ Q__ F__
```

**Sequence:**
1. Orient spindle (M19)
2. Rapid away from hole
3. Rapid to depth
4. Feed bore
5. Retract

**Rare in modern practice** – primarily for horizontal boring mills.

### G88 – Boring Cycle (Feed In, Spindle Stop, Manual Retract)

Boring with manual retract:

```gcode
G88 X__ Y__ Z__ R__ P__ F__
```

**Sequence:**
1. Feed to depth
2. Dwell P seconds
3. Spindle stop
4. **Wait for manual retract** (operator jogs Z)

**Application:** Very large or delicate bores where automatic retract may cause damage.

### G89 – Boring Cycle (Feed In, Dwell, Feed Out)

Precision boring with dwell at depth:

```gcode
G89 X__ Y__ Z__ R__ P__ F__
```

**Sequence:**
1. Rapid to XY at current Z
2. Rapid to R plane
3. Feed to Z depth
4. **Dwell P seconds**
5. Feed out to R plane

**Applications:**
- Precision hole sizing
- Excellent surface finish
- Relieving cutting forces before retract

**Example:**
```gcode
G99 G89 X50 Y50 Z-30 R5.0 P2.0 F50    (Precision bore with 2-sec dwell)
```

## Canned Cycle Summary Table

| Cycle | Name | Feed In | Action at Depth | Retract | Application |
|-------|------|---------|-----------------|---------|-------------|
| **G80** | Cancel | - | - | - | Cancel active cycle |
| **G81** | Drill | Yes | None | Rapid | Simple drilling |
| **G82** | Drill/Dwell | Yes | Dwell | Rapid | Chip break, finish |
| **G83** | Peck Drill | Yes | Full retract each peck | Rapid | Deep holes |
| **G73** | Hi-Speed Peck | Yes | Partial retract | Rapid | Cast iron, short chips |
| **G84** | Tap | Yes | Spindle reverse | Feed out | Right-hand threads |
| **G74** | Left Tap | Yes | Spindle reverse | Feed out | Left-hand threads |
| **G85** | Bore | Yes | None | Feed | Precision boring |
| **G86** | Bore | Yes | Spindle stop | Rapid | Fine finish, no marks |
| **G89** | Bore/Dwell | Yes | Dwell | Feed | Ultra-precision |

## Practical Examples

### Example 1: Bolt Circle (4 Holes)

```gcode
G21 G90 G17 G54
T01 M06                        (6mm drill)
G43 H01
S2000 M03
M08

G00 X50 Y50 Z10.0              (Center of 100mm bolt circle)

(Drill 4 holes on 100mm BC)
G99 G83 Z-15 R5.0 Q5.0 F100    (Peck drill)
X100 Y50                        (0°)
X50 Y100                        (90°)
X0 Y50                          (180°)
X50 Y0                          (270°)
G80                             (Cancel)

G00 Z50.0
M09
M05
M30
```

### Example 2: Drilling, Tapping Sequence

```gcode
G21 G90 G17 G54

(--- TOOL 1: 5MM DRILL (TAP DRILL FOR M6×1.0) ---)
T01 M06
G43 H01
S1500 M03
M08

G99 G81 Z-18 R5.0 F120         (Drill tap holes)
X10 Y10
X40 Y10
X10 Y40
X40 Y40
G80

M09
M05
G00 Z50.0

(--- TOOL 2: M6×1.0 TAP ---)
T02 M06
G43 H02
S400 M03                        (400 RPM for tapping)

G99 G84 Z-15 R5.0 F400          (F = 400 RPM × 1.0 pitch)
X10 Y10
X40 Y10
X10 Y40
X40 Y40
G80

M05
M30
```

### Example 3: Mixed Hole Depths

```gcode
G21 G90 G17 G54
T01 M06
G43 H01
S2000 M03
M08

(Shallow holes)
G98 G81 Z-10 R5.0 F100
X10 Y10
X20 Y10
G80

(Deep holes - change to peck cycle)
G98 G83 Z-50 R5.0 Q8.0 F80
X30 Y10
X40 Y10
G80

(Counterbore - use G82 with dwell)
G98 G82 Z-8 R5.0 P1.0 F60
X10 Y10                         (Counterbore first hole)
X20 Y10                         (Counterbore second hole)
G80

M09
M05
M30
```

### Example 4: Pattern with Subprogram

```gcode
(Main program - 3 rows of holes)
O1000
G21 G90 G17 G54
T01 M06
G43 H01
S2000 M03
M08

G00 Y0                          (Row 1)
M98 P2000                       (Call hole pattern)
G00 Y25                         (Row 2)
M98 P2000
G00 Y50                         (Row 3)
M98 P2000

M09
M05
M30

(Subprogram - row of 5 holes)
O2000
G99 G81 Z-15 R5.0 F100
X0
X25
X50
X75
X100
G80
M99
```

## Troubleshooting Canned Cycles

### Common Errors

**1. Feed rate not set:**
```gcode
G81 X10 Y10 Z-20 R5.0    (ERROR: No F-word)
```
**Solution:** Always specify F in first cycle call.

**2. R plane below surface:**
```gcode
G81 X10 Y10 Z-20 R-5.0 F100    (R below Z depth - invalid)
```
**Solution:** R plane must be above Z depth (R > Z in absolute mode).

**3. Wrong return mode:**
```gcode
G98 G81 X10 Y10 Z-20 R5.0 F100    (Returns to high Z unnecessarily)
```
**Solution:** Use G99 for closely-spaced holes.

**4. Tapping feed rate incorrect:**
```gcode
S500 M03
G84 X10 Y10 Z-20 R5.0 F100    (Wrong: Should be F500 for 1mm pitch)
```
**Solution:** F = S × Pitch

### Verification Techniques

1. **Simulate program** before running
2. **Single block mode** for first hole
3. **Dry run** above work surface
4. **Check R plane clearance** with tool at Z=R
5. **Verify feed rate** calculation for tapping

## Key Takeaways

1. **Canned cycles** simplify repetitive operations into single-block commands
2. **G81-G89** cover drilling, tapping, and boring operations
3. **G98/G99** control return height (initial Z or R plane)
4. **G83** (peck drilling) essential for deep holes and chip management
5. **G84** (tapping) requires **F = S × Pitch** calculation
6. **Q parameter** controls peck increment
7. **P parameter** specifies dwell time
8. **G80** cancels active canned cycle
9. **Modal behavior** repeats cycle at each new XY position
10. **Proper R plane selection** prevents crashes and optimizes cycle time

***

**Next**: [Section 15.7 – Programming Best Practices](section-15.7-programming-best-practices.md)

**Previous**: [Section 15.5 – Auxiliary Functions](section-15.5-auxiliary-functions.md)
