import pandas as pd 

class DataLoader:

    def __init__(self, filepath):
        self.filepath= filepath
        self.data = None

    def load(self):
        self.data = pd.read_csv(self.filepath)
        print("Data loaded Successfully")
        return self.data 

    def clean(self):
        rows_before = len(self.data)
        self.data = self.data.dropna()
        rows_after = len(self.data)
        print(f'Dropped {rows_before} - {rows_after} rows')
        return self.data

    def summary(self):
        print(f'Shape: {self.data.shape}')
        print(f"Nulls per column:\n{self.data.isnull().sum()}")


race_results = DataLoader(r"C:\Users\tejas\OneDrive\Desktop\numpy python\11. F1\f1\fact_race_results.csv")
race_results.load()
race_results.clean()
race_results.summary()


drivers =  DataLoader("C:/Users/tejas/OneDrive/Desktop/numpy python/11. F1/drivers.csv")
drivers.load()
drivers.clean()
drivers.summary()

# print(race_results.data.isnull().sum())

# print(race_results.data.head())
# print(race_results.data.isnull().sum())
# race_results = race_results.data.dropna()
# print(race_results.isnull().sum())

# print(drivers.data.head())
# print(drivers.data.tail())
# print(drivers.data.columns)
print(drivers.data.isnull().sum())