# 10.6 Force Control and Compliance

Force control enables robots to interact with the environment through regulated contact forces, essential for assembly, finishing, and collaborative operations.

## Force Sensing

### Wrist-Mounted Force/Torque Sensors

**Six-Axis F/T Sensor**

Measurement Axes:
- Three forces: Fx, Fy, Fz
- Three torques: Tx, Ty, Tz
- All referenced to sensor coordinate frame

Construction:
- Strain gauges on flexure element
- Wheatstone bridge circuits
- Temperature compensation
- Overload protection (mechanical stops)

Specifications:
- Force range: ±10N to ±1000N (typical)
- Torque range: ±1Nm to ±100Nm
- Resolution: 0.1% to 0.01% of full scale
- Accuracy: 0.5% to 2% of full scale
- Sample rate: 1-10 kHz

Mounting:
- Between robot flange and tool
- Adds 10-30mm height
- Weight: 0.2-2 kg depending on capacity
- Calibration matrix provided by manufacturer

**Signal Processing**

Raw Sensor Data:
- Six voltage channels (Fx, Fy, Fz, Tx, Ty, Tz)
- Amplified and digitized
- Transmitted via analog, serial, or Ethernet

Calibration:
- Converts voltages to force/torque values
- Accounts for cross-talk between axes
- Temperature compensation

Filtering:
- Low-pass filter (10-100 Hz typical)
- Remove sensor noise and vibration
- Balance responsiveness vs. noise

Bias Removal:
- Zero sensor with tool mounted (no contact)
- Subtract tool weight and inertia
- Leaves only external contact forces

**Manufacturers**
- ATI Industrial Automation (most common)
- OnRobot
- Schunk
- Robotiq

### Joint Torque Sensing

**Direct Torque Measurement**

Methods:
- Strain gauges on joint shafts
- Measure torsional deflection
- Convert to torque

Advantages:
- No external sensor needed
- Measures actual joint torque
- Can detect collisions anywhere on robot

Disadvantages:
- Complex installation
- Temperature sensitivity
- Calibration challenges

**Motor Current Sensing**

Indirect Force Measurement:
- Motor current proportional to torque
- Already measured by servo drives
- No additional hardware

Calculation:
```
τ_joint = Kt × I_motor × GR
```
Where:
- Kt = motor torque constant
- I_motor = motor current
- GR = gear ratio

Limitations:
- Includes friction and inertia (not just external forces)
- Less accurate than dedicated sensors
- Requires good dynamic model

Model-Based Estimation:
```
τ_external = τ_measured - τ_model
```
Subtract expected torques from model, leaving external forces.

**Collaborative Robots**

Integrated Torque Sensing:
- All joints have torque sensors
- Safety-rated monitoring
- Detect contact forces throughout workspace
- Examples: KUKA LBR iiwa, Franka Emika, ABB GoFa

## Force Control Strategies

### Position Control with Force Limit

**Simple Force Limiting**

Operation:
- Normal position control
- Monitor contact force
- Stop or retract if force exceeds limit

Example - Assembly:
```python
move_to(insertion_approach)
while force_z < max_force:
    move_down(speed=10 mm/s)
    if force_z > max_force:
        retract()
        signal_error()
        break
```

Applications:
- Collision detection
- Protect parts from damage
- Simple contact tasks

### Hybrid Position/Force Control

**Concept**

Control Different Axes Independently:
- Position control on some axes
- Force control on others
- Selection matrix defines which

Example - Surface Following:
- X, Y: Position control (follow programmed path)
- Z: Force control (maintain contact force)

**Implementation**

Selection Matrix S:
```
S = diag([1, 1, 0, 1, 1, 1])
```
Where 1 = position control, 0 = force control.

Control Law:
```
Command = S × Position_Control + (I - S) × Force_Control
```

**Application - Deburring**

Setup:
- Tool follows edge path (X, Y position controlled)
- Z-axis force controlled (press against surface)
- Adapt to surface height variation

Programming:
```
SET_FORCE_CONTROL(Z_AXIS, TARGET_FORCE=20N, STIFFNESS=LOW)
MOVEL START_POS
ENABLE_FORCE_CONTROL()
MOVEL END_POS SPEED=50mm/s
DISABLE_FORCE_CONTROL()
```

### Impedance Control

**Mass-Spring-Damper Model**

Target Behavior:
```
F_external = M×(ẍ - ẍ_desired) + B×(ẋ - ẋ_desired) + K×(x - x_desired)
```

Parameters:
- M: Virtual mass (inertia)
- B: Damping coefficient
- K: Stiffness
- F_external: Measured external force

**Physical Interpretation**

High Stiffness (K):
- Resists displacement from target
- Similar to position control
- Good for precise positioning

Low Stiffness:
- Compliant, easily displaced
- Safe for contact
- Good for assembly, human interaction

High Damping (B):
- Resists velocity
- Smooth, controlled motion
- Prevents oscillation

Low Mass (M):
- Responsive to forces
- Quick adaptation

**Tuning**

Typical Values (Cartesian axes):
- K: 100-5000 N/m
- B: 10-500 Ns/m
- M: 0.1-10 kg (virtual)

Adjustment:
- Start with low stiffness and high damping
- Increase stiffness for precision
- Reduce damping if too sluggish

**Applications**

Assembly:
- Compliant insertion (peg-in-hole)
- Chamfer finding
- Snap-fit operations

Collaborative Operation:
- Robot yields to human push
- Safe, intuitive interaction

### Admittance Control

**Concept**

Opposite of Impedance:
- Measure force
- Calculate desired motion
- Position control to achieve motion

Admittance:
```
ẍ = (1/M) × (F_external - B×ẋ - K×x)
```

Suitable When:
- Position control already excellent (stiff robot)
- Add compliance via software
- No need to modify low-level controller

**Implementation**

In control loop:
1. Read force sensor
2. Calculate desired velocity from force
3. Integrate to get position
4. Send position command to robot

## Passive Compliance

### Mechanical Compliance Devices

**Remote Center Compliance (RCC)**

Design:
- Flexure-based mechanism
- Allows lateral and angular deflection
- Spring returns to center when released

Function:
- Enables peg-in-hole insertion despite misalignment
- No sensors or active control
- Robust and reliable

Specifications:
- Lateral compliance: 0.5-5 mm typical
- Angular compliance: 1-5 degrees
- Center of compliance at tool tip (peg end)

Applications:
- High-speed assembly
- Screw insertion
- Pin insertion

**Elastic Buffers**

Simple Springs or Rubber:
- Absorb impacts
- Reduce peak forces
- Protect robot and part

Design:
- Mount between flange and tool
- Tune stiffness for application
- May include damping

### Passive vs. Active Compliance

**Passive (RCC, Springs)**

Advantages:
- No power or sensors required
- Very fast response (mechanical)
- Reliable, no software bugs
- Lower cost

Disadvantages:
- Fixed compliance (not adjustable)
- No force feedback or data logging
- Limited to specific tasks

**Active (Force Control)**

Advantages:
- Programmable compliance
- Force data available
- Adaptive to different tasks
- More sophisticated behavior

Disadvantages:
- Requires force sensor
- Complex software
- Limited by control loop bandwidth
- Higher cost

**Hybrid Approach**

Combination:
- Passive compliance for fast, local corrections
- Active control for overall force regulation
- Best of both worlds

## Applications of Force Control

### Assembly

**Peg-in-Hole Insertion**

Challenges:
- Tight clearances (0.05-0.2 mm)
- Jamming if misaligned
- Position control alone insufficient

Force Control Strategy:
1. Approach hole with position control
2. Switch to compliant mode (low stiffness)
3. Search for hole (spiral or raster pattern)
4. Detect insertion (force drop)
5. Insert with force limit
6. Detect full insertion (force rise or distance)

Spiral Search:
```python
set_compliance(lateral_stiffness=100, vertical_stiffness=500)
radius = 0
while not inserted():
    angle += 10 degrees
    radius += 0.1 mm
    move_to(center + radius * [cos(angle), sin(angle)])
    if force_z < threshold:
        # Hole found
        break
```

**Snap-Fit Assembly**

Process:
1. Align parts with force feedback
2. Apply increasing force
3. Detect snap (force spike then drop)
4. Verify engagement

Force Profile:
- Gradual increase
- Spike at snap point (10-50N typical)
- Lower holding force after snap

**Press-Fit**

Controlled Force Application:
- Monitor force vs. displacement
- Ensure part fully seated
- Detect anomalies (cross-threading, missing parts)

Quality Assurance:
- Log force profile
- Compare to reference
- Accept/reject based on criteria

### Surface Finishing

**Deburring**

Setup:
- Grinding or cutting tool on robot
- Force control maintains contact
- Follow edge path

Control:
- Target force: 10-50N (depends on material and tool)
- Adapt to surface variations
- Constant material removal rate

**Polishing**

Requirements:
- Consistent surface pressure
- Smooth, continuous motion
- Overlapping tool paths

Force Control:
- Light force (5-20N)
- Compliant to follow contours
- May use compliant backing pad (passive)

**Challenges**

Surface Variations:
- Height changes require Z-axis compliance
- Curvature requires 3D path following
- Irregular shapes benefit from force control

Robot Stiffness:
- Industrial robots less stiff than dedicated machines
- Force control partially compensates
- Best results with stiff robots and light forces

### Contact Inspection

**Product Testing**

Button Feel:
- Press button with controlled force
- Measure displacement and force profile
- Verify tactile response (click, resistance)

Latch Testing:
- Engage and disengage latches
- Measure actuation force
- Detect proper engagement

**Dimensional Probing**

Touch Probe with Force Control:
- Approach surface slowly
- Detect contact (force threshold)
- Record position
- Compliant approach prevents damage

## Implementation Considerations

### Control Loop Architecture

**Rate Requirements**

Force Sensor Sampling:
- 1-10 kHz typical
- Higher rate for stiff contact

Force Control Update:
- 100-1000 Hz typical
- Match or exceed position control rate
- Faster = better stability and responsiveness

**Software Structure**

Real-Time Layer:
- Force sensor reading
- Control law calculation
- Position command output
- Deterministic timing

Non-Real-Time Layer:
- Task planning
- User interface
- Data logging
- Can tolerate latency

### Stability

**Control Stability**

Potential Issues:
- Oscillation from high gains
- Instability from time delays
- Contact/release transitions

Tuning:
- Start with low gains (compliant)
- Increase gradually
- Test with actual contact conditions

**Contact Stability**

Hard Contact:
- Stiff environment (metal-to-metal)
- Requires lower control gains or higher damping
- Prevent chattering

Soft Contact:
- Compliant materials (foam, rubber)
- More forgiving
- Higher gains possible

### Calibration

**Force Sensor Zero**

Procedure:
1. Mount tool on robot
2. Move to known orientation (typically vertical)
3. Capture force reading (tool weight)
4. Store as bias offset
5. Subtract from all future readings

Gravity Compensation:
- Account for tool weight at any robot orientation
- Calculate from tool mass, center of gravity, and orientation
- Subtract from sensor reading

**Tool Center Point**

Force Application Point:
- For torque calculations, need TCP position relative to sensor
- Enter TCP offset in controller
- Affects torque interpretation

### Safety Considerations

**Force Limits**

Maximum Safe Force:
- Depends on application and hazards
- Collaborative robots: ISO/TS 15066 limits (see Section 10.9)
- Industrial applications: Risk assessment

Monitoring:
- Continuous force monitoring
- Threshold triggers stop or retract
- Safety-rated implementation for collaborative mode

**Fault Detection**

Sensor Failures:
- Out-of-range readings
- Communication loss
- Inconsistent data

Response:
- Disable force control
- Revert to position control or stop
- Alert operator

***

**Next**: [10.7 Programming and Simulation](section-10.7-programming.md)

---

## References

1. **ISO 10218-1:2011** - Robots and robotic devices - Safety requirements
2. **ISO 9283:1998** - Manipulating industrial robots - Performance criteria
3. **Denavit, J. & Hartenberg, R.S. (1955).** "A Kinematic Notation for Lower-Pair Mechanisms." *ASME Journal of Applied Mechanics*, 22, 215-221
4. **Craig, J.J. (2017).** *Introduction to Robotics: Mechanics and Control* (4th ed.). Pearson
5. **Lynch, K.M. & Park, F.C. (2017).** *Modern Robotics*. Cambridge University Press
6. **ABB Robot Studio Software** - Robot simulation and programming
7. **KUKA System Software (KSS)** - Robot control and motion planning
