# -*- coding: utf-8 -*-

import re
import json
import csv
import threading
import os

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
			if i % 200000 == 0:
				fileName = "{}.json".format(i)
				print fileName
			val = json.loads(line)
			if val['body'] != '[deleted]':
				val['tickers'] = extract_tickers(val['body'])
				if len(val['tickers']) > 0:
					append_json_to_file(val, fileName)
	for key, value in count.iteritems():
		print("{} - {}".format(key, value))
	append_json_to_file(count, 'AllCounts.json')

def append_json_to_file(dataVal, fileName):
	if os.path.exists(fileName) == False:
		writeVal = 'w'
	else:
		writeVal = 'a'
	with open(fileName, writeVal) as myfile:
		myfile.write(json.dumps(dataVal) + "\n")


if __name__ == '__main__':
	#messageVal = '''AMD up AH is not very cash money'''
	#print extract_tickers(messageVal)
	read_forumn_data()
