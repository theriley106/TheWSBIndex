# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import sqlite3
import json
connection = sqlite3.connect("myDB.db")


cursor = connection.cursor()
sql_command = """
ALTER TABLE comments ADD COLUMN dateVal TEXT;"""


cursor.execute(sql_command)
connection.commit()


connection.close()
