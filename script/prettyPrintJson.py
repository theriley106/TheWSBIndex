import json
import sys
import os

if __name__ == '__main__':
	filename = sys.argv[1]
	try:
		os.system("cp {} {}".format(filename, filename.partition(".")[0] + "_backup.json"))
		a = json.load(open(filename))
		with open(filename, 'w') as f:
			f.write(json.dumps(a, indent=4))
		os.system("rm {}".format(filename.partition(".")[0] + "_backup.json"))
	except:
		try:
			os.system("cp {} {}".format(filename.partition(".")[0] + "_backup.json", filename))
		except:
			pass
		print("ERROR")
