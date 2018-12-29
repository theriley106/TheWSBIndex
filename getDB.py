import sqlite3
import json

connection = sqlite3.connect("myDB.db")
cur = connection.cursor()
cur.execute("SELECT * FROM comments")
rows = cur.fetchall()
print len(rows)
