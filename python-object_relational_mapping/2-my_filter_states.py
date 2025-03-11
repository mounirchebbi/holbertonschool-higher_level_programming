#!/usr/bin/python3
"""Module to use Mysqldb"""
import MySQLdb
import sys


def List_Filtered_states(username, password, db_name, state_name):
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
    request = f"SELECT * FROM states \
                WHERE states.name = \'{state_name}\' ORDER BY id ASC;"
    cursor.execute(request)
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
    List_Filtered_states(username, password, db_name, state_name)
