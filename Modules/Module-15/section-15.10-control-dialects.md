# Section 15.10 – Control System Dialects

## Overview

While ISO 6983 provides a baseline G-code standard, major CNC control manufacturers have developed distinct dialects with unique syntax, features, and conventions. Understanding these differences is essential for adapting programs across machines, configuring post-processors, and troubleshooting control-specific behavior.

This section compares major control systems—FANUC, Siemens, Heidenhain, Haas, Mazak, and LinuxCNC—highlighting syntax differences, unique features, and practical adaptation strategies.

## ISO 6983 Baseline Standard

### Common Ground Across All Controls

All major control systems share these fundamental concepts:

**Core motion commands:**
- G00 (rapid), G01 (linear feed), G02/G03 (circular interpolation)
- X, Y, Z axis designations
- F (feed rate), S (spindle speed)

**Basic structure:**
- Block-based execution (one line at a time)
- Modal vs. non-modal commands
- Coordinate systems (absolute/incremental)

**Tool management:**
- T-word for tool selection
- M06 for tool change (most controls)

**Program control:**
- M-codes for spindle, coolant, program flow

### Where Dialects Diverge

**Syntax variations:**
- Leading zeros (G01 vs. G1)
- Decimal places
- Comment delimiters
- Line numbering formats

**Feature availability:**
- Canned cycles (different cycle numbers)
- Macro/variable syntax
- Subprogram calls
- Tool compensation methods

**Machine-specific M-codes:**
- Manufacturer-specific auxiliary functions
- Proprietary features

## FANUC Control Dialect

### Overview

FANUC is the most widely used CNC control globally, forming the de facto standard for industrial CNC programming.

**Market presence:**
- ~50% global market share
- Standard on Haas, Doosan, Okuma, DMG Mori, many others
- Most CAM post-processors default to FANUC syntax

### Syntax Characteristics

**Leading zeros:**
```gcode
G01        (Preferred, but G1 also accepted)
M03        (Preferred, but M3 also accepted)
```

**Decimal format:**
```gcode
X10.5      (Decimal point required)
X10.0      (Trailing zero recommended)
```

**Comments:**
```gcode
(COMMENT IN PARENTHESES)
```

**Program structure:**
```gcode
%
O1234
(PROGRAM NAME)
G21 G90 G17
G54
...
M30
%
```

### FANUC-Specific Features

**Subprogram calls:**
```gcode
M98 P8500      (Call local subprogram O8500)
M98 P8500 L5   (Call O8500, repeat 5 times)
M99            (Return from subprogram)
```

**Custom M-codes (common on FANUC machines):**
```gcode
M19            (Spindle orientation)
M41-M44        (Gear range selection)
M60            (Pallet change)
```

**Macro variables:**
```gcode
#1 = 10.5      (Variable assignment)
#100 = #5021   (Read system variable)
```

**FANUC Macro B (parametric programming):**
```gcode
IF [#1 GT 10] THEN #2 = 20
WHILE [#1 LT 100] DO 1
  #1 = #1 + 1
END 1
```

### FANUC Variants

**FANUC 0i/16i/18i/21i:**
- Standard FANUC dialect
- Most common in modern machines

**FANUC 30i/31i/32i:**
- Enhanced features
- Faster processing
- More memory

**FANUC Custom Macro:**
- Variable support (#1-#999)
- Conditional logic
- Loops and arithmetic

## Siemens Control Dialect

### Overview

Siemens (Sinumerik) controls are prevalent in European machines and high-end machining centers.

**Market presence:**
- Strong in Europe (Germany, Switzerland, Italy)
- Common on DMG Mori, Chiron, Hermle, Starrag

### Syntax Characteristics

**No leading zeros:**
```gcode
G1        (Not G01)
M3        (Not M03)
```

**Decimal format:**
```gcode
X10.5     (Same as FANUC)
```

**Comments:**
```gcode
; COMMENT WITH SEMICOLON
```

**Program structure:**
```gcode
; PROGRAM NAME
G54
G17 G90 G94
...
M2        (M2 more common than M30)
```

### Siemens-Specific Features

**Subprogram calls:**
```gcode
CALL "SUBPROG.SPF"     (Call external subprogram by name)
M17                     (Return from subprogram)
```

**R parameters (variables):**
```gcode
R1 = 10.5               (Variable assignment)
R2 = R1 + 5             (Arithmetic)
X = R1 Y = R2           (Use in motion)
```

**Conditional logic:**
```gcode
IF R1 > 10
  R2 = 20
ENDIF
```

**Loops:**
```gcode
REPEAT P1
  G1 X = X + 10
ENDLABEL P1
```

**Siemens Cycles:**
```gcode
CYCLE81(10, 0, 2, -20)  (Drilling cycle with parameters)
MCALL CYCLE81           (Activate cycle)
X10 Y10                 (Drill at position)
MCALL                   (Cancel cycle)
```

### Siemens 840D/828D Specifics

**ShopMill/ShopTurn:**
- High-level conversational programming
- Generates G-code internally

**Synchronized actions:**
```gcode
SYNFCT                  (Synchronized function)
```

**Transformations:**
```gcode
TRANS X10 Y20           (Translation)
ROT RPL = 45            (Rotation)
```

## Heidenhain Control Dialect

### Overview

Heidenhain (TNC) controls emphasize conversational programming with clear, English-like syntax.

**Market presence:**
- Common in Europe, especially Germany
- High-end machine tools
- Popular in tool and die shops

### Syntax Characteristics

**Conversational format:**
```gcode
0 BEGIN PGM PART1 MM    (Program start, metric units)
1 TOOL CALL 5 Z S3000   (Tool 5, spindle 3000 RPM)
2 L X+10 Y+20 R0 F500 M (Linear move to X10 Y20)
3 CC X+50 Y+50          (Circle center at X50 Y50)
4 C X+60 Y+50 DR+ R10 F300 M (Circular move)
...
99 END PGM PART1        (Program end)
```

**Characteristics:**
- Line numbers at start of each block
- Explicit commands (L for linear, C for circular)
- DR+ / DR- for CW/CCW direction
- R0/R/RF for approach behavior

### Heidenhain-Specific Features

**Cycle definitions:**
```gcode
CYCL DEF 200 DRILLING   (Define drilling cycle)
  Q200=2                (Safety clearance)
  Q201=-20              (Depth)
  Q206=250              (Feed rate)
CYCL CALL               (Activate cycle)
L X+10 Y+10 M99         (Drill at position)
```

**Subprograms:**
```gcode
CALL LBL 1              (Call label 1)
...
LBL 1                   (Label definition)
...
LBL 0                   (End of subprogram)
```

**FK Free Contour Programming:**
- Describes part geometry directly
- Controller calculates toolpath

**Q parameters (variables):**
```gcode
FN1: Q1 = 10.5          (Assign to Q parameter)
FN2: Q2 = Q1 + 5        (Arithmetic)
L X+Q1 Y+Q2             (Use in motion)
```

### Heidenhain vs. ISO Mode

Heidenhain controls support **ISO mode** for compatibility:

```gcode
BEGIN PGM ISO_MODE MM
G01 X10 Y20 F500        (Standard ISO syntax)
...
END PGM ISO_MODE
```

Most programmers use Heidenhain's native conversational format for clarity.

## Haas Control Dialect

### Overview

Haas uses FANUC-based controls with manufacturer-specific customizations.

**Market presence:**
- Largest CNC machine builder in North America
- Common in job shops, schools
- FANUC-compatible with Haas extensions

### Syntax Characteristics

**Generally FANUC-compatible:**
```gcode
G01 X10 Y20 F500        (Standard FANUC syntax)
M03 S2000               (Spindle on)
```

**Haas-specific M-codes:**
```gcode
M12                     (Thru-spindle coolant on)
M13                     (Spindle on CW + coolant)
M26                     (Water blast on)
M95                     (Sleep mode - waiting)
M96                     (Jump if no input)
M109                    (Z-axis brake on)
```

### Haas-Specific Features

**Macro programming:**
```gcode
#1 = 10.0               (FANUC-style variables)
IF [#1 GT 5] GOTO 100   (Conditional jump)
```

**Visual Quick Code (VQC):**
- Haas conversational programming
- Generates G-code for common operations
- Similar to FANUC Manual Guide

**Advanced geometry options:**
```gcode
G187                    (Smooth acceleration)
G05.1 Q1                (AI contour control)
```

**Wireless probing (some models):**
```gcode
G65 P9832               (Probing macro call)
```

## Mazak Control Dialect

### Overview

Mazak machines use proprietary Mazatrol conversational programming or ISO G-code.

**Market presence:**
- Major Japanese manufacturer
- Multi-tasking and turn-mill specialists
- Conversational programming focus

### Mazatrol Conversational

**Unit-based programming:**
```
UNIT 1: FACE
  Z-START: 0
  Z-END: -5
  FEED: 0.2
END UNIT
```

**Advantages:**
- No G-code knowledge required
- Graphical programming
- Fast for simple parts

**Disadvantages:**
- Not portable to other machines
- Limited for complex geometry

### Mazak ISO Mode

Mazak controls also support ISO G-code (EIA/ISO mode):

```gcode
O0001
G54 G90 G00 X0 Y0
M03 S2000
G01 Z-5.0 F200
...
M30
```

**Syntax similar to FANUC** with Mazak-specific M-codes:
```gcode
M60                     (Pallet change)
M205                    (Tailstock advance)
M78                     (Sub-spindle interlock on)
```

## LinuxCNC Dialect

### Overview

LinuxCNC is an open-source CNC control running on PC hardware with real-time Linux kernel.

**Market presence:**
- Open-source community
- Hobbyists, researchers, custom machines
- Highly customizable

### Syntax Characteristics

**Generally FANUC-compatible:**
```gcode
G01 X10 Y20 F500        (Standard syntax)
```

**Comment styles:**
```gcode
(PARENTHESIS COMMENT)
; SEMICOLON COMMENT
# HASH COMMENT (some versions)
```

**Case insensitive:**
```gcode
G01 X10 Y20             (Same as...)
g01 x10 y20
```

### LinuxCNC-Specific Features

**O-word programming (structured):**
```gcode
O100 IF [#1 GT 10]
  (statements)
O100 ELSE
  (statements)
O100 ENDIF

O200 WHILE [#1 LT 100]
  #1 = [#1 + 1]
O200 ENDWHILE

O300 DO [#1 = 1, 10, 1]
  (loop body)
O300 ENDDO
```

**Subprograms:**
```gcode
O100 CALL               (Call O100 subprogram)
O100 SUB                (Subprogram start)
  ...
O100 ENDSUB             (Subprogram end)
```

**Digital I/O control:**
```gcode
M64 P0                  (Set digital output 0)
M65 P0                  (Clear digital output 0)
M66 P0 L1               (Wait for digital input 0)
```

**HAL integration:**
- Custom M-codes via shell scripts
- Direct hardware access
- Real-time pin control

**Named parameters:**
```gcode
#<diameter> = 10.0
#<radius> = [#<diameter> / 2]
G01 X#<radius> F500
```

### LinuxCNC Advantages

**Flexibility:**
- Custom kinematics
- Custom M-codes
- Tool change scripts
- Probing routines

**Cost:**
- Free and open-source
- Runs on standard PC hardware

## Control Dialect Comparison Table

| Feature | FANUC | Siemens | Heidenhain | Haas | LinuxCNC |
|---------|-------|---------|------------|------|----------|
| **Leading zeros** | G01 | G1 | N/A | G01 | G01 or G1 |
| **Comment style** | ( ) | ; | ( ) ; | ( ) | ( ) ; |
| **Subprogram call** | M98 P__ | CALL | CALL LBL | M98 P__ | O__ CALL |
| **Variable prefix** | # | R | Q | # | # |
| **Conditional** | IF-THEN | IF-ENDIF | IF-ENDIF | IF-GOTO | O__ IF |
| **Loop** | WHILE-DO | REPEAT | REPEAT | WHILE | O__ WHILE/DO |
| **Program end** | M30 | M2 | END PGM | M30 | M30 or M2 |
| **Arc format** | I/J/K or R | I/J/K | CC + DR | I/J/K or R | I/J/K or R |
| **Conversational** | Manual Guide | ShopMill | TNC Dialog | VQC | None (external) |

## Adapting Programs Between Controls

### FANUC to Siemens

**Changes required:**
```gcode
(FANUC)                 (SIEMENS)
G01 → G1
M03 → M3
M98 P5000 → CALL "O5000.SPF"
#1 = 10 → R1 = 10
(COMMENT) → ; COMMENT
M30 → M2
```

### FANUC to Heidenhain

**Significant rewrite required:**
```gcode
(FANUC)                 (HEIDENHAIN)
O1234 → 0 BEGIN PGM PART1 MM
G01 X10 Y20 F500 → 1 L X+10 Y+20 R0 F500 M
G02 X20 Y20 I5 J0 → CC X+15 Y+20
                    C X+20 Y+20 DR+ R5 F500 M
M30 → END PGM PART1
```

### Universal G-Code Practices

**For maximum portability:**

1. **Stick to ISO 6983 basics:**
   - G00, G01, G02, G03
   - Standard work offsets (G54-G59)
   - Common M-codes (M03, M05, M08, M09, M30)

2. **Avoid control-specific features:**
   - Custom cycles
   - Proprietary macro syntax
   - Manufacturer M-codes

3. **Document dialect:**
   - Note which control the program was written for
   - Include conversion notes

4. **Use post-processors:**
   - Let CAM software handle dialect differences
   - Configure post for target control

## Key Takeaways

1. **ISO 6983** provides baseline standard; **dialects** add manufacturer-specific features
2. **FANUC** is the most common dialect, forming the de facto standard
3. **Siemens** uses no leading zeros, semicolon comments, R parameters
4. **Heidenhain** uses conversational format with English-like commands
5. **Haas** is FANUC-compatible with custom M-codes
6. **LinuxCNC** is open-source, highly customizable, FANUC-like syntax
7. **Adaptation** between controls requires syntax translation and feature mapping
8. **Post-processors** handle dialect differences automatically in CAM workflows
9. **Portability** maximized by sticking to ISO 6983 basics
10. **Understanding dialects** essential for multi-machine shops and troubleshooting

***

**Next**: [Section 15.11 – Simulation and Verification](section-15.11-simulation-verification.md)

**Previous**: [Section 15.9 – Advanced Features](section-15.9-advanced-features.md)
