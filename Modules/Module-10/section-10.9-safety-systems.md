# 10.9 Safety Systems

Robotic arms present serious hazards requiring comprehensive safety design. This section covers applicable standards, safeguarding methods, collaborative operation, and safety validation.

## Applicable Standards

### International Standards

**ISO 10218-1: Robots and Robotic Devices - Safety Requirements for Industrial Robots**

Scope:
- Design and construction of industrial robots
- Inherent safety measures
- Safeguarding requirements
- Information for use

Key Requirements:
- Maximum speed in manual mode: 250 mm/s
- Three-position enabling device
- Emergency stop on teach pendant
- Protective stop function
- Safety-rated monitoring

**ISO 10218-2: Robot Systems and Integration**

Scope:
- Integration of robots into complete systems
- Safeguarding of robot cells
- Risk assessment
- Installation and commissioning

Key Concepts:
- Collaborative operation spaces
- Safety functions (STO, SS1, SS2)
- Operator interaction modes
- Performance level requirements

**ISO/TS 15066: Robots and Robotic Devices - Collaborative Robots**

Collaborative Operation:
- Safety-rated monitored stop
- Hand guiding
- Speed and separation monitoring
- Power and force limiting

Biomechanical Limits:
- Maximum allowable contact forces and pressures
- Varies by body region
- Transient vs. quasi-static contact
- Published force/pressure tables

**ISO 13849-1: Safety-Related Parts of Control Systems**

Performance Levels (PL):
- PLa (lowest) to PLe (highest)
- Based on reliability and fault tolerance
- Robot safety functions typically require PLd or PLe

Categories:
- Category B: Basic (single channel)
- Category 1: Well-tried components
- Category 2: Test at intervals
- Category 3: Single fault safe (dual channel)
- Category 4: Single fault safe with fault detection

**ISO 13850: Emergency Stop**

Requirements:
- Category 0 (immediate power removal) or Category 1 (controlled stop then power removal)
- Red mushroom button on yellow background
- Direct opening action (mechanically linked)
- Manual reset required
- Overrides all other functions

### North American Standards

**ANSI/RIA R15.06: Industrial Robots and Robot Systems**

Harmonized with ISO 10218:
- Safeguarding methods
- Operating modes
- Collaborative operation (references ISO/TS 15066)

Additional Requirements:
- Pendant enabling device specifications
- Lockout/tagout provisions
- Training requirements

**OSHA Regulations**

29 CFR 1910.212:
- Machine guarding general requirements

29 CFR 1910.147:
- Control of Hazardous Energy (lockout/tagout)

**NFPA 79: Electrical Standard for Industrial Machinery**

Electrical Safety:
- Circuit protection
- Grounding and bonding
- Control circuits
- Emergency stop circuits

## Risk Assessment

### Hazard Identification

**Mechanical Hazards**

Crushing:
- Between robot and fixed objects
- Between robot links
- In gripper or tool

Impact:
- Moving robot strikes person
- High speeds increase severity
- Unexpected motion

Shearing:
- At joints
- Between gripper jaws
- Tool cutting edges

Entanglement:
- Cables and hoses
- Rotating joints
- Moving conveyors

**Electrical Hazards**

Contact:
- Live parts in control cabinet
- Motor power connections
- Damaged cables

Arc Flash:
- High-power systems (>480V)
- Proper PPE and procedures required

**Process Hazards**

Welding:
- Arc flash, UV radiation
- Fumes and gases
- Fire hazard

Cutting/Grinding:
- Flying debris
- Sparks
- Dust

Chemical Dispensing:
- Toxic or corrosive materials
- Vapor exposure
- Skin contact

### Risk Evaluation

**Severity Assessment**

S1 - Slight Injury:
- Bruising, minor cuts
- First aid treatment

S2 - Serious Injury:
- Fractures, lacerations requiring stitches
- Medical treatment, possible hospitalization

S3 - Fatal or Permanent Disability:
- Crushing, amputation
- Head or internal injuries

**Frequency and Exposure**

F1 - Rare:
- Less than once per year
- Brief exposure

F2 - Frequent:
- Daily or continuous exposure
- Long duration

**Probability of Occurrence**

P1 - Low:
- Unlikely under normal operation
- Multiple safeguards present

P2 - Medium:
- Possible, has occurred elsewhere

P3 - High:
- Has occurred or likely to occur

**Risk Level Calculation**

Risk = Severity × Frequency × Probability

High Risk:
- Requires additional safeguarding
- Cannot operate until mitigated

Medium Risk:
- Consider additional measures
- Document justification if accepted

Low Risk:
- Acceptable with standard safeguards
- Monitor and maintain

### Risk Reduction

**Hierarchy of Controls (ISO 12100)**

1. Inherently Safe Design:
   - Limit force and speed
   - Rounded edges (no pinch points)
   - Eliminate hazards if possible

2. Safeguarding:
   - Physical guards
   - Interlocks
   - Presence-sensing devices
   - Safety-rated control functions

3. Warnings and Signage:
   - Visual indicators (stack lights, strobes)
   - Audible alarms
   - Safety signs and labels

4. Training and Procedures:
   - Operator training
   - Maintenance procedures
   - Personal protective equipment (PPE)

## Safeguarding Methods

### Physical Barriers

**Perimeter Fencing**

Specifications:
- Height: 1800 mm minimum (2000-2400 mm typical)
- Mesh size: ≤50 mm (prevent reach-through)
- Distance from robot: ≥500 mm (when fully extended)
- Vertical bars (not horizontal, prevent climbing)

Materials:
- Welded wire mesh (most common)
- Expanded metal
- Polycarbonate panels (visibility)
- Powder-coated steel frame

**Interlocked Gates**

Access Gates:
- Self-closing
- Safety switches (ISO 14119)
- Dual-channel monitoring
- Trapped key systems (for maintenance)

Gate Configurations:
- Pedestrian access (operator entry)
- Material access (part loading)
- Maintenance access (larger opening)

Interlock Function:
- Robot stops when gate opens (Category 1 stop)
- Cannot restart while gate open
- Manual reset after gate closes

**Fixed Guards**

Non-Removable Panels:
- Require tools to remove
- Protect specific hazards (pinch points, sharp edges)
- Attached with tamper-resistant fasteners

**Light Curtains**

Type 4 Safety Light Curtains (IEC 61496):
- Infrared beam array
- Detects intrusion
- Safety-rated output

Specifications:
- Protected height: 300-1800 mm typical
- Resolution: 14mm, 30mm, or 50mm
- Response time: <20 ms
- Safety category 4, PLe

Placement:
- At access points where physical gates not practical
- Muting for part passage (requires careful design)

Distance Calculation:
```
Safety distance = K × T + C
```
Where:
- K = hand speed constant (1600 mm/s)
- T = total response time (sensor + robot stop)
- C = additional distance based on resolution

**Safety Laser Scanners**

2D/3D Area Monitoring:
- Configurable zones (warning and protective)
- Automatic zone switching
- Detect personnel entry

Features:
- Range: 3-70 meters
- Angular resolution: 0.1-1 degree
- Update rate: 20-40 Hz
- Multiple zone sets

Applications:
- Large workcells
- Mobile robots
- Dynamic access control

### Safety Functions

**Safe Torque Off (STO)**

Function:
- Removes power to motor drives
- Robot coasts to stop
- Category 0 stop (uncontrolled)

Implementation:
- Dual-channel monitoring
- Directly disables drive power stage
- No reliance on software

Performance Level:
- PLd or PLe depending on architecture

Use:
- Emergency stop
- Guard door interlock
- Basic safety stop

**Safe Stop 1 (SS1)**

Function:
- Controlled deceleration
- Power removed after stop
- Category 1 stop

Advantage:
- Prevents uncontrolled motion
- Protects workpiece and robot

Requirements:
- Safe motion monitoring during stop
- Verify standstill before removing power

**Safe Stop 2 (SS2)**

Function:
- Controlled stop
- Power maintained (holds position)

Use:
- Temporary stops (gate open briefly)
- Operator loads part
- Robot ready to resume

Requirements:
- Continuous position monitoring
- Detect unexpected motion

**Safely-Limited Speed (SLS)**

Function:
- Monitors robot speed
- Stops if exceeds programmed limit

Parameters:
- Typically 250 mm/s for manual mode (ISO 10218)
- Lower limits for collaborative operation

Implementation:
- Safety-rated encoders
- Continuous velocity calculation
- Safe comparison to limit

**Safe Reduced Speed (SRS)**

Function:
- Limits maximum speed in certain modes or zones

Use:
- Teaching mode
- Collaborative zones
- Maintenance mode

**Safe Operating Stop (SOS)**

Function:
- Monitors that robot is stationary
- Allows safe work near robot
- Power maintained

Example:
- Robot holds part while operator inspects
- No motion permitted
- Triggers stop if any movement detected

## Operating Modes

### Automatic Mode

Configuration:
- Full production speed
- All guards closed
- No personnel in restricted space
- Safety functions: STO via e-stop or interlocks

Access:
- Only via interlocked gates (stops robot)
- Emergency stop if entry detected

### Manual Mode (Teach/Programming)

Requirements per ISO 10218:
- Speed limited to 250 mm/s (SLS function)
- Three-position enabling device required
- Hold middle position: Robot enabled
- Release or full press: Robot stops
- Pendant must be within restricted space

Enabling Device:
- Three positions (off, on, panic)
- Panic-stop if squeezed too hard
- Deadman switch principle

Safety:
- Operator has direct control
- Can stop instantly
- Limited speed reduces injury severity

### Maintenance Mode

Lockout/Tagout (LOTO):
- Disconnect all energy sources
- Lock main disconnect in "off" position
- Tag to identify who locked it
- Verify zero energy state

Procedures:
- Only authorized personnel
- Written procedures
- Test before starting work
- Restore and test after work

## Collaborative Operation

### Collaborative Operating Spaces (ISO 10218-2)

**Collaborative Workspace**
- Where robot and operator share space
- Requires safety-rated monitoring

**Non-Collaborative Space**
- Robot operates alone
- Traditional safeguarding

**Transition Zone**
- Robot slows or stops when operator approaches

### Collaborative Methods (ISO/TS 15066)

**1. Safety-Rated Monitored Stop**

Operation:
- Operator enters collaborative space
- Robot stops and remains stopped
- Safety-rated monitoring of standstill
- Operator performs task
- Operator exits, robot resumes

Requirements:
- SOS (Safe Operating Stop) function
- Detection of operator entry (light curtain, scanner, mat)
- Manual restart or automatic after exit

Applications:
- Part loading/unloading
- Inspection
- Adjustment

**2. Hand Guiding**

Operation:
- Operator physically guides robot
- Force sensor or enabling device on tool
- Robot moves with operator
- Three-position enabling device required

Requirements:
- SLS (speed limited to 250 mm/s or less)
- Force/torque sensor or enabling device
- Protective stop if device released

Applications:
- Teaching positions
- Manual operation in constrained spaces

**3. Speed and Separation Monitoring (SSM)**

Operation:
- Minimum distance maintained between robot and operator
- Robot slows as operator approaches
- Stops if separation too small

Implementation:
- Safety laser scanners or vision system
- Real-time position monitoring (robot and human)
- Graduated response (slow → slower → stop)

Separation Distance:
```
S = Sh + Sr + Ss + C
```
Where:
- Sh = distance human can move during robot reaction time
- Sr = distance robot moves during stop
- Ss = safety margin
- C = position uncertainty

**4. Power and Force Limiting (PFL)**

Operation:
- Contact between robot and operator permitted
- Forces limited to safe values per ISO/TS 15066
- No sharp edges or pinch points

Force Limits (Examples from ISO/TS 15066):
- Skull: 130 N (transient), 65 N (quasi-static)
- Face: 140 N / 65 N
- Chest: 140 N / 110 N
- Abdomen: 110 N / 65 N
- Hand/fingers: 140 N / 40 N

Requirements:
- Inherent safe design (limited power, compliant surfaces)
- Force/torque sensing in all joints
- Safety-rated force monitoring
- Validated biomechanical assessment

Design Considerations:
- Padding or soft covers
- Rounded edges
- Limited mass and speed
- Force-limited motors or clutches

### Collaborative Robot Examples

**Universal Robots (UR series)**
- Force/torque sensing in all joints
- Configurable safety zones and speeds
- Hand-guiding capable
- Primarily SSM and PFL modes

**KUKA LBR iiwa**
- Torque sensors in all 7 joints
- High sensitivity
- Medical and precision applications
- All collaborative modes

**ABB GoFa/SWIFTI**
- Dual-encoder safety
- SSM and PFL
- Higher payload than typical cobots

**Franka Emika**
- Integrated force sensing
- Research and precision applications

## Safety Validation

### Pre-Commissioning Checks

**Mechanical**
- Guards installed per design
- Interlocks functional
- No sharp edges or pinch points
- Cable routing secure

**Electrical**
- Emergency stops wired correctly
- Safety circuits dual-channel
- Proper grounding
- Circuit protection (fuses, breakers)

**Control System**
- Safety functions configured
- Speed limits set correctly
- Zones and parameters validated

### Functional Testing

**Emergency Stop**

Test Each E-Stop:
1. Start robot motion (manual or auto)
2. Press e-stop button
3. Verify immediate stop
4. Verify power removed (STO)
5. Attempt to restart (should fail)
6. Reset e-stop
7. Verify manual restart required

Measure stop time and distance.

**Interlock Testing**

Each Interlocked Gate:
1. Start robot motion
2. Open gate
3. Verify robot stops (Category 1)
4. Verify cannot restart with gate open
5. Close gate
6. Verify restart possible
7. Attempt to defeat interlock (tape, bypass)
8. Verify robot stops if defeated

**Light Curtain / Scanner**

Intrusion Test:
1. Start robot motion
2. Break light curtain with test piece
3. Verify robot stops
4. Measure response time
5. Verify safety distance adequate
6. Test muting functions (if applicable)

**Speed Monitoring (SLS)**

Manual Mode Test:
1. Enter manual mode
2. Attempt to exceed 250 mm/s
3. Verify robot stops or limits speed
4. Test with different motion types

Collaborative Mode:
1. Configure speed limit (e.g., 100 mm/s)
2. Run test program
3. Verify limit enforced

### Performance Level Validation

**Calculate Performance Level**

For each safety function:
- Identify architecture (Category 1-4)
- Calculate MTTF (mean time to failure)
- Determine diagnostic coverage
- Use ISO 13849-1 graphs/tables
- Verify achieves required PL (typically PLd or PLe)

**Common Mode Failures**

Check for:
- Single point failures that defeat safety
- Environmental factors (EMI, temperature)
- Software errors (use certified software)

**Periodic Testing**

Requirements:
- Frequency based on risk assessment
- Typically: Daily (e-stop), Weekly (interlocks), Annually (full validation)
- Document all tests

## Documentation

### Safety Manual

Required Contents:
- Risk assessment results
- Safety functions and PLs
- Operating modes and restrictions
- Training requirements
- Maintenance procedures
- Emergency procedures

### Validation Report

Include:
- Test procedures
- Test results and measurements
- Deviations and resolutions
- Date and personnel
- Acceptance signatures

### Training Records

Document:
- Operators trained
- Topics covered
- Competency verification
- Dates and refresher schedule

## Common Safety Violations

**Bypassing Safety Devices**
- Jumper wires around interlocks
- Taping guard switches
- Disabling light curtains
- Holding enabling device in active position

**Inadequate Guarding**
- Gaps allowing reach-in
- Insufficient fence height
- Guards easily removable without tools

**Improper E-Stop Implementation**
- Single-channel only
- No mechanical latching
- Insufficient quantity or placement

**Working Inside Safeguards**
- Without LOTO
- Robot powered
- Relying on software safeties

**Lack of Training**
- Untrained operators
- No emergency procedures
- Unaware of hazards

## Best Practices

- Design inherently safe first (reduce force, speed, mass)
- Use safety-rated components throughout
- Dual-channel monitoring for critical functions
- Regular testing and maintenance
- Comprehensive training program
- Document everything
- Review and update after modifications
- Involve safety professionals

---

**Next**: [10.10 Maintenance](section-10.10-maintenance.md)

---

## References

1. **ISO 10218-1:2011** - Robots and robotic devices - Safety requirements
2. **ISO 9283:1998** - Manipulating industrial robots - Performance criteria
3. **Denavit, J. & Hartenberg, R.S. (1955).** "A Kinematic Notation for Lower-Pair Mechanisms." *ASME Journal of Applied Mechanics*, 22, 215-221
4. **Craig, J.J. (2017).** *Introduction to Robotics: Mechanics and Control* (4th ed.). Pearson
5. **Lynch, K.M. & Park, F.C. (2017).** *Modern Robotics*. Cambridge University Press
6. **ABB Robot Studio Software** - Robot simulation and programming
7. **KUKA System Software (KSS)** - Robot control and motion planning
