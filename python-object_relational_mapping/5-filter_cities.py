#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s\
        ORDER BY cities.id ASC", (state_name,)
    )

    rows = cursor.fetchall()
    city_names = []
    for row in rows:
        city_names.append(row[0])
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
