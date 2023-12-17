#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
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
    
    query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        INNER JOIN states 
        ON states.id=cities.state_id
        ORDER BY cities.id ASC
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
