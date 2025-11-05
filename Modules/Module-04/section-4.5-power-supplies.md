## 5. Power Supplies: The Foundation of Control Electronics

### 5.1 Introduction: The Unseen Heart of the CNC System

In the hierarchy of a CNC control system, the **Power Supply Unit (PSU)** is the foundational element upon which all electronic performance is built. While motion controllers (Section 2) and drives (Section 4) command and execute motion, the PSU is the silent workhorse that provides the stable, clean, and robust electrical energy required for every component to function. Its role is not merely to convert AC mains to DC voltage; it is to deliver that power reliably under the highly dynamic and demanding load conditions characteristic of CNC machining.

A CNC system typically requires multiple DC voltage rails:
1.  **High-Power Motor Bus:** A high-voltage, high-current supply (e.g., 48VDC, 75VDC, or even 320VDC for AC servos) that energizes the stepper or servo drives. This supply must handle massive, rapid fluctuations in current demand during acceleration and deceleration.
2.  **Logic Power:** Low-voltage, regulated supplies (e.g., 5VDC, 12VDC, 24VDC) that power sensitive electronics like the motion controller, breakout board, sensors, and relays. These supplies must be exceptionally clean and stable to prevent logic errors and system crashes.

The selection and implementation of the PSU is a critical engineering decision. An undersized or poorly regulated supply can lead to a cascade of difficult-to-diagnose problems, including lost steps in stepper systems, "under-voltage" faults in servo drives, diminished high-speed motor performance, and logic-level noise that corrupts control signals. A properly engineered power supply system is the bedrock of machine reliability, performance, and safety.

### 5.2 Power Supply Architectures: Linear vs. Switched-Mode

Two primary architectures dominate power supply design: Linear and Switched-Mode. While both convert AC to DC, their methodologies and performance characteristics are vastly different.

#### **5.2.1 Linear Power Supplies**

A linear power supply is the classical approach to DC voltage regulation. Its topology is simple and direct: a step-down transformer, a full-wave rectifier, a large filter capacitor, and a linear regulator (a variable resistor, typically a transistor) that dissipates excess voltage as heat to maintain a constant output.

*   **Pros:** Extremely low output ripple and noise, simple design, excellent transient response.
*   **Cons:** Grossly inefficient, large, heavy, and poor load regulation.

**Equation 5-1: Power Dissipation in a Linear Regulator**
The inefficiency is its defining drawback. The power dissipated as heat in the regulator is:
$$
P_{diss} = (V_{in, unreg} - V_{out, reg}) \times I_{load}
$$
For a 24V input and a 5V output drawing 1A, the regulator wastes `(24V - 5V) * 1A = 19W` of power as heat, for an efficiency of only `(5W / 24W) * 100% ≈ 21%`. This makes linear supplies impractical for high-power applications like motor drives.

#### **5.2.2 Switched-Mode Power Supplies (SMPS)**

The SMPS is the modern standard for all but the most sensitive analog applications. It uses a high-frequency switching element (a MOSFET) to chop up the input DC voltage, pass it through a small, lightweight high-frequency transformer, and then rectify and filter it. A feedback loop controls the duty cycle of the switch to maintain precise output voltage regulation.

*   **Pros:** Highly efficient (85-95%+), compact, lightweight, excellent line and load regulation.
*   **Cons:** More complex, generates high-frequency electromagnetic interference (EMI) that must be carefully filtered.

For CNC applications, the SMPS is the undisputed choice for both motor and logic power due to its efficiency and power density. The remainder of this section will focus exclusively on the application of SMPS technology.

#### **5.2.3 SMPS Topologies and EMI Filtering**

While the internal design of an SMPS is a discipline in itself, understanding its basic topologies and inherent noise characteristics is crucial for system integration. The most common topology for medium-power (100-1000W) CNC applications is the **flyback converter** for logic supplies and the **forward converter** or **half-bridge converter** for motor power supplies due to their balance of efficiency and component count.

A critical byproduct of the high-frequency switching (typically 50-500 kHz) in an SMPS is **Electromagnetic Interference (EMI)**. This noise is generated in two forms:
1.  **Conducted Emissions:** Noise that travels back onto the AC power lines.
2.  **Radiated Emissions:** Noise that is broadcast through the air as electromagnetic waves.

A well-designed industrial PSU incorporates robust internal filtering to meet regulatory standards (e.g., FCC Part 15, CISPR 22). This typically includes:
*   **AC Input Filter:** A multi-stage filter consisting of common-mode chokes (inductors) and X/Y safety capacitors to suppress noise conducted onto the mains.
*   **Shielding:** A grounded metal enclosure that acts as a Faraday cage to contain radiated emissions.
*   **Output Filtering:** An LC (inductor-capacitor) filter on the DC output to reduce voltage ripple to acceptable levels.

**Equation 5-7: LC Output Filter Cutoff Frequency**
The effectiveness of the output filter is determined by its cutoff frequency, `f_c`, which must be significantly lower than the PSU's switching frequency, `f_sw`.
$$
f_c = \frac{1}{2\pi\sqrt{LC}}
$$
For a typical SMPS switching at `f_sw = 100 kHz`, a filter with `f_c` around 1-5 kHz provides excellent attenuation of switching ripple.

***
**Worked Example 5.3: EMI Filter Component Selection**

**Given:**
*   A 48V, 10A (480W) SMPS with a switching frequency `f_sw = 120 kHz`.
*   The output has a measured ripple of 1.5 Vp-p without adequate filtering.
*   Target ripple for servo drives: < 250 mVp-p. This requires an attenuation of `1.5V / 0.25V = 6x`, or approximately -15.5 dB.

**Task:**
*   Design a second-order LC low-pass filter to meet the ripple requirement.

**Solution:**
1.  **Determine Cutoff Frequency:** A second-order filter provides -40 dB/decade attenuation above its cutoff frequency. To achieve -15.5 dB attenuation at 120 kHz, we need a cutoff frequency `f_c` well below this. Let's target `f_c = 10 kHz`, which is more than a decade lower.

2.  **Select Capacitor (C):** The capacitor's primary role is to absorb the ripple current. A good starting point is to allow 10-20% of the maximum DC current as ripple current in the inductor. For a 10A supply, let's assume a ripple current `ΔI_L` of 2A. The required capacitance is:
    $$
    C = \frac{\Delta I_L}{8 \times f_{sw} \times V_{ripple,target}} = \frac{2 \, \text{A}}{8 \times 120,000 \, \text{Hz} \times 0.25 \, \text{V}} = 8.33 \, \mu\text{F}
    $$
    We select a standard **10 µF**, low-ESR electrolytic or ceramic capacitor.

3.  **Select Inductor (L):** Now calculate the required inductance to achieve the 10 kHz cutoff frequency with our 10 µF capacitor.
    $$
    L = \frac{1}{(2\pi f_c)^2 C} = \frac{1}{(2\pi \times 10,000)^2 \times 10 \times 10^{-6}} = \frac{1}{(3.95 \times 10^9) \times (10 \times 10^{-6})} = 25.3 \, \mu\text{H}
    $$
    We select a standard **27 µH** power inductor with a saturation current rating > 12A (peak load).

**Result:** An output filter consisting of a **27 µH inductor** and a **10 µF capacitor** will effectively reduce the 120 kHz switching ripple to meet the <250 mVp-p requirement for the servo drives.

***

### 5.3 Sizing the Motor Power Supply: A Systems Approach

Sizing the main motor PSU is one of the most critical and frequently misunderstood aspects of CNC system design. The process involves determining the required DC voltage and continuous current capacity.

#### **5.3.1 Determining the DC Bus Voltage (V_DC)**

*   **For Stepper Motors:** Higher voltage is crucial for overcoming the motor's back-EMF at high speeds, thus maintaining torque. A common rule of thumb for selecting the optimal voltage is:
    $$
    V_{DC, optimal} = 32 \times \sqrt{L}
    $$
    Where `L` is the motor's phase inductance in millihenries (mH). Using a voltage significantly lower than this will result in poor high-speed performance. Using a voltage much higher can lead to overheating.

*   **For Servo Motors:** The voltage is dictated by the servo drive's specifications. Common DC servo systems operate on 48V, 75V, or 90V. High-power AC servo systems rectify the mains voltage directly, resulting in a DC bus of approximately `V_AC, RMS * sqrt(2)` (e.g., 240VAC -> 340VDC).

#### **5.3.2 Determining the Continuous Current Rating (I_PSU)**

A common mistake is to simply sum the nameplate current ratings of all motors. This leads to a grossly oversized and expensive PSU. The actual continuous current draw is significantly lower due to two factors:
1.  **Duty Cycle:** Motors rarely draw peak current continuously.
2.  **Phase Current vs. Supply Current:** Stepper and servo drives use switching amplifiers, meaning the current drawn from the PSU is not equal to the current in the motor phases.

**Equation 5-2: PSU Current for Stepper Motors**
A robust formula for estimating the continuous PSU current for a system of stepper motors is:
$$
I_{PSU} = \frac{2}{3} \times \sum_{i=1}^{N} I_{phase, i}
$$
Where `I_phase, i` is the rated phase current for motor `i`, and `N` is the number of motors that can be active simultaneously. The `2/3` factor accounts for the fact that not all phases are fully energized at once and the drive's switching action.

**Equation 5-3: PSU Power for Servo Motors**
For servo motors, a power-based approach is more accurate. The total power required from the PSU is the sum of the mechanical power delivered by each motor plus the electrical losses in the drives.
$$
P_{PSU} = \frac{1}{\eta_{drive}} \sum_{i=1}^{N} (T_i \times \omega_i)
$$
Where:
*   `η_drive` is the drive efficiency (typically 90-95%).
*   `T_i` is the continuous torque required from motor `i` (Nm).
*   `ω_i` is the motor's angular velocity (rad/s).

The required PSU current is then simply `I_PSU = P_PSU / V_DC`.

***
**Worked Example 5.1: Sizing a PSU for a 3-Axis Stepper System**

**Given:**
*   X-axis motor: 3A/phase
*   Y-axis motor: 3A/phase
*   Z-axis motor: 2A/phase
*   All motors have an inductance of 4 mH.

**Task:**
1.  Determine the optimal PSU voltage.
2.  Determine the required continuous PSU current.

**Solution:**
1.  **Calculate Voltage:**
    Using the rule of thumb for stepper voltage:
    $$
    V_{DC, optimal} = 32 \times \sqrt{4 \, \text{mH}} = 32 \times 2 = 64V
    $$
    A standard, commercially available **60V or 72V PSU** would be an excellent choice. We will select a 60V PSU for the current calculation.

2.  **Calculate Current:**
    Assuming all three axes can move simultaneously (e.g., during a 3D contouring move):
    $$
    I_{PSU} = \frac{2}{3} \times (I_X + I_Y + I_Z) = \frac{2}{3} \times (3A + 3A + 2A) = \frac{2}{3} \times 8A \approx 5.33A
    $$
    To provide a healthy safety margin (20-25%), a PSU with a continuous rating of **6.5A to 7A** would be appropriate.

**Result:** A **60V, 7A (420W)** regulated SMPS is the correctly sized power supply for this system. Simply summing the phase currents (8A) would have been oversized, while sizing for only one or two motors would be insufficient for complex, high-speed motion.

***

### 5.4 Voltage Regulation, Ripple, and Bulk Capacitance

#### **5.4.1 Load Regulation**
Load regulation specifies how much the output voltage changes when the load current changes from minimum to maximum. A tight regulation (e.g., <1%) is critical. Poor regulation can cause the bus voltage to sag during heavy acceleration, potentially triggering an under-voltage fault in a servo drive.

#### **5.4.2 Output Ripple**
Output ripple is the small, residual AC component on the DC output. For motor drives, a ripple of 1-2% is generally acceptable. However, for logic supplies, ripple must be much lower (<50mV) to prevent errors.

#### **5.4.3 Bulk Capacitance and Regenerative Energy**

During deceleration, a motor acts as a generator, converting kinetic energy back into electrical energy. This "regenerative" current flows back to the PSU, charging its bulk output capacitors and causing the DC bus voltage to rise.

**Equation 5-4: Stored Kinetic Energy**
The kinetic energy of a moving axis that must be absorbed is:
$$
E_k = \frac{1}{2} J_{total} \omega^2
$$
Where `J_total` is the total reflected inertia at the motor shaft and `ω` is the angular velocity.

**Equation 5-5: Bus Voltage Rise from Regeneration**
This energy is stored in the PSU's bulk capacitance (`C`), causing a voltage rise (`ΔV`):
$$
E_k = \frac{1}{2} C (V_{final}^2 - V_{initial}^2)
$$
If the voltage rises too high (`V_final`), it can damage the drive or PSU. This is known as an "over-voltage" fault.

***
**Worked Example 5.2: Analyzing Over-Voltage Risk in a Servo System**

**Given:**
*   A servo system with a 75VDC PSU.
*   The PSU has an internal bulk capacitance of 4700 µF (0.0047 F).
*   The drive's over-voltage fault triggers at 95V.
*   The total kinetic energy of the gantry during a rapid stop is calculated to be 25 Joules.

**Task:**
*   Determine if the bus voltage will exceed the fault limit.

**Solution:**
Rearrange the energy equation to solve for `V_final`:
$$
V_{final} = \sqrt{\frac{2 E_k}{C} + V_{initial}^2}
$$
$$
V_{final} = \sqrt{\frac{2 \times 25 \, J}{0.0047 \, F} + (75V)^2} = \sqrt{10638 + 5625} = \sqrt{16263} \approx 127.5V
$$

**Result:** The bus voltage will spike to **127.5V**. This is well above the drive's 95V limit and will cause an immediate over-voltage fault, shutting down the machine.

**Solution:** A **regeneration resistor** (or "braking resistor") is required. This is a large ceramic resistor that the servo drive switches across the DC bus when it detects a voltage rise. The resistor dissipates the regenerative energy as heat, clamping the bus voltage at a safe level.

***

### 5.5 Protection Circuits and Safety Features

A high-quality industrial PSU includes several essential protection circuits:

*   **Over-Current Protection (OCP):** Prevents damage from short circuits by shutting down or entering a "hiccup" mode.
*   **Over-Voltage Protection (OVP):** Protects the load from a failure in the PSU's regulation circuit.
*   **Over-Temperature Protection (OTP):** Shuts the PSU down if its internal temperature exceeds a safe limit.
*   **Inrush Current Limiting:** When a PSU is first powered on, its large input capacitors draw a massive, brief surge of current. An inrush current limiter (typically an NTC thermistor) is essential to prevent tripping circuit breakers.

**Equation 5-6: Inrush Current without Limiting**
The theoretical peak inrush current `I_inrush` for a capacitive load is:
$$
I_{inrush, peak} = \frac{V_{peak}}{R_{line}} = \frac{V_{AC, RMS} \sqrt{2}}{R_{line}}
$$
Where `R_line` is the resistance of the power line. This can easily exceed 100A for a fraction of a second, making a limiting circuit mandatory.

**Equation 5-8: Inrush Current Limiting with an NTC Thermistor**
An NTC (Negative Temperature Coefficient) thermistor is commonly used. It has a high resistance when cold and a low resistance when hot. At power-on, its high initial resistance `R_NTC` limits the inrush current.
$$
I_{inrush, peak} = \frac{V_{AC, RMS} \sqrt{2}}{R_{line} + R_{NTC}}
$$

***
**Worked Example 5.4: Sizing an Inrush Current Limiter**

**Given:**
*   A large power supply connected to a 240V AC line (`V_AC, RMS`).
*   The line resistance `R_line` is 0.5 Ω.
*   The circuit breaker is rated for a peak instantaneous current of 50A.

**Task:**
*   Determine the minimum initial resistance for an NTC thermistor to prevent tripping the breaker.

**Solution:**
1.  **Calculate Peak Voltage:**
    `V_peak = 240V * sqrt(2) ≈ 340V`.

2.  **Calculate Required Total Resistance:**
    To keep the peak current below 50A:
    `R_total_min = V_peak / I_inrush, max = 340V / 50A = 6.8 Ω`.

3.  **Calculate NTC Resistance:**
    `R_NTC_min = R_total_min - R_line = 6.8 Ω - 0.5 Ω = 6.3 Ω`.

**Result:** An NTC thermistor with an initial "cold" resistance of **at least 6.3 Ω** is required. A standard 10 Ω NTC thermistor would be a safe choice, limiting the inrush current to `340V / (0.5Ω + 10Ω) ≈ 32.4A`, well below the breaker's trip point.

***

### 5.6 Conclusion: More Than Just Watts and Volts

The power supply is a cornerstone of CNC system stability and performance. A systems-level approach to selection, moving beyond simplistic summation of nameplate ratings, is essential. Proper sizing requires a careful analysis of **voltage requirements** based on motor technology, and **current requirements** based on realistic duty cycles and drive architecture. For dynamic servo systems, managing **regenerative energy** through adequate bulk capacitance and braking resistors is non-negotiable to prevent over-voltage faults. Finally, integrated **protection circuits** are the final line of defense that ensures the safety and longevity of the entire control system. Investing in a high-quality, correctly sized industrial power supply is one of the most effective ways to guarantee a reliable and high-performing machine.

---

## References

1. **ISO 230-2:2014** - Test code for machine tools - Positioning accuracy
2. **ISO 13849-1:2015** - Safety of machinery - Safety-related control systems
3. **Franklin, G.F., Powell, J.D., & Emami-Naeini, A. (2014).** *Feedback Control of Dynamic Systems* (7th ed.). Pearson
4. **Ogata, K. (2009).** *Modern Control Engineering* (5th ed.). Pearson
5. **LinuxCNC Integrator's Manual** (linuxcnc.org) - CNC control configuration
6. **Mach4 CNC Controller** (machsupport.com) - Software documentation
7. **FANUC CNC Series Technical Manuals** - Industrial controller specifications
8. **IEC 61000 Series** - Electromagnetic compatibility (EMC) standards
