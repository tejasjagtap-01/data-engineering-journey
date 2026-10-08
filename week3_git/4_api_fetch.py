from dataloader import DataLoader
from apiloader import APILoader   # Pull in your own two classes from other files in the same folder
from sqlalchemy import create_engine  #Tool to connect to a database
import pandas as pd  #data-handling toolkit

engine = create_engine("postgresql://username:password@server:port/database")  #Prepares (doesn't yet open) the connection to f1db

#Existing CSV pipeline 
loader = DataLoader(r"data/fact_race_results.csv")  #Creates an object that knows which CSV file to handle
loader.load()  #Actually reads the CSV into memory
loader.clean()  #	Drops nulls, tracks row counts
loader.data.to_sql('Table_Name', con=engine, if_exists = 'replace', index = False)   #Writes the cleaned CSV data into a Postgres table
print("CSV pipeline complete")

#New: API pipeline 
api = APILoader("API/results.json")   #Creates an object that knows which API URL to hit
api.fetch()   #Actually calls the API, stores the nested JSON response

#For Example.
races = api.data['MRData']['RaceTable']['Races']   #Digs into the nested response to reach the list of races

api_df = pd.json_normalize(  
    record_path='Results',
    meta=['season', 'round', 'raceName', 'date']
)  #Explodes each race's nested Results list into individual rows, keeping race-level info (season, round, etc.) attached to each

api_df.to_sql('NEW_SQL_TABLE_NAME', engine, if_exists='replace', index=False)   #Writes the flattened API data into a second Postgres table
print("API Pipeline Completed")