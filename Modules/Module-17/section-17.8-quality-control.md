# 17.8 Quality Control and Inspection for Advanced Materials

## Unique Inspection Challenges

### Hidden Defects in Composites

**Internal Delamination**:
- Plies separated inside part (not visible externally)
- Causes: Excessive cutting forces, improper cure, impact damage
- Catastrophic failure mode (sudden strength loss)
- **Cannot detect by visual inspection**

**Voids**:
- Air pockets within laminate
- Causes: Improper layup, incomplete resin infiltration
- Reduce strength 5-30% depending on void content
- Not visible once cured

**Fiber Misalignment**:
- Fibers not oriented as designed
- Causes: Shifting during layup, improper cutting
- Reduces strength in load direction

### Hidden Defects in Ceramics

**Subsurface Cracks**:
- Microcracks below surface from grinding
- Not visible to eye (1-50 μm deep)
- Propagate under load → fracture
- Reduce strength 20-50%

**Inclusions**:
- Foreign particles in ceramic body
- Causes: Contamination during powder processing
- Stress concentrators (failure initiation sites)

**Density Variations**:
- Non-uniform sintering
- Weak regions more porous
- Can fracture prematurely

## Dimensional Inspection

### Composites Dimensional Challenges

**Moisture Absorption**:
- Epoxy composites absorb 1-5% water by weight
- Swelling: 0.1-0.5% dimensional change
- Reversible (part shrinks when dried)
- **Measure in controlled environment** (50% RH, 68°F standard)

**Thermal Expansion**:
- Carbon fiber: Near-zero or negative CTE (along fiber)
- Epoxy matrix: Positive CTE (~50 ppm/°C)
- Part dimensions temperature-dependent
- **Measure at reference temperature** (68°F typical)

**Springback**:
- Residual stresses cause shape change after machining
- Parts drift hours to days after cutting
- **Allow stabilization time before final inspection**

### Ceramics Dimensional Challenges

**Firing Shrinkage**:
- Green → fired: 15-20% linear shrinkage typical
- Variation: ±0.5% batch-to-batch
- Cannot hold tight tolerances without fired grinding

**Thermal Expansion** (during measurement):
- Alumina: 8 ppm/°C
- If measured at 80°F instead of 68°F:
  - 2.000" part grows 0.000192" (0.0002")
- Significant for tight tolerances (±0.001")

**Grinding Burn**:
- Overheating during grinding → localized expansion during measurement
- False reading (part appears oversize)
- Cools, shrinks → actually undersize

### Measurement Tools

**Calipers/Micrometers**:
- Standard tools (±0.001" accuracy)
- **Caution with ceramics**: Point contact stress → can chip edge
- Use flat anvils (not pointed)

**Coordinate Measuring Machine (CMM)**:
- Probe touches part, records 3D coordinates
- Accuracy: ±0.0001" (high-end machines)
- Software calculates dimensions, GD&T

**CMM Challenges with Advanced Materials**:
- Composite surfaces soft (probe deforms surface slightly)
- Ceramic surfaces chip easily (probe contact force)
- Solution: Non-contact probe (optical, laser)

**Optical Comparator**:
- Projects magnified shadow of part onto screen
- Compare to overlay (drawing)
- Good for edge inspection, small features
- No contact (gentle on fragile parts)

**Laser Scanner**:
- Non-contact 3D measurement
- Fast (thousands of points per second)
- Good for complex shapes
- Expensive ($20,000-200,000)

### GD&T Considerations

**Flatness** (ceramics):
- Lapping achieves 0.0001" easily
- Measure with optical flat (interference fringes)
- One fringe = 0.000012" deviation

**Parallelism** (ceramics):
- CMM or indicator on surface plate
- Achievable: ±0.0001" for lapped ceramics

**Profile** (composites):
- Complex 3D shapes common
- CMM or laser scanner required
- Compare scan to CAD model

## Non-Destructive Testing (NDT)

### Ultrasonic Inspection (UT)

**Principle**: Sound waves reflect from defects

**Process**:
1. Transducer emits ultrasonic pulse (1-10 MHz)
2. Pulse travels through part
3. Reflects from back surface or internal defect
4. Transducer receives echo
5. Time delay indicates defect depth

**Pulse-Echo Mode**:
```
Transducer ─────► │░░░░░░░░│ ◄───── Echo from back
                  │  Part  │
                  │   •    │ ◄───── Echo from void (earlier)
                  │░░░░░░░░│
```

**Through-Transmission Mode**:
```
Transmitter ──►│░░░░░░░░│──► Receiver
               │  Part  │
               │   •    │ = Void blocks signal (no signal at receiver)
```

**Detects**:
- Delamination (composites)
- Voids (composites)
- Cracks (ceramics)
- Porosity, inclusions

**Advantages**:
- Internal defects detected
- Quantitative (defect size, depth)
- Relatively fast

**Limitations**:
- Requires coupling (water, gel between transducer and part)
- Complex shapes difficult
- Interpretation requires training
- Equipment: $5,000-50,000

**C-Scan Output**:
- 2D map of part (color-coded)
- Good regions: One color
- Defects: Different color (amplitude drop)
- Easy visualization

**Example**:
- Carbon fiber panel, 0.250" thick
- 5 MHz transducer
- Scan 12" × 12" panel: 10-30 minutes
- Defect >0.050" diameter detectable

### Radiography (X-Ray, CT)

**Principle**: X-rays pass through part, absorbed by defects differently

**2D Radiography** (X-ray image):
- X-ray source on one side, film/detector on other
- Dense regions (inclusions) appear lighter
- Voids appear darker
- Similar to medical X-ray

**Computed Tomography (CT)**:
- Multiple X-ray images from different angles
- Computer reconstructs 3D model
- Slice through part virtually (see internal features)
- Very detailed

**Detects**:
- Voids, porosity
- Inclusions (dense particles)
- Cracks (if oriented correctly)
- Fiber orientation (composites)

**Advantages**:
- Excellent visualization (CT)
- No contact
- Permanent record (images)

**Limitations**:
- Expensive (CT: $100,000-1,000,000)
- Slow (CT: 30 min to several hours per part)
- Radiation safety (shielding, licensing)
- Composites: Low contrast (carbon and resin similar density)

**Applications**:
- High-value parts (aerospace)
- Failure analysis
- Production CT for critical parts (automotive, medical)

### Thermography (Infrared Inspection)

**Principle**: Heat flow disrupted by defects

**Active Thermography**:
1. Heat part (flash lamp, hot air)
2. Infrared camera observes cooling
3. Defects (voids, delaminations) cool differently
4. Thermal image shows defects

**Passive Thermography**:
- Part in service generates heat
- Monitor with IR camera
- Hot spots indicate problems (friction, overload)

**Detects**:
- Delamination (composites)
- Voids near surface (<0.125" deep)
- Poor bond lines

**Advantages**:
- Fast (seconds to minutes)
- Large area inspection (full panel)
- Non-contact
- Good for composites (UT sometimes difficult with complex weaves)

**Limitations**:
- Shallow defects only
- Requires thermal contrast
- Equipment: $10,000-100,000 (IR camera)

### Tap Test (Coin Test)

**Principle**: Sound changes when striking defect

**Process**:
- Tap part surface with coin, small hammer, or automated tapper
- Listen to sound
- Solid area: Clear, ringing tone
- Delaminated area: Dull, dead sound (energy absorbed by gap)

**Advantages**:
- Simple, cheap (coin)
- Fast
- Effective for large defects (>0.25" diameter)

**Limitations**:
- Subjective (depends on operator hearing)
- Small defects undetectable
- No permanent record

**Automated Tap Testing**:
- Mechanical tapper + microphone
- Computer analyzes sound frequency
- More objective than manual
- Equipment: $5,000-20,000

### Visual and Optical Inspection

**Borescope** (fiber optic scope):
- Inspect internal passages, holes
- Diameter: 2-10 mm typical
- Composites: Look for delamination at edges, fiber pullout

**Dye Penetrant** (ceramics):
1. Apply bright dye to surface
2. Dye seeps into cracks (capillary action)
3. Wipe surface clean
4. Apply developer (pulls dye back out)
5. Cracks visible as bright lines

**Detects**: Surface-breaking cracks only (not internal)

**Advantages**: Simple, cheap, very sensitive (0.001" wide cracks)

**Limitations**: Surface only, messy (cleaning required)

**Microscopy**:
- Optical microscope: 10-1000× magnification
- Inspect edge quality, fiber orientation, crack size
- Scanning Electron Microscope (SEM): >10,000× magnification
  - Fracture surface analysis (failure mode)
  - Fiber-matrix adhesion quality
  - Very expensive (>$100,000)

## Mechanical Testing

### Destructive Testing (Lot Sampling)

**Purpose**: Verify material properties (not every part, but sample)

**Tensile Test** (composites):
- ASTM D3039 (flat coupon test)
- Measures: Ultimate tensile strength, modulus, strain-to-failure
- Verify: Material meets specification
- Frequency: Each lot of material, or quarterly

**Flexural Test** (ceramics):
- ASTM C1161 (4-point bend)
- Measures: Flexural strength (modulus of rupture)
- Ceramics too brittle for tensile test
- Frequency: Each batch of parts (5-10 samples typical)

**Example** (alumina):
- Specification: σ_flexural >400 MPa
- Test 10 samples per batch
- All pass → accept batch
- Any fail → investigate (possibly reject batch)

**Weibull Statistics**:
- Ceramics have large strength variation (brittle fracture)
- Strength described by Weibull distribution
- Requires many samples (20-30) for accurate characterization
- Used for design (account for probability of failure)

### Non-Destructive Strength Testing

**Proof Testing**:
- Load part to fraction of design load (80-90%)
- If survives → acceptable
- If fails → defective (removed from population)
- Increases reliability of fleet (weak parts eliminated)

**Application**:
- Ceramic parts for critical service (engine components)
- Composite pressure vessels

**Limitation**: Some parts damaged (subcritical crack growth) even if pass test

## Surface Quality Inspection

### Surface Roughness

**Profilometer** (stylus type):
- Quantitative Ra measurement
- Industry standard
- Verifies grinding/polishing quality

**Comparator Blocks**:
- Machined samples with known Ra
- Fingernail test: Drag fingernail across sample, then part
- Match feel/appearance
- Inexpensive, subjective

**Typical Specifications**:
- Composite machined edge: Ra <63 μin
- Ceramic ground surface: Ra <32 μin
- Ceramic polished seal face: Ra <5 μin

### Gloss (Composites)

**Glossmeter**:
- Measures specular reflection (shininess)
- Verifies polish quality
- Batch consistency

**Example Specification**:
- Carbon fiber show panel: >85 GU @ 60° (high gloss)

### Edge Quality (Composites)

**Visual Inspection**:
- Magnification: 5-10× (handheld magnifier)
- Look for:
  - Delamination (gap between plies)
  - Fiber pullout (holes)
  - Fuzzing (loose fibers)
  - Resin voids (gaps)

**Accept/Reject Criteria** (example):
- Delamination >0.010" long: Reject
- Fiber pullout >0.020" diameter: Reject
- Fuzzing: Acceptable if removable by light sanding

### Subsurface Damage (Ceramics)

**Indentation Test**:
- Vickers indenter pressed into surface
- Observe cracks radiating from indentation
- Crack length indicates subsurface damage depth

**Example**:
- As-ground: Cracks extend 50 μm from indentation
- Polished: Cracks extend 5 μm
- Conclusion: Polishing removed 45 μm damaged layer

**Etching**:
- Chemical etch reveals grain structure
- Grinding damage visible as disturbed grain layer
- Metallographic technique (destructive, sample only)

## In-Process Monitoring

### Tool Wear Monitoring

**Why Critical for Advanced Materials**:
- Rapid tool wear (abrasive fibers, hard ceramics)
- Dull tool → poor quality (delamination, chipping)
- Quality degrades before tool "feels" dull

**Dimensional Trending**:
- Measure first part, every 10th part, last part in run
- Plot dimension vs part number
- Trend shows tool wear
- Example: Hole diameter increases 0.001" over 50 parts → tool wearing

**Visual Inspection**:
- Microscope (10-20×) inspect cutting edge
- Compare to new tool
- Replace when wear land >0.010" (composites), >0.005" (ceramics)

**Tool Life Tracking**:
- Log tool hours (spindle on-time)
- Replace at predetermined interval (before failure)
- Example: Diamond endmill in CFRP, 20 hours life

### Part Count to Failure

**Establish Tool Life**:
- Run tools to failure (quality degrades)
- Count parts machined
- Set replacement interval at 70-80% of failure count
- Example: Tool fails at part 150 → replace at part 100

### Force/Vibration Monitoring

**Dynamometer**: Measures cutting forces
- Dull tool → higher forces
- Threshold alarm (force exceeds limit → stop)
- Expensive ($10,000-50,000), research/production use

**Accelerometer**: Detects vibration
- Chatter → poor finish, tool damage
- Monitor vibration amplitude
- Stop machine if excessive

**Spindle Load Monitoring**:
- CNC monitors spindle current
- Dull tool → higher current (more resistance)
- Alarm if current exceeds limit
- Built into some CNCs

## Statistical Process Control (SPC)

### Control Charts

**X-bar Chart** (average):
- Plot average dimension of sample (5 parts)
- Control limits: ±3 standard deviations from mean
- Points outside limits → process out of control

**R Chart** (range):
- Plot range (max - min) of sample
- Monitors variation (consistency)
- Increasing range → tool wear, process instability

**Example** (ceramic grinding):
- Dimension: 2.000 ±0.002"
- Sample: Measure 5 parts every 30 minutes
- Plot average and range
- Trend shows process drift (tool wear)
- Adjust before parts go out of tolerance

### Cpk (Process Capability)

**Definition**: How well process fits within tolerance

$$C_{pk} = \min\left(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right)$$

where:
- $USL$ = Upper Specification Limit
- $LSL$ = Lower Specification Limit
- $\mu$ = Process mean
- $\sigma$ = Process standard deviation

**Interpretation**:
- $C_{pk}$ <1.0: Process produces defects (cannot meet tolerance)
- $C_{pk}$ = 1.33: Acceptable (4-sigma process)
- $C_{pk}$ = 1.67: Good (5-sigma process)
- $C_{pk}$ >2.0: Excellent (6-sigma process)

**Example**:
- Tolerance: 2.000 ±0.002" (LSL = 1.998, USL = 2.002)
- Process mean: μ = 2.000"
- Process std dev: σ = 0.0005"
- $C_{pk}$ = (2.002 - 2.000) / (3 × 0.0005) = 1.33 (acceptable)

**If Cpk Low**:
- Reduce variation (better machine, sharper tools, stable environment)
- Center process (adjust offsets)
- Widen tolerance (negotiate with customer)

## Quality Documentation

### Inspection Reports

**First Article Inspection (FAI)**:
- Complete dimensional inspection of first production part
- Verify all features meet drawing
- AS9102 form (aerospace) or similar
- Submitted to customer for approval

**In-Process Inspection**:
- Frequency: Per control plan (e.g., every 10 parts)
- Record dimensions, visual inspection results
- Batch traceability (lot numbers, material certs)

**Final Inspection**:
- Before shipping
- Verify critical dimensions, visual quality
- Certificate of Conformance (CoC)

### Material Certifications

**Composites**:
- Prepreg lot number, cure date
- Mechanical test results (tensile, flexural)
- Traceability to raw material batch

**Ceramics**:
- Powder lot number
- Sintering parameters (temperature, time)
- Density, grain size
- Mechanical properties (flexural strength, hardness)

**Retention**:
- Aerospace: Permanent (life of aircraft)
- Automotive: 15 years typical
- General industry: 5-10 years

### NDT Reports

**Ultrasonic C-Scan**:
- Image of part (color-coded defect map)
- Operator notes (defect locations, sizes)
- Accept/reject decision with criteria

**Radiography**:
- X-ray images (film or digital)
- Defect call-outs (circles, arrows)
- Interpretation by certified technician (Level II or III per ASNT)

## Acceptance Criteria Development

### Defining Defect Limits

**Cosmetic vs Structural**:
- Cosmetic: Visible defects, don't affect strength (scratches, color variations)
- Structural: Affect performance (cracks, delamination, porosity)

**Example** (composite panel):
- Scratches <0.010" deep: Acceptable (cosmetic)
- Surface porosity <0.020" diameter, <5 per square inch: Acceptable
- Delamination any size: Reject (structural)

**Engineering Analysis**:
- FEA (finite element analysis) with defect modeled
- Stress concentration factor
- Determine safe defect size

**Example** (ceramic):
- Part design: σ_max = 200 MPa in service
- Material strength: 400 MPa (safety factor 2.0)
- Analysis: 0.1 mm surface crack → stress concentration 2.5× → σ_local = 500 MPa
- Conclusion: Reject parts with cracks >0.1 mm

### Industry Standards

**Composites**:
- ASTM D standards (test methods)
- SAE, AMS specs (aerospace materials)
- Customer specifications (often proprietary)

**Ceramics**:
- ASTM C standards (ceramic materials, test methods)
- ISO standards (international)
- Military specs (MIL-STD)

**NDT**:
- ASTM E standards (NDT procedures)
- ASNT (American Society for Nondestructive Testing) certification

## Cost of Quality

### Inspection Cost

**In-Process Inspection**:
- Operator measures dimensions: 2-5 min per part
- @ $25/hour → $0.83-2.08 per part

**Final Inspection**:
- CMM inspection (complex part): 30-60 min
- @ $50/hour (technician + equipment) → $25-50 per part

**NDT (Ultrasonic C-Scan)**:
- Setup + scan: 30 min per part
- @ $60/hour → $30 per part
- Equipment amortization: $10-20 per part
- **Total**: $40-50 per part

**Cost Drivers**:
- Inspection frequency (every part vs sampling)
- Complexity (number of features)
- Equipment cost (CMM, NDT)

### Cost of Poor Quality

**Scrap** (defect found before shipping):
- Material cost
- Machining cost
- Example: $500 part, scrap rate 5% → $25 per good part (scrap cost allocated)

**Rework** (defect repairable):
- Labor to fix (sanding, filling, re-grinding)
- Example: 30 min @ $30/hour = $15
- If 10% require rework → $1.50 per part average

**Return/Warranty** (defect found by customer):
- Replacement part: $500
- Shipping: $50
- Customer downtime: $1,000-10,000 (lost revenue)
- Reputation damage: Unquantifiable
- **Far exceeds scrap cost**

**Liability** (part fails in service):
- Injury, property damage
- Legal costs, settlements: $100,000-10,000,000+
- Aerospace, medical: Extremely high stakes

**Conclusion**: Inspection is cheap compared to failures

## Summary

Quality control for advanced materials requires specialized techniques:

**Inspection Challenges**:
- Hidden defects (delamination, subsurface cracks)
- Dimensional instability (moisture, thermal effects)
- Fragile (contact measurement difficult)

**Dimensional Inspection**:
- CMM, optical measurement (non-contact preferred)
- Control environment (temperature, humidity)
- GD&T: Flatness, parallelism achievable to ±0.0001" (ceramics)

**Non-Destructive Testing**:
- Ultrasonic: Detects internal delamination, voids, cracks
- Thermography: Fast, large area, shallow defects
- Radiography/CT: Excellent visualization, slow, expensive
- Tap test: Simple, effective for large delaminations

**Mechanical Testing**:
- Destructive sampling: Verify material properties
- Proof testing: Remove weak parts from population

**Surface Quality**:
- Profilometer: Ra measurement (objective)
- Glossmeter: Polish quality (composites)
- Visual: Edge quality, defects

**In-Process Monitoring**:
- Tool wear trending (dimensional, visual)
- SPC charts: Detect process drift

**Documentation**:
- FAI, in-process reports, material certs
- NDT reports with images
- Traceability (aerospace: permanent records)

**Cost**:
- Inspection: $5-50 per part (method-dependent)
- Poor quality: $500-1,000,000+ per failure
- **Inspection is cheap insurance**

**Next**: Safety and health hazards in advanced materials machining

---

**Next**: [17.9 Safety and Health Hazards](section-17.9-safety-health.md)
