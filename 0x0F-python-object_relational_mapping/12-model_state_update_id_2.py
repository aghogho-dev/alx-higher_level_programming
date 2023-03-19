#!/usr/bin/python3
"""A module called 11-model_state_insert"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_id2 = session.query(State).filter(State.id == 2).first()
    state_id2.name = "New Mexico"
    session.commit()
