import json
import time
import random
import threading
import requests
from datetime import datetime, timezone

# Load config
with open("config.json") as f:
    config = json.load(f)

ENDPOINT = config["endpoint"]

def generate_value(sensor_type):
    if sensor_type == "temperature":
        return round(random.uniform(15, 35), 2)   # °C
    if sensor_type == "humidity":
        return round(random.uniform(30, 90), 2)   # %
    if sensor_type == "light":
        return round(random.uniform(100, 1000), 2)  # lux

def sensor_worker(sensor):
    sensor_type = sensor["type"]
    interval = sensor["interval_ms"] / 1000
    location = sensor.get("location", {"lat": 0, "lon": 0})  # Default if missing

    while True:
        payload = {
            "sensor_type": sensor_type,
            "value": generate_value(sensor_type),
            # "timestamp": datetime.now().isoformat(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "location": location
        }

        # try:
        #     requests.post(ENDPOINT, json=payload, timeout=1)
        #     print(f"[{sensor_type}] sent:", payload)
        # except Exception as e:
        #     print(f"[{sensor_type}] error:", e)
        try:
            response = requests.post(ENDPOINT, json=payload, timeout=1)
            if response.status_code == 200:
                print(f"[{sensor_type}] sent: {payload}")
            else:
                print(f"[{sensor_type}] FAILED: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[{sensor_type}] error: {e}")

        time.sleep(interval)

# Start all sensors
for sensor in config["sensors"]:
    t = threading.Thread(target=sensor_worker, args=(sensor,))
    t.daemon = True
    t.start()

print("IoT emulator started...")
while True:
    time.sleep(1)
