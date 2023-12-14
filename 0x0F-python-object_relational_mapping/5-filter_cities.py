#!/usr/bin/python3
''' Search cities of a state in a database '''                
import MySQLdb
import sys

def filter_states(username, password, db_name, stte_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to get states starting with 'N'
    query = "SELECT cities.name FROM states INNER JOIN cities ON cities.state_id = (SELECT id FROM states WHERE states.name LIKE BINARY '{}')".format(stte_name)
    cursor.execute(query)

    # Fetch all the rows
    cities = cursor.fetchall()
    # Display results
    i = 1;
    for city in cities:
        if (i == len(cities)):
            print(city)
        else:
            print("{}, ".format(city), end="")
            i+=1

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:5]
    filter_states(username, password, db_name, state_name)

