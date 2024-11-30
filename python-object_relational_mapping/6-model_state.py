#!/usr/bin/python3
"""Start link"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    """Connection"""
    try:
        # Create the engine and connect to the MySQL database
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True
        )

        # Create all tables if they don't exist
        Base.metadata.create_all(engine)
        print("Tables created successfully.")

    except Exception as e:
        print(f"Error: {e}")
