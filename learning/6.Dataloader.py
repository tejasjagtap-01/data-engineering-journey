import pandas as pd 

class DataLoader:

    def __init__(self, filepath):
        self.filepath= filepath
        self.data = None

    def load(self):
        self.data = pd.read_csv(self.filepath)
        print("Data loaded Successfully")
        return self.data 

# race_results = DataLoader(r"C:\Users\tejas\OneDrive\Desktop\numpy python\11. F1\f1\fact_race_results.csv")
# race_results = race_results.load()
# print(race_results.head())

# drivers =  DataLoader("C:/Users/tejas/OneDrive/Desktop/numpy python/11. F1/drivers.csv")
# drivers = drivers.load()
# print(drivers.tail())

fact_lap_times = DataLoader("C:/Users/tejas/OneDrive/Desktop/numpy python/11. F1/f1/fact_lap_times.csv")
fact_lap_times = fact_lap_times.load()
print(fact_lap_times.columns)