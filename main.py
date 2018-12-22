import csv


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
	print len(csvFile)
	return csvFile

class Algo(object):
	"""docstring for Algo"""
	def __init__(self):
		self.dataset = read_dataset()
		# This gets the current dataset


if __name__ == '__main__':
	a = Algo()
