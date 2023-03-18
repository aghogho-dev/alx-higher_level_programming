#!/usr/bin/python3
import MySQLdb
from sys import argv

def func():
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    list(map(print, cur.fetchall()))

if __name__ == "__main__":
    func()
