#!/usr/bin/python3
"""Module to list a state infos in safe mode"""
import MySQLdb
import sys


def list_Filtered_states(username, password, db_name, state_name):
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
        "SELECT * FROM states "
        "WHERE name = %s "
        "ORDER BY id ASC"
    )
    # parameter is tuple because mysql excpects iterable
    cursor.execute(request, (state_name,))
    response = cursor.fetchall()

    # printing response
    for row in response:
        print(row)

    # closing connexions
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} \
                <username> <password> <database> <state_name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    list_Filtered_states(username, password, db_name, state_name)
