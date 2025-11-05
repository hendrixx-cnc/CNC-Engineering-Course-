## 7. Python HAL Components and User-Space Integration

### 7.1 User-Space Components: When Python Makes Sense

Python HAL components execute as normal Linux processes (not real-time kernel modules), making them ideal for:

- **VFD communication**: Modbus RTU/TCP, RS-485, proprietary protocols
- **Custom user interfaces**: PyVCP panels, Glade/GTK GUIs, touchscreen controls
- **Data logging**: Recording HAL signals to CSV, database, network
- **Complex logic**: Decision trees, lookup tables, web API integration
- **Hardware interfaces**: USB devices, network-connected sensors, Arduino communication
- **Development/prototyping**: Rapid iteration without kernel module compilation

**User-Space vs. Real-Time Trade-Offs:**

| Criterion | Real-Time (C comp) | User-Space (Python) |
|-----------|-------------------|---------------------|
| **Latency** | <1 ms deterministic | 1-100 ms variable |
| **Development time** | Hours (compile, test, debug) | Minutes (edit, run) |
| **Crash impact** | Kernel panic (system halt) | Process crash (LinuxCNC continues) |
| **API access** | HAL only | Full Linux (file I/O, network, USB) |
| **Suitable for** | Motion control, step generation, PID | VFD control, UI, logging, preprocessing |

### 7.2 Python HAL Module API

The `hal` Python module provides HAL integration for user-space components.

**Basic Component Structure:**

```python
#!/usr/bin/env python3
import hal
import time

# Create component
h = hal.component("mycomponent")

# Add pins
h.newpin("input", hal.HAL_FLOAT, hal.HAL_IN)
h.newpin("output", hal.HAL_FLOAT, hal.HAL_OUT)

# Add parameters
h.newparam("gain", hal.HAL_FLOAT, hal.HAL_RW)
h["gain"] = 1.0  # Set default value

# Signal component ready
h.ready()

try:
    while True:
        # Read input pin
        input_value = h["input"]

        # Read parameter
        gain_value = h["gain"]

        # Compute output
        h["output"] = input_value * gain_value

        # Sleep to avoid 100% CPU usage
        time.sleep(0.01)  # 10 ms = 100 Hz update rate

except KeyboardInterrupt:
    pass  # Exit cleanly on Ctrl+C
```

**Running:**

```bash
# Make executable
chmod +x mycomponent.py

# Run (keeps running until Ctrl+C)
./mycomponent.py &

# Component now appears in HAL
halcmd show comp mycomponent
```

**Pin/Parameter Types:**

```python
# Pin types
hal.HAL_BIT    # Boolean (True/False, 0/1)
hal.HAL_FLOAT  # 64-bit floating-point
hal.HAL_S32    # 32-bit signed integer
hal.HAL_U32    # 32-bit unsigned integer

# Pin directions
hal.HAL_IN     # Input pin (component reads)
hal.HAL_OUT    # Output pin (component writes)
hal.HAL_IO     # Bidirectional (rare)

# Parameter access modes
hal.HAL_RO     # Read-only
hal.HAL_RW     # Read-write
```

### 7.3 Complete Example: Modbus VFD Controller

**Application:** Control Variable Frequency Drive (spindle motor controller) via Modbus RTU serial protocol.

**modbus_vfd.py:**

```python
#!/usr/bin/env python3
"""
Modbus VFD HAL component
Controls spindle via Modbus RTU (RS-485)

Tested with Huanyang HY-series VFDs
"""

import hal
import time
import serial
import struct

class ModbusVFD:
    def __init__(self, port="/dev/ttyUSB0", slave_id=1, baudrate=9600):
        self.h = hal.component("modbus-vfd")

        # Input pins (commands from LinuxCNC)
        self.h.newpin("speed-cmd", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("enable", hal.HAL_BIT, hal.HAL_IN)
        self.h.newpin("forward", hal.HAL_BIT, hal.HAL_IN)  # True=forward, False=reverse

        # Output pins (feedback to LinuxCNC)
        self.h.newpin("speed-fb", hal.HAL_FLOAT, hal.HAL_OUT)
        self.h.newpin("at-speed", hal.HAL_BIT, hal.HAL_OUT)
        self.h.newpin("fault", hal.HAL_BIT, hal.HAL_OUT)
        self.h.newpin("comm-ok", hal.HAL_BIT, hal.HAL_OUT)

        # Parameters
        self.h.newparam("max-rpm", hal.HAL_FLOAT, hal.HAL_RW)
        self.h["max-rpm"] = 24000.0  # VFD maximum RPM

        self.h.newparam("at-speed-tolerance", hal.HAL_FLOAT, hal.HAL_RW)
        self.h["at-speed-tolerance"] = 50.0  # ±50 RPM tolerance

        self.h.newparam("poll-interval", hal.HAL_FLOAT, hal.HAL_RW)
        self.h["poll-interval"] = 0.1  # Poll VFD every 100 ms

        self.h.ready()

        # Open serial port
        try:
            self.ser = serial.Serial(
                port=port,
                baudrate=baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=0.1
            )
            print(f"Modbus VFD: Connected to {port}")
        except Exception as e:
            print(f"Modbus VFD: Failed to open {port}: {e}")
            self.ser = None

        self.slave_id = slave_id
        self.last_poll_time = 0
        self.comm_error_count = 0

    def modbus_crc(self, data):
        """Calculate Modbus RTU CRC16"""
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return crc

    def write_register(self, register, value):
        """Modbus function 0x06: Write single register"""
        if not self.ser:
            return False

        # Build request: slave_id, function, reg_hi, reg_lo, val_hi, val_lo
        request = struct.pack('>BBHH', self.slave_id, 0x06, register, value)
        crc = self.modbus_crc(request)
        request += struct.pack('<H', crc)

        try:
            self.ser.write(request)
            response = self.ser.read(8)  # Response same size as request

            if len(response) == 8:
                # Verify CRC
                recv_crc = struct.unpack('<H', response[-2:])[0]
                calc_crc = self.modbus_crc(response[:-2])
                if recv_crc == calc_crc:
                    self.comm_error_count = 0
                    return True

            self.comm_error_count += 1
            return False

        except Exception as e:
            print(f"Modbus write error: {e}")
            self.comm_error_count += 1
            return False

    def read_register(self, register):
        """Modbus function 0x03: Read holding register"""
        if not self.ser:
            return None

        # Build request: slave_id, function, reg_hi, reg_lo, count_hi, count_lo
        request = struct.pack('>BBHH', self.slave_id, 0x03, register, 1)
        crc = self.modbus_crc(request)
        request += struct.pack('<H', crc)

        try:
            self.ser.write(request)
            response = self.ser.read(7)  # Response: addr, func, count, data_hi, data_lo, crc_lo, crc_hi

            if len(response) == 7:
                recv_crc = struct.unpack('<H', response[-2:])[0]
                calc_crc = self.modbus_crc(response[:-2])
                if recv_crc == calc_crc:
                    value = struct.unpack('>H', response[3:5])[0]
                    self.comm_error_count = 0
                    return value

            self.comm_error_count += 1
            return None

        except Exception as e:
            print(f"Modbus read error: {e}")
            self.comm_error_count += 1
            return None

    def update(self):
        """Main update loop"""
        now = time.time()

        # Read commands from HAL pins
        enable = self.h["enable"]
        speed_cmd = self.h["speed-cmd"]
        forward = self.h["forward"]
        max_rpm = self.h["max-rpm"]

        # Write command to VFD
        if enable:
            # Scale speed_cmd (0-max_rpm) to VFD register value (0-10000 = 0-100% frequency)
            freq_percent = (abs(speed_cmd) / max_rpm) * 100.0
            freq_scaled = int(freq_percent * 100)  # 0-10000 range
            freq_scaled = max(0, min(10000, freq_scaled))  # Clamp

            # Write frequency setpoint (register 0x2000 typical for HY VFDs)
            self.write_register(0x2000, freq_scaled)

            # Write run command (register 0x2001: 1=forward, 2=reverse)
            run_cmd = 1 if forward else 2
            self.write_register(0x2001, run_cmd)
        else:
            # Stop VFD
            self.write_register(0x2001, 0)

        # Poll feedback at specified interval
        if now - self.last_poll_time > self.h["poll-interval"]:
            self.last_poll_time = now

            # Read actual speed (register 0x200A typical)
            speed_reg = self.read_register(0x200A)
            if speed_reg is not None:
                # Scale register value (0-10000) to RPM
                actual_rpm = (speed_reg / 100.0) * max_rpm / 100.0
                self.h["speed-fb"] = actual_rpm

                # Check if at speed
                speed_error = abs(actual_rpm - abs(speed_cmd))
                self.h["at-speed"] = (speed_error < self.h["at-speed-tolerance"]) and enable

            # Read fault status (register 0x8000 typical)
            fault_reg = self.read_register(0x8000)
            if fault_reg is not None:
                self.h["fault"] = (fault_reg != 0)

        # Communication status
        self.h["comm-ok"] = (self.comm_error_count < 5)

    def run(self):
        """Main loop"""
        try:
            while True:
                self.update()
                time.sleep(0.01)  # 100 Hz update rate
        except KeyboardInterrupt:
            # Stop VFD on exit
            if self.ser:
                self.write_register(0x2001, 0)
                self.ser.close()
            print("\nModbus VFD: Shutdown")

if __name__ == "__main__":
    import sys

    # Parse command-line arguments
    port = sys.argv[1] if len(sys.argv) > 1 else "/dev/ttyUSB0"
    slave_id = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    vfd = ModbusVFD(port=port, slave_id=slave_id)
    vfd.run()
```

**HAL Integration:**

```hal
# Load Python component (runs in background)
loadusr -W modbus_vfd.py /dev/ttyUSB0 1
# -W waits for component ready before continuing

# Configure parameters
setp modbus-vfd.max-rpm 24000
setp modbus-vfd.at-speed-tolerance 100.0
setp modbus-vfd.poll-interval 0.1

# Connect spindle control
net spindle-enable motion.spindle-on => modbus-vfd.enable
net spindle-speed-cmd motion.spindle-speed-out => modbus-vfd.speed-cmd
net spindle-forward motion.spindle-forward => modbus-vfd.forward

# Connect feedback
net spindle-speed-fb modbus-vfd.speed-fb => motion.spindle-speed-in
net spindle-at-speed modbus-vfd.at-speed => motion.spindle-at-speed

# Fault indication
net vfd-fault modbus-vfd.fault => halui.program.pause
net vfd-comm-ok modbus-vfd.comm-ok => pyvcp.led-comm-ok
```

**Usage in G-code:**

```gcode
M3 S12000   ; Start spindle forward at 12,000 RPM
M4 S6000    ; Start spindle reverse at 6,000 RPM
M5          ; Stop spindle
```

### 7.4 PyVCP: Python Virtual Control Panel

PyVCP creates custom control panels in XML, automatically generating HAL pins.

**Example: Simple Jog Panel**

**pyvcp_panel.xml:**

```xml
<?xml version="1.0"?>
<pyvcp>
    <vbox>
        <relief>RIDGE</relief>
        <bd>3</bd>

        <!-- Title -->
        <label>
            <text>"Machine Control Panel"</text>
            <font>("Helvetica",16,"bold")</font>
        </label>

        <!-- Spindle Speed Display -->
        <labelframe text="Spindle">
            <hbox>
                <label>
                    <text>"Speed (RPM):"</text>
                </label>
                <number>
                    <halpin>"spindle-speed"</halpin>
                    <font>("Helvetica",14)</font>
                    <format>"+5.0f"</format>
                </number>
            </hbox>

            <!-- At-speed LED indicator -->
            <hbox>
                <label>
                    <text>"At Speed:"</text>
                </label>
                <led>
                    <halpin>"spindle-at-speed-led"</halpin>
                    <size>30</size>
                    <on_color>"green"</on_color>
                    <off_color>"red"</off_color>
                </led>
            </hbox>
        </labelframe>

        <!-- Jog Controls -->
        <labelframe text="Jog X-Axis">
            <hbox>
                <button>
                    <halpin>"jog-x-minus"</halpin>
                    <text>"X-"</text>
                    <width>3</width>
                </button>

                <button>
                    <halpin>"jog-x-plus"</halpin>
                    <text>"X+"</text>
                    <width>3</width>
                </button>
            </hbox>
        </labelframe>

        <!-- Jog Speed Slider -->
        <labelframe text="Jog Speed">
            <scale>
                <halpin>"jog-speed"</halpin>
                <resolution>1</resolution>
                <orient>HORIZONTAL</orient>
                <min_>0</min_>
                <max_>100</max_>
            </scale>
        </labelframe>

        <!-- Position Display -->
        <labelframe text="Position (mm)">
            <table>
                <tablerow>
                    <label><text>"X:"</text></label>
                    <number>
                        <halpin>"x-pos"</halpin>
                        <format>"+4.3f"</format>
                    </number>
                </tablerow>
                <tablerow>
                    <label><text>"Y:"</text></label>
                    <number>
                        <halpin>"y-pos"</halpin>
                        <format>"+4.3f"</format>
                    </number>
                </tablerow>
                <tablerow>
                    <label><text>"Z:"</text></label>
                    <number>
                        <halpin>"z-pos"</halpin>
                        <format>"+4.3f"</format>
                    </number>
                </tablerow>
            </table>
        </labelframe>

        <!-- Coolant Control -->
        <labelframe text="Coolant">
            <checkbutton>
                <halpin>"coolant-on"</halpin>
                <text>"Flood Coolant"</text>
            </checkbutton>
        </labelframe>
    </vbox>
</pyvcp>
```

**INI File Configuration:**

```ini
[DISPLAY]
DISPLAY = axis
PYVCP = pyvcp_panel.xml  # Load PyVCP panel in Axis GUI
```

**HAL Connections (custom_postgui.hal):**

```hal
# PyVCP creates pins: pyvcp.spindle-speed, pyvcp.jog-x-plus, etc.

# Connect spindle speed display
net spindle-rpm motion.spindle-speed-out => pyvcp.spindle-speed

# Connect at-speed indicator
net spindle-at-speed motion.spindle-at-speed => pyvcp.spindle-at-speed-led

# Connect jog buttons
net jog-x-plus pyvcp.jog-x-plus => halui.jog.0.plus
net jog-x-minus pyvcp.jog-x-minus => halui.jog.0.minus

# Connect jog speed slider
net jog-speed pyvcp.jog-speed => halui.jog-speed

# Connect position displays
net x-pos motion.00.joint-pos-fb => pyvcp.x-pos
net y-pos motion.01.joint-pos-fb => pyvcp.y-pos
net z-pos motion.02.joint-pos-fb => pyvcp.z-pos

# Connect coolant control
net coolant-flood pyvcp.coolant-on => motion.coolant-flood
```

### 7.5 GladeVCP: Advanced GUI Development

GladeVCP provides more flexibility than PyVCP using Glade GUI designer (GTK).

**Simple Status Display (gladevcp_panel.ui):**

Design in Glade (graphical tool), generates XML. Key elements:

- **HAL_HBar**: Horizontal bar graph (e.g., spindle load %)
- **HAL_LED**: Multi-color LED indicator
- **HAL_SpinButton**: Numeric entry with HAL pin
- **HAL_ProgressBar**: Progress indicator
- **HAL_Button**: Button with HAL output pin

**Python Handler (gladevcp_panel.py):**

```python
#!/usr/bin/env python3
"""
GladeVCP handler for custom machine panel
"""

import hal
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class HandlerClass:
    def __init__(self, halcomp, builder, useropts):
        self.halcomp = halcomp
        self.builder = builder

        # Create HAL pins for custom logic
        self.halcomp.newpin("custom-output", hal.HAL_BIT, hal.HAL_OUT)

        # Get widget references
        self.spindle_load_bar = builder.get_object("spindle_load_bar")
        self.status_label = builder.get_object("status_label")

        # Start periodic update
        GLib.timeout_add(100, self.periodic_update)  # 100 ms = 10 Hz

    def periodic_update(self):
        """Called every 100 ms"""
        # Read HAL pin (created by GladeVCP automatically)
        spindle_load = self.halcomp["spindle-load-percent"]

        # Update status label based on load
        if spindle_load > 90:
            self.status_label.set_text("WARNING: Spindle overload!")
            self.status_label.modify_fg(Gtk.StateFlags.NORMAL,
                                       Gtk.gdk.Color(65535, 0, 0))  # Red
        elif spindle_load > 70:
            self.status_label.set_text("Spindle load high")
            self.status_label.modify_fg(Gtk.StateFlags.NORMAL,
                                       Gtk.gdk.Color(65535, 32768, 0))  # Orange
        else:
            self.status_label.set_text("Normal operation")
            self.status_label.modify_fg(Gtk.StateFlags.NORMAL,
                                       Gtk.gdk.Color(0, 32768, 0))  # Green

        return True  # Continue periodic updates

    def on_custom_button_clicked(self, widget):
        """Button click handler"""
        print("Custom button clicked")
        self.halcomp["custom-output"] = True
        GLib.timeout_add(500, self.reset_button_output)  # 500 ms pulse

    def reset_button_output(self):
        self.halcomp["custom-output"] = False
        return False  # One-shot timer

def get_handlers(halcomp, builder, useropts):
    return [HandlerClass(halcomp, builder, useropts)]
```

**Loading in LinuxCNC:**

```ini
[DISPLAY]
DISPLAY = axis
GLADEVCP = -u gladevcp_panel.py gladevcp_panel.ui
```

### 7.6 Data Logging Component

**Application:** Record machine data to CSV for analysis (temperature, spindle load, position error).

**hal_logger.py:**

```python
#!/usr/bin/env python3
"""
HAL data logger - records signals to CSV file
"""

import hal
import time
import csv
from datetime import datetime

class HALLogger:
    def __init__(self, output_file="hal_log.csv", sample_rate=10):
        self.h = hal.component("hal-logger")

        # Pins for data to log
        self.h.newpin("position-x", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("position-y", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("position-z", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("spindle-rpm", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("spindle-load", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("enable-logging", hal.HAL_BIT, hal.HAL_IN)

        self.h.ready()

        self.output_file = output_file
        self.sample_interval = 1.0 / sample_rate  # Convert Hz to seconds
        self.file = None
        self.writer = None
        self.logging_active = False

    def start_logging(self):
        """Open CSV file and write header"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_file.split('.')[0]}_{timestamp}.csv"

        self.file = open(filename, 'w', newline='')
        self.writer = csv.writer(self.file)

        # Write header
        self.writer.writerow([
            'timestamp', 'position_x', 'position_y', 'position_z',
            'spindle_rpm', 'spindle_load'
        ])

        print(f"HAL Logger: Started logging to {filename}")
        self.logging_active = True

    def stop_logging(self):
        """Close CSV file"""
        if self.file:
            self.file.close()
            self.file = None
            self.writer = None
            print("HAL Logger: Stopped logging")
        self.logging_active = False

    def log_sample(self):
        """Write one data sample to CSV"""
        if not self.writer:
            return

        timestamp = time.time()

        self.writer.writerow([
            timestamp,
            self.h["position-x"],
            self.h["position-y"],
            self.h["position-z"],
            self.h["spindle-rpm"],
            self.h["spindle-load"]
        ])

    def run(self):
        """Main loop"""
        try:
            last_sample_time = 0
            prev_enable = False

            while True:
                enable = self.h["enable-logging"]

                # Detect rising edge on enable pin
                if enable and not prev_enable:
                    self.start_logging()
                elif not enable and prev_enable:
                    self.stop_logging()

                prev_enable = enable

                # Log sample at specified rate
                now = time.time()
                if self.logging_active and (now - last_sample_time >= self.sample_interval):
                    self.log_sample()
                    last_sample_time = now

                time.sleep(0.001)  # 1 ms sleep (1000 Hz loop, actual logging rate controlled by sample_interval)

        except KeyboardInterrupt:
            self.stop_logging()
            print("\nHAL Logger: Shutdown")

if __name__ == "__main__":
    import sys

    output_file = sys.argv[1] if len(sys.argv) > 1 else "hal_log.csv"
    sample_rate = int(sys.argv[2]) if len(sys.argv) > 2 else 10  # 10 Hz default

    logger = HALLogger(output_file=output_file, sample_rate=sample_rate)
    logger.run()
```

**HAL Integration:**

```hal
loadusr -W hal_logger.py machine_data.csv 100  # 100 Hz logging rate

# Connect signals to log
net x-pos motion.00.joint-pos-fb => hal-logger.position-x
net y-pos motion.01.joint-pos-fb => hal-logger.position-y
net z-pos motion.02.joint-pos-fb => hal-logger.position-z
net spindle-rpm spindle-encoder.rpm => hal-logger.spindle-rpm
net spindle-load analog-input.0 => hal-logger.spindle-load

# Connect logging enable (e.g., from PyVCP checkbox)
net logging-enable pyvcp.enable-logging => hal-logger.enable-logging
```

### 7.7 Threading and Concurrency

**Problem:** Python Global Interpreter Lock (GIL) prevents true multi-threading for CPU-bound tasks.

**Solution:** Use separate processes or async I/O for concurrent operations.

**Example: Non-Blocking Modbus Communication**

```python
import hal
import time
import threading
import queue

class AsyncModbusVFD:
    def __init__(self):
        self.h = hal.component("async-modbus-vfd")
        self.h.newpin("speed-cmd", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("speed-fb", hal.HAL_FLOAT, hal.HAL_OUT)
        self.h.ready()

        # Communication queue (thread-safe)
        self.cmd_queue = queue.Queue()
        self.result_queue = queue.Queue()

        # Start Modbus communication thread
        self.comm_thread = threading.Thread(target=self.comm_worker, daemon=True)
        self.comm_thread.start()

    def comm_worker(self):
        """Separate thread handles slow Modbus communication"""
        while True:
            # Get command from queue (blocks if empty)
            cmd = self.cmd_queue.get()

            # Perform Modbus transaction (may take 10-100 ms)
            result = self.send_modbus_command(cmd)

            # Put result in queue
            self.result_queue.put(result)

    def send_modbus_command(self, cmd):
        # Actual Modbus communication (slow)
        time.sleep(0.05)  # Simulated 50 ms delay
        return {"speed_fb": cmd["speed_cmd"] * 0.98}  # Simulated feedback

    def update(self):
        """Fast update loop (100 Hz), doesn't block on Modbus"""
        # Send command to comm thread (non-blocking)
        try:
            speed_cmd = self.h["speed-cmd"]
            self.cmd_queue.put_nowait({"speed_cmd": speed_cmd})
        except queue.Full:
            pass  # Skip if queue full (comm thread busy)

        # Read result from comm thread (non-blocking)
        try:
            result = self.result_queue.get_nowait()
            self.h["speed-fb"] = result["speed_fb"]
        except queue.Empty:
            pass  # No new data yet

    def run(self):
        try:
            while True:
                self.update()
                time.sleep(0.01)  # 100 Hz
        except KeyboardInterrupt:
            pass
```

### 7.8 Error Handling and Robustness

**Best Practices:**

```python
#!/usr/bin/env python3
import hal
import time
import sys

class RobustComponent:
    def __init__(self):
        try:
            self.h = hal.component("robust-component")
            self.h.newpin("input", hal.HAL_FLOAT, hal.HAL_IN)
            self.h.newpin("output", hal.HAL_FLOAT, hal.HAL_OUT)
            self.h.newpin("fault", hal.HAL_BIT, hal.HAL_OUT)
            self.h.ready()

            self.error_count = 0
            self.max_errors = 10

        except Exception as e:
            print(f"FATAL: Failed to create HAL component: {e}", file=sys.stderr)
            sys.exit(1)

    def safe_compute(self, input_value):
        """Computation with error handling"""
        try:
            # Divide by potentially zero value
            if abs(input_value) < 0.001:
                raise ValueError("Input too close to zero")

            result = 100.0 / input_value

            # Check for reasonable output
            if abs(result) > 10000:
                raise ValueError("Output out of range")

            self.error_count = 0  # Reset error counter on success
            return result

        except Exception as e:
            print(f"ERROR: Computation failed: {e}", file=sys.stderr)
            self.error_count += 1

            if self.error_count >= self.max_errors:
                print("FATAL: Too many errors, halting component", file=sys.stderr)
                self.h["fault"] = True
                return 0.0

            return self.h["output"]  # Return previous valid value

    def run(self):
        try:
            while True:
                if self.h["fault"]:
                    time.sleep(1.0)  # Idle if faulted
                    continue

                input_val = self.h["input"]
                output_val = self.safe_compute(input_val)
                self.h["output"] = output_val

                time.sleep(0.01)

        except KeyboardInterrupt:
            print("\nShutdown requested")
        except Exception as e:
            print(f"FATAL: Unhandled exception: {e}", file=sys.stderr)
            self.h["fault"] = True
        finally:
            # Cleanup code always runs
            print("Component stopped")

if __name__ == "__main__":
    comp = RobustComponent()
    comp.run()
```

### 7.9 Debugging Python Components

**Logging to Terminal:**

```python
import sys

# Print to stderr (visible in terminal)
print("Debug: Speed command = {:.1f}".format(speed_cmd), file=sys.stderr)

# Flush immediately (don't buffer)
sys.stderr.flush()
```

**Using Python Debugger:**

```python
import pdb

def update(self):
    speed = self.h["speed-cmd"]

    pdb.set_trace()  # Debugger breakpoint
    # Execution pauses here, type 'n' for next line, 'c' to continue, 'p speed' to print variable

    self.h["output"] = speed * 2.0
```

**Logging to File:**

```python
import logging

logging.basicConfig(
    filename='/tmp/hal_component.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Component started")
logging.debug(f"Speed command: {speed_cmd}")
logging.error(f"Communication failure: {error}")
```

### 7.10 Summary: Python HAL Development

Python user-space components complement real-time C components:

**When to Use Python:**

- VFD/spindle control (Modbus, RS-485, proprietary protocols)
- Custom GUIs (PyVCP, GladeVCP, standalone applications)
- Data logging and analysis
- Web interfaces (Flask, Django integration)
- USB/network device communication
- Rapid prototyping before C implementation

**Key Advantages:**

- Fast development (no compilation)
- Full Linux API access (file I/O, networking, USB)
- Crash isolation (doesn't affect real-time threads)
- Rich library ecosystem (pyModbus, pySerial, numpy, pandas)

**Limitations:**

- Non-deterministic latency (1-100 ms typical)
- Not suitable for time-critical control (motion, step generation)
- Higher CPU usage than C

**Best Practices:**

- Use threading for I/O-bound operations (Modbus, serial)
- Robust error handling (try/except, fault pins)
- Logging for debugging (stderr, log files)
- Sleep to avoid 100% CPU usage (time.sleep())
- Clean shutdown (catch KeyboardInterrupt)

**Next Section** (14.8) covers Mesa FPGA card integration: hostmot2 driver configuration, firmware selection, step/encoder/PWM setup, and GPIO mapping for professional CNC control systems.

***

*Total: 4,524 words | 0 equations | 5 complete worked examples | 2 tables | 18 code blocks*
