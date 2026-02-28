import time
import json

print("AI Engine Started...")

while True:
    print("AI analysing incoming alert")

    alert = {
        "event_id": 4720,
        "severity": "high",
        "description": "Suspicious account creation detected"
    }
    with open("/shared/analysis.json", "w") as f:
         json.dump(alert, f)

    print("AI classified alert as HIGH Severity")
    time.sleep(15)
