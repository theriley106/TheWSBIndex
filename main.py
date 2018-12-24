import csv
import json
import re
import dateparser as dp

COLUMNS = ['open', 'high', 'low', 'close']
STOCK_TICKERS = get_all_possible_tickers()

def read_csv(filename):
	# Reads the dataset with historical prices
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		return list(reader)

def convert_date(dateVal):
	# Converts to format 2004-01-05
	dt = dp.parse(dateVal)
	return dt.date()

def extract_tickers(string):
	e = re.findall('[A-Z]{1,4}|\d{1,3}(?=\.)|\d{4,}', string)
	return list(set(e).intersection(set(STOCK_TICKERS)))

class Algo(object):
	"""docstring for Algo"""
	def __init__(self):
		self.days = []
		# These are the days in the dataset
		self.dataset = {}
		# These are the values of the dataset
		self.read_dataset()
		# Fills the dataset with info from the CSV
		#print self.dataset
		self.forumnData = {}
		# This contains the forumn dataset
		#self.read_forumn_data()
		# Reads the dataset



	def read_dataset(self, filename="vixcurrent.csv"):
		csvFile = read_csv(filename)
		# This is the csv file containing historical prices
		csvFile = csvFile[2:]
		# Removes the header columns
		for row in csvFile:
			# This gets the current dataset
			day = row[0]
			# This is the day value
			self.days.append(day)
			# Adds the day to the list of days
			self.dataset[day] = {}
			# This contains the information from each column
			for i, columnVal in enumerate(COLUMNS):
				# Iterates over each column
				self.dataset[day][columnVal] = float(row[i+1])
				# Assigns each value to the info dict

	def read_forumn_data(self, filename="/media/christopher/ssd/wsbData.json"):
		# This is the data from wallstreet bets
		# It populates the forumnData
		with open(filename) as f:
			for i, line in enumerate(f):
				val = json.loads(line)
				dayVal = convert_date(val['created_utc'])
				if dayVal not in self.forumnData:
					self.forumnData[dayVal] = []
				self.forumnData[dayVal].append(val)
				if i % 2000 == 0:
					print i

	def calc_diff_from_date(self, date, days):
		# Calculates the difference in values from a specified day onward
		# Ie: date=1/29/2004, days=7
		dayIndex = self.days.index(date)
		# This is the index of the inputted day
		info = {}
		for column in COLUMNS:
			# Goes over each column in the dataset
			currentVal = self.dataset[date][column]
			futureVal = self.dataset[self.days[dayIndex+days]][column]
			info[column] = currentVal - futureVal
		return info

	def calc_avg_from_date(self, date, days):
		# Calculates the average values from a specified day onward
		# Ie: date=1/29/2004, days=7
		dayIndex = self.days.index(date)
		# This is the index of the inputted day
		info = {}
		for column in COLUMNS:
			# Goes over each column in the dataset
			info[column] = []
		#print dayIndex
		for i in range(dayIndex, dayIndex+days):
			# Goes through each column in the dataset
			dayInfo = self.dataset[self.days[i]]
			# This is all the info for the current day
			for column in COLUMNS:
				# Goes over each column in the dataset
				info[column].append(dayInfo[column])
		for column in COLUMNS:
			# Goes through each column in the dataset
			info[column] = (sum(info[column]) / len(info[column]))
		return info

	def calculate_day_diff(self, date):
		# This calculates the daily change
		return (self.dataset[date]['close'] - self.dataset[date]['open'])

	def calc_for_all(self, functionVal):
		# This will run each day through a specific function
		returnVal = {}
		for val in self.days:
			# Iterates over each day
			 returnVal[val] = functionVal(val)
		return returnVal

	#def calc_forumn_frequency(self):





if __name__ == '__main__':
	a = Algo()
	#print a.calc_diff_from_date('1/5/2004', 7)
	#a.calc_for_all(a.calculate_day_diff)
	print len(a.forumnData)
