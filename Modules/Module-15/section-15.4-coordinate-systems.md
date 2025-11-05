# Section 15.4 – Coordinate Systems and Work Offsets

## Overview

Coordinate systems form the foundation of CNC positioning, enabling programs to reference part geometry independent of machine position. Work offsets, tool length compensation, and cutter radius compensation allow the same program to be used across multiple setups, tools, and machines.

This section covers absolute and incremental positioning, work coordinate systems (G54-G59), tool offsets, and the transformation hierarchy that connects machine coordinates to programmed part features.

## Machine Coordinate System (MCS)

### Definition

The **machine coordinate system** is the fundamental reference frame established when the machine is homed. It represents absolute positions relative to physical hard stops or encoder markers.

**Characteristics:**
- Origin (0, 0, 0) at a fixed machine location
- Established by homing sequence (G28, G30)
- Never changes unless re-homed
- Used internally by controller for limit checking

**Typical machine origin locations:**

| Machine Type | X=0 | Y=0 | Z=0 |
|--------------|-----|-----|-----|
| **Vertical mill** | Left or center | Front or center | Top of travel |
| **Horizontal mill** | Spindle center | Table center | Spindle face |
| **Lathe** | Spindle centerline | - | Chuck face or tail |
| **Gantry** | Lower left | Lower left | Table surface |

### Homing Commands

**G28 – Return to home via intermediate point:**
```gcode
G28 G91 Z0         (Return Z-axis to home via current position)
G28 X0 Y0          (Return X and Y to home via current position)
```

**G28 workflow:**
1. Move in incremental mode to specified intermediate point
2. From intermediate point, move to machine home
3. Reset internal position to machine zero

**G30 – Return to secondary home (if equipped):**
```gcode
G30 G91 Z0         (Return Z to secondary home position)
```

Used for:
- Tool changer position
- Pallet change location
- Safe parking position

### Soft Limits

The machine coordinate system enforces travel limits:

```gcode
(Machine X travel: -500 to +500)
G53 G00 X600       (ERROR: Beyond soft limit)
```

**G53** accesses machine coordinates directly (bypass work offsets).

## Work Coordinate Systems (WCS)

### Purpose

Work offsets allow programming relative to part features rather than machine position. The same program can run on different fixtures, machines, or setups by changing only the offset values.

**Example:**

Program reference: Part corner at X0 Y0 Z0
- **Setup 1**: Part in vise at machine X100 Y50 Z-200
- **Setup 2**: Part in fixture at machine X300 Y150 Z-180

By setting work offsets, the program X0 Y0 Z0 automatically maps to the correct machine position.

### G54 through G59 – Work Offset Selection

ISO 6983 defines six standard work coordinate systems:

| Code | Work Coordinate System |
|------|------------------------|
| **G54** | Work offset 1 (default) |
| **G55** | Work offset 2 |
| **G56** | Work offset 3 |
| **G57** | Work offset 4 |
| **G58** | Work offset 5 |
| **G59** | Work offset 6 |

**Extended offsets (control-dependent):**
- **G59.1** through **G59.9**: Additional offsets
- Some controls support G54.1 P1-P99 for 99+ offsets

**Usage:**
```gcode
G54                (Select work offset 1)
G00 X0 Y0 Z0       (Move to part origin in G54)

G55                (Select work offset 2)
G00 X0 Y0 Z0       (Move to part origin in G55)
```

### Setting Work Offsets

Work offsets are set through controller interface or G10 command:

**Method 1: Manual (touch-off):**
1. Jog tool to known part feature (corner, edge, hole center)
2. Record machine position
3. Enter offset: Machine_Position - Desired_Work_Position

**Example:**
- Touch top of part with tool tip
- Machine Z position: -187.325
- Desired work Z position: 0 (top of part)
- G54 Z offset: -187.325 - 0 = -187.325

**Method 2: Probing (automatic):**
```gcode
G54                (Select work offset to set)
G10 L20 P1 X0 Y0   (Set current position as X0 Y0 in G54)
```

**Method 3: G10 L2 (set offset value):**
```gcode
G10 L2 P1 X100.0 Y50.0 Z-200.0    (Set G54 offsets directly)
```

Where P specifies the offset number (P1=G54, P2=G55, etc.)

### Work Offset Table

Internally, the controller stores offset values:

| Offset | X | Y | Z | Notes |
|--------|---|---|---|-------|
| **G54** | 100.000 | 50.000 | -200.000 | Vise, jaw 1 |
| **G55** | 300.000 | 50.000 | -200.000 | Vise, jaw 2 |
| **G56** | 150.000 | 150.000 | -180.000 | Fixture plate A |
| **G57** | 0 | 0 | 0 | (not set) |
| **G58** | 0 | 0 | 0 | (not set) |
| **G59** | 0 | 0 | 0 | (not set) |

### Coordinate Transformation

When work offset is active, programmed coordinates transform:

$$Machine\_Position = Work\_Position + Offset\_Value$$

**Example:**
- Active offset: G54 (X100, Y50, Z-200)
- Programmed move: G01 X10 Y20 Z-5
- Machine moves to: X110, Y70, Z-205

### G53 – Machine Coordinate Override

**G53** bypasses all offsets for a single block:

```gcode
G54                (Work offset active)
G53 G00 X0 Y0 Z0   (Move to machine home, ignore G54)
G00 X0 Y0 Z0       (Move to work offset origin)
```

**Applications:**
- Tool changer position
- Safe parking location
- Absolute machine moves for setup

**Important:** G53 is non-modal (one block only).

## Absolute and Incremental Positioning

### G90 – Absolute Mode (Default)

In absolute mode, coordinates specify the endpoint position relative to the work coordinate system origin.

```gcode
G90                (Absolute mode)
G54                (Work offset 1)
G01 X10 Y10 F500   (Move to X=10, Y=10 in G54)
G01 X20 Y20        (Move to X=20, Y=20 in G54)
```

**Characteristics:**
- Most common programming mode
- Coordinates match part print dimensions
- Easy to verify and troubleshoot
- Cumulative errors do not occur

### G91 – Incremental Mode

In incremental mode, coordinates specify movement distance from the current position.

```gcode
G91                (Incremental mode)
G01 X10 Y10 F500   (Move +10 in X, +10 in Y from current)
G01 X10 Y10        (Move another +10 in X, +10 in Y)
```

**Characteristics:**
- Used for repetitive patterns, bolt circles
- Easier for some pocketing operations
- Risk of cumulative positioning errors
- Harder to verify against print

### Modal Behavior

Distance mode (G90/G91) is modal and persists until changed:

```gcode
G90                (Absolute mode active)
G01 X10 Y10
G01 X20 Y20        (Still absolute)
G91                (Switch to incremental)
G01 X5 Y5          (Incremental move)
G01 X5 Y5          (Still incremental)
G90                (Return to absolute)
```

**Best practice:** Always initialize G90 or G91 at program start.

### Mixed Mode (G90.1, G91.1)

Some controls support independent distance modes for arcs:

```gcode
G90 G91.1          (Absolute XYZ, incremental IJK)
G02 X20 Y20 I5 J0  (Endpoint absolute, center offset incremental)
```

**G90.1:** Arc center (IJK) in absolute mode
**G91.1:** Arc center (IJK) in incremental mode (default)

## Tool Length Compensation

### Purpose

Tool length offset compensates for differences in tool length, allowing the program to reference part geometry (e.g., top surface Z=0) regardless of which tool is in the spindle.

**Without tool offset:**
- Program must know exact tool length
- Changing tools requires program edits
- Impractical for multi-tool operations

**With tool offset:**
- Program references part geometry
- Tool table stores each tool's length
- Tool changes require no program edits

### G43 – Tool Length Offset Enable

**G43** activates tool length compensation:

```gcode
T01 M06            (Change to tool 1)
G43 H01            (Apply tool length offset 1)
G00 Z0             (Move to Z=0 in work coordinates)
```

**H-word** specifies the offset register (usually matches tool number).

### G49 – Tool Length Offset Cancel

**G49** cancels tool length offset:

```gcode
G49                (Cancel tool length offset)
G00 Z0             (Z=0 in machine coordinates, dangerous!)
```

**Warning:** G49 with Z moves can crash tool into table. Always retract Z before G49.

### Tool Length Offset Table

Controller stores measured tool lengths:

| Tool | H | Length (mm) | Description |
|------|---|-------------|-------------|
| **T01** | H01 | 150.325 | 12mm end mill |
| **T02** | H02 | 175.128 | 6mm drill |
| **T03** | H03 | 148.956 | 8mm end mill |
| **T04** | H04 | 165.442 | Spot drill |

### Setting Tool Lengths

**Method 1: Touch-off to known surface:**
1. Load tool in spindle
2. Jog tool tip to touch reference surface (gauge block, part top)
3. Note machine Z position
4. Calculate: Length = Reference_Height - Machine_Z

**Method 2: Tool height setter (automatic):**
- Tool touches probe on table
- Controller measures and stores length
- Reference height already known

**Method 3: G10 L1 (set tool length directly):**
```gcode
G10 L1 P1 Z150.325    (Set tool 1 length to 150.325)
```

### Tool Length Calculation Example

**Scenario:**
- Reference surface: Top of part, Z=0 in work coordinates
- Machine Z when touching part: -187.325
- Tool tip at part top: -187.325 (machine) = 0 (work)

**With tool change:**
- Tool 1 length: 150.325
- Tool 2 length: 175.128
- Difference: 24.803

When switching from T01 to T02:
- Controller automatically adjusts Z position by -24.803
- Tool tip remains at same work coordinate Z position

### G43.1 – Dynamic Tool Length Offset

Some controls support dynamic offset specification:

```gcode
G43.1 Z150.325     (Apply offset value directly)
```

Used for:
- Temporary offsets
- Parametric tool length from variables
- Special probing operations

## Cutter Radius Compensation

### Purpose

Cutter radius compensation adjusts the toolpath to account for tool radius, allowing programs to be written to part geometry rather than tool center.

**Without compensation:**
- Program must offset path by tool radius
- Changing tool size requires program edits
- CAM must generate tool center path

**With compensation:**
- Program follows part edge
- Tool radius in tool table
- Same program works with different tool sizes

### G40, G41, G42

| Code | Function |
|------|----------|
| **G40** | Cutter compensation off |
| **G41** | Cutter compensation left |
| **G42** | Cutter compensation right |

**G41 (left):** Tool moves to left of programmed path (for outside profile)
**G42 (right):** Tool moves to right of programmed path (for inside profile)

**Direction** is determined by looking in the direction of travel.

### Activation and Cancellation

**Activate:**
```gcode
G00 X-10 Y0        (Approach outside part)
G41 D01 G01 X0 Y0 F500    (Enable compensation, move to part edge)
G01 X50 Y0         (Follow part edge, compensated)
G01 X50 Y25
G01 X0 Y25
G01 X0 Y0
G40 G01 X-10 Y0    (Cancel compensation, move away)
```

**D-word** specifies the tool radius offset register.

**Cancel:**
```gcode
G40                (Cancel compensation)
```

### Tool Radius Table

| Tool | D | Radius (mm) | Diameter (mm) |
|------|---|-------------|---------------|
| **T01** | D01 | 6.000 | 12.0 |
| **T02** | D02 | 3.000 | 6.0 |
| **T03** | D03 | 4.000 | 8.0 |

### Compensation Logic

The controller offsets the tool path perpendicular to the direction of travel:

**Example:**
- Programmed path: X0→X50 (horizontal line)
- Tool radius: 6mm
- G41 active: Tool center moves from Y-6→Y-6 (tool below path)
- G42 active: Tool center moves from Y+6→Y+6 (tool above path)

### Lead-In and Lead-Out

Compensation requires lead-in and lead-out moves:

```gcode
(Outside profile - G41)
G00 X-10 Y0        (Start outside part)
G41 D01 G01 X0 Y0  (Lead-in, activate compensation)
(... part profile ...)
G40 G01 X-10 Y0    (Lead-out, cancel compensation)
```

**Lead-in distance:** At least 1× tool radius, preferably 2-3×

### Look-Ahead

The controller looks ahead to future blocks to calculate correct offset:

```gcode
G41 D01            (Compensation active)
G01 X10 Y0         (Straight)
G01 X10 Y10        (90° corner)
```

At the corner, controller automatically calculates the circular arc to maintain constant offset from both edges.

### G41.1 / G42.1 – Dynamic Compensation

```gcode
G41.1 D6.0         (Activate compensation with radius 6mm directly)
```

Useful for parametric programming with variable tool sizes.

## Coordinate System Priority

### Transformation Hierarchy

Coordinates are transformed through multiple systems:

1. **Programmed coordinate** (as written in G-code)
2. **+ Work offset** (G54-G59)
3. **+ Tool length offset** (G43 H__)
4. **+ Cutter radius compensation** (G41/G42 D__)
5. **= Machine coordinate** (actual axis position)

**Example:**
- Program: G01 Z-10 (cut 10mm deep)
- G54 Z offset: -200.0 (part top at machine Z-200)
- Tool length H01: 150.325
- Machine Z: -10 + (-200.0) + 150.325 = **-59.675**

### Order of Operations

Commands must be issued in correct sequence:

**Correct:**
```gcode
G54                (Select work offset)
T01 M06            (Change tool)
G43 H01            (Apply tool length)
G00 X0 Y0          (Position in work coordinates)
```

**Incorrect:**
```gcode
G00 X0 Y0          (Move where? No work offset or tool length set!)
G54                (Too late)
G43 H01            (Tool length applied after move)
```

## G92 – Work Coordinate System Shift

### Function

**G92** temporarily shifts the work coordinate system without changing stored offsets.

```gcode
G92 X0 Y0 Z0       (Set current position as origin)
```

**Effect:** Current machine position becomes the specified work coordinate.

### Use Cases

**Temporary origin shift:**
```gcode
G54                (Work offset 1)
G00 X50 Y50        (Move to secondary feature)
G92 X0 Y0          (Treat this position as new origin)
(... machine operations relative to X50 Y50 ...)
G92.1              (Clear G92 shift, restore original G54)
```

**Legacy machines:**
- Some older controls use G92 instead of G54-G59
- Common on hobbyist/entry-level machines

### G92 vs. G54

| Feature | G54-G59 | G92 |
|---------|---------|-----|
| **Storage** | Permanent (in offset table) | Temporary (cleared at reset) |
| **Multiple offsets** | Yes (6+) | No (single shift) |
| **Recommended** | Yes (modern practice) | No (legacy only) |

**Best practice:** Avoid G92 if G54-G59 are available.

### G92.1, G92.2, G92.3

- **G92.1**: Cancel G92 offset, restore to G54-G59
- **G92.2**: Suspend G92 offset temporarily
- **G92.3**: Restore suspended G92 offset

## Practical Examples

### Example 1: Multi-Part Fixture

```gcode
(Program machines 3 identical parts in different vise locations)

O1000              (Main program)
G54 M98 P1100      (Part 1 in G54, call subprogram)
G55 M98 P1100      (Part 2 in G55, call subprogram)
G56 M98 P1100      (Part 3 in G56, call subprogram)
M30                (End main)

O1100              (Subprogram - part operations)
G00 X0 Y0 Z5.0     (Rapid to origin)
G01 Z-5.0 F100     (Plunge)
(... machining operations ...)
G00 Z5.0           (Retract)
M99                (Return to main)
```

### Example 2: Tool Change with Offsets

```gcode
(--- TOOL 1: 12MM END MILL ---)
T01 M06
G43 H01            (Tool length offset 1)
S2000 M03
G54                (Part 1 work offset)
G00 X0 Y0 Z5.0
(... machining ...)

(--- TOOL 2: 6MM DRILL ---)
M05
G00 Z50.0
T02 M06
G43 H02            (Tool length offset 2 - automatically adjusts Z)
S3000 M03
(Tool tip remains at same work Z position despite length difference)
G00 X10 Y10 Z5.0
(... drilling ...)
```

### Example 3: Cutter Compensation Profile

```gcode
(12mm end mill, radius 6mm)
G21 G90 G17
G54
T01 M06
G43 H01
S2000 M03

(Approach and lead-in)
G00 X-10 Y12.5 Z5.0
G01 Z-5.0 F100

(Enable compensation, machine outside profile)
G41 D01 G01 X0 Y12.5 F500    (Lead-in to part edge)
G01 X50.0                     (Bottom edge)
G01 Y25.0                     (Right edge)
G01 X0                        (Top edge)
G01 Y12.5                     (Left edge, close)
G40 G01 X-10.0                (Cancel compensation, lead-out)

G00 Z50.0
M05
M30
```

## Key Takeaways

1. **Machine coordinates** are absolute reference; **work offsets** enable part-relative programming
2. **G54-G59** provide six standard work coordinate systems for multiple setups
3. **G90** (absolute) is standard; **G91** (incremental) for special cases
4. **Tool length compensation** (G43) allows part-referenced Z programming
5. **Cutter radius compensation** (G41/G42) offsets path for tool diameter
6. **Transformation hierarchy**: Program → Work Offset → Tool Length → Machine
7. **G53** bypasses offsets for direct machine coordinate access
8. **Proper initialization** of offsets and tool compensation is critical for safe operation

***

**Next**: [Section 15.5 – Auxiliary Functions](section-15.5-auxiliary-functions.md)

**Previous**: [Section 15.3 – Motion Commands](section-15.3-motion-commands.md)
