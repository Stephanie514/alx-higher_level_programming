#!/usr/bin/python3
""" Script that changes the name of a State object from the database
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
    Session = sessionmaker(bind=engine)

    session = Session()

    state_id_to_change = 2
    new_name = 'New Mexico'

    state_to_change = session.query(State).filter_by(id=state_id_to_change).first()

    if state_to_change:
        state_to_change.name = new_name
        session.commit()
    else:
        print("State with ID 2 not found")

    session.close()
