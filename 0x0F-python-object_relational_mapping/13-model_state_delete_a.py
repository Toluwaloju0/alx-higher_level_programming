#!/usr/bin/python3
""" A moduole to delete a column in a table"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}/\
@localhost:3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).filter(State.name.like('%a%'))
    row_to_del = rows.all()
    for row in row_to_del:
        print(row.name)
        session.delete(row)
    session.commit()
    session.close()
