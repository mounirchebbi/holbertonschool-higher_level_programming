#!/usr/bin/python3
"""Module to filter cities by state name"""
import MySQLdb
import sys


def filter_cities(username, password, db_name, state_name):
    """connect to db to retrives recors from states table"""

    # connection to db
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
    )

    # using cursor to fetch response
    cursor = db.cursor()

    # using %s placeholder and passing parameter separately
    request = (
        "SELECT c.name "
        "FROM cities c JOIN states s "
        "ON c.state_id = s.id "
        "WHERE s.name = %s "
        "ORDER BY c.id ASC;"
    )
    # parameter is tuple because mysql excpects iterable
    cursor.execute(request, (state_name,))
    response = cursor.fetchall()

    # printing response
    output = ", ".join(row[0] for row in response)
    print(output)

    # closing connexions
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} \
                <username> <password> <database> <state name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    filter_cities(username, password, db_name, state_name)
