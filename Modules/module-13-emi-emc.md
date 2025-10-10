# Module 13 – EMI and EMC Design for Motion Control Systems

## 1. Introduction

Electromagnetic interference (EMI) and electromagnetic compatibility (EMC) are critical for reliable CNC and robotic systems. Poor EMI/EMC causes missed steps, encoder faults, and controller errors.

## 2. EMI Sources

- Motor drives and switching power supplies.
- High-frequency plasma, laser, or spindle arcs.
- Long cable runs and unshielded wiring.

## 3. EMC Strategies

- Shielded twisted-pair cables for signal lines.
- Metal enclosures connected to earth ground.
- Ferrite beads on motor and encoder cables.
- Star-grounding topology to avoid ground loops.

## 4. Filtering

- Line filters (EMI/RFI) on AC and DC power inputs.
- Capacitive and inductive filters for analog signals.
- Chokes for servo and spindle motor leads.

## 5. Isolation

- Opto-isolators for controller inputs/outputs.
- Transformer isolation on communication lines.
- Galvanic isolation for USB, Ethernet, and analog signals.

## 6. Layout Best Practices

- Separate high-voltage and low-voltage wiring.
- Cross signal cables at 90° to power lines.
- Keep cable runs short and direct.
- Bond shields to enclosure at one end only.

## 7. Grounding

- Single-point earth ground for all shields and enclosures.
- Separate safety ground from signal ground.
- Use copper bus bars for low impedance.

## 8. Diagnostics

- Oscilloscope to identify high-frequency noise.
- Clamp meters for ground loop detection.
- Monitor encoder and drive faults during operation.

## 9. Standards

- CE, FCC, UL, and ISO 61000 compliance for industrial machines.
- Follow manufacturer guidelines for EMC on drives and controllers.

## 10. Maintenance

- Inspect cable shielding regularly.
- Replace worn ferrites and connectors.
- Retighten ground and shield connections annually.

## 11. Troubleshooting

- Encoder errors: check cable shields and grounding.
- Random resets: inspect power supply and filter integrity.
- Communication faults: test isolation and cable routing.

## 12. Conclusion

EMI and EMC design are essential for precision motion control. Invest in quality wiring, shielding, and isolation to prevent errors and downtime.

---