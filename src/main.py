import polars as pl
import duckdb

CSV_PATH = "./data/csv/data.csv"
DELTA_PATH = "./data/delta"

df = pl.read_csv(CSV_PATH)
df.write_delta(DELTA_PATH, mode="overwrite")

delta_df = pl.read_delta(DELTA_PATH)
duckdb.sql("SELECT id, full_name FROM delta_df").show()
    