import main

def by_word_count():
	c = open("comments.txt").read().split("\n")
	a = MultiThread(c, calc_words)
	g = a.run_all()
	print g

def by_word_countz():
	a = DatasetProcess(calc_words, saveAs="myFile.json")
	a.run()

if __name__ == '__main__':
	for tickerVal in main.STOCK_TICKERS:
		try:
			b = main.get_diff_from_ticker(tickerVal)
			g = main.get_percent_diff_from_ticker(tickerVal)
			start_amount = 1000000
			total = 0
			success = 0
			incorrect = 0
			for key, value in main.calc_predicted_direction(tickerVal).iteritems():
				if key in b and value != 0:
					if value < 0:
						start_amount += start_amount * (-1*g[key])
					else:
						start_amount += start_amount * g[key]
			"""print("Correct: {}".format(success))
						print("Incorrect: {}".format(incorrect))
						print("Total: {}".format(total))"""
			print("{} - {}".format(tickerVal, (start_amount/1000000.0)*100))
		except:
			pass
