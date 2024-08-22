#!/usr/bin/python3
""" A module to select everting in a database using sqlalchemy"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(bind=engine)

    result = session.query(State).order_by(State.id).\
        filter(State.name == argv[4]).one_or_none()

    if result is None:
        print("Not found")
    else:
        print(result.id)
    session.close()
