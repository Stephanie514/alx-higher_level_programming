#!/usr/bin/python3
""" This deletes all State objects with a name containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.ilike('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
