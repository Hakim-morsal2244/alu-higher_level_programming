#!/usr/bin/python3
import MySQLdb
import sys


def list_cities(mysql_username, mysql_password, database_name):
    """
    This function lists all cities from the hbtn_0e_4_usa database
    in ascending order by cities.id.
    """

    db = MySQLdb.connect(
        host="localhost", 
        port=3306, 
        user=mysql_username, 
        passwd=mysql_password, 
        db=database_name
    )

    cursor = db.cursor()

    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_cities(mysql_username, mysql_password, database_name)


if __name__ == "__main__":
    main()
