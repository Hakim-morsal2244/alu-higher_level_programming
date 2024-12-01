#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Get command-line arguments
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    # Create a connection to the MySQL database
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{db_name}", pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new state and city
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add the objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to save the changes
    session.commit()

    # Close the session
    session.close()
