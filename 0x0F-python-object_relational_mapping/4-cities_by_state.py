#!/usr/bin/python3
""" list all cities with their states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

def filter_states(username, password, db_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to get states starting with 'N'
    query = "SELECT cities.id, cities.name, state.name FROM cities INNER JOIN states ON states.id=cities.state_id ORDERED by cities.id ASC"
    cursor.execute(query)

    # Fetch all the rows
    states = cursor.fetchall()4-cities_by_state.py

    # Display results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]
    filter_states(username, password, db_name)
