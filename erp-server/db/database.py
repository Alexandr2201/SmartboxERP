from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

# Настройка подключения к PostgreSQL
DATABASE_URI = Config.DATABASE_URI
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
