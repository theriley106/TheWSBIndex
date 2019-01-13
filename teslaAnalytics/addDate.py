import sqlite3
import dateparser as dp

def convert_date(dateVal):
	# Converts to format 2004-01-05
	dt = dp.parse(dateVal)
	return dt.date()

def run_command(sqlCommand):
	connection = sqlite3.connect("myDB.db")
	cur = connection.cursor()
	cur.execute(sqlCommand)
	rows = cur.fetchall()
	return rows

#def update(sqlCommand):


if __name__ == '__main__':
	result = run_command("""SELECT id, created_utc FROM comments""")
	connection = sqlite3.connect("myDB.db")
	cur = connection.cursor()
	i = 0
	for row in result:
		idVal = row[0]
		date = row[1]
		sqlCommand = """UPDATE comments SET dateVal = '"""
		a = str(convert_date(date))
		sqlCommand += a + "' WHERE id = '" + idVal + "';"
		cur.execute(sqlCommand)
		i += 1
		if i % 2000 == 0:
			print a
			print(i)
			connection.commit()
	connection.commit()

	connection.close()
