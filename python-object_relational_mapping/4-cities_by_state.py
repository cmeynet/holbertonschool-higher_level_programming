#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC"
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
