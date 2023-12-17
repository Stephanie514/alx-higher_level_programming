#!/usr/bin/python3
"""This lists all cities of a state in argument"""
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
    
    qry = """
        SELECT cities.name 
        FROM cities 
        INNER JOIN states 
        ON states.id=cities.state_id
        WHERE states.name=%s
        ORDER BY cities.id ASC
    """
    
    cursor.execute(qry, (state_name,))
    rows = cursor.fetchall()
    
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    
    cursor.close()
    db.close()
