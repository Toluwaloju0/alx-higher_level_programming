#!/usr/bin/python3
""" A module to print objects in a cities table"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ =='__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    mapper_registry = registry()
    mapper_registry.configure()

    Session = sessionmaker(bind=engine)
    session = Session()
    
    result = session.query(State, City).join(City, City.state_id==State.id).all()
    for State, City in result:
        print("{}: ({}) {}".format(State.name, City.id, City.name))
