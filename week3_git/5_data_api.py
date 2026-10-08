import logging
from dataloader import DataLoader
from apiloader import APILoader
from sqlalchemy import create_engine
import pandas as pd

logging.basicConfig(
    filename='FileName.log', # WHERE: Saves logs to this file on disk instead of printing to terminal.  
    level=logging.INFO, # THRESHOLD: Logs this severity level and anything higher (INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s : %(levelname)s : %(message)s' # STRUCTURE: Defines how each log line looks.
)

engine = create_engine("postgresql://username:password@server:port/database")

#Existing CSV pipeline 
loader = DataLoader(r"data/fact_race_results.csv")  #Creates an object that knows which CSV file to handle
loader.load()  #Actually reads the CSV into memory
loader.clean()  #	Drops nulls, tracks row counts
loader.data.to_sql('Table_Name', con=engine, if_exists = 'replace', index = False)   #Writes the cleaned CSV data into a Postgres table
logging.info("CSV Pipeline Complete")
print("CSV pipeline complete")


#API Pipeline
api = APILoader("API/results.json") #Creates an object that knows which API URL to hit
api.fetch()  #Actually calls the API, stores the nested JSON response

races = api.data['MRData']['RaceTable']['Races'] #Digs into the nested response to reach the list of races

api_df = pd.json_normalize(
    races,
    record_path='Results',
    meta=['season', 'round', 'raceName', 'date'] #Explodes each race's nested Results list into individual rows, keeping race-level info (season, round, etc.) attached to each
)

api_df.to_sql('API race results', con=engine, if_exists='replace', index=False) #Writes the flattened API data into a second Postgres table
logging.info("API Pipeline Complete")
print("API Pipeline Completed")