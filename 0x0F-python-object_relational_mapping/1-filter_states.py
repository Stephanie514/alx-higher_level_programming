#!/usr/bin/python3
"""Lists all states with a name starting with 'N' (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: ./script.py username password database_name")
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cursor = db.cursor()
    
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)
    
    the_rows = cursor.fetchall()
    for row in the_rows:
        print(row)
    
    cursor.close()
    db.close()
