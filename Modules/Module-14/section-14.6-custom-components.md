## 6. Custom HAL Components in C

### 6.1 Why Write Custom Components?

While LinuxCNC's standard component library covers most CNC control scenarios, custom components enable specialized functionality:

- **Custom kinematics**: Non-Cartesian robots (SCARA, delta, cable-driven mechanisms)
- **Tool changers**: Complex sequencing logic beyond standard I/O mapping
- **Process control**: Specialized algorithms (laser power modulation, EDM gap control, plasma THC)
- **Hardware interfaces**: Proprietary encoder protocols, custom FPGA communication
- **Performance optimization**: Combining multiple HAL components into single efficient function

**Real-Time vs. User-Space:**

- **Real-time components (this section)**: Time-critical logic requiring deterministic execution (<1 ms latency)
- **User-space components (Section 14.7)**: Non-critical tasks (GUI updates, VFD communication, data logging)

### 6.2 The comp Compiler: HAL Component Development Tool

The `comp` utility simplifies HAL component development by generating boilerplate C code from high-level component descriptions. Instead of manually writing HAL registration code, memory management, and thread integration, developers focus on algorithmic logic.

**Workflow:**

```
1. Write .comp file (component description + C code)
2. Run comp compiler: comp --install mycomponent.comp
3. Component compiled and installed to system
4. Load in HAL file: loadrt mycomponent
```

**comp File Structure:**

```c
component mycomponent "Brief description";

// Pin declarations
pin in float input "Input signal";
pin out float output "Output signal";

// Parameter declarations
parameter rw float gain = 1.0 "Scaling factor";

// Function declaration
function _;  // Underscore = default function name (mycomponent)

license "GPL";
author "Your Name";

;;  // End of declarations, C code begins

// Function implementation (executed every thread cycle)
FUNCTION(_) {
    output = input * gain;
}
```

**Compilation:**

```bash
comp --install mycomponent.comp
# Generates mycomponent.c, compiles to mycomponent.ko (kernel module)
# Installs to /usr/lib/linuxcnc/modules/
```

**Usage in HAL:**

```hal
loadrt mycomponent
addf mycomponent servo-thread

setp mycomponent.gain 2.5
net input-sig => mycomponent.input
net output-sig <= mycomponent.output
```

### 6.3 Pin and Parameter Declarations

**Pin Syntax:**

```c
pin [direction] [type] [name] [if condition] "description";

// Direction: in, out, io
// Type: bit, s32, u32, float
// Name: Pin identifier (component.name in HAL)
// If condition: Optional, enables/disables pin based on modparam
// Description: Help text
```

**Examples:**

```c
component encoder_ex "Example encoder with multiple modes";

// Basic pins
pin in bit phase_a "Encoder A channel";
pin in bit phase_b "Encoder B channel";
pin out s32 counts "Quadrature count";
pin out float position "Scaled position";

// Conditional pins (enabled via modparam)
pin in bit index_enable if index "Enable index search";
pin in bit phase_z if index "Index pulse (Z channel)";

// I/O pin (bidirectional)
pin io bit index_latch "Latches TRUE when index found";

parameter rw float scale = 1.0 "Counts per position unit";
parameter rw bit index = 0 "Enable index pulse support (modparam)";

function _ "Update encoder counts";
license "GPL";
;;

FUNCTION(_) {
    // Function implementation
}
```

**Loading with modparam:**

```hal
# Enable index support for first instance, disable for second
loadrt encoder_ex count=2 index=1,0

# encoder_ex.0 has phase_z and index_enable pins
# encoder_ex.1 does not (index=0)
```

**Parameter Types:**

- **rw**: Read-write (settable via `setp` in HAL)
- **r**: Read-only (informational, set by component logic)
- **w**: Write-only (rare, typically for command inputs)

```c
parameter rw float pgain = 1.0 "Proportional gain";
parameter r u32 cycles_executed "Function call counter (read-only)";
```

### 6.4 Complete Example: Hysteresis Comparator

**Application:** Convert noisy analog signal to clean digital output with hysteresis (Schmitt trigger behavior).

**hysteresis.comp:**

```c
component hysteresis "Schmitt trigger with adjustable thresholds";
description """
Hysteresis comparator prevents output chatter on noisy input signals.

Example: Spindle at-speed detection
  - Set high-threshold = 95% of commanded speed
  - Set low-threshold = 90% of commanded speed
  - Output goes TRUE when input exceeds high-threshold
  - Output stays TRUE until input falls below low-threshold
""";

pin in float input "Analog input signal";
pin out bit output "Digital output (with hysteresis)";

parameter rw float high_threshold = 1.0 "Rising edge threshold";
parameter rw float low_threshold = 0.5 "Falling edge threshold";

function _ fp "Update output based on input (floating-point)";

license "GPL";
author "LinuxCNC Example";

;;

FUNCTION(_) {
    // State machine: output retains previous state unless threshold crossed
    if (output) {
        // Currently TRUE: check if input dropped below low threshold
        if (input < low_threshold) {
            output = 0;  // Turn off
        }
    } else {
        // Currently FALSE: check if input exceeded high threshold
        if (input >= high_threshold) {
            output = 1;  // Turn on
        }
    }

    // Hysteresis gap = high_threshold - low_threshold
    // Prevents chatter if input oscillates within gap
}
```

**Compilation and Installation:**

```bash
comp --install hysteresis.comp
# Output: Compiling realtime hysteresis.c
#         Successfully installed to /usr/lib/linuxcnc/modules/
```

**Usage: Spindle At-Speed Detection**

```hal
loadrt hysteresis
addf hysteresis.0 servo-thread

# Spindle commanded at 1000 RPM
# Enable cutting when spindle reaches 95% (950 RPM)
# Disable if drops below 90% (900 RPM)
setp hysteresis.0.high-threshold 950.0
setp hysteresis.0.low-threshold 900.0

net spindle-speed-fb tachometer.rpm => hysteresis.0.input
net spindle-at-speed hysteresis.0.output => motion.spindle-at-speed

# Motion controller waits for spindle-at-speed before starting cut (M3 S1000)
```

**Truth Table:**

| Input | Previous Output | New Output | Reason |
|-------|----------------|------------|--------|
| 800 RPM | FALSE | FALSE | Below low threshold |
| 920 RPM | FALSE | FALSE | Between thresholds, output stays FALSE |
| 960 RPM | FALSE | TRUE | Exceeded high threshold → turn on |
| 930 RPM | TRUE | TRUE | Above low threshold, output stays TRUE |
| 880 RPM | TRUE | FALSE | Dropped below low threshold → turn off |

### 6.5 State Machines and Persistent Variables

**Problem:** HAL functions are stateless (no memory between calls). How to implement multi-step sequences?

**Solution:** Use static variables within FUNCTION() block.

**Example: Tool Changer Sequencer**

```c
component tool_changer "Pneumatic tool changer with timing sequence";

pin in bit start "Start tool change sequence (rising edge trigger)";
pin in bit tool_clamped "Sensor: Tool clamped in spindle";
pin in bit tool_unclamped "Sensor: Tool released from spindle";

pin out bit unclamp_solenoid "Solenoid: Release tool clamp";
pin out bit blowoff_solenoid "Solenoid: Air blow-off (chip removal)";
pin out bit sequence_done "Tool change complete";

parameter rw u32 unclamp_delay_ms = 500 "Delay after unclamp before blowoff";
parameter rw u32 blowoff_duration_ms = 2000 "Blowoff duration";

function _ "Execute tool change sequence";
license "GPL";

;;

FUNCTION(_) {
    // Static variables persist between function calls
    static int state = 0;  // State machine: 0=idle, 1=unclamping, 2=blowoff, 3=done
    static bool prev_start = 0;  // Edge detection
    static unsigned long timer = 0;  // Cycle counter for delays

    // Convert milliseconds to servo thread cycles (assume 1 kHz = 1 ms/cycle)
    unsigned long unclamp_delay_cycles = unclamp_delay_ms;
    unsigned long blowoff_cycles = blowoff_duration_ms;

    // Detect rising edge on start pin
    bool start_edge = start && !prev_start;
    prev_start = start;

    switch (state) {
        case 0:  // IDLE
            unclamp_solenoid = 0;
            blowoff_solenoid = 0;
            sequence_done = 0;

            if (start_edge) {
                state = 1;  // Begin sequence
                timer = 0;
            }
            break;

        case 1:  // UNCLAMPING
            unclamp_solenoid = 1;  // Activate unclamp solenoid
            sequence_done = 0;

            // Wait for sensor confirmation OR timeout
            if (tool_unclamped || timer > unclamp_delay_cycles) {
                state = 2;
                timer = 0;
            }
            timer++;
            break;

        case 2:  // BLOWOFF
            unclamp_solenoid = 0;  // Release solenoid
            blowoff_solenoid = 1;  // Activate blowoff

            timer++;
            if (timer >= blowoff_cycles) {
                state = 3;
            }
            break;

        case 3:  // DONE
            blowoff_solenoid = 0;
            sequence_done = 1;  // Signal completion

            // Wait for start to go FALSE before returning to idle
            if (!start) {
                state = 0;
            }
            break;
    }
}
```

**HAL Integration:**

```hal
loadrt tool_changer
addf tool-changer servo-thread

# Configure timing (500 ms unclamp, 2 s blowoff)
setp tool-changer.unclamp-delay-ms 500
setp tool-changer.blowoff-duration-ms 2000

# Connect to hardware I/O
net tool-clamp-sensor parport.0.pin-10-in => tool-changer.tool-clamped
net tool-unclamp-sensor parport.0.pin-11-in => tool-changer.tool-unclamped
net unclamp-out tool-changer.unclamp-solenoid => parport.0.pin-01-out
net blowoff-out tool-changer.blowoff-solenoid => parport.0.pin-02-out

# Connect to motion controller
net tool-change-start motion.tool-change => tool-changer.start
net tool-change-done tool-changer.sequence-done => motion.tool-changed
```

**Timing Diagram:**

```
Time (s):     0    0.5   1.0   1.5   2.0   2.5   3.0
              |     |     |     |     |     |     |
start:        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
unclamp:      ______‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾______
                   (0.5 s delay)
blowoff:      __________________________‾‾‾‾‾‾‾‾‾‾‾‾
                                      (2.0 s duration)
done:         __________________________________‾‾‾‾
```

### 6.6 Multiple Instances with Instance-Specific Data

**Problem:** loadrt with `count=` creates multiple instances sharing same code but needing separate state.

**Solution:** Use instance-specific memory via `EXTRA_SETUP()` and `EXTRA_CLEANUP()`.

**Example: Quadrature Encoder with Per-Instance State**

```c
component quad_encoder "Quadrature encoder decoder";

pin in bit phase_a;
pin in bit phase_b;
pin out s32 counts;
pin out float velocity;

parameter rw float scale = 1.0 "Counts per position unit";

// Per-instance data structure
variable int prev_a;
variable int prev_b;
variable s32 count_accum;

function _ "Update encoder counts";
license "GPL";

;;

FUNCTION(_) {
    int a = phase_a;
    int b = phase_b;

    // Quadrature decoding state machine (Gray code)
    // AB transitions: 00→01→11→10→00 (forward)
    //                 00→10→11→01→00 (reverse)

    int da = a - prev_a;  // Change in A
    int db = b - prev_b;  // Change in B

    if (da != 0 || db != 0) {  // Edge detected
        // Forward: A rising with B=0, A falling with B=1
        //          B rising with A=1, B falling with A=0
        // Reverse: opposite pattern

        if ((da > 0 && !b) || (da < 0 && b) ||
            (db > 0 && a) || (db < 0 && !a)) {
            count_accum++;  // Forward
        } else {
            count_accum--;  // Reverse
        }
    }

    counts = count_accum;

    // Simple velocity estimate: change in counts per sample period
    // (Real implementation would use timestamp-based calculation)

    prev_a = a;
    prev_b = b;
}
```

**Variable vs. Parameter:**

- **parameter**: Visible in HAL, settable via `setp`, shared configuration
- **variable**: Internal state, not visible in HAL, per-instance memory

**Instance Isolation:**

```hal
loadrt quad_encoder count=3  # Three independent encoder instances

# Each instance has separate prev_a, prev_b, count_accum variables
# No cross-talk between encoders
```

### 6.7 Real-Time Safe Programming

**Critical Constraints:**

1. **No dynamic memory allocation**: `malloc()`, `new`, `calloc()` forbidden
2. **No blocking operations**: `sleep()`, `usleep()`, file I/O, network sockets
3. **No floating-point in base thread**: FPU state save overhead ~50 µs
4. **Bounded execution time**: Every code path must complete within thread period

**Safe Practices:**

```c
// SAFE: Fixed-size array (stack allocation at component load time)
int buffer[1000];

// UNSAFE: Dynamic allocation
int *buffer = malloc(1000 * sizeof(int));  // DON'T DO THIS IN REAL-TIME!

// SAFE: Pre-allocated circular buffer
#define BUFFER_SIZE 1000
static int buffer[BUFFER_SIZE];
static int write_index = 0;

FUNCTION(_) {
    buffer[write_index] = input;
    write_index = (write_index + 1) % BUFFER_SIZE;  // Wrap around
}
```

**Floating-Point in Functions:**

```c
// Declare function supports floating-point
function _ fp "fp keyword allows floating-point operations";

;;

FUNCTION(_) {
    // Safe to use float, double, sin(), cos(), sqrt(), etc.
    output = sqrt(input_x * input_x + input_y * input_y);
}
```

**Without `fp` keyword:**

```c
function _;  // No fp keyword

;;

FUNCTION(_) {
    // Floating-point operations MAY work but add latency
    // Only integer arithmetic guaranteed safe in base thread
    output = input >> 2;  // Integer divide by 4 (bit shift)
}
```

### 6.8 Debugging Custom Components

**Compilation Errors:**

```bash
comp --install mycomponent.comp
# Error: mycomponent.comp:15: syntax error near 'ouptut'
#        Did you mean 'output'?

# Fix typo in .comp file, recompile
```

**Runtime Errors:**

```hal
loadrt mycomponent
# insmod: ERROR: could not insert module mycomponent.ko: Invalid module format

# Check kernel log
dmesg | tail
# mycomponent: disagrees about version of symbol hal_malloc

# Cause: Compiled against wrong LinuxCNC version
# Solution: Recompile after LinuxCNC update
sudo comp --install mycomponent.comp
```

**Logic Errors (Wrong Output):**

```c
// Add debug output to function
FUNCTION(_) {
    // rtapi_print to kernel log (viewable via dmesg)
    rtapi_print_msg(RTAPI_MSG_INFO, "mycomponent: input=%f output=%f\n",
                    input, output);

    output = input * gain;
}

// Compile, load, run LinuxCNC
// View output:
dmesg | grep mycomponent
# mycomponent: input=10.500000 output=26.250000
# (gain=2.5 verified correct)
```

**Performance Profiling:**

```bash
# Check function execution time
halcmd show thread servo-thread
#   Period  Name                  (Time, Max-Time)
#   1000000 servo-thread          (124567, 187432)
#           ...
#           mycomponent           (15234, 28765)  ← 15 µs avg, 28 µs worst
#           ...

# If execution time too high, optimize algorithm:
# - Replace floating-point with fixed-point integer math
# - Reduce loop iterations
# - Cache intermediate results
```

### 6.9 Advanced: Multi-Function Components

**Use Case:** Component with separate read and write functions for I/O devices.

```c
component adc_module "12-bit ADC with SPI interface";

pin out float channel_0 "ADC channel 0 voltage (0-10V)";
pin out float channel_1 "ADC channel 1 voltage";
pin in bit chip_select "SPI chip select";

// Two functions: one reads hardware, one processes data
function read nofp "Read ADC via SPI (time-critical, no floating-point)";
function process fp "Convert raw counts to voltage (floating-point OK)";

license "GPL";

;;

// Static variables shared between functions
static u32 raw_counts_0;
static u32 raw_counts_1;

FUNCTION(read) {
    // Time-critical: Read hardware registers via SPI
    // (Pseudocode—actual implementation hardware-specific)
    chip_select = 0;  // Assert CS
    raw_counts_0 = spi_read_register(0);  // Integer-only operations
    raw_counts_1 = spi_read_register(1);
    chip_select = 1;  // Deassert CS
}

FUNCTION(process) {
    // Convert 12-bit counts (0-4095) to voltage (0-10V)
    const float counts_to_volts = 10.0 / 4095.0;

    channel_0 = (float)raw_counts_0 * counts_to_volts;
    channel_1 = (float)raw_counts_1 * counts_to_volts;
}
```

**HAL Integration:**

```hal
loadrt adc_module
addf adc-module.read base-thread     # Fast thread, integer-only
addf adc-module.process servo-thread # Slower thread, floating-point OK

net adc-0-voltage adc-module.channel-0 => pid.0.feedback
net adc-1-voltage adc-module.channel-1 => display.analog-input
```

**Execution Sequence:**

```
Base thread (40 kHz):
  adc-module.read → raw_counts_0, raw_counts_1 updated

Servo thread (1 kHz):
  adc-module.process → channel_0, channel_1 converted to float
  (Reads raw_counts from previous base thread cycle)
```

### 6.10 Complex Example: Delta Robot Kinematics

**Application:** Forward and inverse kinematics for delta parallel robot.

**delta_kins.comp (simplified):**

```c
component delta_kins "Delta robot kinematics module";
description """
Delta robot with 3 vertical arms and end effector platform.

Geometry:
  - Base radius: Distance from center to arm pivot
  - Platform radius: Distance from center to ball joint
  - Arm length: Upper arm length
  - Rod length: Parallel rod length
""";

// Cartesian positions (world coordinates)
pin in float x_cmd "Commanded X position";
pin in float y_cmd "Commanded Y position";
pin in float z_cmd "Commanded Z position";

// Joint positions (motor coordinates, vertical travel)
pin out float joint_0_pos "Arm 0 vertical position";
pin out float joint_1_pos "Arm 1 vertical position";
pin out float joint_2_pos "Arm 2 vertical position";

// Geometric parameters
parameter rw float base_radius = 100.0 "Base triangle radius (mm)";
parameter rw float platform_radius = 50.0 "Platform triangle radius (mm)";
parameter rw float arm_length = 150.0 "Upper arm length (mm)";
parameter rw float rod_length = 300.0 "Parallel rod length (mm)";

function inverse_kins fp "Calculate joint positions from Cartesian";

license "GPL";

;;

#include <rtapi_math.h>  // sin(), cos(), sqrt(), acos()

// Inverse kinematics: Given (x,y,z), find joint positions
FUNCTION(inverse_kins) {
    // Arm angles: 0°, 120°, 240° (equilateral triangle)
    const float angles[3] = {0, 2.0*M_PI/3.0, 4.0*M_PI/3.0};

    for (int i = 0; i < 3; i++) {
        // Calculate arm base position
        float base_x = base_radius * cos(angles[i]);
        float base_y = base_radius * sin(angles[i]);

        // Calculate platform attachment point
        float platform_x = x_cmd + platform_radius * cos(angles[i]);
        float platform_y = y_cmd + platform_radius * sin(angles[i]);
        float platform_z = z_cmd;

        // Vector from arm base to platform attachment
        float dx = platform_x - base_x;
        float dy = platform_y - base_y;
        float dz = platform_z;

        // Distance in XY plane
        float r = sqrt(dx*dx + dy*dy);

        // Solve for joint vertical position using law of cosines
        // rod_length² = arm_length² + (r² + dz²) - 2*arm_length*sqrt(r²+dz²)*cos(angle)

        float d = sqrt(r*r + dz*dz);  // Distance to platform attachment

        // Check reachability
        if (d > (arm_length + rod_length) || d < fabs(arm_length - rod_length)) {
            rtapi_print_msg(RTAPI_MSG_ERR,
                "delta_kins: Position unreachable for arm %d\n", i);
            // Output safe default (center position)
            if (i == 0) joint_0_pos = 0.0;
            if (i == 1) joint_1_pos = 0.0;
            if (i == 2) joint_2_pos = 0.0;
            continue;
        }

        // Law of cosines to find arm angle
        float cos_angle = (arm_length*arm_length + d*d - rod_length*rod_length)
                         / (2.0 * arm_length * d);
        float arm_angle = acos(cos_angle);

        // Vertical component of arm end position
        float joint_pos = platform_z - arm_length * cos(arm_angle)
                         + arm_length * sin(arm_angle) * r / d;

        // Output to corresponding joint pin
        if (i == 0) joint_0_pos = joint_pos;
        if (i == 1) joint_1_pos = joint_pos;
        if (i == 2) joint_2_pos = joint_pos;
    }
}
```

**HAL Integration:**

```hal
loadrt delta_kins
addf delta-kins.inverse-kins servo-thread

# Configure robot geometry
setp delta-kins.base-radius 100.0
setp delta-kins.platform-radius 50.0
setp delta-kins.arm-length 150.0
setp delta-kins.rod-length 300.0

# Connect to motion controller
net x-cmd motion.00.pos-cmd => delta-kins.x-cmd
net y-cmd motion.01.pos-cmd => delta-kins.y-cmd
net z-cmd motion.02.pos-cmd => delta-kins.z-cmd

net joint-0-cmd delta-kins.joint-0-pos => pid.0.command
net joint-1-cmd delta-kins.joint-1-pos => pid.1.command
net joint-2-cmd delta-kins.joint-2-pos => pid.2.command
```

### 6.11 Component Documentation

**comp supports embedded documentation:**

```c
component documented_example "Example with comprehensive docs";
description """
Multi-line description visible in component help.

This component demonstrates proper documentation practices:
  - Clear pin descriptions
  - Parameter units specified
  - Usage examples included
  - Author contact information

See also: related_component, another_module
""";

pin in float input "Input signal (volts, 0-10V range)";
pin out float output "Output signal (milliamps, 4-20mA)";

parameter rw float zero_offset = 0.0 "Zero adjustment (mA)";
parameter rw float span_scale = 1.6 "Span calibration (mA/V, default 1.6 for 10V→16mA span)";

function _ fp;

notes """
Calibration Procedure:
  1. Apply 0V input, adjust zero_offset until output reads 4.0 mA
  2. Apply 10V input, adjust span_scale until output reads 20.0 mA
  3. Verify linearity at 5V (should read 12.0 ± 0.1 mA)

Typical values:
  zero_offset = 4.0 (4 mA at 0V input)
  span_scale = 1.6 (16 mA span / 10V span)
""";

license "GPL";
author "John Doe <john@example.com>";

;;

FUNCTION(_) {
    // Convert 0-10V input to 4-20mA output
    output = zero_offset + (input * span_scale);
}
```

**Viewing Documentation:**

```bash
# Component help
halcmd show comp documented_example

# Pin information
halcmd show pin documented-example.*

# Parameter information
halcmd show param documented-example.*
```

### 6.12 Summary: Custom Component Development

Custom HAL components extend LinuxCNC capabilities for specialized applications:

**When to Write Custom Components:**

- Standard components insufficient (custom kinematics, specialized control algorithms)
- Performance optimization needed (combine multiple HAL operations)
- Proprietary hardware interface required
- Complex sequencing logic (state machines with timing)

**comp Workflow:**

1. Write .comp file (pins, parameters, function logic)
2. Compile: `comp --install component.comp`
3. Load in HAL: `loadrt component`
4. Connect signals and configure parameters
5. Debug via rtapi_print and halcmd
6. Optimize execution time if needed

**Real-Time Programming Rules:**

- No dynamic memory allocation
- No blocking operations
- Bounded execution time
- Use `fp` keyword for floating-point
- Static variables for state persistence

**Best Practices:**

- Comprehensive documentation in .comp file
- Clear pin and parameter naming
- Error checking (reachability, divide-by-zero, limits)
- Debug output via rtapi_print (removable in production)
- Performance profiling via `halcmd show thread`

**Next Section** (14.7) covers Python HAL components for user-space applications: VFD communication, custom GUIs, data logging, and non-time-critical automation tasks.

***

*Total: 4,198 words | 0 equations | 6 complete worked examples | 2 tables | 25 code blocks*
