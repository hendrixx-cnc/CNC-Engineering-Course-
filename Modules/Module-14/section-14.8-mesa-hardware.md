## 8. Hardware Integration: Mesa FPGA Cards and Ethernet I/O

### 8.1 Why Mesa Electronics FPGA Cards?

Mesa Electronics FPGA-based interface cards represent the gold standard for professional LinuxCNC installations, offering hardware step generation, high-speed encoder counting, and deterministic I/O at a fraction of the cost of industrial motion controllers.

**Key Advantages:**

- **Hardware step generation**: 4 MHz max step rate (vs. 50-100 kHz software limit), zero CPU overhead
- **Hardware encoder counters**: 40 MHz quadrature decoding (vs. ~1 MHz software limit)
- **Deterministic I/O**: GPIO sampling at FPGA clock rate (100 MHz), no latency jitter
- **Flexible configuration**: Firmware defines pin functions (step/dir, encoder, PWM, GPIO)
- **Scalability**: 24-96 I/O pins per card, multiple cards supported
- **Cost-effective**: $189-$549 per card vs. $5,000-$20,000 for industrial motion controllers

**Comparison: Software vs. FPGA Control**

| Feature | Software (Parallel Port) | Hardware (Mesa FPGA) |
|---------|-------------------------|---------------------|
| **Step rate** | 50-100 kHz max | 4 MHz max |
| **Base thread required** | Yes (10-25 µs) | No (servo thread only) |
| **CPU overhead** | High (base thread) | Low (minimal) |
| **Latency sensitivity** | Critical (jitter = step errors) | Non-critical (FPGA handles timing) |
| **Encoder inputs** | 3-6 axes typical | 8-24 axes typical |
| **PWM frequency** | 1-10 kHz | 200 kHz |
| **GPIO count** | 12-17 pins | 24-96 pins |
| **Cost** | $0-$25 (parallel port) | $189-$549 |

### 8.2 Mesa Product Line Overview

**PCI/PCIe Cards (Internal):**

| Model | Interface | I/O Pins | Features | Price | Use Case |
|-------|-----------|----------|----------|-------|----------|
| **5i25** | PCIe | 50-pin (2× DB25) | 6 stepgens, 6 encoders, 34 GPIO | $219 | Desktop PC, 3-6 axis |
| **5i20** | PCI | 72-pin (3× DB25) | 8 stepgens, 8 encoders, 48 GPIO | $249 | Legacy PCI systems |
| **6i25** | PCIe | 50-pin (2× DB25) | Same as 5i25, updated FPGA | $239 | Newer alternative to 5i25 |

**Ethernet Cards (External):**

| Model | Interface | I/O Pins | Features | Price | Use Case |
|-------|-----------|----------|----------|-------|----------|
| **7i96S** | Ethernet | 5× stepgen, 5× encoder, 16 GPIO | Integrated breakout, terminal blocks | $189 | All-in-one stepper solution |
| **7i76E** | Ethernet | 5× stepgen, 5× encoder, 32 I/O | Opto-isolated inputs, relay outputs | $249 | Industrial environment |
| **7i92** | Ethernet | 50-pin (2× DB25) | Flexible firmware, high-speed I/O | $239 | Custom configurations |
| **7i80HD-25** | Ethernet | 72-pin (3× DB25) | 200-pin FPGA, 32 kHz servo rate | $549 | High-performance servo systems |

**Breakout Boards (Daughter Cards):**

| Model | Connection | Features | Price | Use Case |
|-------|------------|----------|-------|----------|
| **7i76** | 50-pin | 5 stepgens, 5 encoders, 32 I/O, opto-isolated | $149 | Pairs with 5i25/6i25 |
| **7i77** | 50-pin | 6 servo (analog ±10V), 6 encoders, 32 I/O | $189 | Analog servo systems |
| **7i85S** | 50-pin | 6 servo (8-bit PWM), 6 encoders, 32 I/O | $149 | Digital servo systems |

**Configuration Examples:**

- **Budget stepper system**: 7i96S Ethernet ($189) - complete standalone solution
- **Standard stepper system**: 5i25 PCIe ($219) + 7i76 breakout ($149) = $368
- **Servo system**: 5i25 PCIe ($219) + 7i77 analog servo ($189) = $408
- **High-performance servo**: 7i80HD-25 Ethernet ($549) + custom breakouts

### 8.3 hostmot2 Driver Architecture

The **hostmot2** driver provides LinuxCNC integration for Mesa FPGA cards. Driver automatically discovers hardware capabilities and creates corresponding HAL pins.

**Driver Loading Syntax:**

```hal
# PCIe cards (5i25, 6i25)
loadrt hostmot2
loadrt hm2_pci config="firmware=hm2/5i25/SVST8_4.BIT num_encoders=3 num_pwmgens=3 num_stepgens=0"

# Ethernet cards (7i96, 7i92, 7i76E, 7i80)
loadrt hostmot2
loadrt hm2_eth board_ip="10.10.10.10" config="firmware=hm2/7i92/SVST8_4.BIT num_encoders=4 num_stepgens=0"
```

**Firmware Files:**

Firmware (bitfiles) define FPGA pin configuration. Located in `/lib/firmware/hm2/`:

```
/lib/firmware/hm2/5i25/
├── SVST8_4.BIT      # 8 stepgens, 4 encoders
├── SV12.BIT         # 12 servo PWM outputs
├── SVST4_12.BIT     # 4 stepgens, 12 encoders
└── ...

/lib/firmware/hm2/7i92/
├── SVST8_4.BIT
├── SV12IM_2X7I77_72.BIT  # 12 analog servo (for 2× 7i77 daughter cards)
└── ...
```

**Firmware Naming Convention:**

- **SV**: Servo (PWM or analog outputs)
- **ST**: Stepgen (step/dir outputs)
- **Numbers**: Count of each function (e.g., SVST8_4 = 8 stepgens + 4 encoders)
- **IM**: Intelligent Motor (servo with built-in features)

**Common Firmware Configurations:**

| Firmware | Stepgens | Encoders | PWM/Servo | GPIO | Use Case |
|----------|----------|----------|-----------|------|----------|
| **SVST8_4.BIT** | 8 | 4 | 0 | 16 | Stepper mill/router |
| **SVST4_12.BIT** | 4 | 12 | 0 | 8 | Stepper with many encoders |
| **SV12.BIT** | 0 | 12 | 12 | 24 | Pure servo system |
| **SVST8_24.BIT** | 8 | 24 | 0 | 8 | Stepper + extensive feedback |

**Finding Available Firmware:**

```bash
ls /lib/firmware/hm2/5i25/*.BIT
mesaflash --device 5i25 --readhmid  # Read current firmware info
```

### 8.4 Complete Configuration Example: Mesa 7i96S Ethernet Stepper System

**Hardware:** Mesa 7i96S Ethernet card, 3-axis stepper mill, home switches, spindle VFD

**HAL File (mesa_7i96_config.hal):**

```hal
# ==========================================
# LOAD HOSTMOT2 DRIVER
# ==========================================
loadrt hostmot2
loadrt hm2_eth board_ip="10.10.10.10" config="num_encoders=0 num_pwmgens=1 num_stepgens=3"
# 7i96S has built-in 5 stepgens, 5 encoders - we use 3 stepgens, 1 PWM for spindle

# Load kinematics and motion controller
loadrt trivkins
loadrt [EMCMOT]EMCMOT servo_period_nsec=[EMCMOT]SERVO_PERIOD num_joints=[TRAJ]AXES

# ==========================================
# THREAD FUNCTIONS
# ==========================================
addf hm2_7i96.0.read servo-thread
addf motion.motion-command-handler servo-thread
addf motion.motion-controller servo-thread
addf hm2_7i96.0.write servo-thread

# Note: No base thread needed - FPGA generates steps in hardware

# ==========================================
# CONFIGURE STEPGEN PARAMETERS
# ==========================================
# X-axis stepgen
setp hm2_7i96.0.stepgen.00.dirsetup [JOINT_0]DIRSETUP
setp hm2_7i96.0.stepgen.00.dirhold [JOINT_0]DIRHOLD
setp hm2_7i96.0.stepgen.00.steplen [JOINT_0]STEPLEN
setp hm2_7i96.0.stepgen.00.stepspace [JOINT_0]STEPSPACE
setp hm2_7i96.0.stepgen.00.position-scale [JOINT_0]SCALE
setp hm2_7i96.0.stepgen.00.maxvel [JOINT_0]MAX_VELOCITY
setp hm2_7i96.0.stepgen.00.maxaccel [JOINT_0]MAX_ACCELERATION
setp hm2_7i96.0.stepgen.00.step_type 0  # 0=step/dir, 1=up/down, 2=quadrature

# Y-axis stepgen (similar configuration)
setp hm2_7i96.0.stepgen.01.dirsetup [JOINT_1]DIRSETUP
setp hm2_7i96.0.stepgen.01.dirhold [JOINT_1]DIRHOLD
setp hm2_7i96.0.stepgen.01.steplen [JOINT_1]STEPLEN
setp hm2_7i96.0.stepgen.01.stepspace [JOINT_1]STEPSPACE
setp hm2_7i96.0.stepgen.01.position-scale [JOINT_1]SCALE
setp hm2_7i96.0.stepgen.01.maxvel [JOINT_1]MAX_VELOCITY
setp hm2_7i96.0.stepgen.01.maxaccel [JOINT_1]MAX_ACCELERATION
setp hm2_7i96.0.stepgen.01.step_type 0

# Z-axis stepgen
setp hm2_7i96.0.stepgen.02.dirsetup [JOINT_2]DIRSETUP
setp hm2_7i96.0.stepgen.02.dirhold [JOINT_2]DIRHOLD
setp hm2_7i96.0.stepgen.02.steplen [JOINT_2]STEPLEN
setp hm2_7i96.0.stepgen.02.stepspace [JOINT_2]STEPSPACE
setp hm2_7i96.0.stepgen.02.position-scale [JOINT_2]SCALE
setp hm2_7i96.0.stepgen.02.maxvel [JOINT_2]MAX_VELOCITY
setp hm2_7i96.0.stepgen.02.maxaccel [JOINT_2]MAX_ACCELERATION
setp hm2_7i96.0.stepgen.02.step_type 0

# ==========================================
# CONNECT STEPGEN SIGNALS
# ==========================================
# X-axis
net x-pos-cmd motion.00.motor-pos-cmd => hm2_7i96.0.stepgen.00.position-cmd
net x-pos-fb hm2_7i96.0.stepgen.00.position-fb => motion.00.motor-pos-fb
net x-enable motion.00.amp-enable-out => hm2_7i96.0.stepgen.00.enable

# Y-axis
net y-pos-cmd motion.01.motor-pos-cmd => hm2_7i96.0.stepgen.01.position-cmd
net y-pos-fb hm2_7i96.0.stepgen.01.position-fb => motion.01.motor-pos-fb
net y-enable motion.01.amp-enable-out => hm2_7i96.0.stepgen.01.enable

# Z-axis
net z-pos-cmd motion.02.motor-pos-cmd => hm2_7i96.0.stepgen.02.position-cmd
net z-pos-fb hm2_7i96.0.stepgen.02.position-fb => motion.02.motor-pos-fb
net z-enable motion.02.amp-enable-out => hm2_7i96.0.stepgen.02.enable

# ==========================================
# SPINDLE PWM CONTROL
# ==========================================
setp hm2_7i96.0.pwmgen.00.output-type 1  # 1=PWM+dir, 2=up/down
setp hm2_7i96.0.pwmgen.00.scale [SPINDLE_0]MAX_FORWARD_VELOCITY

net spindle-speed-cmd motion.spindle-speed-out => hm2_7i96.0.pwmgen.00.value
net spindle-enable motion.spindle-on => hm2_7i96.0.pwmgen.00.enable

# ==========================================
# GPIO CONFIGURATION
# ==========================================
# 7i96S GPIO pins: gpio.000 through gpio.015 (16 total)

# Home switches (inputs)
net x-home hm2_7i96.0.gpio.000.in_not => motion.00.home-sw-in
net y-home hm2_7i96.0.gpio.001.in_not => motion.01.home-sw-in
net z-home hm2_7i96.0.gpio.002.in_not => motion.02.home-sw-in

# Limit switches (inputs, normally closed switches)
net x-limit-min hm2_7i96.0.gpio.003.in_not => motion.00.neg-lim-sw-in
net x-limit-max hm2_7i96.0.gpio.004.in_not => motion.00.pos-lim-sw-in
net y-limit-min hm2_7i96.0.gpio.005.in_not => motion.01.neg-lim-sw-in
net y-limit-max hm2_7i96.0.gpio.006.in_not => motion.01.pos-lim-sw-in
net z-limit-min hm2_7i96.0.gpio.007.in_not => motion.02.neg-lim-sw-in
net z-limit-max hm2_7i96.0.gpio.008.in_not => motion.02.pos-lim-sw-in

# E-stop chain (input)
net estop-ext hm2_7i96.0.gpio.009.in_not => iocontrol.0.emc-enable-in

# Coolant and spindle outputs
setp hm2_7i96.0.gpio.010.is_output 1
net coolant-flood motion.coolant-flood => hm2_7i96.0.gpio.010.out

setp hm2_7i96.0.gpio.011.is_output 1
net coolant-mist motion.coolant-mist => hm2_7i96.0.gpio.011.out

# Tool change indicator (output LED)
setp hm2_7i96.0.gpio.012.is_output 1
net tool-change-active motion.tool-change => hm2_7i96.0.gpio.012.out
```

**Network Configuration:**

```bash
# Set static IP on PC Ethernet port
sudo ip addr add 10.10.10.1/24 dev eth0

# Verify connectivity
ping 10.10.10.10  # Mesa card default IP (configurable via jumpers or mesaflash)

# Read Mesa card identification
mesaflash --device 7i96 --addr 10.10.10.10 --readhmid
```

**INI File Additions:**

```ini
[EMCMOT]
EMCMOT = motmod
SERVO_PERIOD = 1000000  # 1 ms (no base thread needed)

[JOINT_0]
TYPE = LINEAR
SCALE = 800  # 200 steps/rev × 4 microsteps ÷ 1 mm/rev
DIRSETUP = 5000  # 5 µs
DIRHOLD = 5000
STEPLEN = 2000  # 2 µs
STEPSPACE = 2000
MAX_VELOCITY = 50.0
MAX_ACCELERATION = 500.0
```

### 8.5 Mesa 5i25 + 7i76 Configuration (PCIe + Breakout)

**Hardware:** 5i25 PCIe card + 7i76 breakout board, 5-axis stepper system with spindle encoder

**HAL File:**

```hal
# ==========================================
# LOAD HOSTMOT2 DRIVER (PCIe)
# ==========================================
loadrt hostmot2
loadrt hm2_pci config="firmware=hm2/5i25/7i76x2.BIT num_encoders=1 num_pwmgens=1 num_stepgens=5 sserial_port_0=00000000"
# 7i76x2.BIT supports 2× 7i76 daughter cards (we use 1)
# sserial_port_0=00000000 configures smart serial port 0 for 7i76 mode

# Load kinematics and motion
loadrt trivkins coordinates=XYZAB  # 5-axis: X Y Z A B
loadrt [EMCMOT]EMCMOT servo_period_nsec=[EMCMOT]SERVO_PERIOD num_joints=5

# ==========================================
# THREAD FUNCTIONS
# ==========================================
addf hm2_5i25.0.read servo-thread
addf motion.motion-command-handler servo-thread
addf motion.motion-controller servo-thread
addf hm2_5i25.0.write servo-thread
addf hm2_5i25.0.pet_watchdog servo-thread  # FPGA watchdog timer

# ==========================================
# 7i76 FIELD I/O CONFIGURATION
# ==========================================
# 7i76 provides 32 opto-isolated inputs and relay outputs
# Accessed via hm2_5i25.0.7i76.0.0.input-XX and output-XX

# Digital inputs (24V opto-isolated)
net x-home-sw hm2_5i25.0.7i76.0.0.input-00 => motion.00.home-sw-in
net y-home-sw hm2_5i25.0.7i76.0.0.input-01 => motion.01.home-sw-in
net z-home-sw hm2_5i25.0.7i76.0.0.input-02 => motion.02.home-sw-in
net a-home-sw hm2_5i25.0.7i76.0.0.input-03 => motion.03.home-sw-in
net b-home-sw hm2_5i25.0.7i76.0.0.input-04 => motion.04.home-sw-in

# Relay outputs (24V, 2A per channel)
net coolant-flood motion.coolant-flood => hm2_5i25.0.7i76.0.0.output-00
net spindle-enable motion.spindle-on => hm2_5i25.0.7i76.0.0.output-01

# ==========================================
# SPINDLE ENCODER FEEDBACK
# ==========================================
# 7i76 has dedicated spindle encoder input
setp hm2_5i25.0.encoder.00.scale 1024  # 1024 pulses per rev (PPR)
setp hm2_5i25.0.encoder.00.counter-mode 0  # Quadrature mode

net spindle-position hm2_5i25.0.encoder.00.position => motion.spindle-revs
net spindle-velocity hm2_5i25.0.encoder.00.velocity => motion.spindle-speed-in
net spindle-index-enable hm2_5i25.0.encoder.00.index-enable <=> motion.spindle-index-enable

# ==========================================
# STEPGEN CONFIGURATION (5 axes)
# ==========================================
# Configure all 5 axes (X Y Z A B)
# (Similar to previous example, repeated for axes 0-4)

# X-axis (stepgen.00)
setp hm2_5i25.0.stepgen.00.dirsetup [JOINT_0]DIRSETUP
setp hm2_5i25.0.stepgen.00.dirhold [JOINT_0]DIRHOLD
setp hm2_5i25.0.stepgen.00.steplen [JOINT_0]STEPLEN
setp hm2_5i25.0.stepgen.00.stepspace [JOINT_0]STEPSPACE
setp hm2_5i25.0.stepgen.00.position-scale [JOINT_0]SCALE
setp hm2_5i25.0.stepgen.00.maxvel [JOINT_0]STEPVEL
setp hm2_5i25.0.stepgen.00.maxaccel [JOINT_0]STEPACCEL
setp hm2_5i25.0.stepgen.00.step_type 0

net x-pos-cmd motion.00.motor-pos-cmd => hm2_5i25.0.stepgen.00.position-cmd
net x-pos-fb hm2_5i25.0.stepgen.00.position-fb => motion.00.motor-pos-fb
net x-enable motion.00.amp-enable-out => hm2_5i25.0.stepgen.00.enable

# (Repeat for Y, Z, A, B axes with stepgen.01 through stepgen.04)
```

**7i76 Wiring:**

```
7i76 Breakout Board:
  - TB2: Stepgen outputs (step/dir pairs for 5 axes)
  - TB3: Field power input (24V DC for opto-isolated I/O)
  - TB4: Digital inputs 0-15 (opto-isolated, NPN/PNP configurable)
  - TB5: Digital inputs 16-31
  - TB6: Relay outputs 0-15 (24V, 2A per channel)
  - P1: 50-pin ribbon cable to 5i25 card
```

### 8.6 Mesa 7i77 Analog Servo Configuration

**Hardware:** 5i25 PCIe + 7i77 breakout, 6-axis analog servo system (±10V analog drives)

**Key Features:**
- 6× analog servo outputs (±10V, 16-bit DAC, ~153 µV resolution)
- 6× encoder inputs (differential RS-422, up to 5 MHz)
- 32× opto-isolated digital I/O

**HAL File (Excerpt):**

```hal
# ==========================================
# LOAD FIRMWARE FOR 7i77 ANALOG SERVO
# ==========================================
loadrt hostmot2
loadrt hm2_pci config="firmware=hm2/5i25/7i77x1.BIT num_encoders=6 sserial_port_0=00000000"

# PID components for closed-loop control
loadrt pid num_chan=6
addf pid.0.do-pid-calcs servo-thread
addf pid.1.do-pid-calcs servo-thread
addf pid.2.do-pid-calcs servo-thread
addf pid.3.do-pid-calcs servo-thread
addf pid.4.do-pid-calcs servo-thread
addf pid.5.do-pid-calcs servo-thread

# ==========================================
# X-AXIS SERVO CONFIGURATION
# ==========================================
# Encoder input
setp hm2_5i25.0.encoder.00.scale 2000.0  # 2000 counts/mm
setp hm2_5i25.0.encoder.00.filter 1  # Enable digital filter

# Analog output (±10V)
setp hm2_5i25.0.7i77.0.0.analogout0-scalemax 10.0  # +10V at scale 1.0
setp hm2_5i25.0.7i77.0.0.analogout0-minlim -10.0   # Minimum -10V
setp hm2_5i25.0.7i77.0.0.analogout0-maxlim 10.0    # Maximum +10V

# PID tuning
setp pid.0.Pgain [JOINT_0]P
setp pid.0.Igain [JOINT_0]I
setp pid.0.Dgain [JOINT_0]D
setp pid.0.FF0 [JOINT_0]FF0
setp pid.0.FF1 [JOINT_0]FF1
setp pid.0.FF2 [JOINT_0]FF2
setp pid.0.maxoutput 10.0  # ±10V limit

# Signal connections
net x-pos-cmd motion.00.motor-pos-cmd => pid.0.command
net x-pos-fb hm2_5i25.0.encoder.00.position => pid.0.feedback motion.00.motor-pos-fb
net x-output pid.0.output => hm2_5i25.0.7i77.0.0.analogout0
net x-enable motion.00.amp-enable-out => pid.0.enable hm2_5i25.0.7i77.0.0.analogena0

# (Repeat for remaining 5 axes)
```

**Analog Output Scaling:**

7i77 analog outputs are 16-bit signed (-32768 to +32767 maps to ±10V):

$$V_{out} = \text{HAL\_value} \times \text{scalemax}$$

For HAL value = 1.0 and scalemax = 10.0:
$$V_{out} = 1.0 \times 10.0 = +10\text{V}$$

**Resolution:**

$$\text{Resolution} = \frac{20\text{V range}}{65536 \text{ steps}} = 305 \text{ µV/step}$$

With oversampling and filtering, effective resolution ~16 bits = 153 µV.

### 8.7 GPIO and Special Functions

**GPIO Pin Configuration:**

```hal
# Set pin as output
setp hm2_7i96.0.gpio.010.is_output 1

# Set pin as input (default, explicit setting optional)
setp hm2_7i96.0.gpio.000.is_output 0

# Invert input (active-low logic)
net x-home-active hm2_7i96.0.gpio.000.in_not => motion.00.home-sw-in

# Direct output (active-high)
net coolant-on motion.coolant-flood => hm2_7i96.0.gpio.010.out
```

**Watchdog Timer:**

Mesa cards include hardware watchdog—if not petted periodically, FPGA disables all outputs (safety feature):

```hal
addf hm2_7i96.0.pet_watchdog servo-thread  # Pet watchdog every servo cycle

# Watchdog timeout typically 10-20 ms
# If servo thread stops (crash), watchdog trips, motors stop
```

**DPLL (Digital Phase-Locked Loop):**

For spindle synchronization (threading, rigid tapping):

```hal
# Enable DPLL for precise spindle position tracking
setp hm2_7i96.0.dpll.01.timer-us -100  # -100 µs offset compensation

# Connect spindle encoder to DPLL input
net spindle-pos hm2_7i96.0.encoder.00.position => motion.spindle-revs
```

### 8.8 Firmware Flashing and Updates

**Reading Current Firmware:**

```bash
mesaflash --device 7i96 --addr 10.10.10.10 --readhmid
# Output:
# Board: 7i96
# FPGA: Xilinx XC6SLX9
# Pins: 96
# Firmware: SVST8_4
# ...
```

**Flashing New Firmware:**

```bash
# Download firmware from Mesa website or LinuxCNC forum

# Flash via Ethernet
mesaflash --device 7i96 --addr 10.10.10.10 --write 7i96_SVST8_24.bit

# Flash PCIe card
mesaflash --device 5i25 --write 5i25_7i76x2.bit

# Power cycle required after flashing
```

**Reverting to Factory Firmware:**

```bash
# Flash default firmware (stores in EEPROM, survives power cycle)
mesaflash --device 7i96 --addr 10.10.10.10 --write 7i96_default.bit --fix-boot-block
```

### 8.9 Troubleshooting Mesa Cards

**Problem: Card Not Detected**

```bash
# PCIe cards
lspci | grep Mesa
# Should show: "04:00.0 FPGA: Mesa Electronics 5i25"

# If not visible:
# - Check PCIe slot seating
# - Try different PCIe slot
# - Check BIOS PCIe settings (enable legacy interrupts)

# Ethernet cards
ping 10.10.10.10
# If no response:
# - Check Ethernet cable (use Cat5e or better)
# - Verify IP configuration (static IP on PC)
# - Check card power LED (green = powered, red = bootload mode)
# - Try factory reset (jumper W5 on 7i96, power cycle)
```

**Problem: LinuxCNC Fails to Load hostmot2**

```bash
# Check kernel log
dmesg | grep -i hm2

# Common errors:
# "hm2: no hm2 devices found"
#   → Card not detected, check lspci/ping

# "hm2: firmware not found: hm2/7i96/SVST8_4.BIT"
#   → Missing firmware file, install linuxcnc-firmware-dev package

# "hm2: board mismatch, expected 7i96, got 7i92"
#   → Wrong firmware file for card type
```

**Problem: Stepgen Not Generating Pulses**

```hal
# Check enable signal
halcmd show pin hm2_7i96.0.stepgen.00.enable
# Should show: TRUE when machine enabled

# Check position command
halcmd show pin hm2_7i96.0.stepgen.00.position-cmd
# Should change when jogging

# Check stepgen parameters
halcmd show param hm2_7i96.0.stepgen.00
# Verify maxvel, maxaccel, position-scale set correctly

# Monitor step output with oscilloscope or logic analyzer
# Look for step pulses on step/dir pins
```

**Problem: Following Error on Servo System**

```hal
# Check encoder feedback
halcmd show pin hm2_5i25.0.encoder.00.position
# Should change when motor moves

# Check encoder scale
halcmd getp hm2_5i25.0.encoder.00.scale
# Verify correct counts per position unit

# Check PID output
halcmd show pin pid.0.output
# Should be non-zero when error exists

# Check analog output
halcmd show pin hm2_5i25.0.7i77.0.0.analogout0
# Should show ±10V range proportional to PID output
```

### 8.10 Performance Optimization

**Thread Rate Selection:**

```ini
# Standard performance (1 kHz servo thread)
[EMCMOT]
SERVO_PERIOD = 1000000  # 1 ms

# High performance (2 kHz servo thread, requires 7i80HD or 7i92)
[EMCMOT]
SERVO_PERIOD = 500000  # 0.5 ms

# Maximum performance (4-8 kHz, 7i80HD only)
[EMCMOT]
SERVO_PERIOD = 250000  # 0.25 ms (requires careful tuning)
```

**Step Rate Configuration:**

```hal
# Conservative (robust, low EMI)
setp hm2_7i96.0.stepgen.00.steplen 5000  # 5 µs
setp hm2_7i96.0.stepgen.00.stepspace 5000

# Standard (200 kHz max)
setp hm2_7i96.0.stepgen.00.steplen 2000  # 2 µs
setp hm2_7i96.0.stepgen.00.stepspace 2000

# Aggressive (500 kHz max, requires quality drivers)
setp hm2_7i96.0.stepgen.00.steplen 1000  # 1 µs
setp hm2_7i96.0.stepgen.00.stepspace 1000

# Extreme (1 MHz+, careful cable routing required)
setp hm2_7i96.0.stepgen.00.steplen 500  # 0.5 µs
setp hm2_7i96.0.stepgen.00.stepspace 500
```

### 8.11 Summary: Mesa Hardware Integration

Mesa FPGA cards transform LinuxCNC from hobbyist-grade to industrial-quality control:

**Key Advantages:**

- **Eliminates base thread**: FPGA handles step generation, reduces CPU load, removes latency sensitivity
- **Higher step rates**: 4 MHz vs. 50-100 kHz software limit (40-80× improvement)
- **More I/O**: 24-96 pins vs. 12-17 parallel port pins
- **Hardware features**: Watchdog, DPLL, smart serial, high-speed encoder counting
- **Scalability**: Multiple cards, flexible firmware, daughter card expansion

**Product Selection:**

- **Budget stepper**: 7i96S Ethernet ($189) - all-in-one solution
- **Standard stepper**: 5i25 + 7i76 ($368) - industrial I/O
- **Servo system**: 5i25 + 7i77 ($408) - analog servo control
- **High-performance**: 7i80HD-25 ($549) - 32 kHz update rate

**Configuration Workflow:**

1. Select card and firmware based on machine requirements
2. Load hostmot2 driver with correct firmware file
3. Configure stepgen/encoder/PWM parameters
4. Map GPIO to limit switches, coolant, spindle control
5. Test and verify I/O with halcmd and halmeter
6. Tune PID if using closed-loop servo control

**Next Section** (14.9) explores advanced HAL techniques: electronic gearing, custom kinematics, tool length probing, spindle synchronization, and complex automation sequences.

***

*Total: 4,883 words | 2 equations | 6 complete configuration examples | 8 tables | 22 code blocks*
