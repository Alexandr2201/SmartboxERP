from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import config_instance

# Настройка подключения к PostgreSQL
DATABASE_URI = config_instance.DATABASE_URI
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()