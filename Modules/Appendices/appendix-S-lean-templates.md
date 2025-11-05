# Appendix S – L.E.A.N. Strategy Templates and Tools

## Introduction

This appendix provides practical templates, forms, and tools to support implementation of L.E.A.N. (Least Effort Achieves Nothing) strategies in CNC manufacturing environments. These templates are designed to be customizable for your specific shop needs and can be adapted for different scales of operation.

**Complete Contents:**

**Section 1-5: Value Stream Mapping and Waste Analysis**
- Value Stream Mapping (VSM) Templates (Current & Future State)
- Eight Wastes (DOWNTIME) Assessment Tools
- Spaghetti Diagrams
- Process Observation Sheets
- Takt Time Calculators

**Section 6-10: Pull Systems and Kanban**
- Just-In-Time (JIT) System Design
- Kanban Card Templates and Calculations
- Supermarket Planning and Management
- Heijunka (Production Leveling)
- Pull System Metrics

**Section 11-14: Reliability and Continuous Improvement**
- SMED (Setup Reduction) Templates
- TPM (Total Productive Maintenance) Tools
- Poka-Yoke (Error-Proofing) Design
- Kaizen Event Planning and Execution

**Section 15-20: Visual Management and Implementation**
- Visual Management Systems and Andon
- Standardized Work Templates
- Lean Metrics Dashboards
- A3 Problem Solving
- Lean Implementation Roadmap
- Annual Planning Tools

---

## 1. Value Stream Mapping (VSM) Templates

### 1.1 Current State VSM Template

**Purpose:** Document the current flow of materials and information from customer order to delivery.

#### VSM Symbol Legend

```
┌─────────────┐
│  CUSTOMER   │  = External customer or supplier
└─────────────┘

┌─────────────┐
│   PROCESS   │  = Manufacturing process step
└─────────────┘

[PUSH]  →       = Push arrow (scheduled production)
        →       = Physical material flow
- - - →         = Information flow (electronic)
═════►          = Information flow (manual)

🏭               = Supplier or external source
📦               = Inventory (triangle with quantity/days)
⚡               = Kaizen burst (improvement opportunity)
📊               = Data box (cycle time, changeover, uptime, etc.)
```

#### Current State VSM Worksheet

**Product/Product Family:** _______________________
**Completed By:** ______________________ **Date:** __________
**Team Members:** _______________________________________________

**Step 1: Identify Customer Requirements**
- Annual Demand: __________ pieces/year
- Daily Demand: __________ pieces/day (working days: _____)
- Order Frequency: __________
- Delivery Requirements: __________
- Packaging Requirements: __________

**Step 2: Document Process Steps (Left to Right)**

| Step # | Process Name | Cycle Time (sec) | Changeover Time (min) | Uptime % | # Operators | Available Time (sec/shift) | EPE/Batch Size |
|--------|--------------|------------------|----------------------|----------|-------------|----------------------------|----------------|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |

**Step 3: Document Inventory Between Steps**

| Location | Quantity (pieces) | Days of Inventory | Storage Method |
|----------|-------------------|-------------------|----------------|
| Raw Material |  |  |  |
| After Step 1 |  |  |  |
| After Step 2 |  |  |  |
| After Step 3 |  |  |  |
| Finished Goods |  |  |  |

**Step 4: Document Information Flow**

- **Customer Order Entry Method:** ________________
- **Production Scheduling Method:** ________________
- **Schedule Frequency:** ________________
- **Material Release Method:** ________________
- **Communication Between Steps:** ________________

**Step 5: Calculate Timeline**

| Metric | Calculation | Value |
|--------|-------------|-------|
| Total Cycle Time | Sum of all process cycle times | _____ sec |
| Total Lead Time | Sum of cycle times + inventory wait times | _____ days |
| Process Time | Total cycle time only | _____ sec |
| Value-Added Ratio | Process time ÷ Lead time × 100% | _____ % |

**Step 6: Identify Waste and Improvement Opportunities**

Mark kaizen bursts (⚡) on your VSM for:
- Excessive inventory
- Long changeover times
- Poor communication
- Rework or quality issues
- Excessive transportation
- Waiting or delays

### 1.2 Future State VSM Template

**Purpose:** Design the ideal flow with waste eliminated and lean principles applied.

**Future State Design Questions:**

1. **What is the Takt Time?**
   - Takt Time = Available Time ÷ Customer Demand
   - Takt Time = __________ sec/piece
   - *This is the pace at which you must produce to meet customer demand*

2. **Where Can We Implement Continuous Flow?**
   - Can operations be combined or relocated?
   - List process steps that can flow continuously: __________________

3. **Where Do We Need Supermarkets (Pull Systems)?**
   - Which processes must remain disconnected?
   - Supermarket locations: __________________

4. **What Is the Pacemaker Process?**
   - Which single point will be scheduled?
   - Pacemaker: __________________

5. **How Will We Level Production (Heijunka)?**
   - Product mix strategy: __________________
   - Volume leveling approach: __________________

6. **What Process Improvements Are Required?**

| Improvement Area | Current State | Future State | Actions Required |
|------------------|---------------|--------------|------------------|
| Changeover Time |  |  |  |
| Cycle Time |  |  |  |
| Uptime/Reliability |  |  |  |
| Quality (FPY) |  |  |  |
| Batch Size |  |  |  |

**Future State Timeline:**

| Metric | Current State | Future State | Improvement |
|--------|---------------|--------------|-------------|
| Total Lead Time | _____ days | _____ days | _____ % |
| Process Time | _____ sec | _____ sec | _____ % |
| Value-Added Ratio | _____ % | _____ % | _____ % |
| Inventory (days) | _____ days | _____ days | _____ % |

### 1.3 VSM Implementation Plan

**Future State Target Date:** __________

| Kaizen/Improvement | Responsible | Target Date | Resources Needed | Status |
|--------------------|-------------|-------------|------------------|--------|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

## 2. Eight Wastes (DOWNTIME) Assessment Tools

### 2.1 DOWNTIME Waste Identification Checklist

**Assessment Date:** __________
**Assessed By:** __________
**Area/Process:** __________

Rate each waste area: 
- **0** = Not present
- **1** = Minor issue
- **2** = Moderate issue
- **3** = Significant issue
- **4** = Critical issue

#### D – DEFECTS

| Observation | Rating (0-4) | Notes/Examples |
|-------------|--------------|----------------|
| Scrap rate exceeds target |  |  |
| Rework is common |  |  |
| Customer returns/complaints |  |  |
| Inspection failures |  |  |
| Material waste from defects |  |  |
| Time lost to sorting/rework |  |  |
| **TOTAL DEFECTS SCORE** | **/24** |  |

**Top Defect Issues:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

#### O – OVERPRODUCTION

| Observation | Rating (0-4) | Notes/Examples |
|-------------|--------------|----------------|
| Making parts before needed |  |  |
| Producing more than ordered |  |  |
| Running large batches "just in case" |  |  |
| Accumulating WIP inventory |  |  |
| Making parts faster than downstream can consume |  |  |
| Producing to keep people/machines busy |  |  |
| **TOTAL OVERPRODUCTION SCORE** | **/24** |  |

**Top Overproduction Issues:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

#### W – WAITING

| Observation | Rating (0-4) | Notes/Examples |
|-------------|--------------|----------------|
| Machines idle waiting for material |  |  |
| Operators waiting for machines |  |  |
| Waiting for inspection/approval |  |  |
| Waiting for information/drawings |  |  |
| Waiting for tooling or fixtures |  |  |
| Waiting for maintenance/repairs |  |  |
| Waiting for previous operation |  |  |
| **TOTAL WAITING SCORE** | **/28** |  |

**Top Waiting Issues:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

#### N – NON-UTILIZED TALENT

| Observation | Rating (0-4) | Notes/Examples |
|-------------|--------------|----------------|
| Skilled workers doing unskilled tasks |  |  |
| Ideas and suggestions ignored |  |  |
| No involvement in problem-solving |  |  |
| Limited training or development |  |  |
| Narrow job definitions |  |  |
| Underutilized expertise |  |  |
| **TOTAL NON-UTILIZED TALENT SCORE** | **/24** |  |

**Top Talent Utilization Issues:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

#### T – TRANSPORTATION

| Observation | Rating (0-4) | Notes/Examples |
|-------------|--------------|----------------|
| Excessive material movement |  |  |
| Multiple handling of same parts |  |  |
| Long distances between operations |  |  |
| Inefficient layout |  |  |
| Manual material handling |  |  |
| Searching for materials |  |  |
| **TOTAL TRANSPORTATION SCORE** | **/24** |  |

**Top Transportation Issues:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

#### I – INVENTORY

| Observation | Rating (0-4) | Notes/Examples |
|-------------|--------------|----------------|
| Excess raw material inventory |  |  |
| High WIP (work in progress) |  |  |
| Excess finished goods |  |  |
| Obsolete inventory |  |  |
| Poor inventory accuracy |  |  |
| Inventory consuming floor space |  |  |
| Tied-up capital in inventory |  |  |
| **TOTAL INVENTORY SCORE** | **/28** |  |

**Top Inventory Issues:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

#### M – MOTION

| Observation | Rating (0-4) | Notes/Examples |
|-------------|--------------|----------------|
| Excessive walking/reaching |  |  |
| Poor workstation ergonomics |  |  |
| Searching for tools |  |  |
| Bending, twisting movements |  |  |
| Unnecessary handling of parts |  |  |
| Poor tool/material organization |  |  |
| **TOTAL MOTION SCORE** | **/24** |  |

**Top Motion Issues:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

#### E – EXCESS PROCESSING

| Observation | Rating (0-4) | Notes/Examples |
|-------------|--------------|----------------|
| Tighter tolerances than needed |  |  |
| Over-inspection |  |  |
| Redundant operations |  |  |
| Unnecessary features |  |  |
| Poor tooling/methods |  |  |
| Excessive paperwork |  |  |
| **TOTAL EXCESS PROCESSING SCORE** | **/24** |  |

**Top Excess Processing Issues:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

### 2.2 DOWNTIME Summary and Prioritization

**Overall Waste Assessment:**

| Waste Type | Score | Percentage | Rank | Priority Action |
|------------|-------|------------|------|-----------------|
| Defects | /24 | % | | |
| Overproduction | /24 | % | | |
| Waiting | /28 | % | | |
| Non-Utilized Talent | /24 | % | | |
| Transportation | /24 | % | | |
| Inventory | /28 | % | | |
| Motion | /24 | % | | |
| Excess Processing | /24 | % | | |
| **TOTAL** | **/200** | **100%** | | |

**Prioritization Matrix:**

Plot your top 3-5 waste issues on this matrix:

```
HIGH IMPACT
    │
    │   PRIORITY 1        PRIORITY 2
    │   (Do First)        (Plan & Do)
    │
────┼─────────────────────────────
    │
    │   PRIORITY 4        PRIORITY 3
    │   (Eliminate if     (Quick Wins)
    │    possible)
LOW IMPACT
    
    LOW EFFORT ───────────► HIGH EFFORT
```

**Priority 1 Improvements (High Impact, Low Effort):**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Next Steps:**
- Form kaizen teams for Priority 1 items
- Set target completion dates
- Assign ownership
- Track progress

---

## 3. Spaghetti Diagram Template

### 3.1 Purpose
Document the physical path of materials, operators, or information through the shop to identify transportation and motion waste.

### 3.2 Instructions

1. **Select Subject:** What are you tracking?
   - ☐ Operator movement
   - ☐ Material flow (specific part)
   - ☐ Tool movement
   - ☐ Information flow (paperwork)

2. **Draw Shop Layout:** Create a simple floor plan showing:
   - Machines and equipment
   - Work areas
   - Storage locations
   - Desks/offices
   - Receiving/shipping

3. **Track and Mark Movement:** Follow the subject for a complete cycle and draw the path with a colored line

4. **Measure:** Use a measuring wheel or estimate distances

5. **Analyze:** Identify unnecessary movement and plan improvements

### 3.3 Spaghetti Diagram Worksheet

**Subject Tracked:** _______________________
**Date:** __________ **Tracked By:** __________
**Time Period:** __________ to __________

**Observations:**

| Step | From Location | To Location | Distance (ft) | Reason for Movement | Value-Added? |
|------|---------------|-------------|---------------|---------------------|--------------|
| 1 |  |  |  |  | ☐ Yes ☐ No |
| 2 |  |  |  |  | ☐ Yes ☐ No |
| 3 |  |  |  |  | ☐ Yes ☐ No |
| 4 |  |  |  |  | ☐ Yes ☐ No |
| 5 |  |  |  |  | ☐ Yes ☐ No |
| 6 |  |  |  |  | ☐ Yes ☐ No |
| 7 |  |  |  |  | ☐ Yes ☐ No |
| 8 |  |  |  |  | ☐ Yes ☐ No |
| 9 |  |  |  |  | ☐ Yes ☐ No |
| 10 |  |  |  |  | ☐ Yes ☐ No |

**Summary:**
- **Total Distance Traveled:** __________ feet
- **Number of Movements:** __________
- **Value-Added Distance:** __________ feet ( _____% )
- **Non-Value-Added Distance:** __________ feet ( _____% )
- **Estimated Time Spent Moving:** __________ minutes

**Improvement Ideas:**

1. _________________________________________________
2. _________________________________________________
3. _________________________________________________
4. _________________________________________________

**Future State Goal:**
- **Target Total Distance:** __________ feet (____% reduction)
- **Target Movement Time:** __________ minutes (____% reduction)

---

## 4. Process Observation Sheet

### 4.1 Purpose
Conduct detailed observation of a process to identify cycle time, waste, and improvement opportunities.

### 4.2 Process Observation Form

**Process Name:** _______________________
**Part Number:** __________ **Operation:** __________
**Observer:** __________ **Date:** __________ **Time:** __________
**Operator:** __________ **Machine:** __________

#### Setup Information
- **Batch Size:** __________ pieces
- **Setup Time:** __________ minutes
- **First Piece Inspection Time:** __________ minutes

#### Cycle Time Observation (observe 5-10 cycles)

| Cycle # | Start Time | End Time | Cycle Time (sec) | Notes/Issues |
|---------|------------|----------|------------------|--------------|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
| 8 |  |  |  |  |
| 9 |  |  |  |  |
| 10 |  |  |  |  |

**Cycle Time Statistics:**
- **Average Cycle Time:** __________ sec
- **Fastest Cycle:** __________ sec
- **Slowest Cycle:** __________ sec
- **Standard Deviation:** __________ sec
- **Consistency:** ☐ High ☐ Medium ☐ Low

#### Time Element Breakdown (for one representative cycle)

| Element Description | Time (sec) | Value-Added? | Category |
|---------------------|------------|--------------|----------|
| Load part in fixture |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Position and clamp |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Start cycle |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Machine cutting time |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Inspection (in cycle) |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Unload part |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Deburr |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Place in container |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Get next part |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |
| Other: |  | ☐ Yes ☐ No | ☐ Setup ☐ Run ☐ Wait |

**Summary:**
- **Total Cycle Time:** __________ sec
- **Value-Added Time:** __________ sec ( _____% )
- **Non-Value-Added Time:** __________ sec ( _____% )

#### Waste Observations

**DOWNTIME Checklist:**

| Waste Type | Observed? | Description |
|------------|-----------|-------------|
| Defects | ☐ Yes ☐ No |  |
| Overproduction | ☐ Yes ☐ No |  |
| Waiting | ☐ Yes ☐ No |  |
| Non-Utilized Talent | ☐ Yes ☐ No |  |
| Transportation | ☐ Yes ☐ No |  |
| Inventory | ☐ Yes ☐ No |  |
| Motion | ☐ Yes ☐ No |  |
| Excess Processing | ☐ Yes ☐ No |  |

#### Safety and Ergonomics Observations

| Issue | Observed? | Severity | Notes |
|-------|-----------|----------|-------|
| Awkward posture | ☐ Yes ☐ No | ☐ High ☐ Med ☐ Low |  |
| Repetitive motion | ☐ Yes ☐ No | ☐ High ☐ Med ☐ Low |  |
| Heavy lifting | ☐ Yes ☐ No | ☐ High ☐ Med ☐ Low |  |
| Reaching | ☐ Yes ☐ No | ☐ High ☐ Med ☐ Low |  |
| Safety hazards | ☐ Yes ☐ No | ☐ High ☐ Med ☐ Low |  |

#### Improvement Opportunities

**Quick Wins (can implement immediately):**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Moderate Improvements (require planning/resources):**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Long-Term Improvements (significant investment):**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Estimated Improvement Potential:**
- **Cycle Time Reduction:** _____% (from _____ sec to _____ sec)
- **Setup Time Reduction:** _____% (from _____ min to _____ min)
- **Quality Improvement:** _________________________________________________

**Follow-Up Actions:**

| Action Item | Responsible | Target Date | Status |
|-------------|-------------|-------------|--------|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

## 5. Takt Time Calculator

### 5.1 Purpose
Calculate the pace of production required to meet customer demand.

### 5.2 Takt Time Calculation Worksheet

**Product/Family:** _______________________
**Calculated By:** __________ **Date:** __________

#### Step 1: Determine Available Time

**Per Shift:**
- Total shift length: __________ hours × 60 = __________ minutes
- Breaks: __________ minutes
- Lunch: __________ minutes
- Team meetings: __________ minutes
- Planned maintenance: __________ minutes
- Other downtime: __________ minutes
- **Total Planned Downtime:** __________ minutes

**Available Time Per Shift:** __________ minutes

**Per Day:**
- Shifts per day: __________
- **Available Time Per Day:** __________ minutes × __________ = __________ minutes

**Per Week:**
- Working days per week: __________
- **Available Time Per Week:** __________ minutes × __________ = __________ minutes

**Per Month:**
- Working days per month: __________ (typically 20-22)
- **Available Time Per Month:** __________ minutes × __________ = __________ minutes

#### Step 2: Determine Customer Demand

**Monthly Demand:**
- Total units ordered per month: __________ pieces

**Daily Demand:**
- Units per day: __________ pieces ÷ __________ days = __________ pieces/day

**Hourly Demand:**
- Units per hour: __________ pieces ÷ __________ hours = __________ pieces/hour

#### Step 3: Calculate Takt Time

**Takt Time Formula:**

Takt Time = Available Time ÷ Customer Demand

**Takt Time (minutes):**
__________ minutes per day ÷ __________ pieces per day = __________ minutes/piece

**Takt Time (seconds):**
__________ × 60 = __________ seconds/piece

### 5.3 Takt Time Interpretation

**Your Takt Time:** __________ seconds/piece

**This means:** You must complete one unit every __________ seconds to meet customer demand.

**Comparison to Current Performance:**

| Metric | Current | Required (Takt) | Gap | Status |
|--------|---------|-----------------|-----|--------|
| Cycle Time | _____ sec/pc | _____ sec/pc | _____ sec | ☐ OK ☐ Problem |
| Capacity per day | _____ pcs | _____ pcs | _____ pcs | ☐ OK ☐ Problem |

**Status Interpretation:**
- ✓ **Cycle Time < Takt Time:** You have capacity to meet demand (GOOD)
- ✗ **Cycle Time > Takt Time:** You cannot meet demand at current pace (PROBLEM)
- ⚠ **Cycle Time ≈ Takt Time:** No buffer, vulnerable to disruptions (RISK)

**Recommendations:**

If cycle time > takt time:
- Reduce cycle time through process improvement
- Add shifts or overtime
- Add capacity (machines/operators)
- Negotiate longer lead times with customer

If cycle time < takt time:
- Operate at takt pace (don't overproduce)
- Use extra time for maintenance, training, improvement
- Consider accepting more work

### 5.4 Takt Time Example

**Example: Machine Shop Part**

**Available Time:**
- 8-hour shift = 480 minutes
- Breaks: 20 minutes
- Lunch: 30 minutes
- Available: 480 - 20 - 30 = **430 minutes/shift**
- Two shifts per day = 860 minutes/day

**Customer Demand:**
- 200 pieces per day

**Takt Time Calculation:**
- 860 minutes ÷ 200 pieces = **4.3 minutes/piece = 258 seconds/piece**

**Interpretation:**
- Must complete one part every 258 seconds (4 minutes, 18 seconds)
- If current cycle time is 210 seconds → OK, have buffer
- If current cycle time is 300 seconds → Problem, cannot meet demand

---

## Next Steps

Use these templates and tools to:

1. **Map your current state** with Value Stream Mapping
2. **Identify waste** using the DOWNTIME assessment
3. **Document movement** with spaghetti diagrams
4. **Observe processes** in detail to find improvements
5. **Calculate takt time** to understand required pace

**Continue to Part 2:** Just-In-Time, Kanban, and Pull System templates

---

*This appendix is designed to support Module 24: L.E.A.N. Strategies. Adapt these templates to your specific shop environment and scale.*


---


## Contents

This section covers:
- Just-In-Time (JIT) and Pull System Templates
- Kanban Card Designs and Implementation
- Supermarket Setup and Management
- Production Leveling (Heijunka)

---

## 6. Just-In-Time (JIT) System Templates

### 6.1 Pull System Design Worksheet

**Purpose:** Design a pull system for a specific product or process.

**Product/Family:** _______________________
**Designer:** __________ **Date:** __________

#### Step 1: Identify the Pacemaker Process

The pacemaker is the single point where production is scheduled. All upstream processes respond to pull signals.

**Pacemaker Process:** _________________________________

**Criteria for Selection:**
- ☐ Closest to customer
- ☐ Stable cycle time
- ☐ Creates predictable demand for upstream
- ☐ Manageable variation

#### Step 2: Identify Supermarket Locations

Supermarkets are buffers of inventory that enable pull between disconnected processes.

| Supermarket Location | Replenished By | Consumed By | Parts/SKUs | Typical Quantity |
|----------------------|----------------|-------------|------------|------------------|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

#### Step 3: Define Continuous Flow Cells

Which processes can flow continuously without supermarkets?

**Flow Cell 1:** _______________________
- Processes included: _______________________
- Takt time: __________ sec
- Operators: __________

**Flow Cell 2:** _______________________
- Processes included: _______________________
- Takt time: __________ sec
- Operators: __________

#### Step 4: Establish Pull Signals

How will each process know what to produce?

| Process | Pull Signal Type | Trigger Point | Response Time |
|---------|------------------|---------------|---------------|
|  | ☐ Kanban ☐ Electronic ☐ Visual | |  |
|  | ☐ Kanban ☐ Electronic ☐ Visual | |  |
|  | ☐ Kanban ☐ Electronic ☐ Visual | |  |

#### Step 5: Set Inventory Levels

Calculate buffer inventory for each supermarket.

**Formula:**
Buffer = (Demand during Lead Time) + Safety Stock

| Supermarket | Daily Demand | Replenishment Lead Time | Safety Stock | Total Buffer |
|-------------|--------------|------------------------|--------------|--------------|
|  | ___/day | ___ days | ___ pcs | ___ pcs |
|  | ___/day | ___ days | ___ pcs | ___ pcs |
|  | ___/day | ___ days | ___ pcs | ___ pcs |

### 6.2 JIT Implementation Checklist

**Implementation Phase:** ☐ Planning ☐ Pilot ☐ Expansion ☐ Optimization

#### Prerequisites

- ☐ Processes are stable and predictable
- ☐ Quality is consistently high (>95% FPY)
- ☐ Setup times are reasonable or improving
- ☐ Maintenance program ensures uptime
- ☐ Team is trained on pull concepts
- ☐ Management is committed

#### Infrastructure

- ☐ Supermarket locations identified and prepared
- ☐ Kanban cards designed and printed
- ☐ Visual management boards installed
- ☐ Material handling equipment available
- ☐ Storage containers/bins standardized
- ☐ Replenishment routes established

#### Rules and Procedures

- ☐ Pull rules documented and posted
- ☐ Kanban handling procedures trained
- ☐ Responsibility for replenishment assigned
- ☐ Response time targets established
- ☐ Inventory counting procedures defined
- ☐ Troubleshooting process documented

#### Launch

- ☐ Initial inventory established in supermarkets
- ☐ Kickoff meeting with all stakeholders
- ☐ "Go-live" date communicated
- ☐ Support plan for first week
- ☐ Daily check-ins scheduled

#### Sustain and Improve

- ☐ Metrics tracked daily
- ☐ Visual boards updated
- ☐ Weekly review meetings
- ☐ Continuous adjustment of buffer levels
- ☐ Problem-solving for disruptions
- ☐ Celebrate successes

---

## 7. Kanban Card Templates

### 7.1 Standard Production Kanban Card

```
┌─────────────────────────────────────────────────┐
│                 PRODUCTION KANBAN               │
├─────────────────────────────────────────────────┤
│ Part Number: _________________                  │
│ Part Name: ___________________                  │
│                                                 │
│ Produce At: __________________                  │
│ Store At: ____________________                  │
│                                                 │
│ Container Capacity: _________ pieces            │
│ Min Order Qty: _________ pieces                 │
│                                                 │
│ Card # _____ of _____ total cards               │
│                                                 │
│ ┌──────────┐                                    │
│ │          │  [QR CODE]                         │
│ │ PHOTO or │  or Bar Code                       │
│ │ DRAWING  │  for scanning                      │
│ │          │                                    │
│ └──────────┘                                    │
└─────────────────────────────────────────────────┘
```

**Card Details to Include:**
- Part number and description
- Where to produce (workstation/machine)
- Where to store (supermarket location)
- Container size/quantity
- Card sequence number (1 of 3, 2 of 3, etc.)
- Optional: QR code for electronic tracking
- Optional: Photo of part for quick ID

### 7.2 Withdrawal Kanban Card

```
┌─────────────────────────────────────────────────┐
│                WITHDRAWAL KANBAN                │
├─────────────────────────────────────────────────┤
│ Part Number: _________________                  │
│ Part Name: ___________________                  │
│                                                 │
│ Pick Up From: _________________                 │
│ Deliver To: ___________________                 │
│                                                 │
│ Container Capacity: _________ pieces            │
│                                                 │
│ Route: _________________________                │
│ Frequency: ______________________               │
│                                                 │
│ Card # _____ of _____ total cards               │
└─────────────────────────────────────────────────┘
```

**Use Case:** Signals material handler to move parts from one location to another.

### 7.3 Kanban Calculation Worksheet

**Purpose:** Calculate the number of kanban cards needed for a part.

**Part Number:** __________ **Description:** __________
**Calculated By:** __________ **Date:** __________

#### Input Data

1. **Daily Demand (D):** __________ pieces/day
2. **Lead Time (L):** __________ days
   - (Time from signal to replenishment completion)
3. **Safety Factor (S):** __________ %
   - Typically 10-20% for stable processes
   - Higher for unstable processes or critical parts
4. **Container Capacity (C):** __________ pieces
   - Standard container size for this part

#### Kanban Calculation Formula

**Number of Kanbans = (D × L × (1 + S)) ÷ C**

**Calculation:**

Number of Kanbans = (_____ × _____ × (1 + _____)) ÷ _____

Number of Kanbans = __________ (round UP to nearest whole number)

#### Inventory Implications

**Total Inventory in System:**
- Maximum Inventory = Number of Kanbans × Container Capacity
- Maximum = _____ cards × _____ pcs/card = _____ pieces
- Days of Inventory = _____ pieces ÷ _____ pcs/day = _____ days

**Comparison:**
- Before Kanban: _____ pieces ( _____ days)
- With Kanban: _____ pieces ( _____ days)
- Reduction: _____% 

#### Example Calculation

**Example:**
- Daily Demand: 50 pieces/day
- Lead Time: 2 days (from trigger to completion)
- Safety Factor: 20% (0.20)
- Container Capacity: 25 pieces

**Number of Kanbans:**
= (50 × 2 × (1 + 0.20)) ÷ 25
= (50 × 2 × 1.20) ÷ 25
= 120 ÷ 25
= 4.8 → **5 kanbans**

**Inventory:**
- Max Inventory: 5 × 25 = 125 pieces
- Days of Inventory: 125 ÷ 50 = 2.5 days

### 7.4 Kanban Board Template

**Visual Kanban Management Board**

```
┌────────────────────────────────────────────────────┐
│         KANBAN STATUS BOARD - [WORK CENTER]        │
├─────────────┬──────────────┬──────────────────────┤
│   READY     │  IN PROCESS  │      COMPLETE        │
│  (To Do)    │  (Producing) │      (Done)          │
├─────────────┼──────────────┼──────────────────────┤
│             │              │                      │
│  [Card 1]   │   [Card 4]   │      [Card 7]        │
│  Part A     │   Part D     │      Part G          │
│  Qty: 50    │   Qty: 100   │      Qty: 75         │
│             │              │                      │
│  [Card 2]   │   [Card 5]   │      [Card 8]        │
│  Part B     │   Part E     │      Part H          │
│  Qty: 25    │   Qty: 50    │      Qty: 30         │
│             │              │                      │
│  [Card 3]   │   [Card 6]   │                      │
│  Part C     │   Part F     │                      │
│  Qty: 100   │   Qty: 200   │                      │
│             │              │                      │
├─────────────┴──────────────┴──────────────────────┤
│ RULES:                                             │
│ • Move card when starting production               │
│ • Complete oldest card first                       │
│ • Return completed card to supermarket             │
│ • Maximum 2 cards in "In Process" at once         │
└────────────────────────────────────────────────────┘
```

**Board Specifications:**
- Location: Visible at workstation
- Size: 24" × 36" minimum
- Pockets: Clear plastic for card visibility
- Update: Continuously by operators

---

## 8. Supermarket Design Templates

### 8.1 Supermarket Planning Worksheet

**Supermarket Name/ID:** _______________________
**Location:** __________ **Planner:** __________ **Date:** __________

#### Purpose and Scope

**What does this supermarket buffer?**
- Upstream Process: _______________________
- Downstream Process: _______________________
- Reason for Buffer: ☐ Long changeover ☐ Unreliable process ☐ Different cycle times ☐ Other: __________

**Parts Stored:**
- Number of different parts (SKUs): __________
- Product family: _______________________

#### Space and Layout

**Physical Requirements:**

| Parameter | Specification |
|-----------|--------------|
| Floor space needed | _____ sq ft |
| Shelving/racking type | ☐ Flow rack ☐ Static shelf ☐ Floor storage ☐ Other |
| Number of shelves/positions | _____ |
| Accessibility | ☐ Both sides ☐ One side |
| Aisle width | _____ inches |
| Height | _____ feet |

**Location Criteria:**
- ☐ Near consuming process
- ☐ Easy access for replenishment
- ☐ Visible to operators
- ☐ Protected from damage/contamination
- ☐ Adequate lighting

#### Inventory Planning

**Per Part Inventory Calculation:**

| Part # | Daily Demand | Replenish Lead Time | Safety % | Container Size | # Kanbans | Max Inventory |
|--------|--------------|---------------------|----------|----------------|-----------|---------------|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

**Total Supermarket Inventory:**
- Maximum total pieces: __________ pieces
- Maximum total value: $__________
- Total days of inventory: __________ days (average)

#### Material Flow

**Replenishment Process:**
1. Signal: How is replenishment triggered?
   - ☐ Kanban card in collection box
   - ☐ Visual min/max trigger
   - ☐ Electronic signal
   - ☐ Scheduled route check

2. Frequency: How often is supermarket replenished?
   - ☐ Continuous (as cards arrive)
   - ☐ Scheduled routes (every ___ hours)
   - ☐ Once per shift
   - ☐ Once per day

3. Responsibility: Who replenishes?
   - ☐ Material handler
   - ☐ Producing operator
   - ☐ Dedicated runner
   - ☐ Other: __________

**Withdrawal Process:**
1. Who withdraws: __________
2. When: ☐ As needed ☐ Scheduled route ☐ Other: __________
3. Signal: ☐ Withdrawal kanban ☐ FIFO lane ☐ Other: __________

#### Visual Management

**Visual Controls Needed:**
- ☐ Location labels (part numbers)
- ☐ Quantity labels (min/max levels)
- ☐ FIFO lanes marked
- ☐ Kanban card holders
- ☐ Status indicators (full/empty)
- ☐ Refill priority markers
- ☐ Replenishment schedule posted

### 8.2 Supermarket Layout Example

**FIFO Flow Rack Supermarket**

```
View from above:

REPLENISHMENT SIDE                CONSUMPTION SIDE
(Upstream Process)                (Downstream Process)

┌─────────────────┐              ┌─────────────────┐
│  Part A (1/3)   │──────────────>│  [Empty Bin]    │
│  [K] [K] [K]    │  Gravity Flow │                 │
└─────────────────┘              └─────────────────┘

┌─────────────────┐              ┌─────────────────┐
│  Part A (2/3)   │──────────────>│  Part A [K] [K] │
│  [K] [K]        │              │                 │
└─────────────────┘              └─────────────────┘

┌─────────────────┐              ┌─────────────────┐
│  Part B (1/4)   │──────────────>│  Part B [K] [K] │
│  [K] [K] [K]    │              │  [K]            │
└─────────────────┘              └─────────────────┘

Legend:
[K] = Kanban card attached to full container
──> = Flow direction (gravity)
```

**How It Works:**
1. Downstream operator removes container from right side (consumption)
2. Kanban card goes to collection box
3. Upstream process receives kanban signal
4. New container loaded on left side (replenishment)
5. Container flows to right side by gravity (FIFO ensured)

### 8.3 Supermarket Audit Checklist

**Audit Date:** __________ **Auditor:** __________
**Supermarket:** __________

#### Organization (Score: /25)

| Item | Score 0-5 | Notes |
|------|-----------|-------|
| All locations clearly labeled |  |  |
| No unmarked parts |  |  |
| FIFO maintained |  |  |
| Aisles clear and accessible |  |  |
| Cleanliness and housekeeping |  |  |
| **TOTAL** | **/25** |  |

#### Inventory Accuracy (Score: /25)

| Item | Score 0-5 | Notes |
|------|-----------|-------|
| Actual matches kanban quantity |  |  |
| No excess inventory |  |  |
| No stockouts |  |  |
| Proper container quantities |  |  |
| Correct number of kanbans |  |  |
| **TOTAL** | **/25** |  |

#### Visual Management (Score: /25)

| Item | Score 0-5 | Notes |
|------|-----------|-------|
| Min/max levels visible |  |  |
| Status clear at a glance |  |  |
| Kanban cards properly attached |  |  |
| Instructions/procedures posted |  |  |
| Metrics displayed |  |  |
| **TOTAL** | **/25** |  |

#### Process Compliance (Score: /25)

| Item | Score 0-5 | Notes |
|------|-----------|-------|
| Pull rules followed |  |  |
| Timely replenishment |  |  |
| Proper kanban handling |  |  |
| No overproduction |  |  |
| Documentation up to date |  |  |
| **TOTAL** | **/25** |  |

**Overall Score:** _____/100

**Rating:**
- 90-100: Excellent
- 80-89: Good
- 70-79: Acceptable
- <70: Needs Improvement

**Action Items:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

---

## 9. Heijunka (Production Leveling) Templates

### 9.1 Heijunka Box Template

**Purpose:** Level production by scheduling mixed models in a repeating pattern.

**Heijunka Box Structure:**

```
TIME PERIODS (columns) →

P    │ 8:00 │ 9:00 │ 10:00│ 11:00│ 12:00│ 1:00 │ 2:00 │ 3:00 │
R    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
O    │      │      │      │      │      │      │      │      │
D  M │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │
U  O │ A    │ B    │ A    │ C    │ A    │ B    │ A    │ C    │
C  N │      │      │      │      │      │      │      │      │
T  D ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
S  A │      │      │      │      │      │      │      │      │
   Y │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │
     │ D    │ E    │ D    │ F    │ D    │ E    │ D    │ F    │
(  T │      │      │      │      │      │      │      │      │
r  U ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
o  E │      │      │      │      │      │      │      │      │
w  S │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │
s  D │ G    │ H    │ G    │ I    │ G    │ H    │ G    │ I    │
)  A │      │      │      │      │      │      │      │      │
   Y ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
     │      │      │      │      │      │      │      │      │
   W │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │ [K]  │
   E │ J    │ K    │ J    │ L    │ J    │ K    │ J    │ L    │
   D │      │      │      │      │      │      │      │      │
```

**How to Use:**
1. Each row = different product or model
2. Each column = time period (pitch)
3. Kanban cards placed in slots according to schedule
4. Material handler picks cards left to right, top to bottom
5. Creates level, mixed-model production

### 9.2 Pitch Calculation Worksheet

**Purpose:** Determine the production interval (pitch) for moving work.

**Product/Family:** _______________________
**Calculated By:** __________ **Date:** __________

#### Step 1: Calculate Takt Time

- Available time per shift: __________ minutes
- Customer demand per shift: __________ pieces
- **Takt Time** = _____ min ÷ _____ pcs = _____ minutes/piece

#### Step 2: Determine Pack-Out Quantity

**Pack-out quantity** = standard container or shipping quantity

- Standard container/box holds: __________ pieces
- Or shipping quantity: __________ pieces
- **Pack-Out Quantity:** __________ pieces

#### Step 3: Calculate Pitch

**Pitch** = Takt Time × Pack-Out Quantity

**Pitch** = _____ min/pc × _____ pcs = _____ minutes

**Round to practical interval:** __________ minutes
(Common: 10, 15, 20, 30 minutes)

#### Step 4: Determine Pitches per Shift

**Pitches per Shift** = Available Time ÷ Pitch

**Pitches per Shift** = _____ min ÷ _____ min = _____ pitches

#### Example

**Example Calculation:**
- Available time: 450 minutes/shift
- Demand: 225 pieces/shift
- Takt time: 450 ÷ 225 = 2 minutes/piece
- Pack-out quantity: 10 pieces/box
- Pitch: 2 min/pc × 10 pcs = 20 minutes
- Pitches per shift: 450 ÷ 20 = 22.5 → **22 pitches**

**Interpretation:**
- Every 20 minutes, one box of 10 pieces should be completed
- 22 boxes per shift = 220 pieces (close to demand of 225)
- Material handler checks every 20 minutes
- Visual management tracks on-time vs. behind

### 9.3 Production Leveling Planning Worksheet

**Purpose:** Create a level schedule mixing volume and variety.

**Planning Period:** __________ (week, day, shift)
**Planner:** __________ **Date:** __________

#### Step 1: Gather Demand Data

| Product | Weekly Demand | Daily Demand | Takt Time | Batch Pref. |
|---------|---------------|--------------|-----------|-------------|
| A |  |  |  |  |
| B |  |  |  |  |
| C |  |  |  |  |
| D |  |  |  |  |
| E |  |  |  |  |

#### Step 2: Calculate Ideal Frequency

**Every Product Every (EPE)** = How often should we make each product?

**EPE Calculation:**

EPE = (Available Time × Batch Efficiency) ÷ (Setup Time × Number of Products + Total Run Time)

**Simplified Approach:**

| Product | Daily Demand | Setup Time | Run Time/Unit | Total Time | Production Freq. |
|---------|--------------|------------|---------------|------------|------------------|
| A | 100 | 30 min | 2 min | 230 min | Daily |
| B | 50 | 30 min | 2 min | 130 min | Every 2 days |
| C | 200 | 45 min | 1.5 min | 345 min | Daily |
| D | 25 | 30 min | 2 min | 80 min | Weekly |

#### Step 3: Create Leveled Schedule Pattern

**Daily Pattern Example:**

| Time | Product | Quantity | Duration |
|------|---------|----------|----------|
| 7:00-7:30 | A | 25 | 30 min |
| 7:30-8:00 | C | 40 | 30 min |
| 8:00-8:30 | A | 25 | 30 min |
| 8:30-9:00 | B | 15 | 30 min |
| 9:00-9:30 | C | 40 | 30 min |
| ... | ... | ... | ... |

**Pattern Characteristics:**
- ☐ Even mix throughout day (not all A's first, then all B's)
- ☐ High-runners produced multiple times per day
- ☐ Low-runners produced less frequently
- ☐ Setup time minimized by grouping similar products
- ☐ Demand for all products met

#### Step 4: Validate Schedule

**Capacity Check:**

| Resource | Available | Required | Utilization % | Status |
|----------|-----------|----------|---------------|--------|
| Machine Hours |  |  |  | ☐ OK ☐ Over |
| Labor Hours |  |  |  | ☐ OK ☐ Over |
| Material Avail. |  |  |  | ☐ OK ☐ Short |

**Smoothness Check:**
- ☐ Workload relatively even throughout day
- ☐ No large peaks and valleys
- ☐ Material demand on suppliers is leveled
- ☐ Shipping demand is leveled

---

## 10. Pull System Performance Metrics

### 10.1 Pull System Metrics Dashboard

**Week of:** __________

#### Inventory Metrics

| Metric | Target | Monday | Tuesday | Wednesday | Thursday | Friday | Trend |
|--------|--------|--------|---------|-----------|----------|--------|-------|
| WIP Inventory (pcs) | <500 |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| WIP Days | <2.0 |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| Supermarket Stock (pcs) | Target |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| Stockouts | 0 |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| Overstock Instances | 0 |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |

#### Flow Metrics

| Metric | Target | Monday | Tuesday | Wednesday | Thursday | Friday | Trend |
|--------|--------|--------|---------|-----------|----------|--------|-------|
| Kanban Cycle Time (hrs) | <24 |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| On-Time Replenishment % | >95% |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| Pitch Attainment % | 100% |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| Lead Time (days) | <5 |  |  |  |  |  | ☐ ↑ ☐ → ☐ ↓ |

#### Compliance Metrics

| Metric | Target | This Week | Notes |
|--------|--------|-----------|-------|
| Kanban Rules Followed | 100% |  |  |
| Heijunka Box Updated | Daily |  |  |
| Supermarket Audits | 1/week |  |  |
| Visual Board Current | 100% |  |  |

### 10.2 Kanban System Health Check

**Check Date:** __________ **Evaluator:** __________

| Health Indicator | Healthy | Warning | Unhealthy | Score |
|------------------|---------|---------|-----------|-------|
| Stockouts per week | 0 | 1-2 | 3+ | |
| Overstock locations | 0 | 1-3 | 4+ | |
| Kanban card accuracy | 100% | 95-99% | <95% | |
| Replenishment response | <4 hrs | 4-8 hrs | >8 hrs | |
| WIP vs. target | On target | ±10% | >10% | |
| Operator compliance | 100% | 90-99% | <90% | |
| Visual board updated | Always | Usually | Rarely | |

**Overall System Health:** ☐ Healthy ☐ Needs Attention ☐ Critical

**Action Plan:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

---

## Next Steps

Use Part 2 templates to:

1. **Design pull systems** with appropriate supermarkets and signals
2. **Implement kanban** with properly calculated quantities
3. **Set up supermarkets** with visual controls
4. **Level production** using Heijunka methods
5. **Track metrics** to ensure system health

**Continue to Part 3:** SMED, TPM, Poka-Yoke, and Continuous Improvement templates

---

*This appendix is designed to support Module 24: L.E.A.N. Strategies. Adapt these templates to your specific shop environment and scale.*


---


## Contents

This section covers:
- SMED (Single-Minute Exchange of Dies) Templates
- TPM (Total Productive Maintenance) Tools
- Poka-Yoke (Error-Proofing) Design
- Kaizen Event Planning and Execution

---

## 11. SMED (Setup Reduction) Templates

### 11.1 SMED Analysis Worksheet

**Purpose:** Document and analyze current setup process to identify improvement opportunities.

**Machine/Process:** _______________________
**Part/Setup:** _______________________
**Analyst:** __________ **Date:** __________

#### Current State Setup Time

| Measurement | Time |
|-------------|------|
| Average setup time | _____ minutes |
| Best setup time | _____ minutes |
| Worst setup time | _____ minutes |
| Who performs setup | ☐ Operator ☐ Setup specialist ☐ Both |

#### Setup Element Documentation

**Instructions:** Observe 2-3 complete setups. Document every activity with video if possible.

| Step | Activity Description | Time (min) | Internal or External? | Value-Add? | Category |
|------|---------------------|------------|----------------------|------------|----------|
| 1 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 2 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 3 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 4 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 5 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 6 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 7 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 8 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 9 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |
| 10 |  |  | ☐ I ☐ E | ☐ Y ☐ N | ☐ Search ☐ Move ☐ Adjust ☐ Measure |

**Definitions:**
- **Internal:** Must be done while machine is stopped
- **External:** Can be done while machine is running
- **Value-Add:** Directly contributes to changeover (customer would pay for it)

#### Current State Analysis

**Time Breakdown:**

| Category | Time (min) | Percentage |
|----------|------------|------------|
| Internal activities | | % |
| External activities | | % |
| **TOTAL** | | **100%** |

**Activity Type Breakdown:**

| Type | Time (min) | Percentage | Examples |
|------|------------|------------|----------|
| Searching/gathering tools | | % | Looking for wrenches, fixtures, programs |
| Moving/transporting | | % | Getting tools, bringing parts |
| Unfastening/fastening | | % | Bolts, clamps, screws |
| Adjusting/measuring | | % | Offsets, alignments, test cuts |
| Cleaning | | % | Chip removal, coolant cleanup |
| Trial runs | | % | First piece inspection, adjustments |
| Other | | % | |
| **TOTAL** | | **100%** | |

### 11.2 SMED Improvement Ideas Checklist

**Stage 1: Separate Internal and External**

Goal: Perform as much as possible while machine is running.

- ☐ Pre-stage next tooling at machine (external)
- ☐ Pre-heat tools while machine running (external)
- ☐ Prepare fixtures and workholding ahead (external)
- ☐ Gather all tools/wrenches before stopping machine (external)
- ☐ Load program and verify before stopping machine (external)
- ☐ Pre-position material at machine (external)
- ☐ Organize all setup components in cart/kit (external)
- ☐ Complete paperwork while running (external)
- ☐ Post-setup cleanup after starting new job (external)

**Estimated Time Savings:** _____ minutes (____%)

**Stage 2: Convert Internal to External**

Goal: Redesign so activities can be done while running.

- ☐ Standardize tool heights (eliminate touch-off during setup)
- ☐ Quick-change tool holders (eliminate manual tool changes)
- ☐ Duplicate work holding (swap while running)
- ☐ Standardized work offsets (eliminate offset setup)
- ☐ Pre-proven programs (eliminate on-machine editing)
- ☐ Fixture carts (roll on/off without disassembly)

**Estimated Time Savings:** _____ minutes (____%)

**Stage 3: Streamline Internal Activities**

Goal: Make remaining internal activities faster.

**Eliminate Adjustments:**
- ☐ Standardized heights and positions
- ☐ Reference surfaces and hard stops
- ☐ Preset tooling systems
- ☐ Gage blocks for standard setups
- ☐ Visual guides and indicators

**Eliminate Fasteners:**
- ☐ Replace bolts with clamps
- ☐ Replace multiple fasteners with one
- ☐ Quick-release mechanisms
- ☐ Pear-shaped holes for sliding
- ☐ Cam locks instead of threads
- ☐ Magnets instead of clamps (where appropriate)

**Parallel Operations:**
- ☐ Two people setup (where it makes sense)
- ☐ Simultaneous positioning of multiple elements
- ☐ Pre-assembled subcomponents

**Standardization:**
- ☐ Common tooling across similar setups
- ☐ Standardized part orientations
- ☐ Consistent work holding methods
- ☐ Repeatable coordinate systems
- ☐ Standard procedures documented

**Estimated Time Savings:** _____ minutes (____%)

### 11.3 SMED Action Plan

**Setup:** __________ **Target Reduction:** _____% (from _____ to _____ minutes)

| Improvement | Type | Responsibility | Resources Needed | Cost Est. | Target Date | Status |
|-------------|------|----------------|------------------|-----------|-------------|--------|
|  | ☐ S1 ☐ S2 ☐ S3 |  |  |  |  |  |
|  | ☐ S1 ☐ S2 ☐ S3 |  |  |  |  |  |
|  | ☐ S1 ☐ S2 ☐ S3 |  |  |  |  |  |
|  | ☐ S1 ☐ S2 ☐ S3 |  |  |  |  |  |

**Legend:** S1=Separate Internal/External, S2=Convert to External, S3=Streamline Internal

### 11.4 Standard Setup Procedure Template

**Machine:** __________ **Setup:** __________ **Target Time:** _____ min

**Tools/Equipment Required:**
- _________________________________________________
- _________________________________________________
- _________________________________________________

**Pre-Setup (External - Before Stopping Machine):**

| Step | Action | Time | Notes |
|------|--------|------|-------|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

**Setup (Internal - Machine Stopped):**

| Step | Action | Time | Photos/Diagrams | Critical Points |
|------|--------|------|-----------------|-----------------|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Post-Setup (External - After Starting New Job):**

| Step | Action | Time | Notes |
|------|--------|------|-------|
| 1 |  |  |  |
| 2 |  |  |  |

**Total Target Time:** _____ minutes (_____ internal + _____ external)

**Revision History:**

| Date | Rev | Changes | Approved By |
|------|-----|---------|-------------|
|  |  |  |  |

---

## 12. TPM (Total Productive Maintenance) Templates

### 12.1 Overall Equipment Effectiveness (OEE) Tracking

**Purpose:** Measure true equipment productivity considering availability, performance, and quality.

**Machine:** __________ **Week of:** __________

#### Daily OEE Calculation

**OEE = Availability × Performance × Quality**

**Monday:**

| Metric | Calculation | Value |
|--------|-------------|-------|
| **Availability** | | |
| Planned Production Time | Shift time - breaks - planned stops | _____ min |
| Actual Run Time | Planned time - downtime | _____ min |
| Availability % | (Run time ÷ Planned time) × 100 | _____% |
| **Performance** | | |
| Ideal Cycle Time | Engineering standard | _____ sec/pc |
| Total Pieces Produced | Count | _____ pcs |
| Actual Production Time | Run time | _____ min |
| Performance % | (Pieces × Ideal time ÷ Run time) × 100 | _____% |
| **Quality** | | |
| Total Pieces Produced | | _____ pcs |
| Good Pieces | No defects | _____ pcs |
| Quality % | (Good ÷ Total) × 100 | _____% |
| **OEE** | | |
| OEE % | Avail. % × Perf. % × Quality % | _____% |

**Downtime Details (for Availability loss):**

| Reason | Duration (min) | Category |
|--------|----------------|----------|
|  |  | ☐ Breakdown ☐ Setup ☐ Adjustment ☐ Other |
|  |  | ☐ Breakdown ☐ Setup ☐ Adjustment ☐ Other |
|  |  | ☐ Breakdown ☐ Setup ☐ Adjustment ☐ Other |

**Repeat for Tuesday through Friday**

#### Weekly Summary

| Day | Availability | Performance | Quality | OEE | Comments |
|-----|--------------|-------------|---------|-----|----------|
| Mon | _____% | _____% | _____% | _____% |  |
| Tue | _____% | _____% | _____% | _____% |  |
| Wed | _____% | _____% | _____% | _____% |  |
| Thu | _____% | _____% | _____% | _____% |  |
| Fri | _____% | _____% | _____% | _____% |  |
| **AVG** | _____% | _____% | _____% | _____% |  |

**OEE Benchmarks:**
- World Class: 85%+
- Good: 65-85%
- Needs Improvement: <65%

**Current Status:** ☐ World Class ☐ Good ☐ Needs Improvement

### 12.2 Six Big Losses Analysis

**Machine:** __________ **Analysis Period:** __________

| Loss Category | Impact | Time/Cost Lost | % of Total | Priority |
|---------------|--------|----------------|------------|----------|
| **1. Breakdowns** | Availability | | % | |
| Equipment failure, unplanned stops | | | | |
| **2. Setup/Adjustments** | Availability | | % | |
| Changeovers, warmup, adjustments | | | | |
| **3. Small Stops** | Performance | | % | |
| Jams, minor stops (<5 min) | | | | |
| **4. Reduced Speed** | Performance | | % | |
| Running slower than designed | | | | |
| **5. Startup Rejects** | Quality | | % | |
| Scrap/rework during warmup/setup | | | | |
| **6. Production Rejects** | Quality | | % | |
| Scrap/rework during normal production | | | | |
| **TOTAL LOSSES** | | | **100%** | |

**Top 3 Losses to Address:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

### 12.3 Autonomous Maintenance Checklist

**Machine:** __________ **Operator:** __________ **Date:** __________

#### Daily Checks (5-10 minutes)

**CLEANING:**
- ☐ Remove chips from machine surfaces
- ☐ Clean coolant tank and strainer
- ☐ Wipe down ways and covers
- ☐ Clean work area around machine

**INSPECTION:**
- ☐ Check fluid levels (oil, coolant, hydraulic)
- ☐ Listen for unusual noises
- ☐ Check for leaks (oil, coolant, air)
- ☐ Inspect air pressure gauge
- ☐ Check safety devices (guards, e-stop)

**LUBRICATION:**
- ☐ Check auto-lube system operation
- ☐ Manual lube points if required

**DOCUMENTATION:**
- ☐ Record any issues found
- ☐ Tag for maintenance if needed

**Time Spent:** _____ minutes
**Issues Found:** ☐ None ☐ See notes below

**Notes/Issues:**
_________________________________________________________________
_________________________________________________________________

### 12.4 Planned Maintenance Schedule Template

**Machine:** __________ **Year:** __________

#### Maintenance Task Matrix

| Task | Frequency | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|------|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Oil change | Quarterly | ✓ | | | ✓ | | | ✓ | | | ✓ | | |
| Belt inspection | Monthly | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Level check | Semi-annual | ✓ | | | | | | ✓ | | | | | |
| Ball screw inspect | Quarterly | ✓ | | | ✓ | | | ✓ | | | ✓ | | |
| Spindle maintenance | Annual | | | | | | | ✓ | | | | | |
| Way lube check | Monthly | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Planned Downtime Budget:**
- Total hours per year: _____ hours
- Cost per hour: $_____
- Total PM budget: $_____

### 12.5 TPM Improvement Log

**Machine:** __________ **Period:** __________

| Date | Problem/Opportunity | Action Taken | Cost | Time Saved | Responsible | Status |
|------|---------------------|--------------|------|------------|-------------|--------|
|  |  |  |  |  |  | ☐ Open ☐ Complete |
|  |  |  |  |  |  | ☐ Open ☐ Complete |
|  |  |  |  |  |  | ☐ Open ☐ Complete |

**Summary:**
- Total improvements: _____
- Total cost: $_____
- Total time saved: _____ hours/year
- Payback period: _____ months

---

## 13. Poka-Yoke (Error-Proofing) Templates

### 13.1 Error-Proofing Opportunity Assessment

**Process:** __________ **Assessed By:** __________ **Date:** __________

#### Error Identification

| Step | Potential Error | Frequency | Severity | Detection | Risk Score |
|------|----------------|-----------|----------|-----------|------------|
|  |  | ☐ High ☐ Med ☐ Low | ☐ High ☐ Med ☐ Low | ☐ Hard ☐ Med ☐ Easy | /9 |
|  |  | ☐ High ☐ Med ☐ Low | ☐ High ☐ Med ☐ Low | ☐ Hard ☐ Med ☐ Easy | /9 |
|  |  | ☐ High ☐ Med ☐ Low | ☐ High ☐ Med ☐ Low | ☐ Hard ☐ Med ☐ Easy | /9 |

**Risk Scoring:**
- Frequency: High=3, Medium=2, Low=1
- Severity: High=3, Medium=2, Low=1
- Detection: Hard=3, Medium=2, Easy=1
- Risk Score = Frequency × Severity × Detection
- Prioritize scores >12

### 13.2 Poka-Yoke Design Worksheet

**Error to Prevent:** _______________________
**Designer:** __________ **Date:** __________

#### Error Analysis

**Where does error occur?** _______________________
**How does error happen?** _______________________
**Why can this error occur?** _______________________
**Who makes the error?** ☐ Operator ☐ Setup ☐ Inspection ☐ Other: _____
**What is the consequence?** _______________________

#### Poka-Yoke Principle Selection

**Choose approach:**

☐ **Elimination** - Design out the possibility of error
   - Example: Asymmetric design so part only fits one way

☐ **Replacement** - Substitute unreliable process with reliable one
   - Example: Barcode scanning instead of manual entry

☐ **Facilitation** - Make correct action easier than incorrect
   - Example: Color-coding, clear labeling

☐ **Detection** - Identify error before it proceeds
   - Example: Sensor detects missing part

☐ **Mitigation** - Reduce impact of error
   - Example: Breakaway feature prevents damage

#### Poka-Yoke Method

**Type:**
- ☐ **Contact** - Physical detection (shape, dimension)
- ☐ **Fixed-Value** - Counting method (must have exact number)
- ☐ **Motion-Step** - Sequence detection (steps must occur in order)

**Control Function:**
- ☐ **Control** - Stops process when error detected (preferred)
- ☐ **Warning** - Alerts operator to error (less reliable)

#### Design Details

**Description of Poka-Yoke:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**Sketch/Photo:**
[Attach drawing or photo]

**Components Needed:**
- _________________________________________________
- _________________________________________________
- _________________________________________________

**Installation Requirements:**
- _________________________________________________
- _________________________________________________

**Cost Estimate:** $_____
**Implementation Time:** _____ hours

#### Validation Plan

**How will effectiveness be tested?**
_________________________________________________________________

**Success Criteria:**
- ☐ Error completely eliminated, or
- ☐ Error reduced by _____%
- ☐ 100% detection rate

**Testing Results:**
- Test date: __________
- Trials: _____
- Errors prevented: _____
- Effectiveness: _____%

### 13.3 Common Poka-Yoke Examples for CNC

**Loading Errors:**

| Error | Poka-Yoke Solution |
|-------|-------------------|
| Part loaded backwards | Asymmetric fixture, pins at different positions |
| Wrong part loaded | Gage check before clamping, vision system |
| Part not fully seated | Proximity sensor detects seating |
| Forgot to remove previous part | Sensor confirms empty before cycle start |

**Setup Errors:**

| Error | Poka-Yoke Solution |
|-------|-------------------|
| Wrong tool loaded | Tool ID chip, length measurement check |
| Tool in wrong position | Coded tool holders (can only fit correct pocket) |
| Wrong program selected | Barcode on setup sheet auto-loads program |
| Offset not set | Automatic tool measurement system |
| Forgot probe calibration | Software forces calibration before first cycle |

**Process Errors:**

| Error | Poka-Yoke Solution |
|-------|-------------------|
| Missed operation | In-process gaging verifies features present |
| Wrong feed/speed | Program limits prevent dangerous parameters |
| Part moved during cut | Mid-cycle clamp pressure monitoring |
| Coolant not flowing | Flow sensor stops cycle if no coolant |

**Inspection Errors:**

| Error | Poka-Yoke Solution |
|-------|-------------------|
| Forgot to inspect | Gage station blocks access to shipping |
| Wrong gage used | Color-coded gages match part drawing |
| Inspection incomplete | Checklist with all features must be signed |
| Gage out of calibration | Gage locks when calibration due |

---

## 14. Kaizen Event Planning Templates

### 14.1 Kaizen Charter

**Event Name:** _______________________
**Dates:** __________ to __________

#### Problem Statement

**Current Condition:**
_________________________________________________________________
_________________________________________________________________

**Goal/Target Condition:**
_________________________________________________________________
_________________________________________________________________

**Gap:**
_________________________________________________________________

**Business Impact:**
- Cost: $_____ /year wasted or $_____ savings potential
- Quality: _____ defects/week or _____% improvement potential
- Delivery: _____ late orders or _____ days lead time reduction potential
- Safety: _____ incidents or _____ hazards

#### Scope

**In Scope:**
- _________________________________________________
- _________________________________________________
- _________________________________________________

**Out of Scope:**
- _________________________________________________
- _________________________________________________

**Boundaries:**
- Start point: _______________________
- End point: _______________________

#### Team

| Role | Name | Department | Availability |
|------|------|------------|--------------|
| **Sponsor** |  |  | ☐ Full ☐ Part-time |
| **Team Leader** |  |  | ☐ Full ☐ Part-time |
| **Facilitator** |  |  | ☐ Full ☐ Part-time |
| **Team Member** |  |  | ☐ Full ☐ Part-time |
| **Team Member** |  |  | ☐ Full ☐ Part-time |
| **Team Member** |  |  | ☐ Full ☐ Part-time |
| **Team Member** |  |  | ☐ Full ☐ Part-time |

**Subject Matter Experts (as needed):**
- _________________________________________________

#### Targets

| Metric | Current | Target | Stretch Goal |
|--------|---------|--------|--------------|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

#### Resources

**Budget:** $_____
**Tools/Equipment Needed:** _______________________
**Support Needed:** _______________________

**Approvals:**
- Sponsor: _________________ Date: _____
- Management: _________________ Date: _____

### 14.2 Kaizen Week Schedule

**Day 1 - Monday: Orientation and Current State**

| Time | Activity | Responsibility |
|------|----------|----------------|
| 8:00-9:00 | Kickoff meeting, introductions, charter review |  |
| 9:00-10:00 | Training on tools/methods |  |
| 10:00-12:00 | Gemba walk, process observation |  |
| 12:00-1:00 | Lunch |  |
| 1:00-3:00 | Current state mapping (VSM, spaghetti, etc.) |  |
| 3:00-4:00 | Data collection and analysis |  |
| 4:00-5:00 | Day 1 wrap-up, homework assignments |  |

**Day 2 - Tuesday: Analysis and Future State Design**

| Time | Activity | Responsibility |
|------|----------|----------------|
| 8:00-8:30 | Day 1 review, day 2 preview |  |
| 8:30-10:00 | Root cause analysis (5 Whys, fishbone) |  |
| 10:00-12:00 | Generate improvement ideas (brainstorming) |  |
| 12:00-1:00 | Lunch |  |
| 1:00-3:00 | Prioritize ideas, create future state design |  |
| 3:00-4:30 | Action plan development |  |
| 4:30-5:00 | Day 2 wrap-up |  |

**Day 3 - Wednesday: Implementation**

| Time | Activity | Responsibility |
|------|----------|----------------|
| 8:00-8:30 | Day 2 review, day 3 preview |  |
| 8:30-12:00 | Implement improvements (hands-on) |  |
| 12:00-1:00 | Lunch |  |
| 1:00-4:30 | Continue implementation |  |
| 4:30-5:00 | Day 3 wrap-up, adjust plans |  |

**Day 4 - Thursday: Implementation and Testing**

| Time | Activity | Responsibility |
|------|----------|----------------|
| 8:00-8:30 | Day 3 review, day 4 preview |  |
| 8:30-12:00 | Complete implementation |  |
| 12:00-1:00 | Lunch |  |
| 1:00-3:00 | Test and refine improvements |  |
| 3:00-4:30 | Document new procedures |  |
| 4:30-5:00 | Day 4 wrap-up, prepare presentation |  |

**Day 5 - Friday: Validation and Report Out**

| Time | Activity | Responsibility |
|------|----------|----------------|
| 8:00-8:30 | Day 4 review, day 5 preview |  |
| 8:30-10:00 | Final validation and measurement |  |
| 10:00-11:30 | Prepare presentation materials |  |
| 11:30-12:30 | Lunch |  |
| 12:30-2:00 | Rehearse presentation |  |
| 2:00-3:00 | **Report out to management** |  |
| 3:00-4:00 | Celebration, recognition, next steps |  |

### 14.3 Kaizen Report Out Template

**Presentation Structure (30-45 minutes):**

**Slide 1: Title**
- Event name
- Team members
- Dates

**Slide 2: Problem Statement**
- Current condition
- Business impact
- Why we did this event

**Slide 3: Goals/Targets**
- Metric targets
- Scope

**Slide 4: Current State**
- Process map, VSM, or photos
- Key data/metrics
- Waste identified

**Slide 5: Analysis**
- Root causes identified
- Tools used (5 Whys, fishbone, etc.)

**Slide 6: Future State Design**
- New process map
- Key changes

**Slide 7: Improvements Implemented**
- List with photos
- Before/after comparisons

**Slide 8: Results**
- Metrics achieved vs. targets
- Improvements summary

**Slide 9: Financial Impact**
- Cost to implement
- Annual savings
- Payback period

**Slide 10: Lessons Learned**
- What went well
- What was challenging
- Recommendations

**Slide 11: Sustain Plan**
- How will gains be maintained?
- Ownership
- Follow-up dates

**Slide 12: Next Steps**
- Remaining action items
- Future kaizen opportunities
- Thank you/questions

### 14.4 Kaizen Follow-Up Checklist

**30-Day Follow-Up**
- ☐ All action items completed or on track
- ☐ Metrics still at target levels
- ☐ Team members satisfied with changes
- ☐ No unintended consequences
- ☐ Procedures documented and trained

**90-Day Follow-Up**
- ☐ Sustained results (data review)
- ☐ Financial benefits realized
- ☐ Lessons applied to other areas
- ☐ Recognition and celebration
- ☐ Kaizen event closed

---

## Next Steps

Use Part 3 templates to:

1. **Reduce setup times** with SMED methodology
2. **Improve equipment reliability** with TPM practices
3. **Prevent errors** with poka-yoke designs
4. **Run kaizen events** for focused improvement

**Continue to Part 4:** Visual Management, Metrics, and Implementation Planning templates

---

*This appendix is designed to support Module 24: L.E.A.N. Strategies. Adapt these templates to your specific shop environment and scale.*


---


## Contents

This section covers:
- Visual Management and Andon Systems
- Standardized Work Templates
- Lean Metrics and Dashboards
- Lean Implementation Roadmap
- A3 Problem Solving

---

## 15. Visual Management Templates

### 15.1 Visual Management Hierarchy

**Level 1: Information Displays**
- Makes current status visible at a glance
- Examples: Labels, signs, floor markings, shadow boards

**Level 2: Performance Displays**
- Shows performance metrics and targets
- Examples: Production boards, OEE displays, quality charts

**Level 3: Control Displays**
- Enables quick response to abnormalities
- Examples: Andon lights, alarm systems, problem boards

### 15.2 Production Status Board Template

```
┌──────────────────────────────────────────────────────────────┐
│           PRODUCTION STATUS BOARD - [WORK CENTER]            │
│                    Week of: __________                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  TARGET vs ACTUAL                     HOUR-BY-HOUR          │
│                                                              │
│  Daily Target: _____ pcs             Time  | Plan | Actual │
│  Current: _____ pcs                  7:00  |  20  |   18   │
│  % to Target: _____%                 8:00  |  20  |   22   │
│                                      9:00  |  20  |   19   │
│  Status: ☐ ON TRACK                  10:00 |  20  |   --   │
│          ☐ BEHIND                    11:00 |  20  |   --   │
│          ☐ AHEAD                     12:00 |  20  |   --   │
│                                      1:00  |  20  |   --   │
├──────────────────────────────────────┤  2:00  |  20  |   --   │
│                                      │  3:00  |  20  |   --   │
│  DOWNTIME LOG                        │                       │
│                                      └─────────────────────────┘
│  Time   | Reason      | Duration    │                       │
│  8:15   | Tool Break  | 15 min      │  QUALITY STATUS       │
│  ------ | ----------- | -------     │                       │
│  ------ | ----------- | -------     │  First Piece: ☑ PASS │
│                                      │  In-Process: ☐ Issues │
├──────────────────────────────────────┤  Rejects Today: __2__ │
│                                      │                       │
│  CURRENT JOB                         │  SAFETY                │
│                                      │                       │
│  Part #: ___________                 │  Days w/o incident: __│
│  Customer: __________                │  Near misses: ____     │
│  Qty Ordered: _______                │                       │
│  Due Date: __________                │                       │
│                                      │                       │
└──────────────────────────────────────────────────────────────┘
```

**Board Specifications:**
- Size: 48" × 36" minimum
- Location: Visible from all positions in work area
- Update: Every hour by operator or team leader
- Review: Daily huddle at start of shift

### 15.3 Andon System Design

**Purpose:** Real-time alert system for problems requiring attention.

#### Signal Light Colors (Standard)

```
     ┌────┐
     │ 🔴 │  RED = Problem/Stop (immediate help needed)
     ├────┤
     │ 🟡 │  YELLOW = Caution/Attention (minor issue)
     ├────┤
     │ 🟢 │  GREEN = Normal Operation (all OK)
     ├────┤
     │ 🔵 │  BLUE = Material/Support Needed
     └────┘
```

#### Andon Response Procedure

**When Light Activates:**

| Color | Meaning | Who Responds | Max Response Time | Actions |
|-------|---------|--------------|-------------------|---------|
| 🔴 RED | Critical problem | Supervisor, Maintenance | 2 minutes | Immediate assistance, solve or escalate |
| 🟡 YELLOW | Minor issue | Team Leader | 5 minutes | Check status, provide support if needed |
| 🟢 GREEN | Normal | N/A | N/A | Continue production |
| 🔵 BLUE | Material needed | Material Handler | 10 minutes | Deliver material, refill supplies |

#### Andon Board Template

**Work Center Andon Board**

```
┌────────────────────────────────────────────────────┐
│              SHOP ANDON STATUS BOARD               │
├──────┬─────────┬────────┬─────────┬──────────────┤
│ Wk   │ Machine │ Status │ Time    │ Issue        │
│ Ctr  │ ID      │ Light  │ Elapsed │ Description  │
├──────┼─────────┼────────┼─────────┼──────────────┤
│ A1   │ Mill-01 │   🟢   │   --    │ Normal       │
├──────┼─────────┼────────┼─────────┼──────────────┤
│ A2   │ Lathe-3 │   🔴   │  3 min  │ Tool break   │
├──────┼─────────┼────────┼─────────┼──────────────┤
│ A3   │ Mill-02 │   🔵   │  8 min  │ Need bar     │
├──────┼─────────┼────────┼─────────┼──────────────┤
│ B1   │ Lathe-1 │   🟢   │   --    │ Normal       │
├──────┼─────────┼────────┼─────────┼──────────────┤
│ B2   │ VMC-05  │   🟡   │  2 min  │ Part inspect │
└──────┴─────────┴────────┴─────────┴──────────────┘

RESPONSE TIMES TODAY:
Average: _____ min  |  Target: <5 min  |  Status: ________
```

### 15.4 Shadow Board Template

**Purpose:** Visual tool organization - every tool has a designated place.

**Shadow Board Design Principles:**
- ☐ Outline of tool painted or taped on board
- ☐ Tool name labeled at location
- ☐ Missing tools immediately obvious
- ☐ Most-used tools at easiest reach
- ☐ Color coding by frequency (daily, weekly, rarely)
- ☐ Damaged/calibration due tools marked differently

**Example Layout:**

```
┌───────────────────────────────────────────────────────┐
│              TOOL SHADOW BOARD - MILL 3               │
├───────────────────────────────────────────────────────┤
│                                                       │
│   ╔════════╗    ╔══════╗    ╔═══════╗               │
│   ║        ║    ║      ║    ║       ║               │
│   ║ 6" Adj ║    ║ 8" C ║    ║ Hammer║               │
│   ║ Wrench ║    ║Wrench║    ║       ║               │
│   ╚════════╝    ╚══════╝    ╚═══════╝               │
│                                                       │
│   ┌────────┐    ┌──────┐    ┌───────┐    ┌───────┐ │
│   │  Hex   │    │Allen │    │ Torx  │    │ Screw │ │
│   │  Key   │    │ Set  │    │  Set  │    │Driver │ │
│   │  Set   │    │      │    │       │    │  Set  │ │
│   └────────┘    └──────┘    └───────┘    └───────┘ │
│                                                       │
│   [════════]    [══════]    [══════════]             │
│   12" Scale     6" Scale    Digital Caliper          │
│                                                       │
└───────────────────────────────────────────────────────┘

LEGEND:  Daily Use = GREEN    Weekly = YELLOW    Rare = RED
```

### 15.5 Floor Marking Standards

**Purpose:** Create visual workplace with clear pathways, locations, and boundaries.

#### Color Standards (OSHA-based)

| Color | Meaning | Examples |
|-------|---------|----------|
| **YELLOW** | Caution, traffic lanes | Aisles, walkways, forklift paths |
| **WHITE** | Production areas | Work cells, machine locations |
| **RED** | Safety, fire equipment | Fire extinguishers, emergency stops, defect areas |
| **BLUE** | Information, storage | Raw material, WIP holding, tool storage |
| **GREEN** | Finished goods, safety | Completed parts, first aid stations, safety equipment |
| **ORANGE** | Hazardous areas | Machine hazard zones, pinch points |
| **BLACK/YELLOW STRIPE** | Permanent hazards | Columns, protruding structures, height clearances |

#### Floor Marking Plan Template

**Area:** __________ **Designer:** __________ **Date:** __________

| Location | Marking Type | Color | Purpose | Size/Spec |
|----------|--------------|-------|---------|-----------|
|  | ☐ Solid line ☐ Dashed ☐ Shape |  |  | __" width |
|  | ☐ Solid line ☐ Dashed ☐ Shape |  |  | __" width |
|  | ☐ Solid line ☐ Dashed ☐ Shape |  |  | __" width |

**Standards:**
- Main aisles: 4" yellow lines
- Work cells: 2" white lines
- Storage locations: 2" blue shapes/borders
- Safety zones: 2-4" red or orange
- Arrows: Show direction of flow

---

## 16. Standardized Work Templates

### 16.1 Standardized Work Chart

**Process:** __________ **Part #:** __________ **Rev:** ____ **Date:** ____

**Takt Time:** _____ sec | **Cycle Time:** _____ sec | **WIP:** _____ pcs

#### Work Sequence

| Step | Work Element | Time (sec) | Wait Time (sec) | Walk Distance (ft) | Quality Check | Safety |
|------|--------------|------------|-----------------|-------------------|---------------|--------|
| 1 |  |  |  |  | ☐ | ☐ |
| 2 |  |  |  |  | ☐ | ☐ |
| 3 |  |  |  |  | ☐ | ☐ |
| 4 |  |  |  |  | ☐ | ☐ |
| 5 |  |  |  |  | ☐ | ☐ |
| 6 |  |  |  |  | ☐ | ☐ |
| 7 |  |  |  |  | ☐ | ☐ |
| 8 |  |  |  |  | ☐ | ☐ |
| 9 |  |  |  |  | ☐ | ☐ |
| 10 |  |  |  |  | ☐ | ☐ |

**Total Manual Time:** _____ sec
**Total Auto Time:** _____ sec
**Total Cycle Time:** _____ sec

**Critical Quality Points:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Safety Cautions:**
1. _________________________________________________
2. _________________________________________________

### 16.2 Standardized Work Combination Sheet

**Purpose:** Balance operator time with machine auto time.

**Process:** __________ **Part #:** __________ **Operator:** ____

**Timeline Chart:**

```
Time (seconds) →
0    10    20    30    40    50    60    70    80    90   100
├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤

MANUAL  ████░░░░░░██████░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░
WORK

AUTO    ░░░░██████░░░░░░██████████░░░░░░░░░░░░░░░░░░░░░░░
TIME

WALK    ░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░


Legend:  █ = Work time   ░ = Available/Wait time   TAKT = ▼
```

**Analysis:**
- Total cycle time: _____ sec
- Takt time: _____ sec
- Status: ☐ Under takt (OK) ☐ Over takt (Problem) ☐ Close to takt (Risk)
- Operator utilization: _____% (Manual time ÷ Cycle time)
- Idle time: _____ sec per cycle

**Improvement Opportunities:**
- _________________________________________________
- _________________________________________________

### 16.3 Job Instruction Sheet

**Job:** __________ **Part #:** __________ **Revision:** ____ **Date:** ____

**Tools/Equipment Required:**
- _________________________________________________
- _________________________________________________

**Safety Equipment Required:**
☐ Safety glasses  ☐ Gloves  ☐ Hearing protection  ☐ Other: __________

#### Detailed Instructions

| Step | Key Point | Reason | Photo/Diagram |
|------|-----------|--------|---------------|
| 1 |  |  | [Reference] |
| 2 |  |  | [Reference] |
| 3 |  |  | [Reference] |
| 4 |  |  | [Reference] |
| 5 |  |  | [Reference] |

**Key Point:** Critical technique, dimension, or detail that ensures quality/safety
**Reason:** Why this key point matters

**Quality Checks:**

| What to Check | How to Check | Frequency | Specification |
|---------------|--------------|-----------|---------------|
|  |  |  |  |
|  |  |  |  |

**Common Mistakes to Avoid:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Troubleshooting:**

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
|  |  |  |
|  |  |  |

**Approved By:** _________________ **Date:** _____ **Training:** ☐ Complete

---

## 17. Lean Metrics Dashboard

### 17.1 Shop-Level Lean Metrics

**Month:** __________ **Year:** __________

#### Primary Metrics

| Metric | Target | This Month | Last Month | YTD | Trend |
|--------|--------|------------|------------|-----|-------|
| **On-Time Delivery %** | 95% |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| **Overall OEE %** | 75% |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| **First Pass Yield %** | 98% |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| **Inventory Turns** | 12/yr |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| **Lead Time (days)** | <7 |  |  |  | ☐ ↑ ☐ → ☐ ↓ |
| **Setup Time Avg (min)** | <30 |  |  |  | ☐ ↑ ☐ → ☐ ↓ |

#### Supporting Metrics

| Metric | This Month | Last Month | Target |
|--------|------------|------------|--------|
| WIP Inventory ($) |  |  |  |
| Days of WIP |  |  | <3 |
| Raw Material Turns |  |  | >24/yr |
| Finished Goods Turns |  |  | >52/yr |
| Average Batch Size |  |  | Decreasing |
| Defect Rate (PPM) |  |  | <5,000 |
| Scrap Cost ($) |  |  | <2% sales |
| Equipment Downtime % |  |  | <5% |
| Safety Incidents |  |  | 0 |
| Near Misses Reported |  |  | >5/month |
| Kaizen Events |  |  | 2/month |
| Improvement Ideas Submitted |  |  | 10/month |

### 17.2 Value Stream Performance Metrics

**Value Stream:** __________ **Month:** __________

#### Flow Metrics

**Lead Time Analysis:**

| Stage | Days | % of Total |
|-------|------|------------|
| Order Entry | | % |
| Material Procurement | | % |
| Queue/Wait | | % |
| Production | | % |
| Inspection | | % |
| Shipping | | % |
| **TOTAL LEAD TIME** | | **100%** |

**Value-Added Ratio:**
- Total Lead Time: _____ days
- Value-Added Time: _____ days (actual processing)
- VA Ratio: _____% (Target: >10%)

#### Pull System Health

| Indicator | Status | Notes |
|-----------|--------|-------|
| Kanban stockouts | ☐ None ☐ Few ☐ Many |  |
| Overstock situations | ☐ None ☐ Few ☐ Many |  |
| Pull rule compliance | ☐ 100% ☐ >90% ☐ <90% |  |
| Replenishment responsiveness | ☐ Good ☐ OK ☐ Poor |  |

### 17.3 Continuous Improvement Metrics

**Kaizen Activity Tracking:**

| Month | Events Held | Participants | Ideas Generated | Ideas Implemented | Savings ($) |
|-------|-------------|--------------|-----------------|-------------------|-------------|
| Jan |  |  |  |  |  |
| Feb |  |  |  |  |  |
| Mar |  |  |  |  |  |
| YTD |  |  |  |  |  |

**Improvement Project Pipeline:**

| Status | Count | Total Savings Potential |
|--------|-------|------------------------|
| Ideas Submitted |  | $ |
| Under Evaluation |  | $ |
| Approved/In Progress |  | $ |
| Completed This Month |  | $ |
| Completed YTD |  | $ |

---

## 18. A3 Problem Solving Template

### 18.1 A3 Report Structure

**A3 Title:** _______________________
**Owner:** __________ **Date:** __________ **Status:** ☐ In Progress ☐ Complete

**1. Background / Problem Statement** (Top Left)

What is the problem?
_________________________________________________________________
_________________________________________________________________

Where/when does it occur?
_________________________________________________________________

Why is it important?
_________________________________________________________________

**2. Current Condition** (Top Right)

Current performance data:
- Metric: _____ (current) vs _____ (target)
- Frequency: _____
- Cost impact: $_____

Visual representation (chart, graph, photo):
[Attach visual]

**3. Goal / Target Condition** (Middle Left)

What does success look like?
_________________________________________________________________

Specific, measurable targets:
- _________________________________________________
- _________________________________________________

By when: __________

**4. Root Cause Analysis** (Middle Left)

What analysis was done?
☐ 5 Whys  ☐ Fishbone  ☐ Pareto  ☐ Data analysis  ☐ Other: _____

Root causes identified:
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

[Attach analysis diagrams]

**5. Countermeasures / Solutions** (Middle Right)

| Countermeasure | Addresses Root Cause | Impact | Feasibility | Priority |
|----------------|---------------------|--------|-------------|----------|
|  |  | H/M/L | H/M/L | |
|  |  | H/M/L | H/M/L | |
|  |  | H/M/L | H/M/L | |

Selected solution(s):
_________________________________________________________________

**6. Implementation Plan** (Bottom Left)

| Action | Responsible | Resources | Target Date | Status |
|--------|-------------|-----------|-------------|--------|
|  |  |  |  | ☐ ☐ ☐ |
|  |  |  |  | ☐ ☐ ☐ |
|  |  |  |  | ☐ ☐ ☐ |

**7. Follow-Up / Results** (Bottom Right)

Results after implementation:
- Metric: _____ (before) → _____ (after)
- Improvement: _____% or _____ units
- Cost impact: $_____ saved/avoided

Lessons learned:
_________________________________________________________________

Standardization plan:
☐ Procedure updated  ☐ Training completed  ☐ Metrics tracking

Horizontal deployment opportunities:
_________________________________________________________________

---

## 19. Lean Implementation Roadmap

### 19.1 Lean Journey Phases

**Phase 1: Foundation (Months 1-3)**

**Goals:**
- Build lean knowledge
- Stabilize basics
- Create foundation for improvement

**Activities:**
- ☐ Leadership lean training (2 days)
- ☐ 5S implementation (all areas)
- ☐ Visual management basics
- ☐ Standard work for key processes
- ☐ TPM basics (autonomous maintenance)
- ☐ Metrics dashboard established
- ☐ First kaizen event

**Success Criteria:**
- 5S audit scores >80%
- Visual boards in all areas
- 3+ standard work documents created
- Metrics tracked weekly
- 1 completed kaizen event

---

**Phase 2: Flow and Pull (Months 4-9)**

**Goals:**
- Reduce lead time
- Implement pull systems
- Improve flow

**Activities:**
- ☐ Value stream mapping (2-3 value streams)
- ☐ Setup reduction (SMED) on bottleneck machines
- ☐ Kanban pilot for 1-2 product families
- ☐ Cell/flow design for high-runner products
- ☐ Leveled scheduling (heijunka) pilot
- ☐ 2-3 kaizen events per month
- ☐ Error-proofing (poka-yoke) implementations

**Success Criteria:**
- Lead time reduced 30%
- WIP reduced 40%
- Kanban functioning for pilot products
- 3+ SMED improvements completed
- 6+ kaizen events completed

---

**Phase 3: Optimization (Months 10-18)**

**Goals:**
- Expand pull systems
- Optimize equipment reliability
- Develop problem-solving culture

**Activities:**
- ☐ Expand kanban to all products
- ☐ Advanced TPM (planned maintenance, OEE tracking)
- ☐ Continuous flow expansion
- ☐ Supplier integration/pull
- ☐ A3 problem-solving training and practice
- ☐ Hoshin Kanri (policy deployment) introduction
- ☐ 2-3 kaizen events per month sustained

**Success Criteria:**
- OEE >75%
- Pull systems operational shop-wide
- On-time delivery >95%
- 20+ kaizen events completed YTD
- Employee engagement in improvement >70%

---

**Phase 4: Culture and Excellence (Months 18+)**

**Goals:**
- Embed continuous improvement culture
- Pursue operational excellence
- Self-sustaining improvement

**Activities:**
- ☐ Daily huddle systems at all levels
- ☐ Leader standard work
- ☐ Advanced metrics and analytics
- ☐ Value stream management
- ☐ Cross-training and skill development
- ☐ Innovation and advanced improvement methods

**Success Criteria:**
- Self-directed improvement teams
- Idea implementation rate >60%
- World-class metrics (OEE >85%, OTD >98%)
- Lean assessment score >4.0/5.0
- Recognized as lean model shop

### 19.2 Lean Assessment Scorecard

**Assessment Date:** __________ **Assessor:** __________

Rate each category: 1=Beginning, 2=Developing, 3=Established, 4=Advanced, 5=World Class

| Category | Score (1-5) | Evidence | Priority Actions |
|----------|-------------|----------|------------------|
| **5S and Visual Workplace** | | | |
| **Standardized Work** | | | |
| **Setup Reduction (SMED)** | | | |
| **TPM/Equipment Reliability** | | | |
| **Quality at Source** | | | |
| **Pull/Kanban Systems** | | | |
| **Flow/Cell Design** | | | |
| **Continuous Improvement Culture** | | | |
| **Problem Solving (A3, kaizen)** | | | |
| **Metrics and Performance Management** | | | |
| **Leadership and Management System** | | | |
| **Employee Engagement** | | | |
| **TOTAL SCORE** | **/60** | | |

**Overall Lean Maturity:**
- 12-20: Beginning Journey
- 21-35: Developing Capability
- 36-47: Established System
- 48-55: Advanced Performance
- 56-60: World Class

### 19.3 Annual Lean Plan Template

**Year:** __________ **Prepared By:** __________ **Approved:** __________

#### Strategic Objectives

1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

#### Key Metrics Targets

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| Lead Time | ___days | ___days | ___% |
| OEE | ___% | ___% | ___pts |
| On-Time Delivery | ___% | ___% | ___pts |
| Inventory Turns | ___ | ___ | ___ |
| First Pass Yield | ___% | ___% | ___pts |

#### Major Initiatives

| Initiative | Owner | Timeline | Resources | Expected Impact |
|------------|-------|----------|-----------|-----------------|
|  |  | Q1 Q2 Q3 Q4 |  |  |
|  |  | Q1 Q2 Q3 Q4 |  |  |
|  |  | Q1 Q2 Q3 Q4 |  |  |

#### Kaizen Event Calendar

**Target:** _____ events for the year (monthly schedule)

| Month | Event Focus | Facilitator | Status |
|-------|-------------|-------------|--------|
| Jan |  |  | ☐ Planned ☐ Complete |
| Feb |  |  | ☐ Planned ☐ Complete |
| Mar |  |  | ☐ Planned ☐ Complete |
| Apr |  |  | ☐ Planned ☐ Complete |
| May |  |  | ☐ Planned ☐ Complete |
| Jun |  |  | ☐ Planned ☐ Complete |
| Jul |  |  | ☐ Planned ☐ Complete |
| Aug |  |  | ☐ Planned ☐ Complete |
| Sep |  |  | ☐ Planned ☐ Complete |
| Oct |  |  | ☐ Planned ☐ Complete |
| Nov |  |  | ☐ Planned ☐ Complete |
| Dec |  |  | ☐ Planned ☐ Complete |

#### Training Plan

| Training Topic | Target Audience | Frequency | Provider |
|----------------|-----------------|-----------|----------|
| Lean Fundamentals | All employees | Annual | Internal |
| 5S Training | New hires | Onboarding | Supervisor |
| Standard Work | Leads, supervisors | Quarterly | Internal |
| SMED | Setup specialists | Semi-annual | Consultant |
| A3 Problem Solving | Engineers, leads | Semi-annual | Internal |
| Kaizen Facilitation | Leaders | Annual | External |

#### Resource Budget

| Category | Budget ($) |
|----------|-----------|
| Training |  |
| Consulting |  |
| Capital (equipment, tools) |  |
| Supplies and materials |  |
| Events and recognition |  |
| **TOTAL** |  |

---

## 20. Summary and Usage Guide

### Template Selection Guide

**Starting Out?**
→ Use Part 1: VSM, DOWNTIME assessment, Takt time calculator

**Implementing Pull?**
→ Use Part 2: Kanban design, supermarket planning, Heijunka

**Improving Reliability?**
→ Use Part 3: SMED, TPM, Poka-yoke, Kaizen event planning

**Creating Visual Management?**
→ Use Part 4: Visual boards, standardized work, metrics dashboards, A3

### Implementation Sequence Recommendation

1. **Start with 5S and visual management** - Creates foundation
2. **Develop standard work** - Documents current best practice
3. **Map value streams** - Understand current state, identify waste
4. **Implement pull systems** - Reduce inventory, improve flow
5. **Reduce setup times (SMED)** - Enable smaller batches
6. **Improve reliability (TPM)** - Stabilize processes
7. **Error-proof (Poka-yoke)** - Prevent defects
8. **Run kaizen events** - Accelerate improvement
9. **Measure and visualize** - Track progress
10. **Problem-solve systematically (A3)** - Build capability

### Customization Tips

- Adapt all templates to your shop's terminology and culture
- Simplify for smaller shops (you don't need all fields)
- Digitize when helpful, but paper works fine for many tools
- Focus on usefulness, not perfection
- Involve team in template design for buy-in

### Additional Resources

**Recommended Books:**
- "Learning to See" (Rother & Shook) - VSM workbook
- "Quick Changeover for Operators" (Productivity Press) - SMED
- "Creating Continuous Flow" (Rother & Harris) - Flow design
- "The Toyota Way Fieldbook" (Liker & Meier) - Practical implementation

**Software Tools:**
- **Free:** Excel, Google Sheets for tracking
- **Low-Cost:** iAuditor (checklists), Trello (kaizen boards)
- **Mid-Range:** Minitab, Power BI (analytics)
- **Enterprise:** ERP systems with lean modules

**Associations:**
- Lean Enterprise Institute (LEI)
- Society of Manufacturing Engineers (SME)
- Association for Manufacturing Excellence (AME)
- Shingo Institute

---

## Conclusion

These templates provide a complete toolkit for implementing L.E.A.N. strategies in your CNC manufacturing operation. Remember:

✓ **Start small** - Pilot before rolling out shop-wide
✓ **Engage people** - Improvement is everyone's job
✓ **Be patient** - Lean is a journey, not a destination
✓ **Measure results** - Data drives improvement
✓ **Sustain gains** - Standardize successful changes
✓ **Keep learning** - Continuous improvement applies to your lean system too

**Final Thought:** Lean isn't about the templates—it's about developing people who see problems, solve them systematically, and continuously improve. Use these tools to enable that culture.

---

*This completes Appendix S: L.E.A.N. Strategy Templates and Tools. These templates support Module 24: L.E.A.N. Strategies and provide practical implementation guidance for CNC shops of all sizes.*

**Appendix S Parts:**
- Part 1: VSM, DOWNTIME, Process Observation
- Part 2: JIT, Kanban, Pull Systems, Heijunka
- Part 3: SMED, TPM, Poka-Yoke, Kaizen Events
- Part 4: Visual Management, Standard Work, Metrics, A3, Implementation

**Total Pages: ~85 pages of practical lean tools and templates**
