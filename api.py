from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd
import uvicorn

app = FastAPI()

engine = create_engine("postgresql://ubaid:admin@localhost:5433/weather_db")

@app.get("/weather_data")
def get_weather_data():
    query = pd.read_sql("SELECT * FROM weather_logs", engine)
    return query.to_dict(orient="records")

if __name__=='__main__':
    uvicorn.run(app, port=8080)