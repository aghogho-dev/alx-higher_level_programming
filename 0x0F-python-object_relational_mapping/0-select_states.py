#!/usr/bin/python3
# Get all states from db
# Usage: ./0-select-states.py <mysql username> \
#                             <mysql passwd> \
#                             <db name>
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    list(map(print, cur.fetchall()))
    cur.close()
    db.close()
