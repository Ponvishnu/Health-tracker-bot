import pandas as pd
from datetime import date
import os

DATA_PATH = "data/health_log.csv"

def init_data_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_PATH):
        df = pd.DataFrame(columns=["date", "metric", "value"])
        df.to_csv(DATA_PATH, index=False)

def log_data(metric, value):
    init_data_file()
    df = pd.read_csv(DATA_PATH)
    df = df.append({"date": date.today().isoformat(), "metric": metric, "value": value}, ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

def get_daily_summary():
    init_data_file()
    df = pd.read_csv(DATA_PATH)
    today = date.today().isoformat()
    today_data = df[df['date'] == today]
    return today_data.groupby("metric")["value"].sum().to_dict()
