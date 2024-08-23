#!/usr/bin/python3
""" A module to print all the states and ...
their corresponding cities in a database"""


from relationship_model_state import State, Base
from relationship_model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/\
{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(bind=engine)

    result = session.query(State).order_by(State.id).all()

    for state in result:
        print(state.id, ":", state.name)
        for city in state.cities:
            print("\t", city.id, ":", city.name)

    session.close()
