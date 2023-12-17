#!/usr/bin/python3
"""This lists all states with a name starting with 'N' (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=mysql_user,
                         passwd=mysql_password, db=mysql_db, port=3306)
    cursor = db.cursor()
    
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)
    
    result_rows = cursor.fetchall()
    for row in result_rows:
        print(row)
    
    cursor.close()
    db.close()
