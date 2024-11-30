#!/usr/bin/python3
"""
This script lists all states from the hbtn_0e_0_usa database
where the name matches the given argument.
It takes 4 arguments: MySQL username, MySQL password, database name, and state name to search.
The results are displayed in ascending order by states.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish the database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve states where name matches the input
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch and print all results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()
