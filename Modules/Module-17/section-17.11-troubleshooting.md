# 17.11 Troubleshooting Common Issues in Advanced Materials Machining

## Composite Machining Problems

### Delamination

**Symptom**: Plies separate at edges, visible gaps between layers

**Entry Delamination** (top surface):
```
     ↓ Tool entry
═════════════  ← Top ply lifts
  ───────────
  ───────────  Intact plies
  ───────────
═════════════
```

**Exit Delamination** (bottom surface):
```
═════════════
  ───────────
  ───────────  Intact plies
  ───────────
═════════════  ← Bottom ply peels away
     ↓ Tool exit (unsupported)
```

**Causes**:

| Cause | Why It Happens | Evidence |
|-------|----------------|----------|
| Dull tool | High forces peel plies apart | Delamination worsens over run |
| Feed too high | Excessive force per revolution | Consistent delamination, even new tool |
| No backing support | Exit ply unsupported (bends, tears) | Exit side only, entry side clean |
| Wrong tool (conventional) | Upcut pushes bottom ply down, downcut lifts top | Entry or exit specific |
| Insufficient clamping | Part vibrates (peeling action) | Random locations |

**Solutions**:

**Immediate**:
1. **Reduce feed rate**: Cut feed by 30-50%
   - Example: 100 IPM → 50 IPM
2. **Replace tool**: If dull (check wear land)
3. **Add backing**: Sacrificial MDF, phenolic, or same material underneath
   - Clamp sandwich (backing + part) together
4. **Use compression cutter**: Upcut flutes at tip (push bottom ply up), downcut at top (push top ply down)
   - Both surfaces compressed into part

**Long-term**:
- Establish tool life (replace proactively)
- Use compression or diamond-coated tools
- Vacuum table (distributed clamping, no point loads)

**Repairing Delamination**:
- Minor (<0.030"): Inject thin epoxy (syringe), clamp, cure, sand flush
- Major (>0.030"): Part likely scrap (structural weakness)

### Fuzzing

**Symptom**: Loose fibers standing up from surface (hairy appearance)

**Causes**:
- Dull tool (fibers torn, not cut cleanly)
- Cutting against fiber direction (fibers pulled)
- Wrong tool geometry (too aggressive)
- Aramid fibers (Kevlar): Naturally fuzzy (fiber is tough, hard to cut)

**Solutions**:

**Prevention**:
1. **Sharp tools**: Replace when fuzzing starts
2. **Cut with fiber direction**: If unidirectional, feed along fibers
3. **Higher speed, lower feed**: Less force per fiber
   - Example: 18,000 RPM, 50 IPM (vs 12,000 RPM, 100 IPM)
4. **Compression cutter**: Shears fibers cleanly

**Cleanup** (if fuzzing occurs):
1. Light sanding (220-320 grit) removes loose fibers
2. Flame polish (very brief propane torch pass): Melts fuzz (dangerous, practice required)
3. Sharp blade scraping (carefully)

**Aramid-Specific**:
- Extremely fuzzy by nature (tough fiber resists cutting)
- Scissors-type cutters work better than mills
- Ultrasonic cutting (high-frequency vibration) reduces fuzzing

### Burning/Heat Damage

**Symptom**: Darkened, charred surface; melted resin; smoking during cut

**Causes**:
- Dull tool (friction generates heat)
- Speed too high (heat from rubbing)
- Feed too low (tool dwells in cut, heat accumulates)
- Insufficient chip evacuation (chips recutting = heat)

**Solutions**:

**Immediate**:
1. **Reduce spindle speed**: Cut RPM by 20-30%
   - Example: 24,000 RPM → 18,000 RPM
2. **Increase feed rate**: Reduce dwell time
   - Example: 50 IPM → 80 IPM
3. **Replace tool**: If dull
4. **Air blast**: Compressed air (coolant) at cut zone

**Long-term**:
- Optimize feeds/speeds (high feed, moderate speed)
- Sharp tools (proactive replacement)
- Chip evacuation (vacuum near cutter, air blast)

**Temperature Limits**:
- Epoxy: 250-350°F (starts softening)
- Phenolic: 300-400°F
- Visual smoke = >400°F (resin burning)

**Damage Assessment**:
- Light discoloration: Cosmetic (usually acceptable)
- Heavy charring: Resin degraded (structural damage, reject)
- Matrix Analysis: DSC (differential scanning calorimetry) detects thermal damage

### Fiber Pullout

**Symptom**: Holes where fibers torn out (not cut cleanly)

**Causes**:
- Dull tool
- Wrong fiber orientation (cutting perpendicular to fibers)
- Tool geometry (negative rake pulls instead of shears)

**Solutions**:
1. **Sharp tool**: Positive rake geometry preferred
2. **Reduce feed**: Less force per fiber
3. **Higher speed**: Shearing action (not pulling)
4. **Climb milling**: Cutting fibers at entry (not exit)

**Repair** (if minor):
- Fill with epoxy (color-matched), sand flush
- Major pullout: Structural concern, possibly reject

### Uneven Edge Quality

**Symptom**: Some edges clean, others ragged (same part)

**Causes**:
- Fiber orientation variation (woven fabrics have 0° and 90° fibers)
- Uneven clamping (part vibrates in some areas)
- Tool runout (cutting edge wobbles)

**Solutions**:
1. **Check fiber orientation**: Adjust feed direction if possible
2. **Improve clamping**: Add clamps, use vacuum table
3. **Check tool runout**: Collet, holder, spindle taper
   - Acceptable: <0.0005" TIR (total indicator reading)
   - Poor: >0.001" TIR → replace collet/holder

**Runout Measurement**:
- Dial indicator on tool shank (near cutting edge)
- Rotate spindle by hand, observe reading
- Causes: Dirty taper, worn collet, bent tool

## Ceramic Machining Problems

### Edge Chipping

**Symptom**: Small chips (0.001-0.020") missing from edges, corners

**Causes**:

| Cause | Mechanism | Evidence |
|-------|-----------|----------|
| Depth of cut too high | Excessive force (brittle fracture) | Chipping size correlates with DOC |
| Wheel too coarse | Large grains create large chips | Chipping size matches grit size |
| Exit edge unsupported | Edge breaks off (no backing) | Exit side only |
| Grinding burn | Localized heating → thermal stress → crack | Discoloration near chip |

**Solutions**:

**Immediate**:
1. **Reduce depth of cut**: Cut DOC by 50%
   - Example: 0.002" → 0.001" per pass
2. **Finer grit wheel**:
   - If using 120 grit, switch to 220-320 grit
3. **Add support**: Magnetic chuck, adhesive backing
4. **Spark-out passes**: 2-5 passes at zero depth (wheel/part spring back)

**Long-term**:
- Dress wheel regularly (sharp particles)
- Optimize parameters (lower DOC, finer grit for finishing)
- Post-grinding chamfer (0.002-0.005" × 45°): Removes fragile edge

**Repair** (if necessary):
- Light chipping (<0.005"): May be acceptable (check drawing)
- Diamond honing: Remove sharp edges of chip (cosmetic improvement)
- Large chips: Part likely scrap (stress concentrator)

### Cracking

**Symptom**: Visible cracks (usually radial from holes, corners)

**Causes**:
- Thermal shock (rapid heating/cooling)
  - Coolant application: Intermittent = cycling = cracks
  - Grinding burn: Localized heating
- Mechanical stress (excessive force)
- Pre-existing flaws (propagate under stress)

**Thermal Shock Mechanism**:
1. Grinding heats surface locally
2. Surface expands (thermal expansion)
3. Cooler interior restrains expansion (stress)
4. Rapid cooling (coolant splash): Surface contracts
5. Tensile stress exceeds fracture strength → crack

**Solutions**:

**Thermal Management**:
1. **Flood coolant**: Continuous, not intermittent
   - Flow rate: 5-10 GPM minimum
2. **Reduce heat generation**:
   - Lower wheel speed (reduce friction)
   - Lighter DOC (less energy input)
   - Sharp wheel (less rubbing)
3. **Slow down**: Lower table speed (longer coolant contact, better cooling)

**Mechanical Stress Reduction**:
1. **Support part**: Avoid point clamping (stress concentrations)
2. **Reduce forces**: Lighter cuts, finer wheel

**Prevention**:
- Stress relief anneal (after grinding): Heat to 50-70% sintering temp, slow cool
  - Removes residual stresses
  - Example (alumina): 1000-1200°C, 2 hours, slow cool
- Quality raw material (low defect content)

**Inspection**:
- Dye penetrant (surface cracks)
- Ultrasonic (internal cracks)

### Grinding Burn

**Symptom**: Discoloration (yellow, brown, blue on white ceramics); surface damage

**Causes**:
- Excessive heat from grinding (friction)
- Dull wheel (rubbing, not cutting)
- Insufficient coolant
- Too high wheel speed or DOC

**Damage**:
- Localized phase transformation (material structure changes)
- Residual tensile stress (weakens part)
- Microcracks (subsurface)

**Detection**:
- Visual: Discoloration
- Nital etch (metallographic): Burned layer appears different
- Hardness test: Burned zone often softer (over-tempered) or harder (re-hardened)

**Solutions**:

**Immediate**:
1. **Dress wheel**: Expose sharp particles
2. **Increase coolant flow**: 10+ GPM
3. **Reduce DOC**: Cut by 50% (0.001" → 0.0005")
4. **Lower wheel speed**: Reduce by 10-20%

**Prevention**:
- Sharp wheel (frequent dressing)
- Flood coolant (proper application, aimed at cutting zone)
- Conservative parameters (slower = cooler)

**Repair**:
- Grind off burned layer (0.002-0.010" deep typically)
- Re-grind part to spec (if enough stock remains)
- Otherwise: Scrap

### Wheel Loading

**Symptom**: Grinding wheel clogs (pores filled with debris), grinding slows, poor finish

**Causes**:
- Soft material (relatively): Some ceramics smear into wheel
- Inadequate coolant (chips not flushed)
- Wheel too hard (bond doesn't release dulled particles)
- Wheel too fine (pores too small, fill quickly)

**Evidence**:
- Increasing grinding forces
- Surface finish degrades
- Wheel face appears clogged (gray, glazed)

**Solutions**:

**Immediate**:
1. **Dress wheel**: Removes loaded material
2. **Increase coolant flow**: Better chip flushing
3. **Dressing stick**: Aluminum oxide stick (cleans wheel during grinding)
   - Hold stick against rotating wheel (breaks up loading)

**Long-term**:
1. **Softer wheel grade**: Self-dressing (particles release sooner)
   - Example: N grade → M grade
2. **Coarser grit**: Larger pores (resist loading)
   - Example: 320 grit → 220 grit
3. **Lower concentration**: Fewer diamonds = more pore space
   - Example: 150 → 100 concentration

### Poor Surface Finish

**Symptom**: Scratches, roughness above specification

**Causes**:

| Symptom | Cause | Solution |
|---------|-------|----------|
| Coarse, even scratches | Grit too coarse | Finer grit wheel |
| Random deep scratches | Contamination (chip re-cutting) | Better coolant flow, dressing |
| Chatter marks (wavy) | Vibration | Reduce DOC, check setup rigidity |
| Dull, smeared surface | Wheel loaded | Dress wheel |

**Solutions**:

**Grit Selection**:
- Current: 120 grit (Ra 100 μin)
- Target: Ra 32 μin
- Solution: 320 grit wheel (Ra 20-40 μin capable)

**Contamination Control**:
- Flood coolant (flush chips)
- Clean coolant (filter, change regularly)
- Dress wheel (remove embedded chips)

**Vibration Reduction**:
- Check workholding (loose part?)
- Machine rigidity (level machine, tighten gibs)
- Wheel balance (out-of-balance = vibration)
- Reduce DOC (less force = less vibration)

**Final Finish Improvement**:
- Spark-out passes (2-5× at zero depth)
- Lapping (if ultra-smooth required)
- Polishing (colloidal silica)

## Dust Collection Problems

### Insufficient Capture

**Symptom**: Visible dust in air, accumulation on surfaces

**Causes**:
- Insufficient airflow (CFM too low)
- Poor hood design (dust escapes capture zone)
- Leaks in ductwork (lose velocity)
- Blocked filter (high resistance)

**Diagnosis**:

**Airflow Test**:
- Anemometer: Measure velocity at hood face
- Calculate CFM: Area (ft²) × Velocity (FPM)
- Compare to design CFM

**Example**:
- Hood: 6" × 6" (0.25 ft²)
- Measured velocity: 120 FPM
- Actual CFM: 0.25 × 120 = 30 CFM
- Design CFM: 200 CFM
- **Conclusion**: 85% loss (blockage or leak)

**Solutions**:

1. **Check filter**: Replace if loaded (pressure drop >6" WC)
2. **Inspect ductwork**: Look for disconnections, holes
3. **Seal leaks**: Aluminum tape, gaskets
4. **Increase blower**: Larger motor or faster speed (if possible)
5. **Reduce duct length**: Shorter run = less resistance

**Hood Improvement**:
- Closer to source (capture zone = ~1× hood diameter)
- Larger hood (more area, lower velocity needed)
- Flanges around hood (improve capture efficiency 25%)

### Filter Blinding

**Symptom**: Pressure drop very high (>8" WC), airflow drops rapidly

**Causes**:
- Fine dust (plugs pores)
- Moist dust (sticks to filter)
- Pulse cleaning inadequate (dust cake not removed)

**Solutions**:

**Immediate**:
1. **Manual cleaning**: Shake filters (if safe to access)
2. **Compressed air**: Blow filters clean (outside, wear respirator)

**Long-term**:
1. **More filter area**: Add cartridges (lower velocity, longer life)
2. **Pre-filter**: Cyclone separator (removes coarse dust before filter)
   - Captures 80-90% of dust by weight (centrifugal force)
   - Filter sees only fine dust (longer life)
3. **Better pulse system**: Higher pressure (60-90 PSI), more frequent pulses
4. **Nanofiber filters**: Surface-loading (dust cake on surface, not in pores)
   - Easier to pulse-clean
   - Cost: 2-3× standard filters

### Dust Escaping System

**Symptom**: Clean air side has visible dust (filter failure)

**Causes**:
- Filter torn (hole)
- Poor seal (gasket leaking)
- Filter saturated (dust passes through)

**Diagnosis**:
- Visual: White cloth on exhaust, run system 1 min, check cloth (dust?)
- Light test: Shine flashlight inside collector (look for light leaks = dust leaks)

**Solutions**:
1. **Inspect filters**: Replace torn filters immediately
2. **Check seals**: Gaskets between filter and housing
3. **Replace filters**: Even if not torn (efficiency degrades over time)

**Safety**:
- Dust escaping = exposure
- Investigate immediately (respiratory hazard)

## Equipment Malfunctions

### Spindle Issues

**Symptom**: Vibration, noise, overheating, loss of power

**Diagnosis**:

| Symptom | Probable Cause | Test | Solution |
|---------|---------------|------|----------|
| Vibration (new) | Tool imbalance, runout | Check runout (indicator) | Balance tool, replace collet |
| Vibration (gradual) | Bearing wear | Temperature (IR gun), noise | Replace bearings |
| Noise (grinding) | Dust in bearings | Spin by hand (rough?) | Rebuild spindle |
| Overheating (>140°F) | Seal failure, lubrication loss | Thermal camera | Replace seals, re-lubricate |
| Loss of power | Winding failure (carbon fiber short) | Resistance test (multimeter) | Rewind or replace |

**Runout Measurement**:
- Indicator on tool (near tip)
- Rotate spindle by hand
- TIR >0.001" = excessive (check collet, holder, taper)

**Bearing Temperature**:
- IR gun (non-contact thermometer)
- Normal: 100-130°F
- Warning: 130-150°F
- Shutdown: >150°F (risk of seizure)

**Prevention**:
- Dust control (air purge)
- Regular maintenance (seal replacement)
- Avoid crashes (bearing damage)

### Coolant System Problems

**Symptom**: Coolant not flowing, low pressure, foaming, smell

**Diagnosis**:

**No Flow**:
- Check pump (running?)
- Check filter (clogged?)
- Check lines (kinked, blocked?)

**Low Pressure**:
- Measure at nozzle (pressure gauge)
- Normal: 50-200 PSI (depending on system)
- Low: Clogged nozzle, weak pump, leak

**Foaming**:
- Cause: Concentration too high, contamination (soap, oil)
- Test: Measure concentration (refractometer)
  - Normal: 5-10%
  - High: >12% (foaming)
- Solution: Dilute (add water), skim foam

**Smell** (rotten, sulfur):
- Cause: Bacteria growth (anaerobic)
- Solution: Add biocide, change coolant, clean system
- Prevention: Maintain pH 8.5-9.5 (inhibits bacteria)

### Machine Accuracy Loss

**Symptom**: Parts out of tolerance, drift over time

**Causes**:
- Thermal drift (machine warming/cooling)
- Ballscrew wear (backlash)
- Scale contamination (dust on encoders)
- Foundation issues (machine not level)

**Diagnosis**:

**Thermal Drift**:
- Measure first part (cold machine) vs 10th part (warm)
- If dimensions drift consistently → thermal
- Solution: Warm-up cycle (run machine 15-30 min before production)

**Backlash Test**:
- Dial indicator on table
- Command +0.100" move, then -0.100"
- Measure actual movement in each direction
- Backlash = difference (should be <0.0005")
- High backlash → ballscrew/nut wear

**Scale Contamination**:
- Clean linear encoders (compressed air, lint-free cloth)
- Fine dust causes position errors

**Leveling**:
- Precision level (0.0005"/ft resolution)
- Check machine bed (should be within 0.001"/ft)
- Shim feet if needed

## Process Optimization

### Long Cycle Times

**Symptom**: Machining too slow, low productivity

**Optimization Strategies**:

**Increase Feed Rate**:
- Current: Conservative (safe but slow)
- Test: Increase feed by 20% (monitor quality)
- If quality OK: Continue increasing until quality degrades or forces excessive
- Example: CFRP routing 60 IPM → test 72 IPM → if OK, test 86 IPM

**Increase Depth of Cut**:
- Composites: Can often double DOC if feed reduced proportionally
- Example: 0.050" DOC @ 100 IPM → 0.100" DOC @ 70 IPM
  - Material removal rate increased 40%

**Optimize Tool Path**:
- Reduce rapid moves (non-cutting time)
- Use trochoidal milling (arcs instead of linear plunge)
- Minimize tool changes (group similar operations)

**Better Tools**:
- Diamond-coated: 10× tool life (fewer changes)
- Compression cutters: Clean entry/exit (less cleanup)

**Measurement**:
- Cycle time (current): 15 minutes
- Improvement: 20% faster feed = 12 minutes
- Savings: 3 min per part × 100 parts/day = 300 min/day (5 hours)

### Excessive Tool Wear

**Symptom**: Tools wearing faster than expected, high tool cost per part

**Diagnosis**:

**Compare to Baseline**:
- Expected tool life: 500 parts
- Actual: 150 parts
- **3× faster wear** → find cause

**Possible Causes**:

1. **Material harder than expected**:
   - Test hardness (different batch?)
   - Check material cert (correct material?)

2. **Feed/speed incorrect**:
   - Too high speed: Excessive heat (oxidation wear)
   - Too low feed: Rubbing (abrasive wear)
   - Optimize: Manufacturer recommendations

3. **Coolant issues**:
   - Concentration low: Poor lubrication
   - Contamination: Chips re-cutting

4. **Runout**:
   - High runout: One flute does all work (overloads)
   - Uneven wear on flutes
   - Check: TIR <0.0005"

**Solutions**:
- Optimize parameters (feeds/speeds database)
- Maintain coolant (concentration, cleanliness)
- Check setup (runout, clamping, vibration)
- Better tools (coating, geometry, material)

### Poor Part Quality

**Systematic Approach**:

1. **Define Problem**:
   - What feature(s) out of spec?
   - How much (measurement)?
   - When did it start (sudden or gradual)?

2. **Check Setup**:
   - Tool: Correct tool, sharp, properly seated?
   - Work offset: Confirmed (probe or edge finder)?
   - Clamping: Secure, not deforming part?

3. **Check Machine**:
   - Accuracy: Run test part or calibration routine
   - Maintenance: Lubrication, covers, seals OK?

4. **Check Process**:
   - Parameters: Feed/speed appropriate?
   - Tool path: Optimized (no chatter, good lead-in/out)?
   - Coolant: Flowing, correct concentration?

5. **Check Material**:
   - Correct material (verify cert)?
   - Consistent (same batch as previous good parts)?

6. **Check Environment**:
   - Temperature stable (thermal growth)?
   - Vibration (nearby equipment)?

**Document Findings**:
- Keep log (problem → investigation → solution)
- Build tribal knowledge (next time faster)

## Emergency Response

### Fire

**Types**:
- **Class A**: Ordinary combustibles (wood, paper)
  - Extinguisher: Water or ABC dry chemical
- **Class B**: Flammable liquids (resin, solvent)
  - Extinguisher: ABC dry chemical, CO₂, foam
- **Class C**: Electrical
  - Extinguisher: ABC dry chemical, CO₂ (non-conductive)

**Small Fire** (<3 ft):
1. Evaluate: Safe to fight?
2. Get extinguisher
3. Pull pin, aim at base, squeeze, sweep
4. If grows: Evacuate, call 911

**Large Fire**:
1. Evacuate immediately (activate fire alarm)
2. Close doors (contain)
3. Call 911 (from safe location)
4. Do not re-enter

### Dust Explosion

**Indicators** (rarely warning):
- Flash, fireball, pressure wave
- Usually sudden (no time to react)

**After Explosion**:
1. Evacuate (secondary explosion possible)
2. Account for personnel
3. Call 911 (injuries, fire)
4. Do not re-enter (structural damage, fire risk)

**Prevention** (critical):
- Housekeeping (no dust accumulation)
- Dust collection (remove fuel)
- No ignition sources (spark-proof tools, grounding)

### Major Coolant Spill

**Hazards**: Slip hazard, contamination

**Response**:
1. Stop source (shut off pump)
2. Contain (absorbent booms)
3. Absorb (pads, absorbent, kitty litter)
4. Dispose (per regulations, likely hazardous waste)
5. Clean/decontaminate area

**Prevent**:
- Berm around machines (contain spills)
- Regular inspection (hoses, connections)

## Summary

Troubleshooting advanced materials machining requires systematic diagnosis:

**Composites**:
- Delamination: Dull tool, high feed, no backing → compression cutter, backing support
- Fuzzing: Dull tool, wrong feed direction → sharp tools, cut with fibers
- Burning: Excessive heat → reduce speed, increase feed, sharp tools

**Ceramics**:
- Edge chipping: Excessive force, coarse wheel → lighter DOC, finer grit, spark-out
- Cracking: Thermal shock → flood coolant, reduce heat generation
- Grinding burn: Dull wheel, inadequate coolant → dress wheel, increase coolant flow

**Dust Collection**:
- Insufficient capture: Low CFM, poor hood → check filters, seal leaks, improve hood
- Filter blinding: Fine dust → pre-separator (cyclone), more filter area

**Equipment**:
- Spindle issues: Vibration, noise → check runout, bearings, dust ingression
- Coolant problems: No flow, foaming → check pump, filter, concentration

**Optimization**:
- Long cycle times: Conservative parameters → increase feed/DOC incrementally
- Excessive tool wear: Incorrect parameters → optimize feeds/speeds, check setup

**Emergency Response**:
- Fire: ABC extinguisher for small fires, evacuate for large
- Dust explosion: Evacuate immediately, prevention critical (housekeeping)

**Systematic Approach**:
1. Define problem (measurement, observation)
2. Check setup (tool, offsets, clamping)
3. Check machine (accuracy, maintenance)
4. Check process (parameters, tool path)
5. Document (build knowledge base)

**Next**: Conclusion and future trends in advanced materials machining

---

**Next**: [17.12 Conclusion and Future Trends](section-17.12-conclusion.md)
