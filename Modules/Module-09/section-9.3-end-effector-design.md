# 9.3 End Effector Design

End effectors physically interact with parts. Selection depends on part geometry, material, weight, and surface characteristics.

## Vacuum Grippers

**Principles**
- Use suction to hold smooth, flat surfaces
- Fast pick/release
- Gentle on delicate parts

**Components**
- Suction cups (bellows, flat, foam)
- Vacuum source (venturi or pump)
- Vacuum sensors
- Solenoid valves

**Force Calculation**
```
F = P × A × n × η
```
- P = vacuum pressure (kPa)
- A = cup area (mm²)
- n = number of cups
- η = efficiency (0.7-0.9)

**Vacuum Generation**

Venturi:
- Uses compressed air
- Fast response
- Typical: -60 to -80 kPa

Pump:
- Electric rotary vane
- Higher vacuum: -80 to -95 kPa
- Lower air consumption

**Cup Types**
- Bellows: Compensate for height variation
- Flat: Maximum grip force
- Foam: Conforms to texture

**Applications**
- PCB handling
- Sheet metal
- Glass and flat plastics
- Smooth packaging

## Mechanical Grippers

**Parallel Jaw Grippers**
- Two jaws move in parallel
- Pneumatic or electric actuation
- Handles irregular shapes

**Grip Force Required**
```
F_grip = (m × a × SF) / (2 × μ)
```
- m = mass (kg)
- a = acceleration (m/s²)
- SF = safety factor (2-4)
- μ = friction coefficient

**Jaw Types**
- Soft jaws: Urethane padding
- Form-fitting: Machined to part
- V-block: Centers round parts
- Serrated: High friction

**Actuation**

Pneumatic:
- Fast (0.1-0.3 sec)
- Fixed force
- Simple control

Electric:
- Variable position/force
- Encoder feedback
- More flexible

**Three-Jaw Grippers**
- Self-centering
- Good for round parts
- Higher complexity

## Magnetic Grippers

**Electromagnetic**
- Coil around iron core
- Controllable on/off
- Works only on ferrous materials
- Fast pick/release

**Permanent Magnets**
- Switchable mechanism
- No electrical power
- Manual or pneumatic switch

**Applications**
- Steel sheet handling
- Ferrous parts
- High duty cycle operations

## Specialized End Effectors

**Needle Grippers**
- Pins grip inside holes
- For rings, washers
- Requires precision alignment

**Hook Grippers**
- Catches part features
- Simple mechanism

**Adhesive Pads**
- Tacky silicone or gel
- For difficult materials
- Limited lifespan

**Custom 3D Printed**
- Rapid prototyping
- Part-specific geometry
- Lower strength

## Quick-Change Systems

**Tool Changer Interface**
- Mechanical coupling
- Pneumatic/electrical pass-through
- Tool identification sensors

**Benefits**
- Handle multiple part types
- Reduce changeover time
- Automated tool selection

## Sensors

**Part Presence**
- Proximity sensors
- Optical through-beam
- Vacuum pressure switches

**Position Feedback**
- Encoders (electric grippers)
- Reed switches (pneumatic)

**Force Sensing**
- Load cells
- Prevent part damage
- Verify grip security

## Design Guidelines

**Selection Criteria**
- Part surface (smooth vs. textured)
- Material (ferrous, plastic, etc.)
- Weight and acceleration
- Cycle time requirements
- Damage tolerance

**Safety Factors**
- Vacuum: 10-20× weight
- Mechanical grip: 2-4× dynamic force
- Magnetic: 5-10× weight

***

**Next**: [9.4 Vision Systems and Sensors](section-9.4-vision-sensors.md)

---

## References

1. **Gripper Manufacturers**
   - SCHUNK Grippers and Gripping Systems - Technical Catalogs
   - SMC Pneumatics - Vacuum Equipment and Grippers
   - DESTACO - End Effector Solutions
   - Piab Vacuum Technology - Suction Cup Selection Guide

2. **Engineering Handbooks**
   - Monkman, G.J. et al. (2007). *Robot Grippers*. Wiley-VCH
   - Cutkosky, M.R. & Wright, P.K. (1986). "Modeling Manufacturing Grips and Robotic Hands"

3. **Vacuum Technology**
   - SMC Vacuum Technology Reference Guide
   - Piab Vacuum Handbook
   - ISO 6358:2013 - Pneumatic components - Flow characteristics

4. **Material Properties**
   - Engineering friction coefficient tables
   - MatWeb Material Property Database
   - Permanent magnet specifications - K&J Magnetics
