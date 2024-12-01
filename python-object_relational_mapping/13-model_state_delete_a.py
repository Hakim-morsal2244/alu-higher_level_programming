#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database passed as an argument.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> <password> <database>")
        exit(1)

    # Create engine to connect to the MySQL database
    username, password, database = argv[1], argv[2], argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)

    # Bind the engine and create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states with names containing 'a' and delete them
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit changes to the database
    session.commit()

    # Close the session
    session.close()
