# -*- coding: utf-8 -*-

import re
import json
import csv

def get_all_possible_tickers(fileName="companylist.csv"):
	with open(fileName, 'rb') as f:
		reader = csv.reader(f)
		your_list = list(reader)
	return [x[0] for x in your_list[1:]]

def convert_utc_to_date(utcTime):
	# This is currently not working properly
	return utcTime

STOCK_TICKERS = get_all_possible_tickers()

def extract_tickers(string):
	e = re.findall('[A-Z]{1,4}|\d{1,3}(?=\.)|\d{4,}', string)
	return list(set(e).intersection(set(STOCK_TICKERS)))

def read_forumn_data(filename="/media/christopher/ssd/wsbData.json"):
	# This is the data from wallstreet bets
	# It populates the forumnData
	count = {}
	with open(filename) as f:
		for i, line in enumerate(f):
			val = json.loads(line)
			if val['body'] != '[deleted]':
				for val in extract_tickers(val['body']):
					if val not in count:
						count[val] = 0
					count[val] += 1
			if i % 20000 == 0 and i != 0:
				break
	for key, value in count.iteritems():
		print("{} - {}".format(key, value))


if __name__ == '__main__':
	#messageVal = '''AMD up AH is not very cash money'''
	#print extract_tickers(messageVal)
	read_forumn_data()
