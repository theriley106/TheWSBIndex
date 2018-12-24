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
		print va
		with open(va) as f:
			for i, line in enumerate(f):
				v = [x + "}" for x in line.split("}\n") if len(x) > 0]
				for l in v:
					try:
						val = json.loads(l)
						if len(val['tickers']) > 0:
							print val['tickers']
							append_json_to_file(val, "onlyTickers.json")
					except:
						pass
		print('done with {}'.format(va))
