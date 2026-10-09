import logging
from dataloader import DataLoader
from apiloader import APILoader
from sqlalchemy import create_engine
import pandas as pd

logging.basicConfig(
    filename=r'file.log',
    level=logging.INFO,
    format='%(asctime)s : %(levelname)s : %(message)s'
)

engine = create_engine("postgresql://username:password@server:port/database")

#CSV Pipeline
loader = DataLoader(r'data/fact_lap_times.csv')
loader.load()
# print(loader.data.head())
loader.data.to_sql('lap_times', engine, if_exists='replace', index=False)
logging.info("CSV Pipeline Complete")
print("CSV Pipeline Completed")

#API Pipeline
api = APILoader("API/results.json")
api.fetch()

races = api.data['MRData']['RaceTable']['Races']

api_df = pd.json_normalize(
    races,
    record_path='Results',
    meta=['season', 'round', 'raceName', 'date']
)

api_df.to_sql('SQL Table Name', con = engine, if_exists='replace', index=False)
logging.info("API Pipeline Complete")
print("API Pipeline Completed")