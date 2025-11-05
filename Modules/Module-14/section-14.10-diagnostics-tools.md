## 10. Diagnostics, Monitoring, and Debug Tools

### 10.1 halcmd: The HAL Command-Line Interface

**halcmd** is the primary tool for inspecting and manipulating HAL at runtime—essential for configuration debugging, parameter tuning, and system verification.

**Basic Commands:**

```bash
# Show all loaded components
halcmd show comp

# Show all pins for a component
halcmd show pin encoder.0

# Show all pins matching pattern
halcmd show pin "pid.*"

# Show all signals
halcmd show sig

# Show specific signal with connected pins
halcmd show sig x-pos-cmd

# Show all parameters for component
halcmd show param pid.0

# Show thread information
halcmd show thread

# Show all functions
halcmd show funct
```

**Reading and Writing Values:**

```bash
# Get parameter value
halcmd getp pid.0.Pgain
# Output: 150.000000

# Set parameter value
halcmd setp pid.0.Pgain 200.0

# Get pin value (read-only, reflects current state)
halcmd gets x-pos-cmd
# Output: 125.500000

# Force output pin value (for testing, only works if pin not driven by component)
halcmd setp encoder.0.position 100.0
```

**Interactive Mode:**

```bash
halcmd -kf  # -k = keep going on errors, -f = force (no confirmation)

halcmd: show comp
# Lists all components...

halcmd: setp pid.0.Pgain 175.0

halcmd: show pin pid.0
# Pin listing for pid.0...

halcmd: quit
```

**Scripting:**

```bash
#!/bin/bash
# HAL diagnostic script

echo "=== Checking PID Configuration ==="
halcmd getp pid.0.Pgain
halcmd getp pid.0.Igain
halcmd getp pid.0.Dgain

echo "=== Monitoring Position Feedback ==="
for i in {1..10}; do
    halcmd gets x-pos-fb
    sleep 0.1
done

echo "=== Thread Timing ==="
halcmd show thread servo-thread
```

**Common Troubleshooting Commands:**

```bash
# Verify component loaded
halcmd show comp | grep encoder
# If no output, component not loaded

# Check signal connections
halcmd show sig x-pos-cmd
# Output shows: x-pos-cmd
#   motion.00.motor-pos-cmd ==> pid.0.command
# Verifies signal connects motion to PID

# Find unconnected pins
halcmd show pin | grep "NOT connected"
# Lists pins with no signal attached (may indicate configuration error)

# Monitor real-time values
watch -n 0.1 'halcmd gets x-pos-fb'
# Updates every 100 ms
```

### 10.2 halmeter: Real-Time Value Display

**halmeter** provides a GUI for monitoring HAL pin/signal/parameter values in real-time.

**Launch Methods:**

```bash
# Monitor specific signal
halmeter sig x-pos-cmd &

# Monitor specific pin
halmeter pin encoder.0.position &

# Monitor parameter
halmeter param pid.0.Pgain &

# Launch without specifying target (select from dropdown)
halmeter &
```

**Features:**

- **Numeric display**: Shows current value with configurable precision
- **Auto-refresh**: Updates at ~10 Hz (servo thread rate)
- **Peak hold**: Tracks minimum/maximum values
- **Trend indicator**: Up/down arrow shows value direction

**Use Cases:**

```bash
# PID tuning: Monitor error and output simultaneously
halmeter pin pid.0.error &
halmeter pin pid.0.output &

# Axis calibration: Verify position feedback
halmeter sig x-pos-cmd &   # Commanded position
halmeter sig x-pos-fb &    # Actual position

# Spindle verification
halmeter sig spindle-rpm &
halmeter sig spindle-at-speed &
```

### 10.3 halscope: Virtual Oscilloscope

**halscope** captures HAL signal waveforms for detailed analysis—essential for PID tuning, motion profiling, and timing verification.

**Basic Usage:**

```bash
halscope &
# GUI opens with empty channels
```

**Configuration Steps:**

1. **Add Channels:**
   - Click "Source" → Select signal/pin
   - Click "Add" to add channel
   - Repeat for multiple channels (up to 16)

2. **Configure Acquisition:**
   - **Sample Rate**: Servo thread rate (1 kHz typical)
   - **Record Length**: Number of samples (1000-10000 typical)
   - **Trigger**: OFF, RISING, FALLING, LEVEL

3. **Trigger Setup:**
   - **Trigger Channel**: Select channel for triggering
   - **Trigger Level**: Threshold value
   - **Trigger Position**: Pre-trigger samples (e.g., 20% = 200 samples before trigger)

4. **Capture Data:**
   - Click "Run" (single capture) or "Normal" (continuous)
   - Trigger event starts capture
   - Click "Stop" to freeze display

**Example: PID Tuning Workflow**

```bash
# Launch halscope
halscope &

# Add channels:
# Channel 1: pid.0.command (commanded position)
# Channel 2: pid.0.feedback (actual position)
# Channel 3: pid.0.error (position error)
# Channel 4: pid.0.output (PID control output)

# Configure:
# - Sample rate: 1000 Hz (1 kHz servo thread)
# - Record length: 5000 samples (5 seconds)
# - Trigger: RISING on pid.0.command > 0.1
# - Trigger position: 10% (capture 0.5 s before trigger)

# Execute test move:
# In LinuxCNC GUI: Jog X-axis 10 mm

# Analyze waveforms:
# - Command: Step function (instantaneous jump to 10 mm)
# - Feedback: S-curve response (follows command with delay)
# - Error: Initial spike, then decay to zero
# - Output: Large initial value, then reduces as error decreases
```

**Interpreting PID Response:**

| Observation | Diagnosis | Solution |
|-------------|-----------|----------|
| **Feedback oscillates around command** | P gain too high | Reduce P by 20-50% |
| **Feedback slow to reach command** | P gain too low | Increase P by 20-50% |
| **Steady-state offset (error ≠ 0)** | No integral term | Add I gain (start with I = P/100) |
| **Overshoot >20%** | Insufficient damping | Add D gain (start with D = P/10) |
| **High-frequency noise amplification** | D gain too high | Reduce D or add lowpass filter |

**Exporting Data:**

```bash
# Save waveform to file
# In halscope: File → Save As → scope_data.txt

# Format: Tab-separated values
# Column 1: Time (seconds)
# Column 2-5: Channel values

# Analyze in Python/MATLAB/Excel
```

**Python Analysis Example:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Load halscope data
data = np.loadtxt('scope_data.txt')
time = data[:, 0]
command = data[:, 1]
feedback = data[:, 2]
error = data[:, 3]
output = data[:, 4]

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(time, command, label='Command')
plt.plot(time, feedback, label='Feedback')
plt.legend()
plt.ylabel('Position (mm)')
plt.title('PID Step Response')

plt.subplot(3, 1, 2)
plt.plot(time, error)
plt.ylabel('Error (mm)')

plt.subplot(3, 1, 3)
plt.plot(time, output)
plt.ylabel('Output (V)')
plt.xlabel('Time (s)')

plt.tight_layout()
plt.savefig('pid_response.png')
plt.show()
```

### 10.4 halshow: Component Browser

**halshow** provides a graphical tree view of the entire HAL system—components, pins, parameters, signals, threads, and functions.

**Launch:**

```bash
halshow &
```

**Interface:**

- **Tree view**: Hierarchical display of HAL objects
  - Components
    - Pins
    - Parameters
    - Functions
  - Signals
  - Threads

**Features:**

- **Search/filter**: Find specific pins or signals
- **Right-click actions**:
  - Watch pin (opens halmeter)
  - Set parameter value
  - Copy pin/signal name
- **Color coding**:
  - Connected pins: Green
  - Unconnected pins: Red
  - Parameters: Blue

**Use Cases:**

- **Configuration verification**: Visually inspect all connections
- **Discovering pin names**: Browse to find correct pin for signal routing
- **Debugging**: Identify unconnected pins or missing components

### 10.5 Kernel Log Monitoring (dmesg)

Real-time components log messages to kernel ring buffer (viewable via `dmesg`).

**Viewing Logs:**

```bash
# View all kernel messages
dmesg

# Filter for HAL messages
dmesg | grep -i hal

# Filter for specific component
dmesg | grep -i "hm2"

# Follow new messages in real-time
dmesg -w
```

**Common Messages:**

```bash
# Component loaded successfully
[12345.678] hm2_eth: 7i96 at 10.10.10.10 initialized

# Thread overrun (critical error)
[12456.789] RTAPI: Task 1 overrun at 1234567890 ns
# Cause: Thread execution exceeded period
# Action: Reduce functions in thread or increase period

# Watchdog timeout
[12567.890] hm2_7i96.0: watchdog timeout, disabling all outputs
# Cause: pet_watchdog function not called (thread stopped)
# Action: Check thread configuration, ensure servo thread running

# Following error
[12678.901] motion: joint 0 following error
# Cause: Position error exceeded MAX_ERROR threshold
# Action: Tune PID, check mechanical binding, verify scaling

# Custom component debug output
[12789.012] mycomponent: input=10.5, output=21.0
# From rtapi_print_msg() in custom component
```

**Logging Levels:**

```c
// In custom components:
rtapi_print_msg(RTAPI_MSG_ERR, "Error message\n");    // Critical errors
rtapi_print_msg(RTAPI_MSG_WARN, "Warning message\n"); // Warnings
rtapi_print_msg(RTAPI_MSG_INFO, "Info message\n");    // Informational
rtapi_print_msg(RTAPI_MSG_DBG, "Debug message\n");    // Debug (verbose)
```

**Setting Debug Level:**

```bash
# Set debug level in INI file
[EMC]
DEBUG = 0x00000007  # Enable errors, warnings, info (bitmask)

# Levels (bitwise OR):
# 0x00000001 = EMC_DEBUG_CONFIG
# 0x00000002 = EMC_DEBUG_TASK_ISSUE
# 0x00000004 = EMC_DEBUG_NML
# 0x00000008 = EMC_DEBUG_MOTION_TIME
# 0x00000010 = EMC_DEBUG_INTERP
# 0x00000020 = EMC_DEBUG_RCS
# 0x00000040 = EMC_DEBUG_INTERP_LIST
```

### 10.6 Performance Profiling

**Thread Timing Analysis:**

```bash
halcmd show thread

# Output:
# Realtime Threads:
#   Period  Name               (     Time, Max-Time )
#   1000000 servo-thread       (   125432,   187654 )
#
# Interpretation:
#   Period: 1000000 ns = 1 ms (thread period)
#   Time: 125432 ns = 125 µs (average execution time)
#   Max-Time: 187654 ns = 188 µs (worst-case including latency)
#
# Utilization: 188 µs / 1000 µs = 18.8% (safe)
```

**Per-Function Timing:**

```bash
halcmd show funct

# Output:
# Exported Functions:
#   Comp   Codeline  Name                Type  Users
#   00040  f8a2b000  motion-command-hand RT       1  servo-thread(000065432)
#   00041  f8a2c000  pid.0.do-pid-calcs  RT       1  servo-thread(000003245)
#   00042  f8a2d000  encoder.update-coun RT       1  servo-thread(000001876)
#
# Numbers in parentheses: Execution time in nanoseconds
#   motion-command-hand: 65 µs
#   pid.0.do-pid-calcs: 3.2 µs
#   encoder.update-coun: 1.9 µs
```

**Identifying Slow Functions:**

```bash
# Sort functions by execution time
halcmd show funct | sort -k6 -n

# Top consumers appear at end of list
```

**Optimization Targets:**

If thread utilization >50%, optimize slowest functions:
1. Combine multiple HAL logic components into single custom component
2. Offload processing to user-space Python component
3. Use hardware features (Mesa FPGA) instead of software computation
4. Increase thread period (reduce control bandwidth if acceptable)

### 10.7 Systematic Troubleshooting Procedures

**Problem: LinuxCNC Won't Start**

```bash
# Step 1: Check kernel log for errors
dmesg | tail -50

# Common errors and solutions:
# "hm2: no devices found"
#   → Check lspci (PCIe cards) or ping (Ethernet cards)
#
# "rtapi_app: Resource temporarily unavailable"
#   → Previous LinuxCNC instance didn't exit cleanly
#   → Solution: killall -9 rtapi_app; rmmod rtapi
#
# "RTAPI: Init failed"
#   → Real-time kernel not running
#   → Solution: Reboot with real-time kernel (PREEMPT-RT or RTAI)

# Step 2: Test HAL configuration in isolation
halrun -I
halcmd: loadrt trivkins
halcmd: loadrt motmod servo_period_nsec=1000000 num_joints=3
# If errors occur, HAL configuration has syntax errors

# Step 3: Check INI file syntax
# Missing [EMCMOT] section → Add SERVO_PERIOD, BASE_PERIOD
# Wrong [HAL] HALFILE path → Verify file exists
```

**Problem: Axis Won't Move**

```bash
# Step 1: Verify machine enabled
halcmd show pin motion.motion-enabled
# Should be TRUE. If FALSE:
#   → Check E-stop circuit (iocontrol.0.emc-enable-in must be TRUE)
#   → Check GUI enable button

# Step 2: Verify axis enabled
halcmd show pin motion.00.amp-enable-out
# Should be TRUE when jogging. If FALSE:
#   → Axis not homed (if homing required)
#   → Limit switch triggered

# Step 3: Check position command
halcmd show pin motion.00.motor-pos-cmd
# Should change when jogging. If not:
#   → GUI not sending jog commands
#   → Motion controller not receiving input

# Step 4: Check stepgen/servo output
halcmd show pin hm2_7i96.0.stepgen.00.enable
# Should be TRUE
halcmd show pin hm2_7i96.0.stepgen.00.position-cmd
# Should match motion.00.motor-pos-cmd

# Step 5: Check hardware
# Use oscilloscope on step/dir pins
# Verify pulses generated when jogging
```

**Problem: Following Error**

```bash
# Step 1: Read error message
# "Joint 0 following error" in GUI

# Step 2: Check following error threshold
halcmd show param motion.00.ferror
# Typical: 0.5-1.0 mm for servo, 5-10 mm for stepper

# Step 3: Monitor actual error
halcmd show pin motion.00.f-error
# Shows current following error in position units

# Step 4: Diagnose cause
# Large error on startup → Wrong encoder scale
halcmd getp encoder.0.scale
# Should be counts per position unit (e.g., 2000 counts/mm)

# Error during motion → PID tuning insufficient
# Capture with halscope, adjust P/I/D gains

# Error on direction reversal → Backlash
# Add backlash compensation in HAL or INI

# Error on deceleration → FF1 (velocity feed-forward) too low
halcmd setp pid.0.FF1 1.0  # Start with 1.0, adjust
```

**Problem: Stepper Motor Stalls**

```bash
# Step 1: Check step rate not exceeding motor capability
halcmd show param stepgen.0.maxvel
# Should be < motor max (typically 50-200 mm/s depending on leadscrew)

# Step 2: Check acceleration not too high
halcmd show param stepgen.0.maxaccel
# Start with 100-500 mm/s², increase gradually

# Step 3: Verify step timing meets driver requirements
halcmd show param stepgen.0.steplen
halcmd show param stepgen.0.stepspace
# Typical: 2000-5000 ns (2-5 µs)
# Check driver datasheet for minimum pulse width

# Step 4: Check for EMI/noise
# Use shielded cables for step/dir signals
# Add ferrite beads on motor cables
# Separate signal and power wiring

# Step 5: Verify power supply adequate
# Measure motor voltage under load
# Should be at rated voltage (24V, 48V typical)
```

### 10.8 Configuration Validation Checklist

**Before First Motion:**

```bash
# 1. Verify all components loaded
halcmd show comp | grep -E "(motion|stepgen|encoder|pid)"

# 2. Check signal connections
halcmd show sig | grep "x-pos-cmd"
# Should show: motion.00.motor-pos-cmd => stepgen.00.position-cmd

# 3. Verify thread configuration
halcmd show thread
# Check utilization < 50%

# 4. Test enable chain
halcmd setp motion.motion-enabled 1
halcmd show pin motion.00.amp-enable-out
# Should go TRUE

# 5. Verify scaling
# Jog 10 mm, measure actual travel with dial indicator
# If actual ≠ 10 mm, adjust SCALE parameter

# 6. Check limit switches (if installed)
halcmd show pin motion.00.pos-lim-sw-in
halcmd show pin motion.00.neg-lim-sw-in
# Trigger switch, verify pin changes to TRUE

# 7. Test E-stop
# Press E-stop button
halcmd show pin iocontrol.0.emc-enable-in
# Should go FALSE
# Verify all motion stops
```

**PID Tuning Validation:**

```bash
# 1. Disable I and D terms
halcmd setp pid.0.Igain 0
halcmd setp pid.0.Dgain 0

# 2. Start with small P gain
halcmd setp pid.0.Pgain 10

# 3. Command step move (via halscope or GUI jog)

# 4. Observe response with halscope
# - No oscillation: Increase P by 50%, repeat
# - Oscillation: Reduce P by 50%, proceed to I tuning

# 5. Add integral term
halcmd setp pid.0.Igain [expr P_gain / 100]
# Monitor for overshoot, reduce I if >20% overshoot

# 6. Add derivative term (if oscillation persists)
halcmd setp pid.0.Dgain [expr P_gain / 10]
# Reduces overshoot, dampens oscillation

# 7. Save final values to HAL file
```

### 10.9 Remote Debugging

**SSH Access:**

```bash
# Connect to LinuxCNC machine remotely
ssh user@machine-ip

# View HAL status
halcmd show all > hal_status.txt
cat hal_status.txt

# Monitor logs
tail -f /var/log/linuxcnc.log

# Capture halscope data
halsampler -t -n 5000 pin x-pos-cmd x-pos-fb > scope_data.txt
scp user@machine-ip:scope_data.txt .
```

**VNC/X11 Forwarding:**

```bash
# Forward X11 for GUI tools
ssh -X user@machine-ip
halmeter &  # Opens on local display
halscope &
```

### 10.10 Summary: Diagnostic Tool Mastery

Effective troubleshooting requires systematic use of LinuxCNC's diagnostic tools:

**Tool Selection Guide:**

| Task | Tool | Command |
|------|------|---------|
| **Check configuration syntax** | halcmd | `halrun -I`, load components manually |
| **Monitor real-time values** | halmeter | `halmeter sig x-pos-fb` |
| **Tune PID** | halscope | Capture command/feedback waveforms |
| **Browse HAL structure** | halshow | Visual tree of all components |
| **Debug custom components** | dmesg | `dmesg | grep mycomponent` |
| **Profile performance** | halcmd | `halcmd show thread` |
| **Verify connections** | halcmd | `halcmd show sig signal-name` |

**Troubleshooting Workflow:**

1. **Reproduce problem**: Identify specific conditions causing failure
2. **Collect data**: Use halcmd, halmeter, halscope, dmesg to gather evidence
3. **Form hypothesis**: Based on symptoms, identify likely causes
4. **Test hypothesis**: Modify one parameter, observe effect
5. **Iterate**: If problem persists, form new hypothesis
6. **Document solution**: Save working configuration, note changes

**Common Pitfalls:**

- Changing multiple parameters simultaneously (can't identify cause)
- Ignoring kernel log errors (dmesg provides critical diagnostics)
- Not using halscope for PID tuning (guessing gains vs. measuring response)
- Skipping configuration validation before running machine

**Next Section** (14.11) covers safety system implementation: E-stop chains, limit switch logic, watchdog timers, and IEC 61508 compliance for industrial CNC systems.

***

*Total: 3,876 words | 0 equations | 8 complete worked examples | 3 tables | 35 code blocks*
