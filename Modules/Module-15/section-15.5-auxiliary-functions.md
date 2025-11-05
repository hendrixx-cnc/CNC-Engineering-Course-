# Section 15.5 – Auxiliary Functions (M-Codes)

## Overview

M-codes (Miscellaneous functions) control auxiliary machine functions beyond motion: spindle rotation, coolant activation, tool changes, program flow, and machine-specific operations. Unlike preparatory functions (G-codes) that primarily control motion, M-codes interact with peripheral systems.

This section covers standard M-codes, their syntax, modal behavior, and the sequence in which they execute relative to motion commands.

## M-Code Fundamentals

### Syntax

M-codes follow the same word format as G-codes:

```gcode
M03        (Letter M + numeric code)
M08        (Most M-codes are two digits)
M30        (Some controls support M100-M999 for custom macros)
```

### Execution Timing

M-codes execute at specific points in block processing:

**Type 1: Before motion**
- M-code executes, then motion begins
- Example: M03 (spindle on) starts before G01 move

**Type 2: After motion**
- Motion completes, then M-code executes
- Example: M00 (program stop) after move to position

**Type 3: Immediate**
- M-code executes instantly, independent of motion
- Example: M30 (program end) terminates immediately

### Modal vs. Non-Modal

Most M-codes are **non-modal** (execute once):
```gcode
M03            (Spindle on, stays on until turned off)
```

Some M-codes are **modal** and remain active:
```gcode
M08            (Coolant on, stays on)
M09            (Coolant off)
```

### Multiple M-Codes Per Block

ISO 6983 limits blocks to **one M-code** per line. Some modern controls allow multiple if they don't conflict:

**Standard (safe):**
```gcode
M03            (Spindle on)
M08            (Coolant on - separate block)
```

**Some controls allow:**
```gcode
M03 M08        (Spindle and coolant on - check manual)
```

**Best practice:** One M-code per block for maximum compatibility.

## Spindle Control

### M03 – Spindle On Clockwise (CW)

Starts spindle rotation in the clockwise direction (viewed from spindle nose toward motor).

```gcode
S2000 M03      (Spindle on at 2000 RPM clockwise)
```

**Characteristics:**
- Requires S-word for spindle speed (RPM)
- Waits for spindle to reach speed (if control monitors RPM)
- Modal: remains on until M05 or M04

**Typical applications:**
- Milling (most operations)
- Drilling
- Right-hand thread cutting

### M04 – Spindle On Counterclockwise (CCW)

Starts spindle rotation counterclockwise:

```gcode
S2000 M04      (Spindle on at 2000 RPM counterclockwise)
```

**Typical applications:**
- Left-hand thread tapping
- Reverse facing operations (lathes)
- Spindle cleaning / chip evacuation

**Safety:** Verify tool rotation direction before use. Right-hand tools with M04 can self-loosen.

### M05 – Spindle Stop

Stops spindle rotation:

```gcode
M05            (Spindle off)
```

**Characteristics:**
- Non-modal (executes once)
- Controller may wait for spindle to reach zero RPM
- Always issue before tool change

**Standard sequence:**
```gcode
M05            (Stop spindle)
G04 P2.0       (Dwell 2 seconds for spindle to stop)
T02 M06        (Safe to change tool)
```

### S-Word – Spindle Speed

The S-word specifies spindle speed in RPM:

```gcode
S3000          (Set spindle speed to 3000 RPM)
M03            (Start spindle at 3000 RPM)
```

**Modal behavior:**
- S-word is modal (remains active)
- Can be changed during operation:

```gcode
S2000 M03      (Start at 2000 RPM)
G01 X50 F500   (Cutting move)
S2500          (Increase to 2500 RPM mid-cut)
```

**Speed limits:**
- Controlled by machine parameters
- Typical ranges: 100-8000 RPM (milling), 10-50,000 RPM (spindles)
- Controller enforces maximum speed limits

### M19 – Spindle Orientation

Orients spindle to a specific angular position:

```gcode
M19            (Orient spindle to 0° - control-specific)
M19 P90        (Orient to 90° on some controls)
```

**Applications:**
- Tool change orientation for automatic tool changers
- Angle head positioning
- Spindle probe mounting

## Coolant Control

### M08 – Coolant On

Activates flood coolant:

```gcode
M08            (Flood coolant on)
```

**Characteristics:**
- Modal: remains on until M09
- Usually activates primary coolant pump
- May activate multiple coolant nozzles

**Standard usage:**
```gcode
S2000 M03      (Spindle on)
M08            (Coolant on)
G01 Z-10 F100  (Begin cutting with coolant)
```

### M09 – Coolant Off

Deactivates coolant:

```gcode
M09            (Coolant off)
```

**Standard usage:**
```gcode
G00 Z50        (Retract to safe height)
M09            (Coolant off)
M05            (Spindle off)
```

### M07 – Mist Coolant On

Activates mist coolant (if equipped):

```gcode
M07            (Mist coolant on)
```

**Characteristics:**
- Used for air-oil mist or air blast
- Often for high-speed finishing
- Machine-dependent implementation

**Combined coolant:**
```gcode
M07 M08        (Both mist and flood - if control allows)
```

### M88/M89 – Through-Spindle Coolant (TSC)

Some machines support coolant through tool center:

```gcode
M88            (TSC on - control-specific)
M89            (TSC off - control-specific)
```

**Applications:**
- Deep hole drilling
- Gun drilling
- High-pressure peck drilling

**Pressure requirements:**
- Typically 300-1000 PSI (20-70 bar)
- Requires special tooling with coolant passages

## Tool Change

### M06 – Tool Change

Executes automatic tool change:

```gcode
T05 M06        (Change to tool 5)
```

**Sequence:**
1. Spindle stops (if not already stopped)
2. Z-axis retracts to tool change position
3. Tool changer swaps tools
4. Spindle returns to ready position

**Standard tool change block:**
```gcode
M05            (Stop spindle)
M09            (Coolant off)
G28 G91 Z0     (Retract Z to home)
T02 M06        (Change to tool 2)
G43 H02        (Apply new tool length offset)
S3000 M03      (Start spindle at new speed)
M08            (Coolant on)
```

### T-Word – Tool Selection

The T-word specifies tool number:

```gcode
T01            (Prepare tool 1 for change)
M06            (Execute tool change)
```

**Pre-selection (some controls):**
```gcode
T02            (Pre-select tool 2)
(... machining with tool 1 ...)
M06            (Change to pre-selected tool 2)
```

Pre-selection reduces tool change time on machines with tool magazines.

### M61 – Set Tool Number

Sets current tool number without physical change:

```gcode
M61 Q5         (Tell control tool 5 is in spindle)
```

**Use cases:**
- Manual tool changes
- Tool broke, replaced with same type
- Program restart after interruption

## Program Control

### M00 – Program Stop

Stops program execution and waits for operator input:

```gcode
G00 X50 Y50
M00            (Stop here, wait for cycle start)
G01 Z-10 F100  (Continues after operator presses start)
```

**Behavior:**
- Motion stops
- Spindle and coolant remain on (usually)
- Operator must press Cycle Start to continue
- Use for inspection, measurement, chip clearing

### M01 – Optional Program Stop

Conditional stop, active only if "Optional Stop" switch is enabled:

```gcode
G00 X50 Y50
M01            (Stop only if optional stop enabled)
G01 Z-10 F100
```

**Use cases:**
- Inspection points for first article
- Chip clearing for long programs
- Coolant check
- Can be disabled for production runs

### M02 – Program End

Ends program execution:

```gcode
M02            (Program end)
```

**Behavior:**
- Stops motion
- Does NOT stop spindle or coolant (machine-dependent)
- Does NOT rewind program
- Less common than M30

### M30 – Program End and Rewind

Ends program and resets to beginning:

```gcode
M30            (Program end and rewind)
```

**Behavior:**
- Stops motion
- Stops spindle (M05)
- Stops coolant (M09)
- Rewinds program to beginning
- Resets some modal states (machine-dependent)

**Standard program ending:**
```gcode
G00 Z50.0      (Retract)
M09            (Coolant off)
M05            (Spindle off)
G28 G91 Z0     (Home Z)
G28 X0 Y0      (Home XY)
G90            (Restore absolute mode)
M30            (End and rewind)
```

### M98 – Subprogram Call

Calls an external subprogram:

```gcode
M98 P1234      (Call program O1234)
M98 P1234 L5   (Call O1234, repeat 5 times)
```

**Syntax variations:**
- **P-word**: Subprogram number
- **L-word**: Repeat count (optional, default = 1)

**Subprogram structure:**
```gcode
O1234          (Subprogram number)
G01 X10 Y10 F500
G01 X20 Y20
M99            (Return to main program)
```

### M99 – Return from Subprogram

Returns control to calling program:

```gcode
M99            (Return from subprogram)
M99 P5000      (Jump to block N5000 in main program)
```

**Behavior:**
- Resumes at block following M98 call
- Can specify return address with P-word (control-dependent)

## Machine-Specific M-Codes

### Common Extensions

Many controls define custom M-codes beyond ISO 6983:

| M-Code | Function | Notes |
|--------|----------|-------|
| **M10** | Clamp engaged | 4th axis, pallet |
| **M11** | Clamp released | 4th axis, pallet |
| **M21-M28** | Mirror image on/off | Axis-specific |
| **M50-M59** | Custom coolant zones | Multi-nozzle |
| **M60** | Pallet change | Horizontal machining centers |
| **M70-M72** | Save/restore modal state | Program nesting |
| **M98-M99** | Subprogram call/return | Universal |
| **M100+** | Custom macros | User-defined |

### LinuxCNC Custom M-Codes

LinuxCNC supports custom M-codes via external scripts:

**Example M101 (custom coolant):**
```bash
#!/bin/bash
# File: M101
# Activate high-pressure coolant
echo "Activating high-pressure coolant"
hal setp coolant-hp.enable true
```

```gcode
M101           (Calls /usr/local/bin/M101 script)
```

### Probing M-Codes (G38.x alternative)

Some controls use M-codes for probing:

```gcode
M75            (Enable probe)
G38.2 Z-50 F50 (Probe toward Z-50)
M76            (Disable probe)
```

## Air and Chip Management

### M88/M89 – Air Blast

On some machines, M88/M89 control air blast:

```gcode
M88            (Air blast on)
M89            (Air blast off)
```

**Applications:**
- Chip clearing during drilling
- Part cleaning
- Dry machining assist

### M35/M36 – Chip Conveyor

Chip conveyor control (machine-dependent):

```gcode
M35            (Chip conveyor forward)
M36            (Chip conveyor reverse)
M37            (Chip conveyor stop)
```

## Execution Examples

### Example 1: Basic Spindle and Coolant

```gcode
G21 G90 G17 G54            (Initialize)
T01 M06                    (Tool 1)
G43 H01                    (Tool length offset)

S2000 M03                  (Spindle on 2000 RPM clockwise)
G04 P2.0                   (Dwell 2 seconds for spindle to reach speed)
M08                        (Coolant on)

G00 X0 Y0 Z5.0             (Position)
G01 Z-10.0 F100            (Plunge with coolant)
G01 X50.0 F500             (Cut)

G00 Z50.0                  (Retract)
M09                        (Coolant off)
M05                        (Spindle off)
M30                        (End program)
```

### Example 2: Tool Change Sequence

```gcode
(--- TOOL 1: ROUGHING ---)
T01 M06
G43 H01
S2000 M03
M08
G00 X0 Y0 Z5.0
(...machining operations...)

(--- TOOL CHANGE TO TOOL 2 ---)
G00 Z50.0                  (Retract)
M09                        (Coolant off)
M05                        (Spindle stop)
G04 P3.0                   (Dwell for spindle stop)
T02 M06                    (Change to tool 2)

(--- TOOL 2: FINISHING ---)
G43 H02                    (New tool length)
S3000 M03                  (Higher speed for finishing)
M08                        (Coolant back on)
G00 X0 Y0 Z5.0
(...finishing operations...)

M09
M05
M30
```

### Example 3: Optional Stop for Inspection

```gcode
G21 G90 G17 G54
T01 M06
G43 H01
S2000 M03
M08

(Rough pass)
G00 X0 Y0 Z5.0
G01 Z-10.0 F100
G01 X50.0 F500

M01                        (Optional stop - inspect if switch enabled)

(Finish pass)
G01 Z-10.2 F100            (Deeper for finish)
G01 X50.0 F300             (Slower feed for finish)

G00 Z50.0
M09
M05
M30
```

### Example 4: Subprogram for Bolt Circle

```gcode
(Main program)
O1000
G21 G90 G17 G54
T01 M06
G43 H01
S3000 M03
M08

G00 X50.0 Y50.0 Z5.0       (Center of bolt circle)

M98 P2000 L4               (Call hole subprogram 4 times)

G00 Z50.0
M09
M05
M30

(Subprogram - drill one hole and rotate)
O2000
G81 X10.0 Y0 Z-10.0 R2.0 F100    (Drill hole at 0°)
G00 G91 A90.0                     (Rotate 90° incremental)
G90                               (Back to absolute)
M99                               (Return)
```

## M-Code Timing and Safety

### Dwell for Spindle Stabilization

Always allow spindle to reach commanded speed:

```gcode
S5000 M03                  (Start 5000 RPM spindle)
G04 P3.0                   (Wait 3 seconds)
G01 Z-10 F100              (Safe to begin cutting)
```

**Typical dwell times:**
- Low RPM (< 2000): 1-2 seconds
- Medium RPM (2000-5000): 2-3 seconds
- High RPM (> 5000): 3-5 seconds

### Coolant Before Spindle

To prevent dry start:

```gcode
M08                        (Coolant on first)
G04 P1.0                   (Brief delay)
S2000 M03                  (Spindle on with coolant flowing)
```

### Safe Tool Change

Standard safe sequence:

```gcode
G00 Z50.0                  (Retract to safe Z)
M09                        (Coolant off)
M05                        (Spindle off)
G04 P3.0                   (Wait for spindle stop)
G28 G91 Z0                 (Home Z-axis)
T02 M06                    (Now safe to change tool)
```

## Control-Specific Variations

### FANUC

```gcode
M03 S2000                  (S before or after M03)
M98 P8500                  (Subprogram call, local)
M198 P8500                 (Subprogram call, external)
```

### Siemens

```gcode
M3 S2000                   (No leading zero)
M17                        (End of subprogram)
M02                        (Program end, more common than M30)
```

### Heidenhain

```gcode
M3                         (No leading zero)
M6                         (Tool change)
M91                        (Activate subprogram)
```

### LinuxCNC

```gcode
M03 S2000                  (Standard)
M64 P0                     (Set digital output bit 0)
M65 P0                     (Clear digital output bit 0)
M66 P0 L1                  (Wait for digital input bit 0)
```

## Key Takeaways

1. **M-codes control auxiliary functions**: spindle, coolant, tool changes, program flow
2. **M03/M04** start spindle CW/CCW; **M05** stops spindle
3. **M08** coolant on; **M09** coolant off
4. **M06** tool change with T-word for tool selection
5. **M00** program stop; **M01** optional stop; **M30** end and rewind
6. **M98/M99** subprogram call and return
7. **Timing is critical**: dwell after spindle start, coolant before cutting
8. **One M-code per block** for maximum compatibility
9. **Machine-specific M-codes** extend functionality beyond ISO 6983 standard

***

**Next**: [Section 15.6 – Canned Cycles](section-15.6-canned-cycles.md)

**Previous**: [Section 15.4 – Coordinate Systems](section-15.4-coordinate-systems.md)
