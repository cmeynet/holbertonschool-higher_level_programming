#!/usr/bin/python3
"""
Script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connecting to MySQL Database via SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Session creation
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State) \
        .filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
