#!/usr/bin/python3
"""Script that display the State object that contains
the the letter 'a' from the database hbtn_0e_6_usa"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


argv = sys.argv
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
for state in session.query(State).filter(State.name.like('%a%')):
    print("{}: {}".format(state.id, state.name))
session.close()
