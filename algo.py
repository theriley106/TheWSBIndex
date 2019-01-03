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

def strategy0(tradeClass):
	description = """Buying and holding the stock"""
	strategy = {'trades': {}, 'delay': 0, "description": description}
	for date, ratio in tradeClass.ratio_by_date.iteritems():
		strategy['trades'][date] = {"trade": "long"}
	return strategy

def strategy1(tradeClass):
	description = """Trading based off of changes in ticker mention frequency"""
	strategy = {'trades': {}, 'delay': 0, "description": description}
	for date, ratio in tradeClass.ratio_by_date.iteritems():
		diffVal = (ratio - tradeClass.average_ratio)
		if abs(diffVal / tradeClass.average_ratio) * 100 < 25:
			strategy['trades'][date] = {"trade": None}
		else:
			if diffVal > 0:
				strategy['trades'][date] = {"trade": "long"}
			else:
				strategy['trades'][date] = {"trade": "short"}
	return strategy

def strategy2(tradeClass):
	dayDelay = 14
	for i in range(dayDelay, len(tradeClass.modified_dates)):
		indicatorDay = tradeClass.modified_dates[i-dayDelay]
		tradeDay = tradeClass.modified_dates[i]
		if indicatorDay in tradeClass.historical_data:
			pass


if __name__ == '__main__':
	a = main.Trade("TSLA")
	startAmount = 1000000
	buyAndHold = a.calc_buy_and_hold(startAmount)
	strat1 = a.test_strategy(strategy1, startAmount)
	print("Returns from buy and hold: ${:,.2f}".format(buyAndHold-startAmount))
	print("Returns from Strategy 1: ${:,.2f}".format(strat1-startAmount))
