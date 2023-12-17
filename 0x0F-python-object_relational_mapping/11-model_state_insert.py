#!/usr/bin/python3
""" prints the State object with the name passed as argument
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)

    session.close()
