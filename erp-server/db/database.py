from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Настройка подключения к PostgreSQL
DATABASE_URI = 'postgresql://postgres:A12345aa@localhost:5432/Smartbox SQL'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
