#!/usr/bin/python3

"""
Script that lists all State objects that contain the letter a
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    connection_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection_str.format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
