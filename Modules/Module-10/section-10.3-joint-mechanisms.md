# 10.3 Joint Mechanisms and Actuators

Joint design determines robot performance, precision, and reliability. This section covers actuators, transmissions, bearings, and sensors for articulated robot joints.

## Motor Selection

### Servo Motors

**AC Servo Motors**
- Three-phase brushless permanent magnet
- High power density
- Integrated encoder (typically 20-bit absolute)
- Standard for industrial robots
- Rated by continuous torque and peak torque
- Typical sizes: 100W to 5kW per joint

**DC Brushless Servo Motors**
- Similar performance to AC servos
- Simpler drive electronics (for small systems)
- Direct battery operation possible
- Common in collaborative robots

**Motor Specifications**

Torque Requirements:
```
T_motor = (T_load × GR) / η + T_accel
```
Where:
- T_load = Static torque from gravity and forces
- GR = Gear ratio
- η = Transmission efficiency (0.85-0.95)
- T_accel = Torque for acceleration

Example Calculation (Shoulder Joint):
- Arm mass: 5 kg
- Center of gravity: 300 mm from joint
- Load: 2 kg at 500 mm
- Static torque: (5×0.3 + 2×0.5)×9.81 = 24.5 Nm
- Gear ratio: 100:1
- Required motor torque: 24.5/100/0.9 = 0.27 Nm continuous

Add dynamic torque:
- Desired acceleration: 2 rad/s²
- Link inertia: I = 0.5 kg⋅m²
- Dynamic torque: 0.5×2 = 1 Nm at joint
- Motor torque: 1/100 = 0.01 Nm
- Total: 0.27 + 0.01 = 0.28 Nm

Select motor with 0.5-1.0 Nm continuous rating for margin.

**Speed Requirements**
- Typical joint speeds: 90-180 deg/s
- Motor speed = Joint speed × Gear ratio
- Example: 180 deg/s × 100 = 18,000 deg/s = 3000 RPM

**Thermal Considerations**
- RMS torque over duty cycle
- Intermittent rating vs. continuous
- Cooling (natural convection, forced air)
- Derating for elevated temperatures

### Stepper Motors

**Applicability to Robots**

Rarely used in articulated arms due to:
- Lower torque-to-weight ratio
- Step loss under high loads
- No inherent position feedback
- Lower efficiency

Acceptable for:
- Small desktop robots (<1 kg payload)
- Closed-loop steppers (with encoder)
- Educational/hobby projects

**Sizing**
- Safety factor: 3-5× for open-loop
- Closed-loop steppers similar to servos

## Gear Reducers

### Harmonic Drives

**Principle of Operation**

Components:
- Wave generator (elliptical cam with bearings)
- Flexspline (thin flexible cup with external teeth)
- Circular spline (rigid ring with internal teeth)

Operation:
- Wave generator rotates inside flexspline
- Flexspline deforms and meshes with circular spline
- Two teeth difference creates reduction

**Specifications**

Reduction Ratios:
- Common: 50:1, 80:1, 100:1, 120:1, 160:1
- Single-stage reduction

Backlash:
- Typically <1 arcmin (0.017°)
- Near-zero for precision applications

Efficiency:
- 65-85% typical
- Lower than planetary gears
- Heat generation consideration

Torque Capacity:
- Range: 0.5 Nm to 1000+ Nm
- Rated and peak torque specifications

Life Expectancy:
- 3,000 to 10,000 hours typical
- Depends on load, speed, lubrication
- Flexspline is wear component

**Sizing**

Safety Factor:
- Rated torque = Peak load / 2 (minimum)
- Account for shock loads and accelerations

Mounting:
- Typically hollow bore (shaft through center)
- Bolt pattern for motor and output
- Compact package (diameter similar to motor)

**Manufacturers**
- Harmonic Drive LLC (original patent holder)
- Leaderdrive (Chinese alternative, lower cost)
- Sumitomo (SHD series)

### Planetary Gearboxes

**Construction**

Components:
- Sun gear (motor input)
- Planet gears (3-4, rotating around sun)
- Ring gear (fixed housing)
- Planet carrier (output)

Advantages:
- Robust and reliable
- High efficiency (95-98%)
- Lower cost than harmonic drives
- Long service life

Disadvantages:
- Higher backlash (3-10 arcmin typical)
- Can be minimized with preload or dual-stage designs
- Larger package for same reduction

**Reduction Ratios**
- Single stage: 3:1 to 10:1
- Two-stage: 10:1 to 100:1
- Common: 10:1, 20:1, 50:1, 100:1

**Applications in Robots**
- Base and shoulder joints (high torque, backlash acceptable)
- Wrist joints (lighter loads, lower precision requirements)
- Collaborative robots (lower speeds, compliance)

**Manufacturers**
- Apex Dynamics
- Neugart
- Wittenstein
- SEW-Eurodrive

### Cycloidal Drives

**Operation**
- Eccentric input rotates cycloidal disc
- Disc engages with ring gear pins
- High contact ratio (all teeth engaged)

**Characteristics**
- Very low backlash (<1 arcmin)
- High shock load capacity
- Compact and robust
- Efficiency: 85-90%

**Applications**
- Alternative to harmonic drives
- Heavy-duty robots
- Less common in standard designs

### Timing Belt Reduction

**Wrist Joint Applications**

Advantages:
- Lightweight
- Remote motor mounting (reduces wrist inertia)
- Low backlash with proper tension
- Quiet operation

Design:
- GT2 or GT3 profile belts
- Aluminum or steel pulleys
- Reduction via pulley diameter ratio
- Example: 20-tooth drive, 100-tooth driven = 5:1

**Tension and Backlash**
- Spring-loaded tensioner
- Initial tension: 2-3% of belt strength
- Check and adjust periodically
- Backlash <0.1° with proper tension

**Belt Selection**
- Width based on torque
- Length to accommodate pulley spacing
- Reinforced belts (steel or Kevlar cords)

## Bearings

### Types for Robot Joints

**Crossed Roller Bearings**

Construction:
- Rollers arranged perpendicular to each other
- Single compact unit
- High rigidity in all directions

Advantages:
- Extremely compact
- High load capacity (radial, axial, moment)
- Low friction
- Excellent for rotary tables and joints

Disadvantages:
- Expensive
- Sensitive to contamination
- Requires precision housing

**Angular Contact Ball Bearings (Paired)**

Configuration:
- Two bearings in back-to-back or face-to-face arrangement
- Preloaded to eliminate play

Advantages:
- Lower cost than crossed roller
- High speed capability
- Wide availability

Applications:
- Mid-size robot joints
- Speed-critical applications

**Tapered Roller Bearings**

Characteristics:
- Heavy-duty loads
- Adjustable preload via shimming
- Large robots (payloads >50 kg)

**Deep Groove Ball Bearings**

Use:
- Light-duty joints
- Where some play acceptable
- Low cost

### Preload

**Purpose**
- Eliminate play and backlash
- Increase stiffness
- Improve positioning accuracy

**Methods**

Spring Preload:
- Belleville washers or wave springs
- Maintains preload despite wear or temperature
- Moderate stiffness

Rigid Preload:
- Shims or spacers set during assembly
- Maximum stiffness
- Requires precision assembly

Adjustment:
- Too little: Play and vibration
- Too much: Friction, heat, premature wear
- Follow manufacturer specifications

### Sealing

**Protection Requirements**
- Dust and chips (machining environments)
- Liquids (washdown, coolant splash)
- Grease retention

**Seal Types**

Contact Seals:
- Elastomer lip seals
- Effective sealing
- Some friction
- Typical for IP54+

Non-Contact Seals:
- Labyrinth or gap seals
- Lower friction
- Suitable for clean environments

Combination:
- Primary labyrinth seal
- Secondary lip seal
- Best protection for harsh environments

## Brakes

**Purpose**
- Hold position when power removed (safety)
- Prevent back-driving under gravity
- Parking brake for transport/maintenance

**Types**

Electromagnetic Spring-Set Brakes:
- Spring applies brake, electromagnet releases
- Fail-safe (brake on power loss)
- Integrated with motor or gearbox
- Holding torque rated

Permanent Magnet Brakes:
- Active control (PWM) to engage/release
- No holding power required
- More complex control

**Sizing**
- Holding torque ≥ 1.5× maximum static joint torque
- Thermal capacity for repeated operations
- Response time (<100 ms typical)

**Applications**
- Vertical joints (shoulder, elbow)
- Safety requirement per ISO 10218
- Optional for horizontal joints (base rotation)

## Encoders and Feedback

### Encoder Types

**Incremental Encoders**

Operation:
- Outputs pulses for motion
- A and B channels (quadrature) for direction
- Index pulse for homing reference

Resolution:
- 1000-10,000 CPR (counts per revolution) typical
- Higher resolution via quadrature (4× multiplication)
- After gearing: Very high resolution at joint

Advantages:
- Lower cost
- Simple interface
- High resolution available

Disadvantages:
- Lose position on power loss
- Requires homing sequence on startup
- Susceptible to noise (pulse loss)

**Absolute Encoders**

Operation:
- Outputs unique position code (no homing needed)
- Retains position through power cycles
- Multi-turn versions count full rotations

Protocols:
- Parallel (individual wires per bit, rare)
- Serial: SSI, BiSS, EnDat
- Networked: EtherCAT, PROFINET

Resolution:
- Single-turn: 12-20 bits (4096 to 1M positions/rev)
- Multi-turn: Tracks 12-16 additional bits (4096-65536 turns)

Advantages:
- No homing required
- Reliable position data
- Standard for industrial robots

Disadvantages:
- Higher cost
- More complex interfacing

**Resolvers**

Operation:
- Analog sensor with sine/cosine outputs
- Rotating transformer principle
- Requires resolver-to-digital converter

Advantages:
- Very robust (harsh environments)
- Immune to electrical noise
- Infinite resolution (analog)

Disadvantages:
- Lower accuracy than optical encoders
- Bulkier
- Requires specialized interface

Applications:
- Military, aerospace, harsh environments
- Less common in modern industrial robots

### Encoder Mounting

**Motor-Mounted**
- Integral or attached to motor shaft
- Measures motor position
- Gear backlash and compliance not measured
- Standard for servo motors

**Joint-Mounted (Dual Encoder)**
- Second encoder at joint output
- Measures actual joint position
- Compensates for transmission errors
- Used in high-precision systems

**Calibration**
- Encoder zero relative to joint mechanical zero
- Teach mode to define home position
- Store offsets in controller non-volatile memory

## Cable and Hose Routing

**Internal Routing**

Advantages:
- Protected from environment
- Clean appearance
- No snagging on obstacles

Design Requirements:
- Sufficient channel cross-section
- Smooth bends (no sharp corners)
- Support and strain relief
- Access for replacement

**External Routing**

Cable Carriers (Drag Chains):
- Manage cables through joint motion
- Prevent twisting and strain
- Sized for cable bundle diameter

Spiral Cable Wrap:
- Flexible protective sleeving
- Allows limited rotation
- Simpler than drag chains

**Rotary Joint Considerations**

Continuous Rotation:
- Slip rings for electrical signals
- Rotary unions for pneumatic/hydraulic lines
- Expensive, limit maintenance

Limited Rotation:
- Cables routed to allow twist
- Mechanical stops prevent over-rotation
- Typical: ±350° for base joint
- Wrist: Cables through hollow shafts and gearboxes

**Cable Types**

Power Cables:
- Flexible stranded conductors
- Oil-resistant insulation
- Shield for EMI protection

Signal Cables:
- Encoder: Shielded twisted pair
- I/O: Multi-conductor
- Network: Industrial Ethernet (Cat5e/6)

Pneumatic/Hydraulic:
- Flexible hoses rated for pressure
- Push-to-connect or threaded fittings
- Routing to minimize bending stress

## Joint Assembly Example

**Shoulder Joint (Joint 2) for 5kg Payload Robot**

Components:
- Motor: 400W AC servo, 1.3 Nm continuous
- Gearbox: 100:1 harmonic drive
- Bearings: Crossed roller bearing, 150 mm OD
- Encoder: 20-bit absolute, motor-mounted
- Brake: 15 Nm holding torque
- Housing: Aluminum, machined and welded

Assembly:
1. Install crossed roller bearing in housing
2. Mount harmonic drive to bearing outer race
3. Mount motor to harmonic drive input
4. Install brake between motor and gearbox
5. Route cables through hollow shaft
6. Seal housing with gasket and cover
7. Install encoder and calibrate zero position

Testing:
- Friction test (motor current at slow speed)
- Backlash measurement (<1 arcmin target)
- Encoder functionality and calibration
- Brake holding torque verification
- Joint temperature under load

## Performance Considerations

**Backdrivability**

High Ratio Gearboxes:
- Harmonic drives with >100:1 difficult to backdrive
- Planetary gears with <50:1 easily backdriven

Safety Implications:
- Non-backdrivable requires brakes for safety
- Backdrivable allows manual movement (teaching, collision recovery)
- Collaborative robots typically backdrivable

**Friction and Efficiency**

Total Friction:
- Bearing friction (seal type, preload)
- Gear friction (tooth mesh, lubrication)
- Cable drag

Efficiency Chain:
```
η_total = η_bearings × η_gears × η_seals
Example: 0.98 × 0.85 × 0.95 = 0.79 (79%)
```

Low friction important for:
- Energy efficiency
- Heat generation
- Backdrivability
- Force control sensitivity

**Inertia Matching**

Optimal motor-to-load inertia ratio:
```
Ratio = J_load_reflected / J_motor
```

Ideal: 1:1 to 5:1
- Lower ratio: Better dynamic response
- Higher ratio: Motor undersized or load too high

Reflected inertia:
```
J_reflected = J_load / GR²
```

High gear ratios reduce reflected inertia, allowing smaller motors.

***

**Next**: [10.4 End Effectors and Tool Changers](section-10.4-end-effectors.md)

---

## References

1. **ISO 10218-1:2011** - Robots and robotic devices - Safety requirements
2. **ISO 9283:1998** - Manipulating industrial robots - Performance criteria
3. **Denavit, J. & Hartenberg, R.S. (1955).** "A Kinematic Notation for Lower-Pair Mechanisms." *ASME Journal of Applied Mechanics*, 22, 215-221
4. **Craig, J.J. (2017).** *Introduction to Robotics: Mechanics and Control* (4th ed.). Pearson
5. **Lynch, K.M. & Park, F.C. (2017).** *Modern Robotics*. Cambridge University Press
6. **ABB Robot Studio Software** - Robot simulation and programming
7. **KUKA System Software (KSS)** - Robot control and motion planning
