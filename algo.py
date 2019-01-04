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
	strategy = {'trades': {}, 'delay': 3, "description": description}
	for date, ratio in tradeClass.ratio_by_date.iteritems():
		diffVal = (ratio - tradeClass.average_ratio)
		if abs(diffVal / tradeClass.average_ratio) * 100 < 25:
			strategy['trades'][date] = {"trade": None}
		else:
			if diffVal > 0:
				strategy['trades'][date] = {"trade": "long"}
			else:
				#strategy['trades'][date] = {"trade": "long"}
				strategy['trades'][date] = {"trade": "short"}
	return strategy

def strategy3(tradeClass):
	description = """Trading based off of changes in ticker mention frequency"""
	strategy = {'trades': {}, 'delay': 3, "description": description}
	for date, ratio in tradeClass.ratio_by_date.iteritems():
		diffVal = (ratio - tradeClass.average_ratio)
		if abs(diffVal / tradeClass.average_ratio) * 100 < 25:
			strategy['trades'][date] = {"trade": None}
		else:
			strategy['trades'][date] = {"trade": "short"}
	return strategy

def strategy5(tradeClass):
	description = """Trading based off of changes in ticker mention frequency"""
	strategy = {'trades': {}, 'delay': 3, "description": description}
	for date, ratio in tradeClass.ratio_by_date.iteritems():
		diffVal = (ratio - tradeClass.average_ratio)
		if abs(diffVal / tradeClass.average_ratio) * 100 < 25:
			strategy['trades'][date] = {"trade": None}
		else:
			strategy['trades'][date] = {"trade": "long"}
	return strategy

def strategy6(tradeClass):
	description = """Trading based off of changes in ticker mention frequency"""
	strategy = {'trades': {}, 'delay': 3, "description": description}
	for date, ratio in tradeClass.ratio_by_date.iteritems():
		diffVal = (ratio - tradeClass.average_ratio)
		if abs(diffVal / tradeClass.average_ratio) * 100 < 25:
			strategy['trades'][date] = {"trade": "long"}
		else:
			strategy['trades'][date] = {"trade": None}
	return strategy

def strategy7(tradeClass):
	description = """Trading based off of changes in ticker mention frequency"""
	strategy = {'trades': {}, 'delay': 3, "description": description}
	for date, ratio in tradeClass.ratio_by_date.iteritems():
		diffVal = (ratio - tradeClass.average_ratio)
		if abs(diffVal / tradeClass.average_ratio) * 100 < 25:
			strategy['trades'][date] = {"trade": "short"}
		else:
			strategy['trades'][date] = {"trade": None}
	return strategy

def strategy4(tradeClass):
	description = """Trading based off of changes in ticker mention frequency"""
	strategy = {'trades': {}, 'delay': 3, "description": description}
	prevTrade = None
	for date, ratio in tradeClass.ratio_by_date.iteritems():
		diffVal = (ratio - tradeClass.average_ratio)
		if abs(diffVal / tradeClass.average_ratio) * 100 < 25:
			strategy['trades'][date] = {"trade": prevTrade}
		else:
			if diffVal > 0:
				prevTrade = "long"
				strategy['trades'][date] = {"trade": "long"}
			else:
				prevTrade = "short"
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
	infoz = {'buyAndHold': 0}
	for stock in main.STOCK_TICKERS:
		try:
			if main.get_total_count_by_ticker(stock) > 1000:
				a = main.Trade(stock)
				startAmount = 1000000
				buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
				strat1 = a.test_strategy(strategy1, startAmount)-startAmount
				strat3 = a.test_strategy(strategy3, startAmount)-startAmount
				strat4 = a.test_strategy(strategy4, startAmount)-startAmount
				strat5 = a.test_strategy(strategy5, startAmount)-startAmount
				strat6 = a.test_strategy(strategy6, startAmount)-startAmount
				strat7 = a.test_strategy(strategy7, startAmount)-startAmount
				print("{} | Returns from buy and hold: ${:,.2f}".format(stock, buyAndHold))
				print("{} | Returns from Strategy 1: ${:,.2f}".format(stock, strat1))
				print("{} | Returns from Strategy 3: ${:,.2f}".format(stock, strat3))
				print("{} | Returns from Strategy 4: ${:,.2f}".format(stock, strat4))
				print("{} | Returns from Strategy 5: ${:,.2f}".format(stock, strat5))
				print("{} | Returns from Strategy 6: ${:,.2f}".format(stock, strat6))
				print("{} | Returns from Strategy 7: ${:,.2f}".format(stock, strat7))
				info = []
				info.append({'name': 'strat1','count': strat1})
				info.append({'name': 'strat3','count': strat3})
				info.append({'name': 'strat4','count': strat4})
				info.append({'name': 'strat5','count': strat5})
				info.append({'name': 'strat6','count': strat6})
				info.append({'name': 'strat7','count': strat7})
				info.append({'name':'buyAndHold', 'count': buyAndHold})
				if max([strat1, strat3, strat4, strat5, strat6, strat7]) > buyAndHold:
					print("WINNER")
				print("\n")
				newlist = sorted(info, key=lambda k: k['count'])
				name = newlist[-1]['name']
				if name not in infoz:
					infoz[name] = 0
				infoz[name] += 1
				print infoz

		except Exception as exp:
			#print exp
			pass
	print info
