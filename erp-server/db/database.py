from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config

# Настройка подключения к PostgreSQL
DATABASE_URI = config.DATABASE_URI
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
