#!/usr/bin/python3
"""
This starts link class to table in database
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table states"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(id='%s', name='%s')>" % (self.id, self.name)


if __name__ == "__main__":
    from sqlalchemy import create_engine

    connection_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(connection_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)
