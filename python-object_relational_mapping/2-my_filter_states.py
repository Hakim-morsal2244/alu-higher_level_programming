#!/usr/bin/python3
import MySQLdb
import sys

def filter_states():
    """Connect to the MySQL database and fetch states based on user input."""
    # Check if the right number of arguments is passed
    if len(sys.argv) != 5:
        return
    
    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", user=mysql_user, passwd=mysql_password, db=mysql_db)
    cursor = db.cursor()

    # Use format() to safely insert the state name into the SQL query
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch and display the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states()
