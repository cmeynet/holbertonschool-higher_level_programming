#!/usr/bin/python3
"""
Script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa.
"""

import sys
from model_state import Base, State
from model_city import City
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

    cities = session.query(City).join(State) \
        .order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    main()
