#!/usr/bin/python3
''' print the first state object from the database '''
from model_state import Base, State
from sqlalchemy import (create_engine)
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}.{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instances = session.query(State).filter(State.name.like('%a%'))
    for instance in instances:
        print(instance.id, instance.name, sep=': ')
