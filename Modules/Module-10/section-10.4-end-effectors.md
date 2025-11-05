# 10.4 End Effectors and Tool Changers

End effectors are the interface between robot and task. This section covers grippers, process tools, sensors, and automatic tool changing systems.

## Tool Mounting Interface

### ISO 9409 Standard

**Flange Specifications**

Common sizes:
- ISO 9409-1-31.5: 31.5 mm diameter (small robots)
- ISO 9409-1-40: 40 mm diameter
- ISO 9409-1-50: 50 mm diameter (most common)
- ISO 9409-1-63: 63 mm diameter
- ISO 9409-1-80: 80 mm diameter
- ISO 9409-1-100: 100 mm diameter (large robots)

Features:
- Bolt circle diameter
- Centering pilot diameter
- Dowel pin holes for orientation
- Standard bolt pattern (M5, M6, M8)

**Tool Coordinate System**
- Origin at center of flange
- Z-axis perpendicular to flange (tool direction)
- X and Y in flange plane

### Custom Flanges

For non-standard applications:
- Adapter plates to convert between sizes
- Custom mounting for legacy tools
- Quick-disconnect features
- Alignment features (keys, pins)

## Grippers

### Parallel Jaw Grippers (From Module 9, Applied to Arms)

**Pneumatic Parallel Grippers**

Advantages for robotic arms:
- Fast actuation (0.1-0.3 sec)
- Simple control (on/off valve)
- High grip force
- Reliable and robust

Sizing:
- Stroke: Part size variation × 2 (jaw travel each side)
- Force: Calculate per Module 9.3
- Typical sizes: 16mm, 25mm, 40mm, 63mm stroke

Integration:
- Mount to tool flange via adapter plate
- Pneumatic lines through robot arm
- Solenoid valve at base or on gripper
- Proximity sensors for open/closed feedback

**Electric Parallel Grippers**

Features:
- Variable position and force control
- Encoder feedback (jaw position)
- Force sensing (current monitoring)
- Slower than pneumatic

Advantages:
- Adaptive grasping (different part sizes without tool change)
- Force monitoring (detect part presence, prevent damage)
- No compressed air required

Control:
- Digital or analog signal for position
- Current limit for force control
- RS-485, EtherCAT, or CAN communication

**Gripper Finger Design**

Modular Jaws:
- Quick-change interface on gripper body
- Part-specific soft jaws
- 3D printed for rapid prototyping
- Machined aluminum for production

Materials:
- Aluminum: General purpose, lightweight
- Urethane: Soft, high friction, no part damage
- Rubber: Conformable to shape
- Steel: Heavy-duty, wear-resistant

Features:
- V-grooves for round parts
- Form-fitting profiles for shaped parts
- Serrations for high friction
- Vacuum integration (combination gripper)

### Angular Grippers

Design:
- Jaws pivot about axis
- Suitable for round parts (internal or external grip)
- More compact than parallel for same stroke

Applications:
- Shaft handling
- Tube gripping
- Turning parts in assembly

### Three-Jaw Grippers

Characteristics:
- Self-centering (like lathe chuck)
- Excellent for round parts
- More complex mechanism
- Typically pneumatic actuation

### Vacuum Grippers for Robotic Arms

**Suction Cup Arrays**

Design:
- Multiple cups on rigid or flexible base
- Independent spring-loaded cups compensate for surface variation
- Bellows cups for uneven surfaces

Advantages:
- Handle large flat parts (sheet metal, panels, glass)
- No grip force, gentle on parts
- Fast pick/release

Vacuum Distribution:
- Manifold distributes vacuum to all cups
- Independent zones for different part sizes
- Valves for zone control

**Integrated Vacuum Generators**

Venturi Ejector on Tool:
- Compact, mounts near suction cups
- Minimal tubing (reduces lag)
- Only compressed air line to tool

Centralized Vacuum Pump:
- Single pump serves multiple tools/robots
- Vacuum reservoir for quick response
- More energy efficient for continuous use

### Magnetic Grippers

**Electromagnets**

Design:
- Coil wrapped around iron core
- Controllable via relay or PWM
- Strong holding force when energized

Power Requirements:
- Continuous power to maintain grip
- Power through robot umbilical
- Fail-safe requires backup power or safety catching device

Demagnetization:
- Residual magnetism may prevent release
- Active demagnetization cycle (reverse polarity pulse)
- May interfere with machining or inspection

**Permanent Magnet Systems**

Switchable Permanent Magnets:
- Mechanical or pneumatic actuation rotates magnet
- No electrical power required
- Robust and simple

Applications:
- Steel part handling
- Large sheet metal
- Scrap handling

## Process Tools

### Welding Tools

**Spot Welding Guns**

Components:
- Pneumatic or servo-electric actuation
- Water-cooled electrodes
- Transformer (if integrated)
- Force control

Integration:
- Heavy (10-25 kg typical)
- High current and water lines
- Force feedback for quality
- Electrode wear compensation

Programming:
- Approach position
- Clamp force and weld time
- Retract and move to next spot

**Arc Welding Torches**

MIG/MAG Torch:
- Wire feed mechanism (may be robot-mounted or external)
- Contact tip and nozzle
- Gas shroud
- Typically 3-6 kg

TIG Torch:
- Tungsten electrode
- Separate filler wire feed (if used)
- Precision gas control

Control Integration:
- Welding power source (separate unit)
- Start/stop signals from robot
- Wire feed speed control
- Arc voltage and current monitoring
- Seam tracking sensors (optional)

### Cutting and Grinding Tools

**Deburring Spindles**

Specifications:
- Speed: 10,000-60,000 RPM
- Power: 0.5-3 kW
- Air or electric drive
- Collet or quick-change tooling

Force Control:
- Constant force against surface
- Adapt to part variation
- Requires force/torque sensor

Applications:
- Edge deburring after machining
- Weld seam grinding
- Surface finishing

**Routing and Milling**

High-Speed Spindle:
- Similar to CNC spindle (see Module 6)
- Lighter weight for robot mounting
- Rigid mounting required (robot stiffness limits)

Limitations:
- Robot compliance reduces achievable tolerances
- Best for non-precision material removal
- Foam, composites, wood suitable
- Metal milling requires extremely rigid robot

### Dispensing Tools

**Adhesive and Sealant Dispensers**

Types:
- Pneumatic pressure pots
- Positive displacement pumps
- Cartridge dispensers

Control:
- On/off valves
- Flow rate control
- Pressure regulation

Programming:
- Continuous path (bead along seam)
- Dot patterns (adhesive dots)
- Speed coordination (consistent bead width)

**Spray Guns**

Paint/Coating:
- HVLP (High Volume Low Pressure)
- Electrostatic for efficiency
- Explosion-proof construction

Robot Requirements:
- Smooth motion (avoid texture from motion artifacts)
- Speed control (consistent coating thickness)
- Rotational wrist for complex geometries

### Inspection Tools

**Touch Probes**

CMM-Style Probes:
- Contact trigger probe
- 3-axis or 5-axis measurement
- Repeatability: 0.01-0.02 mm

Operation:
- Robot moves probe to surface
- Contact triggers measurement
- Record position and calculate dimensions

Limitations:
- Robot repeatability limits accuracy
- Suitable for go/no-go inspection
- Not precision metrology

**Vision Systems**

End-Effector Mounted Camera:
- Inspect parts at multiple angles
- Defect detection
- Barcode/OCR reading
- Position verification

Integration:
- Lighting (LED ring, structured light)
- Image processing computer
- Communication to robot controller

**Force/Torque Sensors**

Wrist-Mounted F/T Sensor:
- Measures forces and torques in 6 axes
- Mounts between flange and tool
- Enables force-controlled tasks

Applications:
- Assembly (insertion with force feedback)
- Contour following (grinding, deburring)
- Contact detection
- Product testing (button feel, latch engagement)

## Tool Changers

### Manual Tool Change

Simple Systems:
- Bolt tool to flange manually
- Disconnect utilities (air, electrical)
- For infrequent changes or simple applications

Quick-Disconnect Couplings:
- Pneumatic: Push-to-connect
- Electrical: Threaded connectors or pogo pins
- Reduces changeover time to 2-5 minutes

### Automatic Tool Changers (ATC)

**Master/Tool Side**

Master Side (on robot):
- Mechanical coupling (bayonet, tapered, or kinematic)
- Pneumatic actuation for lock/unlock
- Utility pass-throughs (air, electrical, data)
- Pogo pins or inductive coupling for signals

Tool Side (on end effector):
- Complementary coupling
- Receptacles for utilities
- Alignment features (pins, tapers)

**Coupling Mechanisms**

Bayonet Coupling:
- Rotate and lock (quarter-turn)
- High repeatability
- Moderate force coupling

Tapered Coupling:
- Pull tool into taper (Hirth coupling)
- Very high stiffness and repeatability
- Used in precision applications

Kinematic Coupling:
- Three ball-and-groove pairs
- Highest repeatability (±0.005 mm)
- Expensive

**Utility Pass-Through**

Pneumatic:
- Quick-disconnect valves in coupling
- Multiple circuits (typically 2-4)
- Pressure rating: 6-10 bar

Electrical:
- Pogo pins (spring-loaded contacts)
- Inductive coupling (contactless)
- Power and signal lines (typically 6-16 circuits)

Data:
- Ethernet (M12 connectors)
- Serial communication
- Tool identification (RFID or coded resistors)

**Tool Rack**

Design:
- Holds multiple tools
- Passive or active retention (locking mechanisms)
- Organized layout for robot access
- Typically 4-12 tool capacity

Tool Identification:
- RFID tags on each tool
- Robot reads tag to verify correct tool
- Load tool-specific parameters (TCP offset, mass, etc.)

**Change Sequence**

Return Old Tool:
1. Move to tool rack position
2. Insert tool into holder
3. Unlock coupling (pneumatic signal)
4. Retract robot
5. Verify tool released (sensor)

Pick New Tool:
1. Move to new tool position
2. Engage coupling
3. Lock coupling (pneumatic signal)
4. Verify locked (sensor)
5. Load tool parameters (TCP, weight)
6. Move to ready position

Cycle Time:
- Typical: 5-15 seconds per tool change
- Add time to move between rack and work area

### Tool Changer Sizing

**Payload Capacity**
- Static payload: Tool weight
- Dynamic payload: Tool plus part plus forces
- Safety factor: 2-3×

**Moment Capacity**
- Torque from tool extending from flange
- Example: 5 kg tool at 150 mm = 7.5 Nm moment
- Changer rated for moment loading

**Repeatability**
- Critical for precision applications
- Typical: ±0.01-0.05 mm
- Kinematic coupling: ±0.005 mm

**Manufacturers**
- ATI Industrial Automation
- Schunk
- Destaco
- Stäubli
- Zimmer Group

## Tool Design Considerations

**Weight and Center of Gravity**

Minimize Weight:
- Reduce motor torque requirements
- Increase speed and acceleration
- Extend robot reach capability

Balance:
- Center tool mass along wrist axis
- Reduce moments on wrist joints
- Counterweights if necessary

**Tool Center Point (TCP) Definition**

TCP Location:
- Functional point of tool (gripper center, torch tip, probe ball)
- Defined relative to flange coordinate system
- Entered in robot controller

TCP Calibration:
- Four-point method: Touch reference point from four different robot orientations
- Controller calculates TCP position
- Accuracy critical for path precision

**Reach Extension**

Trade-offs:
- Longer tool extends reach
- Increases moment on wrist
- Reduces effective payload
- May increase deflection and vibration

Optimize:
- Minimize tool length while meeting functional requirements
- Use lightweight materials (carbon fiber, aluminum)

**Collision Geometry**

Robot Path Planning:
- Software needs tool collision geometry
- Define as simple shapes (cylinders, boxes)
- Conservative envelope for safety
- Allows collision-free path generation

**Cable Management**

Routing:
- Through or along robot arm
- Strain relief at wrist
- Protection from abrasion and snagging

Connectors:
- Secure and reliable
- Industrial grade (M12, M8 for sensors)
- Polarized to prevent miswiring

## Multi-Function End Effectors

**Combination Tools**

Gripper + Sensor:
- Gripper with integrated force sensor
- Camera on gripper for visual feedback
- Vacuum and mechanical grip combined

Welding + Gripper:
- Pick part, place in fixture, weld
- Reduces tool changes
- Complex integration

**Tradeoffs**
- Increased complexity
- Higher weight
- More failure modes
- Justified if reduces cycle time

***

**Next**: [10.5 Motion Planning and Control](section-10.5-motion-planning.md)

---

## References

1. **ISO 10218-1:2011** - Robots and robotic devices - Safety requirements
2. **ISO 9283:1998** - Manipulating industrial robots - Performance criteria
3. **Denavit, J. & Hartenberg, R.S. (1955).** "A Kinematic Notation for Lower-Pair Mechanisms." *ASME Journal of Applied Mechanics*, 22, 215-221
4. **Craig, J.J. (2017).** *Introduction to Robotics: Mechanics and Control* (4th ed.). Pearson
5. **Lynch, K.M. & Park, F.C. (2017).** *Modern Robotics*. Cambridge University Press
6. **ABB Robot Studio Software** - Robot simulation and programming
7. **KUKA System Software (KSS)** - Robot control and motion planning
