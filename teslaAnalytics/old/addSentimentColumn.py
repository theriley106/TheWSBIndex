# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import sqlite3
import json
connection = sqlite3.connect("myDB.db")


cursor = connection.cursor()
sql_command = """
ALTER TABLE comments ADD COLUMN polarity DECIMAL;"""


cursor.execute(sql_command)

sql_command = """
ALTER TABLE comments ADD COLUMN subjectivity DECIMAL;"""


cursor.execute(sql_command)
connection.commit()
connection.close()
