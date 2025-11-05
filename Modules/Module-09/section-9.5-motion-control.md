# 9.5 Motion Control and Path Planning

Motion control determines how the robot moves between positions efficiently, accurately, and safely.

## Motion Controllers

**Controller Types**

Dedicated Robot Controller:
- Specialized for robot kinematics
- Built-in trajectory planning
- Examples: KUKA KRC, ABB IRC5, Universal Robots
- Commercial systems, proprietary interfaces

CNC Controller (LinuxCNC, Mach3):
- General-purpose motion control
- G-code programming
- Open source options available
- Requires kinematics configuration

PLC + Motion Modules:
- Allen-Bradley, Siemens, Omron
- Integrated with factory automation
- Higher cost

Standalone Motion Controller:
- Galil, Delta Tau, ACS
- Flexible programming
- Multi-axis coordination

**DIY Options**
- LinuxCNC with custom kinematics component
- GRBL (limited to 3 axes, Cartesian only)
- Marlin (3D printer firmware, adapted)
- Custom Arduino/Raspberry Pi solutions

## Coordinate Systems

**Machine Coordinates**
- Fixed reference frame
- Motor positions or joint angles
- Controller operates in this space

**World Coordinates**
- User-defined reference frame
- Typically part fixture or table origin
- Programming done in this space

**Tool Coordinates**
- Origin at tool center point (TCP)
- Accounts for end effector geometry
- Critical for accurate positioning

**Transformations**
```
Position_machine = Transform_world_to_machine × Position_world
Position_tool = Transform_tool_offset × Position_machine
```

## Kinematics Algorithms

**Forward Kinematics**
Given: Joint positions (motor angles/positions)
Find: Tool position in world space

Cartesian:
```
X = X_motor
Y = Y_motor
Z = Z_motor
```

SCARA:
```
X = L1×cos(θ1) + L2×cos(θ1+θ2)
Y = L1×sin(θ1) + L2×sin(θ1+θ2)
Z = Z_motor
```

**Inverse Kinematics**
Given: Desired tool position
Find: Required joint positions

Cartesian: Trivial (1:1 mapping)

SCARA: Analytical solution (see Section 9.2)

Delta: Complex analytical or numerical solution

**Singularities**
Configurations where small tool motions require infinite joint velocities:
- SCARA: Fully extended or folded
- Delta: Near workspace boundaries
- Solution: Avoid via path planning or joint limits

## Trajectory Planning

**Point-to-Point (PTP) Motion**
- Moves from start to end position
- Path is not controlled (joint space interpolation)
- Fastest for simple pick-and-place
- Each joint accelerates/decelerates independently

**Linear (Cartesian) Motion**
- Tool moves in straight line
- Requires inverse kinematics at each timestep
- Slower than PTP
- Used when path matters (avoiding obstacles)

**Circular/Spline Motion**
- Tool follows arc or smooth curve
- Complex planning
- Uncommon in pick-and-place

## Velocity Profiling

**Trapezoidal Profile**
- Constant acceleration, constant velocity, constant deceleration
- Simple to implement
- Discontinuous acceleration (jerk)

```
Phase 1: Accel    v = a×t
Phase 2: Constant v = v_max
Phase 3: Decel    v = v_max - a×t
```

**S-Curve Profile**
- Smooth acceleration (limited jerk)
- Reduces vibration and wear
- More complex calculation
- Better for high-speed systems

**Motion Time Calculation**

Trapezoidal profile:
```
If distance allows reaching v_max:
  t_total = d/v_max + v_max/a

If too short (triangular profile):
  t_total = 2×√(d/a)
```

## Multi-Axis Coordination

**Synchronized Motion**
- All axes reach end position simultaneously
- Scale velocities to slowest axis
- Smooth coordinated motion

**Blending**
- Round corners between move segments
- Reduces cycle time (no complete stop)
- Trade-off: path accuracy vs. speed

**Look-Ahead**
- Controller examines upcoming moves
- Optimizes velocity through corners
- Prevents unnecessary deceleration

## Control Loops

**Position Control**
- PID feedback loop
- Typical update rate: 1-2 kHz
- Tuning parameters: Kp, Ki, Kd

**Velocity Control**
- Inner loop for servo drives
- Faster update rate (10-20 kHz)
- Reduces following error

**Torque/Current Control**
- Innermost loop in servo drive
- Limits motor stress
- Enables force control

## Path Planning Strategies

**Pick-and-Place Sequence**

Standard sequence:
1. Move to approach position (above part)
2. Lower to pick position
3. Activate gripper/vacuum
4. Raise to clearance height
5. Move to place approach position
6. Lower to place position
7. Release gripper/vacuum
8. Raise to clearance height
9. Return to home or next pick

**Clearance Heights**
- Safe Z height to avoid collisions
- Typically 50-100mm above highest obstacle
- Balance safety vs. cycle time

**Approach Strategies**

Z-First:
- Move Z to clearance
- Move XY to target
- Lower Z to final position
- Safe, slower

XYZ-Simultaneous:
- Interpolate all axes together
- Faster
- Requires collision-free path

**Obstacle Avoidance**
- Define keep-out zones in workspace
- Path planner routes around obstacles
- Simple: Use via points
- Advanced: A* or RRT path planning algorithms

## Homing and Calibration

**Homing Sequence**
1. Move axes to home switches at slow speed
2. Back off and re-approach at creep speed
3. Set machine zero position
4. Move to known calibration position

**Absolute Encoders**
- Eliminate need for homing
- Position known on power-up
- Higher cost

**Calibration Procedures**

Tool Center Point (TCP):
- Jog tool to known reference point
- Measure offset from wrist to tool tip
- Enter offset in controller

Vision Calibration:
- Place calibration grid in camera FOV
- Robot moves to grid points
- Calculate camera-to-robot transformation

**Repeatability Testing**
- Move to position 100+ times
- Measure variation with indicator or CMM
- Should be <0.05mm for Cartesian, <0.02mm for SCARA

## Motion Programming

**G-Code (CNC-Style)**
```gcode
G0 X100 Y50 Z50      ; Rapid to approach
G1 Z10 F500          ; Feed to pick height
M42 P1               ; Activate vacuum
G4 P0.5              ; Dwell 0.5 sec
G0 Z50               ; Retract
G0 X200 Y150         ; Move to place
G1 Z15               ; Lower to place
M43 P1               ; Release vacuum
G0 Z50               ; Retract
```

**Teach Pendant**
- Jog robot to positions
- Record positions to program
- Playback sequence
- Common on commercial robots

**Scripting (Python, JavaScript)**
```python
robot.move_to(x=100, y=50, z=50, speed=1000)
robot.move_to(z=10, speed=100)
robot.gripper_on()
time.sleep(0.5)
robot.move_to(z=50)
robot.move_to(x=200, y=150)
```

**Graphical Programming**
- Drag-and-drop blocks (LabVIEW, Blockly)
- Visual sequence design
- Easier for non-programmers

## Performance Optimization

**Minimize Air Time**
- Reduce unnecessary Z moves
- Optimize travel paths
- Use blending/rounding

**Maximize Acceleration**
- Reduce moving mass
- Stiffen structure
- Tune control loops

**Parallel Operations**
- Gripper activation during motion
- Vision processing during previous cycle
- Multi-robot coordination

**Cycle Time Analysis**
Break down into components:
- Move time: 60-70%
- Gripper actuation: 10-15%
- Vision processing: 10-20%
- Settling time: 5-10%

Focus optimization on largest contributors.

## Real-Time Control

**Deterministic Timing**
- Real-time operating system (RTOS or Linux PREEMPT_RT)
- Guaranteed response times
- Critical for servo control

**Trajectory Generation**
- Pre-compute paths
- Stream points to controller
- Buffer to prevent starvation

**Communication Latency**
- Minimize overhead in control loops
- Direct memory access (DMA) for high-speed I/O
- Avoid polling delays

***

**Next**: [9.6 CNC Integration](section-9.6-cnc-integration.md)

---

## References

1. **Motion Control Theory**
   - Craig, J.J. (2017). *Introduction to Robotics: Mechanics and Control*. Pearson
   - Spong, M.W. et al. (2005). *Robot Modeling and Control*. Wiley
   - LaValle, S.M. (2006). *Planning Algorithms*. Cambridge University Press

2. **Trajectory Planning**
   - Lynch, K.M. & Park, F.C. (2017). *Modern Robotics*. Cambridge University Press
   - Siciliano, B. et al. (2009). *Robotics: Modelling, Planning and Control*. Springer

3. **Real-Time Control**
   - LinuxCNC Documentation - Real-time motion control
   - PREEMPT_RT Linux Kernel Documentation
   - EtherCAT Technology Group - Real-time Ethernet

4. **Control Systems**
   - Åström, K.J. & Murray, R.M. (2008). *Feedback Systems*. Princeton University Press
