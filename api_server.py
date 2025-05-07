from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()
#app.mount("/static", StaticFiles(directory="web_dashboard"), name="static")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

csv_file = 'machine_data.csv'

def read_machine_data():
    if not os.path.exists(csv_file):
        return None
    return pd.read_csv(csv_file)

@app.get("/")
def home():
    return {"message": "Welcome to Smart Factory Connector API!"}

@app.get("/latest")
def get_latest_record():
    df = read_machine_data()
    if df is None or df.empty:
        return {"message": "No data available yet."}
    
    latest_record = df.tail(1).to_dict(orient="records")[0]
    return latest_record

@app.get("/history")
def get_last_10_records():
    df = read_machine_data()
    if df is None or df.empty:
        return {"message": "No data available yet."}
    
    last_10 = df.tail(30).to_dict(orient="records")
    return last_10

@app.get("/latest_all")
def get_latest_per_machine():
    df = read_machine_data()
    if df is None or df.empty:
        return {"message": "No data available yet."}

    latest_by_machine = (
        df.sort_values("timestamp")
          .groupby("machine_id", as_index=False)
          .tail(1)
          .sort_values("machine_id")
    )

    return latest_by_machine.to_dict(orient="records")

