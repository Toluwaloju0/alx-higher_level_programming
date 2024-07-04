#!/usr/bin/python3
""" A module to create a cities table"""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
