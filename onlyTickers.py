import glob
import json
import os


def append_json_to_file(dataVal, fileName):
	if os.path.exists(fileName) == False:
		writeVal = 'w'
	else:
		writeVal = 'a'
	with open(fileName, writeVal) as myfile:
		myfile.write(json.dumps(dataVal))


if __name__ == '__main__':
	for va in glob.glob("*.json"):
		with open(va) as f:
			for i, line in enumerate(f):
				val = json.loads(line)
				if len(val['tickers']) > 0:
					append_json_to_file(val, "onlyTickers.json")
		print('done with {}'.format(va))
