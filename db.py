from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DB_CONNECTOR

engine = create_engine(DB_CONNECTOR)
Session = sessionmaker(bind=engine)

Base = declarative_base()
