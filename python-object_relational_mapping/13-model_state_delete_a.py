#!/usr/bin/python3
"""Delete states with the letter 'a' in their name"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Connect to MySQL and delete states with 'a' in the name"""
    # Create engine and bind to Base
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch and print all states before deletion for debugging
    all_states_before = session.query(State).all()
    print("Before deletion:")
    for state in all_states_before:
        print(f"{state.id}: {state.name}")

    # Query and delete all states with 'a' in their name using LIKE
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')
            ).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Fetch and print all states after deletion for debugging
    all_states_after = session.query(State).all()
    print("After deletion:")
    for state in all_states_after:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
