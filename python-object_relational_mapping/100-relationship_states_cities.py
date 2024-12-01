#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco'
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Arguments: mysql username, mysql password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Database connection
    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost/{database}")
    Base.metadata.create_all(engine)

    # Session creation
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Add and commit objects to the database
    session.add(new_state)
    session.commit()
    session.close()
