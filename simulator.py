import random
import time
import csv
import os
from datetime import datetime

csv_file = 'machine_data.csv'

# Write header if file does not exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["machine_id", "temperature", "pressure", "status", "timestamp"])

def generate_machine_data(machine_id):
    temperature = round(random.uniform(30.0, 90.0), 2)
    pressure = round(random.uniform(1.0, 6.0), 2)
    status = random.choice(["ON", "OFF"])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "machine_id": machine_id,
        "temperature": temperature,
        "pressure": pressure,
        "status": status,
        "timestamp": timestamp
    }

def save_to_csv(data):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            data["machine_id"],
            data["temperature"],
            data["pressure"],
            data["status"],
            data["timestamp"]
        ])

def main():
    machine_ids = [1, 2, 3]  # You can add more later!

    while True:
        for machine_id in machine_ids:
            data = generate_machine_data(machine_id)
            save_to_csv(data)
            print(f"[{data['timestamp']}] MachineID: {data['machine_id']} | "
                  f"Temp: {data['temperature']}°C | Pressure: {data['pressure']} bar | Status: {data['status']}")
        time.sleep(5)

if __name__ == "__main__":
    main()
