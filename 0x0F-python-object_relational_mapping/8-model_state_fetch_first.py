#!/usr/bin/python3
"""This prints the first State object from the database"""
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

    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
