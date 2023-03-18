#!/usr/bin/python3
"""A module called 1-filter_states"""


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
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")
    list(map(print, cur.fetchall()))
    cur.close()
    db.close()