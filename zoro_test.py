"""
ZORO THREE-SWORD PHYSICS SIMULATION
Experimental measurement of jaw clamping force required to retain a sword
against cannonball impact.
"""

import math

# ========== MODEL CONSTANTS ==========
SWORD_MASS = 1.5          # kg
SWORD_LENGTH = 1.35       # m
COM_DIST = 0.4            # m, center of mass from jaw
JAW_CONTACT = 0.05        # m, bite contact distance (moment arm)
FRICTION_COEF = 0.5

CANNON_MASS = 15.0        # kg, 36-pound cannonball
CANNON_VEL = 450.0        # m/s
COLLISION_DT = 0.015      # s

G = 9.80665

# ========== DERIVED PHYSICS ==========
MOMENTUM_J = CANNON_MASS * CANNON_VEL
F_IMPACT = MOMENTUM_J / COLLISION_DT
TAU_IMPACT = F_IMPACT * COM_DIST
THEORETICAL_TF = TAU_IMPACT / JAW_CONTACT / G / 1000

MAX_ROTATION_DEG = 5.0
MAX_JAW_OPENING_CM = 5.1

def simulate(jaw_tf):
    jaw_N = jaw_tf * 1000 * G
    rot_resist = jaw_N * JAW_CONTACT
    friction_limit = jaw_N * FRICTION_COEF
    gravity_torque = SWORD_MASS * G * COM_DIST

    if rot_resist >= TAU_IMPACT * 1.1:
        rotation = 0.0
        jaw_opening = 5.0
        result = "SUCCESS"
        reason = "Sword remains secured after impact"
    elif rot_resist >= TAU_IMPACT:
        rotation = (TAU_IMPACT - rot_resist * 0.95) / TAU_IMPACT * 10.0
        rotation = max(0.0, rotation)
        jaw_opening = 5.0 + rotation * 0.05
        if rotation < MAX_ROTATION_DEG:
            result = "SUCCESS"
            reason = "Sword remains secured after impact"
        else:
            result = "FAILED"
            reason = "Sword rotation angle limit exceeded"
    else:
        deficit = (TAU_IMPACT - rot_resist) / TAU_IMPACT
        rotation = 48.5 * deficit + 0.5
        jaw_opening = 5.1 + deficit * 2.0
        if jaw_opening > MAX_JAW_OPENING_CM:
            result = "FAILED"
            reason = "Jaw opening limit exceeded"
        else:
            result = "FAILED"
            reason = "Sword rotation angle limit exceeded"

    displacement = max(0.0, (F_IMPACT - friction_limit) / 1e6) * 10

    return {
        "jaw_tf": jaw_tf,
        "jaw_N": jaw_N,
        "rot_resist": rot_resist,
        "friction": friction_limit,
        "gravity_torque": gravity_torque,
        "rotation": rotation,
        "displacement": displacement,
        "jaw_opening": jaw_opening,
        "result": result,
        "reason": reason
    }

def find_minimum():
    low, high = 0.0, 2000.0
    for _ in range(30):
        mid = (low + high) / 2
        if simulate(mid)["result"] == "SUCCESS":
            high = mid
        else:
            low = mid
    return high

# ========== CLI OUTPUT ==========
print("="*72)
print("        ZORO THREE-SWORD PHYSICS SIMULATION")
print("                    CLI VERSION")
print("="*72)

print("\nPHYSICS MODEL")
print("-"*72)
print(f"Sword mass             : {SWORD_MASS} kg")
print(f"Sword length           : {SWORD_LENGTH} m")
print(f"Center of mass         : {COM_DIST} m")
print(f"Impact point           : {COM_DIST} m")
print(f"Jaw contact distance   : {JAW_CONTACT} m")
print(f"Friction coefficient   : {FRICTION_COEF}")
print(f"Cannonball mass        : {CANNON_MASS} kg")
print(f"Cannonball velocity    : {CANNON_VEL} m/s")
print(f"Collision duration     : {COLLISION_DT} s")
print("")
print(f"Cannonball momentum J  : {MOMENTUM_J:,.2f} kg·m/s")
print(f"Impact force F_impact  : {F_IMPACT:,.2f} N")
print(f"Impact torque T_impact : {TAU_IMPACT:,.2f} Nm")

print("\n" + "="*72)
print("                    SIMULATION START")
print("="*72)

cases = [
    (0.015, "12 kgf"),
    (0.08, "80 kgf"),
    (1.6, "1.6 t - Young Zoro"),
    (10, "10 t"),
    (100, "100 t"),
    (367.10, "367.1 t - Theoretical Threshold"),
    (400, "400 t - Practical Minimum"),
    (1000, "1000 t"),
    (2000, "2000 t"),
]

for i, (tf, label) in enumerate(cases, 1):
    r = simulate(tf)
    print(f"\n{'='*72}")
    print(f"[{i}] {label}")
    print("-"*72)
    print(f"Jaw force        : {r['jaw_tf']:.3f} tf ({r['jaw_N']/1000:.2f} kN)")
    print(f"Gravity torque   : {r['gravity_torque']:.2f} Nm")
    print(f"Rotational resistance : {r['rot_resist']:.2f} Nm")
    print(f"Friction limit   : {r['friction']:.2f} N")
    print(f"Impact force     : {F_IMPACT/1000:.2f} kN ({F_IMPACT/G/1000:.2f} tf)")
    print(f"Impact torque    : {TAU_IMPACT:,.2f} Nm")
    print(f"Sword rotation   : {r['rotation']:.2f}°")
    print(f"Sword displacement : {r['displacement']:.4f} cm")
    print(f"Jaw opening      : {r['jaw_opening']:.4f} cm")
    print("")
    print(f"Result           : {r['result']}")
    print(f"Reason           : {r['reason']}")

minimum = find_minimum()

print("\n\n" + "="*72)
print("                         SUMMARY")
print("="*72)
print(f"\n{'Jaw Force':<22} {'Rot. Resistance (Nm)':<22} {'Impact Torque (Nm)':<20} {'Result'}")
print("-"*72)
for tf, label in cases:
    r = simulate(tf)
    print(f"{label:<22} {r['rot_resist']:>15,.0f} {TAU_IMPACT:>18,.0f}     {r['result']}")

success_count = sum(1 for tf,_ in cases if simulate(tf)["result"]=="SUCCESS")
fail_count = len(cases) - success_count

print(f"\nSUCCESS : {success_count}")
print(f"FAILED  : {fail_count}")
print(f"\nMinimum successful jaw force : {minimum:.2f} tf ({minimum*G:.2f} kN)")
print(f"Theoretical threshold        : {THEORETICAL_TF:.2f} tf")
print(f"Growth from Young Zoro       : {minimum/1.6:.1f} x ( {minimum:.2f} / 1.6 )")

print("\n" + "="*72)
print("SIMULATION COMPLETE")
print("="*72)