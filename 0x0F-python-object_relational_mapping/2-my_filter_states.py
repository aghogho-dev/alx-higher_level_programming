#!/usr/bin/python3
"""A module called 2-my_filter_states"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cur = db.cursor()
    query = f"SELECT * FROM `states` WHERE `name` = '{argv[4]}';"
    cur.execute(query)
    list(map(print, sorted(cur.fetchall(), key=lambda x: x[0])))
    cur.close()
    db.close()
