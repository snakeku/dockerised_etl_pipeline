# Dockerised ETL Pipeline: NYC Taxi Data

This project demonstrates a simple data engineering pipeline using the following:

- Docker
- Docker Compose
- Postgres
- pgAdmin
- Python

It extracts the NYC Taxi trip csv data via a url, does simple data transformation, and lastly load the data into a Postgres database for future analysis.

---

# Tech Stack

- Postgres - Database to store raw and transformed data
- pgAdmin - UI browser for querying and managing the DB
- Python - Pandas and SQLAlchemy for ingestion and transformation
- Docker Compose - Container orchestration for reproducibility

---

# How to Run

1. Clone the repo
   `cp .env.example .env`

2. Build Ingestor Image (Python script)
   `docker compose build ingestor`

3. Start Postgres + pgAdmin
   `docker compose up -d postgres pgadmin`

4. Run Python ingestion script
   `docker compose run --rm ingestor --url "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz" --table_name yellow_taxi_trips --output_file data/yellow_2024_01.csv`

5. Query Data via pgadmin

- Open pgAdmin via http://localhost:8080/
- Create/Register server and input the following:
  1. Name "local docker etl"
  2. Under 'Connection' tab, fill in the following:
     2.1 Host name: "postgres"
     2.2 port: "5432"
     2.3 username: "root"
     2.4 password: "root"
- Copy paste queries from sql/test_queries.sql
