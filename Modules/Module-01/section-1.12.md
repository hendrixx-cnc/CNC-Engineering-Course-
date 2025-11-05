## 12. Linear Motion & Drive Foundations: System Integration and Commissioning

### 12.1 Integration Philosophy: Bridging Mechanical Structure to Motion Control

The mechanical frame (Sections 1-11) provides the structural foundation, but the machine only becomes functional when linear motion systems are integrated:

1. **Profile rail linear guides** convert the frame's geometric datums into precision motion paths
2. **Drive systems** (racks, screws) translate motor rotation into linear motion
3. **Mounting techniques** transfer the datum precision from flatbars to moving components
4. **Lubrication and sealing** ensure long-term performance under contaminated environments

This section addresses the **system-level integration** of these components, building upon the detailed component analyses in earlier sections (helical racks in Section 3, ball screws in Section 4.2) and referencing the comprehensive tribology and preload mechanics detailed in **Module 3 (Linear Motion Systems)**.

### 12.2 Profile Rail Linear Guide Selection and Specification

#### **12.2.1 Rail Size and Load Rating**

Profile rails are designated by series and size: **HGR20** = Hiwin, G-series (moderate preload), Rail size 20 (width = 20mm).

**Load Rating Parameters:**

- **$C$** = Dynamic load rating (N): Load for 50 km travel life (L10)
- **$C_0$** = Static load rating (N): Maximum static load for permanent deformation <0.0001 × ball diameter
- **$M$** = Moment load rating (N·m): Allowable moment about each axis

**Life Calculation** (per ISO 281):

$$L_{10} = \left(\frac{C}{P}\right)^3 \times 50 \text{ km}$$

where $P$ = equivalent dynamic load (N), accounting for radial, moment, and preload effects.

**Practical Example: Y-Axis Rail Selection**

**Given Requirements:**
- Axis travel: 2,500 mm
- Gantry + payload mass: 400 kg → $W = 3,924$ N per rail pair (two rails, load shared)
- Acceleration: 1 m/s² → $F_{accel} = 400 \times 1 = 400$ N
- Design life: 10,000 hours at 50% duty cycle, 15 m/min average speed
  - Total travel: $10,000 \times 0.5 \times 15 \times 60 = 4,500$ km

**Load Calculation:**

$$P = F_W + F_{accel} + F_{preload}$$

where:
- $F_W = 3,924/2 = 1,962$ N per rail (static component)
- $F_{accel} = 400/2 = 200$ N per rail (dynamic component, bidirectional)
- $F_{preload} \approx 0.1 \times C$ (medium preload, Z1 class)

Try **HGR25** (25mm rail):
- $C = 32,760$ N (dynamic rating)
- $C_0 = 47,380$ N (static rating)
- $F_{preload} = 0.1 \times 32,760 = 3,276$ N

$$P = 1,962 + 200 + 3,276 = 5,438 \text{ N}$$

**Life Check:**

$$L_{10} = \left(\frac{32,760}{5,438}\right)^3 \times 50 = (6.02)^3 \times 50 = 10,920 \text{ km}$$

**Result**: 10,920 km >> 4,500 km requirement → **HGR25 acceptable with 2.4× safety factor**.

#### **12.2.2 Rail Length and Block Quantity**

**Rail Length:** Match axis travel + mounting margin:

$$L_{rail} = L_{travel} + 2 \times S_{block} + 100\text{–}150 \text{ mm}$$

where $S_{block}$ = length of linear bearing block (~60–100 mm depending on size).

For 2,500 mm Y-axis travel with HGR25 blocks (length 77.5 mm):

$$L_{rail} = 2,500 + 2 \times 77.5 + 150 = 2,805 \text{ mm}$$

**Standard rail available:** 3,000 mm → Use 3,000 mm rail, cut to 2,805 mm or leave full length.

**Block Quantity per Rail:**

**Minimum:** 2 blocks per carriage (defines one line of support)

**Typical:** 4 blocks per rail (2 blocks per carriage, 2 carriages per gantry side)
- Provides moment rigidity (resists pitch and yaw)
- Distributes load (reduces load per ball → longer life)
- Allows adjustment via spacer shims

**Block Spacing:**

For gantry beam of length $L_{gantry} = 1,500$ mm:
- Outer blocks at $\pm 600$ mm from center → span = 1,200 mm
- Provides moment arm to resist torsion from X-axis carriage offset

**Rule of Thumb:** Block spacing $S_{blocks} = 0.6$–0.8 × gantry width for optimal stiffness-to-mass ratio.

### 12.3 Rail Mounting to Datum Surfaces: Precision Installation

#### **12.3.1 Pre-Installation Verification**

**1. Datum Surface Preparation (from Section 9)**
- Flatness: ±0.010 mm over full length
- Straightness: ±0.015 mm over full length
- Surface finish: Ra < 3.2 µm (N7 grind or better)
- Parallelism (for dual rails): ±0.020 mm over full span

**2. Rail Inspection**
- Straightness (manufacturer spec): ±0.005 mm per meter typical for precision-grade rails
- Mounting hole position tolerance: ±0.05 mm
- Surface rust or damage: None (clean with solvent if slight oxidation)

**3. Fastener Preparation**
- Socket-head cap screws: M8×1.25 for HGR20/25, length = rail height + datum thickness + 1.5×diameter
- Grade: 12.9 (high-strength)
- Washers: Hardened steel, thickness 1.5–2.0 mm
- Thread locker: Medium-strength (Loctite 243) for prevention of vibration loosening

#### **12.3.2 Installation Procedure: 10-Step Protocol**

**Step 1: Datum Cleaning**
- Solvent-clean flatbar surface (acetone or isopropyl alcohol)
- Dry with lint-free cloth
- Protect from contamination until rail mounted

**Step 2: Rail Positioning and Clamping**
- Place rail on datum, align to reference edge using precision ground parallels or dial indicator
- C-clamp at 3–4 locations along length (hand-tight, no deformation)
- Verify straightness: Place granite straight-edge (accuracy 0.005 mm/m) on rail top surface, sweep 0.001 mm indicator along length
  - Deviation must be <0.015 mm peak-to-peak

**Step 3: Hole Preparation**
- Using rail as template, center-punch hole locations
- Remove rail, drill tap holes:
  - M8 tap: 6.8 mm drill through datum flatbar
  - If flatbar sits on steel frame: Drill 8.5 mm clearance hole through frame (allows micro-adjustment)
- Tap holes to M8×1.25 depth = 1.5×diameter = 12 mm minimum
- De-burr holes, clean chips with vacuum and solvent

**Step 4: Trial Fit**
- Re-position rail, insert all fasteners finger-tight
- Check alignment:
  - Straightness (granite straight edge + indicator): <0.010 mm
  - Parallelism to reference edge: <0.020 mm (measured at 3 points along length)
- If misaligned: Micro-adjust by loosening one end, tapping with soft mallet, re-check

**Step 5: Preload Application and Torquing**
- Apply thin film of retaining compound (Loctite 638) to fastener threads (optional, prevents loosening)
- Torque sequence:
  1. Start at center fastener, torque to 50% final (for M8 Grade 12.9: 50% × 22 N·m = 11 N·m)
  2. Work outward in alternating pattern (center → end A → end B → intermediate positions)
  3. Second pass: 75% torque (16.5 N·m)
  4. Final pass: 100% torque (22 N·m)

**Step 6: Post-Torque Straightness Verification**
- Re-check straightness with indicator sweep
- Acceptable: <0.012 mm deviation (torque-induced clamping may introduce 0.002–0.005 mm distortion)
- If excessive: Loosen fasteners in affected zone, re-torque with reduced torque (18 N·m), add shim under rail (brass shim stock, 0.025 mm thickness)

**Step 7: Block Installation and Preload Verification**
- Install bearing blocks on rail
- Slide blocks by hand through full travel:
  - Z0 (light preload): Slides with 20–50 N force (measurable with fish scale or force gauge)
  - Z1 (medium preload): 50–100 N force (typical for CNC)
  - Z2 (heavy preload): 100–200 N force (high stiffness, high-load applications)
- Preload should feel **uniform along full travel** (no tight spots indicating local rail distortion)

**Step 8: Lubrication System Installation**
- Install lubrication fittings on each block (Zerk grease fittings or automatic lube manifold connection)
- Initial lubrication: Pump NLGI #2 lithium-based grease until old grease purges from seals (typically 2–3 pumps per fitting)
- Cycle blocks through 10 complete traverses to distribute lubricant

**Step 9: Dual-Rail Parallelism Verification (Y-Axis Critical)**
- Install bearing blocks on both left and right rails
- Mount gantry beam dummy (precision ground bar, length = gantry width, straightness <0.015 mm)
- Attach dial indicators to beam ends, positioned to contact each rail top surface
- Traverse full length:
  - Parallelism error = difference in indicator readings at any position
  - Acceptable: <0.030 mm over 2,500 mm travel (±0.015 mm per rail)
- If out-of-spec: Identify high/low zones, adjust with shims (0.025 mm brass shim stock)

**Step 10: Final Documentation**
- Record:
  - Rail serial numbers and positions (left vs. right)
  - Torque values applied
  - Straightness measurements (3 positions minimum)
  - Parallelism measurements (5 positions minimum)
  - Lubrication type and quantity
- Photograph installation for future reference
- Create maintenance schedule (Section 12.7)

#### **12.3.3 Common Installation Errors and Corrections**

| Error | Symptom | Cause | Correction |
|-------|---------|-------|------------|
| **Wavy motion** | Position error varies sinusoidally with position | Rail supported on uneven surface (unsupported sections between fasteners) | Increase fastener density, shim low spots |
| **Binding/tight spots** | Increased friction at specific positions | Over-torqued fasteners distorting rail, debris under rail | Loosen fasteners, re-clean surface, shim if needed |
| **Excessive wear** | Premature bearing failure (<1,000 km life) | Insufficient lubrication, contamination ingress, misalignment | Improve sealing, increase lube frequency, check parallelism |
| **Noise/vibration** | Audible rumbling, vibration during motion | Damaged balls, contamination, preload mismatch | Replace blocks, flush and re-lubricate, verify preload class |
| **Gantry racking** | Gantry beam not perpendicular to Y-rails | Left/right rail parallelism error >0.05 mm | Re-shim rails, use laser diagonal test to verify squareness |

### 12.4 Rack and Pinion Drive System Integration

#### **12.4.1 Rack Mounting Specifications**

**Rack Selection** (from Section 3 analysis):
- Module: 1.25
- Helix angle: 15° (standard)
- Material: Case-hardened steel, 58–62 HRC surface
- Length: 1,000 mm sections (standard), joined end-to-end for longer axes

**Mounting Configuration:**

Racks mount to **opposite side of flatbar from linear guide rails** to maintain symmetric loading and thermal expansion balance.

**Fastening:**
- M8 socket-head cap screws, 150 mm spacing
- Countersunk holes in rack base (flush-mount to minimize height)
- Dowel pins at joints (Ø6 mm, h7 tolerance) for precision alignment

**Installation Procedure:**

**Step 1: Rack Section Alignment**
- Lay first rack section on flatbar, reference to datum edge
- Drill and tap mounting holes, install first section
- Install precision dowel pins (Ø6 × 10 mm, h7 press-fit into flatbar, g6 clearance in rack)
- Position next section, align using dowel pins (ensures pitch continuity ±0.01 mm)
- Repeat for all sections

**Step 2: Rack Straightness Verification**
- Mount dial indicator on carriage (secured to bearing blocks)
- Indicator stylus contacts rack tooth flank
- Traverse full length, record indicator readings
- Maximum run-out: ±0.020 mm (per tooth variation <0.015 mm)

**Step 3: Rack-to-Rail Parallelism**
- Rack centerline must be parallel to rail within ±0.03 mm over full length
- Measure distance from rail reference surface to rack tooth flank at 500 mm intervals
- Adjust using shims if needed

#### **12.4.2 Pinion and Gearbox Installation**

**Pinion Specification:**
- 40 teeth, Module 1.25 → Pitch diameter = 1.25 × 40 = 50 mm
- Face width: 20 mm (matches rack width)
- Material: Case-hardened alloy steel, 58–62 HRC
- Accuracy: DIN 6 quality (comparable to AGMA 10-11)

**Gearbox Selection:**
- Type: Planetary (concentric input/output, high torque density)
- Ratio: 10:1 (reduces motor speed from 3,000 RPM to 300 RPM)
- Backlash: <5 arcmin (0.083°) → linear backlash = $\frac{50 \times \pi \times 0.083}{360} = 0.036$ mm
- Mounting: NEMA 34 or IEC 90 mm flange interface

**Motor Selection:**
- Y-axis (gantry): 750W AC servo, 2.39 N·m rated torque, 3,000 RPM rated speed
- X-axis (carriage): 400W AC servo, 1.27 N·m rated torque, 3,000 RPM
- Encoder: 2,500 line (10,000 counts/rev after quadrature) → resolution = $\frac{50 \times \pi}{10,000 \times 10} = 0.00157$ mm

**Mounting Procedure:**

**Step 1: Gearbox-to-Motor Coupling**
- Use zero-backlash coupling (bellows or oldham type, stiffness >10,000 N·m/rad)
- Align motor shaft to gearbox input shaft using laser alignment tool (angularity <0.05 mm/m)
- Torque coupling clamp screws to manufacturer spec

**Step 2: Pinion-to-Gearbox Shaft Mounting**
- Pinion bore: Typically 16–20 mm with keyway (ISO R773)
- Secure pinion to gearbox output shaft using:
  - Key (DIN 6885): 6×6 mm for Ø18 shaft
  - Locking collar or shaft clamp (double-slit type, friction grip)
- Ensure pinion face is within 0.1 mm of rack face (lateral alignment)

**Step 3: Mesh Adjustment**
- **Center Distance**: Position gearbox/motor assembly such that pinion meshes with rack at correct center distance:

$$CD = \frac{m (Z_{pinion} + Z_{rack,equiv})}{2} = \frac{1.25 \times (40 + \infty)}{2} \rightarrow \text{use } r_{pinion} = 25 \text{ mm}$$

- **Backlash Measurement**: Insert 0.05–0.10 mm feeler gauge between pinion and rack teeth on non-driving flank
  - Adjust center distance (via slotted motor mount holes) to achieve 0.05–0.08 mm backlash
  - Tighten motor mount bolts: M8 Grade 12.9, torque to 22 N·m

**Step 4: Preload Implementation (If Using Dual-Motor Drive)**
- For dual-motor Y-axis (left and right), implement **torque biasing** (Section 3.1.3):
  - Command 5–10% of rated torque as opposing preload
  - Monitor motor currents: Should be equal ±10% during steady-state motion
  - Effective backlash after preload: <0.010 mm (verified via laser interferometry)

### 12.5 Z-Axis Ball Screw System Integration

#### **12.5.1 Ball Screw Specification** (Detailed Analysis in Module 3)

**Given Specification** (from Section 2 case study):
- Diameter: Ø16 mm
- Lead: 5 mm (single-start)
- Precision: C7 grade (±52 µm/300 mm positioning accuracy)
- Preload: 3–5% of dynamic load rating (light preload for precision)
- Length: 350 mm between bearings (for 150 mm Z-travel)

**Life Calculation:**

Dynamic load:
- $F = m \cdot g + F_{cutting} = (50 \times 9.81) + 200 = 690$ N
- Preload: $F_{preload} = 0.04 \times C = 0.04 \times 15,000 = 600$ N (typical for Ø16, C7 screw)

Equivalent load:

$$P = F + F_{preload} = 690 + 600 = 1,290 \text{ N}$$

Required life: 10,000 hours at 10 m/min average (Z-axis usage is intermittent):
- Total distance: $10,000 \times 0.3 \times 10 = 30$ km (30% duty cycle)

Life calculation:

$$L_{10} = \left(\frac{C}{P}\right)^{3} \times 1 \text{ million revs}$$

For Ø16, C7 screw: $C \approx 15,000$ N

$$L_{10} = \left(\frac{15,000}{1,290}\right)^3 = (11.63)^3 = 1,573 \text{ million revs}$$

At 5 mm lead:

$$L_{10,km} = \frac{1,573 \times 10^6 \times 5}{10^6} = 7,865 \text{ km}$$

**Result**: 7,865 km >> 30 km → **260× safety factor, acceptable**.

#### **12.5.2 Mounting Configuration**

**Fixed-End Bearing (Nut-End)**:
- Angular contact ball bearings in back-to-back configuration (for axial stiffness)
- Bearing size: 30 mm OD, 15 mm ID (e.g., 7002 ACDGA/P4A)
- Preload: 100–200 N axial (light preload)
- Axial stiffness: ~150 N/µm

**Floating-End Bearing (Motor-End)**:
- Deep groove ball bearing or single angular contact
- Radially fixed, axially free (allows thermal expansion of screw)
- Bellows coupling to motor (accommodates 0.5 mm axial growth, 0.2 mm radial misalignment)

**Nut Mounting**:
- Ball nut attaches to Z-axis carriage via precision-machined adapter plate
- Dowel pins (Ø6 mm) ensure repeatable positioning
- Preload nut (double-nut type or preloaded single nut) eliminates axial backlash

### 12.6 Motor Sizing and Drive Selection

#### **12.6.1 Torque Requirements**

**Y-Axis Gantry Motor Sizing:**

**Load Components:**
1. **Friction**: $F_f = \mu (W + F_{preload})$ where $\mu = 0.003$ (linear guides), $W = 3,924$ N, $F_{preload} = 800$ N
   $$F_f = 0.003 \times (3,924 + 800) = 14.2 \text{ N}$$

2. **Acceleration**: $F_a = m \cdot a = 400 \times 1.5 = 600$ N (for 1.5 m/s² rapid acceleration)

3. **Cutting force**: $F_c = 200$ N (typical plasma torch reaction force)

4. **Total linear force**: $F_{total} = 14.2 + 600 + 200 = 814$ N

**Convert to motor torque:**

$$T_{motor} = \frac{F_{total} \times r_{pinion}}{G \times \eta}$$

where:
- $r_{pinion} = 25$ mm (radius of 40-tooth, Module 1.25 pinion)
- $G = 10$ (gearbox ratio)
- $\eta = 0.85$ (combined efficiency of gearbox and rack/pinion)

$$T_{motor} = \frac{814 \times 25}{10 \times 0.85} = \frac{20,350}{8.5} = 2,394 \text{ N·mm} = 2.39 \text{ N·m}$$

**Motor Selection:**
- **Rated torque ≥ 2.39 N·m**
- Rated speed: 3,000 RPM (provides max linear speed = $\frac{3.14 \times 50 \times 300}{1,000} = 47.1$ m/min)
- Power: $P = \frac{T \times \omega}{9,550} = \frac{2.39 \times 3,000}{9,550} = 750$ W

**Selected**: 750W AC servo motor, 2.39 N·m continuous torque, 7.2 N·m peak (3× continuous)

#### **12.6.2 Servo Drive Configuration**

**Drive Specifications:**
- Input: 220V AC, single-phase or 3-phase
- Output: 3-phase variable frequency/voltage to motor
- Control modes: Position, velocity, torque
- Communication: EtherCAT, CANopen, or pulse/direction

**Tuning Parameters** (Simplified; detailed in Module 4 - Control Electronics):

**Position Loop:**
- $K_p$ = 50–100 (position gain, 1/s)
- Determines stiffness and following error

**Velocity Loop:**
- $K_v$ = 200–500 (velocity gain, 1/s)
- $T_i$ = 5–10 ms (integral time constant)
- Determines speed regulation and disturbance rejection

**Filters:**
- Notch filters at structural resonances (from Section 6.4): Place notch at $f_n$ ± 5 Hz, depth 20–30 dB

### 12.7 Lubrication and Maintenance

#### **12.7.1 Lubrication Schedule**

| Component | Lubricant Type | Initial | Interval | Method | Quantity |
|-----------|---------------|---------|----------|--------|----------|
| **Linear guide blocks** | NLGI #2 lithium grease | Installation | 500–1,000 km or 6 months | Manual grease gun or auto-lube system | 2–3 cc per block |
| **Rack and pinion** | ISO VG 220 gear oil | Installation | 1,000 km or 12 months | Drip oiler or spray | Light film, no pooling |
| **Ball screw** | NLGI #2 lithium grease or ISO VG 68 oil | Installation | 500 km or 6 months | Grease: manual; Oil: wick or drip | Grease: 1–2 cc; Oil: 2–5 drops/min |
| **Motor bearings** | Sealed, pre-lubricated | Factory | 20,000 hours | None (sealed for life) | N/A |
| **Gearbox** | ISO VG 220 synthetic | Factory fill | 2,000 hours | Drain and refill | Per manufacturer (typically 0.2–0.5 L) |

**Automatic Lubrication Systems:**
- Progressive divider blocks (Bibus, SKF) distribute grease from central reservoir to multiple points
- Reduces manual labor, ensures consistent lubrication
- Cost: $500–2,000 depending on number of outlets

#### **12.7.2 Inspection and Adjustment Schedule**

**Weekly (or every 40 operating hours):**
- Visual inspection: Check for unusual wear, contamination, leaks
- Audible check: Listen for grinding, rumbling, or irregular noise
- Lubrication check: Verify grease present at linear block seals

**Monthly (or every 200 hours):**
- Positional accuracy check: Run ISO 230-2 abbreviated test (5 positions, bidirectional)
- Backlash measurement: Command ±0.1 mm reversals, measure with indicator
- Fastener torque verification: Spot-check 10% of rail mounting bolts (should not turn with torque wrench set to 90% spec)

**Quarterly (or every 1,000 hours):**
- Full positional accuracy test (21-point ISO 230-2)
- Rail parallelism re-check (bridge gauge method, Section 8.3.2)
- Gearbox oil analysis (if applicable): Check for metal particles indicating wear

**Annually (or every 5,000 hours):**
- Bearing block replacement (if wear limits reached: >0.05 mm backlash increase)
- Rack wear inspection: Measure tooth thickness with gear tooth caliper (acceptable wear: <10% reduction)
- Complete system re-calibration (laser interferometry, ballbar testing)

#### **12.7.3 Sealing and Contamination Management**

**Linear Guides:**
- Standard seals: Contact seals on block ends (rubber or felt)
- Upgrade: Add scrapers or bellows boots for plasma/laser environments (metal chips, slag)

**Racks:**
- Cover with flexible bellows (nylon-reinforced rubber) spanning full travel
- Prevents chip accumulation in tooth gaps

**Ball Screws:**
- Telescoping covers (steel or polymer) protect screw from contamination
- Wiper seals at nut interface

**Effectiveness:** Proper sealing extends component life by 3–5× in contaminated environments.

### 12.8 System Commissioning: From Assembly to First Part

**Phase 1: Mechanical Verification (No Power)**
- [ ] All fasteners torqued to spec
- [ ] Rails parallel within ±0.03 mm
- [ ] Racks installed, run-out <0.02 mm
- [ ] Manual motion smooth (no binding, uniform preload feel)
- [ ] Lubrication applied, no leaks

**Phase 2: Electrical Integration**
- [ ] Motors wired to drives (verify phase sequence with motor rotation test)
- [ ] Encoders connected, signals verified (A, B, Z pulses present)
- [ ] E-stops functional (test hard-wired safety circuit)
- [ ] Limit switches installed and tested (physical home switches at Y-, X-, Z- travel limits)

**Phase 3: Initial Motion Tests**
- [ ] Jog each axis at 10% rapid speed: Smooth, quiet, no vibration
- [ ] Home all axes (using limit switches or index pulse)
- [ ] Run programmed moves: 100 mm increments, bidirectional, verify position with indicator

**Phase 4: Performance Verification**
- [ ] Maximum speed test: Achieve 80% of calculated max speed without fault
- [ ] Acceleration test: Reach target acceleration (1.5 m/s² for Y-axis) without following error >0.5 mm
- [ ] Laser interferometry accuracy test: ±0.050 mm over full travel

**Phase 5: First Part Production**
- [ ] Load test program (simple square or circle)
- [ ] Run at 50% feedrate, verify dimensional accuracy with calipers
- [ ] Increase to 100% feedrate, verify no degradation
- [ ] Inspect part for witness marks, dimensional errors, surface finish issues

**Acceptance Criteria:**
- Positional accuracy: ±0.050 mm (per ISO 230-2)
- Repeatability: ±0.010 mm (2σ)
- Backlash: <0.020 mm (closed-loop)
- Maximum speed: >80% of design target
- No thermal drift >0.05 mm/10°C after 30-minute warm-up

***


---

## References

1. **THK Linear Motion Systems Catalog** - Linear guide specifications and mounting
2. **Hiwin Linear Guideway Technical Manual** - Preload selection and installation
3. **NSK Linear Guides CAT. No. E728g** - Profile rail systems engineering data
4. **ISO 14728-1:2017** - Rolling bearings - Linear motion rolling bearings - Part 1: Dynamic load ratings
5. **Slocum, A.H. (1992).** *Precision Machine Design*. SME. - Linear bearing system selection
6. **LinuxCNC Integration Manual** - Motor and drive configuration
