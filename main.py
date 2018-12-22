import csv
COLUMNS = ['open', 'high', 'low', 'close']

def read_csv(filename):
	# Reads the dataset with historical prices
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		return list(reader)

def read_dataset(filename="vixcurrent.csv"):
	csvFile = read_csv(filename)
	# This is the csv file containing historical prices
	csvFile = csvFile[2:]
	# Removes the header columns
	return csvFile

class Algo(object):
	"""docstring for Algo"""
	def __init__(self):
		self.days = []
		# These are the days in the dataset
		self.dataset = {}
		# These are the values of the dataset
		for row in read_dataset():
			# This gets the current dataset
			day = row[0]
			# This is the day value
			self.dataset[day] = {}
			# This contains the information from each column
			for i, columnVal in enumerate(COLUMNS):
				# Iterates over each column
				self.dataset[day][columnVal] = row[i+1]
				# Assigns each value to the info dict
		print self.dataset



if __name__ == '__main__':
	a = Algo()
