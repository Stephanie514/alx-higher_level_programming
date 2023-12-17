#!/usr/bin/python3
"""This displays all values in the states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("Usage: ./script.py username password database_name state_name")
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cursor = db.cursor()
    
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(state_name)
    cursor.execute(query)
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
