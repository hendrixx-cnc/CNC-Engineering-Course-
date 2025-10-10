# Module 5 – Plasma Cutting Systems

## 1. Introduction

Plasma cutting uses a high-velocity jet of ionized gas to melt and blow away metal, providing fast and precise cuts in steel, aluminum, and other conductive materials. CNC plasma tables automate torch movement for repeatable, complex shapes.

## 2. Plasma Torch Types

- **Handheld torches**: For manual cutting and edge prep.
- **Mechanized torches**: Designed for CNC tables, with straight bodies and machine mounts.

## 3. Power Supplies

- Rated by amperage (30–125 A common).
- Higher currents cut thicker metal.
- Duty cycle defines how long the machine can cut before cooling.

## 4. Consumables

- **Electrode**: Conducts current; wears over time.
- **Nozzle**: Shapes plasma arc; controls cut quality.
- **Shield cap**: Directs airflow, protects nozzle.
- **Swirl ring**: Controls gas flow pattern.

Replace consumables regularly for best cut quality.

## 5. Gas Selection

- **Air**: Standard for mild steel, aluminum, and stainless.
- **Oxygen**: Improved speed and edge quality in steel.
- **Nitrogen/argon/hydrogen**: Used for specialty metals.

## 6. Table Design

- **Water table**: Submerges work for fume suppression; cools parts.
- **Down-draft table**: Uses fans to pull fumes through grated bed.

## 7. Torch Height Control (THC)

- Maintains optimal arc distance (≈1–2 mm).
- Uses voltage feedback to adjust Z axis.
- Critical for consistent cut quality and consumable life.

## 8. CNC Control Integration

- Connect torch relay and arc OK signals to controller.
- THC via analog or digital interface.
- Program pierce delay, cut speed, and lead-in/out for best results.

## 9. Cut Quality Factors

- **Pierce delay**: Time to fully penetrate metal before motion.
- **Cut speed**: Too fast = dross and angle; too slow = wide kerf.
- **Kerf width**: Varies by nozzle and current; offset in CAM.
- **Dross formation**: Minimized by correct speed and height.

## 10. Safety

- Use fume extraction, eye and ear protection.
- Shield electronics from high-frequency arc starting.
- Ground table and torch for operator safety.

## 11. Maintenance

- Inspect and replace consumables.
- Clean torch and table after use.
- Check air supply for moisture and oil.

## 12. Conclusion

CNC plasma cutting is a versatile, high-speed process for metal fabrication. Proper setup, maintenance, and safety ensure quality results and long consumable life.

---