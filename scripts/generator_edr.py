import json
import random
from datetime import datetime, timedelta

behaviors = ["Process Hollowing", "Registry Modification", "Code Injection", "Script Execution", "Credential Du>processes = ["powershell.exe", "cmd.exe", "svchost.exe", "lsass.exe", "explorer.exe"]
users = [f"user{i}" for i in range(1, 30)]

def generate_edr_log():
    return {
        "timestamp": (datetime.now() - timedelta(seconds=random.randint(0, 7200))).isoformat(),
        "device_name": f"endpoint-{random.randint(1, 50)}",
        "user": random.choice(users),
        "suspicious_behavior": random.choice(behaviors),
        "process_name": random.choice(processes),
        "pid": random.randint(1000, 10000),
        "parent_process": random.choice(processes),
        "risk_score": random.randint(20, 100)
    }

logs = [{"event": generate_edr_log()} for _ in range(100)]

with open("edr_logs.json", "w") as f:
    for log in logs:
        json.dump(log, f)
        f.write("\n")

print("Berhasil generate 100 EDR logs di 'edr_logs.json'")
