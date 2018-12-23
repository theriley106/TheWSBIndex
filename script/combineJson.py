import os
import sys
import json

if __name__ == '__main__':
	filenames = sys.argv[1:]
	saveAs = filenames.pop(-1)
	writeAs = 'w'
	for filename in filenames:
		with open(filename) as f:
			with open(saveAs, writeAs) as s:
				for line in f:
					s.write(json.dumps(line) + "\n")
		writeAs = 'a'
