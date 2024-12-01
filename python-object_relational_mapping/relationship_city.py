from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_base import Base  # Assuming you have Base defined in model_base.py

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define the relationship back to the State model
    state = relationship("State", back_populates="cities")
