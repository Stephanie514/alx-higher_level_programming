#!/usr/bin/python3

"""Lists all State objects and corresponding City objects contained in the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def create_engine_session(username, password, database_name):
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}"
    engine = create_engine(conn_str)
    Session = sessionmaker(bind=engine)
    return Session()


def display_states_cities(session):
    query_result = session.query(State).order_by(State.id).all()
    for state in query_result:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")


def main():
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    session = create_engine_session(username, password, database_name)
    Base.metadata.create_all(session.get_bind())
    display_states_cities(session)
    session.close()


if __name__ == "__main__":
    main()
