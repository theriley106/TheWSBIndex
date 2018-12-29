# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import sqlite3
import json

connection = sqlite3.connect("myDB.db")

cursor = connection.cursor()
sql_command = """
CREATE TABLE comments (
body TEXT,
score_hidden BOOLEAN,
archived BOOLEAN,
name TEXT,
author TEXT,
downs INT,
created_utc TEXT,
subreddit_id TEXT,
link_id TEXT,
parent_id TEXT,
score INT,
retrieved_on TEXT,
gilded INT,
id TEXT PRIMARY KEY,
subreddit TEXT,
ups INT,
controversiality INT
);"""


cursor.execute(sql_command)
def gen_command(jsonVal):
	sql_command = """INSERT INTO comments ("""
	vals = [u'body', u'score_hidden', u'archived', u'name', u'author', u'downs', u'created_utc', u'subreddit_id', u'link_id', u'parent_id', u'score', u'retrieved_on', u'gilded', u'id', u'subreddit', u'ups', u'controversiality']
	for val in vals:
		sql_command += val + ","
	sql_command = sql_command[:-1] + ") VALUES ("
	for val in vals:
		try:
			gVal = str(jsonVal[val]).replace("'", "").replace('"', '')
			if gVal == "True":
				gVal = str(1)
			elif gVal == "False":
				gVal = str(0)
			sql_command += '"' + gVal + '", '
		except:
			sql_command += "NULL, "

	sql_command = sql_command[:-2]
	sql_command += ");"
	return sql_command
i = 0
with open("/media/christopher/ssd/wsbData.json") as f:
	for line in f:
		g = json.loads(line)
		sql_command = gen_command(g)
		#print sql_command
		try:
			cursor.execute(sql_command)
		except Exception as exp:
			print exp
		i += 1
		if i % 2000 == 0:
			print(i)
			# never forget this, if you want the changes to be saved:
			connection.commit()




connection.commit()


connection.close()
