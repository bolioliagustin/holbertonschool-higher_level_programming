#!/usr/bin/python3
"""Script that fetches all states from a database"""


from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

argv = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session = Session()
    for state in Session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    Session.close()
