#!/usr/bin/python3
"""A script to query a database"""

from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/\
{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(bind=engine)

    result = session.query(City).order_by(City.id).all()
    for city in result:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()
