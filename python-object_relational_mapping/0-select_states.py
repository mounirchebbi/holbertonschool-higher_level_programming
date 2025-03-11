#!/usr/bin/python3
"""Module to use Mysqldb"""
import MySQLdb
import sys


def List_states(username, password, db_name):
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    response = cursor.fetchall()

    # printing response
    for row in response:
        print(row)

    # closing connexions
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    List_states(username, password, db_name)
