print("--- AI Project 18: Hyper-Defense Core Initialized 🛡️⚛️ ---")

def hyper_defense_grid_controller(threat_level_score, quantum_encryption_active, system_load_percentage):
    if threat_level_score > 85.0 and not quantum_encryption_active:
        print("[Critical Breach Alert: High threat detected with compromised encryption!]")
        if system_load_percentage > 90.0:
            return "Defense Action: Emergency Core Purge, Server Isolation & Blackout Mode 🚨🔥"
        else:
            return "Defense Action: Immediate Firewall Lockdown & Emergency IP Blacklisting 🛑🔒"
    elif threat_level_score <= 30.0 and quantum_encryption_active and system_load_percentage < 50.0:
        print("[Grid Status: System is fully secure, encrypted, and operating normally.]")
        return "Defense Action: Maintain Optimal Autonomous Operations & Routine Backup ✅⚡"
    else:
        print("[Grid Warning: Moderate anomaly or fluctuating quantum state detected.]")
        return "Defense Action: Engage Secondary Redundant Shield & Rate-Limiting Protocols ⚠️🔄"

print(hyper_defense_grid_controller(92.5, False, 95.0))
print("-" * 75)
print(hyper_defense_grid_controller(88.0, False, 75.0))
print("-" * 75)
print(hyper_defense_grid_controller(15.0, True, 40.0))
