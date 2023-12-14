#!/usr/bin/python3

import MySQLdb
import sys


db = MySQLdb.connect(host=localhost, port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
states = cur.execute("SELECT * FROM states ORDERED BY states.id ASC")
i = 1
for state in states:
    print(f"({i}, '{state.name}')")

cursor.close()
db.close()
