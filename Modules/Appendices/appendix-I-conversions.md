# Appendix I: Unit Conversions and Constants

---

## I.1 Length Conversions

| From/To | Millimeter (mm) | Centimeter (cm) | Meter (m) | Inch (in) | Foot (ft) |
|---------|----------------|----------------|-----------|----------|-----------|
| **1 mm** | 1 | 0.1 | 0.001 | 0.03937 | 0.003281 |
| **1 cm** | 10 | 1 | 0.01 | 0.3937 | 0.03281 |
| **1 m** | 1000 | 100 | 1 | 39.37 | 3.281 |
| **1 in** | 25.4 | 2.54 | 0.0254 | 1 | 0.08333 |
| **1 ft** | 304.8 | 30.48 | 0.3048 | 12 | 1 |

**Common CNC Conversions:**
- 1 inch = 25.4 mm (exact)
- 1 foot = 304.8 mm
- 1 mil (0.001") = 0.0254 mm = 25.4 μm
- 1 micron (μm) = 0.001 mm = 0.00003937"

---

## I.2 Area and Volume Conversions

### I.2.1 Area

| From/To | mm² | cm² | m² | in² | ft² |
|---------|-----|-----|----|----|-----|
| **1 mm²** | 1 | 0.01 | 10⁻⁶ | 0.00155 | 1.076×10⁻⁵ |
| **1 cm²** | 100 | 1 | 10⁻⁴ | 0.155 | 0.001076 |
| **1 m²** | 10⁶ | 10⁴ | 1 | 1550 | 10.76 |
| **1 in²** | 645.2 | 6.452 | 6.452×10⁻⁴ | 1 | 0.00694 |
| **1 ft²** | 92,903 | 929.03 | 0.0929 | 144 | 1 |

### I.2.2 Volume

| From/To | cm³ (cc) | Liter (L) | m³ | in³ | ft³ | US Gallon |
|---------|----------|-----------|----|----|-----|-----------|
| **1 cm³** | 1 | 0.001 | 10⁻⁶ | 0.06102 | 3.531×10⁻⁵ | 0.000264 |
| **1 L** | 1000 | 1 | 0.001 | 61.02 | 0.03531 | 0.2642 |
| **1 m³** | 10⁶ | 1000 | 1 | 61,024 | 35.31 | 264.2 |
| **1 in³** | 16.39 | 0.01639 | 1.639×10⁻⁵ | 1 | 5.787×10⁻⁴ | 0.004329 |
| **1 ft³** | 28,317 | 28.32 | 0.02832 | 1728 | 1 | 7.481 |
| **1 US gal** | 3785 | 3.785 | 0.003785 | 231 | 0.1337 | 1 |

---

## I.3 Force, Pressure, and Torque Conversions

### I.3.1 Force

| From/To | Newton (N) | Kilonewton (kN) | Kilogram-force (kgf) | Pound-force (lbf) |
|---------|-----------|----------------|---------------------|------------------|
| **1 N** | 1 | 0.001 | 0.102 | 0.2248 |
| **1 kN** | 1000 | 1 | 102.0 | 224.8 |
| **1 kgf** | 9.807 | 0.009807 | 1 | 2.205 |
| **1 lbf** | 4.448 | 0.004448 | 0.4536 | 1 |

### I.3.2 Pressure and Stress

| From/To | Pascal (Pa) | kPa | MPa | Bar | PSI | kg/cm² |
|---------|------------|-----|-----|-----|-----|--------|
| **1 Pa** | 1 | 0.001 | 10⁻⁶ | 10⁻⁵ | 1.450×10⁻⁴ | 1.020×10⁻⁵ |
| **1 kPa** | 1000 | 1 | 0.001 | 0.01 | 0.1450 | 0.01020 |
| **1 MPa** | 10⁶ | 1000 | 1 | 10 | 145.0 | 10.20 |
| **1 bar** | 10⁵ | 100 | 0.1 | 1 | 14.50 | 1.020 |
| **1 PSI** | 6895 | 6.895 | 0.006895 | 0.06895 | 1 | 0.07031 |
| **1 kg/cm²** | 98,067 | 98.07 | 0.09807 | 0.9807 | 14.22 | 1 |

**Common Pneumatic Pressures:**
- 100 PSI = 6.9 bar = 0.69 MPa
- 6 bar (typical CNC) = 87 PSI = 0.6 MPa

### I.3.3 Torque

| From/To | N·m | kN·m | lb·ft | lb·in | oz·in |
|---------|-----|------|-------|-------|-------|
| **1 N·m** | 1 | 0.001 | 0.7376 | 8.851 | 141.6 |
| **1 kN·m** | 1000 | 1 | 737.6 | 8851 | 141,615 |
| **1 lb·ft** | 1.356 | 0.001356 | 1 | 12 | 192 |
| **1 lb·in** | 0.1130 | 1.130×10⁻⁴ | 0.08333 | 1 | 16 |
| **1 oz·in** | 0.007062 | 7.062×10⁻⁶ | 0.005208 | 0.0625 | 1 |

---

## I.4 Power and Energy Conversions

### I.4.1 Power

| From/To | Watt (W) | Kilowatt (kW) | Horsepower (HP) | ft·lb/s |
|---------|---------|--------------|----------------|---------|
| **1 W** | 1 | 0.001 | 0.001341 | 0.7376 |
| **1 kW** | 1000 | 1 | 1.341 | 737.6 |
| **1 HP** | 745.7 | 0.7457 | 1 | 550 |
| **1 ft·lb/s** | 1.356 | 0.001356 | 0.001818 | 1 |

**Spindle Power Example:**
- 2.2 kW spindle = 2.95 HP
- 3 HP spindle = 2.24 kW

### I.4.2 Energy and Work

| From/To | Joule (J) | Kilojoule (kJ) | Watt-hour (Wh) | Kilowatt-hour (kWh) | BTU |
|---------|-----------|---------------|---------------|-------------------|-----|
| **1 J** | 1 | 0.001 | 2.778×10⁻⁴ | 2.778×10⁻⁷ | 9.478×10⁻⁴ |
| **1 kJ** | 1000 | 1 | 0.2778 | 2.778×10⁻⁴ | 0.9478 |
| **1 Wh** | 3600 | 3.6 | 1 | 0.001 | 3.412 |
| **1 kWh** | 3.6×10⁶ | 3600 | 1000 | 1 | 3412 |
| **1 BTU** | 1055 | 1.055 | 0.2931 | 2.931×10⁻⁴ | 1 |

---

## I.5 Velocity and Acceleration Conversions

### I.5.1 Linear Velocity

| From/To | mm/s | m/s | m/min | in/s | in/min (IPM) | ft/min |
|---------|------|-----|-------|------|-------------|--------|
| **1 mm/s** | 1 | 0.001 | 0.06 | 0.03937 | 2.362 | 0.1969 |
| **1 m/s** | 1000 | 1 | 60 | 39.37 | 2362 | 196.9 |
| **1 m/min** | 16.67 | 0.01667 | 1 | 0.6562 | 39.37 | 3.281 |
| **1 in/s** | 25.4 | 0.0254 | 1.524 | 1 | 60 | 5.0 |
| **1 IPM** | 0.4233 | 4.233×10⁻⁴ | 0.0254 | 0.01667 | 1 | 0.08333 |
| **1 ft/min** | 5.08 | 0.00508 | 0.3048 | 0.2 | 12 | 1 |

**Common CNC Feeds:**
- 1000 mm/min = 39.37 IPM
- 100 IPM = 2540 mm/min = 42.3 mm/s

### I.5.2 Rotational Speed

| From/To | RPM | rad/s | deg/s |
|---------|-----|-------|-------|
| **1 RPM** | 1 | 0.1047 | 6.0 |
| **1 rad/s** | 9.549 | 1 | 57.30 |
| **1 deg/s** | 0.1667 | 0.01745 | 1 |

### I.5.3 Acceleration

| From/To | m/s² | ft/s² | g (gravity) |
|---------|------|-------|------------|
| **1 m/s²** | 1 | 3.281 | 0.102 |
| **1 ft/s²** | 0.3048 | 1 | 0.03108 |
| **1 g** | 9.807 | 32.17 | 1 |

**CNC Acceleration:** 1 m/s² = 60,000 mm/min² (units commonly seen in controller settings)

---

## I.6 Temperature Conversions

| From | To Celsius (°C) | To Fahrenheit (°F) | To Kelvin (K) |
|------|----------------|-------------------|---------------|
| **Celsius** | °C | (°C × 9/5) + 32 | °C + 273.15 |
| **Fahrenheit** | (°F - 32) × 5/9 | °F | (°F - 32) × 5/9 + 273.15 |
| **Kelvin** | K - 273.15 | (K - 273.15) × 9/5 + 32 | K |

**Common Temperatures:**
- Water freezing: 0°C = 32°F = 273.15K
- Room temperature: 20°C = 68°F = 293K
- Water boiling: 100°C = 212°F = 373K
- Grease max temp: 150°C = 302°F

---

## I.7 Material Property Conversions

### I.7.1 Density

| From/To | kg/m³ | g/cm³ | lb/in³ | lb/ft³ |
|---------|-------|-------|--------|--------|
| **1 kg/m³** | 1 | 0.001 | 3.613×10⁻⁵ | 0.06243 |
| **1 g/cm³** | 1000 | 1 | 0.03613 | 62.43 |
| **1 lb/in³** | 27,680 | 27.68 | 1 | 1728 |
| **1 lb/ft³** | 16.02 | 0.01602 | 5.787×10⁻⁴ | 1 |

**Common Materials:**
- Steel: 7.85 g/cm³ = 7850 kg/m³ = 0.284 lb/in³
- Aluminum 6061: 2.70 g/cm³ = 2700 kg/m³ = 0.098 lb/in³

### I.7.2 Hardness (Approximate Conversions)

**Rockwell C (HRC) to Brinell (HB) to Tensile Strength (MPa):**

| HRC | HB | Approx. Tensile (MPa) |
|-----|----|--------------------|
| 20 | 230 | 800 |
| 30 | 285 | 1000 |
| 40 | 370 | 1300 |
| 50 | 480 | 1700 |
| 60 | 670 | 2200 |

**Note:** Conversions are approximate, vary by material composition.

---

## I.8 Physical Constants

| Constant | Symbol | Value | Units |
|----------|--------|-------|-------|
| **Gravitational acceleration (Earth)** | g | 9.80665 | m/s² |
| **Speed of light** | c | 299,792,458 | m/s |
| **Pi** | π | 3.14159265359 | - |
| **Euler's number** | e | 2.71828182846 | - |
| **Boltzmann constant** | k | 1.380649×10⁻²³ | J/K |
| **Stefan-Boltzmann constant** | σ | 5.670374×10⁻⁸ | W/(m²·K⁴) |

---

## I.9 Quick Reference Formulas

### I.9.1 Cutting Speed to Spindle RPM

$$\text{RPM} = \frac{V_c \times 1000}{\pi \times D}$$

where:
- $V_c$ = cutting speed (m/min)
- $D$ = cutter diameter (mm)

**Example:** 100 m/min cutting speed, 10mm endmill
$$\text{RPM} = \frac{100 \times 1000}{\pi \times 10} = 3183 \text{ RPM}$$

### I.9.2 Feed Rate Calculation

$$F = f_z \times Z \times \text{RPM}$$

where:
- $F$ = feed rate (mm/min)
- $f_z$ = chip load per tooth (mm)
- $Z$ = number of teeth
- RPM = spindle speed

**Example:** 0.1 mm/tooth, 4-flute, 3000 RPM
$$F = 0.1 \times 4 \times 3000 = 1200 \text{ mm/min}$$

### I.9.3 Material Removal Rate (MRR)

$$\text{MRR} = W \times D \times F$$

where:
- MRR = material removal rate (mm³/min)
- $W$ = width of cut (mm)
- $D$ = depth of cut (mm)
- $F$ = feed rate (mm/min)

---

**End of Unit Conversions and Constants Appendix**
