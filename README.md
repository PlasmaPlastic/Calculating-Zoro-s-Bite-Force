# ⚔️ Calculating Zoro's Bite Force in the Three-Sword Style

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A physics-based analysis & Python simulation of Roronoa Zoro's jaw clamping force required to block a cannonball in Three-Sword Style.

---

## 📌 Project Overview

In *One Piece*, Roronoa Zoro holds a third sword (Wado Ichimonji) in his mouth while fighting. This project constructs a simplified mechanical rigid-body model and a Python numerical simulation to estimate the theoretical jaw force required to retain the mouth-held sword during an extreme cannonball impact.

<p align="center">
  <img src="https://i.pinimg.com/1200x/cc/ff/8c/ccff8c0784aa47f4c08fc73719226539.jpg" width="450" alt="Zoro Three-Sword Style">
</p>

---

## 📊 Summary of Results

* **Theoretical Minimum Jaw Force:** `367.10 tf` (~3,600,000 N)
  * **Average Impact Force:** `450.00 kN` (15 kg cannonball at 450 m/s, $\Delta t = 0.015$ s)
* **Impact Torque:** `180,000 N·m` (Lever arm $r = 0.40$ m)
* **Key Comparisons:**
  * **~4,000×** an average adult human bite force (0.05–0.09 tf)
  * **~20–36×** the estimated upper bite force of a Megalodon (10.2–18.36 tf)
  * **~229.4×** the model's assumed Young Zoro baseline (1.6 tf)

---

## 📂 Repository Structure

```text

├── Calculating Zoro's Bite Force in the Three-Sword Style Cannon Scene.pdf
├── simulation.py     # Python physics simulation
└── README.md

```

---

## 💡 Extra TMI: Zoro's Teeth Strength & Material Analysis

When applying **3,600,000 N** over the tiny bite contact area ($\approx 10 \text{ cm}^2$), the compressive pressure exerted on Zoro's teeth reaches **~3.60 GPa** (Gigapascals).

To put **3.60 GPa** into perspective, this equals a load of **36 tons force per 1 cm²**.

### 💎 Compressive Strength Comparison (GPa)

| Material | Compressive Strength (GPa) | Status under Zoro's Load (3.6 GPa) |
| :--- | :--- | :--- |
| Real Human Teeth Enamel | `~0.36 GPa` | 💥 **Instantly shattered into powder** |
| Titanium Alloy (Grade 5) | `~1.15 GPa` | 🔨 **Permanently crushed & deformed** |
| Tungsten Carbide  | `3.0 ~ 5.0 GPa`| ⚙️ **Barely holds (Industrial Cutting Tool level)** |
| Zoro's Required Tooth Strength | **`~3.60 GPa`** | ⚔️ **Resists 450 kN cannonball impact** |
| Diamond (Natural) | `60 ~ 110+ GPa` | 💎 **Perfectly holds without any damage** |

### 🛠️ Real-World Equivalent Materials (3.6 GPa Level)
* **Tungsten Carbide (WC):** Used in industrial drill bits and metal cutting tools.
* **Advanced Ceramics ($\text{Si}_3\text{N}_4$, $\text{Al}_2\text{O}_3$):** Used in bulletproof armor plates and high-speed bearings.
* **Ultra-High-Strength Tool Steel:** Special heat-treated martensitic steel.

> 📌 **Conclusion:**  
> Real human teeth (`0.36 GPa`) would instantly vaporize into dust.  
> To withstand **3.60 GPa** of compressive pressure without breaking, **Zoro's teeth must have a hardness and mechanical durability equivalent to Industrial Tungsten Carbide or Natural Diamond.**
