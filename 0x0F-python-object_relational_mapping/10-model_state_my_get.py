#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("Usage: ./script.py username password database_name state_name")

    username, password, database, state_name = sys.argv[1:5]

    connection_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    engine = create_engine(connection_str)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_query = session.query(State).filter(State.name == state_name).first()

    if state_query is None:
        print("Not found")
    else:
        print(state_query.id)
    session.close()
