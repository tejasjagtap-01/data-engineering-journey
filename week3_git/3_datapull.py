from dataloader import DataLoader
from sqlalchemy import create_engine

# 1. Connect to PostgreSQL (placeholder credentials for public repo)
engine = create_engine("postgresql://username:password@server:port/database")

# 2. Initialize DataLoader with the source file
loader = DataLoader("data/f1_2023_results.csv")

# 3. Ingest and extract the DataFrame
loader.load()  # or loader.fetch() / loader.clean_data()
loader.clean()
df = loader.data

# 4. Write into the database table
df.to_sql("table_name", con=engine, if_exists="replace", index=False)
print("Data successfully loaded into PostgreSQL!")