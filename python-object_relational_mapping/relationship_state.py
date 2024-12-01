from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_base import Base  # Assuming you have Base defined in model_base.py

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Establish a relationship with the City model
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
