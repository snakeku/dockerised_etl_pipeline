SELECT COUNT(*) AS total_rows FROM yellow_taxi_trips;

SELECT
  MIN(tpep_pickup_datetime) AS min_pickup,
  MAX(tpep_dropoff_datetime) AS max_dropoff
FROM yellow_taxi_trips;