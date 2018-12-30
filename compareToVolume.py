import json
import main

if __name__ == '__main__':
	a = json.load(open("dataset/AllCounts.json"))
	myVals = {}
	for key, val in a.iteritems():
		totalVolume = main.get_average_volume_by_ticker(key)
		if key != 0 and val != 0:
			ratio = float(totalVolume) / float(val)
		else:
			ratio = 0
		myVals[key] = ratio
		print("{} - {}".format(key, ratio))
	with open('volumeCommentRatio.json', 'w') as fout:
		json.dump(myVals, fout)
