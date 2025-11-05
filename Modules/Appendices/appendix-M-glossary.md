# Appendix M: Comprehensive Glossary of CNC Engineering Terms

---

## M.1 Mechanical Design Terms

- **Backlash:** Lost motion in mechanical systems due to clearances between components (measured in mm or inches). Target: <0.05mm for precision CNC. Anti-backlash compensation: ball screw preload, spring-loaded nuts.

- **Ball Screw:** Precision lead screw using recirculating ball bearings to convert rotary to linear motion with high efficiency (90-95%) and low backlash (<0.01mm). Grades: C10 (±52μm/300mm) to C2 (±8μm/300mm).

- **Bearing Types:**
  - **Angular Contact:** High-speed spindle bearings with contact angle 15-40°. Preload required.
  - **Deep Groove Ball:** General-purpose radial/thrust bearing. Most common type.
  - **Tapered Roller:** Heavy radial and thrust loads. Used in large gantries.
  - **Linear Ball Bearing:** Recirculating ball bearing for linear motion on hardened shafts.

- **Cantilever:** Beam supported at one end only. Z-axis spindle head is cantilever load. Deflection = FL³/(3EI).

- **Compliance:** Inverse of stiffness (μm/N). Higher compliance = more deflection under load.

- **Critical Damping:** Damping ratio ζ=1. System returns to equilibrium without oscillation. Under-damped: ζ<1 (oscillates), Over-damped: ζ>1 (slow return).

- **Datum:** Reference surface, line, or point from which measurements are made. Critical for alignment and repeatability. Kinematic datum: 3-2-1 constraint principle (6 DOF constraint).

- **Degrees of Freedom (DOF):** Number of independent motions. Rigid body: 6 DOF (3 translation + 3 rotation). CNC mill: 3 DOF (XYZ), 5-axis: 5 DOF.

- **Dynamic Load Rating (C):** Load capacity of bearing/guide that allows 1 million meters of travel (or 1 million revolutions for rotary bearings) before fatigue failure (90% reliability, L10 life).

- **Elastic Modulus (Young's Modulus):** Material stiffness (stress/strain ratio). Steel: 200 GPa, Aluminum: 69 GPa, Cast Iron: 100-140 GPa.

- **Fastener Preload:** Tensile force applied during bolt tightening. Prevents joint separation and improves fatigue life. Target: 75-90% of proof load.

- **Gantry:** Bridge structure spanning machine bed, carrying Y-axis and Z-axis. Types: open (one rail) vs. closed (two rails). Closed gantry: better torsional rigidity.

- **Hysteresis:** Lag between input and output in mechanical systems. Ball screw hysteresis: <2μm typical. Caused by micro-slip in contacts.

- **Inertia (Moment of):** Resistance to rotational acceleration. I = mr² for point mass. Critical for motor sizing and resonance analysis.

- **Kerf:** Width of material removed by cutting process. Plasma: 1-3mm, Fiber Laser: 0.1-0.5mm, Waterjet: 0.5-1.5mm, Router: tool diameter + deflection.

- **Kinematic Coupling:** Exact-constraint mounting using 3 spheres on 3 V-grooves (or equivalents). Provides repeatable positioning <1μm. Used in precision fixtures.

- **Lead:** Linear travel per revolution of screw. Ball screw: 5mm, 10mm, 20mm typical. Lead ≠ pitch for multi-start screws.

- **Linear Guide (Profiled Rail):** Precision bearing system with hardened rail and ball-bearing carriage. Accuracy: ±5-15μm over 300mm. Load ratings: 5-200 kN.

- **Load Capacity:**
  - **Dynamic (C):** For moving loads, L10 life calculation.
  - **Static (C₀):** Maximum load at standstill without permanent deformation.
  - **Moment Loads (M):** Torque about carriage axes. Causes premature wear.

- **Natural Frequency:** Frequency at which structure vibrates freely. fn = (1/2π)√(k/m). Avoid excitation near fn (resonance amplification).

- **Pitch:** Distance between screw threads. Ball screw: pitch × starts = lead. Rack & pinion: pitch circle diameter/# teeth.

- **Preload:** Internal force applied to bearing or screw to eliminate clearance and increase stiffness. Ball screw: 3-7% of dynamic load. Linear guide: light/medium/heavy preload options.

- **Rack and Pinion:** Linear drive converting pinion rotation to rack translation. Module 1.5-3mm typical. Backlash: 0.1-0.3mm (larger than ball screw).

- **Repeatability:** Ability to return to same position. Spec: ±10μm typical for CNC. Better than accuracy (absolute position error).

- **Resolution:** Minimum increment of motion. Encoder: 0.1-1μm typical. Stepper: microstep size (e.g., 1/8 step = 0.025mm for 5mm lead).

- **Runout (TIR):** Total Indicator Reading - maximum deviation of rotating component from true circular path. Spindle target: <5 μm TIR at nose. Collet runout: <10 μm.

- **Static Load Rating (C₀):** Maximum load bearing/guide can support without permanent deformation (0.0001× bearing diameter deformation criterion).

- **Stiffness:** Resistance to deflection under load, measured in N/μm. Higher = better precision under cutting forces. System stiffness: series springs (1/k_total = 1/k₁ + 1/k₂ + ...).

- **Straightness:** Maximum deviation from true straight line over specified length. Linear rail: 20μm/m typical. Measured with autocollimator or laser interferometer.

- **Structural Loop:** Load path from cutting tool to workpiece through machine structure. Shorter/stiffer loop = higher rigidity and accuracy.

- **Thermal Growth:** Dimensional change due to temperature. Aluminum: 23.6 μm/(m·°C). Critical for precision machines - requires thermal compensation or cooling.

- **Tramming:** Squaring spindle axis perpendicular to table. Indicator sweep method. Target: <0.01mm over 300mm diameter.

- **Torsional Rigidity:** Resistance to twisting under torque. Hollow tube 4-8× better than solid shaft of same weight. Critical for gantry beams.

- **Whipping:** High-frequency vibration of unsupported screw section. Occurs above critical speed: Ncrit = (4.76 × 10⁶ × d) / L² (RPM, mm). Requires center support.

---

## M.2 Electrical and Control Terms

- **AC Servo Motor:** Brushless motor with encoder feedback for closed-loop control. Higher power density than steppers. Typical: 0.1-15 kW per axis.

- **Absolute Encoder:** Position sensor providing unique code for each position. Retains position after power loss. Resolution: 17-25 bit (130k-33M positions/rev).

- **Bus Voltage:** DC link voltage in servo drive (rectified AC). Typically 300-400V DC from 230V AC, 600-800V DC from 480V AC.

- **Commutation:** Switching current between motor windings to produce rotation. Stepper: external drive. Servo: internal with encoder feedback (field-oriented control).

- **Current Loop:** Innermost control loop in servo drive. Bandwidth: 1-3 kHz. Controls motor torque proportional to commanded current.

- **Duty Cycle:** Percentage of time component operates vs. rests. Servo peak torque: 30s duty cycle typical (3× continuous). Intermittent: cycles <10 min.

- **Electromagnetic Compatibility (EMC):** Ability of equipment to operate without EM interference. CE marking requires EMC testing per IEC 61000 series.

- **Electromagnetic Interference (EMI):** Unwanted electromagnetic radiation from electrical components interfering with signals. Mitigation: shielded cables, star grounding, ferrites, filters.

- **Encoder:**
  - **Incremental:** Outputs A/B pulses (position change). Requires homing. Z-index pulse per revolution. Typical: 2500-10,000 PPR.
  - **Absolute:** Direct position reading. Battery-backed or multi-turn (magnetic gearing). 17-bit = 131,072 counts/rev = 0.0027°.
  - **Resolver:** Analog rotary transformer. Robust but low resolution. Used in harsh environments.

- **EtherCAT:** Real-time Ethernet protocol for motion control. 1000 axes at 1 kHz cycle time. Beckhoff, Delta, many drives support.

- **Field-Oriented Control (FOC):** Advanced servo algorithm controlling flux and torque independently. Enables maximum torque/amp efficiency.

- **Grounding:** Connecting electrical circuits to earth potential. Types:
  - **Safety Ground:** Green/yellow wire, protects against shock.
  - **Signal Ground:** Common reference for signals. Star topology prevents ground loops.
  - **Chassis Ground:** Frame/enclosure ground. Bonds to safety ground.

- **Hall Effect Sensor:** Magnetic position sensor. Used for commutation in brushless motors (3 sensors, 60° apart). Binary output.

- **Holding Torque:** Maximum torque stepper motor can produce at standstill (0 RPM). Decreases with speed (torque curves).

- **Incremental Encoder:** See Encoder (Incremental). Requires limit switch homing on power-up. More common than absolute (lower cost).

- **Inductance:** Opposition to current change in coil. Motor inductance: 1-50 mH. Limits acceleration capability (voltage = L × di/dt).

- **Inrush Current:** Initial surge current when powering equipment. Servo drive: 20-100× steady-state. Requires soft-start or pre-charge resistor.

- **Isolation (Optical):** Galvanic separation using LED/phototransistor. Isolates sensitive circuits from high-voltage/noisy circuits. Typical: 2500V isolation.

- **Jerk:** Rate of acceleration change (m/s³). High jerk causes vibration. S-curve acceleration profiles limit jerk for smooth motion.

- **Latency:** Delay between command and response. Motion control: <1ms required. Ethernet latency: 0.1-1ms depending on protocol.

- **Microstepping:** Dividing motor full steps into smaller increments (1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128). Smoother motion but lower torque and positional accuracy at high microstep ratios.

- **MOSFET:** Metal-Oxide-Semiconductor Field-Effect Transistor. Fast switching device in motor drives. Low on-resistance (Rds_on: 5-50 mΩ).

- **Optical Isolation:** See Isolation (Optical). Protects control circuits from motor noise and voltage spikes.

- **PID Control:** Proportional-Integral-Derivative feedback controller. Standard servo tuning: Kp (position gain), Ki (integral - removes steady-state error), Kd (derivative - damping).

- **Position Loop:** Outermost servo control loop. Bandwidth: 10-100 Hz. Compares commanded vs. actual position (encoder), outputs velocity command.

- **Power Factor:** Ratio of real power to apparent power. Inductive loads (motors): 0.6-0.9 typical. Unity (1.0) is ideal. VFDs improve power factor.

- **PWM (Pulse Width Modulation):** Motor drive technique varying duty cycle to control average voltage/current. Frequency: 4-20 kHz typical (above audible range).

- **Regenerative Braking:** Converting motor kinetic energy back to electrical energy during deceleration. Requires braking resistor (dissipate) or bus sharing (return to supply).

- **Resolver:** See Encoder (Resolver). Analog rotary position sensor. Rugged but requires resolver-to-digital converter (RDC) chip.

- **RMS (Root Mean Square):** Effective value of AC waveform. Motor continuous ratings in RMS amps/volts. Peak = √2 × RMS for sine wave.

- **Servo:** Closed-loop motor system with encoder feedback for precise position/velocity control. Corrects for disturbances (cutting forces, friction).

- **Shielding:** Conductive layer around cable preventing EM radiation. Braid (80-95% coverage) or foil (100% coverage). Ground shield at ONE end only (avoid ground loops).

- **Slip:** Difference between synchronous speed and actual speed in AC induction motors. 2-5% at full load. Servo motors: zero slip (synchronous).

- **Stepper Motor:** Open-loop motor moving in discrete steps. Holding torque: 0.3-30 N·m. Steps/rev: 200 (1.8°) or 400 (0.9°) typical. Loses steps if overloaded.

- **Transistor Ratings:**
  - **Vds:** Drain-source voltage rating (e.g., 600V MOSFET).
  - **Ids:** Continuous drain current (e.g., 50A MOSFET).
  - **Rds_on:** On-resistance (e.g., 10 mΩ = 0.5W at 10A).

- **Trajectory Planning:** Calculation of position/velocity/acceleration profiles. Trapezoidal profile: constant accel/decel. S-curve: limited jerk.

- **Tuning:** Adjusting PID gains for optimal servo response. Manual (Ziegler-Nichols, Lambda), Auto-tune (drive feature). Goal: fast settling without overshoot.

- **Velocity Loop:** Middle servo control loop. Bandwidth: 100-500 Hz. Compares commanded vs. actual velocity (encoder derivative), outputs current command.

- **VFD (Variable Frequency Drive):** Electronic controller varying AC motor speed by adjusting frequency and voltage (V/Hz control). Spindle control: 0-400 Hz = 0-24,000 RPM.

---

## M.3 CNC Control and Programming Terms

- **Absolute Positioning (G90):** Coordinates specified relative to fixed origin (work zero). Example: G90 G01 X100 → move to X=100.

- **Arc (Circular Interpolation):** G02 (CW) or G03 (CCW) circular path. Parameters: I/J (center offset) or R (radius). Requires XY plane (G17).

- **Automatic Tool Changer (ATC):** Mechanism swapping tools automatically. Carousel type: 8-40 tools. Arm type: 10-20s tool change. ISO 30/40/50 taper.

- **Axis Naming:**
  - **Primary (X, Y, Z):** Linear translation axes. Z typically vertical (spindle axis). Right-hand rule.
  - **Rotary (A, B, C):** Rotation about X, Y, Z respectively. 4th axis: rotary table. 5-axis: A+C or B+C.

- **Canned Cycles:** Pre-programmed routines for common operations. G81 (drilling), G83 (peck drilling), G84 (tapping), G73 (high-speed peck).

- **Compensation:**
  - **Tool Length (G43):** Offset Z position by tool length in table. G43 H01 = use tool 1 length.
  - **Tool Radius (G41/G42):** Offset path left/right by tool radius. Climb milling: G41. Conventional: G42.
  - **Backlash Compensation:** Software correction for mechanical backlash. LinuxCNC: [AXIS_0]BACKLASH parameter.

- **Contour Error (Following Error):** Difference between commanded and actual position during motion. Servo: <0.1mm typical. Exceeding limit triggers alarm.

- **Coordinate System:**
  - **Machine (G53):** Absolute position relative to home switches. Fixed reference.
  - **Work (G54-G59):** User-defined origins for parts. G54 most common. G10 L2 sets offsets.

- **Dry Run:** Test mode running program at reduced speed without tool engaged. Verify program before cutting.

- **DXF (Drawing Exchange Format):** CAD file format. 2D vector graphics. Common CAM input format for plasma/laser/waterjet.

- **Feed Rate:** Speed of tool movement through material (mm/min or in/min). Programmed with F-word. Higher = faster machining but more tool wear. Inverse time (G93) for 5-axis.

- **Feed Per Tooth (Chipload):** Material removed per cutter tooth. Formula: fz = F / (N × RPM) where F=feedrate, N=# teeth. Aluminum: 0.05-0.15 mm/tooth.

- **G-Code:** Machine programming language (RS-274). G00 (rapid), G01 (linear), G02/G03 (arc), G90/G91 (absolute/incremental).

- **HAL (Hardware Abstraction Layer):** LinuxCNC real-time software layer connecting G-code to hardware. Configuration: .hal files. Signals: bit/float/s32/u32 types.

- **Home Switch:** Limit switch establishing machine origin. Homing sequence: rapid to switch, slow off switch, zero position. Index pulse optional (repeatable to 0.1μm).

- **Incremental Positioning (G91):** Coordinates specified relative to current position. Example: G91 G01 X10 → move 10mm from current X.

- **Interpolation:** CNC calculating intermediate points between programmed endpoints. Linear (G01): straight line. Circular (G02/G03): arc. NURBS: complex curves.

- **Inverse Kinematics:** Calculating joint positions for desired tool position. Required for robotic arms, delta robots. LinuxCNC: genserkins, pumakins.

- **Jog Mode:** Manual axis movement via buttons/handwheel. Continuous (hold button) or incremental (0.001", 0.01", 0.1" steps).

- **Look-Ahead:** Controller analyzing upcoming G-code to optimize velocity. Prevents overshoot at corners. Depth: 100-1000 segments typical.

- **M-Code:** Auxiliary machine functions (not motion). M03 (spindle CW), M08 (coolant on), M06 (tool change), M30 (program end).

- **Machine Coordinates:** Absolute position relative to machine home (physical limits). G53 ignores work offsets. Used for tool changes, safe positions.

- **MDI (Manual Data Input):** Keyboard entry of single G-code commands. Useful for setup, probing, jogging to position.

- **Modal:** Command remains active until cancelled. G01 (linear mode), G90 (absolute mode). Non-modal: G04 (dwell), G28 (home).

- **Offsets:**
  - **Work Coordinate (G54-G59):** Part origin locations. G10 L2 P1 X10 Y20 = set G54 to X+10, Y+20.
  - **Tool Length (G43):** Z compensation for tool length. Measured from gage line to tool tip.
  - **Tool Diameter (G41/G42):** Radius compensation around programmed path.

- **Override:** Real-time adjustment of programmed values. Feed override: 0-200% typical. Spindle override: 50-120%. Lets operator fine-tune.

- **Parametric Programming:** Using variables in G-code. #1=10 (assignment), G01 X#1 (use variable). Loops with WHILE, conditionals with IF.

- **Post-Processor:** Software converting CAM toolpaths to machine-specific G-code. Custom posts for each control (Fanuc, Haas, LinuxCNC, Mach3).

- **Probe (Touch Probe):** Precision switch for automatic workpiece/tool measurement. Renishaw: repeatability 0.5μm. G38.2 (probe toward), G38.4 (probe away).

- **Program Stop:** M00 (mandatory stop), M01 (optional stop - requires operator enable). Spindle/coolant off, requires cycle start to continue.

- **Rapid (G00):** Non-cutting move at maximum feedrate. Not guaranteed straight line (may move axes sequentially). No F-word.

- **Real-Time:** System guaranteeing response within specified time. LinuxCNC: 1ms servo cycle, 25μs base thread (steppers). RTAI or Preempt-RT kernel.

- **Scaling (G51):** Proportionally increase/decrease programmed dimensions. G51 X2 Y2 = double size. G50 cancels. Useful for families of parts.

- **Single Block:** Execution mode pausing after each G-code line. Used for program verification and debugging.

- **Spindle Synchronization:** Coordinating spindle rotation with linear motion. Rigid tapping (G33.1): spindle encoder required. Thread milling: G02/G03 with helical interpolation.

- **Subprogram:** Reusable G-code block called with M98 P1234 (call program O1234). M99 returns. Useful for repeated patterns (bolt holes).

- **Tool Offset:** Compensation for tool length/diameter differences. Length offset (G43): Z-axis. Radius compensation (G41/G42): XY plane. Stored in tool table.

- **Tool Table:** Database of tool dimensions. Tool # (T), length offset (H), diameter (D), pocket (P). G10 L1 sets values. G43 H01 applies tool 1 length.

- **Trajectory Planner:** Calculates smooth motion profiles respecting velocity/acceleration limits. Acceleration: 0.5-5 m/s² typical. Jerk limiting optional.

- **Work Offset (G54-G59):** User-defined origin for part coordinates. G54 most common (work offset 1), allows multiple fixtures/setups. Extended: G54.1 P1-P9 (G59.3).

---

## M.4 Machining and Cutting Terms

- **Abrasive Waterjet (AWJ):** Waterjet with garnet abrasive (80 mesh typical). Cuts metals, stone, ceramics. Pressure: 55,000-90,000 PSI. Kerf: 0.8-1.5mm.

- **Adaptive Clearing:** CAM toolpath maintaining constant tool engagement. Varies feedrate and stepover for consistent chip load. Reduces tool wear 30-50%.

- **Built-Up Edge (BUE):** Material welding to tool edge at low speeds. Causes poor finish and tool failure. Solution: increase speed or use coated tools.

- **Chip Evacuation:** Removing chips from cutting zone. Methods: flood coolant (washing), air blast, vacuum, chip conveyor. Poor evacuation causes recutting and heat.

- **Chipload:** Thickness of chip removed per tooth. Formula: Chipload = Feed / (RPM × # teeth). Aluminum roughing: 0.10-0.20 mm/tooth. Finishing: 0.03-0.08 mm/tooth.

- **Chatter:** Self-excited vibration causing poor surface finish and tool breakage. Frequency: 100-5000 Hz. Causes: low rigidity, excessive DOC/WOC, tool runout. Solutions: reduce DOC, change RPM, increase rigidity.

- **Climb Milling (Down Milling):** Cutter rotation direction matches feed direction. Chip thickness: thick to thin. Advantages: better finish, lower forces, longer tool life. Requires backlash elimination.

- **Conventional Milling (Up Milling):** Cutter rotation opposes feed direction. Chip thickness: thin to thick. Advantages: works with backlash. Disadvantages: lifts workpiece, more tool wear.

- **Coolant:** Fluid for cooling tool and workpiece. Types: water-soluble (emulsion, 5-20:1 dilution), synthetic, straight oil, MQL. Functions: cooling, lubrication, chip evacuation.

- **Cutter Compensation:** Tool radius offset (G41/G42). Programming to part edge, controller offsets by tool radius. Enables tool wear compensation without reprogramming.

- **Cutting Force:** Resistance of material to cutting. Components: tangential (Ft), radial (Fr), axial (Fa). Ft = Ks × DOC × WOC × fz^n (specific cutting force Ks from tables).

- **Cutting Speed (Vc):** Velocity at tool cutting edge. Formula: Vc = π × D × N where D=diameter (mm), N=RPM. Steel: 100-300 m/min HSS, 150-500 m/min carbide.

- **Depth of Cut (DOC):** Axial depth tool enters material. Symbol: ap. Roughing: 3-10mm or 50-100% of tool diameter. Finishing: 0.1-0.5mm.

- **EDM (Electrical Discharge Machining):** Material removal by electrical sparks. Wire EDM: 0.1-0.3mm wire cuts intricate shapes. Sinker EDM: shaped electrode. Surface finish: 0.1-3μm Ra.

- **Feeds and Speeds:** Feed rate (mm/min or IPM) and spindle speed (RPM) for specific material/tool combination. Calculate from chipload, # teeth, cutting speed.

- **Fixture:** Device holding workpiece during machining. Types: vise, toe clamps, vacuum table, custom (3-2-1 locating). Rigidity critical - workpiece stiffness > machine stiffness.

- **Flood Coolant:** High-volume coolant delivery (5-50 GPM). Nozzles at tool-workpiece interface. Removes heat and chips. Requires sump, pump, filtration.

- **Garnet (Abrasive):** Crushed mineral for abrasive waterjet cutting. Mesh size: 50 (coarse), 80 (standard), 120 (fine). Cost: $0.10-$0.30/lb. Consumption: 0.3-1.0 lb/min.

- **Heat-Affected Zone (HAZ):** Region near cut edge with altered microstructure. Plasma/laser: 0.5-2mm HAZ. Waterjet/router: zero HAZ (cold cutting).

- **High-Speed Machining (HSM):** Cutting at 5-10× conventional speeds. Aluminum: 15,000-30,000 RPM. Steel: 8,000-15,000 RPM. Requires rigid machine, balanced tools, high-performance spindle.

- **Kerf:** Width of material removed by cutting process. Compensation: program 0.5× kerf inside (internal features) or outside (external features).

- **Lead-In/Lead-Out:** Ramp or arc entry/exit to cut to avoid plunge marks. Circular lead-in: radius 1-5mm. Helps tool engagement and surface finish.

- **Material Removal Rate (MRR):** Volume of material removed per unit time. MRR = DOC × WOC × Feed (mm³/min). Roughing: maximize MRR. Finishing: minimize (better surface).

- **Minimum Quantity Lubrication (MQL):** Micro-mist lubrication (0.01-0.1 mL/hr oil + air). Replaces flood coolant. Benefits: dry chips (recyclable), no disposal, cleaner. Aluminum, cast iron applications.

- **Nesting:** Arranging parts on material sheet to minimize waste. CAM nesting software. Common spacing: 3-10mm between parts (avoid thermal effects in plasma/laser).

- **Pierce:** Initial penetration of material before cutting. Plasma: 2-5 seconds pierce time, height above work (pierce height = 2× cut height). Laser: oxygen assist for thick steel.

- **Power (Spindle):** P = (Ks × DOC × WOC × Feed) / (60 × η) where Ks=specific cutting force (N/mm²), η=efficiency (0.7-0.9). Steel: 0.5-10 kW typical.

- **Radial Immersion:** Percentage of cutter diameter engaged in material. Full slot: 100%. Half slot: 50%. Light finish: 10-30%. Affects cutting forces and tool life.

- **Roughing:** High-MRR material removal leaving finishing stock. Larger DOC/WOC, faster feed, 0.1-0.5mm stock remaining. Surface finish: 3-10 μm Ra.

- **Scallop Height:** Residual cusps between toolpath passes. Smaller stepover = smaller scallop. Formula: h = stepover² / (8R) for ball end mill radius R.

- **Speeds and Feeds:** See Feeds and Speeds. Critical for tool life and surface finish. Too fast: excessive heat/wear. Too slow: built-up edge, poor finish.

- **SFM (Surface Feet per Minute):** Cutting speed at tool edge (imperial). Formula: SFM = (π × D × RPM) / 12 (D in inches). Metric equivalent: Vc (m/min).

- **Stepover:** Lateral offset between toolpath passes. Percentage of tool diameter. Roughing: 40-60%. Finishing: 5-20%. Smaller = better finish, longer cycle time.

- **Surface Finish (Ra):** Arithmetic average roughness. Typical: Roughing 3-10 μm, General 0.8-3 μm, Precision 0.2-0.8 μm, Grinding <0.2 μm. Measured with profilometer.

- **Through-Spindle Coolant (TSC):** High-pressure coolant (50-100 PSI) through hollow spindle and tool. Essential for deep hole drilling (>3× diameter). Rotary union seals coolant to rotating spindle.

- **Trochoidal Milling:** Circular toolpath with advancing motion. Maintains small radial engagement (10-20%). Benefits: longer tool life, higher MRR in hard materials, deeper cuts.

- **Width of Cut (WOC):** Radial depth (stepover in one pass). Symbol: ae. Slotting: 100% diameter. Roughing: 40-60% diameter. Finishing: 10-30% diameter.

- **Work Hardening:** Material surface hardening from plastic deformation. Austenitic stainless (304/316): severe work hardening. Requires positive rake tools and adequate feedrates (avoid rubbing).

---

## M.5 Material and Metallurgy Terms

- **Alloy:** Metal mixture improving properties. Steel: C + Fe + Mn/Cr/Ni. Aluminum: 6061 (Mg+Si), 7075 (Zn). Properties vary widely by composition.

- **Annealing:** Heat treatment reducing hardness and internal stress. Process: heat to 700-900°C, slow cool. Makes material easier to machine.

- **Austenite:** FCC crystal structure of iron (stable above 912°C). Non-magnetic. Retained in stainless 304/316 (austenitic stainless).

- **Carbide (Cemented Carbide):** WC particles in Co binder. Hardness: 1500-2000 HV (vs. 800 HV HSS). Cutting tools: grades C1-C8 (ISO K, M, P). Brittle but heat-resistant.

- **Case Hardening:** Surface hardening via carburizing/nitriding. Hard exterior (50-62 HRC), tough core (30-40 HRC). Gears, bearing races.

- **Cast Iron:** Fe-C alloy with 2-4% carbon. Types: Gray (graphite flakes, good damping), Ductile (nodular graphite), White (cementite, very hard). Machinable without coolant.

- **Ferrite:** BCC crystal structure of iron (stable <912°C). Soft, magnetic. Pure iron mostly ferrite at room temperature.

- **Grain Size:** Crystal size in material. Finer grain = stronger (Hall-Petch effect). Coarse grain: easier to machine but weaker. ASTM grain size number: 5-8 typical.

- **Hardness:** Resistance to deformation. Scales: Rockwell (HRC 20-65), Brinell (HB 100-650), Vickers (HV 100-1000). Conversion tables available. Harder materials require lower feeds/speeds.

- **Heat Treatment:** Controlled heating/cooling altering microstructure. Types: annealing (soften), normalizing (refine grain), quenching (harden), tempering (toughness).

- **High-Speed Steel (HSS):** Tool steel with W, Mo, Cr, V. Hardness: 62-65 HRC. Cutting tools: drills, taps, end mills. Lower cost than carbide but lower heat resistance.

- **Martensite:** Hard, brittle phase formed by rapid quenching steel from austenite. BCT structure. 58-65 HRC typical. Requires tempering to reduce brittleness.

- **Precipitation Hardening:** Strengthening via precipitate formation. Aluminum 6061-T6: Mg₂Si precipitates. Stainless 17-4PH: copper precipitates. Age hardening process.

- **Quenching:** Rapid cooling from austenite temperature forming martensite. Media: water (fastest, cracking risk), oil (moderate), air (slow). Hardness depends on cooling rate.

- **Rockwell Hardness (HRC):** Hardness scale using diamond cone indenter. HRC 20 (mild steel), HRC 30-40 (prehardened steel), HRC 50-60 (hardened steel, cutting tools). Converted to HB, HV.

- **Stainless Steel:** Fe-Cr alloy (>10.5% Cr) forming passive oxide layer. Types:
  - **Austenitic (304, 316):** Non-magnetic, corrosion-resistant, work-hardens severely. Difficult to machine.
  - **Ferritic (430):** Magnetic, less corrosion resistance, easier to machine.
  - **Martensitic (410, 420):** Hardenable, magnetic, moderate corrosion resistance.

- **Temper:** Designation of aluminum heat treatment. T6: solution treated + artificially aged (peak strength). T4: solution treated + naturally aged. O: annealed (soft).

- **Tempering:** Reheating quenched steel to reduce brittleness and stress. Temperature: 150-650°C. Higher temp = softer but tougher. Required after quenching to avoid cracking.

- **Thermal Conductivity:** Heat transfer rate. Aluminum: 205 W/(m·K), Steel: 50 W/(m·K), Stainless: 15 W/(m·K). Higher = better coolant effectiveness, less thermal damage.

- **Toughness:** Energy absorption before fracture. Opposite of brittleness. Charpy/Izod impact tests. Tempered martensite: tough. Untempered martensite: brittle.

- **Ultimate Tensile Strength (UTS):** Maximum stress before failure. Mild steel: 400 MPa. 4140 steel: 655 MPa (annealed) to 1800 MPa (quenched). Design safety factor: 2-4×.

- **Yield Strength:** Stress causing permanent deformation (0.2% offset). Design limit for structures. Mild steel: 250 MPa. Aluminum 6061-T6: 276 MPa. Factor of safety applied.

---

## M.6 Safety and Regulatory Terms

- **Arc Flash:** Explosive electrical fault creating plasma arc. Energy: up to 40 cal/cm² (lethal). Protection: arc-rated PPE, proper clearances, lockout/tagout.

- **ANSI (American National Standards Institute):** Standards organization. B11 series: machine tool safety. Z87.1: eye protection. Z49.1: welding safety.

- **CE Marking:** EU declaration of conformity to safety directives. Required for machinery sold in Europe. Self-certification or notified body assessment.

- **Confined Space:** Area with limited egress and not designed for continuous occupancy. Sump, tank interiors. OSHA 1910.146: permit required, atmosphere testing, rescue plan.

- **Double Insulation:** Two independent layers of insulation protecting against shock. Class II equipment (no ground required). Symbol: square within square.

- **E-Stop (Emergency Stop):** Immediately removes power to motion/spindle. Required by ISO 13850 on all machines. Type: Category 0 (uncontrolled stop) or Category 1 (controlled stop then power off). Red mushroom button with yellow background.

- **Enabling Device:** Three-position switch for pendant operation. Squeezed: machine enabled. Fully pressed or released: machine disabled. Prevents unintended motion.

- **Fall Protection:** Arrest system for work >4 feet height (OSHA). Full-body harness + lanyard + anchor. Machine access platforms require guardrails or personal fall arrest.

- **Ground Fault Circuit Interrupter (GFCI):** Detects current imbalance (leakage to ground) and trips circuit. 5 mA threshold, <25ms trip time. Required for temporary/outdoor 120V circuits.

- **Guarding:** Physical barrier preventing access to hazards. Fixed (permanent), interlocked (door switch), adjustable. ANSI B11.19 specifies distances and openings.

- **Hazard Analysis:** Systematic identification of dangers. Risk = Severity × Probability. ISO 12100 risk assessment. Mitigation hierarchy: eliminate, guard, warn, train, PPE.

- **Interlock:** Safety device preventing machine operation unless conditions met (door closed, guards in place). Positive opening (mechanically driven to open state). Monitored by safety relay/PLC.

- **ISO (International Organization for Standardization):** Global standards body. ISO 12100: machinery safety principles. ISO 13849-1: safety control systems. ISO 13850: emergency stop.

- **Light Curtain:** Optical safety device creating invisible barrier. 14mm spacing between beams typical. Safety category 2 or 4. Response time: 10-30ms. Replaces physical guarding.

- **Lockout/Tagout (LOTO):** Procedure isolating energy sources during maintenance (OSHA 1910.147). Lock device on disconnects, tags identifying worker. De-energize, dissipate stored energy, verify zero energy.

- **Machine Guarding:** See Guarding. OSHA 1910.212 general requirements. Point of operation guarding: distance to hazard vs. opening size tables (1/4" opening = 4" distance minimum).

- **NFPA (National Fire Protection Association):** Fire safety standards. NFPA 70 (National Electrical Code), NFPA 79 (Industrial Machinery Electrical Standard), NFPA 654 (Combustible Dust).

- **OSHA (Occupational Safety and Health Administration):** US workplace safety enforcement. 29 CFR 1910: General Industry standards. 1910.212: machine guarding, 1910.147: LOTO, 1910.1000: air contaminants.

- **PEL (Permissible Exposure Limit):** Maximum airborne concentration of substance allowed (OSHA). Oil mist: 5 mg/m³ (8-hr TWA). Hexavalent chromium (welding stainless): 5 μg/m³.

- **Performance Level (PL):** ISO 13849-1 safety reliability rating. PLa (lowest) to PLe (highest). PLd/PLe: redundant channels, diagnostics, fault tolerance. Emergency stops: typically PLd.

- **PPE (Personal Protective Equipment):** Safety gear required for operation. Hierarchy: last resort (engineering controls preferred). Minimum CNC: Z87.1 safety glasses, hearing protection >85 dB, steel-toe boots.

- **Residual Current Device (RCD):** European term for GFCI. 30 mA threshold typical for personnel protection. 300 mA for equipment protection (fire prevention).

- **Risk Assessment:** Evaluating hazard severity and probability. ISO 12100 methodology. Risk matrix: severity (1-4) × probability (1-4) = risk (1-16). Acceptable risk: <6 typical.

- **Safety Category:** IEC 60204-1 classification of emergency stop reliability. Category 0: uncontrolled stop (immediate power removal). Category 1: controlled stop, then power removal. Category 2: controlled stop, power maintained.

- **Safety Integrity Level (SIL):** IEC 61508 classification of safety system reliability. SIL 1 (10⁻¹ to 10⁻² failure probability) to SIL 4 (10⁻⁵ to 10⁻⁴). Industrial machinery: typically SIL 2.

- **Safety Relay:** Redundant relay module monitoring safety circuits. Dual-channel inputs, force-guided contacts (mechanically linked NO/NC). Pilz, Phoenix Contact manufacturers.

- **Two-Hand Control:** Operator must use both hands on buttons to activate machine. Prevents hands in hazard zone. Anti-tie-down: buttons <300mm apart, must press within 0.5s.

---

## M.7 Measurement and Metrology Terms

- **Accuracy:** Closeness of measurement to true value. Specification: ±10 μm/300mm typical for CNC. Systematic error (calibrated out with compensation).

- **Autocollimator:** Optical instrument measuring angular deviation. Resolution: 0.1 arc-second (0.5 μm/m). Leveling precision machines, measuring spindle axis alignment.

- **Calibration:** Comparison to known standard. Traceable to NIST/NPL national standards. Period: annual for production equipment, quarterly for metrology. Adjustment if out of tolerance.

- **Coordinate Measuring Machine (CMM):** Precision measurement device with touch probe on 3-axis gantry. Accuracy: 2-5 μm typical. Temperature-controlled room (20°C ±1°C).

- **Dial Indicator:** Contact probe with 0.001" (0.01mm) resolution. Long-range (1-3"), continuous dial. Used for setup, runout measurement, tramming spindle.

- **Feeler Gauge:** Precision thickness blades for measuring gaps. 0.001" (0.025mm) to 0.040" (1mm) typical set. Used for gap setting, workpiece leveling.

- **Gauge Block (Jo Block):** Precision length standard. Grade 0: ±0.05 μm, Grade 1: ±0.1 μm, Grade 2: ±0.2 μm. Wrung together to create exact lengths. Calibration reference.

- **Interferometry (Laser):** Optical measurement using light wave interference. Accuracy: <1 ppm (1 μm/m). Renishaw XL-80 laser: 0.5 ppm linear accuracy. Machine tool calibration.

- **Micrometer:** Precision screw-threaded measuring instrument. 0.001" (0.01mm) graduation, 0.0001" (0.001mm) vernier. Outside, inside, depth types. Thimble friction ratchet for consistent force.

- **Parallax Error:** Measurement error from viewing dial at angle. Avoided by perpendicular viewing or mirror scale (align pointer with reflection).

- **Precision:** Repeatability of measurements (scatter). Standard deviation of repeated measurements. High precision with poor accuracy: systematic error (bias).

- **Repeatability:** Ability to return to same position. Spec: ±10 μm typical for CNC. Better than accuracy (absolute position error). Critical for production machining.

- **Resolution:** Minimum increment of motion or measurement. Encoder: 0.1-1 μm typical. Stepper: microstep size. Display resolution ≠ accuracy.

- **Straightedge:** Precision flat reference. Grade A: 50 μm/m, Grade AA: 15 μm/m. Camelback beam shape (self-weight sag compensation). Used with feeler gauges, height gauges.

- **Surface Plate:** Precision flat reference surface. Granite (Grade A, AA, AAA). Grade A: 25 μm over 600×900mm plate. Temperature-stable (20°C). Inspection and layout.

- **Test Indicator (Dial Test Indicator):** Horizontal plunger indicator with 0.0001"-0.001" graduation. Small contact point. Used for fine centering, edge finding, small radii.

- **Tolerance:** Acceptable variation from nominal dimension. ±0.1mm typical. ISO 2768: general tolerances (fine, medium, coarse). Geometric tolerances: position, flatness, perpendicularity (GD&T).

- **Traceability:** Documented chain to national standards. Calibration certificate from NIST-accredited lab. Required for AS9100 aerospace, ISO 17025 metrology labs.

- **Vernier Scale:** Secondary scale for interpolation between main scale graduations. 0.02mm or 0.001" resolution typical. Used on calipers, height gauges, protractors.

---

## M.8 Plasma, Laser, and Waterjet Terms

- **Abrasive Waterjet (AWJ):** See Waterjet terminology. Garnet cutting hard materials (steel, titanium, stone, glass).

- **Assist Gas:** Gas flow during laser cutting improving quality and speed. Oxygen (steel: exothermic oxidation), Nitrogen (stainless, aluminum: inert, no oxidation), Air (mild steel, budget option).

- **Beam Divergence:** Laser beam spreading with distance. <0.1 mrad typical for fiber lasers. Affects focal position sensitivity and cut edge taper.

- **Consumables (Plasma):** Electrode, nozzle, swirl ring, shield cap. Life: 1-4 hours piercing heavy plate, 10-50 hours cutting thin sheet. Cost: $5-$30 per set depending on amperage.

- **Cutting Height:** Nozzle standoff from workpiece. Plasma: 3-6mm (initial height controllers maintain). Laser: focal point at or below surface. Waterjet: 2-5mm (abrasive jet spread).

- **Dross:** Solidified slag on cut edge underside. Plasma/laser: oxidized metal. Minimized by proper parameters (speed, gas flow, height). Removal: grinding, wire wheel.

- **Focal Length:** Distance from laser lens to focal point. Common: 5" (127mm), 7.5" (190mm). Shorter = smaller spot, thinner material. Longer = more working distance, less sensitive.

- **Heat-Affected Zone (HAZ):** See Machining Terms. Plasma: 1-2mm HAZ with hardness changes. Laser: 0.3-1mm HAZ. Waterjet: zero HAZ (cold process).

- **Hypertherm:** Leading plasma system manufacturer. PowerMax (handheld), Powermax (light duty), HPR (heavy duty). Market standard for CNC plasma.

- **Kerf Width:** See General terms. Plasma: 1-3mm depending on amperage (45A-200A). Laser: 0.1-0.5mm (1-6 kW fiber). Waterjet: 0.8-1.5mm (orifice + abrasive expansion).

- **Nozzle (Plasma):** Copper component focusing plasma arc. Orifice size: 0.8-2mm depending on amperage. Cools rapidly during cutting. Replace when orifice eroded >25%.

- **Orifice (Waterjet):** Sapphire or diamond jewel forming high-pressure water stream. Diameter: 0.010"-0.020" (0.25-0.50mm). Life: sapphire 50-100 hrs, diamond 800-2000 hrs.

- **Pierce (Plasma/Laser):** Initial penetration before cutting. Plasma: 1-5 seconds at 1.5-2× cut height to avoid blowback. Laser: 0.1-2 seconds depending on power and thickness.

- **Power Density:** Laser power per unit area. 10⁶-10⁸ W/cm² for cutting. Higher = faster cutting speeds. Focused fiber laser: 10× CO₂ laser power density.

- **Preheat (Plasma):** Lower-amperage arc stabilization before main arc transfer. 10-30A preheat. Improves arc starts and consumable life.

- **Taper (Cut Edge):** Angle deviation from vertical. Plasma: 0-3° typical. Laser: 0-2°. Waterjet: trailing edge (jet lag). Minimized by slow speeds and proper standoff.

- **THC (Torch Height Control):** Automated nozzle height adjustment during cutting. Capacitive sensor (non-contact) or arc voltage (plasma). Maintains constant height over warped sheets.

- **Transfer Arc:** Main plasma cutting arc (vs. pilot arc). Workpiece completes electrical circuit. Higher efficiency than non-transfer arc (gouging).

- **Wavelength:** Laser light wavelength. CO₂: 10.6 μm (infrared). Fiber/Nd:YAG: 1.06 μm (near-infrared). Fiber absorbed better by metals (higher cutting efficiency).

---

**End of Glossary**
