# -*- coding: utf-8 -*-

import re
import json
import csv

def get_all_possible_tickers(fileName="companylist.csv"):
	with open(fileName, 'rb') as f:
		reader = csv.reader(f)
		your_list = list(reader)
	return [x[0] for x in your_list[1:]]

STOCK_TICKERS = get_all_possible_tickers()

def extract_tickers(string):
	e = re.findall('[A-Z]{1,4}|\d{1,3}(?=\.)|\d{4,}', string)
	return list(set(e).intersection(set(STOCK_TICKERS)))


if __name__ == '__main__':
	messageVal = '''AMD up AH is not very cash money'''
	print extract_tickers(messageVal)
