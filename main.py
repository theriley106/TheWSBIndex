import csv


def read_dataset(filename="vixcurrent.csv"):
	# Reads the dataset with historical prices
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		return list(reader)
