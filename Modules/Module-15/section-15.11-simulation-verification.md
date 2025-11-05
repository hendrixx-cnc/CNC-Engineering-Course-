# Section 15.11 – Simulation, Verification, and Program Validation

## Overview

Simulation and verification are critical safeguards that prevent costly crashes, tool breakage, and scrapped parts. Virtual machining validates G-code programs before they ever reach physical hardware, enabling detection of collisions, feed rate errors, missing tool offsets, and geometric mistakes in a safe software environment.

This section covers simulation strategies, verification tools, DNC communication, and systematic validation workflows for ensuring program correctness.

## Why Simulation is Essential

### Risks of Running Unverified Programs

**Without simulation:**
- Tool crashes into fixtures, clamps, or workpiece
- Rapid moves executed at cutting depth
- Missing feed rates cause stalls or runaway
- Wrong work offsets position tool incorrectly
- Tool length offsets not applied, causing table crashes
- Arc geometry errors create unexpected motion

**Consequences:**
- Broken tools ($50-$500+ per tool)
- Damaged spindle ($5,000-$50,000 repair)
- Scrapped parts ($100-$10,000+ material and labor)
- Machine downtime (hours to days)
- Safety hazards (flying debris, crashes)

### Benefits of Simulation

**Detect errors before machining:**
- Collision detection
- Toolpath verification
- Feed rate validation
- Work offset verification
- Tool length offset confirmation
- Cycle time estimation

**Optimize programs:**
- Identify inefficient rapids
- Find bottlenecks in cycle time
- Visualize tool engagement
- Confirm surface finish approach

**Training and communication:**
- Show operators expected toolpath
- Document setup requirements
- Verify part geometry match

## Types of Simulation

### 1. Toolpath Verification (2D/3D Visualization)

**What it does:**
- Displays programmed toolpath as 3D lines
- Shows rapid moves vs. feed moves
- Visualizes arcs and helical paths
- No material removal simulation

**Tools:**
- CAMotics (free, open-source)
- NC Viewer (web-based, free)
- G-Wizard Editor
- CAM software built-in viewers

**Example - CAMotics:**
```bash
camotics program.nc    # Load and visualize G-code
```

**Advantages:**
- Fast (no material calculation)
- Easy to spot missing feed rates, wrong positions
- Good for quick verification

**Limitations:**
- Doesn't show material removal
- Won't detect tool/part collisions in 3D space
- Can't verify surface finish quality

### 2. Material Removal Simulation

**What it does:**
- Simulates actual cutting process
- Removes material from virtual stock
- Shows remaining material, gouges, excess
- Calculates final part geometry

**Tools:**
- CAM software (Fusion 360, Mastercam, HSMWorks)
- Standalone simulators (NCSimul, VERICUT, CimcoEdit)
- Machine control built-in simulation

**Example - Fusion 360 simulation:**
1. Setup → Simulate
2. Select stock model
3. Run simulation, observe material removal
4. Check for collisions, excess material, gouges

**Advantages:**
- Realistic visualization of cutting process
- Detects over-cutting (gouges) and under-cutting (excess material)
- Verifies clearances between tool and part
- Provides accurate cycle time estimation

**Limitations:**
- Slower than toolpath-only verification
- Requires accurate stock and fixture models

### 3. Machine Simulation (Kinematic)

**What it does:**
- Simulates entire machine including spindle, table, fixtures
- Detects collisions between tool holder, spindle head, and fixtures
- Accounts for machine kinematics (especially 4/5-axis)
- Validates work envelope limits

**Tools:**
- VERICUT (industry standard)
- NCSimul Machine
- CAM software with machine models
- Control-built-in simulation (Siemens, Heidenhain)

**Example - VERICUT:**
- Import machine model (geometry, kinematics, limits)
- Load G-code program
- Run full simulation with collision detection
- Review collision report, analyze near-misses

**Advantages:**
- Most comprehensive verification
- Essential for complex multi-axis machines
- Detects fixture/clamp collisions
- Validates rotary axis limits and coordination

**Limitations:**
- Expensive software ($10,000+)
- Requires accurate machine model
- Slower simulation time

## Simulation Workflow

### Step 1: Quick Toolpath Check

**Before running detailed simulation:**

```gcode
(Load program in NC Viewer or CAMotics)
1. Verify program loads without syntax errors
2. Check toolpath appears reasonable
3. Confirm rapids and feeds are distinct
4. Verify arcs are smooth (no radius errors)
5. Check Z-height clearances
```

**Look for obvious errors:**
- Tool starting inside part (work offset wrong)
- Rapids at Z=0 (Z-clearance missing)
- Single straight line instead of expected contour (feed rate zero)
- Unexpected jumps (wrong work offset or coordinate mode)

### Step 2: Material Removal Simulation

**In CAM software or standalone simulator:**

1. **Define stock:**
   - Material dimensions
   - Stock origin relative to part
   - Material type (optional, for force simulation)

2. **Load fixtures (if available):**
   - Vise model
   - Clamps, parallels
   - Workholding

3. **Run simulation:**
   - Play forward at real-time or fast-forward
   - Pause at tool changes
   - Inspect part at critical features

4. **Check for errors:**
   - **Gouges**: Tool cuts into finished surface (red regions)
   - **Excess material**: Part features not fully cut (blue regions)
   - **Collisions**: Tool/holder hits fixture or part
   - **Out-of-tolerance**: Part geometry exceeds tolerance bands

### Step 3: Control-Based Verification

**On the machine control (if available):**

```gcode
(Most modern controls have built-in graphics)
1. Load program into control
2. Select "Graphics" or "Verify" mode
3. Run program in simulation (spindle/axes don't move)
4. Watch toolpath trace on screen
5. Verify against part print
```

**Advantages:**
- Uses actual machine kinematics
- Accounts for control-specific G-code interpretation
- Tests program compatibility with control dialect

**Limitations:**
- Basic visualization (typically 2D or simple 3D)
- No material removal or collision detection

### Step 4: Dry Run on Machine

**After simulation, before cutting:**

```gcode
(Dry run procedure)
1. Load all tools, measure and set offsets
2. Set work offsets (touch-off on stock or fixture)
3. Load program
4. Enable "Dry Run" or "Single Block" mode
5. Set feed override to 0% or 10%
6. Run program with Z-axis 25-50mm above actual work surface
   (Either raise Z-offset or position stock lower)
7. Watch for unexpected motion, verify tool changes work
```

**Critical checks during dry run:**
- Tool approaches correct XY positions
- Rapids clear all fixtures and clamps
- Tool changes execute properly
- Feed moves occur where expected (not rapids)
- Program completes without alarms

### Step 5: First Article Inspection

**First part with new program:**

1. **Reduced speed:** Run at 50% feed override
2. **Single block:** Step through critical sections
3. **Stop and measure:** Check dimensions after roughing, before finishing
4. **Full inspection:** Measure all dimensions, check surface finish
5. **Document issues:** Note any required offsets, program edits

## Simulation Tools and Software

### Free and Open-Source

**CAMotics:**
- Platform: Windows, Mac, Linux
- Features: 3D toolpath, material removal, STL export
- Best for: General G-code verification, hobbyists
- Download: https://camotics.org

**NC Viewer:**
- Platform: Web browser
- Features: 3D toolpath visualization, no installation
- Best for: Quick checks, sharing with others
- URL: https://ncviewer.com

**LinuxCNC Axis GUI:**
- Platform: Linux (LinuxCNC)
- Features: Real-time preview, backplot, DRO
- Best for: LinuxCNC users, real machine control

### Commercial CAM Software (Includes Simulation)

**Fusion 360 ($495/year or free for hobbyists):**
- Integrated CAM and simulation
- Material removal, tool library
- Cloud-based, cross-platform

**Mastercam ($5,000-$15,000+):**
- Industry-standard CAM
- Advanced simulation and verification
- Backplot, solid verify, toolpath analysis

**HSMWorks (SolidWorks add-in, $5,000+):**
- Integrated with SolidWorks CAD
- Stock simulation, collision detection

### Professional Verification Software

**VERICUT ($10,000-$50,000+):**
- Industry-leading machine simulation
- Full kinematic validation
- Collision detection, optimization
- Used in aerospace, automotive

**NCSimul Machine ($8,000-$20,000):**
- Machine-centric simulation
- Virtual machine commissioning
- Post-processor validation

**CimcoEdit ($500-$1,500):**
- G-code editor with backplot
- 2D/3D verification
- DNC communication

## DNC Communication and File Transfer

### Direct Numerical Control (DNC)

DNC enables communication between computers and CNC machines:

**RS-232 serial (legacy):**
```bash
Baud rate: 9600, 19200 (machine-dependent)
Data bits: 7 or 8
Parity: Even, Odd, or None
Stop bits: 1 or 2
Flow control: XON/XOFF or hardware
```

**Ethernet (modern):**
- FTP, SFTP, or manufacturer protocol
- Faster, more reliable
- Supports large file transfers

**USB (some controls):**
- Direct USB drive insertion
- USB cable to control

### Drip-Feed Programs

**For programs larger than control memory:**

```gcode
(DNC software sends program line-by-line as machine executes)
1. Connect computer to machine via serial/Ethernet
2. Load program in DNC software
3. Start drip-feed mode
4. Machine requests blocks as needed
5. Computer sends next block when requested
```

**DNC software:**
- Predator DNC
- CIMCO DNC-Max
- OpenDNC
- Machine vendor software (Haas DNC, etc.)

### File Transfer Best Practices

**1. Verify file integrity:**
```bash
(After transfer, compare file sizes)
Original: 12,345 bytes
Transferred: 12,345 bytes ✓

(Check first and last lines of program)
Original: % ... M30 %
Transferred: % ... M30 % ✓
```

**2. Use correct line endings:**
- Windows: CR+LF (\r\n)
- Linux/Mac: LF (\n)
- Most CNC controls accept either

**3. Character encoding:**
- ASCII only (no Unicode, special characters)
- Avoid extended characters in comments

**4. File naming:**
- No spaces (use underscores or hyphens)
- Short names (8.3 format for older controls)
- Example: PART_001.NC, BRK100-OPN10.NC

## Program Validation Checklist

**Before running any new program:**

- [ ] Program simulated in CAMotics/NC Viewer
- [ ] Material removal simulation completed (if available)
- [ ] No collisions detected with fixtures/clamps
- [ ] All tool numbers present in tool library
- [ ] Tool lengths measured and offsets set
- [ ] Work offsets set and verified (touch-off)
- [ ] Feed rates appropriate for material and tools
- [ ] Spindle speeds within tool and machine limits
- [ ] Rapids clear all obstacles by safe margin
- [ ] Dry run completed with Z-axis raised
- [ ] First article inspection planned
- [ ] Safety equipment in place (guards, e-stop accessible)

## Common Simulation Findings

### Feed Rate Errors

**Missing F-word:**
```gcode
G01 X10 Y10        (No feed rate - machine stalls)
```

**Simulation shows:** Tool freezes at start of move, alarm condition.

**Fix:**
```gcode
G01 X10 Y10 F500
```

### Work Offset Errors

**Wrong offset selected:**
```gcode
G55                (Should be G54)
G00 X0 Y0          (Tool goes to wrong position)
```

**Simulation shows:** Tool approaches unexpected location, possible collision.

**Fix:**
```gcode
G54                (Correct work offset)
G00 X0 Y0
```

### Tool Length Not Applied

**Missing G43:**
```gcode
T01 M06
(G43 H01 MISSING)
G00 Z0             (Tool plunges into table)
```

**Simulation shows:** Tool crashes into stock or table.

**Fix:**
```gcode
T01 M06
G43 H01            (Apply tool length offset)
G00 Z0
```

### Clearance Errors

**Rapids at cutting depth:**
```gcode
G01 Z-10 F100      (Cut to depth)
G00 X100 Y50       (Rapid at Z-10, still in part)
```

**Simulation shows:** Tool drags through part during rapid.

**Fix:**
```gcode
G01 Z-10 F100
G00 Z5.0           (Retract first)
G00 X100 Y50       (Safe rapid)
```

## Advanced Verification Techniques

### Chip Load Validation

Calculate and verify chip loads match tooling recommendations:

$$\text{Chip Load} = \frac{F}{S \times N \times Z}$$

Where:
- F = Feed rate (mm/min)
- S = Spindle speed (RPM)
- N = Number of teeth
- Z = Number of flutes

**Example:**
```gcode
S2000 M03          (2000 RPM)
G01 X100 F800      (800 mm/min)
(Tool: 4-flute end mill)

Chip load = 800 / (2000 × 1 × 4) = 0.1 mm/tooth ✓
```

### Cutting Force Simulation

Advanced simulators estimate cutting forces:
- Detect overload conditions
- Predict tool deflection
- Optimize feeds and speeds
- Identify chatter risk

**Software:** VERICUT Force, HSMWorks Force Module

### Cycle Time Analysis

**Breakdown by operation:**
```
Total cycle time: 12:35
  Rapids: 1:20 (10.5%)
  Roughing: 7:45 (61.7%)
  Finishing: 2:15 (17.9%)
  Tool changes: 1:15 (9.9%)
```

**Optimization targets:**
- Reduce air cutting (rapids)
- Increase feed rates where safe
- Combine operations to reduce tool changes

## Key Takeaways

1. **Never run unverified programs** on physical machines
2. **Three-stage verification**: Toolpath check → Material removal → Dry run
3. **Free tools** (CAMotics, NC Viewer) sufficient for basic verification
4. **Commercial simulators** (VERICUT) essential for complex/high-value work
5. **Dry run procedures** catch setup and offset errors before cutting
6. **DNC communication** enables large file transfer and drip-feeding
7. **Common errors** detected: Missing feed rates, wrong offsets, clearance issues
8. **First article inspection** validates program produces correct part
9. **Simulation workflow** is systematic: Quick check → Detailed sim → Dry run → First part
10. **Professional shops** use multi-stage verification for all new programs

***

**Next**: [Section 15.12 – Conclusion](section-15.12-conclusion.md)

**Previous**: [Section 15.10 – Control System Dialects](section-15.10-control-dialects.md)
