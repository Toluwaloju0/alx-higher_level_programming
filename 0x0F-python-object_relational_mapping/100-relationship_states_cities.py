#!/usr/bin/python3
"""A module to link two tables toghether"""

from sys import argv
from relationship_model_state import State, Base
from relationship_model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"\
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Claifornia")
    print(new_state)
    print('------------')
    new_state.cities = [City(name="San Francisco")]

    session.add(new_state)
    session.commit()
    session.close()
