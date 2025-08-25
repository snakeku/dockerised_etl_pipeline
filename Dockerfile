FROM python:3.9-slim

WORKDIR /app

# Install Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Python Ingest Script
COPY ingest_data.py .

# Command to run the script
ENTRYPOINT ["python", "ingest_data.py"]