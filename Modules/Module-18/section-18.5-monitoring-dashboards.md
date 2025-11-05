# Section 18.5: Real-Time Monitoring and Dashboard Design

## Introduction

Data acquisition, communication, and storage provide the foundation for smart manufacturing, but the value is realized through effective visualization and monitoring. Well-designed dashboards transform raw sensor data into actionable insights, enabling operators to respond to problems quickly, maintenance teams to prioritize interventions, and management to track performance trends.

This section examines the selection of key performance indicators (KPIs), dashboard platform options, real-time alerting systems, visualization best practices, mobile monitoring capabilities, and multi-machine fleet dashboards that provide comprehensive operational visibility.

## Key Performance Indicators (KPIs) for CNC Monitoring

Effective dashboards focus on metrics that drive business outcomes. Too many metrics create information overload; too few miss critical issues. The following KPIs provide comprehensive coverage for CNC operations.

### Overall Equipment Effectiveness (OEE)

OEE is the gold standard manufacturing metric, measuring the percentage of planned production time that is truly productive.

**Formula:**
```
OEE = Availability × Performance × Quality
```

**Availability:** Percentage of scheduled time that machine is running (not down for breakdowns, changeovers, or shortages).
```
Availability = (Planned Production Time - Downtime) / Planned Production Time
```

**Performance:** Actual production rate vs. ideal rate (accounting for slow cycles and minor stops).
```
Performance = (Actual Cycle Time / Ideal Cycle Time) × (Parts Produced / Target Parts)
```

**Quality:** Good parts vs. total parts produced.
```
Quality = (Good Parts - Defective Parts) / Good Parts
```

**Example Calculation:**

Planned production time: 480 minutes (8-hour shift)
Unplanned downtime: 47 minutes (breakdown + material shortage)
Availability = (480 - 47) / 480 = 90.2%

Ideal cycle time: 60 seconds/part
Actual average cycle time: 75 seconds/part (slow feeds due to tool wear)
Target parts: 433 parts (480 min × 60 sec/min ÷ 60 sec/part)
Actual parts produced: 347 parts
Performance = (60/75) × (347/433) = 0.80 × 0.80 = 64.1%

Good parts: 347
Defective parts: 13 (scrapped due to dimensional errors)
Quality = (347 - 13) / 347 = 96.3%

**OEE = 90.2% × 64.1% × 96.3% = 55.7%**

World-class OEE is 85%+. This example machine has significant performance losses to address.

**Dashboard Display:**

OEE is best displayed as:
- Current shift OEE (primary metric)
- 7-day trend line (identify patterns)
- Pareto chart showing loss breakdown (availability, performance, quality)
- Target OEE line (visual comparison to goal)

**Data Requirements:**
- Machine running status (from controller or current sensor)
- Part counts (from controller or vision system)
- Quality inspection results (manual or automated)
- Cycle time per part

### Spindle Utilization

Percentage of time spindle motor is actively cutting (not idle, loading, or changing tools).

**Formula:**
```
Spindle Utilization = (Spindle Cutting Time) / (Total Machine Running Time) × 100%
```

**Measurement:** Monitor spindle motor current. Cutting current typically 20-80% of rated current. Idle current <10% of rated.

**Threshold Example:**
- Cutting: Spindle current >15% of rated
- Idle: Spindle current <15% of rated

**Typical Values:**
- Lights-out automated cell: 70-85% utilization
- Operator-attended manual loading: 40-60% utilization
- Job shop with frequent setups: 25-40% utilization

**Dashboard Display:**
- Gauge showing current utilization percentage
- Breakdown: Cutting time vs. idle time vs. tool change time
- Trend: Utilization over past 30 days (detect declining trends)

Low utilization indicates opportunities to reduce cycle time by optimizing tool paths, reducing air cuts, or improving material handling.

### Cycle Time

Time from part start to part completion. Critical for production planning and detecting process degradation.

**Measurement Methods:**
- Program cycle time from CNC controller (M30 program end to next cycle start)
- Part counter increments (time between counts)
- Door close to door open cycle (for operator-loaded machines)

**Dashboard Display:**
- Current part cycle time
- Average cycle time for current job
- Trend chart: Cycle time over past 100 parts (detect tool wear causing feeds/speeds reduction)
- Target cycle time line

**Cycle Time Variability:** High variability (standard deviation >10% of mean) indicates process instability—investigate tool wear, fixturing issues, or material variation.

### Alarm Frequency and Duration

Machine alarms indicate problems requiring intervention. Tracking alarm patterns reveals chronic issues.

**Metrics:**
- Total alarm count per shift
- Mean time to acknowledge (operator response time)
- Mean time to clear (problem resolution time)
- Top 10 alarms by frequency (Pareto analysis)

**Example:**
Alarm: "Low coolant flow" occurred 23 times in past week
Average duration: 4.2 minutes
**Action:** Inspect coolant system, likely clogged filter or failing pump

**Dashboard Display:**
- Active alarms (red banner at top of dashboard)
- Alarm history table (timestamp, alarm code, duration, resolution)
- Pareto chart of most frequent alarms
- Alarm-free operating time counter (gamification for operators)

### Temperature Monitoring

Critical for thermal stability and preventing bearing failures.

**Key Temperature Points:**
- Spindle bearing: Normal 40-60°C, warning >70°C, alarm >80°C
- Servo motors: Normal 50-70°C, warning >80°C, alarm >90°C
- Coolant: Normal 20-25°C, warning >30°C
- Hydraulic oil: Normal 40-50°C, warning >60°C, alarm >70°C

**Dashboard Display:**
- Multi-sensor temperature plot (all temperatures on one chart with different colors)
- Alarm thresholds shown as horizontal lines
- Historical maximum temperature per shift (detect gradual increases indicating developing problems)

### Vibration Monitoring

**Metrics:**
- Vibration RMS (root mean square) velocity in mm/s
- ISO 10816 severity zones:
  - Zone A (green, <1.8 mm/s): Good condition
  - Zone B (yellow, 1.8-4.5 mm/s): Acceptable
  - Zone C (orange, 4.5-11.2 mm/s): Unsatisfactory, plan maintenance
  - Zone D (red, >11.2 mm/s): Unacceptable, immediate action required

**Dashboard Display:**
- Vibration gauge with ISO zones color-coded
- FFT spectrum (frequency analysis) for diagnostic purposes
- Vibration trend: Weekly maximum vibration over past 6 months

### Tool Life Tracking

**Metrics:**
- Cumulative cutting time per tool
- Parts produced per tool
- Estimated remaining tool life percentage
- Unscheduled tool changes (breakage) vs. scheduled changes

**Dashboard Display:**
- Tool life gauges for all active tools in magazine
- Red/yellow/green status indicators
- Predicted tool change time (based on current production rate)

**Data Source:** CNC controller tool life counters, or calculated from spindle current (high current indicates dull tool).

### Energy Consumption

**Metrics:**
- kWh per part produced (energy intensity)
- Peak power demand (kW)
- Total daily/weekly energy consumption
- Energy cost per shift

**Dashboard Display:**
- Real-time power meter (kW)
- Energy per part trend (detect inefficiencies)
- Comparison to baseline or similar machines

**Cost Calculation:**
If electricity cost is $0.12/kWh and machine draws average 15 kW while running:
- Energy per hour: 15 kWh × $0.12 = $1.80/hour
- 8-hour shift: $14.40/shift
- Annual (2-shift, 250 days/year): $7,200/year per machine

## Dashboard Platforms

### Grafana (Open-Source)

**Overview:** Leading open-source dashboard and visualization platform with extensive data source support.

**Key Features:**
- 150+ data source plugins (InfluxDB, Prometheus, PostgreSQL, MySQL, AWS CloudWatch, Azure Monitor, etc.)
- Rich visualization library: Time-series graphs, gauges, tables, heat maps, 3D panels
- Alerting with notification channels (email, Slack, PagerDuty, SMS via Twilio)
- Template variables for creating reusable dashboards (select machine from dropdown, dashboard updates)
- User authentication and role-based access control

**Deployment:**
- Self-hosted: Free open-source, run on Linux/Windows/Docker
- Grafana Cloud: Managed service, free tier (10k series, 50 GB logs, 14-day retention), paid tiers $49-299+/month

**Typical Implementation:**

```
Data Flow:
Sensors → InfluxDB/TimescaleDB/Prometheus → Grafana Dashboard
```

**Dashboard Example - Machine Overview:**

Panel 1: OEE gauge (current shift)
Panel 2: Spindle utilization bar chart
Panel 3: Temperature multi-line graph (past 4 hours)
Panel 4: Vibration gauge with ISO zones
Panel 5: Active alarms table
Panel 6: Parts produced counter
Panel 7: Cycle time trend (past 100 parts)

**Advantages:**
- Free and open-source
- Huge community and plugin ecosystem
- Flexible and customizable
- Vendor-neutral (works with any database)

**Disadvantages:**
- Requires technical expertise to configure
- Limited pre-built manufacturing templates (must build from scratch)
- Self-hosted requires server administration

**Cost:**
- Self-hosted: $0 software + $50-150/month for server (small-medium deployment)
- Grafana Cloud: $0 (free tier) to $299/month (professional tier)

### Tableau

**Overview:** Enterprise business intelligence platform with powerful analytics and visualization.

**Key Features:**
- Drag-and-drop interface (low-code, business user friendly)
- Advanced analytics: Forecasting, trend lines, statistical functions
- Data blending: Combine data from multiple sources (join time-series sensor data with ERP production orders)
- Mobile apps for iOS/Android
- Sharing and collaboration features

**Deployment:**
- Tableau Desktop: Windows/Mac application for creating dashboards
- Tableau Server: On-premise web server for sharing dashboards
- Tableau Cloud: SaaS hosted service

**Manufacturing Use Cases:**
- Executive dashboards (plant-wide KPIs, production vs. plan)
- Quality analytics (correlate defects with process parameters)
- Cross-functional reporting (combine OEE, maintenance, quality, cost data)

**Advantages:**
- Intuitive interface for non-technical users
- Powerful analytics and calculations
- Beautiful, publication-quality visualizations
- Strong data governance and security

**Disadvantages:**
- High cost
- Overkill for simple real-time monitoring (better suited to business analytics)
- Less optimized for high-frequency time-series updates

**Cost:**
- Tableau Desktop: $70/user/month (Creator license)
- Tableau Server: $35/user/month (Viewer license) + server infrastructure
- Tableau Cloud: $42/user/month (Explorer license)

Typical cost for 10 users (2 creators, 8 viewers): $900/month

### Microsoft Power BI

**Overview:** Microsoft's business intelligence platform, tightly integrated with Azure and Office 365.

**Key Features:**
- Data modeling and transformation (Power Query)
- DAX formula language for complex calculations
- Integration with Excel, SharePoint, Teams
- Power BI Mobile apps
- Natural language queries ("show me OEE by machine last week")

**Deployment:**
- Power BI Desktop: Free Windows application for creating reports
- Power BI Service: Cloud service for sharing dashboards
- Power BI Premium: Dedicated cloud capacity for large organizations

**Advantages:**
- Low cost (especially if already Microsoft 365 customer)
- Familiar interface for Excel users
- Excellent integration with Microsoft ecosystem
- Growing manufacturing templates and community

**Disadvantages:**
- Windows-only for Desktop (Mac/Linux users must use web interface)
- Limited real-time streaming (1 second refresh minimum, designed for periodic updates)
- Less flexible than Grafana for time-series data

**Cost:**
- Power BI Desktop: Free
- Power BI Pro: $10/user/month (cloud sharing)
- Power BI Premium: $20/user/month or $4,995/month (dedicated capacity)

Typical cost for 20 users: $200/month (Pro licenses)

### Custom Web Applications

**Overview:** Build dashboards using web frameworks (React, Vue, Angular) with charting libraries (Chart.js, D3.js, Highcharts, Plotly).

**When to Build Custom:**
- Unique requirements not met by commercial platforms
- Embed dashboards in existing web applications
- Maximum control over appearance and functionality
- Avoid per-user licensing costs for large user bases

**Technology Stack Example:**
- Frontend: React + TypeScript
- Charting: Plotly.js (interactive time-series charts)
- Data API: Node.js Express server
- Database: TimescaleDB (PostgreSQL)
- Hosting: AWS EC2 or containerized (Docker + Kubernetes)

**Development Cost:**
- Initial build: 200-500 hours ($20,000-75,000 at $100/hour)
- Ongoing maintenance: 5-10 hours/month ($500-1,000/month)

**Advantages:**
- Complete customization
- No per-user licensing fees
- Can integrate tightly with proprietary systems
- Intellectual property ownership

**Disadvantages:**
- High initial cost
- Requires software development expertise
- Ongoing maintenance responsibility
- Longer time to first value

**When Custom Makes Sense:**
- Very large user bases (100+ users, licensing costs exceed development costs)
- Highly specialized requirements
- Integration with complex proprietary systems
- Development team already available in-house

## Real-Time Alerting

Dashboards are pull-based (user looks at dashboard). Alerts are push-based (system notifies user). Critical for time-sensitive problems.

### Alert Channels

**Email Alerts:**
- Appropriate for: Non-urgent issues, daily/weekly summary reports
- Response time: Minutes to hours (users don't constantly check email)
- Cost: Free (SMTP server) or $0.001-0.01 per email (SendGrid, AWS SES)

**SMS/Text Alerts:**
- Appropriate for: Urgent issues requiring immediate attention (machine breakdown, safety alarm)
- Response time: Seconds to minutes (high attention rate)
- Cost: $0.01-0.05 per message (Twilio, AWS SNS)

**Example:** 100 SMS alerts/month = $2-5/month

**Push Notifications (Mobile Apps):**
- Appropriate for: Medium-urgency issues, targeted to on-duty personnel
- Response time: Seconds to minutes
- Cost: Free (Firebase Cloud Messaging, Apple Push Notification Service)

**Voice Calls:**
- Appropriate for: Critical emergencies, escalation if SMS not acknowledged
- Cost: $0.01-0.05 per minute (Twilio Voice)

**Collaboration Platforms (Slack, Microsoft Teams):**
- Appropriate for: Team notifications, shift handoffs, maintenance requests
- Response time: Minutes (if team actively monitoring channel)
- Cost: Included in platform subscription

### Alert Thresholds and Logic

**Simple Threshold:**
```
IF spindle_temperature > 75°C THEN send_alert("High spindle temperature")
```

**Hysteresis (prevent alert flapping):**
```
IF spindle_temperature > 75°C THEN set_alarm()
IF spindle_temperature < 70°C THEN clear_alarm()
```
Alarm triggers at 75°C but doesn't clear until temperature drops below 70°C, preventing rapid on/off toggling.

**Rate of Change:**
```
IF (current_temperature - temperature_10min_ago) > 15°C THEN send_alert("Rapid temperature rise")
```
Detects abnormal transients even if absolute value not yet critical.

**Statistical Anomaly:**
```
IF vibration_rms > (30_day_mean + 3 × std_dev) THEN send_alert("Abnormal vibration")
```
Adapts to machine's normal baseline, alerts on deviations.

**Alarm Suppression (prevent alert storms):**
- Rate limiting: Maximum 1 alert per 15 minutes for same condition
- Acknowledge requirement: Subsequent alerts suppressed until operator acknowledges first alert
- Maintenance mode: Suppress alerts during scheduled maintenance windows

### Alert Escalation

For critical issues, use escalation chains:

**Tier 1 (0-5 minutes):** Notification to on-floor operator (push notification + audible alarm on HMI)

**Tier 2 (5-15 minutes):** If not acknowledged, SMS to shift supervisor + maintenance technician

**Tier 3 (15-30 minutes):** If still not resolved, phone call to maintenance manager + email to plant manager

### Alert Effectiveness Metrics

Track alert system performance:
- Mean time to acknowledge (MTTA): How quickly do personnel respond?
- Mean time to resolve (MTTR): How long until problem fixed?
- False alarm rate: Percentage of alerts that don't require action (target: <10%)

High false alarm rates cause alert fatigue—operators ignore alerts. Continuously tune thresholds to minimize false positives while catching real problems.

## Visualization Best Practices

### Color Coding

Use intuitive, universal color schemes:

**Status Colors:**
- Green: Normal, within spec, healthy
- Yellow: Warning, approaching limit, attention needed
- Red: Alarm, out of spec, immediate action required
- Gray: Offline, no data, disabled

**Trend Colors:**
- Blue: Neutral metric (temperature, speed—no inherent good/bad)
- Green: Positive trend (production increasing, cycle time decreasing)
- Red: Negative trend (defect rate increasing, efficiency declining)

**Avoid:**
- Red/green for non-status metrics (accessibility issue for colorblind users ~8% of males)
- Too many colors (>6 colors creates visual confusion)
- Low contrast (light yellow text on white background)

### Chart Type Selection

**Time-Series Line Chart:** Best for continuous data over time (temperature, vibration, cycle time). Shows trends and patterns clearly.

**Bar Chart:** Best for comparing discrete categories (OEE by machine, defects by type, production by shift).

**Gauge/Meter:** Best for single current values with defined ranges (OEE percentage, spindle utilization, temperature with alarm zones).

**Table:** Best for detailed data requiring exact values (alarm history, part counts, tool life remaining).

**Heat Map:** Best for patterns in 2D data (machine utilization by hour × day of week, revealing usage patterns).

**Pareto Chart:** Best for identifying top contributors (80/20 rule—80% of downtime from 20% of causes).

### Dashboard Layout

**F-Pattern Layout:** Users scan in F-shape (top-left → top-right → down left side). Place most important KPIs in top-left corner.

**Example Layout:**

```
┌─────────────────────────────────────────┐
│ [OEE Gauge]  [Status]  [Part Count]     │ ← Primary KPIs
├─────────────────────────────────────────┤
│ [Temperature Chart - 4 hours]           │ ← Key trends
├─────────────────────────────────────────┤
│ [Vibration] [Cycle Time] [Spindle Load] │ ← Secondary metrics
├─────────────────────────────────────────┤
│ [Active Alarms Table]                   │ ← Actionable details
└─────────────────────────────────────────┘
```

**Information Density:** Balance detail vs. clutter. One machine per screen for operator dashboards. Multi-machine fleet overviews can show 10-20 machines with simplified metrics (status + OEE only).

### Update Frequency

**Real-Time Metrics (1-5 second updates):**
- Current machine status (running/idle/alarm)
- Active alarms
- Spindle load, axis position (for operator monitoring during setup)

**Near-Real-Time (10-60 second updates):**
- Temperature, vibration (thermal/mechanical time constants in minutes)
- Part counts, cycle time
- OEE (updates at end of each cycle)

**Periodic Updates (5-60 minute updates):**
- Shift summaries
- Trend analyses
- Energy consumption totals

Avoid unnecessarily fast updates—updating temperature every second creates database load and visual distraction without adding value (temperature changes slowly).

### Responsive Design

Dashboards must work on multiple form factors:

- **Large Monitors (55" shop floor displays):** High information density, visible from distance (large fonts, high contrast)
- **Desktop/Laptop (engineering workstations):** Moderate density, detailed analysis tools
- **Tablets (supervisor rounds):** Touch-optimized, simplified interface
- **Smartphones (on-call alerts):** Minimal interface, critical metrics only

Use responsive web design techniques (CSS media queries, flexible grids) to adapt layout automatically.

## Mobile Monitoring Applications

### Native Mobile Apps

**Features:**
- Push notifications
- Offline functionality (cache recent data)
- Camera integration (photo documentation for maintenance)
- Touch-optimized controls

**Development:**
- iOS (Swift) + Android (Kotlin): $50,000-150,000 for initial development (separate codebases)
- Cross-platform (React Native, Flutter): $30,000-80,000 (single codebase for both platforms)

**When Justified:**
- Large organizations with 100+ machines
- Need for offline operation
- Integration with device features (GPS for technician tracking, camera, barcode scanner)

### Progressive Web Apps (PWA)

**Features:**
- Web-based but installable on home screen
- Push notification support
- Limited offline functionality
- Single codebase for all platforms

**Development:**
- Cost: $15,000-40,000
- Maintenance: Lower than native apps

**When to Choose PWA:**
- Faster time to market
- Limited budget
- Primarily online usage

### Mobile Dashboard Design Principles

**Prioritize Critical Information:**
Mobile screen: 375×667 pixels (iPhone SE) vs. 1920×1080 desktop
Show only essential metrics: Machine status, OEE, active alarms

**Large Touch Targets:**
Minimum 44×44 pixels for buttons (Apple Human Interface Guidelines)
Avoid tiny click targets requiring precision

**Simplified Navigation:**
Desktop: Multi-level menus acceptable
Mobile: Maximum 2 levels deep (top-level: machine list → detail: machine dashboard)

## Multi-Machine Fleet Dashboards

For facilities with 10-100+ machines, fleet-level visibility is essential for resource allocation and identifying systemic issues.

### Fleet Overview Design

**Heat Map Matrix:**
Rows: Machines (CNC-01 through CNC-50)
Columns: Metrics (Status, OEE, Temp, Vibration)
Colors: Green/yellow/red cells for quick visual scanning

Example: Glance reveals CNC-17 (yellow OEE) and CNC-23 (red temperature) need attention.

**Aggregated KPIs:**
- Fleet average OEE: 68.3%
- Machines running: 37/50 (74%)
- Machines in alarm: 3
- Total parts produced (shift): 4,847

**Filtering and Drill-Down:**
- Filter by: Production line, machine model, shift, operator
- Click machine → view detailed dashboard for that machine

### Comparative Analysis

**Peer Comparison:**
Show all machines of same model side-by-side:
- CNC-01 OEE: 72%, CNC-02: 68%, CNC-03: 81%, CNC-04: 59%
- Identify underperformers (CNC-04) and best performers (CNC-03)
- Investigate: Why is CNC-03 outperforming? Can practices be replicated?

**Trend Analysis:**
- Fleet OEE over past 90 days (detect gradual decline plant-wide)
- Seasonal patterns (December lower OEE due to holidays)

### Anomaly Highlighting

Automatically highlight outliers:
- CNC-17 vibration 3× higher than fleet average → maintenance needed
- CNC-09 cycle time 20% longer than expected → investigate tooling/programming

## Conclusion

Effective monitoring dashboards transform vast quantities of sensor data into actionable insights that drive operational improvements. The selection of meaningful KPIs—OEE, spindle utilization, cycle time, alarms, temperature, vibration—focuses attention on metrics that directly impact productivity and machine health.

Dashboard platforms range from powerful open-source tools like Grafana to enterprise business intelligence platforms like Tableau and Power BI, each with distinct strengths. Real-time alerting ensures time-sensitive problems receive immediate attention, while mobile applications enable monitoring from anywhere.

Visualization best practices—appropriate color coding, chart type selection, responsive layout—make dashboards intuitive and actionable. For multi-machine facilities, fleet dashboards provide high-level visibility while supporting drill-down to individual machine details.

With comprehensive monitoring in place, the next section examines how to move beyond reactive monitoring to proactive intervention through predictive maintenance and machine learning.

---

**Section 18.5 Complete**
*Word count: ~2,500 words*
*Technical depth: KPI calculations, platform comparisons, alert logic, visualization standards*
