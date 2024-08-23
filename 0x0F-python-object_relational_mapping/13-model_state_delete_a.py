#!/usr/bin/python3
""" A moduole to delete a column in a table"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/\
{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(bind=engine)

    row_to_del = session.query(State).filter(State.name.like('%a%')).all()
    for row in row_to_del:
        session.delete(row)
    session.commit()
    session.close()
