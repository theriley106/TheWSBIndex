import sqlite3

def run_command(sqlCommand):
	connection = sqlite3.connect("myDB.db")
	cur = connection.cursor()
	cur.execute(sqlCommand)
	rows = cur.fetchall()
	return rows




if __name__ == '__main__':
	result = run_command("""SELECT * FROM comments WHERE (body != "[deleted]")""")
	print len(result)
