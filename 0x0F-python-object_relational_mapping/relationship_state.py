#!/usr/bin/python3
""" A module to create a table in a database"""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sys import argv

Base = declarative_base()


class State(Base):
    """A class to create a table in the database"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    # relationship to city
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete, delete-orphan"
    )
