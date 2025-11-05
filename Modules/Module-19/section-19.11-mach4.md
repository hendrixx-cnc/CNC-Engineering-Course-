# 19.11 Implementation in Mach4

## Mach4 Overview

**Mach4**: Commercial CNC control software for Windows, successor to Mach3.

**Key Features**:
- Plugin-based motion control (external motion controller required)
- Lua scripting for customization
- Modern GUI with touchscreen support
- Support for steppers and servos
- Real-time trajectory planning (depends on plugin)
- Cost: ~$200 (hobby license)

**Architecture**:
```
G-Code → Mach4 Core → Motion Plugin → External Controller
                                           (ESS, CSMIO, etc.)
                                                 ↓
                                           Motor Drivers
                                                 ↑
                                            Encoders
```

**Key Difference from LinuxCNC**: Mach4 relies on external motion controller hardware (not software-based real-time control).

## Motion Controller Hardware

### Common Motion Controllers

**Ethernet SmoothStepper (ESS)**:
- Ethernet connection to PC
- 6-axis control
- Step/direction output (steppers or step-servo drives)
- Servo tuning parameters accessible via Mach4
- Cost: ~$200-250

**CNC4PC C11G** (Galil-based):
- USB connection
- 4-axis control
- Analog ±10V outputs (servo drives)
- Built-in PID loops (tuning via Mach4)
- Cost: ~$300-400

**CSMIO/IP-A**:
- Ethernet connection
- Up to 6 axes
- Analog ±10V outputs
- Advanced features (probe, spindle control)
- Cost: ~$400-500

**Smoothieboard**:
- Open-source firmware
- USB connection
- Step/direction outputs
- Limited servo support
- Cost: ~$150-200

### Selecting a Motion Controller

**Stepper Systems**:
- ESS (best value)
- Smoothieboard (open-source)
- UC100 (USB, budget option)

**Servo Systems**:
- CSMIO/IP-A (full-featured)
- Galil-based cards (industrial-grade)
- ESS (if using step-servo drives)

**Key Consideration**: Servo tuning accessibility (can you adjust PID gains from Mach4?)

## Initial Setup and Configuration

### Mach4 Installation

**Steps**:
1. Download Mach4 installer from machsupport.com
2. Install Mach4 (default path: C:\Mach4Hobby)
3. Install motion controller plugin (ESS, CSMIO, etc.)
4. Launch Mach4, select profile

**Profile**: Contains machine-specific configuration
- Create new profile for your machine
- Name: e.g., "MyMill", "RouterCNC"

### Machine Configuration Wizard

**Mach4 Menu**: Configure → Mach

**Steps**:

**1. Units and Axis**:
- Units: inch or mm
- Active axes: X, Y, Z (select which axes present)
- Homing: Enable if home switches installed

**2. Motor Configuration** (per axis):
- Steps per unit: (encoder resolution or step/dir ratio)
- Velocity: Maximum velocity (in/min or mm/min)
- Acceleration: Maximum acceleration (in/s² or mm/s²)
- Motor direction: CW/CCW (invert if needed)

**3. Soft Limits**:
- Minimum position: -0.1 (slight negative for homing)
- Maximum position: 24.0 (axis travel)

**4. Homing**:
- Home switch location (min or max end)
- Home speed: Fast search (50 IPM) and slow latch (5 IPM)
- Home offset: Distance from switch to zero position

**5. Save Configuration**

## Servo Tuning in Mach4

### Accessing Servo Parameters

**Method 1: Motor Configuration Screen**:
- Configure → Mach → Motor
- Select axis
- Servo tuning tab

**Method 2: Registers (CSMIO/IP)**:
- Configure → Plugins → CSMIO/IP-A
- Servo parameters

**Available Parameters** (depends on controller):
- P Gain (Proportional)
- I Gain (Integral)
- D Gain (Derivative)
- Velocity Feedforward (if supported)
- Acceleration Feedforward (if supported)
- Maximum output
- Deadband

### Tuning Procedure (Mach4)

**Example**: ESS with servo drives

**Step 1: Set Initial Gains**
- Open Motor Configuration → Servo Tuning
- Set conservative values:
  - P = 50
  - I = 0
  - D = 0
  - Max Output = 100%

**Step 2: Test Motion**
- Jog axis slowly (10 IPM)
- Observe: Does axis follow smoothly?
- If sluggish: Increase P
- If oscillates: Reduce P

**Step 3: Increase P Gain**
- Increment P by 25-50%
- Test jog after each change
- Continue until:
  - Slight overshoot appears, or
  - Oscillation begins
- Back off 20-30% from oscillation point

**Example**:
- P = 50: Sluggish
- P = 100: Better, still slow
- P = 150: Responsive
- P = 200: Slight overshoot (8%)
- P = 250: Oscillation
- **Final**: P = 180-200

**Step 4: Add Integral Gain**
- Set I = P / 20 (starting point)
- Test: Does axis hold position when stopped?
- Increase I until steady-state error eliminated
- Watch for overshoot increase

**Example**:
- I = 0: Position drifts 0.002" when stopped
- I = 5: Drift = 0.0005"
- I = 10: Drift < 0.0001" (good)
- I = 20: Overshoot increases to 15% (too much)
- **Final**: I = 10-12

**Step 5: Add Derivative Gain**
- Set D = P / 10 (starting point)
- Test: Does overshoot reduce?
- Increase D until overshoot < 5-10%
- Watch for jittery motion (noise amplification)

**Example**:
- D = 0: Overshoot = 8%
- D = 10: Overshoot = 5%
- D = 20: Overshoot = 2%, slight jitter
- **Final**: D = 12-15

**Step 6: Test at Various Speeds**
- Jog slowly (10 IPM)
- Jog medium (100 IPM)
- Jog fast (max velocity)
- Run test G-code program
- Adjust gains if instability at specific speeds

### Velocity Feedforward (if supported)

**Check**: Does your motion controller support velocity feedforward?
- ESS: Limited support (check documentation)
- CSMIO/IP: Yes (parameter available)
- Galil-based: Yes

**Configuration**:
- Set FF (or FF1) = 0.9 (starting point)
- Jog at constant velocity
- Measure following error (if controller displays)
- Increase FF until following error minimized
- Typical: FF = 0.95-1.0

**Example** (CSMIO/IP):
- Parameter: "Velocity Feedforward Gain"
- Range: 0-100%
- Set to 95% for best tracking

### External Drive Tuning

**Some Servo Drives Have Internal PID Loops**:
- Yaskawa, Delta, Panasonic drives
- Drive has velocity/current loops (fast, 10-20 kHz)
- Mach4 only sends velocity or position commands

**Configuration**:
- Tune drive first (use drive's auto-tune if available)
- Then tune Mach4 position loop (if applicable)
- Cascaded loops: Drive (inner) + Mach4 (outer)

**Example** (Delta ASDA-A2):
- Set drive to Position Mode or Velocity Mode
- Run drive auto-tune (Parameter Pn102 = 2)
- Drive tunes internal velocity loop
- Mach4 sends position commands (no PID tuning needed in Mach4)

## Trajectory Planning Configuration

### Trajectory Parameters

**Mach4 Menu**: Configure → Mach → Trajectory

**Parameters**:
- **Look Ahead**: Number of blocks to read ahead (50-200)
- **CV Distance Mode**: Constant Velocity distance (blending mode)
- **CV Tolerance**: Maximum path deviation (similar to G64 P)
- **Stop on Angles >**: Angle threshold for exact stop (e.g., 90°)

**Example Configuration**:
- Look Ahead: 100 blocks
- CV Tolerance: 0.005" (finishing) or 0.020" (roughing)
- Stop on Angles > 90°: Stop only at corners sharper than 90°

### G-Code Blending Modes

**G64**: Constant Velocity (CV) mode - blend corners

**Example**:
```gcode
G64
G1 X10 Y0 F100
G1 X10 Y10  ; Blend through (10,0) corner
G1 X0 Y10   ; Blend through (10,10) corner
```

**Effect**: Smooth continuous motion, corners rounded within CV tolerance.

**G61**: Exact Stop mode

```gcode
G61
G1 X10 Y0 F100
G1 X10 Y10  ; Stop completely at (10,0)
```

**Effect**: Stop at every programmed point.

**G61.1**: Exact Path mode (maintain path, but don't stop)

```gcode
G61.1
G1 X10 Y0 F100
G1 X10 Y10  ; Follow path exactly, slow if needed
```

**Effect**: Maintains geometric accuracy, slows at corners to stay on path.

### Motion Plugin Settings

**ESS Plugin**:
- Configure → Plugins → ESS
- Charge Pump: Enable (safety feature)
- Step Resolution: 25 kHz typical
- Encoder Resolution: Set if using encoders

**CSMIO Plugin**:
- Configure → Plugins → CSMIO/IP-A
- Encoder Setup: Input scaling, filtering
- Analog Outputs: Range (±10V), offset
- MPG Setup: Manual pulse generator

## Homing Configuration

### Homing Setup

**Configure → Mach → Homing**:

**Per-Axis Parameters**:
- **Home Offset**: Distance from home switch to machine zero
- **Home Speed %**: Percentage of max velocity for homing
- **Slow Home Speed %**: Percentage for slow latch (after switch found)
- **Home Direction**: + or - (which direction to search)

**Example** (X-Axis):
- Home switch at X = -1" (left end)
- Machine zero at X = 0"
- Home Offset = 1.0"
- Home Speed % = 50% (of max velocity)
- Slow Home Speed % = 10%
- Home Direction = Negative (search left)

**Homing Sequence**:
1. Press "Ref All Home" button
2. X-axis moves left at 50% speed
3. Triggers home switch
4. Backs off, approaches at 10% speed
5. Latches on switch
6. Moves to home offset position (0.0)
7. Repeat for Y, Z axes

### Home Switch Wiring

**Single Switch per Axis** (simple):
- Wire switch between input pin and ground
- Normally Open (NO) or Normally Closed (NC)
- Configure in Mach4: Input Signals → Home X

**Shared Home/Limit Switch**:
- One switch acts as both home and limit
- Reduce wiring
- Configure: Enable "Home is Limit" option

**Index Pulse Homing** (high precision):
- Use encoder index pulse as latch
- Requires motion controller with index support (CSMIO)
- Repeatability: ±1 encoder count

## Testing and Diagnostics

### Diagnostics Screen

**Mach4 Menu**: Diagnostics

**Monitor**:
- **Axis Position**: Commanded vs. actual (if encoder feedback)
- **Following Error**: Real-time display
- **Inputs**: Home switches, limit switches, E-stop
- **Outputs**: Motor enable, coolant, spindle

**Test Motion**:
- Jog each axis
- Observe diagnostics for:
  - Position tracking (actual follows commanded)
  - Following error magnitude
  - Smooth motion (no jumps or stuttering)

### Circular Interpolation Test

**G-Code**:
```gcode
G0 X2 Y0
G1 Z-0.1 F20
G2 I-2 J0 F100  ; 360° circle, R=2"
G0 Z0.1
M30
```

**Run Program**:
- Observe motion (smooth circle, no faceting)
- Measure actual radius (dial indicator or probe)
- Compare to nominal (2.000")

**Typical Results**:
- Good tuning: ±0.002" radial error
- Poor tuning: ±0.010" radial error
- Mechanical issues: Oval shape (different X/Y stiffness)

### Velocity Override Test

**Function**: Test feed rate override (real-time speed adjustment)

**Procedure**:
1. Run G-code program at F100
2. During motion, adjust Feed Rate Override slider (50%-150%)
3. Observe: Smooth speed changes, no stuttering

**Expected**: Motion smoothly ramps to new feedrate.

**Problem**: Jerky motion or stuttering → motion controller buffer issue or insufficient look-ahead.

## Lua Scripting for Customization

### Lua Basics in Mach4

**Mach4 uses Lua** for:
- Custom M-codes (M100-M199)
- Screen scripts (button actions)
- PLC script (background logic, runs continuously)
- Macros (reusable functions)

**Accessing Lua Editor**:
- Operator → Edit Screen
- Right-click button → Edit Script

### Example: Custom Probing Routine

**M-Code Script** (m6.mcs - tool change macro):
```lua
-- M6 Tool Change with Probing
function m6()
    local selectedTool = mc.mcToolGetSelected(inst)
    local currentTool = mc.mcToolGetCurrent(inst)

    if (selectedTool == currentTool) then
        return -- No change needed
    end

    -- Move to tool change position
    mc.mcCntlGcodeExecuteWait(inst, "G53 G0 Z0")
    mc.mcCntlGcodeExecuteWait(inst, "G53 G0 X-1 Y-1")

    -- Prompt for manual tool change
    wx.wxMessageBox("Change to Tool #" .. selectedTool)

    -- Probe new tool length
    mc.mcCntlGcodeExecuteWait(inst, "G30")  -- Move to probe position
    mc.mcCntlGcodeExecuteWait(inst, "G38.2 Z-2 F5")  -- Probe down
    local probeZ = mc.mcAxisGetPos(inst, 2)  -- Get Z position

    -- Set tool offset
    mc.mcToolSetData(inst, mc.MTOOL_MILL_HEIGHT, selectedTool, probeZ)
    mc.mcToolSetCurrent(inst, selectedTool)
end

if (mc.mcInEditor() == 1) then
    m6()
end
```

**Use**: Automatic tool length probing after tool change.

### PLC Script (Background Tasks)

**PLC Script Runs Continuously** (every cycle):

**Example**: Monitor spindle speed, adjust feedrate
```lua
-- PLC Script: Adaptive Feed
function PLCScript()
    local spindleRPM = mc.mcSpindleGetCurrentRPM(inst)
    local targetRPM = mc.mcSpindleGetCommandedRPM(inst)

    -- If spindle load high (RPM drops), reduce feedrate
    if (spindleRPM < targetRPM * 0.8) then
        mc.mcCntlSetFRO(inst, 70)  -- Reduce to 70% feedrate
    else
        mc.mcCntlSetFRO(inst, 100)  -- Restore 100%
    end
end
```

**Use**: Prevent spindle stall during heavy cuts.

## Plugin Development (Advanced)

### Mach4 Plugin API

**For Advanced Users**: Create custom motion control plugins.

**Language**: C/C++

**API**: Mach4 Plugin SDK (available from machsupport.com)

**Use Cases**:
- Custom motion controller hardware
- Specialized kinematics (e.g., SCARA robot)
- Integration with external systems

**Example Plugins**:
- ESS Plugin (Ethernet SmoothStepper)
- CSMIO Plugin (CS-Lab motion controllers)
- Galil Plugin (Galil motion controllers)

**Complexity**: High (requires C++ programming, real-time considerations)

## Common Issues and Solutions

### Issue: Jerky Motion

**Possible Causes**:
1. Insufficient look-ahead buffer
2. PC performance (Mach4 running slow)
3. USB latency (if using USB controller)
4. Short G-code line segments (CAM output)

**Solutions**:
- Increase look-ahead: Configure → Mach → Trajectory → Look Ahead = 200
- Close background programs (browser, etc.)
- Use Ethernet controller instead of USB
- Adjust CAM tolerance (longer line segments)

### Issue: Following Error

**Symptom**: Axis lags command, following error alarm

**Causes**:
1. P gain too low
2. No velocity feedforward
3. Mechanical binding (friction)
4. Motor undersized

**Solutions**:
- Increase P gain (test for stability)
- Enable velocity feedforward (if supported)
- Lubricate ways, check for binding
- Upgrade motor (more torque)

### Issue: Oscillation

**Symptom**: Axis shakes or buzzes, unstable

**Causes**:
1. P or D gain too high
2. Mechanical resonance
3. Encoder noise
4. Loose coupling

**Solutions**:
- Reduce P and D gains 20-30%
- Add mechanical damping
- Check encoder wiring, shielding
- Tighten couplings, check alignment

## Summary

Mach4 provides accessible servo control for hobby and professional CNC:

**Key Components**:
1. **External Motion Controller**: ESS, CSMIO, Galil (handles real-time control)
2. **Mach4 Software**: G-code interpretation, trajectory planning, GUI
3. **Lua Scripting**: Customization, macros, PLC logic

**Tuning Process**:
1. Configure machine (axes, limits, motors)
2. Set motion controller parameters (steps/unit, velocity, accel)
3. Tune servo gains (P, I, D, feedforward)
4. Test and validate (jog, circular interp, cutting)

**Advantages**:
- Easy setup (GUI-based)
- Good plugin support (motion controllers)
- Lua scripting (flexible customization)
- Active community support

**Limitations**:
- Requires external motion controller (added cost)
- Real-time performance depends on controller hardware
- Less transparent than LinuxCNC (closed-source core)

**Next**: [19.12 Troubleshooting and Optimization](section-19.12-troubleshooting.md)

---

**Next**: [19.12 Troubleshooting and Optimization](section-19.12-troubleshooting.md)
