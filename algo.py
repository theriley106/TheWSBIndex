import main
import json
import traceback

INVERSE = True
DAY_DELAY = 14

def by_word_count():
	c = open("comments.txt").read().split("\n")
	a = MultiThread(c, calc_words)
	g = a.run_all()
	print g

def by_word_countz():
	a = DatasetProcess(calc_words, saveAs="myFile.json")
	a.run()

if __name__ == '__main__':
	g = json.load(open("dataset/AllCounts.json"))
	h = []
	a = json.load(open('sentimentByTicker.json'))
	for key, val in g.iteritems():
		h.append({'count': val, 'ticker': key})
	newlist = sorted(h, key=lambda k: k['count'])
	i = 0
	for tickerVal in newlist[::-1]:
		tickerVal = tickerVal['ticker']
		try:
			b = main.get_diff_from_ticker(tickerVal)
			g = main.get_percent_diff_from_ticker(tickerVal)
			start_amount = 1000000
			total = 0
			success = 0
			incorrect = 0
			h = json.load(open("dataset/ListOfDatesOrder.json"))
			directions = main.calc_predicted_direction(tickerVal)
			for val in h:
				if val not in b:
					h.remove(val)
			for i in range(DAY_DELAY,len(h)):
				prevKey = h[i-DAY_DELAY]
				key = h[i]
				if key in b:
					if directions[prevKey] != 0:
						#raw_input(g[key])
						if INVERSE:
							if directions[prevKey] > 0:
								start_amount += (start_amount * ((-1*g[key])*.01))
							else:
								start_amount += (start_amount * (g[key]*.01))
						else:
							if directions[prevKey] < 0:
							start_amount += (start_amount * ((-1*g[key])*.01))
						else:
							start_amount += (start_amount * (g[key]*.01))
			"""print("Correct: {}".format(success))
						print("Incorrect: {}".format(incorrect))
						print("Total: {}".format(total))"""
			if start_amount - 1000000 > 0:
				print("{} - +{}".format(tickerVal, start_amount - 1000000))
			else:
				print("{} - {}".format(tickerVal, (start_amount - 1000000)))
		except Exception as exp:
			#traceback.print_exc()
			pass
