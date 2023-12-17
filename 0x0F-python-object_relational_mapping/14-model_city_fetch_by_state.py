#!/usr/bin/python3
""" model_city.py that contains the class definition of a City
"""

import sys
from model_state import Base, State
from model_city import City
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

    city_states = (session.query(State.name, City.id, City.name)
                   .filter(State.id == City.state_id)
                   .order_by(City.id).all())

    for state_name, city_id, city_name in city_states:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
