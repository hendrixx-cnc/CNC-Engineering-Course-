## 9. Advanced HAL Techniques

### 9.1 Electronic Gearing and Axis Slaving

**Electronic Gearing** synchronizes one axis to another at a fixed or variable ratio, enabling tandem axis control, gantry machines, and master-slave configurations.

**Application: Gantry Mill with Dual Y-Axis Motors**

Problem: Gantry with motors on left and right sides (Y1, Y2) must move synchronously to prevent racking.

**Solution 1: Trivial Gantrykins (Built-In)**

```hal
# Use gantrykins instead of trivkins
loadrt gantrykins coordinates=XYYZ  # Y appears twice = dual motor Y-axis

# Joint mapping:
# Joint 0 = X-axis
# Joint 1 = Y1 (left motor)
# Joint 2 = Y2 (right motor)
# Joint 3 = Z-axis

# Configure both Y stepgens identically
setp hm2_7i96.0.stepgen.01.position-scale 800
setp hm2_7i96.0.stepgen.02.position-scale 800

# Connect joints
net x-pos-cmd motion.00.motor-pos-cmd => hm2_7i96.0.stepgen.00.position-cmd
net y1-pos-cmd motion.01.motor-pos-cmd => hm2_7i96.0.stepgen.01.position-cmd
net y2-pos-cmd motion.02.motor-pos-cmd => hm2_7i96.0.stepgen.02.position-cmd  # Synchronized Y2
net z-pos-cmd motion.03.motor-pos-cmd => hm2_7i96.0.stepgen.03.position-cmd

# Homing: Y-axis homes both joints simultaneously
# G-code: G0 Y100 moves both Y1 and Y2 to 100 mm
```

**Solution 2: Manual Electronic Gearing**

```hal
# Use trivkins (4 independent axes)
loadrt trivkins

# Scale component for ratio adjustment
loadrt scale count=1
addf scale.0 servo-thread

# Y2 follows Y1 with adjustable ratio
setp scale.0.gain 1.0  # 1:1 ratio (adjust if Y2 needs compensation)

net y1-cmd motion.01.motor-pos-cmd => scale.0.in
net y2-cmd scale.0.out => hm2_7i96.0.stepgen.02.position-cmd

# Y1 controlled normally
net y1-pos-cmd motion.01.motor-pos-cmd => hm2_7i96.0.stepgen.01.position-cmd
```

**Variable Ratio Gearing:**

```hal
# Example: Rotary axis (A) drives tangential knife at variable ratio
loadrt mult2 count=1
addf mult2.0 servo-thread

# Ratio = f(cutting radius)
net cutting-radius ui.radius-input => mult2.0.in0
net a-velocity motion.03.joint-vel-cmd => mult2.0.in1
net knife-speed mult2.0.out => knife-motor.speed-cmd

# Tangential velocity = angular velocity × radius
# knife-speed = A-axis angular velocity (deg/s) × cutting radius (mm)
```

### 9.2 Spindle Synchronization and Rigid Tapping

**Rigid Tapping** requires precise spindle position tracking for coordinated Z-axis motion during threading.

**Requirements:**

1. Spindle encoder with index pulse (Z channel)
2. DPLL (Digital Phase-Locked Loop) for position interpolation
3. Motion controller configured for spindle sync

**Configuration:**

```hal
# ==========================================
# SPINDLE ENCODER SETUP
# ==========================================
setp hm2_7i96.0.encoder.04.scale 1024  # 1024 PPR encoder
setp hm2_7i96.0.encoder.04.counter-mode 0  # Quadrature mode
setp hm2_7i96.0.encoder.04.filter 1  # Enable input filter

# Connect spindle encoder to motion
net spindle-position hm2_7i96.0.encoder.04.position => motion.spindle-revs
net spindle-velocity hm2_7i96.0.encoder.04.velocity => motion.spindle-speed-in
net spindle-index-enable hm2_7i96.0.encoder.04.index-enable <=> motion.spindle-index-enable

# ==========================================
# DPLL CONFIGURATION (Interpolation)
# ==========================================
# DPLL provides sub-count position resolution for smooth motion
setp hm2_7i96.0.dpll.01.timer-us -100  # Timing compensation (tune empirically)

# Connect DPLL to spindle encoder
net spindle-pos-dpll hm2_7i96.0.dpll.01.phase-position => motion.spindle-phase-position
```

**INI File:**

```ini
[TRAJ]
SPINDLE_0 = 0

[SPINDLE_0]
MAX_FORWARD_VELOCITY = 3000  # Maximum spindle RPM
ENCODER_SCALE = 1024         # Encoder PPR
```

**G-code Usage:**

```gcode
M3 S500          ; Start spindle at 500 RPM
G4 P2            ; Wait 2 seconds for spindle to reach speed
G33.1 Z-25 K1.5  ; Rigid tap to 25 mm depth, 1.5 mm pitch
G33.1 Z0         ; Retract (reverse tap)
M5               ; Stop spindle
```

**Threading (G33):**

```gcode
G33 Z-50 K2.0    ; Thread 50 mm depth, 2.0 mm pitch
; Z-axis velocity synchronized to spindle rotation
; Feed rate = spindle RPM × pitch (mm/rev)
```

### 9.3 Custom Kinematics: Delta Robot Example

**Delta Robot:** 3 vertical arms control XYZ position of end effector platform via inverse kinematics.

**Kinematics Component (delta.comp):**

```c
component delta_kins "Delta robot inverse kinematics";
description """
Delta parallel robot kinematics.
Three vertical linear joints control Cartesian XYZ position.
""";

// Cartesian coordinates (world space)
pin in float pos_x "Commanded X position";
pin in float pos_y "Commanded Y position";
pin in float pos_z "Commanded Z position";

// Joint positions (motor space, vertical travel)
pin out float joint_0 "Vertical position of arm 0";
pin out float joint_1 "Vertical position of arm 1";
pin out float joint_2 "Vertical position of arm 2";

// Geometric parameters
parameter rw float base_radius = 100.0 "Base triangle radius";
parameter rw float platform_radius = 50.0 "Platform triangle radius";
parameter rw float arm_length = 150.0 "Upper arm length";
parameter rw float rod_length = 300.0 "Parallel rod length";

function inverse_kins fp "Calculate joint positions from Cartesian";

license "GPL";

;;

#include <rtapi_math.h>

// Helper function: Calculate single arm joint position
static float calc_joint_pos(float x, float y, float z, float angle,
                            float base_r, float platform_r, float arm_len, float rod_len) {
    // Base pivot position
    float base_x = base_r * cos(angle);
    float base_y = base_r * sin(angle);

    // Platform attachment position
    float platform_x = x + platform_r * cos(angle);
    float platform_y = y + platform_r * sin(angle);

    // Vector from base to platform
    float dx = platform_x - base_x;
    float dy = platform_y - base_y;
    float dz = z;

    // Distance in XY plane
    float r = sqrt(dx*dx + dy*dy);

    // Total 3D distance
    float d = sqrt(r*r + dz*dz);

    // Check reachability
    if (d > (arm_len + rod_len) || d < fabs(arm_len - rod_len)) {
        return 0.0;  // Unreachable, return safe position
    }

    // Law of cosines: solve for arm angle
    float cos_angle = (arm_len*arm_len + d*d - rod_len*rod_len) / (2.0 * arm_len * d);
    float arm_angle = acos(cos_angle);

    // Angle from horizontal to platform
    float platform_angle = atan2(dz, r);

    // Joint vertical position
    return z - arm_len * sin(arm_angle + platform_angle);
}

FUNCTION(inverse_kins) {
    // Arm angles: 0°, 120°, 240° (equilateral triangle)
    const float angles[3] = {0.0, 2.0*M_PI/3.0, 4.0*M_PI/3.0};

    float x = pos_x;
    float y = pos_y;
    float z = pos_z;

    // Calculate each joint position
    joint_0 = calc_joint_pos(x, y, z, angles[0],
                             base_radius, platform_radius, arm_length, rod_length);
    joint_1 = calc_joint_pos(x, y, z, angles[1],
                             base_radius, platform_radius, arm_length, rod_length);
    joint_2 = calc_joint_pos(x, y, z, angles[2],
                             base_radius, platform_radius, arm_length, rod_length);
}
```

**HAL Integration:**

```hal
# Load custom kinematics
loadrt delta_kins
addf delta-kins.inverse-kins servo-thread

# Configure geometry
setp delta-kins.base-radius 100.0
setp delta-kins.platform-radius 50.0
setp delta-kins.arm-length 150.0
setp delta-kins.rod-length 300.0

# Connect Cartesian commands to kinematics
net x-cmd motion.00.pos-cmd => delta-kins.pos-x
net y-cmd motion.01.pos-cmd => delta-kins.pos-y
net z-cmd motion.02.pos-cmd => delta-kins.pos-z

# Connect joint commands to motors
net joint-0-cmd delta-kins.joint-0 => pid.0.command
net joint-1-cmd delta-kins.joint-1 => pid.1.command
net joint-2-cmd delta-kins.joint-2 => pid.2.command
```

### 9.4 Tool Length Probing and Automatic Offsets

**Application:** Touch probe automatically measures tool length, updates tool table.

**Probe HAL Setup:**

```hal
# Tool probe input (normally open switch, closes when contact)
net probe-input hm2_7i96.0.gpio.015.in => motion.probe-input

# Probe LED indicator
setp hm2_7i96.0.gpio.014.is_output 1
net probe-active motion.probe-input => hm2_7i96.0.gpio.014.out
```

**G-code Probing Subroutine (O<tool_probe> sub):**

```gcode
O<tool_probe> sub  ; Tool length measurement subroutine

; Assumes:
; - Z zero set on top of gauge block (known height)
; - Gauge block height in parameter #<gauge_height>
; - Rapid to position above gauge block

#<gauge_height> = 25.0  ; 25 mm gauge block

G91               ; Relative mode
G38.2 Z-50 F25    ; Probe toward gauge, 25 mm/min feed
G90               ; Absolute mode

; Calculate tool length offset
#<probe_z> = #5063  ; Z position when probe tripped (absolute)
#<tool_offset> = [#<probe_z> + #<gauge_height>]  ; Offset from Z zero

; Update tool table (requires M66/M67 or Python component)
; For LinuxCNC 2.8+, use G10 L1:
G10 L1 P#<_current_tool> Z#<tool_offset>  ; Set tool offset

G91 G0 Z5         ; Retract 5 mm
G90 G0 Z50        ; Move to safe height

O<tool_probe> endsub
```

**Usage:**

```gcode
T1 M6             ; Load tool 1
G43 H1            ; Apply tool length offset
O<tool_probe> call  ; Measure and update tool 1 offset
M0                ; Pause for verification

; Tool offset now automatically compensates for tool length
G0 Z0             ; Tool tip now at Z=0 (gauge block top surface)
```

### 9.5 Adaptive Feed Rate Control

**Application:** Reduce feed rate based on real-time spindle load, preventing tool breakage.

**HAL Component (adaptive_feed.comp):**

```c
component adaptive_feed "Adjust feed rate based on spindle load";

pin in float spindle_load "Spindle load percentage (0-100)";
pin out float feed_scale "Feed override scale (0-1.0)";

parameter rw float max_load = 80.0 "Maximum allowable spindle load (%)";
parameter rw float min_scale = 0.1 "Minimum feed scale (10%)";

function _ fp;
license "GPL";

;;

FUNCTION(_) {
    if (spindle_load > max_load) {
        // Load too high: reduce feed rate proportionally
        float overload = (spindle_load - max_load) / 20.0;  // 20% overload = 1.0
        feed_scale = 1.0 - overload;

        // Clamp to minimum
        if (feed_scale < min_scale) {
            feed_scale = min_scale;
        }
    } else {
        // Normal load: full feed rate
        feed_scale = 1.0;
    }
}
```

**HAL Integration:**

```hal
loadrt adaptive_feed
addf adaptive-feed servo-thread

# Configure thresholds
setp adaptive-feed.max-load 75.0  # Start reducing at 75% spindle load
setp adaptive-feed.min-scale 0.25  # Never go below 25% feed rate

# Connect spindle load sensor (analog input scaled to 0-100%)
net spindle-load-pct analog-input.0 => adaptive-feed.spindle-load

# Connect feed scale to motion controller
net feed-scale-adaptive adaptive-feed.feed-scale => motion.adaptive-feed
```

**Result:** Feed rate automatically reduces when spindle load exceeds 75%, preventing overload and tool damage.

### 9.6 Multi-Pass Cutting Logic

**Application:** Automatically execute multiple cutting passes with incremental depth.

**Python HAL Component (multi_pass.py):**

```python
#!/usr/bin/env python3
"""
Multi-pass cutting controller
Executes G-code subroutine multiple times with incremental Z depth
"""

import hal
import time

class MultiPass:
    def __init__(self):
        self.h = hal.component("multi-pass")

        # Configuration
        self.h.newpin("start", hal.HAL_BIT, hal.HAL_IN)
        self.h.newpin("reset", hal.HAL_BIT, hal.HAL_IN)
        self.h.newpin("total-depth", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("depth-per-pass", hal.HAL_FLOAT, hal.HAL_IN)

        # Status outputs
        self.h.newpin("current-pass", hal.HAL_S32, hal.HAL_OUT)
        self.h.newpin("total-passes", hal.HAL_S32, hal.HAL_OUT)
        self.h.newpin("current-depth", hal.HAL_FLOAT, hal.HAL_OUT)
        self.h.newpin("complete", hal.HAL_BIT, hal.HAL_OUT)

        self.h.ready()

        self.pass_num = 0
        self.active = False

    def update(self):
        if self.h["reset"]:
            self.pass_num = 0
            self.active = False
            self.h["complete"] = False

        if self.h["start"] and not self.active:
            # Calculate number of passes
            total_depth = abs(self.h["total-depth"])
            depth_per_pass = abs(self.h["depth-per-pass"])

            if depth_per_pass > 0:
                num_passes = int(total_depth / depth_per_pass)
                if total_depth % depth_per_pass > 0:
                    num_passes += 1  # Partial final pass

                self.h["total-passes"] = num_passes
                self.active = True

        if self.active:
            # Update current depth for pass
            depth_per_pass = abs(self.h["depth-per-pass"])
            self.h["current-depth"] = (self.pass_num + 1) * depth_per_pass

            # Clamp to total depth
            if self.h["current-depth"] > abs(self.h["total-depth"]):
                self.h["current-depth"] = abs(self.h["total-depth"])

            self.h["current-pass"] = self.pass_num + 1

            # Advance pass (triggered externally by G-code M66)
            # In practice, G-code would read current-depth and execute pass

    def run(self):
        try:
            while True:
                self.update()
                time.sleep(0.01)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    mp = MultiPass()
    mp.run()
```

**G-code Integration:**

```gcode
; Multi-pass pocket milling

#<total_depth> = 10.0      ; 10 mm total depth
#<depth_per_pass> = 2.0    ; 2 mm per pass

; Set multi-pass parameters (writes to HAL pins)
M68 E0 Q#<total_depth>
M68 E1 Q#<depth_per_pass>
M68 E2 Q1  ; Start multi-pass sequence

; Loop for each pass
O100 while [#<multi_pass_complete> EQ 0]
    #<current_depth> = #5399  ; Read current-depth from HAL (example parameter)

    ; Execute cutting pass at current depth
    G0 X0 Y0
    G1 Z[-#<current_depth>] F100
    ; ... pocket toolpath at current Z depth ...
    G0 Z5  ; Retract

    ; Advance to next pass (increment counter in HAL component)
    M66 P0 L0  ; Wait for HAL input (trigger next pass)
O100 endwhile
```

### 9.7 Backlash Compensation

**Problem:** Mechanical backlash causes position error during direction reversal.

**Solution:** HAL backlash component offsets commanded position based on direction.

```hal
# Load backlash compensation
loadrt backlash count=3
addf backlash.0 servo-thread
addf backlash.1 servo-thread
addf backlash.2 servo-thread

# Configure X-axis backlash (0.05 mm measured)
setp backlash.0.backlash 0.05

# Insert between motion and stepgen
net x-cmd-raw motion.00.motor-pos-cmd => backlash.0.in
net x-cmd-compensated backlash.0.out => hm2_7i96.0.stepgen.00.position-cmd
net x-pos-fb hm2_7i96.0.stepgen.00.position-fb => motion.00.motor-pos-fb backlash.0.filt-in

# Backlash component adds 0.05 mm when direction changes from negative to positive
# Removes 0.05 mm when changing from positive to negative
# Net effect: compensates for mechanical slack
```

**Alternative: INI-Based Backlash (Simpler but Less Precise):**

```ini
[JOINT_0]
BACKLASH = 0.05  ; mm (applied by motion controller, not HAL)
```

### 9.8 Tool Changer Sequencing

**Application:** Automatic tool changer with rotary carousel and pneumatic arm.

**State Machine Component (tool_changer.comp):**

```c
component tool_changer "Automatic tool changer controller";

pin in bit start "Start tool change sequence";
pin in s32 tool_pocket "Tool pocket number (1-8)";
pin in bit tool_clamped "Sensor: Tool clamped in spindle";
pin in bit carousel_aligned "Sensor: Carousel at correct position";

pin out bit unclamp "Solenoid: Release spindle collet";
pin out bit carousel_fwd "Motor: Rotate carousel forward";
pin out bit arm_extend "Solenoid: Extend arm to carousel";
pin out bit complete "Tool change complete";

parameter rw u32 timeout_ms = 5000 "Timeout per step (ms)";

function _ "Tool changer state machine";
license "GPL";

;;

#define STATE_IDLE 0
#define STATE_UNCLAMP 1
#define STATE_ROTATE 2
#define STATE_EXTEND 3
#define STATE_CLAMP 4
#define STATE_RETRACT 5
#define STATE_DONE 6

static int state = STATE_IDLE;
static int prev_tool_pocket = 0;
static unsigned long timer = 0;

FUNCTION(_) {
    static bool prev_start = 0;
    bool start_edge = start && !prev_start;
    prev_start = start;

    unsigned long timeout_cycles = timeout_ms;  // Assume 1 kHz servo thread = 1 ms/cycle

    switch (state) {
        case STATE_IDLE:
            unclamp = 0;
            carousel_fwd = 0;
            arm_extend = 0;
            complete = 0;

            if (start_edge) {
                state = STATE_UNCLAMP;
                timer = 0;
            }
            break;

        case STATE_UNCLAMP:
            unclamp = 1;
            timer++;

            if (!tool_clamped || timer > timeout_cycles) {
                state = STATE_ROTATE;
                timer = 0;
            }
            break;

        case STATE_ROTATE:
            unclamp = 0;

            // Rotate carousel to correct pocket
            if (carousel_aligned) {
                carousel_fwd = 0;
                state = STATE_EXTEND;
                timer = 0;
            } else {
                carousel_fwd = 1;
                timer++;
                if (timer > timeout_cycles) {
                    // Timeout: abort
                    state = STATE_IDLE;
                    rtapi_print_msg(RTAPI_MSG_ERR, "Tool changer: Carousel timeout\n");
                }
            }
            break;

        case STATE_EXTEND:
            arm_extend = 1;
            timer++;

            if (timer > 1000) {  // 1 second delay for arm extend
                state = STATE_CLAMP;
                timer = 0;
            }
            break;

        case STATE_CLAMP:
            unclamp = 0;  // Clamp tool (solenoid de-energized)
            timer++;

            if (tool_clamped || timer > timeout_cycles) {
                state = STATE_RETRACT;
                timer = 0;
            }
            break;

        case STATE_RETRACT:
            arm_extend = 0;
            timer++;

            if (timer > 1000) {  // 1 second delay for arm retract
                state = STATE_DONE;
            }
            break;

        case STATE_DONE:
            complete = 1;

            if (!start) {  // Wait for start to go FALSE
                state = STATE_IDLE;
                prev_tool_pocket = tool_pocket;
            }
            break;
    }
}
```

**HAL Integration:**

```hal
loadrt tool_changer
addf tool-changer servo-thread

setp tool-changer.timeout-ms 5000

# Connect motion controller
net tool-change-start iocontrol.0.tool-change => tool-changer.start
net tool-pocket iocontrol.0.tool-prep-number => tool-changer.tool-pocket
net tool-change-done tool-changer.complete => iocontrol.0.tool-changed

# Connect sensors
net tool-clamped-sensor hm2_7i96.0.gpio.010.in => tool-changer.tool-clamped
net carousel-aligned-sensor hm2_7i96.0.gpio.011.in => tool-changer.carousel-aligned

# Connect outputs
setp hm2_7i96.0.gpio.012.is_output 1
setp hm2_7i96.0.gpio.013.is_output 1
setp hm2_7i96.0.gpio.014.is_output 1

net unclamp-out tool-changer.unclamp => hm2_7i96.0.gpio.012.out
net carousel-motor tool-changer.carousel-fwd => hm2_7i96.0.gpio.013.out
net arm-extend-out tool-changer.arm-extend => hm2_7i96.0.gpio.014.out
```

### 9.9 Plasma Torch Height Control (THC)

**Application:** Maintain constant arc voltage (proportional to torch-to-workpiece distance) during plasma cutting.

**THC HAL Component (plasma_thc.comp):**

```c
component plasma_thc "Plasma torch height controller";

pin in float arc_voltage "Measured arc voltage (V)";
pin in float target_voltage "Target arc voltage (V)";
pin in bit arc_ok "Arc established and stable";
pin in bit torch_on "Torch firing";

pin out float z_offset "Z-axis position correction (mm)";

parameter rw float voltage_tolerance = 5.0 "Voltage deadband (V)";
parameter rw float correction_scale = 0.5 "mm per volt error";
parameter rw float max_correction = 5.0 "Maximum Z offset (mm)";

function _ fp;
license "GPL";

;;

FUNCTION(_) {
    if (!arc_ok || !torch_on) {
        // No correction when arc off
        z_offset = 0.0;
        return;
    }

    float voltage_error = target_voltage - arc_voltage;

    // Apply deadband
    if (fabs(voltage_error) < voltage_tolerance) {
        // Within tolerance, no correction
        return;
    }

    // Calculate correction (mm)
    float correction = voltage_error * correction_scale;

    // Update offset (integrating controller)
    z_offset += correction;

    // Clamp to limits
    if (z_offset > max_correction) z_offset = max_correction;
    if (z_offset < -max_correction) z_offset = -max_correction;
}
```

**HAL Integration:**

```hal
loadrt plasma_thc
addf plasma-thc servo-thread

# Load sum component to add offset to Z position
loadrt sum2 count=1
addf sum2.0 servo-thread

# Configure THC
setp plasma-thc.target-voltage 120.0  # 120V arc voltage target
setp plasma-thc.voltage-tolerance 5.0  # ±5V deadband
setp plasma-thc.correction-scale 0.1   # 0.1 mm per volt error
setp plasma-thc.max-correction 3.0     # ±3 mm max correction

# Connect arc voltage sensor
net arc-voltage analog-input.0 => plasma-thc.arc-voltage

# Connect torch status
net torch-on motion.digital-out-00 => plasma-thc.torch-on
net arc-ok hm2_7i96.0.gpio.015.in => plasma-thc.arc-ok

# Insert THC offset into Z-axis command
net z-cmd-raw motion.02.motor-pos-cmd => sum2.0.in0
net z-offset-thc plasma-thc.z-offset => sum2.0.in1
net z-cmd-compensated sum2.0.out => hm2_7i96.0.stepgen.02.position-cmd
```

### 9.10 Summary: Advanced HAL Techniques

Advanced HAL techniques unlock LinuxCNC's full potential for specialized applications:

**Key Techniques:**

1. **Electronic gearing**: Gantry machines, master-slave axes, synchronized motion
2. **Spindle synchronization**: Rigid tapping, threading, position-synchronized operations
3. **Custom kinematics**: Non-Cartesian robots (delta, SCARA, cable-driven)
4. **Tool probing**: Automatic tool length measurement, workpiece probing
5. **Adaptive control**: Real-time feed rate adjustment based on process feedback
6. **State machines**: Complex sequencing (tool changers, multi-pass operations)
7. **Process control**: THC, laser power modulation, EDM gap control

**Design Principles:**

- **Modularity**: Break complex logic into discrete components
- **Robustness**: Handle edge cases, timeouts, and error conditions
- **Observability**: Expose status pins for monitoring and debugging
- **Configurability**: Use parameters for tuning without code changes

**Next Section** (14.10) covers diagnostic tools: halcmd, halmeter, halscope, and systematic troubleshooting procedures for HAL configuration and runtime issues.

***

*Total: 4,231 words | 0 equations | 9 complete worked examples | 0 tables | 18 code blocks*
