# 20.8 Coolant and Chip Management

## Functions of Coolant

Coolant (also called cutting fluid) serves multiple critical functions:

### 1. Cooling

**Primary function**: Remove heat from cutting zone

**Heat generation**:
- 60-80% carried away by chip
- 10-20% absorbed by tool
- 10-20% enters workpiece
- Coolant intercepts heat before it damages tool or workpiece

**Temperature reduction**:
- Flood coolant: Reduces cutting temperature 200-400°F
- Tool life improvement: 2-5× (due to exponential wear/temperature relationship)

### 2. Lubrication

**Reduces friction**:
- Between chip and tool rake face (secondary shear zone)
- Between tool flank and workpiece (tertiary zone)

**Results**:
- Lower cutting forces (10-30% reduction)
- Better surface finish
- Reduced tool wear

**Most effective at low speeds** (<200 SFM):
- Longer contact time allows lubrication
- High speeds: Cooling function dominates (less time for lubrication)

### 3. Chip Flushing

**Evacuates chips** from cutting zone:
- Prevents chip recutting (surface finish)
- Prevents chip packing (tool breakage)
- Clears view for operator
- Critical in drilling (deep holes)

**Pressure matters**:
- Low pressure (gravity flow): Minimal flushing
- Medium pressure (50-100 PSI): Good flushing
- High pressure (300-1000 PSI): Excellent flushing, breaks chips

### 4. Corrosion Protection

**Protects metal surfaces**:
- Prevents rust on steel parts
- Protects machine ways and surfaces
- Maintains clean appearance

**Rust inhibitors** added to coolant formulations

## Types of Coolant

### Straight Oils (Mineral Oils)

**Composition**:
- Petroleum-based oil
- Additives: Sulfur, chlorine, phosphorus (extreme pressure)

**Properties**:
- Excellent lubrication
- Moderate cooling
- No mixing required (use straight)

**Applications**:
- Low-speed operations (tapping, threading, broaching)
- Difficult materials (stainless, titanium)
- Gear cutting, form tools
- Heavy-duty operations

**Advantages**:
- Best lubrication
- Good tool life
- No mixing issues

**Disadvantages**:
- Poor cooling vs water-based
- Smoke/mist at high speeds
- Fire hazard above 400°F
- Disposal issues
- Expensive

**Typical use**: 5-10% of metalworking operations

### Soluble Oils (Emulsifiable Oils)

**Composition**:
- Mineral oil (60-90%)
- Emulsifiers (allow mixing with water)
- Mixed with water at 5-20% concentration

**Properties**:
- Good lubrication (from oil)
- Good cooling (from water)
- Milky appearance when mixed

**Mixing ratios**:
- Heavy duty: 1:4 to 1:10 (oil:water) = 10-20%
- General purpose: 1:10 to 1:20 = 5-10%
- Light duty: 1:20 to 1:40 = 2.5-5%

**Applications**:
- General machining (milling, turning, drilling)
- Steel, aluminum, cast iron
- Most versatile coolant type

**Advantages**:
- Balance of cooling and lubrication
- Lower cost than straight oil
- Fire-safe (water-based)
- Easy to monitor (visual)

**Disadvantages**:
- Requires mixing and maintenance
- Bacterial growth (requires biocide)
- Separates over time (requires mixing)

**Typical use**: 50-60% of operations

### Semi-Synthetic Fluids

**Composition**:
- Small amount of mineral oil (2-30%)
- Chemical additives for lubrication
- Water-based
- Translucent to semi-transparent

**Properties**:
- Better cooling than soluble oils
- Good lubrication from additives
- Longer sump life
- Resistant to bacterial growth

**Mixing ratios**:
- 1:10 to 1:40 (typically 1:20) = 5%

**Applications**:
- General machining
- Aluminum (excellent choice)
- High-speed operations
- Grinding operations

**Advantages**:
- Excellent cooling
- Good lubrication
- Long sump life (3-6 months)
- Less bacteria than soluble oils
- Clean (no oil residue)

**Disadvantages**:
- More expensive than soluble oils
- Skin irritation (some users)
- Harder to monitor concentration

**Typical use**: 30-40% of operations

### Synthetic Fluids

**Composition**:
- No petroleum oil (water + chemical additives only)
- Synthetic lubricants and corrosion inhibitors
- Clear solution

**Properties**:
- Excellent cooling (highest of all)
- Moderate lubrication (chemical-based)
- Very long sump life (6-12 months)
- Excellent bacterial resistance

**Mixing ratios**:
- 1:20 to 1:100 = 1-5%

**Applications**:
- Grinding operations (cooling critical)
- High-speed machining
- Aluminum (excellent choice)
- Light-duty operations

**Advantages**:
- Best cooling performance
- Longest sump life
- Clean (no oil residue)
- Minimal bacterial growth
- Easy to see work (clear)

**Disadvantages**:
- Poorest lubrication
- Most expensive
- Not suitable for heavy cuts or difficult materials
- Staining issues on some metals

**Typical use**: 5-10% of operations

## Coolant Selection Guide

| Operation | Material | Recommended Coolant |
|-----------|----------|---------------------|
| High-speed milling | Aluminum | Semi-synthetic or synthetic |
| General milling | Steel | Soluble oil or semi-synthetic |
| Turning | Steel, stainless | Soluble oil |
| Drilling | All | Soluble oil (through-spindle) |
| Tapping | All | Straight oil or soluble oil (20%) |
| Threading | All | Straight oil |
| Grinding | All | Synthetic or semi-synthetic |
| Titanium | Titanium | Straight oil (never water-based) |
| Magnesium | Magnesium | Mineral oil (never water-based) |

**Special cases**:
- **Cast iron**: Dry cutting preferred (graphite self-lubricates)
- **Titanium**: Water-based causes fire risk and hydrogen embrittlement
- **Magnesium**: Water-based causes violent fire (burns at 3100°F)

## Coolant Delivery Methods

### Flood Cooling

**Description**: High-volume coolant flow over cutting area

**Flow rates**:
- Small machines: 1-5 GPM (gallons per minute)
- Large machines: 10-50 GPM

**Pressure**:
- Typical: 50-100 PSI (gravity + pump)
- High-pressure: 300-1000 PSI (optional)

**Advantages**:
- Excellent cooling
- Good chip flushing
- Covers large area
- Simple system

**Disadvantages**:
- Messy (splash, mist)
- Large sump required (30-100 gallons)
- Maintenance intensive
- Environmental concerns (disposal)

**Applications**: General production machining, most CNC operations

### Mist Cooling

**Description**: Atomized coolant mixed with compressed air

**Delivery**:
- Air pressure: 60-100 PSI
- Coolant flow: 2-20 ml/hour
- Creates fine mist

**Advantages**:
- Minimal coolant consumption
- Clean (little splash)
- Good visibility
- Small sump (1-5 gallons)

**Disadvantages**:
- Inhalation hazard (requires extraction)
- Poor chip flushing
- Limited cooling vs flood
- Not for heavy cuts

**Applications**: Light-duty milling, engraving, hobbyist machines

**Safety**: **Mist extraction system mandatory** (respiratory hazard)

### Minimum Quantity Lubrication (MQL)

**Description**: Micro-droplets of lubricant in air stream

**Delivery**:
- Flow rate: 2-50 ml/hour (extremely low)
- Air pressure: 60-90 PSI
- Directed at cutting edge

**Advantages**:
- Virtually dry machining (minimal fluid)
- No disposal issues
- Clean parts (no washing)
- Environmentally friendly
- Cost savings (minimal fluid consumption)

**Disadvantages**:
- Limited cooling (air blast only)
- Requires extraction
- More expensive equipment
- Not for all materials/operations

**Applications**:
- Aluminum machining
- Titanium (with straight oil)
- High-speed machining
- Environmentally sensitive operations

**Best results with**:
- High cutting speeds (less heat generation per unit)
- Sharp tools
- Light to moderate DOC

### Through-Tool (Through-Spindle) Coolant

**Description**: Coolant pumped through hollow tool, exits at cutting edge

**Pressure**:
- Standard: 300-500 PSI
- High-pressure: 1000-1500 PSI

**Advantages**:
- Excellent cooling at cutting edge
- Superior chip evacuation (drilling)
- Breaks chips (high pressure)
- Works in blind holes

**Disadvantages**:
- Requires special tooling (hollow tools)
- High-pressure pump needed ($3k-10k)
- Machine must support through-spindle coolant
- Higher tool cost

**Applications**:
- Deep hole drilling (> 3× diameter)
- Gun drilling
- Tapping (excellent chip clearing)
- High-performance machining

**Performance**:
- Tool life improvement: 50-200% in drilling
- Enables deeper holes (10× diameter possible)
- Faster speeds and feeds

### Dry Machining

**Description**: No coolant used

**Advantages**:
- No coolant cost
- No disposal cost
- Clean parts (no washing)
- No coolant-related health issues
- Environmentally friendly

**Disadvantages**:
- Limited tool life (no cooling)
- Lower speeds required
- Not suitable for all materials
- Heat in workpiece (distortion risk)

**When appropriate**:
- **Cast iron** (graphite self-lubricates - preferred!)
- **Aluminum** (good thermal conductivity, with air blast)
- **Brass** (free-machining, low forces)
- Finishing operations (light cuts, less heat)

**Requirements for success**:
- Coated tools (TiAlN)
- High cutting speeds (less time for heat transfer)
- Air blast for chip clearing
- Proper chip evacuation

## Coolant Concentration and Maintenance

### Measuring Concentration

**Why important**:
- Too dilute: Poor lubrication, corrosion, bacteria growth
- Too concentrated: Waste, residue, skin irritation, foaming

**Refractometer method** (most accurate):
- Measures refractive index of fluid
- Read Brix scale
- Convert to concentration using coolant factor
- Example: Read 5.0° Brix, factor = 1.0, concentration = 5%

**Measuring frequency**:
- Daily: High-use machines
- Weekly: General machines
- After adding water or coolant

**Correcting concentration**:
- Too dilute: Add concentrated coolant
- Too concentrated: Add water (soft water preferred)

### pH Management

**Target pH**: 8.5-9.5 (alkaline)

**Why important**:
- pH < 8.0: Bacterial growth, corrosion risk
- pH > 10.0: Skin irritation, foam, shortened sump life

**Measuring**: pH test strips or pH meter

**Correcting pH**:
- Too low: Add biocide (kill bacteria) or alkaline buffer
- Too high: Dilute with water or add buffer

### Bacterial Control

**Problem**: Water-based coolants support bacterial growth
- Smells: Rotten egg smell (sulfur bacteria)
- Appearance: Slime, discoloration
- pH drops: Bacteria produce acids

**Prevention**:
- Maintain proper concentration (bacteria thrive when dilute)
- Good aeration (bacteria are often anaerobic)
- Clean sump regularly
- Remove tramp oil (floating oil feeds bacteria)

**Treatment**:
- Biocides: Add per manufacturer spec
- Pasteurization: Heat coolant to 160°F for 30 minutes
- Replacement: Last resort if severe contamination

**Frequency**:
- Biocide: Every 2-4 weeks (preventive)
- Sump cleaning: Every 3-6 months

### Tramp Oil Removal

**Tramp oil**: Hydraulic oil, way oil, slideway oil contaminating coolant

**Problems**:
- Feeds bacterial growth
- Reduces cooling effectiveness
- Smoke/mist generation
- Shortened sump life

**Removal methods**:
- Skimmer: Floating belt or disk removes oil from surface
- Coalescer: Filters fine oil droplets
- Manual: Skim with absorbent pads

**Prevention**: Regular machine maintenance (stop leaks)

## Chip Management

### Chip Formation

**Ideal chips**: Short, broken segments (easy to handle, good evacuation)

**Problem chips**:
- Long, stringy chips (tangle, safety hazard)
- Fine dust (inhalation, fire/explosion risk)
- Hot chips (burn risk)

**Chip control methods**:
1. **Chip breaker geometry** on tool (most important)
2. **Proper coolant** (pressure breaks chips)
3. **Feed rate** (heavier feed = thicker, more brittle chips)
4. **Material properties** (brittle materials break naturally)

### Chip Breakers

**Function**: Force chip to curl tightly and fracture

**Types**:
- Form ground: Groove in rake face
- Clamped: Separate chip breaker piece
- Geometry: Built into insert design

**Selection**:
- Aggressive (deep groove): Heavy cuts, soft materials, long chips
- Moderate: General purpose
- Light (shallow groove): Finishing, hard materials, thin chips

**Material-specific**:
- Steel: Chip breakers very effective
- Aluminum: Less effective (ductile, soft)
- Cast iron: Not needed (brittle chips naturally)
- Stainless: Critical (gummy, stringy chips)

### Chip Evacuation

**Importance**:
- Prevents chip recutting (finish)
- Prevents chip packing (tool breakage)
- Allows coolant access to cutting zone
- Safety (keeps work area clear)

**Methods**:

**1. Gravity** (simplest):
- Machine bed slopes to chip pan
- Effective for heavy chips (steel, cast iron)
- Not effective for fine chips (aluminum)

**2. Coolant flushing**:
- High flow rate washes chips away
- Direction matters (aim chips toward drain)
- Through-tool coolant excellent for drilling

**3. Air blast**:
- Compressed air directed at cutting zone
- Effective for dry machining
- Caution: Creates airborne particles (extraction needed)

**4. Auger conveyors**:
- Screw conveyor in chip pan
- Moves chips to collection point
- Common on production machines

**5. Chip conveyor belts**:
- Hinged steel belt or magnetic belt
- Continuous removal from sump
- Separates chips from coolant (returns coolant)

**In drilling**:
- **Peck cycle**: Retract frequently to break and evacuate chips
- **Through-tool coolant**: Flushes chips out of hole
- **Chip breaker geometry**: Breaks long chips into segments

### Chip Disposal

**Volume**: Significant in production (hundreds of pounds per day)

**Options**:

**1. Scrap metal recycling**:
- Steel, aluminum, brass have scrap value
- Cleaner chips = higher value
- Dry chips more valuable (no coolant)

**2. Chip processing**:
- Centrifuge: Removes coolant (recovers coolant)
- Briquetting: Compresses chips into dense blocks
- Result: Easier transport, higher scrap value

**3. Waste disposal**:
- Chips with coolant = hazardous waste (expensive)
- Dry chips = metal scrap (value)
- **Incentive for dry machining or MQL**

**Safety**:
- Sharp chips (cut risk - use gloves, tools)
- Hot chips (burn risk - allow cooling)
- Never handle with bare hands while machine running
- Fire risk (magnesium, titanium fine chips)

## Safety Considerations

### Coolant Health Hazards

**Skin contact**:
- Dermatitis (irritation, rash)
- Bacterial contamination risk
- Chemical sensitivity

**Prevention**:
- Barrier cream before work
- Wash hands frequently
- Avoid prolonged contact
- Use gloves for chip handling

**Inhalation**:
- Mist/vapor from high-speed cutting
- Bacterial aerosols (legionella risk)
- Chemical irritants

**Prevention**:
- Mist collection system
- Good ventilation
- Regular coolant maintenance (control bacteria)

**Ingestion** (rare):
- Splashing into mouth
- Eating with contaminated hands

**Prevention**:
- Wash hands before eating
- No food/drink in machine area

### MSDS / SDS

**Material Safety Data Sheet**: Required for all coolants

**Contains**:
- Chemical composition
- Health hazards
- First aid procedures
- Handling and storage
- Disposal requirements
- Emergency contact

**Read and understand** before using any coolant.

### Fire Hazards

**Straight oils**:
- Flammable (flash point 300-450°F)
- Can ignite at high cutting temperatures
- Fire extinguisher accessible

**Water-based coolants**:
- Non-flammable (water-based)
- Safer for high-speed operations

**Special cases**:
- **Magnesium**: Water-based coolant causes violent fire
  - Use mineral oil only
  - Class D extinguisher required
- **Titanium**: Fine chips pyrophoric (self-ignite)
  - Never allow chip accumulation
  - Mineral oil only (water causes fire)

## Troubleshooting

### Problem: Poor Tool Life

**Possible causes**:
1. Insufficient cooling (dilute coolant)
2. Wrong coolant type (lubrication inadequate)
3. Low flow rate (not reaching cutting zone)

**Solutions**:
- Check concentration, increase if low
- Switch to soluble oil or straight oil (better lubrication)
- Increase flow rate, direct nozzle at cutting edge

### Problem: Poor Surface Finish

**Possible causes**:
1. Chip recutting (poor flushing)
2. Built-up edge (inadequate lubrication)
3. Coolant contamination (swarf, bacteria)

**Solutions**:
- Improve coolant direction and flow
- Increase concentration or switch to better lubricating coolant
- Clean and filter coolant

### Problem: Coolant Odor

**Cause**: Bacterial growth (anaerobic bacteria produce H₂S)

**Solutions**:
- Add biocide
- Increase concentration (bacteria thrive when dilute)
- Improve aeration (skim off floating oil, circulate coolant)
- Clean sump thoroughly
- If severe: Replace coolant

### Problem: Foaming

**Causes**:
1. Too concentrated
2. Contamination (detergent, soap)
3. Soft water (excessive)

**Solutions**:
- Dilute to proper concentration
- Avoid contamination (clean tools before using)
- Add defoamer (small amount)
- Change coolant if severe

### Problem: Rust on Parts

**Causes**:
1. Insufficient concentration (corrosion inhibitors diluted)
2. Low pH (acidic = corrosion)
3. Coolant aged (additives depleted)

**Solutions**:
- Increase concentration
- Check and correct pH (target 8.5-9.5)
- Replace coolant if old (>6 months)
- Dry parts promptly after machining

## Summary

**Coolant functions**:
1. Cooling (temperature control, tool life)
2. Lubrication (reduce forces, improve finish)
3. Chip flushing (evacuation, visibility)
4. Corrosion protection

**Coolant types**:
- **Straight oil**: Best lubrication, low-speed operations
- **Soluble oil**: Versatile, general machining
- **Semi-synthetic**: Good balance, aluminum, high-speed
- **Synthetic**: Best cooling, grinding, least lubrication

**Delivery methods**:
- **Flood**: Standard for production
- **Mist/MQL**: Clean alternative, requires extraction
- **Through-tool**: Best for drilling, tapping
- **Dry**: Cast iron preferred, environmentally friendly

**Maintenance essentials**:
- Monitor concentration (refractometer)
- Check pH weekly (target 8.5-9.5)
- Control bacteria (biocide, cleanliness)
- Remove tramp oil
- Replace coolant 2-4× per year

**Chip management**:
- Chip breakers on tools
- Adequate coolant flow
- Evacuation system (gravity, conveyor)
- Proper disposal (recycle dry chips)

**Safety priorities**:
- Skin protection (barrier cream, gloves)
- Mist extraction (inhalation risk)
- MSDS review (know hazards)
- Special materials (magnesium, titanium - fire risk)

**Economic benefits of proper coolant management**:
- 2-5× tool life improvement
- Better surface finish (less rework)
- Faster cutting speeds
- Reduced machine downtime

---

**Next**: [20.9 Troubleshooting and Optimization](section-20.9-troubleshooting.md)
