# Section 15.9 – Advanced Features: Macros, Variables, and Parametric Programming

## Overview

Advanced G-code features—variables, expressions, conditional logic, loops, and subprograms—transform static programs into flexible, parametric systems. These capabilities enable adaptive machining, part families, automatic error recovery, and in-process measurement integration.

This section covers parametric programming techniques, macro variables, control flow, mathematical expressions, and practical applications for advanced CNC programming.

## Variables and Parameters

### System Variables (Read-Only)

System variables provide access to machine state and position:

| Variable | Description | Example Value |
|----------|-------------|---------------|
| **#5161-#5166** | G28 home position (X, Y, Z, A, B, C) | 0.0 |
| **#5181-#5186** | G30 secondary home (X, Y, Z, A, B, C) | 100.0 |
| **#5201-#5206** | G54 work offset (X, Y, Z, A, B, C) | -200.0 |
| **#5221-#5226** | G55 work offset | -180.5 |
| **#5241-#5326** | G56-G59 work offsets | varies |
| **#5401-#5406** | Current position (X, Y, Z, A, B, C) | 50.325 |
| **#5410** | Current tool number | 5 |
| **#5420-#5428** | Current tool offsets (H, D, etc.) | 150.325 |
| **#_feed** | Current feed rate | 500.0 |
| **#_rpm** | Current spindle speed | 2000 |

**Example - Reading current position:**
```gcode
#100 = #5421         (Store current X position in variable #100)
#101 = #5422         (Store current Y position)
#102 = #5423         (Store current Z position)
```

### User Variables (Read-Write)

User-defined variables store values for calculations and parametric operations:

**Local variables:** #1 through #33 (cleared at program end)
```gcode
#1 = 10.0            (Assign 10.0 to variable #1)
#2 = 20.5            (Assign 20.5 to variable #2)
#3 = [#1 + #2]       (Calculate: #3 = 30.5)
```

**Global variables:** #100 through #999 (persistent across programs)
```gcode
#100 = 5             (Remains in memory after M30)
#101 = [#100 * 2]    (Calculate: #101 = 10)
```

**Common variables:** #500 through #999 (shared between programs, persistent)
```gcode
#500 = 25            (Part count - persists across program runs)
```

### Variable Assignment

**Direct assignment:**
```gcode
#1 = 10.5            (Assign literal value)
#2 = #1              (Copy from another variable)
#3 = #5421           (Copy from system variable)
```

**Expression assignment:**
```gcode
#4 = [#1 + #2]       (Addition)
#5 = [#1 * #2]       (Multiplication)
#6 = [#2 - #1]       (Subtraction)
#7 = [#2 / #1]       (Division)
```

### Using Variables in Motion Commands

Variables can substitute for any numeric value:

```gcode
#1 = 50.0            (X target position)
#2 = 25.0            (Y target position)
#3 = -10.0           (Z depth)
#4 = 500.0           (Feed rate)

G01 X#1 Y#2 Z#3 F#4  (Move to variable positions)
```

**Result:**
```gcode
G01 X50.0 Y25.0 Z-10.0 F500.0
```

## Mathematical Expressions

### Arithmetic Operators

| Operator | Function | Example | Result |
|----------|----------|---------|--------|
| **+** | Addition | [10 + 5] | 15 |
| **-** | Subtraction | [10 - 5] | 5 |
| **\*** | Multiplication | [10 * 5] | 50 |
| **/** | Division | [10 / 5] | 2 |
| **MOD** | Modulo | [10 MOD 3] | 1 |

**Example:**
```gcode
#1 = [100 + 50]      (#1 = 150)
#2 = [#1 * 2]        (#2 = 300)
#3 = [#2 / 10]       (#3 = 30)
```

### Trigonometric Functions

| Function | Description | Example |
|----------|-------------|---------|
| **SIN[]** | Sine (degrees) | SIN[30] = 0.5 |
| **COS[]** | Cosine (degrees) | COS[60] = 0.5 |
| **TAN[]** | Tangent (degrees) | TAN[45] = 1.0 |
| **ASIN[]** | Arc sine | ASIN[0.5] = 30 |
| **ACOS[]** | Arc cosine | ACOS[0.5] = 60 |
| **ATAN[]** | Arc tangent (2-argument) | ATAN[1]/[1] = 45 |

**Example - Bolt circle calculations:**
```gcode
#1 = 100.0           (Bolt circle diameter)
#2 = 8               (Number of holes)
#3 = 360.0 / #2      (Angle between holes: 45°)

#10 = [#1/2] * COS[#3 * 1]    (X position, hole 1)
#11 = [#1/2] * SIN[#3 * 1]    (Y position, hole 1)

G81 X#10 Y#11 Z-20 R5 F100    (Drill hole 1)
```

### Other Mathematical Functions

| Function | Description | Example |
|----------|-------------|---------|
| **SQRT[]** | Square root | SQRT[25] = 5 |
| **ABS[]** | Absolute value | ABS[-10] = 10 |
| **ROUND[]** | Round to nearest integer | ROUND[10.6] = 11 |
| **FIX[]** | Truncate (round down) | FIX[10.9] = 10 |
| **FUP[]** | Round up | FUP[10.1] = 11 |
| **LN[]** | Natural logarithm | LN[2.718] = 1 |
| **EXP[]** | Exponential (e^x) | EXP[1] = 2.718 |

**Example - Calculate hypotenuse:**
```gcode
#1 = 30.0            (Side A)
#2 = 40.0            (Side B)
#3 = SQRT[[#1 * #1] + [#2 * #2]]    (#3 = 50.0)
```

## Conditional Logic

### IF-THEN-ELSE Statements

**Syntax (FANUC/LinuxCNC style):**
```gcode
O100 IF [condition]
  (statements if true)
O100 ELSE
  (statements if false)
O100 ENDIF
```

**Comparison operators:**
- **EQ**: Equal to
- **NE**: Not equal to
- **GT**: Greater than
- **GE**: Greater than or equal to
- **LT**: Less than
- **LE**: Less than or equal to

**Example 1: Simple condition**
```gcode
#1 = 10.0
#2 = 20.0

O100 IF [#1 LT #2]
  (MSG, #1 is less than #2)
  #3 = #1           (Use smaller value)
O100 ELSE
  #3 = #2
O100 ENDIF
```

**Example 2: Check for zero to avoid division error**
```gcode
#1 = 100.0
#2 = 0

O200 IF [#2 EQ 0]
  (ABORT, DIVISION BY ZERO ERROR)
O200 ELSE
  #3 = [#1 / #2]
O200 ENDIF
```

**Example 3: Adaptive depth based on tool diameter**
```gcode
#1 = 12.0            (Tool diameter)

O300 IF [#1 GT 10.0]
  #2 = 5.0           (Large tool: 5mm depth per pass)
O300 ELSE
  #2 = 2.0           (Small tool: 2mm depth per pass)
O300 ENDIF

G01 Z[0 - #2] F100   (Plunge to calculated depth)
```

### Nested Conditions

```gcode
#1 = 15.0            (Tool diameter)

O100 IF [#1 GT 20.0]
  #2 = 10.0          (Very large tool)
O100 ELSE
  O110 IF [#1 GT 10.0]
    #2 = 5.0         (Large tool)
  O110 ELSE
    #2 = 2.0         (Small tool)
  O110 ENDIF
O100 ENDIF
```

## Loops and Iteration

### WHILE Loop

**Syntax:**
```gcode
O100 WHILE [condition]
  (statements)
O100 ENDWHILE
```

**Example - Drill holes in a line:**
```gcode
#1 = 0               (Starting X position)
#2 = 100             (Ending X position)
#3 = 10              (Spacing between holes)

O100 WHILE [#1 LE #2]
  G81 X#1 Y0 Z-20 R5 F100    (Drill hole)
  #1 = [#1 + #3]             (Increment position)
O100 ENDWHILE

G80                  (Cancel cycle)
```

**Result:** Drills holes at X0, X10, X20, ... X100

### DO-WHILE Loop

**Syntax:**
```gcode
O100 DO [#var = start, end, increment]
  (statements)
O100 ENDDO
```

**Example - Pocket with multiple depth passes:**
```gcode
#1 = 0               (Start depth)
#2 = -15             (Final depth)
#3 = -3              (Depth increment)

O100 DO [#1 = #3, #2, #3]    (Loop from -3 to -15, step -3)
  G01 Z#1 F100               (Plunge to depth)
  (... pocket toolpath at this depth ...)
  G00 Z5.0                   (Retract)
O100 ENDDO
```

**Result:** Pockets at Z=-3, Z=-6, Z=-9, Z=-12, Z=-15

### FOR Loop Style (Alternative Syntax)

Some controls use different syntax:

```gcode
FOR #1 = 1 TO 10 STEP 1
  G81 X[#1 * 10] Y0 Z-20 R5 F100
ENDFOR
```

## Subprograms with Parameters

### Calling Subprograms with Arguments

**Main program:**
```gcode
O1000              (Main program)
G54
T01 M06
G43 H01
S2000 M03
M08

(Call subprogram with different parameters)
#1 = 10.0  #2 = 10.0  #3 = -5.0     (X, Y, Z for pocket 1)
M98 P2000                            (Call pocket subprogram)

#1 = 50.0  #2 = 50.0  #3 = -10.0    (X, Y, Z for pocket 2)
M98 P2000                            (Call pocket subprogram)

M09
M05
M30
```

**Subprogram (O2000 - parametric pocket):**
```gcode
O2000              (Pocket subprogram)
G00 X#1 Y#2        (Position to pocket center)
G00 Z5.0
G01 Z#3 F100       (Plunge to specified depth)
(... pocket cutting pattern ...)
G00 Z5.0           (Retract)
M99                (Return to main program)
```

### Subprogram with Local Variables

**Avoid conflicts by using local variables (#1-#33):**

```gcode
O3000              (Subprogram: drill bolt circle)
(Expects: #1=center X, #2=center Y, #3=diameter, #4=holes)

#10 = #1           (Store inputs in local variables)
#11 = #2
#12 = #3
#13 = #4
#14 = 360.0 / #13  (Calculate angle increment)

G00 X#10 Y#11      (Move to center)

O100 DO [#15 = 0, #13-1, 1]    (Loop through holes)
  #16 = [#12/2] * COS[#14 * #15]  (Calculate X offset)
  #17 = [#12/2] * SIN[#14 * #15]  (Calculate Y offset)
  G81 X[#10 + #16] Y[#11 + #17] Z-20 R5 F100
O100 ENDDO

G80
M99
```

## Practical Applications

### Application 1: Parametric Bolt Circle

```gcode
O1000              (Main program)
G21 G90 G17 G54
T01 M06
G43 H01
S2000 M03
M08

(Define bolt circle parameters)
#100 = 50.0        (Center X)
#101 = 50.0        (Center Y)
#102 = 80.0        (Bolt circle diameter)
#103 = 6           (Number of holes)
#104 = 0.0         (Starting angle)
#105 = -15.0       (Hole depth)

(Calculate angle increment)
#106 = 360.0 / #103

(Loop through holes)
O100 DO [#1 = 0, #103-1, 1]
  #110 = [#102/2] * COS[[#104 + #106 * #1]]    (X offset)
  #111 = [#102/2] * SIN[[#104 + #106 * #1]]    (Y offset)
  G81 X[#100 + #110] Y[#101 + #111] Z#105 R5.0 F100
O100 ENDDO

G80
M09
M05
M30
```

### Application 2: Adaptive Roughing Based on Material

```gcode
O2000              (Adaptive roughing)

(Material codes: 1=Aluminum, 2=Steel, 3=Stainless)
#100 = 1           (Select material)

(Set parameters based on material)
O100 IF [#100 EQ 1]
  #101 = 5.0       (Depth per pass)
  #102 = 800       (Feed rate)
  #103 = 3000      (Spindle speed)
O100 ELSE
  O110 IF [#100 EQ 2]
    #101 = 3.0
    #102 = 400
    #103 = 2000
  O110 ELSE
    #101 = 2.0
    #102 = 200
    #103 = 1500
  O110 ENDIF
O100 ENDIF

(Apply parameters)
S#103 M03
G04 P2.0

(Roughing with calculated depth)
O200 DO [#1 = [0 - #101], -15.0, [0 - #101]]
  G01 Z#1 F100
  (... cutting moves at F#102 ...)
O200 ENDDO

M05
M30
```

### Application 3: Part Count and Tool Life Tracking

```gcode
O3000              (Main program with tool life tracking)

(Global variables for tracking)
#500 = 0           (Part count - initialized once)
#501 = 0           (T01 usage count)
#502 = 500         (T01 tool life limit)

(Increment part count)
#500 = [#500 + 1]
(MSG, STARTING PART #500)

(Check tool life)
O100 IF [#501 GT #502]
  (ALARM, TOOL 1 HAS EXCEEDED LIFE LIMIT)
  M00            (Stop for tool replacement)
  #501 = 0       (Reset counter after replacement)
O100 ENDIF

T01 M06
G43 H01
S2000 M03

(... machining operations ...)

#501 = [#501 + 1]    (Increment tool usage)

M05
M30
```

### Application 4: In-Process Probing and Measurement

```gcode
O4000              (Probe and measure part thickness)

G54
T01 M06            (Touch probe)
G43 H01

(Probe top surface)
G30.1             (Store current position)
G38.2 Z-50 F50    (Probe down until contact)
#100 = #5063      (Store Z position of top surface)

(Probe bottom surface - assumes open bottom)
G00 Z5.0
G38.2 Z-100 F50   (Probe down to bottom)
#101 = #5063      (Store Z position of bottom)

(Calculate thickness)
#102 = [#100 - #101]

(Check tolerance)
O100 IF [ABS[#102 - 25.0] GT 0.5]    (Target 25mm ± 0.5mm)
  (ALARM, PART THICKNESS OUT OF SPEC: #102 MM)
  M00
O100 ENDIF

(MSG, PART THICKNESS OK: #102 MM)
M30
```

## Macro Programming Best Practices

### 1. Document Variable Usage

```gcode
(VARIABLE DEFINITIONS)
(#100 = Pocket center X)
(#101 = Pocket center Y)
(#102 = Pocket width)
(#103 = Pocket height)
(#104 = Pocket depth)
(#110-#119 = Temporary calculation variables)
```

### 2. Use Meaningful Variable Numbers

```gcode
(Poor practice)
#1 = 50
#2 = 25
#3 = #1 + #2

(Better practice - grouped by function)
#100 = 50        (Part dimensions #100-#109)
#101 = 25
#110 = #100 + #101    (Calculations #110-#119)
```

### 3. Initialize Variables

```gcode
(Initialize all variables at program start)
#1 = 0
#2 = 0
#3 = 0
```

### 4. Add Error Checking

```gcode
O100 IF [#1 EQ 0]
  (ABORT, PARAMETER #1 NOT SET)
O100 ENDIF

O200 IF [#2 LT 0]
  (ABORT, PARAMETER #2 MUST BE POSITIVE)
O200 ENDIF
```

### 5. Test with Simple Values First

Before complex calculations, test with known values:

```gcode
#1 = 10.0        (Simple test value)
#2 = 20.0
#3 = [#1 + #2]   (Should be 30.0)
(MSG, TEST RESULT: #3)    (Verify on screen)
M00
```

## Key Takeaways

1. **Variables** (#1-#999) store values for parametric programming
2. **System variables** (#5xxx, #_xxx) provide access to machine state and position
3. **Mathematical expressions** support arithmetic, trigonometry, and advanced functions
4. **Conditional logic** (IF-THEN-ELSE) enables adaptive programming
5. **Loops** (WHILE, DO) automate repetitive operations
6. **Subprograms with parameters** create reusable, flexible code modules
7. **Practical applications** include bolt circles, adaptive feeds, tool life tracking, probing
8. **Best practices**: Document variables, check for errors, test incrementally
9. **Parametric programming** enables part families and adaptive machining
10. **Advanced features** require thorough testing and simulation

***

**Next**: [Section 15.10 – Control System Dialects](section-15.10-control-dialects.md)

**Previous**: [Section 15.8 – Post-Processing](section-15.8-post-processing.md)
