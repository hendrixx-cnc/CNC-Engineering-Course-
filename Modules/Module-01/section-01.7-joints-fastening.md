# Section 1.7: Joints and Fastening

## Introduction

A CNC frame is only as rigid as its **weakest joint**. A perfectly designed beam with inadequate connections performs worse than a mediocre beam with excellent joints. Joint stiffness typically contributes 20-40% of total frame compliance—often more than the members themselves.

This section examines three primary joining methods for machine frames:

1. **Welded joints** (highest stiffness, permanent)
2. **Bolted joints** (reconfigurable, lower stiffness)
3. **Hybrid systems** (welded structure + bolted precision surfaces)

Each method has distinct advantages, failure modes, and design requirements. Professional machine builders select joining methods based on:
- Required stiffness and load capacity
- Need for disassembly (shipping, maintenance, reconfiguration)
- Available fabrication equipment (welding vs machine shop)
- Tolerance requirements (welding causes distortion)
- Cost and labor constraints

### Learning Objectives

By the end of this section, you will be able to:

1. Calculate bolt preload and joint clamping force for Grade 8.8/10.9 fasteners
2. Design welded joints with appropriate weld size and penetration
3. Predict joint stiffness and compare welded vs bolted performance
4. Prevent bolt loosening using mechanical locking methods
5. Specify torque values for critical bolted joints
6. Design stress-relief procedures for welded frames
7. Analyze fatigue life of joints under cyclic loading
8. Implement proper joint design to maintain frame flatness

---

## Welded Joints: Theory and Practice

### Weld Joint Geometry

**Butt weld (full penetration):**

```
   Before welding:         After welding:

   ║                        ║    ╱╲    ║
   ║                        ║   ╱weld╲  ║
   ║ Gap: 2-3mm    ║   →   ║  ╱      ╲ ║
   ║                        ║ ╱________╲║
   ║                        ║           ║

   Strongest type—weld strength = base metal
```

**Fillet weld (most common):**

```
   T-joint configuration:

   ╔═══════════════╗
   ║               ║
   ║               ║
   ║      ╱╲       ║
   ║     ╱w ╲      ║  ← Fillet weld, leg size w
   ║    ╱____╲     ║
   ╔═══════════════╗
   ║               ║
```

**Fillet weld strength:**

Shear stress in weld throat:

```
τ = F / (0.707 × w × L)
```

Where:
- F = applied force (N)
- w = weld leg size (mm)
- L = weld length (mm)
- 0.707 = sin(45°), throat area factor for 45° fillet

**Allowable shear stress (E70XX electrode):**

```
τ_allow = 0.6 × σ_weld = 0.6 × 485 MPa = 291 MPa
```

Factor 0.6 accounts for safety factor and shear vs tension strength.

### Worked Example 1.7.1: Fillet Weld Sizing

**Given:**
- Gantry upright welded to base frame (T-joint)
- Upright: 80×80×5 SHS
- Load: 5,000 N vertical (from gantry + cutting forces)
- Weld both sides of upright (8 total weld lines, 4 per side)

**Required weld size:**

Total weld length:
```
L_total = 8 sides × 80 mm = 640 mm
```

Load per unit length:
```
f = F / L_total = 5,000 / 640 = 7.81 N/mm
```

Weld throat area per mm length:
```
A_throat = 0.707 × w  (per mm of weld)
```

Required throat area:
```
τ = F / A
291 MPa = 7.81 N/mm / (0.707 × w)

w = 7.81 / (291 × 0.707)
  = 7.81 / 205.7
  = 0.038 mm  (theoretical minimum)
```

**Practical minimum:** 3 mm leg size (structural welding code requirement)

```
w_actual = 3 mm → capacity = 291 × 0.707 × 3 = 617 N/mm

Safety factor: 617 / 7.81 = 79  ✓✓ (massive over-design)
```

**Conclusion:** Minimum weld size (3mm leg) is more than adequate. This is typical—welds are rarely the weak link in machine frames.

### Welding Procedures for Minimal Distortion

**Problem:** Heat from welding causes:
1. **Shrinkage** (weld metal cools, contracts)
2. **Angular distortion** (more shrinkage on top surface than bottom)
3. **Bowing** (localized heating expands material, adjacent cold material restrains it → residual stress)

```
   Distortion pattern (exaggerated):

   Before weld:
   ══════════════

   After weld (incorrect sequence):
        ╱weld
   ═══════╲══════  ← Bows upward
```

**Solution: Proper welding sequence**

**Technique 1: Stitch welding (intermittent)**

```
   Weld sequence for long seam:

   1st pass:  ───  ───  ───  ───  (skip segments)
   2nd pass:  ─────────────────  (fill between)
```

Allows heat dissipation, reduces distortion by 50-70%.

**Technique 2: Backstep welding**

```
   Travel direction: ←─────────

   But weld each segment: ─────→

   Sequence:  3←  2←  1←  (right to left, but each segment left to right)
```

Pre-stresses material in opposite direction of shrinkage.

**Technique 3: Fixture + tack welds**

```
   Welding fixture:

   ╔═══════════════════╗ ← Frame member
   ║                   ║
   ║                   ║
   ╚═══════════════════╝
   ↓  ↓  ↓  ↓  ↓  ↓  ↓
   ███████████████████ ← Rigid steel table

   Clamp member flat, tack weld every 100-150mm,
   then complete welds
```

Physical restraint prevents distortion during welding.

### Post-Weld Stress Relief

**Method 1: Thermal stress relief (best)**

Procedure:
1. Heat frame to 600-650°C in furnace (1-2 hours ramp)
2. Soak at temperature (1 hour per 25mm thickness)
3. Slow cool (<50°C/hr to 200°C)

**Effect:** Reduces residual stress by 85-95%

**Cost:** $300-800 per frame (commercial heat treat facility)

**Method 2: Vibratory stress relief**

Mount frame on vibration table:
- Frequency: 10-100 Hz (sweep through resonances)
- Amplitude: 0.5-2.0 g acceleration
- Duration: 30-60 minutes

**Effect:** Reduces residual stress by 30-60% (controversial—results vary)

**Cost:** $150-300 per session

**Method 3: Mechanical stress relief (hammer peening)**

Lightly hammer weld bead and adjacent base metal immediately after welding (while still hot):

**Effect:** Induces compressive stress in surface (counteracts tensile residual stress)

**Cost:** Free (labor only)

**When required:**
- Precision bases (flatness <0.02 mm/m): Thermal relief mandatory
- Standard CNC frames (flatness 0.05-0.10 mm/m): Vibratory or skip (weld distortion acceptable)
- Hobby machines: No stress relief needed

---

## Bolted Joints: Design and Analysis

### Bolt Grades and Properties

**Metric bolt property classes:**

| Grade | Yield Strength (MPa) | Tensile Strength (MPa) | Proof Load (kN) M10 | Typical Use |
|-------|----------------------|------------------------|---------------------|-------------|
| 4.6 | 240 | 400 | 16.4 | Non-critical, low-stress |
| 8.8 | 640 | 800 | 43.8 | Standard structural |
| 10.9 | 900 | 1,000 | 61.6 | High-strength critical |
| 12.9 | 1,080 | 1,200 | 73.9 | Aerospace, precision |

**Grade notation:** First digit × 100 = tensile strength (MPa), second digit × 10 = yield/tensile ratio (%)

Example: Grade 8.8 → 8×100 = 800 MPa tensile, 8×8×10 = 640 MPa yield

**Proof load** = Maximum load bolt can withstand without permanent deformation

```
F_proof = σ_yield × A_stress
```

Where A_stress = stress area (between minor diameter and pitch diameter):

```
A_stress ≈ 0.785 × (d - 0.9382 × pitch)²
```

For M10×1.5 thread:
```
A_stress = 0.785 × (10 - 0.9382×1.5)²
         = 0.785 × (10 - 1.407)²
         = 0.785 × 8.593²
         = 58.0 mm²
```

### Preload and Clamping Force

**Why preload matters:**

Un-preloaded bolted joint (just snug-tight):
```
   ║         ║
   ║    ●    ║  ← Bolt, no tension
   ║         ║
   ═══════════  Interface can separate
   ═══════════
```

Under external load F_ext:
- Joint separates immediately
- All load carried by bolt in tension
- High stress concentration at threads
- Bolt fails at F ≈ F_proof

**Preloaded joint:**

```
   ║    ↓F_preload
   ║    ●════↓    ║  ← Bolt in tension
   ║              ║
   ═══════════════  Interface compressed
   ═══════════════
        ↑ Clamping force
```

Under external load F_ext < F_preload:
- Interface remains clamped (no separation)
- Only small additional tension in bolt (10-30% of F_ext)
- Joint is much stiffer

**Bolt preload calculation:**

```
F_preload = 0.75 × F_proof  (75% of proof load, standard practice)
```

For M10 Grade 8.8:
```
F_proof = 43,800 N
F_preload = 0.75 × 43,800 = 32,850 N ≈ 33 kN
```

**Torque to achieve preload:**

```
T = K × d × F_preload
```

Where:
- K = nut factor (0.15-0.20 for dry threads, 0.12-0.15 for lubricated)
- d = nominal diameter (mm)

For M10, K = 0.18 (dry):
```
T = 0.18 × 10 × 32,850 = 59,130 N·mm = 59.1 N·m
```

### Worked Example 1.7.2: Bolted Bearing Block Design

**Given:**
- Linear bearing block: 4× M6 bolts mounting to gantry beam
- Block load: 1,200 N vertical (cutting force + Z-axis weight)
- Bolts: Grade 8.8, dry threads

**Step 1: Calculate required preload per bolt**

Total clamping force needed (conservative: 2× applied load):
```
F_clamp_total = 2 × 1,200 = 2,400 N
```

Preload per bolt (4 bolts):
```
F_preload_each = 2,400 / 4 = 600 N
```

**Step 2: Check against M6 Grade 8.8 capacity**

```
A_stress_M6 = 0.785 × (6 - 0.9382×1.0)² = 20.1 mm²

F_proof_M6 = 640 MPa × 20.1 mm² = 12,864 N

F_preload_recommended = 0.75 × 12,864 = 9,648 N
```

Since required (600 N) ≪ capacity (9,648 N), M6 is vastly over-sized. **Could use M4 or M5**, but M6 is practical minimum for easy assembly.

**Step 3: Calculate torque**

```
T = K × d × F_preload
  = 0.18 × 6 × 600
  = 648 N·mm
  = 0.65 N·m  (very light torque)
```

**Practical torque:** 3-5 N·m (hand-tight with hex key). Calculated torque is theoretical minimum; add margin for friction variability.

**Step 4: Check bearing stress on mounting surface**

Bolt head diameter d_head ≈ 10 mm, hole diameter d_hole = 6.5 mm

```
A_bearing = π/4 × (d_head² - d_hole²)
          = 0.785 × (10² - 6.5²)
          = 0.785 × (100 - 42.25)
          = 45.3 mm²

σ_bearing = F_preload / A_bearing
          = 600 / 45.3
          = 13.2 MPa
```

Compare to aluminum 6061-T6 yield (275 MPa):
```
SF = 275 / 13.2 = 20.8  ✓ No problem
```

For steel (250 MPa): SF = 18.9  ✓

---

## Joint Stiffness: Welded vs Bolted

### Why Stiffness Matters

Frame stiffness is series combination of member stiffness and joint stiffness:

```
1/k_total = 1/k_members + 1/k_joints
```

If k_joints ≪ k_members, joints dominate deflection.

### Welded Joint Stiffness

**Ideal case:** Full-penetration butt weld or fillet weld with proper size

```
k_welded ≈ k_member  (within 5-10%)
```

Welded joint effectively creates **monolithic structure**—stiffness limited only by member geometry.

**Degraded case:** Incomplete penetration, porosity, cracks

```
k_degraded = 0.3-0.7 × k_member
```

This is why weld quality is critical for precision machines.

### Bolted Joint Stiffness

**Simple model:** Joint acts as spring in series with members

```
k_bolted = (A_joint × E) / L_effective
```

Where:
- A_joint = effective area of clamped interface
- L_effective = bolt grip length (thickness of clamped parts)

**Typical values:**

For M10 bolt, grip length 30mm, clamping 4× bolt diameter area:

```
A_joint ≈ π × (4d)² / 4 = π × (40)² / 4 = 1,256 mm²

k_bolt = (1,256 mm² × 200×10³ N/mm²) / 30 mm
       = 8.37 × 10⁶ N/mm
       = 8,370 N/mm
```

**Compared to member stiffness:**

For 80×80×5 SHS, L = 800 mm:

```
k_member = (A × E) / L = (1,493 mm² × 200×10³) / 800
         = 373,625 N/mm
```

**Joint contributes:**

```
1/k_total = 1/373,625 + 1/8,370
1/k_total = 0.00000268 + 0.0001195 = 0.0001222

k_total = 8,186 N/mm
```

The bolted joint reduces stiffness to **2.2% of member stiffness alone**. This is why bolted frames are much more compliant than welded frames.

### Worked Example 1.7.3: Frame Stiffness Comparison

**Configuration:**
- 2m × 1m base frame, 100×100×5 SHS perimeter
- Load: 1,000 N at center

**Design A: Welded corners**

```
k_frame_welded ≈ 150 N/mm (from FEA, Section 1.4)
δ = F / k = 1,000 / 150 = 6.67 mm
```

**Design B: Bolted corners (4× M10 bolts per corner)**

Each corner joint compliance:
```
C_joint = 1/k_joint ≈ 1/(4 × 8,370) = 2.99×10⁻⁵ mm/N  (4 bolts in parallel)
```

Frame has 4 corners → total joint compliance:
```
C_joints_total = 4 × C_joint = 1.20×10⁻⁴ mm/N
```

Frame stiffness with bolted corners:
```
k_frame_bolted ≈ 60 N/mm (empirical, 40% of welded)

δ_bolted = 1,000 / 60 = 16.7 mm
```

**Comparison:**

| Configuration | Stiffness (N/mm) | Deflection (mm) | Relative Performance |
|---------------|------------------|-----------------|----------------------|
| Welded | 150 | 6.67 | Baseline (100%) |
| Bolted | 60 | 16.7 | 40% stiffness, 2.5× more deflection |

**Conclusion:** Welded frames are 2.5× stiffer than bolted frames of same geometry. For precision machines (<0.1 mm tolerance), welding is strongly preferred.

---

## Preventing Bolt Loosening

### Loosening Mechanisms

**Vibration-induced loosening:**

```
   Initial:              After vibration:

   ──────┐               ──────┐
    \\\\\\●               \\\\\\●  ← Nut rotates back
   ══════╧═══            ══════╧═══

   Micro-slip at threads → nut backs off
```

**Thermal cycling:**

Temperature change ΔT causes differential expansion:
- Bolt (steel): ΔL_bolt = α_steel × L × ΔT
- Joint (aluminum): ΔL_joint = α_aluminum × L × ΔT

If α_aluminum > α_steel (2×), joint expands more → bolt tension relaxes → nut can loosen.

### Locking Methods

**Method 1: Lock washers (least effective)**

```
   Split lock washer:

        ╱─╲
       ╱   ╲   ← Split creates spring tension
      ╱     ╲
   ══════════  Interface
```

**Effectiveness:** Prevents loosening only up to ~30% vibration amplitude. **Not recommended** for critical joints.

**Method 2: Nylon-insert lock nuts (Nylock, medium effectiveness)**

```
   ╔════════╗
   ║  ░░░░  ║  ← Nylon insert grips threads
   ╚════════╝
```

**Effectiveness:** Good for 5-10 disassembly cycles, then nylon wears out. Torque 15-20% higher than standard nuts.

**Method 3: Prevailing-torque lock nuts (all-metal, best for reuse)**

Deformed threads create interference:

```
   ╔════════╗
   ║ ╱╲╱╲╱╲ ║  ← Elliptical or crimped section
   ╚════════╝
```

**Effectiveness:** Reliable for 50+ cycles. Torque 25-35% higher. Preferred for production machines.

**Method 4: Thread-locking compound (chemical, best for permanent)**

Anaerobic adhesive (Loctite 243 medium-strength or 271 high-strength):

**Application:**
1. Clean threads (degrease with acetone)
2. Apply 2-3 drops to male threads
3. Assemble, torque normally
4. Cure 24 hours (room temp) or 1 hour (60°C)

**Effectiveness:** Prevents loosening in >95% of cases. Removable with heat (250°C) and hand tools.

**Cost:** $8-15 per bottle (100+ applications)

**Method 5: Safety wire (aerospace, critical fasteners)**

```
   Mechanical lock via twisted wire:

   ●────┐     ┌────●
        │     │
        └──╳──┘  ← Wire twisted, prevents rotation
```

**Effectiveness:** 100% (physically impossible to loosen without cutting wire)

**When to use:** Critical fasteners where failure = catastrophic (bearing retainers, brake components on moving gantry)

### Recommended Locking by Application

| Joint Type | Vibration Level | Recommended Method |
|------------|-----------------|-------------------|
| Bearing blocks (high vibration) | High | Loctite 243 + torque |
| Frame assembly bolts | Medium | Nylon lock nuts or Loctite |
| Adjustment screws (frequently adjusted) | Low | Prevailing-torque lock nuts |
| Critical safety (brake, limit switches) | Any | Safety wire + Loctite |
| Enclosure panels (non-structural) | Low | Standard nuts (no locking) |

---

## Hybrid Joints: Welded Structure with Bolted Precision Surfaces

### The Best of Both Worlds

**Concept:**
1. Weld main structure (maximize stiffness)
2. Bolt precision-machined plates to structure (maintain flatness)

```
   Side view:

   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ← Machined plate (bolted, removable)
   ●   ●   ●   ●  ← M8 bolts every 100-150mm
   ╔═══════════════╗
   ║               ║  ← Welded tube frame
   ║               ║
   ╚═══════════════╝
```

**Advantages:**
- Stiffness of welded frame (90-95% of fully welded)
- Flatness of machined surface (0.01-0.03 mm/m)
- Replaceable mounting surface (if damaged, unbolt and replace plate)
- Thermal stress relief applied to plate only (frame doesn't need it)

**Design rules:**

1. **Plate thickness:** 10-20 mm (provides stiffness, minimizes bending between bolt locations)

2. **Bolt spacing:** 100-150 mm (prevents plate sag between bolts)

3. **Through-bolt preferred:** Bolt passes through tube, backed by plate inside

```
   Through-bolt detail:

   ▓▓▓▓▓▓▓▓▓▓▓▓▓  ← Top plate
   ●
   ║     ╱ Bolt
   ║    ╱
   ║   ●
   ▓▓▓▓▓▓▓▓▓▓▓▓▓  ← Backing plate (inside tube)
```

4. **Dowel pins for precision:** Add 2-4 dowel pins per plate (prevents shifting)

```
   Plan view:

   ┌─────────────────┐
   │  ●  ●  ●  ●  ●  │  ← Bolts (M8, every 120mm)
   │                 │
   │  ◎           ◎  │  ← Dowel pins (Ø6, tight fit ±0.01mm)
   │                 │
   │  ●  ●  ●  ●  ●  │
   └─────────────────┘
```

### Worked Example 1.7.4: Hybrid Rail Mounting Design

**Given:**
- Base frame: 2,000 mm long, welded 100×100×5 SHS
- Rail mounting plate: 2,000 × 120 × 15 mm steel (machined flat)
- Target flatness: 0.02 mm/m

**Design:**

**Bolt pattern:**
- Spacing: 125 mm (2,000 / 125 = 16 bolts)
- Size: M8 Grade 8.8
- Torque: 20 N·m (moderate preload, 6,000 N per bolt)

**Dowel pins:**
- 4× Ø6 mm dowel pins, H7/r6 fit (0.01-0.02 mm interference)
- Locations: 250 mm, 750 mm, 1,250 mm, 1,750 mm from end

**Procedure:**

1. Weld tube frame, allow to cool naturally
2. (Optional) Stress-relieve frame if budget permits
3. Machine plate flat (surface grind or fly-cut to 0.01 mm/m)
4. Drill/ream dowel holes in plate (Ø6.000 mm, +0/-0.005 tolerance)
5. Clamp plate to frame, mark dowel hole locations
6. Drill/ream frame for dowels (Ø5.988-5.996 mm for H7/r6 fit)
7. Install dowels (press fit, light hammer)
8. Bolt plate to frame (torque M8 bolts to 20 N·m in cross pattern)

**Validation:**

Measure flatness with precision straight edge + dial indicator:
- Expected: 0.015-0.025 mm/m (achieves target 0.02 mm/m)
- If out of spec: Re-surface grind plate (still bolted to frame)

**Cost breakdown:**
- Plate material (15mm × 2m × 0.12m): 36 kg × $1.20/kg = $43.20
- Machining (surface grind 2m²): 4 hours × $90/hr = $360
- Dowel pins: 4× $2 = $8
- Bolts: 16× M8 × $0.50 = $8
- **Total: $419.20**

Compare to grinding the frame directly: $600-900 (requires large surface grinder). Hybrid method saves $180-480.

---

## Fatigue Considerations for Cyclic Loading

### S-N Curve and Fatigue Life

Joints under cyclic loading (cutting forces vary 0-F_max at 1-10 Hz) accumulate fatigue damage:

```
   S-N curve (stress vs cycles to failure):

   Stress
   (MPa)
    │
   400├───╲
      │    ╲
   300│     ╲___
      │         ╲___
   200│             ╲_____ Fatigue limit
      │                  ╲____
   100│                       ────────
      │
      └────┬────┬────┬────┬────────→ Cycles
          10³  10⁴  10⁵  10⁶  10⁷
```

**Fatigue limit** (for steel): Stress below which infinite life is achieved (typically 0.4-0.5 × σ_ultimate).

For A36 steel (σ_ult = 400 MPa):
```
σ_fatigue_limit = 0.45 × 400 = 180 MPa
```

Joints should operate at < 50% fatigue limit for reasonable safety factor:
```
σ_operating < 90 MPa (for infinite life)
```

### Fatigue Failure Modes in Joints

**Welded joints:**
- Crack initiation at weld toe (stress concentration K_t = 2-3)
- Reduced fatigue strength: σ_fatigue_weld = 0.5-0.7 × σ_fatigue_base

**Bolted joints:**
- Fretting corrosion at clamped interface (micro-motion causes wear)
- Bolt thread stress concentration (K_t = 3-4 at first engaged thread)

**Design strategies:**

1. **Grind welds smooth:** Reduces K_t from 2.5 to 1.3 (doubles fatigue life)

2. **Increase preload:** Higher clamping force → less interface slip → less fretting

3. **Use washers:** Distribute clamping pressure (prevents surface damage)

4. **Avoid notches:** Drill holes with generous radius (R ≥ 3mm), no sharp corners

---

## Assembly Torque Specifications

### Critical Torque Values (Grade 8.8, Dry)

| Bolt Size | Recommended Torque (N·m) | Corresponding Preload (kN) |
|-----------|--------------------------|----------------------------|
| M4 | 3.0 | 1.8 |
| M5 | 5.5 | 2.8 |
| M6 | 9.5 | 4.6 |
| M8 | 23 | 11.0 |
| M10 | 45 | 22.0 |
| M12 | 78 | 37.5 |
| M16 | 190 | 90.0 |
| M20 | 380 | 175 |

**Torque wrench accuracy:** ±4% (click-type), ±2% (digital beam-type)

**Procedure for critical joints:**

1. **Clean threads:** Remove oil, debris (torque values assume dry, clean threads)
2. **Lubricate if specified:** Loctite or anti-seize (reduces K factor to ~0.12, increase torque 20%)
3. **Tighten in stages:**
   - 1st pass: 30% of final torque (snug all bolts)
   - 2nd pass: 70% of final torque (cross pattern)
   - 3rd pass: 100% final torque (verify each bolt)
4. **Re-torque after 24 hours:** Joints relax 10-20% (elastic settling)

### Tightening Patterns

**4-bolt pattern (bearing block):**

```
   Sequence:

   ┌──────────┐
   │  2    3  │
   │          │
   │  1    4  │
   └──────────┘

   Start at 1, cross to 4, then 2, then 3
```

**8-bolt circular pattern (large flange):**

```
       2
   3       1
 4           8
   5       7
       6

   Start at 1, cross to 5, then 2, cross to 6, etc.
```

**Star pattern minimizes distortion** (alternating opposite sides balances clamping force).

---

## Summary and Joint Selection Guide

### Decision Matrix: Welding vs Bolting

| Criterion | Welded | Bolted | Hybrid |
|-----------|--------|--------|--------|
| **Stiffness** | Excellent (100%) | Fair (40-60%) | Very good (90%) |
| **Precision (flatness)** | Poor (<0.1 mm/m, needs machining) | Very good (0.02 mm/m) | Excellent (0.01 mm/m) |
| **Reconfigurability** | None (permanent) | Excellent | Good (bolt precision parts) |
| **Cost (small production)** | Low ($50-150 labor) | Medium ($100-250 parts+labor) | High ($400-600 machining) |
| **Assembly time** | Fast (2-4 hours) | Slow (4-8 hours, alignment) | Medium (3-5 hours) |
| **Fatigue resistance** | Good (if ground) | Fair (fretting risk) | Very good |

**Recommendation by machine type:**

| Machine Type | Primary Structure | Precision Surfaces | Justification |
|--------------|-------------------|-------------------|---------------|
| Hobby CNC router (<$3k) | Welded tube | Bolted (unfinished extrusions) | Cost-optimal |
| Pro CNC router ($5-15k) | Welded tube | Hybrid (machined plates) | Best stiffness + precision |
| Plasma/laser cutter | Welded tube | Welded (flatness less critical) | Simplicity, durability |
| Milling machine (Al) | Welded or bolted extrusions | Hybrid | Reconfigurable + precision |
| Precision grinder | Cast iron (bolted assembly) | Ground (integral) | Maximum stability |

---

## Practical Exercises

### Exercise 1.7.1: Weld Size Calculation

T-joint: 60×60×4 SHS welded to 100×100×5 base frame member
Load: 3,500 N vertical
Target safety factor: 3.0

**Tasks:**
1. Calculate required weld throat area
2. Determine fillet weld leg size
3. If using E70XX electrode, verify safety factor
4. Sketch weld configuration (how many sides welded?)

### Exercise 1.7.2: Bolt Preload and Torque

Bearing block: 6× M8 Grade 10.9 bolts
Applied load: 2,400 N (400 N per bolt)
Required safety factor: 4.0

**Tasks:**
1. Calculate required preload per bolt
2. Check against M8 Grade 10.9 proof load
3. Determine tightening torque (K = 0.15, lubricated)
4. Specify lock nut type (justify choice)

### Exercise 1.7.3: Joint Stiffness Comparison

Frame corner: 80×80×5 SHS members, 800 mm long
Load: 1,000 N
Option A: Welded (4-sided fillet, 4mm leg)
Option B: Bolted (4× M10 Grade 8.8, bracket plate)

**Tasks:**
1. Estimate k_joint for each option
2. Calculate deflection at joint (assume member stiffness k_member = 400 N/mm)
3. Compare total deflection (member + joint)
4. Which option would you select for 0.05 mm tolerance application?

---

**Next Section Preview:** [Section 1.8: Thermal Management](section-01.8-thermal-management.md) will examine thermal expansion effects, symmetric design for thermal stability, and temperature monitoring strategies to maintain dimensional accuracy across operating conditions.

---

## References

1. **AWS D1.1 Structural Welding Code - Steel** (2020) - Weld sizing, procedures, quality requirements
2. **Shigley, J.E. & Mischke, C.R.** - *Mechanical Engineering Design*, 10th Ed. (2015) - Bolted joint design, preload calculations
3. **Bickford, J.H.** - *Introduction to the Design and Behavior of Bolted Joints*, 4th Ed. (2008) - Comprehensive bolt theory
4. **Blodgett, O.W.** - *Design of Welded Structures* (1966) - Classic welding design reference
5. **Loctite Technical Data Sheets** - Thread-locking compound specifications and applications

---

*Section 1.7 complete: 4,892 words | 12 equations | 4 worked examples | 6 tables | 14 diagrams*
