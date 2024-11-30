#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py mysql_username "
              "mysql_password database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and check how many states have 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    print(f"Found {len(states_to_delete)} states with 'a' in their name.")

    # Delete matching records
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()
    print(f"Deleted {len(states_to_delete)} states.")

    # Check if there are any remaining states with 'a' in their name
    remaining_states = session.query(State).filter(
        State.name.like('%a%')
    ).all()
    print(f"Remaining states with 'a' in their name: "
          f"{len(remaining_states)}")

    session.close()
