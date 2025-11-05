# 17.10 Maintenance and Tool Management for Advanced Materials

## Tool Wear Characteristics

### Composite Machining Tool Wear

**Abrasive Wear** (dominant mechanism):
- Carbon fibers: 10× harder than aluminum (Mohs 6-7)
- Glass fibers: Very abrasive (Mohs 5-6)
- Aramid fibers (Kevlar): Less abrasive but fibrous (difficult to cut cleanly)

**Wear Progression**:
1. **New tool**: Sharp edge, clean cuts
2. **Initial wear** (5-20% tool life): Edge radius increases slightly
   - Quality still acceptable
   - Cutting forces increase ~10%
3. **Accelerated wear** (20-80% tool life): Visible flank wear
   - Surface finish degrades
   - Forces increase 20-40%
4. **End of life** (80-100%): Rapid quality loss
   - Delamination, fuzzing
   - Burning (heat from friction)
   - Catastrophic failure possible (chip breakage)

**Tool Life Examples**:

| Material | Tool | Operation | Parts Before Replacement |
|----------|------|-----------|--------------------------|
| CFRP | Carbide endmill | Slotting | 50-150 |
| CFRP | Diamond-coated compression | Trimming | 500-2000 |
| GFRP | Carbide endmill | Profiling | 100-300 |
| GFRP | PCD endmill | Production routing | 5000-15000 |

**Factors Affecting Tool Life**:
- Fiber type: Carbon = moderate wear, Glass = high wear, Aramid = low wear but poor cut quality
- Fiber content: 60% fiber volume ≈ 2× wear vs 40%
- Layer thickness: Thick layers = less delamination stress
- Cutting speed: Higher speed = more heat = shorter life
- Tool coating: Diamond coating increases life 10-20×

### Ceramic Machining Tool Wear

**Grinding Wheel Wear**:

**Mechanisms**:
1. **Grain fracture**: Diamond particles break (self-sharpening)
2. **Bond wear**: Bonding material erodes, particles fall out
3. **Glazing**: Particles dull but don't fracture (wheel loads)

**Wear Rate**:
- G-ratio (grinding ratio): Volume material removed / volume wheel wear
- Diamond on alumina: G-ratio 1000-10000 (excellent)
- Diamond on SiC: G-ratio 100-500 (lower, SiC extremely hard)

**Example**:
- Grinding alumina
- Material removed: 1.0 in³
- Wheel wear: 0.001 in³
- G-ratio: 1000
- Wheel life: 1000 in³ material per 1 in³ wheel (months of grinding)

**Dressing** (wheel sharpening):
- Required when: Wheel glazes (dull), loading (pores filled with debris)
- Frequency: Every 10-100 parts (depends on material, conditions)
- Method: Single-point diamond dresser
- Removes thin layer of wheel (exposes fresh diamonds)

**Wheel Life**: 500-5000 dressings before replacement (bond worn away)

## Tool Inspection and Monitoring

### Visual Inspection

**Composites**:

**Inspection Intervals**:
- Initial: Every 10 parts
- Once pattern established: Every 50 parts or 2 hours

**What to Look For**:

**Flank Wear** (cutting edge):
- Bright, worn flat behind edge
- Measure width (wear land)
- Acceptable: <0.005-0.010" (depends on application)
- Replace when: >0.015"

**Chipping**:
- Small chips missing from cutting edge
- Causes immediate quality loss
- Replace immediately

**Built-up Edge** (BUE):
- Resin accumulated on cutting edge
- Dulls tool, causes poor finish
- Clean with solvent (acetone)
- If returns quickly → tool too hot (reduce speed)

**Tool** for Inspection:
- 10-20× magnifier or USB microscope
- Good lighting
- Compare to new tool (reference photo)

**Ceramics** (grinding wheels):

**Visual Check**:
- **Glazed surface**: Shiny, smooth (should be slightly rough)
  - Solution: Dress wheel
- **Loading**: Pores filled with ceramic debris
  - Solution: Dress wheel, check coolant flow
- **Cracks**: Radial cracks in wheel (dangerous!)
  - Solution: Replace immediately (burst risk)

**Ring Test** (wheel integrity):
- Suspend wheel by hole (string)
- Tap with plastic hammer
- Sound: Clear ring = good, dull thud = cracked
- Frequency: Before mounting, weekly during use

### Dimensional Monitoring

**Tool Wear Trending**:

**Process**:
1. Measure critical dimension (first part after tool change)
2. Measure same dimension every N parts
3. Plot dimension vs part number
4. Trend line shows wear rate
5. Predict when tool reaches end of life

**Example** (CFRP hole drilling):
- Specification: 0.250 ±0.002" diameter
- Hole grows as drill wears (cutting edge erodes)

| Part Number | Hole Diameter | Status |
|-------------|---------------|--------|
| 1 (new drill) | 0.2495" | Good |
| 25 | 0.2500" | Good |
| 50 | 0.2505" | Good |
| 75 | 0.2512" | Warning (approaching limit) |
| 100 | 0.2521" | **Out of tolerance** |

**Wear rate**: 0.0026" per 100 parts
**Tool life**: ~70 parts (conservative replacement point)

**Benefit**: Prevents scrap (replace before out-of-tolerance)

### Force/Current Monitoring

**Spindle Load Monitoring**:
- CNC controller measures spindle motor current
- Dull tool → higher cutting forces → higher current
- Set threshold (e.g., 120% of new tool current)
- Alarm when exceeded

**Example**:
- New tool current: 8.5 A (average during cut)
- Threshold: 10.2 A (120%)
- Part 60: Current 10.5 A → alarm → inspect tool

**Advantages**:
- Automatic (no manual inspection)
- Real-time (immediate notification)
- Prevents quality issues

**Limitations**:
- Requires CNC with load monitoring
- Must establish baseline (new tool)
- Feed rate variations affect reading

## Tool Inventory Management

### Tool Identification

**Labeling System**:
- Tool number (unique ID)
- Tool type (e.g., "0.250 CFRP drill")
- Purchase date
- First use date
- Part count (cumulative)

**Example Label**:
```
Tool #: C-042
Type: 1/4" carbide drill, 118° point
Material: CFRP
Purchased: 2024-01-15
First Use: 2024-01-20
Parts Machined: 237
Status: In service (limit 300 parts)
```

**Tracking Methods**:
- Spreadsheet: Simple, manual
- Tool management software: Automatic (scans barcode, logs use)
- ERP integration: Links tool use to jobs (cost accounting)

### Stock Levels

**Determine Par Levels**:

$$\text{Par Level} = \text{Weekly Usage} \times \text{Lead Time (weeks)} \times \text{Safety Factor}$$

**Example** (PCD router bit for CFRP):
- Weekly usage: 2 bits (production rate ÷ tool life)
- Lead time: 3 weeks (order to delivery)
- Safety factor: 2× (avoid stockouts)
- **Par level**: 2 × 3 × 2 = **12 bits**

**When stock drops below par**: Reorder

**Cost Trade-off**:
- Too much inventory: Cash tied up, tools expire (carbide doesn't, but resharpenable tools degrade)
- Too little inventory: Production stops (lost revenue)

### Tool Cost Tracking

**Cost Per Part**:

$$\text{Tool Cost Per Part} = \frac{\text{Tool Price}}{\text{Parts Per Tool}}$$

**Example**:
- Diamond-coated compression cutter: $120
- Tool life: 1500 parts
- **Cost per part**: $120 / 1500 = **$0.08**

**Compare to Alternative**:
- Carbide compression cutter: $30
- Tool life: 150 parts
- **Cost per part**: $30 / 150 = **$0.20**

**Diamond cutter 60% cheaper per part** (despite 4× higher initial cost)

**Total Cost** includes:
- Tool purchase price
- Regrinding cost (if resharpenable)
- Downtime for tool changes (labor)
- Scrap from worn tools

## Tool Reconditioning

### Resharpening Carbide Tools

**Candidates**:
- Endmills, drills (simple geometry)
- Significant material remaining (not chipped away)
- Cost-effective if tool >$50 (resharpening ~$15-30)

**Process**:
- Send to tool grinding service
- Grind flutes, cutting edges back to new geometry
- Inspect, measure (diameter reduced by 0.005-0.020")
- Apply new coating (optional, extends life)

**Regrind Count**:
- Typical: 2-5 regrinds before tool too small
- 1/4" endmill: Can regrind to ~0.230" (0.015" under)

**Cost Savings**:
- New 1/4" carbide endmill: $50
- Regrind: $20
- **Savings**: $30 per regrind × 3 regrinds = $90 savings over tool life

**Not Recommended**:
- PCD tools (diamond cannot be easily reground)
- Severely worn tools (more material to remove than cost-effective)

### Diamond Tool Refurbishment

**PCD Tools**:
- Grinding PCD requires specialized equipment (diamond wheels, EDM)
- Expensive ($100-300 per regrind)
- Only economical for large, expensive tools (>$500)

**Diamond-Coated Tools**:
- Cannot regrind (coating only a few microns thick)
- Once worn → discard
- Some suppliers: Recoating service (strip old coating, reapply)
  - Cost: 40-60% of new tool price
  - Quality variable (coating adhesion issues possible)

## Machine Maintenance for Advanced Materials

### Spindle Maintenance

**Challenges**:
- Fine dust ingests into bearings (abrasive wear)
- Carbon fiber conductive (can short windings)
- High-speed operation (thermal expansion, vibration)

**Preventive Maintenance**:

**Air Purge System**:
- Positive pressure (clean, filtered air) blown into spindle housing
- Pressure: 5-15 PSI
- Flow rate: 5-10 CFM
- Prevents dust entry (air flows out through seals)

**Seal Replacement**:
- Frequency: Annually or per manufacturer (composites/ceramics accelerate wear)
- Signs of wear: Dust inside spindle housing, increased spindle temperature
- Cost: $200-1000 (seals + labor)

**Bearing Inspection**:
- Frequency: Per manufacturer schedule (1000-5000 hours typical)
- Check: Play (radial/axial runout), noise, temperature
- Replace if: Runout >0.0002", noisy, hot (>140°F in operation)

**Rebuild Cost**: $2,000-20,000 (depends on spindle size)

**Extend Spindle Life**:
- Excellent dust collection (minimize ingestion)
- Air purge system (mandatory for ceramics)
- Avoid overheating (proper speeds, sharp tools, coolant)
- Gentle handling (no impacts, avoid crash)

### Way and Ballscrew Protection

**Threats**:
- Abrasive dust (ceramic, glass fiber) acts as grinding compound
- Settles on ways → ballscrew ingests → rapid wear

**Protection**:

**Bellows/Covers**:
- Accordion-style covers over ways (X, Y, Z axes)
- Prevent dust settling on guideways
- Inspect for tears (dust enters through holes)
- Replace annually or as needed

**Wipers**:
- Scraper at carriage/table (wipes dust off ways)
- Made of plastic or felt
- Inexpensive, replace quarterly

**Lubrication**:
- Increase frequency (dust contaminates oil)
- Composites/ceramics: Daily way oiling (vs weekly for metals)
- Use centralized lube system (automatic, consistent)

**Inspection**:
- Weekly: Check for dust accumulation on ways (vacuum if present)
- Monthly: Check ballscrew (rotate by hand, feel for roughness)

**Ballscrew Replacement**: $1,000-10,000 per axis (expensive!)

### Coolant System Maintenance

**Coolant Contamination**:
- Ceramic dust settles in tank (sludge)
- Composite dust floats (scum on surface)
- Bacteria growth (water-based coolants)

**Maintenance**:

**Daily**:
- Skim surface (remove floating debris)
- Check level (top off if low)

**Weekly**:
- Measure concentration (refractometer)
  - Too dilute: Poor lubrication, bacteria growth
  - Too concentrated: Waste, possible residue
  - Target: Per manufacturer (typically 5-10%)
- Measure pH
  - Target: 8.5-9.5 (alkaline inhibits bacteria)
  - Low pH: Add fresh concentrate

**Monthly**:
- Clean tank (remove sludge)
- Inspect pump, filters
- Replace filters if clogged

**Quarterly** (or sooner if contaminated):
- Drain tank completely
- Clean tank, piping (remove biofilm)
- Refill with fresh coolant

**Alternative**: Dry machining or MQL (minimal quantity lubrication)
- Eliminates coolant maintenance
- Good for composites (dust suppression less critical than metals)
- Ceramics: Water spray for cooling, dust suppression

### Dust Collection System Maintenance

**Daily**:
- Empty dust hopper (don't let overfill)
- Check pressure drop gauge (clean filter if high)

**Weekly**:
- Pulse-clean filters (manual if no automatic system)
- Inspect ductwork (loose connections, clogs)

**Monthly**:
- Inspect filter cartridges (tears, excessive loading)
- Check blower (unusual noise, vibration)

**Quarterly**:
- Replace intake filters (control cabinet)
- Inspect blower impeller (dust buildup)

**Annually**:
- Replace filter cartridges (even if pressure OK, efficiency degrades)
- Blower maintenance (bearings, belts)

**Cost**: $150-900/year (filters), $200-500 (blower maintenance)

## Preventive Maintenance Schedule

### Daily Tasks (Operator)

- [ ] Vacuum machine surfaces (HEPA vac)
- [ ] Empty dust collector hopper
- [ ] Wipe control panel (damp cloth)
- [ ] Check coolant level
- [ ] Inspect tools (visual, magnifier)

**Time**: 10-15 minutes

### Weekly Tasks (Operator/Technician)

- [ ] Clean machine thoroughly (remove guards, vacuum inside)
- [ ] Check coolant concentration, pH
- [ ] Inspect way covers (tears)
- [ ] Pulse-clean dust collector filters
- [ ] Check dust collection pressure drop
- [ ] Review tool wear logs (trending)

**Time**: 30-60 minutes

### Monthly Tasks (Technician)

- [ ] Deep clean coolant tank (remove sludge)
- [ ] Inspect ballscrews (rotate, check for rough spots)
- [ ] Grease ballscrew bearings (if required)
- [ ] Inspect spindle seals (look inside housing for dust)
- [ ] Check machine level (spirit level on table, ways)
- [ ] Test interlocks (door switches, E-stop)

**Time**: 2-4 hours

### Quarterly Tasks (Technician)

- [ ] Replace control cabinet intake filters
- [ ] Inspect/clean dust collection blower impeller
- [ ] Replace coolant entirely (drain, clean tank, refill)
- [ ] Inspect/replace way wipers
- [ ] Lubricate machine (detailed per manual: hinges, latches, etc.)

**Time**: 4-8 hours

### Annual Tasks (Specialist)

- [ ] Replace dust collector filter cartridges
- [ ] Spindle seal replacement
- [ ] Spindle bearing inspection (runout, play, noise)
- [ ] Ballscrew backlash measurement
- [ ] Laser alignment check (if available)
- [ ] Electrical connections inspection (tighten, check for corrosion)

**Time**: 8-16 hours

**Cost** (parts + labor): $2,000-5,000 per machine

## Tool Storage and Organization

### Storage Conditions

**Temperature**: Room temperature (60-80°F)
- Extreme temperatures: Epoxy bonding (PCD) can fail

**Humidity**: Low (<50% RH)
- High humidity: Carbide corrosion (cobalt binder rusts)
- Store in desiccant cabinet (silica gel packs)

**Protection**:
- Individual tool boxes (plastic tubes)
- Foam inserts (prevent tools contacting each other)
- Never: Loose in drawer (edges chip)

### Organization System

**Shadow Board**:
- Outline of each tool drawn on board
- Tool hangs in specific spot
- Missing tool immediately visible
- Good for frequently used tools

**Tool Crib**:
- Locked cabinet
- Tools checked out (logged)
- Enforces inventory tracking
- Reduces loss/theft

**Color Coding** (material-specific tools):
- Blue labels: Aluminum tools (don't use on composites)
- Red labels: Composite tools
- Yellow labels: Ceramic tools (diamond)
- Prevents cross-contamination (aluminum chips on composite = corrosion)

## Cost-Benefit Analysis

### Preventive Maintenance ROI

**Cost of Prevention**:
- Labor: 50 hours/year @ $40/hour = $2,000
- Parts: Filters, seals, coolant = $1,000
- **Total**: $3,000/year

**Cost of Reactive Maintenance** (failure-based):
- Spindle failure: $10,000 (rebuild) + $5,000 (downtime)
- Ballscrew replacement: $5,000 + $2,000 (downtime)
- Probability without PM: 10-20% per year
- **Expected cost**: $15,000 × 15% = $2,250/year

**Breakeven**: But doesn't include:
- Lost production (downtime for emergency repairs)
- Scrap (worn tools produce bad parts before caught)
- Reputation damage (late deliveries)

**Realistic ROI**: 3:1 to 5:1 (every $1 spent on PM saves $3-5 in reactive costs)

### Tool Management ROI

**Without Tool Management**:
- Replace tools when they break or quality issues occur
- 5-10% scrap from worn tools (not caught in time)
- Downtime: 30 min per tool failure (find replacement, load, restart)

**With Tool Management**:
- Replace tools at 70-80% of life (before failure)
- Scrap: 1-2% (proactive replacement)
- Downtime: Planned (during shift breaks)

**Example** (small shop, $200k/year revenue):
- Scrap reduction: 5% → 1.5% (saves 3.5%)
- $200k × 3.5% = **$7,000/year saved**
- Tool management cost: 2 hours/week × $30/hour × 50 weeks = $3,000/year
- **Net benefit**: $4,000/year

**Payback**: Immediate (first year)

## Summary

Effective tool and machine maintenance is critical for advanced materials machining:

**Tool Wear**:
- Composites: Abrasive fibers wear tools rapidly (50-2000 parts typical)
- Ceramics: Grinding wheels last long but require dressing (G-ratio 100-10000)
- Monitor: Visual inspection (wear land), dimensional trending, force monitoring

**Tool Management**:
- Inventory: Track usage, maintain par levels (avoid stockouts)
- Cost tracking: Tool cost per part (diamond often cheaper than carbide long-term)
- Resharpening: Carbide tools 2-5 regrinds ($20-30 per regrind)

**Machine Maintenance**:
- Spindle: Air purge system (prevents dust ingestion), annual seal replacement
- Ways/ballscrews: Covers, wipers, frequent lubrication
- Coolant: Clean weekly, replace quarterly (bacteria growth)
- Dust collection: Daily hopper emptying, annual filter replacement

**Preventive Maintenance**:
- Daily (10-15 min): Vacuum, empty dust collector, inspect tools
- Monthly (2-4 hours): Deep clean, inspect seals, test interlocks
- Annual (8-16 hours): Replace filters, seals, bearings
- Cost: $3,000/year (saves $10,000+ in reactive repairs)

**ROI**:
- Preventive maintenance: 3:1 to 5:1 return
- Tool management: $4,000/year savings (small shop example)
- Avoiding spindle failure alone justifies program

**Next**: Troubleshooting common problems in advanced materials machining

---

**Next**: [17.11 Troubleshooting Common Issues](section-17.11-troubleshooting.md)
