#!/usr/bin/python3
""" A module to select everting in a database using sqlalchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).\
        filter(State.name.like('%a%')).all()

    for state in result:
        print("{}: {}".format(state.id, state.name))

    session.close()
