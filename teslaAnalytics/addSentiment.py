import sqlite3
from textblob import TextBlob

def run_command(sqlCommand):
	connection = sqlite3.connect("myDB.db")
	cur = connection.cursor()
	cur.execute(sqlCommand)
	rows = cur.fetchall()
	return rows

#def update(sqlCommand):



if __name__ == '__main__':
	result = run_command("""SELECT id, body FROM comments""")
	connection = sqlite3.connect("myDB.db")
	cur = connection.cursor()
	i = 0
	for row in result:
		idVal = row[0]
		date = row[1]
		sqlCommand = """UPDATE comments SET polarity = '"""
		s = TextBlob(date)
		sqlCommand += str(s.polarity) + "' WHERE id = '" + idVal + "';"
		cur.execute(sqlCommand)
		sqlCommand = """UPDATE comments SET subjectivity = '"""
		sqlCommand += str(s.subjectivity) + "' WHERE id = '" + idVal + "';"
		cur.execute(sqlCommand)
		i += 1
		if i % 2000 == 0:
			print sqlCommand
			print("{}/1896000".format(i))
			connection.commit()
	connection.commit()

	connection.close()
