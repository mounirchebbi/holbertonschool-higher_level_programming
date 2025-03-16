#!/usr/bin/python3
"""Script to list State objects containing 'a'"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing 'a'
    states = (
    session.query(State)
    .filter(State.name.like('%a%'))
    .order_by(State.id)
    .all()
    )

    # Display result
    for state in states:
        print(f"{state.id}: {state.name}")
    # Close the session
    session.close()
