from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from postgres_conn import ConnectToPostgres
from datetime import datetime

Base = declarative_base()

class CityChart(Base):
    
    __tablename__ = 'city_chart'
    date = Column('date', datetime)
    city_id = Column('city_id',String,primary_id=True)
    city_name = Column('city_name', String)
    Views = Column('Views',Integer)

    def __init__(self,date,city_id,city_name,Views):
      self.date = date
      self.city_id = city_id
      self.city_name = city_name
      self.Views = Views


# Replace the connection string with the appropriate one for your PostgreSQL database
engine = create_engine('postgresql://username:password@localhost:15432/youtube_data', echo=True)
Base.metadata.create_all(bind=engine)