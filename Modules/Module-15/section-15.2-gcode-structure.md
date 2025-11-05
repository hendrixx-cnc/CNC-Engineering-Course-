# Section 15.2 – G-Code Structure and Syntax

## Overview

G-code programs are composed of sequential blocks of ASCII text, each specifying machine actions through address codes and numerical parameters. Understanding the fundamental structure of G-code blocks, the meaning of address letters, and the distinction between modal and non-modal commands is essential for reading, writing, and debugging CNC programs.

This section provides a comprehensive examination of G-code syntax, block organization, command types, and formatting conventions used across modern CNC control systems.

## Block Structure

### Anatomy of a G-Code Block

A G-code block is a single line of code terminated by a line feed (LF) or carriage return/line feed (CR/LF). Each block contains one or more words that specify machine operations.

**Basic block format:**
```
N100 G01 X10.5 Y20.3 Z-5.0 F500 S2000 M03
```

**Block components:**

| Component | Example | Description |
|-----------|---------|-------------|
| **Line number** | N100 | Optional sequence identifier |
| **Preparatory function** | G01 | Motion or mode command |
| **Coordinate data** | X10.5 Y20.3 Z-5.0 | Axis endpoint positions |
| **Feed rate** | F500 | Cutting speed (units/min) |
| **Spindle speed** | S2000 | Rotation speed (RPM) |
| **Miscellaneous function** | M03 | Auxiliary command (spindle on CW) |

### Word Format

A **word** consists of an address letter followed by a numerical value:

```
Letter + Number = Word
    G  +  01    = G01
    X  +  10.5  = X10.5
    F  +  500   = F500
```

**Word syntax rules:**

1. **Address letter**: Single uppercase character (A-Z)
2. **Numerical value**: Integer or decimal, signed or unsigned
3. **No spaces**: Between letter and number (most controls)
4. **Leading zeros**: Optional in most dialects (G01 = G1)
5. **Trailing zeros**: Required for precision (X10.0 not X10.)
6. **Sign convention**: + assumed if not specified, - must be explicit

### Block Execution Order

Words within a block are not executed left-to-right. The controller processes them in a fixed sequence regardless of their order in the block:

**Standard execution order:**

1. **Comments** – Processed/ignored first
2. **N (Sequence number)** – Stored for reference
3. **G (Preparatory)** – Sets motion mode
4. **X, Y, Z, A, B, C** – Axis coordinates
5. **F (Feed rate)** – Sets feed for this and subsequent moves
6. **S (Spindle speed)** – Sets RPM for this and subsequent operations
7. **T (Tool)** – Selects tool (prepared for change)
8. **M (Miscellaneous)** – Auxiliary functions last

**Example demonstrating order independence:**
```gcode
X10 G01 Y20 F100 Z5    (Same result as...)
G01 X10 Y20 Z5 F100    (... written in logical order)
```

Both blocks produce identical motion: linear interpolation to X10 Y20 Z5 at 100 units/min feed rate.

## Address Codes

### Standard Address Letters

ISO 6983 defines specific meanings for each letter address:

| Letter | Function | Example | Units/Range |
|--------|----------|---------|-------------|
| **A** | Rotary axis (around X) | A45.0 | Degrees |
| **B** | Rotary axis (around Y) | B90.0 | Degrees |
| **C** | Rotary axis (around Z) | C180.0 | Degrees |
| **D** | Tool radius offset number | D01 | Index |
| **E** | Reserved (not standardized) | - | Varies |
| **F** | Feed rate | F500 | mm/min or in/min |
| **G** | Preparatory function | G01 | Code number |
| **H** | Tool length offset number | H03 | Index |
| **I** | Arc center X offset | I5.0 | Distance |
| **J** | Arc center Y offset | J-3.0 | Distance |
| **K** | Arc center Z offset | K2.0 | Distance |
| **L** | Loop count (subprograms) | L10 | Iterations |
| **M** | Miscellaneous function | M08 | Code number |
| **N** | Sequence number | N100 | Index |
| **O** | Program number | O1234 | Index |
| **P** | Dwell time / parameter | P500 | Milliseconds |
| **Q** | Peck increment (drilling) | Q2.0 | Distance |
| **R** | Arc radius / retract plane | R5.0 or R10.0 | Distance |
| **S** | Spindle speed | S2000 | RPM |
| **T** | Tool selection | T05 | Tool number |
| **U** | Secondary X-axis (parallel) | U10.0 | Distance |
| **V** | Secondary Y-axis (parallel) | V5.0 | Distance |
| **W** | Secondary Z-axis (parallel) | W-2.0 | Distance |
| **X** | Primary X-axis | X100.0 | Distance |
| **Y** | Primary Y-axis | Y50.0 | Distance |
| **Z** | Primary Z-axis | Z-10.0 | Distance |

### Extended Addressing

Some controls use additional conventions:

- **# variables**: #100 = 5.5 (parametric programming)
- **E-axis**: Extruder position (3D printing)
- **Expressions**: #1 = [#2 + #3 * COS[45]]

## Modal and Non-Modal Commands

### Modal Commands (Sticky)

**Modal commands** remain active until explicitly changed by another command in the same group. They define the machine's current state.

**Example of modal behavior:**
```gcode
G01 F100        (Linear mode active, feed = 100)
X10 Y10         (Still G01 at F100)
X20 Y20         (Still G01 at F100)
G00             (Now rapid mode active)
X30 Y30         (Rapid move, no feed rate)
```

Once G01 is specified, all subsequent coordinate moves use linear interpolation until a different motion mode (G00, G02, etc.) is commanded.

### Non-Modal Commands (Single Block)

**Non-modal commands** execute only in the block where they appear and do not affect subsequent blocks.

**Examples of non-modal commands:**
- **G04** (Dwell) – Pause for specified time in current block only
- **G28** (Return to home) – Execute homing in current block only
- **G92** (Set work coordinate) – Set offset in current block only

**Example:**
```gcode
G04 P1000       (Dwell 1 second, then continue)
X10 Y10         (Move continues in previous modal state)
```

### Modal Groups

Commands are organized into modal groups. Only one command from each group can be active at a time.

**Common modal groups:**

| Group | Function | Commands |
|-------|----------|----------|
| **Motion** | Move type | G00, G01, G02, G03, G04, G80-G89 |
| **Plane selection** | Arc plane | G17 (XY), G18 (XZ), G19 (YZ) |
| **Distance mode** | Coordinate type | G90 (absolute), G91 (incremental) |
| **Units** | Measurement system | G20 (inches), G21 (millimeters) |
| **Cutter compensation** | Tool radius | G40 (off), G41 (left), G42 (right) |
| **Tool length** | Z offset | G43 (on), G49 (off) |
| **Coordinate system** | Work offset | G54, G55, G56, G57, G58, G59 |
| **Path control** | Trajectory mode | G61 (exact stop), G64 (continuous) |
| **Return mode** | Canned cycle return | G98 (initial Z), G99 (R-plane) |

**Group conflict example (ERROR):**
```gcode
G01 G00 X10 Y10    (INVALID: Both G01 and G00 in motion group)
```

The controller will reject this block or execute only the last command (G00).

### Active Modal State

The controller maintains the active state of each modal group. This state persists:
- Through program execution
- After cycle stops (on most controls)
- Across program restarts (unless reset)

**Best practice**: Always initialize modal states at program start to ensure predictable behavior.

## Program Structure

### Typical Program Layout

A complete G-code program follows this general structure:

```gcode
%                          (Program start flag - optional)
O1234                      (Program number)
(PART: SAMPLE BRACKET)     (Comment: part identification)
(MATERIAL: 6061-T6 AL)     (Comment: material specification)
(SETUP: VISE JAW 1)        (Comment: fixturing information)

(--- INITIALIZATION ---)
G21 G90 G17               (Metric, absolute, XY plane)
G54                       (Work coordinate system 1)
G49                       (Cancel tool length offset)
G40                       (Cancel cutter radius compensation)

(--- TOOL 1: 12MM END MILL ---)
T01 M06                   (Select and change to tool 1)
G43 H01                   (Apply tool length offset 1)
S2000 M03                 (Spindle 2000 RPM clockwise)
G00 X0 Y0                 (Rapid to start position)
G00 Z5.0                  (Rapid to safe Z)
M08                       (Coolant on)

(--- MACHINING OPERATIONS ---)
G01 Z-5.0 F100            (Plunge into material)
G01 X50.0 Y0 F500         (Cut to endpoint)
G01 Z5.0 F100             (Retract)

(--- CLEANUP ---)
G00 Z50.0                 (Rapid to safe Z)
M09                       (Coolant off)
M05                       (Spindle off)
G28 G91 Z0                (Home Z-axis)
G28 X0 Y0                 (Home XY axes)
G90                       (Restore absolute mode)
M30                       (Program end, rewind)
%                          (Program end flag - optional)
```

### Header Block

The program header establishes context and initial conditions:

```gcode
O1234 (PROGRAM NUMBER AND NAME)
(PROGRAMMER: SMITH, J.)
(DATE: 2025-01-15)
(PART: BRK-100-REV-C)
(MATERIAL: 6061-T6 ALUMINUM)
(STOCK: 6.25 X 4.25 X 1.00)
(ORIGIN: CENTER-CENTER-TOP)
```

### Safety Block

The safety/initialization block sets known modal states:

```gcode
G21                    (Metric units)
G90                    (Absolute positioning)
G17                    (XY plane selection)
G40                    (Cutter compensation off)
G49                    (Tool length offset off)
G80                    (Cancel canned cycles)
G54                    (Work offset 1)
G94                    (Feed per minute mode)
```

### Tool Change Block

Tool changes follow a standard sequence:

```gcode
(--- TOOL 2: 6MM DRILL ---)
M05                    (Stop spindle)
M09                    (Coolant off)
G00 Z50.0              (Retract to safe Z)
T02 M06                (Change to tool 2)
G43 H02                (Tool length offset 2)
S3000 M03              (Spindle 3000 RPM)
M08                    (Coolant on)
```

### Program Termination

Programs end with cleanup and termination codes:

```gcode
M05                    (Spindle off)
M09                    (Coolant off)
G28 G91 Z0             (Home Z)
G28 X0 Y0              (Home XY)
G90                    (Restore absolute)
M30                    (Program end and rewind)
```

## Syntax Conventions

### Line Numbers (N-words)

Line numbers provide reference points for program editing and troubleshooting:

```gcode
N10 G21 G90 G54
N20 T01 M06
N30 G43 H01
N40 S2000 M03
```

**Conventions:**
- Increment by 5 or 10 to allow insertions
- Not required for execution (controller ignores)
- Useful for editing, debugging, restart points
- Some CAM systems omit to reduce file size

### Comments

Comments document program intent and are ignored during execution:

**Parenthesis comments:**
```gcode
G01 X10 Y20 (MOVE TO POSITION 1)
```

**Semicolon comments (LinuxCNC, some controls):**
```gcode
G01 X10 Y20 ; Move to position 1
```

**Best practices:**
- Explain operations, not obvious syntax
- Document tool descriptions, cutting parameters
- Note critical setup requirements
- Include revision history for program changes

### Case Sensitivity

Most CNC controls are **case-insensitive**:

```gcode
G01 X10 Y20    (Same as...)
g01 x10 y20    (... lowercase)
```

**Convention**: Use uppercase for consistency and readability.

### Whitespace

**Spaces between words** (modern controls):
```gcode
G01 X10 Y20 F100    (Readable format)
```

**No spaces** (legacy/compact format):
```gcode
G01X10Y20F100       (Compact format)
```

Most modern controls accept either format, but spaced format is preferred for human readability.

## Decimal and Precision

### Decimal Point Format

Always use decimal points for fractional values:

```gcode
X10.5    (Correct: 10.5 units)
X10,5    (WRONG: Comma not recognized)
X10.     (WRONG: Trailing decimal ambiguous)
```

### Leading Zeros

Leading zeros are optional on most controls:

```gcode
G01    (Same as...)
G1     (... no leading zero)

X005.0    (Same as...)
X5.0      (... no leading zeros)
```

**Convention**: Use leading zeros for consistency (G01, G00, M03).

### Trailing Zeros and Precision

Specify precision appropriate to machine capability:

```gcode
X10.0       (0.1 resolution - standard milling)
X10.00      (0.01 resolution - precision work)
X10.000     (0.001 resolution - grinding, EDM)
X10.0000    (0.0001 resolution - ultra-precision)
```

**Best practice**: Match resolution to machine capability and part tolerance.

## Special Characters

### Program Delimiters

- **%** – Program start/end marker (DNC/RS-232 transmission)
- **EOB** – End of block (line feed character, invisible)

### Reserved Characters

Characters with special meaning:

| Character | Function |
|-----------|----------|
| ( )       | Comment delimiters |
| %         | Program boundary |
| ;         | Comment (some controls) |
| #         | Variable prefix |
| [ ]       | Expression delimiters |
| /         | Block skip (optional execution) |

### Block Skip

The **/** character at the start of a block makes it conditionally executable:

```gcode
/G01 X10 Y20    (Executed only if block skip switch is OFF)
```

Used for:
- Optional roughing passes
- Debug output
- Conditional probing operations

## Error Prevention

### Common Syntax Errors

**Missing feed rate:**
```gcode
G01 X10 Y10    (ERROR: Feed rate not defined)
```

**Solution**: Always specify F-word before or with first G01:
```gcode
G01 X10 Y10 F500    (Correct)
```

**Ambiguous arc parameters:**
```gcode
G02 X10 Y10    (ERROR: Missing I, J, or R)
```

**Solution**: Specify arc center or radius:
```gcode
G02 X10 Y10 I5 J0    (Correct: center offset)
G02 X10 Y10 R5       (Correct: radius)
```

**Modal group conflicts:**
```gcode
G01 G00 X10    (ERROR: Both linear and rapid)
```

**Solution**: Use one motion command:
```gcode
G01 X10    (Correct)
```

### Syntax Validation

Before running a program:

1. **Use a syntax checker** – CAM software, LinuxCNC verify mode
2. **Simulation** – Visualize toolpath for unexpected moves
3. **Dry run** – Execute with feed override at 0% or in simulation mode
4. **Single block mode** – Step through line-by-line for new programs

## Key Takeaways

1. **G-code blocks** consist of words (letter + number) executed in a defined order
2. **Address letters** (G, M, X, Y, Z, F, S, etc.) specify different machine functions
3. **Modal commands** remain active until changed; **non-modal** execute once
4. **Modal groups** organize commands; only one per group can be active
5. **Program structure** includes initialization, tool changes, operations, and cleanup
6. **Comments** document intent; **line numbers** aid debugging
7. **Syntax rules** include decimal format, precision, and special character usage
8. **Error prevention** requires understanding modal state and parameter requirements

***

**Next**: [Section 15.3 – Motion Commands](section-15.3-motion-commands.md)

**Previous**: [Section 15.1 – Introduction](section-15.1-introduction.md)
