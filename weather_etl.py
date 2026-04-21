import requests
import json
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine #import sqlite3
import time

print("Waiting for the database to be ready...")
time.sleep(10)

hubs = [
    {"city": "New York", "lat": 40.7143, "lon": -74.0060},
    {"city": "London", "lat": 51.5085, "lon": -0.1257},
    {"city": "Tokyo", "lat": 35.6895, "lon": 139.6917}
]

class WeatherAPIClient:
  def __init__(self, url):
    self.url = url

  def get_current_temp(self):
    try:
      data = requests.get(self.url)
      json_data = data.json()
      temperature = json_data['current_weather']['temperature']
      return temperature
    except Exception as e:
      print("Warning: Failed to fetch data")
      return None

for hub_data in hubs:
  nyc_weather_client = WeatherAPIClient(f"https://api.open-meteo.com/v1/forecast?latitude={hub_data['lat']}&longitude={hub_data['lon']}&current_weather=true")
  hub_data['temperature'] = nyc_weather_client.get_current_temp()

weather_df = pd.DataFrame(hubs)
weather_df.rename(columns={'temperature': 'Current_Temp_C'}, inplace=True)
weather_df['timestamp'] = datetime.utcnow()
print(weather_df)

#----------------------SQLITE----------------------------#

# conn = sqlite3.connect("weather_warehouse.db")
# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE weather_logs(
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   city TEXT,
#   lat REAL,
#   lon REAL,
#   Current_Temp_C REAL,
#   timestamp DATETIME
# )""")
# weather_df.to_sql('weather_logs', conn, if_exists='append', index=False)
# query_2 = cursor.execute("SELECT * FROM weather_logs").fetchone()
# print(query_2)
# conn.commit()
# conn.close()

#-----------------------POSTGRESQL----------------------------#
engine = create_engine("postgresql://ubaid:admin@db:5432/weather_db")

weather_df.to_sql('weather_logs', engine, if_exists='append', index=False)

query_1 = pd.read_sql("SELECT * FROM weather_logs", engine)
print(query_1)