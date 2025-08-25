import os
import argparse
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environmnet variables from .env file
load_dotenv()

# Getting DB credentials from environment variables
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DB = os.getenv("POSTGRES_DB")

ENGINE = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

# CLI argument parsing
parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
parser.add_argument("--url", required=True, help="URL of the CSV file")
parser.add_argument("--table_name", required=True, help="Name of the target table in Postgres")
parser.add_argument("--output_file", required=True, help="Path to save the downloaded CSV file")
args = parser.parse_args()

# Reading of CSV file
print("[1/3] Downloading and reading of CSV file from URL...")
df = pd.read_csv(args.url)

# Transforming Data (Just simple column conversion to datetime as an example)
print("[2/3] Transforming data...")
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

# Creating folder /data if not exists and saving a local copy of the CSV file
os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
df.to_csv(args.output_file, index=False)

# Loading data to Postgres
print("[3/3] Loading data to Postgres...")
df.to_sql(name=args.table_name, con=ENGINE, if_exists="replace", index=False)
print(f"Data successfully loaded to the '{args.table_name}' table in Postgres.")
