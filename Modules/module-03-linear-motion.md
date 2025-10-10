# Module 3 – Linear Motion Systems

## 1. Introduction

Linear motion systems convert rotary motor motion into precise, repeatable linear travel. The primary types in CNC machine design are ball screws, lead screws, rack and pinion, linear guides, and belt drives.

## 2. Ball Screws

### 2.1 Characteristics

- Recirculating ball bearings provide low friction and minimal backlash.
- Available in rolled (cost-effective) and ground (high-precision) forms.
- Common diameters: 12–32 mm; leads: 5–20 mm.
- Critical speed and buckling must be considered for long screws.

### 2.2 Key Equations

**Critical speed:**
\[
n_{cr} = \frac{4.76 \times 10^6 \cdot k \cdot d_s}{L^2}
\]
where \( d_s \) is screw diameter (mm), \( L \) is free length (mm), \( k \) is end-fixity factor.

**Buckling load:**
\[
F_{cr} = \frac{\pi^2 E I}{K L^2}
\]
where \( E \) is modulus, \( I \) is moment of inertia, \( K \) is fixity coefficient.

## 3. Lead Screws

- Trapezoidal thread profile; higher friction and backlash than ball screws.
- Suitable for low-load, low-speed axes and Z axes.
- Self-locking at rest.

## 4. Rack & Pinion

### 4.1 Characteristics

- Used for long axes (>1 m) and high speeds.
- Helical racks increase contact ratio and reduce noise.
- Pinion diameter and tooth count chosen for desired speed and resolution.
- Preload via split pinion or dual motors to eliminate backlash.

### 4.2 Key Equations

**Linear speed:**
\[
V = \frac{\pi D N}{60 G}
\]
where \( D \) is pinion diameter (mm), \( N \) is motor rpm, \( G \) is gear ratio.

## 5. Linear Guides

- Precision rails (profile or round) with recirculating ball carriages.
- Offer high stiffness and low friction.
- Preload carriages for zero clearance.
- Mount to machined datums for accuracy.

## 6. Belt Drives

- Used for low-load, high-speed axes (e.g., laser, pick-and-place).
- GT2, HTD, and T5 profiles are common.
- Tension and pulley size affect accuracy and wear.

## 7. Universal Linear Motion Requirements

- Select system type based on axis length, speed, load, and accuracy.
- Mount rails and screws to flat, aligned datums.
- Minimize backlash and compliance for best performance.
- Maintain cleanliness and lubrication.

## 8. Alignment and Maintenance

- Use dial indicators and granite squares to set rail straightness.
- Adjust ball-screw nut preload as needed.
- Inspect rack teeth for wear and lubricate periodically.
- Check belt tension and pulley alignment.

## 9. Conclusion

Linear motion systems are the backbone of CNC accuracy. Choose the right technology for each axis, ensure precision mounting, and schedule regular maintenance for reliable operation.

---