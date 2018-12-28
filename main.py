import csv
import json
import re
import dateparser as dp
import threading
import random

COLUMNS = ['open', 'high', 'low', 'close']
IS_TICKER = re.compile("[A-Z]{1,4}|\d{1,3}(?=\.)|\d{4,}")
# This is a regex that determines if a string is a stock ticker

def get_all_possible_tickers(fileName="companylist.csv"):
	with open(fileName, 'rb') as f:
		reader = csv.reader(f)
		your_list = list(reader)
	return [x[0] for x in your_list[1:]]

STOCK_TICKERS = get_all_possible_tickers()
STOCK_TICKERS.remove("EDIT")

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

def isTicker(stringVal):
	if IS_TICKER.match(stringVal):
		return stringVal in set(STOCK_TICKERS)
	return False

def extract_buy_or_sell(string):
	info = {'puts': [], 'calls': [], 'buy': [], 'sell': []}
	# Extracts the words buy or sell from the comment
	for val in re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", string):
		# This splits the string into sentences
		allWords = re.findall("\w+", str(val))
		while len(allWords) > 0:
			word = allWords.pop(0)
			if re.match("[\W]?([Bb]uy)[\W]?", word):
				# This means it's the word buy
				tempList = []
				while len(allWords) > 0:
					newWord = allWords.pop(0)
					if isTicker(newWord):
						tempList.append(newWord)
					elif re.match("[\W]?([Pp]ut[s]?)[\W]?", newWord):
						if len(tempList) > 0:
							# This means a sentence like
							# put $5 in TSLA
							while len(tempList) > 0:
								info['puts'].append(tempList.pop())
							break

					elif re.match("[\W]?([Cc]all[s]?)[\W]?", newWord):
						if len(tempList) > 0:
							# This means a sentence like
							# call my friend to put $5 in TSLA
							while len(tempList) > 0:
								info['calls'].append(tempList.pop())
							break
				info['buy'] += tempList

			elif re.match("[\W]?[Ss]horting?[\W]?", word):
				while len(allWords) > 0:
					newWord = allWords.pop(0)
					if isTicker(newWord):
						info['sell'].append(newWord)
					else:
						break

			elif re.match("[\W]?([Ss]ell|[Ss]old|[Cc]los[(e|ing)]|[Ss]hort[s]?)[\W]?", word):
				# This means it's indicating they want to sell
				# Sell TSLA puts would be equivilant to a call
				tempList = []
				while len(allWords) > 0:
					newWord = allWords.pop(0)
					if isTicker(newWord):
						tempList.append(newWord)
					elif re.match("[\W]?([Pp]ut[s]?)[\W]?", newWord):
						if len(tempList) > 0:
							# This means a sentence like
							# put $5 in TSLA
							while len(tempList) > 0:
								info['calls'].append(tempList.pop())
							break

					elif re.match("[\W]?([Cc]all[s]?)[\W]?", newWord):
						if len(tempList) > 0:
							# This means a sentence like
							# call my friend to put $5 in TSLA
							while len(tempList) > 0:
								info['puts'].append(tempList.pop())
							break

					elif re.match("[Ss]hort[s]?", newWord):
						# IE closing out a short == buy
						if len(tempList) > 0:
							# This means a sentence like
							# call my friend to put $5 in TSLA
							while len(tempList) > 0:
								info['buy'].append(tempList.pop())
							break

				info['sell'] += tempList

			elif isTicker(word):
				tempList = [word]
				while len(allWords) > 0:
					newWord = allWords.pop(0)
					if isTicker(newWord):
						tempList.append(newWord)
					elif re.match("[\W]?([Pp]ut[s]?)[\W]?", newWord):
						if len(tempList) > 0:
							# This means a sentence like
							# put $5 in TSLA
							while len(tempList) > 0:
								info['puts'].append(tempList.pop())
							break

					elif re.match("[\W]?([Cc]all[s]?)[\W]?", newWord):
						if len(tempList) > 0:
							# This means a sentence like
							# call my friend to put $5 in TSLA
							while len(tempList) > 0:
								info['calls'].append(tempList.pop())
							break
				info['buy'] += tempList


		#e =
		#[Ss]ell
	#if len(e) > 1:
	# This means it was a relatively complex sentence.
	#for val in re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", string):
	#print val
	#e = re.findall('[A-Z]{1,4}|\d{1,3}(?=\.)|\d{4,}', string)
	#return list(set(e).intersection(set(STOCK_TICKERS)))
	return info

def random_string(stringVal):
	# Should return float or int
	return float(stringVal)

def calc_words(stringVal):
	return stringVal.count(" ")

class MultiThread(object):
	def __init__(self, listOfObjects, function, threads=20):
		self.lock = threading.Lock()
		self.threads = threads
		self.totalLength = len(listOfObjects)
		# This is the lock for multithreading
		self.objects = [{'id': x, 'val': e} for x, e in enumerate(listOfObjects)]
		self.functionVal = function
		self.totalRuns = 0
		self.totalCount = 0
		self.results = {}

	def run_single(self):
		while len(self.objects) > 0:
			self.lock.acquire()
			if len(self.objects) == 0:
				self.lock.release()
				break
			this_val = self.objects.pop()
			self.lock.release()
			returnVal = self.functionVal(this_val['val'])
			self.lock.acquire()
			self.totalRuns += 1
			self.totalCount += float(returnVal)
			self.lock.release()
			self.results[str(this_val['id'])] = returnVal
			self.toReturn = []

	def run_all(self):
		threads = [threading.Thread(target=self.run_single) for i in range(self.threads)]
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()
		self.average = (float(self.totalCount) / float(self.totalRuns))
		self.toReturn = [self.results[str(i)] for i in range(self.totalLength)]
		return self.toReturn

	def get_average(self):
		self.average = (float(self.totalCount) / float(self.totalRuns))
		return self.average

	def get_diff_from_average(self):
		self.average = (float(self.totalCount) / float(self.totalRuns))
		return [x - self.average for x in self.toReturn]

def run_on_all(listOfStrings, function):
	a = MultiThread(listOfStrings, function, 20)
	function()

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
	#a = Algo()
	#print a.calc_diff_from_date('1/5/2004', 7)
	#a.calc_for_all(a.calculate_day_diff)
	#print len(a.forumnData)
	#message = """you should buy TSLA.  Maybe even AMD if you feel like it."""
	#message = """buying TSLA calls and maybe AMD if I feel like it"""
	#message = """closing out my TSLA shorts"""
	#message = """short TSLA probably or put put AMD call"""
	#message = """dude i don't even know"""
	#e = re.compile("[\W]?([Bb]uy|[Ss]ell)[\W]?")
	#if e.match('bestbuy'):
	#	print("Found")
	'''for message in open("dataset/onlyComments.txt").read().split("\n"):

					if len(message) > 0:
						f =  extract_buy_or_sell(message)
						if len(message) < 100:
							totalCount = 0
							for key, val in f.iteritems():
								totalCount += len(val)
							if val > 0:
								print("{} | {}".format(message, f))'''
	#print isTicker("BARH")
	#newWord = "puts"
	#print re.match("[\W]?([Pp]ut[s]?)[\W]?", newWord)
	#listOfObjects = range(1,100)
	#objectVal = [{'id': x, 'val': e} for x, e in enumerate(listOfObjects)]
	#print objectVal
	c = open("comments.txt").read().split("\n")
	a = MultiThread(c, calc_words)
	g = a.run_all()
	print g
	print a.get_diff_from_average()
	#a = MultiThread([str(i) for i in range(0,101)], random_string)
	#b = a.run_all()
	#print a.get_diff_from_average()
	#print b
