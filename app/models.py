from sqlalchemy import Column, Integer, String

from .database import Base

# Herda de Base criada em database.py para criar os models
class Student(Base):
    __tablename__ = "students"

    ra = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    course = Column(String, nullable=False)
    subject = Column(String, nullable=False)
