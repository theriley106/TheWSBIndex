import sqlite3
import main

def run_command(sqlCommand):
	connection = sqlite3.connect("myDB.db")
	cur = connection.cursor()
	cur.execute(sqlCommand)
	rows = cur.fetchall()
	return rows

#def update(sqlCommand):


#"""SELECT tickers FROM comments WHERE tickers not NULL"""



if __name__ == '__main__':
	result = run_command("""SELECT tickers FROM comments WHERE tickers not NULL""")
	print len(result)
	#for row in result:
	#	print row
