import json
import random
import time
from datetime import datetime, timedelta

src_ips = ["192.168.1." + str(i) for i in range(1, 50)]
dst_ips = ["10.0.0." + str(i) for i in range(1, 50)]
ports = [22, 80, 443, 3389, 53, 8080]
actions = ["allowed", "blocked"]
protocols = ["TCP", "UDP", "ICMP"]

def generate_firewall_log():
    log = {
        "timestamp": (datetime.now() - timedelta(seconds=random.randint(0, 3600))).isoformat(),
        "src_ip": random.choice(src_ips),
        "dst_ip": random.choice(dst_ips),
        "src_port": random.randint(1024, 65535),
        "dst_port": random.choice(ports),
        "action": random.choice(actions),
        "protocol": random.choice(protocols),
        "rule_name": f"Rule-{random.randint(1, 10)}",
        "fw_device": f"fw-{random.randint(1,3)}.corp.local"
    }
    return log

logs = [generate_firewall_log() for _ in range(100)]

with open("firewall_logs.json", "w") as f:
    for entry in logs:
        json.dump({"event": entry}, f)
        f.write("\n")

print("Berhasil generate 100 firewall logs di 'firewall_logs.json'")
