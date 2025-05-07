import pandas as pd
import time
import os

csv_file = 'machine_data.csv'

def show_last_records():
    if not os.path.exists(csv_file):
        print("No data available yet.")
        return

    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Show the last 5 records
    last_records = df.tail(5)

    print("\n--- Last 5 Machine Records ---")
    print(last_records.to_string(index=False))
    print("------------------------------")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        show_last_records()
        time.sleep(5)  # Refresh every 5 seconds

if __name__ == "__main__":
    main()
