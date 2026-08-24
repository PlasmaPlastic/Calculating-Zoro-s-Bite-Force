# ⚔️ Calculating Zoro's Bite Force in the Three-Sword Style

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A physics-based analysis & Python simulation of Roronoa Zoro's jaw clamping force required to block a cannonball in Three-Sword Style.

---

## 📌 Project Overview

In *One Piece*, Roronoa Zoro holds a third sword (Wado Ichimonji) in his mouth while fighting[cite: 1]. This project constructs a simplified mechanical rigid-body model and a Python numerical simulation to estimate the theoretical jaw force required to retain the mouth-held sword during an extreme cannonball impact[cite: 1].

<p align="center">
  <img src="https://i.pinimg.com/1200x/cc/ff/8c/ccff8c0784aa47f4c08fc73719226539.jpg" width="450" alt="Zoro Three-Sword Style">
</p>

---

## 📊 Summary of Results

* **Theoretical Minimum Jaw Force:** `367.10 tf` (~3,600,000 N)[cite: 1]
* **Average Impact Force:** `450.00 kN` (15 kg cannonball at 450 m/s, $\Delta t = 0.015$ s)[cite: 1]
* **Impact Torque:** `180,000 N·m` (Lever arm $r = 0.40$ m)[cite: 1]
* **Key Comparisons:**
  * **~4,000×** an average adult human bite force (0.05–0.09 tf)[cite: 1]
  * **~20–36×** the estimated upper bite force of a Megalodon (10.2–18.36 tf)[cite: 1]
  * **~229.4×** the model's assumed Young Zoro baseline (1.6 tf)[cite: 1]

---

## 📂 Repository Structure

```text
.
├── Calculating Zoro's Bite Force in the Three-Sword Style Cannon Scene.pdf
├── simulation.py     # Python physics simulation
└── README.md

