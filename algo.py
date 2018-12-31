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
	tickerVal = raw_input("Ticker: ").upper()
	b = main.get_diff_from_ticker(tickerVal)
	total = 0
	success = 0
	incorrect = 0
	for key, value in main.calc_predicted_direction(tickerVal).iteritems():
		if key in b and value != 0:
			total += 1
			if value < 0:
				if b[key] < 0:
					success += 1
				else:
					incorrect += 1
			else:
				if b[key] > 0:
					success += 1
				else:
					incorrect += 1
	print("Correct: {}".format(success))
	print("Incorrect: {}".format(incorrect))
	print("Total: {}".format(total))

