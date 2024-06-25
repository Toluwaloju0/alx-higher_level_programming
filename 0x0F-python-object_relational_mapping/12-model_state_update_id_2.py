#!/usr/bin/python3
""" A module to select everting in a database using sqlalchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.orm.exc import NoResultFound
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).\
        filter(State.id == 2).one()

    state.name = 'New Mexico'
    session.commit()
    session.close()
