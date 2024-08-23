#!/usr/bin/python3
""" A module to print objects in a cities table"""

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/\
{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    result = session.query(State, City).filter(State.id == City.state_id).all()
    for S, C in result:
        print("{}: ({}) {}".format(S.name, C.id, C.name))
