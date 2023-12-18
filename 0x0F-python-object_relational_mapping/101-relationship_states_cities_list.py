#!/usr/bin/python3

""" Lists all State objects and corresponding City objects contained in the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    INPUT = sys.argv
    if len(INPUT) < 4:
        exit(1)

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(INPUT[1], INPUT[2], INPUT[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    my_query = session.query(State).order_by(State.id).all()
    for state, *_ in my_query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
