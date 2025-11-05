# Appendix J: Troubleshooting Flowcharts and Diagnostics

---

## J.1 No Motion on Axis

```
START: Axis does not move when commanded
│
├─> Test 1: Does motor make any sound when commanded?
│   │
│   ├─> NO sound
│   │   ├─> Check controller LED (step pulses present?)
│   │   │   ├─> LED flashing → Problem: Cable/driver connection
│   │   │   │   └─> Solution: Check step/dir cable continuity, reseat connectors
│   │   │   └─> LED not flashing → Problem: Controller configuration
│   │   │       └─> Solution: Check steps/mm, enable signal, port assignment
│   │   │
│   │   └─> Check driver enable signal (is driver enabled?)
│   │       ├─> Disabled → Solution: Check enable wiring, E-stop circuit, software enable
│   │       └─> Enabled → Problem: Driver fault
│   │           └─> Solution: Check driver LEDs for fault code, reset driver
│   │
│   └─> YES sound (motor humming/vibrating)
│       ├─> Test 2: Is motor stalled (high current, hot)?
│       │   ├─> YES → Problem: Excessive load or mechanical binding
│       │   │   └─> Solution: Manually move axis (disconnect motor), check for binding,
│       │   │       reduce load, increase motor torque setting
│       │   └─> NO → Problem: Motor not receiving step pulses correctly
│       │       └─> Solution: Check step/dir polarity, microstepping setting,
│       │           driver current setting (too low)
│       │
│       └─> Test 3: Does motor shaft turn when commanded?
│           ├─> YES (shaft turns, no axis motion) → Problem: Mechanical disconnect
│           │   └─> Solution: Check coupling (set screws loose), ball screw connection
│           └─> NO (shaft locked) → Problem: Driver or motor fault
│               └─> Solution: Swap driver with known-good, test motor resistance
│                   (should be <5Ω per phase)
```

---

## J.2 Poor Surface Finish

```
START: Part surface finish is rough, chatter marks, or uneven
│
├─> Type of defect?
│   │
│   ├─> CHATTER (regular ripple pattern)
│   │   ├─> Is chatter frequency regular (harmonic)?
│   │   │   ├─> YES → Resonance problem
│   │   │   │   ├─> Check spindle RPM (adjust ±10% to move off resonance frequency)
│   │   │   │   ├─> Increase rigidity (tighten gibs, preload bearings)
│   │   │   │   └─> Reduce depth of cut or width of cut (lower cutting forces)
│   │   │   │
│   │   │   └─> NO → Random chatter
│   │   │       ├─> Check tool overhang (reduce as much as possible)
│   │   │       ├─> Increase feeds (exit from rubbing to cutting)
│   │   │       └─> Use carbide tooling (stiffer than HSS)
│   │   │
│   │   └─> Test: Does chatter change with RPM?
│   │       ├─> YES → Spindle speed related (adjust RPM)
│   │       └─> NO → Structural issue (low rigidity, loose parts)
│   │
│   ├─> ROUGHNESS (uneven texture, not chatter)
│   │   ├─> Check feed per tooth (too high causes rough finish)
│   │   │   └─> Solution: Reduce feedrate or increase RPM (lower chip load)
│   │   ├─> Check tool condition (dull or chipped)
│   │   │   └─> Solution: Replace tool, check for proper chip evacuation
│   │   └─> Check coolant (inadequate cooling/lubrication)
│   │       └─> Solution: Increase coolant flow, use finishing flood coolant
│   │
│   ├─> STEPS/RIDGES (visible facets instead of smooth surface)
│   │   ├─> Problem: Steps/mm or microstepping incorrect
│   │   │   └─> Solution: Calibrate steps/mm, enable microstepping (min 1/8 step)
│   │   └─> Problem: Backlash or lost steps
│   │       └─> Solution: Check ball screw preload, tighten couplings, reduce acceleration
│   │
│   └─> BURN MARKS (discolored, overheated)
│       ├─> Problem: Excessive heat from cutting (too slow feeds, dull tool)
│       │   └─> Solution: Increase feed rate, reduce RPM, replace tool, add coolant
│       └─> Problem: Rubbing (feeds too low for given RPM)
│           └─> Solution: Increase IPM (chip load must be >0.05mm/tooth minimum)
```

---

## J.3 Axis Stalling or Skipping Steps

```
START: Axis loses position, motors skip steps, or stall during operation
│
├─> Test 1: Does stalling occur at specific location or random?
│   │
│   ├─> SPECIFIC LOCATION (same spot every time)
│   │   ├─> Problem: Mechanical obstruction or tight spot
│   │   │   └─> Solution:
│   │   │       ├─> Check linear guides for damage, debris
│   │   │       ├─> Check ball screw for bent shaft, damaged balls
│   │   │       ├─> Lubricate guides and screw (inadequate lubrication causes binding)
│   │   │       └─> Check rail parallelism (misaligned rails cause binding)
│   │   │
│   │   └─> Problem: Electrical interference at specific location
│   │       └─> Solution: Check for nearby power cables (VFD, spindle), reroute signal cables
│   │
│   └─> RANDOM LOCATION (inconsistent)
│       ├─> Test 2: Does stalling occur during rapid moves or cutting?
│       │   │
│       │   ├─> RAPID MOVES (G00)
│       │   │   ├─> Problem: Insufficient motor torque at high speed
│       │   │   │   └─> Solution:
│       │   │   │       ├─> Reduce max velocity (rapid override in controller)
│       │   │   │       ├─> Increase driver voltage (48V → 72V for steppers)
│       │   │   │       └─> Check driver current setting (must be ≥motor rated current)
│       │   │   │
│       │   │   └─> Problem: Excessive acceleration
│       │   │       └─> Solution: Reduce acceleration setting in controller (lower is smoother)
│       │   │
│       │   └─> CUTTING MOVES (G01)
│       │       ├─> Problem: Cutting forces too high for motor
│       │       │   └─> Solution:
│       │       │       ├─> Reduce depth of cut (lower axial force)
│       │       │       ├─> Reduce width of cut (lower radial force)
│       │       │       ├─> Increase motor size (NEMA 23 → NEMA 34)
│       │       │       └─> Use sharper tool (reduce cutting force)
│       │       │
│       │       └─> Problem: Ball screw binding under load
│       │           └─> Solution: Check preload (too high causes binding), increase diameter
│       │
│       └─> Test 3: Check driver fault LED
│           ├─> Fault LED on → Driver overheating or over-current
│           │   └─> Solution: Add cooling fan to driver, reduce motor current, check short circuit
│           └─> No fault → Problem: EMI/noise causing missed steps
│               └─> Solution: Use shielded cables, ferrite cores on motor leads, separate power/signal cables
```

---

## J.4 Spindle Issues

### J.4.1 Spindle Won't Start

```
START: Spindle does not rotate when M03 commanded
│
├─> Test 1: VFD display shows error code?
│   │
│   ├─> YES → Error Code Diagnostics
│   │   ├─> E001 (Over-current) → Check motor for short, reduce acceleration parameter
│   │   ├─> E002 (Over-voltage) → Check input voltage, brake resistor if decelerating
│   │   ├─> E003 (Over-temperature) → Clean VFD heatsink, check fan, reduce load
│   │   ├─> E010 (Ground fault) → Check motor insulation, ground wire continuity
│   │   └─> Other → Consult VFD manual, reset parameters to factory default
│   │
│   └─> NO error → Test 2: VFD receives run command?
│       ├─> Check VFD input terminals (FOR/REV closure or 0-10V signal present?)
│       │   ├─> NO signal → Problem: Controller output or wiring
│       │   │   └─> Solution: Check relay, optocoupler output, wire continuity
│       │   └─> Signal present → Problem: VFD parameter configuration
│       │       └─> Solution: Check VFD source (terminal/Modbus), run enable, frequency source
│       │
│       └─> Test 3: Does spindle motor hum but not rotate?
│           ├─> YES → Problem: Single-phase input to 3-phase motor
│           │   └─> Solution: Check all 3 phases present (measure VAC on U, V, W outputs)
│           └─> NO sound → Problem: VFD output disabled
│               └─> Solution: Check enable switch, emergency stop circuit, VFD enable parameter
```

### J.4.2 Spindle Runout or Vibration

```
START: Spindle has excessive runout (>0.02mm TIR) or vibration
│
├─> Test 1: Measure runout at spindle taper (ER collet/tool holder interface)
│   │
│   ├─> Runout >0.01mm → Problem: Spindle bearing wear or damage
│   │   └─> Solution:
│   │       ├─> Replace spindle bearings (angular contact bearings)
│   │       ├─> Check preload (adjust or replace preload springs/spacers)
│   │       └─> Verify spindle taper not damaged (clean thoroughly, inspect for dings)
│   │
│   └─> Runout <0.01mm → Test 2: Measure runout at tool tip
│       │
│       ├─> Runout >0.05mm → Problem: Tool holder or collet issue
│       │   └─> Solution:
│       │       ├─> Clean ER collet and nut (remove all chips/debris)
│       │       ├─> Replace worn collet (clamping surfaces worn)
│       │       ├─> Check tool shank diameter (must match collet size exactly)
│       │       └─> Torque collet nut to spec (too loose causes runout, too tight damages collet)
│       │
│       └─> Runout acceptable → Problem: Tool unbalance (high-speed vibration)
│           └─> Solution:
│               ├─> Use balanced tool holders (BT40, HSK for >10,000 RPM)
│               ├─> Reduce RPM (lower vibration frequency below resonance)
│               └─> Check motor mounting (motor must be rigidly attached, no play)
```

---

## J.5 Homing and Limit Switch Issues

```
START: Homing fails or limit switch triggers unexpectedly
│
├─> Test 1: Do limit switches trigger correctly when manually pressed?
│   │
│   ├─> NO (switch not detected)
│   │   ├─> Check wiring continuity (multimeter in continuity mode)
│   │   ├─> Check switch type (NO vs. NC - CNC typically uses NC for safety)
│   │   ├─> Verify input pin assignment in controller config
│   │   └─> Test with multimeter (should see 24V when switch open, 0V when closed for NC)
│   │
│   └─> YES (switch works manually) → Test 2: False triggering?
│       │
│       ├─> Triggers during rapid moves or spindle operation
│       │   ├─> Problem: Electrical noise (EMI from motor/VFD)
│       │   │   └─> Solution:
│       │   │       ├─> Use shielded cable for limit switches (ground shield at controller end only)
│       │   │       ├─> Add RC filter (0.1μF capacitor + 1kΩ resistor across switch)
│       │   │       ├─> Separate switch wiring from motor power cables (min 30cm separation)
│       │   │       └─> Use opto-isolated inputs (if controller supports)
│       │   │
│       │   └─> Problem: Mechanical vibration causing switch to flutter
│       │       └─> Solution: Secure switch mounting, adjust switch actuation distance
│       │
│       └─> Test 3: Homing direction wrong or doesn't stop at switch?
│           ├─> Homing in wrong direction → Problem: Home direction parameter inverted
│           │   └─> Solution: Change home search direction in controller config
│           └─> Doesn't stop at switch → Problem: Home switch polarity inverted
│               └─> Solution: Invert switch input logic (active high/low setting)
```

---

## J.6 Controller Faults

### J.6.1 LinuxCNC Joint Following Error

```
ERROR: Joint [N] following error (position command vs. feedback mismatch)
│
├─> Stepper system (open-loop, no encoder feedback)
│   ├─> This error should NOT occur (no feedback loop)
│   └─> Problem: Closed-loop mode enabled accidentally
│       └─> Solution: Set controller to open-loop (step/dir mode), disable PID loop
│
└─> Servo system (closed-loop with encoder)
    ├─> Check following error amount
    │   ├─> Small error (<1mm) → Problem: Tuning (PID gains too low)
    │   │   └─> Solution: Increase proportional gain (Kp), check derivative gain (Kd)
    │   └─> Large error (>10mm) → Problem: Mechanical or feedback issue
    │       ├─> Check encoder wiring (A/B phases swapped causes wrong direction)
    │       ├─> Check encoder counts per revolution (must match motor spec)
    │       ├─> Check for mechanical binding (manually move axis, should be smooth)
    │       └─> Check motor direction (command forward, motor should move forward)
    │
    └─> Error occurs during rapid acceleration
        └─> Solution: Increase ferror limits in HAL config, reduce max acceleration
```

### J.6.2 Mach3/Mach4 Charge Pump Fault

```
ERROR: Charge pump fault (external E-stop or interlock open)
│
├─> Check E-stop circuit
│   ├─> All E-stop buttons released (twisted to unlock)?
│   └─> E-stop relay energized (contactor pulled in)?
│       └─> If not: Check 24V supply to E-stop circuit, check relay coil
│
├─> Check safety interlocks
│   ├─> All doors closed (limit switch actuated)?
│   ├─> Guard interlock switches closed?
│   └─> If not: Adjust switch position, check NC contact wiring
│
└─> Check breakout board (BOB)
    ├─> Charge pump signal present? (10-25 kHz square wave on output pin)
    │   └─> If not: Reinstall Mach3, check parallel port driver
    └─> Charge pump relay energized?
        └─> If not: Check relay coil voltage, replace relay if faulty
```

---

**End of Troubleshooting Flowcharts and Diagnostics Appendix**
