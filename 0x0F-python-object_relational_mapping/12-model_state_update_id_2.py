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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_change = session.query(State).filter_by(id=2).first()

    if state_to_change:
        state_to_change.name = 'New Mexico'
        session.commit()
    else:
        print("Not found")

    session.close()
