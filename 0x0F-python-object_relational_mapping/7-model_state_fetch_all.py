#!/usr/bin/python3

""" 
This script lists all State objects 
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
    Base.metadata.create_all(engine)
    
    session = Session()
    
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    session.close()
