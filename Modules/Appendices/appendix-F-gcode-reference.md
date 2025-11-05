# Appendix F: G-Code Quick Reference

---

## F.1 Motion Commands (G00-G03)

### F.1.1 Positioning Modes

| Code | Name | Description | Feedrate | Applications |
|------|------|-------------|----------|--------------|
| **G00** | Rapid Positioning | Move at maximum traverse rate to position | Ignored | Non-cutting moves, tool changes |
| **G01** | Linear Interpolation | Move in straight line at programmed feed | F word | Cutting, milling, all machining ops |
| **G02** | Circular Interpolation CW | Arc clockwise at programmed feed | F word | Arcs, radii, circular pockets |
| **G03** | Circular Interpolation CCW | Arc counter-clockwise at programmed feed | F word | Arcs, radii, circular pockets |

**Format Examples:**

```gcode
G00 X100 Y50 Z10        ; Rapid move to X100, Y50, Z10
G01 X200 Y100 F500      ; Linear move at 500 mm/min
G02 X50 Y50 I25 J0 F300 ; CW arc, center offset I25, J0
G03 X100 Y100 R25 F300  ; CCW arc, radius 25mm
```

### F.1.2 Arc Programming (G02/G03)

**Center Format (I, J, K):**
- I = X-axis offset from start point to arc center
- J = Y-axis offset from start point to arc center
- K = Z-axis offset (for helical interpolation)

**Radius Format (R):**
- R = arc radius
- R positive = arc ≤180° (short arc)
- R negative = arc >180° (long arc)

**Example: Quarter-circle arc from (0,0) to (50,50), center at (50,0):**

```gcode
G90                     ; Absolute positioning
G00 X0 Y0               ; Rapid to start point
G01 Z-5 F200            ; Plunge to depth
G03 X50 Y50 I50 J0 F500 ; CCW arc (I=50, J=0 offset)
; OR
G03 X50 Y50 R50 F500    ; Same arc using radius
```

**Full Circle Programming:**

```gcode
G91                     ; Incremental mode
G02 X0 Y0 I25 J0 F500   ; Full circle (returns to start, I=radius)
G90                     ; Back to absolute mode
```

---

## F.2 Coordinate System Commands (G17-G59.3)

### F.2.1 Plane Selection

| Code | Plane | Arc Axes | Normal Axis | Applications |
|------|-------|----------|-------------|--------------|
| **G17** | XY | X, Y | Z | Standard milling (default) |
| **G18** | XZ | X, Z | Y | Lathe operations, side facing |
| **G19** | YZ | Y, Z | X | Vertical milling, rotary axis |

**Example:**
```gcode
G17             ; Select XY plane (arcs in XY, Z perpendicular)
G02 X10 Y10 R5  ; Arc in XY plane
```

### F.2.2 Work Coordinate Systems

**Coordinate System Offsets (WCS):**

| Code | System | Typical Use |
|------|--------|-------------|
| **G54** | Work Offset 1 | Primary workpiece/fixture (default) |
| **G55** | Work Offset 2 | Second fixture or part |
| **G56** | Work Offset 3 | Third fixture |
| **G57** | Work Offset 4 | Fourth fixture |
| **G58** | Work Offset 5 | Fifth fixture |
| **G59** | Work Offset 6 | Sixth fixture |
| **G59.1** | Work Offset 7 | Extended offset 1 |
| **G59.2** | Work Offset 8 | Extended offset 2 |
| **G59.3** | Work Offset 9 | Extended offset 3 |

**Setting Work Offsets (Manual):**
```gcode
G10 L2 P1 X0 Y0 Z0      ; Set G54 origin to current position
G10 L2 P2 X100 Y0 Z0    ; Set G55 origin 100mm offset in X
```

**Using Work Offsets:**
```gcode
G54                     ; Activate work offset 1 (fixture A)
G00 X0 Y0 Z10           ; Rapid to fixture A origin + 10mm Z
G01 Z-5 F200            ; Plunge relative to G54 origin
; ... machining operations ...
G55                     ; Switch to work offset 2 (fixture B)
G00 X0 Y0 Z10           ; Rapid to fixture B origin
```

### F.2.3 Distance Mode

| Code | Mode | Description | Example |
|------|------|-------------|---------|
| **G90** | Absolute | Coordinates relative to WCS origin | G01 X100 Y50 (move to X100, Y50 in WCS) |
| **G91** | Incremental | Coordinates relative to current position | G01 X10 Y5 (move +10 in X, +5 in Y from current) |

**Common Use:**
```gcode
G90 G54         ; Absolute mode, work offset 1
G00 X50 Y50     ; Rapid to X50, Y50 (absolute)
G91             ; Switch to incremental
G01 X10 F500    ; Move +10mm in X (relative)
G90             ; Back to absolute
```

---

## F.3 Feed Rate and Spindle Commands (F, S, M03-M05)

### F.3.1 Feed Rate Modes

| Code | Mode | Units | Description |
|------|------|-------|-------------|
| **G93** | Inverse Time | 1/min | Feed rate = 1 / (time to complete move in minutes) |
| **G94** | Units/Minute | mm/min or in/min | Standard feed rate mode (default) |
| **G95** | Units/Revolution | mm/rev or in/rev | Feed per spindle revolution (threading, constant chip load) |

**F Word (Feed Rate):**
- **G94 mode:** F500 = 500 mm/min
- **G95 mode:** F0.1 = 0.1 mm/rev

**Example (G94 - Units per Minute):**
```gcode
G94                 ; Units/minute mode
G01 X100 F1000      ; Move to X100 at 1000 mm/min
```

**Example (G95 - Units per Revolution):**
```gcode
M03 S2000           ; Start spindle at 2000 RPM
G95                 ; Units/revolution mode
G01 X50 F0.15       ; Move to X50 at 0.15 mm/rev
                    ; Actual feed = 2000 RPM × 0.15 mm/rev = 300 mm/min
```

### F.3.2 Spindle Control

| Code | Function | Parameter | Description |
|------|----------|-----------|-------------|
| **S** | Spindle Speed | RPM | S1000 = 1000 RPM |
| **M03** | Spindle CW | - | Start spindle clockwise (normal) |
| **M04** | Spindle CCW | - | Start spindle counter-clockwise (tapping, reverse) |
| **M05** | Spindle Stop | - | Stop spindle |

**Example:**
```gcode
M03 S3000       ; Start spindle at 3000 RPM clockwise
G04 P2.0        ; Dwell 2 seconds (spindle ramp-up)
G01 Z-10 F500   ; Plunge to depth
; ... machining ...
M05             ; Stop spindle
```

---

## F.4 Tool and Coolant Commands (M06, M07-M09)

### F.4.1 Tool Change

| Code | Function | Description |
|------|----------|-------------|
| **T** | Tool Select | T1 = select tool #1 (not activated) |
| **M06** | Tool Change | Execute tool change (load selected tool) |

**Manual Tool Change Sequence:**
```gcode
T2              ; Select tool 2 (e.g., 6mm endmill)
M06             ; Execute tool change (machine stops, prompts operator)
G43 H2 Z10      ; Apply tool length offset for tool 2, move to Z10
M03 S4000       ; Start spindle
; ... machining with tool 2 ...
```

**Automatic Tool Changer (ATC):**
```gcode
T1 M06          ; Select and load tool 1 automatically
G43 H1          ; Apply tool offset
```

### F.4.2 Tool Length Offset

| Code | Function | Description |
|------|----------|-------------|
| **G43** | Tool Length Offset + | Apply positive tool length offset (H word) |
| **G44** | Tool Length Offset - | Apply negative offset (rarely used) |
| **G49** | Cancel Tool Offset | Remove tool length compensation |

**Example:**
```gcode
G43 H5 Z100     ; Apply offset for tool 5, move Z to 100mm (compensated)
G49             ; Cancel offset (return to machine coordinates)
```

### F.4.3 Coolant Control

| Code | Function | Description |
|------|----------|-------------|
| **M07** | Mist Coolant On | Activate mist coolant (fine spray) |
| **M08** | Flood Coolant On | Activate flood coolant (high flow) |
| **M09** | Coolant Off | Stop all coolant |

**Example:**
```gcode
M08             ; Flood coolant on
G01 X100 F800   ; Cutting move with coolant
M09             ; Coolant off (end of program)
```

---

## F.5 Canned Cycles (G80-G89)

### F.5.1 Drilling Cycles

| Code | Cycle | Description | Parameters |
|------|-------|-------------|------------|
| **G80** | Cancel | Cancel canned cycle | - |
| **G81** | Drill | Rapid to R, feed to Z, rapid out | R, Z, F |
| **G82** | Spot Drill | Drill + dwell at bottom | R, Z, P (dwell), F |
| **G83** | Peck Drill | Drill with pecking (chip clearing) | R, Z, Q (peck depth), F |
| **G85** | Bore | Feed in, feed out (finish bore) | R, Z, F |
| **G73** | High-Speed Peck | Partial retract between pecks | R, Z, Q, F |

**Parameters:**
- **R:** Retract plane (safe height above workpiece)
- **Z:** Hole depth (final depth)
- **Q:** Peck increment (G83, G73)
- **P:** Dwell time in seconds (G82, G89)
- **F:** Feed rate

**Example: Drilling 10 holes with G81**

```gcode
G90 G54             ; Absolute mode, work offset 1
G00 X0 Y0           ; Rapid to first hole location
G81 R5 Z-20 F200    ; Define drill cycle: R=5mm retract, Z=-20mm depth
X10                 ; Drill hole 2 at X10 (Y unchanged)
X20                 ; Drill hole 3 at X20
X30 Y10             ; Drill hole 4 at X30, Y10
; ... additional holes ...
G80                 ; Cancel drill cycle
```

**Example: Deep Hole Peck Drilling (G83)**

```gcode
G83 R5 Z-50 Q5 F150 ; Peck drill: R=5mm safe, Z=-50mm depth, Q=5mm peck increment
X0 Y0               ; Hole 1
X25 Y0              ; Hole 2
G80                 ; Cancel
```

### F.5.2 Canned Cycle Behavior

**Sequence (G81 example):**
1. Rapid (G00) in XY to hole location
2. Rapid (G00) in Z to R plane (retract height)
3. Feed (G01) to Z depth at F feedrate
4. Rapid (G00) back to R plane

**Modal Behavior:** Canned cycle remains active until G80 or another motion mode (G00, G01, G02, G03) is called.

---

## F.6 Dwell and Program Control (G04, M00-M02)

### F.6.1 Dwell Command

| Code | Function | Parameter | Description |
|------|----------|-----------|-------------|
| **G04** | Dwell | P (seconds) | Pause program for specified time |

**Examples:**
```gcode
G04 P2.5        ; Dwell for 2.5 seconds
G04 P0.5        ; Dwell for 0.5 seconds (spindle stabilization)
```

**Common Uses:**
- Spindle ramp-up after M03
- Chip clearing pause
- Finish pass dwell (dimensional stability)

### F.6.2 Program Stop Commands

| Code | Function | Description | Resume |
|------|----------|-------------|--------|
| **M00** | Program Stop | Unconditional stop, spindle/coolant off | Operator presses cycle start |
| **M01** | Optional Stop | Stop only if optional stop switch enabled | Cycle start |
| **M02** | Program End | End program, reset to start | Restart program |
| **M30** | Program End & Reset | End + rewind, return to start position | Restart program |

**Example: Mid-Program Tool Check**
```gcode
G01 X50 Y50 F800
M00             ; Stop for inspection (operator checks part)
; (Operator presses cycle start to continue)
G01 X100 Y100
```

---

## F.7 Parametric Programming and Macros

### F.7.1 Variables

**Persistent Variables (Linuxcnc #-parameters):**
- `#1` - `#30`: Temporary variables (cleared on program end)
- `#100` - `#999`: Persistent variables (saved between programs)
- `#5220`: X-axis work offset (G54)
- `#5221`: Y-axis work offset (G54)

**Example:**
```gcode
#1 = 100                ; Store 100 in variable #1
#2 = 50                 ; Store 50 in variable #2
G01 X[#1] Y[#2] F500    ; Move to X100, Y50 (use variables)
```

### F.7.2 Expressions and Operators

**Supported Operators:**
- Arithmetic: `+`, `-`, `*`, `/`, `MOD` (modulus)
- Comparison: `EQ`, `NE`, `LT`, `LE`, `GT`, `GE`
- Logical: `AND`, `OR`, `XOR`
- Functions: `SIN`, `COS`, `TAN`, `SQRT`, `ABS`, `ATAN`

**Example: Bolt Circle Pattern**
```gcode
; Drill 8 holes on 50mm diameter bolt circle
#1 = 0                  ; Hole counter
o100 while [#1 LT 8]
  #2 = [#1 * 360 / 8]   ; Angle for this hole
  #3 = [25 * COS[#2]]   ; X position (radius 25mm)
  #4 = [25 * SIN[#2]]   ; Y position
  G81 X[#3] Y[#4] R2 Z-10 F200
  #1 = [#1 + 1]         ; Increment counter
o100 endwhile
G80                     ; Cancel drill cycle
```

### F.7.3 Conditional Branching

**IF-THEN-ELSE:**
```gcode
#1 = 5
o100 if [#1 GT 10]
  G01 X100 F500         ; Execute if #1 > 10
o100 else
  G01 X50 F500          ; Execute if #1 ≤ 10
o100 endif
```

**Subroutines:**
```gcode
o200 sub                ; Define subroutine o200
  G01 X[#1] Y[#2] F500
  G02 X[#3] Y[#4] R10
o200 endsub

; Call subroutine with parameters
o200 call [10] [20] [30] [40]  ; #1=10, #2=20, #3=30, #4=40
```

---

## F.8 Common G-Code Program Structure

### F.8.1 Program Template

```gcode
%                               ; Program start delimiter (optional)
O1000                           ; Program number
(Generic Milling Program)       ; Comment
G21                             ; Metric units (G20 for inch)
G90                             ; Absolute positioning
G17                             ; XY plane selection
G40 G49 G80                     ; Cancel: cutter comp, tool offset, canned cycle

T1 M06                          ; Load tool 1
G43 H1 Z50                      ; Tool length offset, safe Z height
G54                             ; Work coordinate system 1
M03 S4000                       ; Spindle on, 4000 RPM
G04 P2.0                        ; Dwell 2 seconds (spindle ramp)
M08                             ; Coolant on

; Machining operations
G00 X10 Y10                     ; Rapid to position
G01 Z-5 F200                    ; Plunge to depth
X50 Y50 F800                    ; Cut to X50, Y50
G02 X70 Y50 I10 J0 F800         ; Arc
G01 Z5 F500                     ; Retract

M09                             ; Coolant off
M05                             ; Spindle off
G00 Z50                         ; Retract to safe Z
G53 G00 Z0                      ; Move to machine home Z (G53 = machine coords)
M30                             ; Program end and rewind
%                               ; Program end delimiter (optional)
```

### F.8.2 Safety Lines (Program Start)

**Standard Safety Block:**
```gcode
G21                     ; Metric mode (or G20 for inch)
G90                     ; Absolute distance mode
G17                     ; XY plane
G40                     ; Cancel cutter radius compensation
G49                     ; Cancel tool length offset
G80                     ; Cancel canned cycles
G54                     ; Select work coordinate system
G94                     ; Feed per minute mode
```

**Explanation:** Ensures machine is in known state (important after E-stop or program interruption).

---

## F.9 Common Modal G-Codes Summary

**Modal Groups (only one code active per group):**

| Group | Codes | Function |
|-------|-------|----------|
| **1 (Motion)** | G00, G01, G02, G03, G80-G89 | Motion type (rapid, linear, arc, canned cycle) |
| **2 (Plane)** | G17, G18, G19 | Plane selection (XY, XZ, YZ) |
| **3 (Distance)** | G90, G91 | Absolute vs. incremental positioning |
| **5 (Feed Mode)** | G93, G94, G95 | Feed rate mode (inverse time, per min, per rev) |
| **6 (Units)** | G20, G21 | Inch vs. metric units |
| **7 (Cutter Comp)** | G40, G41, G42 | Cutter radius compensation |
| **8 (Tool Offset)** | G43, G44, G49 | Tool length offset |
| **10 (Return Mode)** | G98, G99 | Canned cycle return (initial level, R-point) |
| **12 (Work Offset)** | G54-G59.3 | Work coordinate system selection |

**Non-Modal Commands (execute once, don't persist):**
- G04 (dwell)
- G10 (coordinate system setting)
- G28, G30 (return to home)
- G92 (coordinate system offset - use with caution)

---

**End of G-Code Quick Reference Appendix**
