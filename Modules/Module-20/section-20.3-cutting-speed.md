# 20.3 Cutting Speed and Spindle RPM Calculations

## Understanding Cutting Speed

**Cutting Speed (V)**: The velocity at which the cutting edge moves through material
- Imperial: Surface Feet per Minute (SFM)
- Metric: Meters per Minute (m/min)

**Spindle Speed (N)**: The rotational speed in RPM

**Why this matters**: Cutting speed determines tool wear and temperature. Same cutting speed = similar tool conditions regardless of tool size.

## RPM Calculation Formulas

### Imperial System

$$N = \frac{12 \times V}{\pi \times D} = \frac{3.82 \times V}{D}$$

**Quick approximation**: $N \approx \frac{4 \times V}{D}$

**Examples**:
- Aluminum 600 SFM, 1/2" endmill: N = 3.82 × 600 / 0.5 = 4584 RPM
- Steel 300 SFM, 2" face mill: N = 3.82 × 300 / 2.0 = 573 RPM

### Metric System

$$N = \frac{1000 \times V}{\pi \times D} = \frac{318.3 \times V}{D}$$

**Example**: Aluminum 200 m/min, 12mm endmill: N = 318.3 × 200 / 12 = 5305 RPM

### Reverse Calculation (RPM → SFM)

$$V = \frac{N \times D}{3.82} \text{ (Imperial)}$$

$$V = \frac{N \times D}{318.3} \text{ (Metric)}$$

## Recommended Cutting Speeds

### Ferrous Metals

| Material | HSS | Uncoated Carbide | Coated Carbide |
|----------|-----|------------------|----------------|
| Mild Steel 1018 | 90-120 | 250-350 | 350-500 |
| Alloy Steel 4140 | 50-80 | 150-250 | 250-400 |
| Stainless 304 | 40-60 | 100-150 | 150-250 |
| Tool Steel (annealed) | 40-60 | 100-150 | 150-250 |
| Tool Steel (hardened) | - | 50-150 | CBN: 200-400 |
| Cast Iron (gray) | 60-100 | 300-500 | Ceramic: 1000-2500 |

### Non-Ferrous Metals

| Material | HSS | Carbide | PCD |
|----------|-----|---------|-----|
| Aluminum 6061 | 200-400 | 600-1200 | 1500-4000 |
| Brass | 200-300 | 400-800 | - |
| Bronze | 90-150 | 300-600 | - |
| Copper | 100-150 | 300-500 | - |

### Exotic Alloys

| Material | Carbide | Ceramic/CBN |
|----------|---------|-------------|
| Titanium Ti-6Al-4V | 150-250 | - |
| Inconel 718 | 50-120 | 200-600 |
| Hastelloy | 40-80 | - |

### Non-Metals

| Material | Cutting Speed (SFM) |
|----------|---------------------|
| Plastics (acrylic, nylon) | 300-1200 |
| Carbon Fiber/Composites | 400-1500 (PCD recommended) |
| Wood | 300-1200 |
| Foam (tooling board) | 800-1500 |

## Operation-Specific Calculations

### Turning with Constant Surface Speed (CSS)

**Problem**: As diameter decreases, cutting speed drops if RPM stays constant.

**Solution**: Use CSS mode
```gcode
G96 S350 M3    (CSS mode, 350 SFM)
G50 S2000      (Max RPM limit)
```

Controller automatically adjusts: N = 3.82 × V / D_current

**Example**:
- At 2.0" diameter: 669 RPM
- At 1.5" diameter: 892 RPM (auto-adjusted)
- At 1.0" diameter: 1337 RPM (auto-adjusted)

### Drilling

Use drill diameter, but reduce RPM 25-50% for deep holes (>3× diameter) to improve chip evacuation.

**Example**: 1/4" drill, aluminum, 2" deep hole
- Standard: 300 SFM → 4584 RPM
- Deep hole: 2500 RPM (reduced for chip clearance)

### Reaming

Reduce cutting speed 50% compared to drilling (more flutes, finishing operation).

### Tapping

Not based on cutting speed optimization. Use:
$$N = \frac{F}{TPI}$$ or $$N = \frac{F}{P}$$ (metric)

## Adjusting Cutting Speeds

### Reduce Speed When:
- Tool material limited (HSS = 50% of carbide speeds)
- Machine lacks rigidity (reduce 20-30%)
- Small/long tools prone to deflection (reduce 20-50%)
- Interrupted cuts (reduce 10-30%)
- No coolant on steel (reduce 20-40%)

### Increase Speed When:
- High-speed machining with light engagement (increase 50-100%)
- Excellent fixturing and rigidity (increase 10-20%)
- Flood coolant available (increase 10-20%)
- Coated tools (increase 30-50% over uncoated)

## Spindle Limitations

### Typical RPM Ranges
- Manual mills: 60-4,000 RPM
- Hobby CNC: 1,000-10,000 RPM
- VMC (40-taper): 8,000-15,000 RPM
- VMC (30-taper): 12,000-20,000 RPM
- High-speed spindle: 24,000-60,000+ RPM

### Power vs Torque
- **Low RPM**: Torque-limited (heavy cuts possible)
- **High RPM**: Power-limited (light cuts only)

Formula: $T = \frac{P \times 5252}{N}$ (lb-ft, hp, RPM)

## Troubleshooting

**Tool burning/smoking**: Reduce RPM 25-40%, increase feed rate, check tool sharpness

**Poor surface finish**: Increase RPM 20-30% (aluminum/steel), check for tool wear

**Chatter**: Change RPM ±10-20% to shift away from resonance frequency

**Tool breakage**: Check feed rate first, reduce DOC if at low RPM (torque-limited)

## Summary

**Key principles**:
1. Use formula: N = 3.82 × V / D (Imperial) or N = 318.3 × V / D (Metric)
2. Select cutting speed based on material and tool material
3. Adjust for machine rigidity, tool size, and application
4. Always use CSS for turning operations
5. Check spindle limits (min/max RPM, power curve)

---

**Next**: [20.4 Feed Rate Optimization](section-20.4-feed-rate.md)
