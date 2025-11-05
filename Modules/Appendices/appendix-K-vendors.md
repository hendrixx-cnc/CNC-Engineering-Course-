# Appendix K: Vendor and Supplier Directory

---

## K.1 Linear Motion Components

### K.1.1 Ball Screws and Linear Guides

| Vendor | Products | Region | Website | Notes |
|--------|----------|--------|---------|-------|
| **THK** | Linear guides, ball screws, actuators | Global | thk.com | Premium quality, OEM standard |
| **HIWIN** | Linear guides, ball screws, ballscrews | Global | hiwin.com | Good quality, competitive pricing |
| **TBI Motion** | Ball screws, linear guides | Asia/Global | tbimotion.com | Budget-friendly, decent quality |
| **PMI (AMT)** | Linear guides, ball screws | Taiwan/Global | pmi-amt.com | Mid-range quality and price |
| **Schneeberger** | Linear guides, ball screws (ground) | Europe/USA | schneeberger.com | Ultra-precision, high cost |
| **SBC Linear** | Budget linear guides, SBR rails | China/Global | sbclinear.com | Budget CNC, DIY-friendly |

**Recommendation:**
- **Precision CNC:** THK or HIWIN HG-series (HGH blocks, C5 ball screws)
- **Budget CNC:** TBI Motion or PMI (C7 ball screws)
- **DIY/Hobbyist:** SBC Linear supported rails, rolled ball screws

### K.1.2 Rack and Pinion Systems

| Vendor | Products | Region | Notes |
|--------|----------|--------|-------|
| **Atlanta Drive Systems** | Precision racks, helical racks | USA/Global | Wide module range (M1-M12) |
| **Ozgear** | Ground racks, pinions | Australia | High precision, CNC-ready |
| **C&U** | Standard spur racks | China/Global | Budget option, plasma tables |

---

## K.2 Motors and Drives

### K.2.1 Stepper Motors and Drivers

| Vendor | Products | Region | Website | Notes |
|--------|----------|--------|---------|-------|
| **Nema23.com** | NEMA 17/23/34 steppers + drivers | USA | nema23.com | CNC-focused bundles, good support |
| **StepperOnline (OOZOOO)** | NEMA 11-42 steppers, closed-loop | Global | omc-stepperonline.com | Wide range, competitive pricing |
| **Leadshine** | Steppers, drivers (DM series) | China/Global | leadshine.com | Reliable drivers, industrial quality |
| **Gecko Drive** | G203V, G540 (4-axis controller) | USA | geckodrive.com | High-performance stepper drivers |
| **ClearPath** | Servo-steppers (hybrid closed-loop) | USA | teknic.com | No tuning required, step/dir input |

**Recommendation:**
- **Budget:** StepperOnline NEMA 23 + DM542 driver
- **Mid-range:** Leadshine DM856 or Nema23.com bundles
- **High-performance:** Gecko G203V or ClearPath SDSK

### K.2.2 Servo Motors and Drives

| Vendor | Products | Region | Notes |
|--------|----------|--------|-------|
| **Yaskawa** | Sigma-7 servo systems | Global | Industrial standard, EtherCAT |
| **Mitsubishi** | MR-J4 servo amplifiers | Global | High performance, expensive |
| **Delta Electronics** | ASDA-A2 servo drives | Asia/Global | Mid-range price, good quality |
| **JMC** | AC servo motors + iHSV drivers | China | Budget servo option for DIY |
| **Teknic** | ClearPath servos (step/dir interface) | USA | Easy setup, integrated driver |

---

## K.3 Spindles and VFDs

### K.3.1 Spindle Motors

| Vendor | Products | Power Range | Website | Notes |
|--------|----------|-------------|---------|-------|
| **HQD (Hanqi)** | Air-cooled, water-cooled spindles | 0.8-7.5 kW | hqd-motor.com | Popular for DIY CNC, affordable |
| **Jianken** | ER11/16/20/25 spindles | 1.5-5.5 kW | jkongmotor.com | Good quality, ISO20/30 tapers |
| **ELTE** | High-frequency spindles (24k RPM) | 2.2-9 kW | eltemotor.com | Precision machining, engraving |
| **Teknomotor** | ISO/BT spindles, ATC-ready | 3-20 kW | teknomotor.com | Industrial, tool changer compatible |
| **Perske** | Ultra-high-speed spindles | 5-50 kW | perske.com | 40,000+ RPM, very expensive |

**Recommendation:**
- **Router/Wood:** HQD 2.2 kW air-cooled (ER20 collet)
- **Milling/Aluminum:** Jianken 3.0 kW water-cooled (ER25)
- **High-speed:** ELTE 4.0 kW (24,000 RPM, ER20)

### K.3.2 VFDs (Variable Frequency Drives)

| Vendor | Models | Power Range | Notes |
|--------|--------|-------------|-------|
| **Huanyang** | HY-series | 0.75-7.5 kW | Budget VFD, RS485 Modbus, common in DIY |
| **Teco** | L510 series | 0.75-15 kW | Reliable, industrial-grade |
| **Delta Electronics** | VFD-E series | 0.4-3.7 kW | Compact, easy setup |
| **Fuling** | DZB200 | 1.5-5.5 kW | Mid-range price, good quality |
| **ABB** | ACS580 | 0.75-250 kW | Industrial, very reliable, expensive |

---

## K.4 Control Electronics

### K.4.1 CNC Controllers

| Controller | Interface | Axes | Software | Price | Best For |
|----------|-----------|------|----------|-------|----------|
| **LinuxCNC** | PC + Mesa FPGA card | Unlimited | Open-source | $$ | Advanced users, custom machines |
| **Mach3** | PC + parallel port/USB | 6 | Windows (legacy) | $ | Hobbyist, older PCs |
| **Mach4** | PC + Ethernet/USB | 6+ | Windows (modern) | $$ | Hobbyist/pro, modern hardware |
| **UCCNC** | PC + UC series controllers | 6 | Windows | $$ | User-friendly, good support |
| **Centroid Acorn** | Standalone + PC | 4-6 | Embedded Linux | $$$ | Retrofit, industrial-grade |
| **PathPilot** | Dedicated controller | 3-4 | Embedded Linux | $$$$ | Tormach machines, easy to use |

**Recommendation:**
- **Beginner:** Mach4 + ESS Ethernet controller
- **Advanced:** LinuxCNC + Mesa 7i96 FPGA
- **Plug-and-play:** Centroid Acorn or UCCNC

### K.4.2 Breakout Boards (BOBs)

| Vendor | Model | Axes | Inputs/Outputs | Interface | Notes |
|--------|-------|------|---------------|-----------|-------|
| **CNC4PC** | C10, C11 | 4-5 | 10-20 I/O | Parallel port | Opto-isolated, charge pump |
| **Ethernet SmoothStepper** | ESS | 6 | 16 I/O | Ethernet | Mach3/4 compatible, reliable |
| **Mesa Electronics** | 7i96 | 5 | 32 I/O | Ethernet | LinuxCNC FPGA, advanced |
| **PMDX** | 126, 134 | 4 | 8-16 I/O | Parallel/USB | Industrial-quality, UL-listed |
| **UC100** | USB controller | 6 | 16 I/O | USB | UCCNC compatible, plug-and-play |

---

## K.5 Structural Materials

### K.5.1 Aluminum Extrusion

| Vendor | Products | Region | Website | Notes |
|--------|----------|--------|---------|-------|
| **80/20 Inc.** | T-slot extrusion (10-series, 15-series) | USA | 8020.net | Premium, USA-made, excellent selection |
| **Misumi** | HFS-series extrusion | Global | us.misumi-ec.com | Japanese quality, fast shipping |
| **Faztek** | T-slot framing systems | USA | faztek.com | Competitive pricing, large selection |
| **Tnutz** | Budget T-slot extrusion | USA | tnutz.com | Lower cost than 80/20, decent quality |
| **Maytec** | Aluminum profiles (40x80, 45x90) | Europe | maytec.com | European standard, metric sizing |

**Common Sizes:**
- **Light CNC:** 40x40mm, 40x80mm
- **Medium CNC:** 60x60mm, 80x40mm
- **Heavy CNC:** 80x80mm, 80x160mm

### K.5.2 Steel and Plate

| Vendor | Products | Region | Notes |
|--------|----------|--------|-------|
| **Online Metals** | Sheet, plate, bar stock | USA | onlinemetals.com | Small quantities, hobbyist-friendly |
| **McMaster-Carr** | All materials, fasteners, tools | USA | mcmaster.com | Fast shipping, excellent catalog |
| **Speedy Metals** | Precision ground plate, shafting | USA | speedymetals.com | CNC-ready stock, tight tolerances |
| **Metal Supermarkets** | Cut-to-size service | USA/Canada | metalsupermarkets.com | Retail locations, instant quotes |

---

## K.6 Plasma and Laser Components

### K.6.1 Plasma Torches and Consumables

| Vendor | Products | Notes |
|--------|----------|-------|
| **Hypertherm** | Powermax series (45-125A) | Industry standard, expensive consumables |
| **Everlast** | PowerPro series (50-80A) | Budget-friendly, good for DIY tables |
| **Razorweld** | Cut series (45-60A) | Australian brand, reliable |
| **Consumable parts:** | Tips, electrodes, shields, nozzles | Use OEM or quality aftermarket (avoid cheap eBay) |

### K.6.2 Fiber Laser Sources and Optics

| Vendor | Products | Power Range | Notes |
|--------|----------|-------------|-------|
| **Raycus** | Fiber laser sources | 20W-100kW | Chinese, budget-friendly, widely used |
| **JPT** | MOPA fiber lasers | 20W-100W | Adjustable pulse, marking applications |
| **IPG Photonics** | Fiber lasers | 100W-100kW | Premium, industrial-grade, very reliable |
| **II-VI (Coherent)** | CO₂ lasers, cutting heads | 40W-6kW | CO₂ legacy, excellent optics |

---

## K.7 Waterjet Components

| Vendor | Products | Notes |
|--------|----------|-------|
| **KMT Waterjet** | Pumps, cutting heads (60k-90k PSI) | Industry leader, expensive |
| **OMAX** | Complete waterjet systems | USA-made, software integrated |
| **Jet Edge** | Ultra-high-pressure pumps (up to 94k PSI) | Custom systems, industrial |
| **Waterjet Corporation** | Abrasive delivery, nozzles, consumables | OEM and aftermarket parts |

**Abrasive Suppliers:**
- **Barton Garnet:** 80-mesh garnet (standard for waterjet)
- **GMA Garnet:** Australian garnet, high quality

---

## K.8 Electronics and Sensors

### K.8.1 Limit Switches and Proximity Sensors

| Vendor | Products | Notes |
|--------|----------|-------|
| **Omron** | D2F micro switches, E2E proximity sensors | Reliable, industrial-grade |
| **Honeywell** | Micro switches (V-series) | USA-made, durable |
| **Pepperl+Fuchs** | Inductive proximity sensors (M12, M18) | German quality, expensive |
| **Autonics** | Photoelectric sensors, proximity switches | Korean brand, good value |

### K.8.2 Power Supplies

| Vendor | Products | Notes |
|--------|----------|-------|
| **Mean Well** | 24V DC, 48V DC industrial supplies | Reliable, UL-listed, affordable |
| **TDK-Lambda** | High-power supplies (500W-3kW) | Industrial, very reliable |
| **Phoenix Contact** | DIN-rail power supplies | Compact, easy panel mounting |

---

## K.9 Tooling and Cutters

### K.9.1 Endmills and Cutting Tools

| Vendor | Products | Notes |
|--------|----------|-------|
| **Harvey Tool** | Micro endmills, specialty tools | USA-made, excellent quality |
| **OSG** | Endmills, drills, taps | Japanese, carbide specialists |
| **Kennametal** | Indexable tools, inserts | Industrial, large-scale production |
| **Onsrud** | Router bits, wood tooling | CNC router specialist |
| **Amana Tool** | Router bits, compression bits | Wood and composite cutting |

### K.9.2 Budget Tooling

| Vendor | Products | Notes |
|--------|----------|-------|
| **YG-1** | Carbide endmills (1-20mm) | Korean, good quality/price ratio |
| **ZCC-CT** | Carbide tooling | Chinese, budget option for prototyping |
| **Drill Hog** | HSS drills, taps, bits | USA warehouse, fast shipping |

---

## K.10 Metrology and Measurement Tools

| Vendor | Products | Notes |
|--------|----------|-------|
| **Mitutoyo** | Calipers, micrometers, indicators | Japanese, industry standard |
| **Starrett** | Precision measuring tools | USA-made, premium quality |
| **Fowler** | Budget calipers, indicators | Good value, accurate |
| **iGaging** | Digital scales, DRO kits | Budget-friendly, hobbyist-grade |
| **Renishaw** | Touch probes, tool setters | Industrial, CNC automation |

---

**End of Vendor and Supplier Directory Appendix**
