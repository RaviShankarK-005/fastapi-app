from sqlalchemy import Column, Integer, Float, String, DateTime
from dbutil.database import Base
import datetime

class User(Base):
    __tablename__ = "user"

    userid = Column(Integer, primary_key=True, index=True)
    username = Column(String(32),unique=True,index=True)
    email = Column(String(40),unique=True,index=True)
    password = Column(String(120))
    role = Column(String(15))
    mobile = Column(String(10),unique=True,index=True)
    createdon = Column(DateTime, default=datetime.datetime.utcnow)
    updateddon = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

