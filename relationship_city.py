#!/usr/bin/python3
"""City class."""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base

class City(Base):
    """City class.

    Attributes:
        id: city id, primary key.
        name: city name.
        state_id: foreign key to states.id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
