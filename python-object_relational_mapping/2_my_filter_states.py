#!/usr/bin/python3
"""
This script filters and displays all states in the states table where 
the state name matches the user input.

Usage:
    python3 2_my_filter_states.py mysql_username mysql_password 
    database_name state_name
"""
import MySQLdb
import sys

def filter_states():
    # Establish a connection to the database
    db = MySQLdb.connect(
        host="localhost", 
        user=sys.argv[1], 
        passwd=sys.argv[2], 
        db=sys.argv[3]
    )
    cursor = db.cursor()
    
    # Create and execute the query to find states by name
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    rows = cursor.fetchall()
    
    # Print the result
    for row in rows:
        print(row)
    
    # Close the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states()
