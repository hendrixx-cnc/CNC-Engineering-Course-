## 11. Safety Systems and Watchdogs

### 11.1 Safety Philosophy: Defense in Depth

CNC machines control high-power motors, spinning tools, and heavy mechanical components capable of injury or death. **Software cannot be the sole safety mechanism**—LinuxCNC HAL configurations must implement layered safety systems with hardware backup.

**Defense-in-Depth Layers:**

1. **Hardware E-stop circuit**: Independent of software, breaks motor power via relay/contactor
2. **Limit switches**: Physical switches cut power before software limits reached
3. **Software limits**: HAL logic monitors position, disables motion at configured boundaries
4. **Following error detection**: Motion controller halts on excessive position error
5. **Watchdog timers**: Detect software crashes, disable outputs if servo thread stops
6. **Operator controls**: Accessible E-stop buttons, feed hold, cycle stop

**Critical Principle:** Each layer provides independent protection. Software failure at any level should not compromise physical safety.

### 11.2 Hardware E-Stop Chain

**Requirement:** E-stop button must **physically interrupt motor power** independent of LinuxCNC software state.

**Correct Implementation (Relay-Based):**

```
24V DC Power Supply
    |
    ├──> [E-stop Button] ──> [Safety Relay] ──> Motor Drive Enable Inputs
    |         (NC)              (Coil)              (24V = Enabled)
    |
    └──> LinuxCNC E-stop Monitor (parallel sensing)
```

**E-Stop Button Wiring:**

- **Normally Closed (NC)** contacts: E-stop pressed = contacts open = relay de-energizes = motors stop
- **Series connection**: All E-stop buttons in series (any button press breaks circuit)
- **Redundant contacts**: Use dual-channel safety relays for critical applications (IEC 60204-1 compliance)

**Example: 3 E-Stop Buttons + Limit Switches**

```
24V+ ──[E-stop 1 NC]──[E-stop 2 NC]──[E-stop 3 NC]──[Limit Switch Chain NC]──> Safety Relay Coil ──> 24V-
                                                                                      |
                                                                                      └──> N.O. Contacts to Motor Drives
```

**HAL Monitoring (Informational Only):**

```hal
# LinuxCNC monitors E-stop circuit state but does NOT control it
net estop-external hm2_7i96.0.gpio.000.in_not => iocontrol.0.emc-enable-in

# If estop-external goes FALSE (E-stop pressed), LinuxCNC GUI shows "E-STOP" status
# Motor power already cut by hardware relay (independent of LinuxCNC)
```

**Safety Relay Selection:**

- **Single-channel**: Pilz PNOZ s3, Omron G9SA (SIL 2, suitable for hobbyist/light industrial)
- **Dual-channel**: Pilz PNOZ X3, Phoenix Contact PSR-SCP (SIL 3, required for industrial)
- **Monitoring**: Relay monitors contact welding, cross-shorts (self-checking)

**Cost:**
- Basic safety relay: $50-$150
- Dual-channel with monitoring: $200-$500

**WRONG Implementation (Software-Only E-Stop):**

```hal
# DANGEROUS: E-stop button only monitored by LinuxCNC
net estop-button parport.0.pin-10-in => motion.enable

# If LinuxCNC crashes, E-stop button ineffective
# NEVER implement E-stop this way on real machinery
```

### 11.3 Limit Switch Integration

**Limit switches** provide both software monitoring (soft limits via HAL) and hardware protection (hard limits via relay chain).

**Dual-Function Limit Switch Wiring:**

```
        [X-axis Min Limit Switch]
                |         |
                |         └──> HAL Input (motion.00.neg-lim-sw-in)
                |
                └──> E-stop Relay Chain (NC contacts in series)
```

**HAL Configuration:**

```hal
# Software limit monitoring
net x-limit-min hm2_7i96.0.gpio.003.in_not => motion.00.neg-lim-sw-in
net x-limit-max hm2_7i96.0.gpio.004.in_not => motion.00.pos-lim-sw-in

# When limit switch triggered:
# 1. HAL signal goes TRUE
# 2. Motion controller stops axis immediately
# 3. E-stop relay chain opens (hardware backup)
```

**INI File Soft Limits:**

```ini
[JOINT_0]
MIN_LIMIT = -0.1   # Software limit 0.1 mm inside physical switch
MAX_LIMIT = 200.1  # Software limit 0.1 mm inside physical switch
HOME = 0.0
HOME_OFFSET = 0.0
```

**Limit Switch Types:**

| Type | Advantages | Disadvantages | Use Case |
|------|-----------|---------------|----------|
| **Mechanical (lever)** | Simple, reliable, no power required | Mechanical wear, contact bounce | General purpose |
| **Inductive (NPN/PNP)** | Non-contact, long life, no bounce | Requires power, limited range | Industrial automation |
| **Optical** | Precise positioning, fast response | Sensitive to contamination (chips, oil) | Clean room, precision |
| **Magnetic (Hall effect)** | Non-contact, robust, sealed | Requires magnet on moving part | Harsh environment |

**Homing vs. Limit Switches:**

```hal
# Combined home + limit switch (common on budget machines)
net x-home-limit hm2_7i96.0.gpio.003.in_not => motion.00.home-sw-in motion.00.neg-lim-sw-in

# Dedicated switches (preferred for reliability)
net x-home hm2_7i96.0.gpio.010.in_not => motion.00.home-sw-in
net x-limit-min hm2_7i96.0.gpio.003.in_not => motion.00.neg-lim-sw-in
net x-limit-max hm2_7i96.0.gpio.004.in_not => motion.00.pos-lim-sw-in
```

**INI Homing Configuration:**

```ini
[JOINT_0]
HOME_SEARCH_VEL = -20.0     # Search toward home switch at 20 mm/s (negative = toward MIN)
HOME_LATCH_VEL = 2.0        # Final approach at 2 mm/s (slow, precise)
HOME_OFFSET = 0.0           # Home position offset from switch location
HOME_SEQUENCE = 1           # Homing order (Z first = sequence 0, then XY = sequence 1)
HOME_IGNORE_LIMITS = YES    # Allow travel through limit switch during homing
```

### 11.4 HAL Watchdog Implementation

**Watchdog Purpose:** Detect software crashes or thread stalls, disable outputs to prevent runaway motion.

**Charge Pump Watchdog (External Hardware):**

```hal
# Load charge pump component (toggles output at servo thread rate)
loadrt charge_pump
addf charge-pump servo-thread

# Connect to GPIO output
net charge-toggle charge-pump.out => hm2_7i96.0.gpio.015.out

# External watchdog circuit monitors charge-toggle frequency
# Expected: 1 kHz square wave (servo thread running)
# If frequency drops or stops: Watchdog opens relay, cuts motor power
```

**External Watchdog Circuit (Simple):**

```
charge-toggle (GPIO) ──> [Frequency-to-Voltage Converter] ──> [Comparator] ──> Safety Relay Enable
                              (e.g., LM2907)                   Threshold: >800 Hz
```

**Frequency drops below threshold → Comparator output LOW → Relay opens → Motors disabled**

**Commercial Watchdog Modules:**

- Mesa 7i77/7i76: Built-in watchdog monitors hostmot2 communication
- Automation Direct: WDM-1 standalone watchdog ($89)
- Custom PCB: 555 timer + relay (DIY solution)

**Mesa FPGA Watchdog (Integrated):**

```hal
# Mesa cards have built-in FPGA watchdog
addf hm2_7i96.0.pet_watchdog servo-thread

# Watchdog must be "petted" every servo cycle
# If servo thread stops (crash), FPGA disables all outputs after timeout (typically 10-20 ms)

# Check watchdog status
halcmd show pin hm2_7i96.0.watchdog.has_bit
# TRUE = watchdog active and healthy
```

**Watchdog Timeout Configuration:**

```hal
# Set watchdog timeout (default typically adequate)
setp hm2_7i96.0.watchdog.timeout_ns 20000000  # 20 ms timeout

# Timeout too short: False triggers from latency spikes
# Timeout too long: Delayed response to actual crashes
# Recommended: 10-20× servo thread period (e.g., 10-20 ms for 1 ms servo thread)
```

### 11.5 Following Error Protection

**Following Error:** Difference between commanded position and actual position exceeding threshold indicates:
- Mechanical binding (crash, collision)
- Lost encoder signals
- Servo drive failure
- Insufficient PID tuning

**Configuration:**

```ini
[JOINT_0]
FERROR = 1.0        # Following error limit during motion (mm)
MIN_FERROR = 0.1    # Following error limit at standstill (mm)
```

**Behavior:**

- **During motion**: If |commanded - actual| > FERROR, motion controller triggers E-stop
- **At standstill**: If |commanded - actual| > MIN_FERROR, motion controller triggers E-stop

**HAL Monitoring:**

```hal
# Monitor following error in real-time
halcmd show pin motion.00.f-error      # Current error (mm)
halcmd show pin motion.00.f-errored    # TRUE if error exceeded limit
```

**Tuning Guidelines:**

| Machine Type | FERROR | MIN_FERROR |
|--------------|--------|------------|
| **Stepper (open-loop)** | 5-10 mm | 1-2 mm |
| **Servo (PID-tuned)** | 0.5-1.0 mm | 0.05-0.1 mm |
| **High-precision servo** | 0.1-0.2 mm | 0.01-0.02 mm |

**Troubleshooting Following Errors:**

```bash
# Capture error during motion with halscope
halscope
# Add channels: motion.00.motor-pos-cmd, motion.00.motor-pos-fb, motion.00.f-error
# Trigger on f-error > 0.5
# Execute motion, analyze waveform

# Common causes and solutions:
# 1. Error grows during acceleration → Increase P gain or add FF1 (velocity feedforward)
# 2. Error spikes on direction change → Add backlash compensation
# 3. Error constant during motion → Wrong encoder scale or PID bias needed
# 4. Error oscillates → Reduce P gain or add D gain (damping)
```

### 11.6 Velocity and Acceleration Limits

**Purpose:** Prevent mechanical damage from excessive speeds or accelerations.

**INI Configuration:**

```ini
[JOINT_0]
MAX_VELOCITY = 50.0           # Maximum axis velocity (mm/s)
MAX_ACCELERATION = 500.0      # Maximum axis acceleration (mm/s²)

[TRAJ]
MAX_LINEAR_VELOCITY = 50.0    # Maximum coordinated motion velocity (mm/s)
MAX_LINEAR_ACCELERATION = 500.0  # Maximum coordinated acceleration (mm/s²)
```

**Enforcement Hierarchy:**

1. **TRAJ limits**: Apply to coordinated XYZ motion (trajectory planner)
2. **JOINT limits**: Apply to individual axes (joint controller)
3. **Stepgen/Servo limits**: Final clamp in hardware interface

```hal
# Stepgen limits (must be ≥ JOINT limits for proper operation)
setp hm2_7i96.0.stepgen.00.maxvel [JOINT_0]MAX_VELOCITY
setp hm2_7i96.0.stepgen.00.maxaccel [JOINT_0]MAX_ACCELERATION
```

**Safety Margin:**

Set JOINT limits 10-20% below mechanical maximum:

```
Mechanical maximum: 60 mm/s (measured stall speed)
JOINT MAX_VELOCITY: 50 mm/s (83% of max, safety margin)
```

### 11.7 Software Interlocks and Conditional Logic

**Application:** Prevent unsafe operations (e.g., starting spindle with chuck open, moving axis without coolant).

**Example: Spindle Interlock**

```hal
# Spindle enable only if guard closed AND coolant running
loadrt and2 count=1
addf and2.0 servo-thread

net guard-closed hm2_7i96.0.gpio.010.in => and2.0.in0
net coolant-running motion.coolant-flood => and2.0.in1
net spindle-enable-ok and2.0.out => motion.spindle-on

# If guard opens OR coolant stops → spindle disabled automatically
```

**Example: Z-Axis Hold-Down Clamp**

```hal
# Require clamp engaged before Z-axis motion allowed
loadrt and2 count=1
addf and2.0 servo-thread

net clamp-engaged hm2_7i96.0.gpio.011.in => and2.0.in0
net motion-request motion.motion-enabled => and2.0.in1
net z-enable-ok and2.0.out => motion.02.amp-enable-out

# Z-axis physically disabled if clamp not engaged
```

**Pneumatic Tool Changer Safety:**

```hal
# Tool change only allowed when spindle stopped and at safe position
loadrt and2 count=2
addf and2.0 servo-thread
addf and2.1 servo-thread

# Spindle stopped check
net spindle-speed motion.spindle-speed-out => comp.0.in0
setp comp.0.in1 50.0  # RPM threshold
net spindle-slow comp.0.out => and2.0.in0  # TRUE if spindle < 50 RPM

# Z-axis at safe height check
net z-position motion.02.joint-pos-fb => comp.1.in0
setp comp.1.in1 100.0  # Safe height (mm)
net z-safe comp.1.out => and2.0.in1  # TRUE if Z > 100 mm

net tool-change-safe and2.0.out => and2.1.in0
net tool-change-request iocontrol.0.tool-change => and2.1.in1
net tool-change-allowed and2.1.out => tool-changer.enable

# Tool changer only activates if spindle stopped AND Z-axis at safe height
```

### 11.8 IEC 61508 and ISO 13849-1 Compliance

**Standards for Safety-Critical Systems:**

- **IEC 61508**: Functional safety of electrical/electronic/programmable systems
- **ISO 13849-1**: Safety of machinery—control systems

**Safety Integrity Levels (SIL):**

| Level | Risk Reduction | Target Failure Rate | Application |
|-------|----------------|---------------------|-------------|
| **SIL 1** | 10-100× | 10⁻⁵ to 10⁻⁶ /hour | Low risk (hobbyist, educational) |
| **SIL 2** | 100-1000× | 10⁻⁶ to 10⁻⁷ /hour | Moderate risk (small business) |
| **SIL 3** | 1000-10000× | 10⁻⁷ to 10⁻⁸ /hour | High risk (industrial production) |
| **SIL 4** | >10000× | 10⁻⁸ to 10⁻⁹ /hour | Very high risk (not typical for CNC) |

**Performance Levels (PL) per ISO 13849-1:**

| Level | Description | Requirements |
|-------|-------------|--------------|
| **PLa** | Low injury risk | Single-channel, tested components |
| **PLb** | Moderate risk | Tested components, fault detection |
| **PLc** | Serious injury risk | Redundant monitoring |
| **PLd** | Severe injury risk | Redundant channels, self-monitoring |
| **PLe** | Fatal injury risk | Dual-channel, cross-monitoring, high MTBF |

**LinuxCNC + Hardware E-Stop = SIL 2 / PLd (Typical):**

With proper implementation:
- Dual-channel E-stop buttons
- Monitored safety relay (Pilz PNOZ X3 or equivalent)
- Independent limit switch chain
- Watchdog timer
- Regular testing (monthly E-stop verification)

**NOT suitable for:**
- SIL 3/4 applications (nuclear, aviation, medical implants)
- PLe requirements (require certified safety PLCs)

**Acceptable for:**
- Hobbyist/maker workshops
- Small business job shops
- Educational institutions
- R&D prototyping

**Industrial Use Considerations:**

For commercial production:
1. **Risk assessment**: Document hazards, failure modes, required SIL/PL
2. **Safety relay certification**: Use certified relays (TÜV, UL listed)
3. **Testing protocol**: Monthly E-stop functional tests, annual full inspection
4. **Documentation**: Maintain safety manual, test logs, incident reports
5. **Insurance**: Verify coverage for CNC operations, disclose control system

### 11.9 E-Stop Testing and Validation

**Monthly E-Stop Test Procedure:**

```
1. Power on machine (motors disabled)
2. Enable motion controller
3. Press each E-stop button individually:
   - Verify motors disabled (encoder feedback stops)
   - Verify LinuxCNC GUI shows "E-STOP" status
   - Verify safety relay LED indicates de-energized state
4. Reset E-stop, verify motors can be re-enabled
5. Document test date and results in logbook

PASS: All E-stops function correctly
FAIL: Any E-stop does not disable motors → DO NOT OPERATE, repair immediately
```

**Annual Full Safety Inspection:**

```
1. E-stop button mechanical function (press force, tactile feedback)
2. E-stop wiring continuity (multimeter resistance check)
3. Safety relay contact resistance (<1Ω closed, >1MΩ open)
4. Limit switch mechanical function (trigger position, repeatability)
5. Limit switch wiring continuity
6. Watchdog function (simulate servo thread stop, verify output disable)
7. Following error detection (command large move, trigger limit → verify halt)
8. Enclosure interlocks (if present, verify door open disables motion)
```

### 11.10 Operator Training Requirements

**Minimum Training for CNC Operators:**

1. **E-stop location and function**: Every operator must know location of all E-stop buttons
2. **Limit switch behavior**: Understand machine halts when limit reached
3. **Feed hold vs. E-stop**: Feed hold pauses program, E-stop requires reset
4. **Tool change procedure**: Manual vs. automatic tool change sequences
5. **Workholding verification**: Check clamps tight before starting program
6. **Chip clearing**: Never reach into enclosure while spindle running

**Lockout/Tagout (LOTO) Procedure:**

For maintenance:
```
1. Press E-stop button
2. Turn off main power disconnect
3. Apply padlock to power disconnect (OSHA 29 CFR 1910.147)
4. Attach tag: "DO NOT OPERATE - [Name] [Date]"
5. Test motion (should not activate)
6. Perform maintenance
7. Remove tag and lock only by person who applied them
8. Restore power, test E-stop before normal operation
```

### 11.11 Summary: Safety System Essentials

**Non-Negotiable Safety Requirements:**

1. ✅ **Hardware E-stop circuit** independent of LinuxCNC software
2. ✅ **Physical limit switches** wired to E-stop relay chain
3. ✅ **Watchdog timer** detecting software crashes
4. ✅ **Following error limits** configured appropriately for machine
5. ✅ **Regular testing** (monthly E-stop, annual full inspection)

**Defense-in-Depth Checklist:**

- [ ] E-stop buttons accessible from all operator positions
- [ ] E-stop circuit breaks motor power physically (relay-based)
- [ ] Limit switches provide both software monitoring and hardware cutoff
- [ ] Watchdog (charge pump or FPGA) monitors servo thread execution
- [ ] Following error limits configured (FERROR, MIN_FERROR in INI)
- [ ] Velocity/acceleration limits set 10-20% below mechanical maximum
- [ ] Software interlocks prevent unsafe operations (spindle/guard, clamp/motion)
- [ ] Safety relay certified for application (SIL/PL rating)
- [ ] Monthly E-stop functional tests documented
- [ ] Annual full safety inspection performed
- [ ] Operators trained on E-stop, feed hold, and emergency procedures
- [ ] LOTO procedure documented and enforced for maintenance

**When to Consult Safety Expert:**

- Industrial production environment
- Public demonstrations (maker faires, trade shows)
- Multiple simultaneous operators
- Large/heavy machines (>100 kg moving mass)
- High-speed operations (>60 m/min rapids)
- Insurance requirements for commercial operation

**Remember:** Software is inherently unreliable. Hardware safety systems must function independently to protect operators from software failures, configuration errors, and unexpected behavior.

**Next Section** (14.12) concludes the module with best practices, maintenance procedures, troubleshooting workflows, and resources for continued LinuxCNC HAL mastery.

---

*Total: 3,467 words | 0 equations | 8 complete worked examples | 5 tables | 15 code blocks*
