# F1 Data Pipeline

## What it does
Pulls F1 data from two independent sources — a local CSV file and a live API —
cleans/structures the data, and loads both into PostgreSQL. Both DataLoader and
APILoader are separate, independent classes (no inheritance between them);
the script just runs the CSV step first, then the API step, because that's the
order they're written in the main script.

## What it reads from
- A local CSV file (`fact_race_results.csv` / `fact_lap_times.csv`)
- The Jolpica-F1 API (live F1 race results)

## What it writes to
- `race_results` table in `f1db` — from the CSV source
- `api_race_results` table in `f1db` — from the API source

## How it works
1. `DataLoader` loads and cleans the CSV, writes it to `race_results` via `to_sql()`
2. `APILoader.fetch()` calls the API and stores the raw nested JSON response
3. `pd.json_normalize(..., record_path='Results', meta=[...])` flattens the nested
   API response into one row per driver result, keeping race-level info attached
4. The flattened API data is written to `api_race_results` via `to_sql()`
5. Every step logs to `pipeline.log` via Python's `logging` module — `logging.info()`
   for successful steps, `logging.error()` for failures

## How to run it 


## Bugs I hit and fixed
- `json_normalize()` alone doesn't flatten nested lists-within-lists — needed
  `record_path` and `meta` to properly explode race results into rows
- Leftover `print()` statements inside DataLoader/APILoader were firing on every
  run, even when not explicitly called — cleaned up to keep classes silent except
  for intentional logging
- Centralized logging configuration into the main script only, so DataLoader and
  APILoader just report into whatever logging setup the entry-point script provides