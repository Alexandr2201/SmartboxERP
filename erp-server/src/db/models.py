from sqlalchemy import Column, Uuid, String
from db.database import Base

class User(Base):
    __tablename__ = 'users'

    uuid = Column(Uuid, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
