import pandas as pd

class DataLoader:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load(self):
        try:
            self.data = pd.read_csv(self.filepath)
        except FileNotFoundError:
            print(f'File not found: {self.filepath}')
        return self.data

p = DataLoader(r"C:\Users\tejas\OneDrive\Desktop\numpy python\11. F1\f1\fact_race_results.csv")
p = p.load()
print(p.head(5))
print(p.tail())