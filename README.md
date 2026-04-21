# 🌤️ Weather Data Pipeline & API

An end-to-end, fully containerized Data Engineering and Backend architecture that extracts live weather data, stores it in a relational database, and serves it via a REST API.

## 🚀 Architecture Stack
* **Language:** Python
* **Data Engineering:** Pandas, SQLAlchemy, Requests
* **Database:** PostgreSQL
* **API:** FastAPI, Uvicorn
* **Infrastructure:** Docker, Docker Compose

## ⚙️ How It Works
1. **The ETL Service:** A Python script fetches live API data, transforms it using Pandas, and loads it into a PostgreSQL data warehouse.
2. **The Database:** A containerized PostgreSQL server automatically initializes the schema and stores historical time-series data.
3. **The API Service:** A FastAPI backend connects to the database and serves the cleansed data as JSON for frontend consumption.

## 🛠️ Run it Locally
```bash
docker-compose up --build