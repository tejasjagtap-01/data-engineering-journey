# loading the CSV files into the Python Environment

import pandas as pd

class DataLoader:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load(self):
        self.data = pd.read_csv(self.filepath)
        print('Data Loaded Successfully')
        return self.data

fact_race_results = DataLoader(r"C:\Users\tejas\OneDrive\Desktop\numpy python\11. F1\f1\fact_race_results.csv")
race_result = fact_race_results.load()
print(race_result.head(2))

fact_pit_stops = DataLoader("C:/Users/tejas/OneDrive/Desktop/numpy python/11. F1/f1/fact_pit_stops.csv")
pit_stops = fact_pit_stops.load()
print(pit_stops.head(2))

fact_lap_times = DataLoader(r"C:\Users\tejas\OneDrive\Desktop\numpy python\11. F1\f1\fact_lap_times.csv")
lap_times = fact_lap_times.load()
print(lap_times.head(2))