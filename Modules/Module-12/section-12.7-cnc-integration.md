## 7. CNC Integration and Motion Control

### 7.1 Control System Architecture

Water-jet guided laser systems require coordinated control of three subsystems: (1) CNC motion controller managing X-Y-Z axis positioning, (2) laser power supply with analog/digital modulation interface, and (3) high-pressure pump with pressure setpoint control. Integration complexity exceeds conventional laser or waterjet systems due to timing-critical synchronization—laser must not fire until pump reaches pressure setpoint AND water flow confirmed, while motion must not begin until laser coupling stabilizes (100-500 ms laser-on delay).

**Control Hierarchy:**

```
Level 1: Safety PLC (Hardware Interlocks)
  ├─ E-stop circuit monitoring
  ├─ Door/enclosure interlocks
  └─ Pressure overshoot protection

Level 2: Motion Controller (CNC)
  ├─ G-code parsing and execution
  ├─ X-Y-Z axis coordination (LinuxCNC, Mach4, or proprietary)
  └─ M-code processing (laser/pump control)

Level 3: Subsystem Controllers
  ├─ Laser driver (power modulation, temperature monitoring)
  ├─ Pump controller (pressure regulation, accumulator management)
  └─ Auxiliary systems (water filtration, cooling, extraction)
```

**Signal Interface Requirements:**

| Signal | Direction | Type | Purpose | Typical Specification |
|--------|-----------|------|---------|----------------------|
| **Laser Enable** | CNC → Laser | Digital Out | Enable/disable laser emission | 24V DC or dry contact |
| **Laser Power** | CNC → Laser | Analog Out | Power modulation 0-100% | 0-10V DC or 4-20 mA |
| **Laser Ready** | Laser → CNC | Digital In | Laser at temperature, ready | Normally open relay |
| **Pump Enable** | CNC → Pump | Digital Out | Start/stop pump operation | 24V DC or dry contact |
| **Pressure Setpoint** | CNC → Pump | Analog Out | Target pressure command | 4-20 mA (3,000-6,000 bar) |
| **Pressure OK** | Pump → CNC | Digital In | Pressure within tolerance | NO relay, ±2% window |
| **Flow OK** | Sensor → CNC | Digital In | Water flow detected | Turbine flow switch >0.08 L/min |
| **E-stop Status** | Safety → All | Digital | Emergency stop activated | Series NC contacts |

### 7.2 Start-Up Sequence and Interlock Logic

Proper sequencing prevents system damage (laser firing into dry nozzle, motion beginning before coupling stabilizes).

**Power-On Sequence:**

```
1. System power applied → Safety PLC self-test (0-2 s)
2. Enclosure door closed AND E-stop reset → Enable subsystems (2-5 s)
3. CNC motion controller boot → Home all axes (5-30 s)
4. Pump standby mode → Maintain 500 bar pilot pressure (continuous)
5. Laser chiller running → Fiber temperature <25°C (30-120 s)
6. System ready → Indicator lamp green, accept G-code program
```

**Cutting Cycle Sequence:**

```
Start Cycle (M3 command or cycle start button)
  ↓
1. Pump Ramp-Up (0-3 s)
   - Pressure increases from 500 bar standby to 5,000 bar setpoint
   - Accumulator charges, pressure ripple stabilizes
   - "Pressure OK" signal asserted when within ±100 bar (±2%)
  ↓
2. Laser Enable (after Pressure OK = TRUE)
   - Laser driver enables diode pumps
   - Power ramps to setpoint over 100-300 ms
   - "Laser Ready" signal asserted at 95% power
  ↓
3. Coupling Stabilization Delay (100-500 ms)
   - Allow water jet to stabilize
   - Laser-water coupling efficiency reaches steady-state
   - (Programmable delay, material/thickness dependent)
  ↓
4. Motion Begins
   - CNC releases axis hold
   - X-Y traverse begins at programmed feed rate
   - Z-axis maintains standoff via closed-loop control
  ↓
5. Cutting in Progress
   - Continuous monitoring: Pressure OK, Laser Ready, Flow OK
   - If ANY fault → immediate laser disable, axes decelerate
  ↓
6. Motion Complete
   - Axes decelerate to stop
   - Dwell 50-200 ms (complete cut at corner)
  ↓
7. Laser Disable (M5 command)
   - Laser power ramps down over 50-100 ms
   - Diode pumps disabled
  ↓
8. Pump Ramp-Down (0-2 s)
   - Pressure decreases to 500 bar standby
   - Accumulator bleeds down
  ↓
End Cycle
```

**Critical Interlock Logic (AND gates, all must be TRUE for laser operation):**

$$\text{Laser\_Enable} = \text{E-stop OK} \land \text{Door Closed} \land \text{Pressure OK} \land \text{Flow OK} \land \text{Motion Ready}$$

If ANY condition becomes FALSE during cutting → laser disables within 10 ms (hardware-enforced)

### 7.3 G-Code Considerations for WGL Systems

Standard G-code (RS-274) requires extensions for WGL-specific operations.

**M-Code Definitions (Typical Implementation):**

| M-Code | Function | Parameters | Example |
|--------|----------|------------|---------|
| **M3** | Laser/pump ON (spindle on analog) | S = power (0-100%) | M3 S80 (80% power) |
| **M5** | Laser/pump OFF | None | M5 |
| **M7** | Auxiliary water ON (coolant) | None | M7 (for table wash) |
| **M8** | Shield gas ON (if equipped) | None | M8 |
| **M9** | Auxiliary water/gas OFF | None | M9 |
| **M51** | Pressure setpoint 1 (e.g., 4,000 bar) | None | M51 (thin materials) |
| **M52** | Pressure setpoint 2 (e.g., 5,000 bar) | None | M52 (standard) |
| **M53** | Pressure setpoint 3 (e.g., 6,000 bar) | None | M53 (thick materials) |

**Pierce Delay (G04 Dwell):**

Unlike plasma (2-5 s pierce) or laser (<0.1 s pierce), WGL requires 0.2-1.0 s delay after M3 for pressure/coupling stabilization:

```gcode
G00 X10 Y20           (Rapid to pierce point)
M3 S100               (Laser/pump ON, 100% power)
G04 P0.5              (Dwell 0.5 seconds - stabilization)
G01 X50 Y20 F300      (Begin cutting at 300 mm/min)
```

**Corner Slowdown:**

Sharp corners (<90° included angle) require feed rate reduction to prevent jet deflection and coupling loss:

```gcode
G01 X100 Y0 F400      (Straight cut at 400 mm/min)
G01 X100 Y100 F250    (90° corner, reduce to 250 mm/min)
G01 X0 Y100 F400      (Straight cut, restore full speed)
```

**Automatic corner slowdown** (if supported by CNC controller):
- LinuxCNC: Path tolerance setting limits corner velocity
- Mach4: Corner rounding or CV (constant velocity) mode
- Industrial controllers (Siemens, Fanuc): Built-in corner deceleration algorithms

### 7.4 LinuxCNC HAL Configuration Example

LinuxCNC's Hardware Abstraction Layer (HAL) enables flexible WGL integration (Module 14).

**HAL Component Connections:**

```hal
# Load components
loadrt wgl_control (custom component for WGL-specific logic)
loadrt pid count=1 (PID controller for Z-axis height control)

# Motion outputs to laser
net laser-enable <= motion.spindle-on => wgl-laser.enable
net laser-power <= motion.spindle-speed-out => wgl-laser.power-cmd
# (spindle-speed-out scaled 0-1.0, multiply by 100 for percentage)

# Motion outputs to pump
net pump-enable <= motion.digital-out-00 => wgl-pump.enable
net pump-pressure <= motion.analog-out-00 => wgl-pump.pressure-setpoint
# (analog-out-00 scaled for 4-20 mA: 3,000-6,000 bar)

# Subsystem status inputs to motion
net pressure-ok <= wgl-pump.pressure-ok => motion.digital-in-00
net flow-ok <= wgl-flow-sensor.status => motion.digital-in-01
net laser-ready <= wgl-laser.ready => motion.digital-in-02

# Interlock logic (all must be true for motion enable)
net motion-enable <= motion.digital-in-00 
net motion-enable <= motion.digital-in-01
net motion-enable <= motion.digital-in-02
net motion-enable => motion.motion-enabled

# E-stop chain (hardware-enforced)
net estop-external <= input.0.estop-button => iocontrol.emc-enable-in
```

**Custom HAL Component Functions:**

```c
// wgl-control.c - Custom HAL component for WGL sequencing
component wgl_control;

pin in bit laser_enable_req;    // Request from motion controller
pin out bit laser_enable_out;   // Actual enable to laser driver
pin in bit pressure_ok;          // Pressure within tolerance
pin in bit flow_ok;              // Water flow detected
pin in float stabilization_delay; // Delay after M3 before motion (seconds)

function _;

//@ Implementation: Delay laser enable until pressure OK AND flow OK
//@ Then maintain delay timer before asserting motion-ready signal
```

### 7.5 Z-Axis Height Control (Standoff Maintenance)

Maintaining constant standoff distance (1.5-2.5 mm) despite workpiece height variations requires closed-loop Z-axis control.

**Sensing Methods:**

**1. Capacitive Proximity Sensor:**
- Range: 0.5-5 mm
- Resolution: ±0.01 mm
- Output: 0-10V proportional to distance
- Advantages: Non-contact, immune to water/metal debris
- Disadvantages: Calibration required per material (dielectric constant varies)

**2. Laser Triangulation Sensor:**
- Range: 2-20 mm
- Resolution: ±0.005 mm
- Output: Analog voltage or digital (RS-485)
- Advantages: High accuracy, material-independent
- Disadvantages: Cost ($500-1,500), sensitive to mist/splashing

**3. Conductive Touch Probe (Initial Height Setting Only):**
- Touch workpiece surface before cutting
- Set Z=0 datum
- Then maintain programmed offset (e.g., Z=2.0 mm)
- Advantages: Simple, accurate initial setting
- Disadvantages: No real-time correction during cutting

**Closed-Loop Z-Control (PID Algorithm):**

$$u(t) = K_p e(t) + K_i \int e(t) dt + K_d \frac{de(t)}{dt}$$

where:
- $u(t)$ = motor command (velocity or position adjustment)
- $e(t)$ = error (target standoff - measured standoff)
- $K_p$ = proportional gain (typical 2-5 mm/s per mm error)
- $K_i$ = integral gain (eliminates steady-state error, 0.5-2 mm/s per mm·s)
- $K_d$ = derivative gain (damping, 0.1-0.5 mm/s per mm/s)

**Tuning Procedure:**
1. Set $K_i = K_d = 0$, increase $K_p$ until oscillation occurs
2. Reduce $K_p$ to 50% of oscillation threshold
3. Add $K_i$ to eliminate steady-state offset (start with $K_i = K_p / 10$)
4. Add $K_d$ if overshoot occurs (start with $K_d = K_p / 20$)

**Response time:** <50 ms (maintains standoff over ±1 mm/s workpiece height changes)

### 7.6 Feed Rate Override and Adaptive Control

Real-time feed rate adjustment optimizes cutting based on sensor feedback.

**Manual Override (Operator Control):**
- Feed rate dial: 10-150% of programmed value
- Common during setup: Run first part at 50-70% to verify parameters
- Production: Lock override at 100% (prevent operator variation)

**Automatic Adaptive Control (Advanced Systems):**

**Input Signals:**
- Acoustic emission intensity (cutting effectiveness indicator)
- Laser transmission power (coupling efficiency monitor)
- Z-axis load (contact force if excessive)

**Control Logic:**

```
IF (acoustic_emission < threshold_low):
    feed_rate = feed_rate × 0.90  # Reduce 10% - incomplete cut
ELIF (acoustic_emission > threshold_high):
    feed_rate = feed_rate × 1.05  # Increase 5% - cutting well
ELSE:
    feed_rate = feed_rate  # Maintain current rate

Limit: 0.70 × programmed_feed ≤ feed_rate ≤ 1.20 × programmed_feed
```

**Benefit:** Compensates for material thickness variations (±0.5 mm typical in production stock) without operator intervention

### 7.7 Multi-Head Coordination (Production Systems)

High-throughput systems employ 2-4 cutting heads on single gantry.

**Configurations:**

**1. Tandem (Same-Part Duplication):**
- Two heads spaced 500-1,000 mm apart
- Cut identical parts simultaneously
- Throughput: 2× single-head
- Synchronization: Master-slave control (both heads follow same G-code with X-offset)

**2. Independent (Different Parts):**
- Each head executes separate G-code program
- Requires collision avoidance logic (minimum separation 200 mm enforced)
- Throughput: 2× for different parts
- Synchronization: Independent CNC channels

**Collision Avoidance Algorithm:**

$$\text{IF} \quad \sqrt{(X_1 - X_2)^2 + (Y_1 - Y_2)^2} < D_{min} \quad \text{THEN halt motion}$$

where $D_{min} = 200$ mm (safety separation)

### 7.8 Integration Checklist and Commissioning

**Pre-Commissioning Verification:**

✅ **Electrical:**
- Signal wiring verified per schematic (laser, pump, sensors)
- Interlock circuits tested (E-stop, door switches)
- Ground continuity <0.1 Ω (plasma ground to CNC ground to earth)

✅ **Pneumatic/Hydraulic:**
- Pressure transducers calibrated (±1% accuracy)
- Accumulator pre-charge verified (N₂ pressure 60-70% of operating pressure)
- Leak test: Hold 5,000 bar for 10 minutes, <1% pressure drop

✅ **Software:**
- HAL configuration loaded and tested (all signals respond)
- M-code definitions verified (M3 enables laser AND pump)
- Feed rate limits set (max 5,000 mm/min prevents jet deflection)

✅ **Mechanical:**
- All axes homed successfully
- Repeatability test: ±0.02 mm over 10 cycles
- Nozzle alignment verified (coupling efficiency >75%)

**First-Article Test:**
1. Cut 100 mm square in 3 mm stainless steel
2. Measure: Kerf width (target 0.10-0.15 mm), edge roughness (Ra <2 μm), dimensional accuracy (±0.05 mm)
3. If within specification → proceed to production
4. If out-of-spec → adjust parameters (Section 6.6)

Mastering CNC integration—signal interfacing, interlock logic, G-code extensions, LinuxCNC HAL configuration, and Z-axis height control—enables reliable WGL operation with 99%+ uptime and consistent part quality across production runs.

***

---

## References

1. **ISO 11553 Series** - Safety of machinery - Laser processing machines
2. **ANSI Z136.1-2014** - Safe Use of Lasers
3. **ISO 9013:2017** - Thermal cutting - Classification of thermal cuts
4. **Steen, W.M. & Mazumder, J. (2010).** *Laser Material Processing* (4th ed.). Springer
5. **Flow International Waterjet Technology Handbook** - Hybrid system applications
6. **TRUMPF TruLaser Technical Documentation** - Combined processing systems
7. **Hashish, M. (2014).** "Hybrid Waterjet-Laser Cutting Technology." *Journal of Manufacturing Processes*
