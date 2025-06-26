#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def main():
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to get all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()


# Ensure the script is not executed when imported
if __name__ == "__main__":
    main()
