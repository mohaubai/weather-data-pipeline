FROM python:3.10-slim

WORKDIR /weather_etl_pipeline

COPY weather_etl.py .

RUN pip install requests pandas sqlalchemy psycopg2-binary

CMD ["python", "weather_etl.py"]