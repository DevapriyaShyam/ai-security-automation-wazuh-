import time
import json
import os

print("Remediation Engine Started...")

while True:
    if os.path.exists("/shared/analysis.json"):
        with open("/shared/analysis.json", "r") as f:
            alert = json.load(f)
        if alert["severity"] == "high":
            print("Action: Disable suspicious user (controlled allowlisted action)")
        else:
            print("No action required")
    time.sleep(15)
