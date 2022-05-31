from email.mime import base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    password = Column(String(8))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_update = Column(DateTime(timezone=True), onupdate=func.now())
