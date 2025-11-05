# 19.12 Troubleshooting and Optimization

## Systematic Troubleshooting Approach

**Effective Troubleshooting Requires**:
1. **Observation**: What exactly is the problem? When does it occur?
2. **Hypothesis**: What could cause this behavior?
3. **Testing**: Change one variable, observe result
4. **Verification**: Confirm root cause, not just symptom
5. **Documentation**: Record findings for future reference

**Golden Rule**: **Change only one thing at a time.**

## Common Problems and Solutions

### Problem 1: Oscillation (Instability)

**Symptoms**:
- Axis shakes or vibrates
- Audible buzzing or whining
- Visible oscillation in position plot
- May occur at rest or during motion

**Observation Checklist**:
- Frequency of oscillation? (low ~1-5 Hz, mid ~10-50 Hz, high >100 Hz)
- Occurs at rest, during motion, or both?
- All axes or specific axis?
- Consistent or intermittent?

#### Root Cause 1: Gains Too High

**Test**:
- Reduce P gain by 30-50%
- If oscillation stops: Gains too high

**Solution**:
- Reduce P gain to 70-80% of oscillation threshold
- Add D gain to increase damping
- Re-test for stability

**Example**:
- P = 150: Oscillation at 15 Hz
- Reduce to P = 100: Stable
- Add D = 10: Can increase P to 120 while maintaining stability
- **Final**: P = 120, D = 10

#### Root Cause 2: Mechanical Resonance

**Test**:
- Tap axis with hammer, observe ring-down
- Use accelerometer + FFT (if available)
- Increase gains slowly - oscillation appears at specific P value

**Identify Resonance**:
- Tap test shows ring-down at ~200 Hz
- As P increases, oscillation appears at 200 Hz
- **Conclusion**: Exciting mechanical resonance

**Solution**:
- **Option 1**: Add notch filter at resonance frequency
  - LinuxCNC: `loadrt notch`, set freq = 200 Hz
  - Eliminates resonance from control loop
- **Option 2**: Mechanical damping
  - Add foam, rubber mounts, constrained-layer damping
  - Reduces resonance amplitude
- **Option 3**: Lower gains
  - Avoid exciting resonance (accept slower response)

**Notch Filter Configuration** (LinuxCNC):
```hal
loadrt notch names=notch.x
setp notch.x.freq 200
setp notch.x.q 5.0
addf notch.x servo-thread
net x-pid-out pid.x.output => notch.x.in
net xoutput notch.x.out => pwmgen.0.value
```

#### Root Cause 3: Encoder Noise

**Test**:
- Observe encoder position with axis stationary
- If position jitters (±several counts): Noise problem

**Sources**:
- Electrical interference (motor cables near encoder cables)
- Poor shielding
- Grounding issues
- Encoder resolution too coarse for application

**Solution**:
- **Shielding**: Use shielded twisted-pair cables for encoders
- **Separation**: Route encoder cables away from motor power cables (6" minimum)
- **Grounding**: Ground shield at one end only (prevent ground loops)
- **Filtering**: Add low-pass filter to encoder signals (hardware or software)
- **Encoder upgrade**: Higher resolution encoder (reduces quantization noise)

**Software Filter** (LinuxCNC):
```hal
loadrt lowpass names=lowpass.x-pos
setp lowpass.x-pos.gain 1.0
setp lowpass.x-pos.time-constant 0.001  # 1 ms filter
addf lowpass.x-pos servo-thread
net x-pos-raw encoder.0.position => lowpass.x-pos.in
net x-pos-filt lowpass.x-pos.out => pid.x.feedback
```

#### Root Cause 4: Loose Coupling or Bearing

**Test**:
- Manually move axis (motors disabled)
- Feel for play, looseness, binding
- Check coupling screws, bearing preload

**Solution**:
- Tighten coupling set screws
- Adjust bearing preload
- Replace worn components

### Problem 2: Following Error Alarm

**Symptoms**:
- Controller stops with "Following Error" alarm
- Error message: "Joint X following error exceeded limit"
- Occurs during rapid moves or cutting

**Observation**:
- When does it occur? (rapids, heavy cuts, specific moves?)
- Following error magnitude at fault?
- Consistent location or random?

#### Root Cause 1: P Gain Too Low

**Test**:
- Observe following error during motion (before alarm)
- If error consistently approaches limit: Insufficient gain

**Solution**:
- Increase P gain by 25-50%
- Verify stability (no oscillation)
- Increase following error limit if necessary (temporary)

**Example**:
- Following error limit: 0.050"
- Actual error during rapids: 0.045" (close to limit)
- Increase P from 80 to 120
- New following error: 0.020" (safe margin)

#### Root Cause 2: No Velocity Feedforward

**Test**:
- Observe following error during constant velocity motion
- Large error during cruise phase: Missing feedforward

**Solution**:
- Add velocity feedforward (FF1)
- Start with FF1 = 0.9, increase to 1.0
- Following error should reduce 5-10×

**Example**:
- Without FF1: Following error = 0.008" during 200 IPM motion
- With FF1 = 0.95: Following error = 0.0008"
- **10× improvement**

#### Root Cause 3: Mechanical Obstruction

**Test**:
- Following error occurs at specific location
- Axis physically encounters resistance

**Check**:
- Binding (misaligned bearings, rails)
- Crash damage
- Chips/debris in ways
- Insufficient lubrication

**Solution**:
- Inspect mechanical system
- Clean ways, screws
- Realign components
- Lubricate

#### Root Cause 4: Motor Undersized

**Test**:
- Following error increases under load (cutting forces)
- Motor reaches torque limit

**Calculation**:
$$\text{Required Torque} = (\text{Inertia} \times \text{Accel}) + \text{Friction} + \text{Load}$$

**Example**:
- Max acceleration: 200 in/s²
- Axis inertia (reflected): 0.01 kg·m²
- Required torque: 0.01 × (200 × 0.0254) = 0.051 N·m + friction + load
- If motor continuous torque < required: Undersized

**Solution**:
- Upgrade to higher torque motor
- Reduce acceleration (temporary)
- Reduce cutting forces (slower feedrate, lighter DOC)

### Problem 3: Poor Surface Finish

**Symptoms**:
- Visible vibration marks (chatter)
- Ripples or waves in surface
- Inconsistent finish

**Observation**:
- Pattern regular or random?
- Occurs on all surfaces or specific directions?
- Frequency of pattern? (measure wavelength)

#### Root Cause 1: Mechanical Vibration

**Test**:
- Accelerometer on spindle or toolholder
- Measure vibration frequency
- Match to surface finish wavelength

**Calculation**:
$$\text{Wavelength} = \frac{\text{Feedrate}}{\text{Vibration Frequency}}$$

**Example**:
- Feedrate: 100 IPM = 1.67 in/s
- Measured wavelength: 0.010"
- Vibration frequency: 1.67 / 0.010 = 167 Hz

**Solution**:
- Identify vibration source (spindle imbalance, tool runout, resonance)
- Add damping or stiffness
- Adjust spindle speed (avoid resonant frequencies)
- Use different feeds/speeds to shift frequency

#### Root Cause 2: Servo Tuning Issues

**Test**:
- Run circular interpolation test (perfect circle G-code)
- Measure actual path deviation (contouring error)
- Large error (>0.005"): Tuning problem

**Typical Issues**:
- Following error during motion
- Axis response mismatch (X fast, Y slow → oval circles)
- Inadequate feedforward

**Solution**:
- Balance servo response (match bandwidth of all axes)
- Increase P gain (reduce following error)
- Add velocity and acceleration feedforward
- Verify circular path within tolerance

#### Root Cause 3: Excessive Corner Blending

**Test**:
- Measure corner radius vs. programmed
- Large radius (>tolerance): Excessive blending

**G-Code Check**:
```gcode
G64 P0.020  ; Tolerance too loose for finishing
```

**Solution**:
- Reduce blend tolerance for finishing passes
```gcode
G64 P0.002  ; Tighter tolerance
```
- Trade-off: Longer cycle time, better finish
- Use G61 (exact stop) for critical corners

### Problem 4: Inconsistent Positioning

**Symptoms**:
- Parts dimensionally inconsistent
- Position varies between runs
- Hysteresis (different position depending on approach direction)

**Observation**:
- Repeatability test: Move to position 10×, measure variation
- Unidirectional vs. bidirectional error

#### Root Cause 1: Backlash

**Test**:
- Move axis +1", then -1", measure actual position
- If position offset = backlash amount

**Measurement**:
- Mount dial indicator on spindle
- Touch off on fixed surface
- Move +0.5", return to zero: read indicator
- Difference = backlash

**Solution**:
- **Mechanical**: Anti-backlash nut, preload
  - Replace worn ballscrew nut
  - Adjust preload (eliminate play)
- **Software compensation** (temporary):
  - LinuxCNC: Set backlash parameter
  - Mach4: Set backlash compensation
  - Limitations: Only compensates slow moves

**LinuxCNC Backlash Compensation**:
```ini
[AXIS_X]
BACKLASH = 0.002  ; 0.002" backlash compensation
```

**Better Solution**: Eliminate backlash mechanically (more accurate).

#### Root Cause 2: Thermal Expansion

**Test**:
- Measure position when cold, after warm-up (30-60 min)
- Position shift indicates thermal growth

**Typical Expansion**:
- Aluminum: 13 µm/m/°C (13 ppm/°C)
- Steel: 11 µm/m/°C
- Example: 1 meter (40") aluminum, 10°C rise → 130 µm (0.005") growth

**Solution**:
- Allow warm-up before precision work
- Temperature-controlled environment
- Thermal compensation (measure, correct in software)
- Use low-expansion materials (granite, carbon fiber, Invar)

#### Root Cause 3: Missed Steps (Steppers)

**Test** (stepper systems):
- Command large move (e.g., 10")
- Measure actual distance
- If short: Missed steps

**Causes**:
- Motor undersized (insufficient torque)
- Acceleration too high (resonance)
- Mechanical binding

**Solution**:
- Reduce acceleration (avoid resonance)
- Increase motor current (if within rating)
- Upgrade to larger motor
- **Best**: Convert to closed-loop (servos detect/correct errors)

### Problem 5: Noise and Jitter

**Symptoms**:
- High-frequency jitter in motion
- Audible whine from motors
- "Nervous" behavior

**Observation**:
- Frequency of jitter? (low hum vs. high whine)
- Occurs at rest, during motion, or both?

#### Root Cause 1: Derivative Gain Too High

**Test**:
- Reduce D gain by 50%
- If jitter reduces: Derivative amplifying noise

**Solution**:
- Reduce D gain to acceptable level
- Add low-pass filter to derivative term
- Improve encoder resolution (reduce quantization noise)

#### Root Cause 2: Quantization Noise (Coarse Encoder)

**Calculation**:
$$\text{Resolution} = \frac{\text{Screw Pitch}}{\text{Encoder CPR} \times 4}$$

**Example**:
- Encoder: 500 CPR → 2000 counts/rev (4× quadrature)
- Screw pitch: 0.2 in/rev
- Resolution: 0.2 / 2000 = 0.0001" per count

If D gain high, ±1 count jitter → large velocity estimate change → jittery motor command.

**Solution**:
- Upgrade encoder (2000 CPR → 10,000 CPR: 5× better resolution)
- Filter encoder signal (software low-pass)
- Reduce D gain

#### Root Cause 3: Ground Loops

**Test**:
- Disconnect encoder shield ground at one end
- If noise reduces: Ground loop problem

**Ground Loop**:
- Shield grounded at both ends
- Current flows through shield (creates magnetic field)
- Couples noise into signal wires

**Solution**:
- Ground shield at drive/controller end only (not motor end)
- Use isolated encoder power supply
- Check for multiple ground paths (eliminate)

## Performance Optimization

### Maximizing Cycle Time Reduction

**Goal**: Minimize total machining time while maintaining quality.

**Strategies**:

**1. Optimize Trajectory Planning**:
- Use blending mode (G64) instead of exact stop (G61)
- Set appropriate tolerance (G64 P0.005 typical)
- Look-ahead buffer size: 100-200 blocks

**2. Increase Velocities and Accelerations** (if mechanically sound):
- Gradually increase max velocity (test for vibration, accuracy)
- Increase acceleration (test for following error, overshoot)
- Typical gains: 20-50% improvement before reaching limits

**3. Add Feedforward Control**:
- Velocity feedforward (FF1): Reduces following error 5-10×
- Acceleration feedforward (FF2): Reduces transient errors
- Allows faster motion with same accuracy

**4. CAM Optimization**:
- Larger line segment tolerance (fewer short segments)
- Avoid unnecessary Z retracts
- Optimize tool paths (minimize rapid moves)
- Trochoidal milling (constant engagement, higher feedrates)

**5. Adaptive Feed**:
- Monitor spindle load (current or RPM drop)
- Reduce feedrate if load high (prevent tool breakage)
- Increase feedrate if load low (maximize metal removal rate)

### Improving Contouring Accuracy

**Goal**: Minimize path deviation during multi-axis motion.

**Strategies**:

**1. Match Axis Response**:
- Tune all axes to similar bandwidth (20-50 Hz typical)
- Use circular interpolation test to verify
- Adjust gains to eliminate oval circles

**2. Increase Control Loop Rate**:
- LinuxCNC: 1-2 kHz typical (limited by PC real-time performance)
- Mach4 + external controller: 5-20 kHz (depends on controller)
- Higher loop rate → better tracking → lower contouring error

**3. Mechanical Improvements**:
- Increase stiffness (bigger rails, thicker frame)
- Reduce moving mass (lighter gantry, aluminum vs. steel)
- Better bearings (preloaded, higher stiffness)

**4. Use Linear Encoders** (glass scales):
- Eliminate ballscrew pitch errors
- Directly measure position
- Typical improvement: 0.0005" → 0.0001" accuracy

### Noise Reduction

**Goal**: Quiet operation, reduce vibration.

**Strategies**:

**1. Mechanical Damping**:
- Foam padding under machine base
- Constrained-layer damping (metal-rubber-metal sandwich)
- Tuned mass dampers for specific resonances

**2. S-Curve Profiles** (jerk-limited):
- Replace trapezoidal with S-curve
- Smoother acceleration transitions
- Reduces excitation of mechanical resonances

**3. Notch Filters**:
- Identify resonance frequencies (tap test, frequency sweep)
- Add notch filter at each resonance
- Allows higher gains without exciting resonances

**4. Quiet Motor Drives**:
- Higher PWM frequency (20-40 kHz, inaudible)
- Sinusoidal commutation (smoother than trapezoidal)
- Current control tuning (reduce current ripple)

## Benchmarking and Validation

### Performance Metrics

**1. Positioning Accuracy**:
- Measure: Laser interferometer, length standards
- Typical: ±0.001-0.005" (hobbyist), ±0.0002-0.001" (industrial)

**2. Repeatability**:
- Measure: Return to same position 10×, record variation
- Typical: ±0.0001-0.0005" (hobbyist), ±0.00005-0.0002" (industrial)

**3. Contouring Accuracy**:
- Measure: Circular interpolation test, compare actual vs. nominal radius
- Typical: ±0.002-0.005" (hobbyist), ±0.0005-0.002" (industrial)

**4. Cycle Time**:
- Measure: Time to complete test part
- Compare: Before/after optimization
- Typical improvement: 20-50% with tuning and trajectory optimization

**5. Surface Finish**:
- Measure: Surface roughness (Ra, Rz) with profilometer
- Visual inspection (chatter marks, start/stop marks)
- Typical: Ra = 50-200 µin (1.3-5 µm) for milling

### Standard Test Programs

**1. Circular Interpolation Test**:
```gcode
G0 X2 Y0 Z0.1
G1 Z-0.1 F20
G2 I-2 J0 F100  ; Full circle, R=2"
G0 Z0.1
M30
```

**Measure**: Radial deviation at 0°, 90°, 180°, 270°

**2. Square with Rounded Corners**:
```gcode
G64 P0.005
G0 X0 Y0 Z0.1
G1 Z-0.05 F10
G1 X4 F100
G3 X4.5 Y0.5 I0 J0.5
G1 Y4
G3 X4 Y4.5 I-0.5 J0
G1 X0
G3 X-0.5 Y4 I0 J-0.5
G1 Y0
G3 X0 Y-0.5 I0.5 J0
G0 Z0.1
M30
```

**Measure**: Corner radius, dimensional accuracy, cycle time

**3. Ballbar Test** (ISO 230-4):
- Circular motion with telescoping ballbar
- Measures geometric errors, servo performance
- Professional tool (~$5000-15000)

### Documentation

**Record Final Configuration**:

**1. Machine Specifications**:
- Travel: X, Y, Z
- Max velocity: per axis
- Max acceleration: per axis
- Motor specifications (model, torque, speed)
- Encoder specifications (model, resolution)
- Drive specifications (model, voltage, current)

**2. Servo Tuning Parameters**:
| Axis | P | I | D | FF1 | FF2 | Bias | Max Output |
|------|---|---|---|-----|-----|------|------------|
| X | 125 | 10 | 15 | 0.95 | 0.002 | 0.0 | 10.0 |
| Y | 120 | 10 | 14 | 0.94 | 0.002 | 0.0 | 10.0 |
| Z | 100 | 12 | 12 | 0.90 | 0.001 | 2.5 | 10.0 |

**3. Test Results**:
- Date of testing
- Circular interpolation test: ±0.0015" radial error
- Repeatability: ±0.0002"
- Cycle time (test part): 3.2 minutes

**4. Known Issues and Workarounds**:
- Resonance at 247 Hz (notch filter active)
- Thermal drift: 0.001"/hour (allow 30 min warm-up)

## Advanced Diagnostics

### Frequency Response Measurement

**Purpose**: Measure actual system bandwidth, identify resonances.

**Method** (LinuxCNC with Halscope):
1. Apply sinusoidal position command (varying frequency)
2. Measure position response amplitude and phase
3. Plot Bode diagram (gain and phase vs. frequency)
4. Identify: Bandwidth, resonances, phase margin

**Tools**:
- MATLAB/Octave: Signal processing toolbox
- Python: scipy.signal
- LinuxCNC: External script + Halscope data export

**Example Findings**:
- Bandwidth: 35 Hz (-3 dB point)
- Resonance at 247 Hz (+8 dB peak)
- Phase margin: 42° (acceptable, 30-60° target)

**Action**: Add notch filter at 247 Hz, increase P gain (bandwidth → 50 Hz).

### Modal Analysis (Mechanical)

**Purpose**: Identify mechanical resonance modes (frequency, damping, mode shape).

**Method**:
1. Impact hammer + accelerometer
2. Measure frequency response function (FRF)
3. FFT analysis
4. Identify peaks (resonances)

**Software**:
- Professional: ME'scope, LMS Test.Lab ($$$)
- DIY: Smartphone accelerometer app + Python FFT

**Example**:
- Mode 1: 120 Hz (gantry vertical bending)
- Mode 2: 247 Hz (Z-axis torsion)
- Mode 3: 380 Hz (spindle holder)

**Action**: Add bracing to reduce Mode 1, notch filter for Mode 2.

## Summary

Systematic troubleshooting and optimization achieve high-performance CNC:

**Key Practices**:
1. **Systematic Approach**: Observe, hypothesize, test, verify
2. **One Variable at a Time**: Isolate root cause
3. **Documentation**: Record configuration, results
4. **Benchmarking**: Measure performance objectively

**Common Issues**:
- **Oscillation**: Gains too high, mechanical resonance, noise
- **Following Error**: Gains too low, no feedforward, mechanical resistance
- **Poor Finish**: Vibration, tuning mismatch, excessive blending
- **Inconsistent Position**: Backlash, thermal expansion, missed steps

**Optimization Strategies**:
- Feedforward control (biggest performance gain)
- Trajectory planning (blending, look-ahead)
- Mechanical improvements (stiffness, damping)
- Advanced techniques (notch filters, S-curves)

**Validation**:
- Circular interpolation test (contouring accuracy)
- Repeatability testing (precision)
- Surface finish measurement (quality)
- Cycle time comparison (throughput)

**Final Thought**: Advanced control transforms mechanical machines into precision instruments. Proper tuning and optimization unlock machine potential.

---

**Module 19 Complete**: You now have comprehensive knowledge of advanced control systems for CNC applications.

**Continue Learning**:
- Practice tuning on real machines
- Study control theory in depth (textbooks, courses)
- Experiment with advanced techniques (notch filters, adaptive control)
- Join CNC communities (LinuxCNC forum, CNCzone, etc.)

**Next Modules**:
- Module 20: CAM Software and Toolpath Generation
- Module 21: Advanced Manufacturing Techniques
