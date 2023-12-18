#!/usr/bin/python3

""" Lists all State objects and corresponding City objects
contained in the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    db_username, db_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    connection_string = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(connection_string.format(db_username, db_password, db_name))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    with Session() as session:
        query_result = session.query(State, City) \
                              .filter(State.id == City.state_id) \
                              .order_by(State.id, City.id) \
                              .all()

        for state, city in query_result:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))
