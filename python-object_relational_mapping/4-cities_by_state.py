#!/usr/bin/python3
"""
This script lists all cities from the hbtn_0e_4_usa database, 
with the cities sorted in ascending order by cities.id.
The cities are displayed with the state name for each city.
"""

import MySQLdb
import sys

def list_cities():
    """Connect to the MySQL database and list all cities from the database."""
    if len(sys.argv) != 4:
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Execute the query to list cities with their state names
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_cities()
