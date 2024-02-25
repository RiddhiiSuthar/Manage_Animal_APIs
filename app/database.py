import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from models import City
import uuid
PREDEFINED_CITIES = ["Frankfurt", "Berlin", "Hamburg", "Munich", "Cologne"]
# Add predefined cities to the database if they don't exist
with engine.connect() as conn:
    for city_name in PREDEFINED_CITIES:
        # Check if the city already exists in the table
        existing_city = conn.execute(
            City.__table__.select().where(City.name == city_name)
        ).fetchone()
        if not existing_city:
            city_id = str(uuid.uuid4())
            city = City(id=city_id, name=city_name)
            conn.execute(City.__table__.insert().values(id=city_id, name=city_name))
