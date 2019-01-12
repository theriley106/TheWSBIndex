import json
import main
import saveScreenshot


if __name__ == '__main__':
	ticker = raw_input("Ticker: ").upper()
	a = main.Trade(ticker)
	startAmount = 1000000
	stockMentionRanking = main.calc_stock_ranking(ticker) + 1
	totalCount = main.get_total_count_by_ticker(ticker)
	sentiment = main.get_sentiment_by_ticker(ticker)
	mentionsByDay = main.get_weekday_by_ticker(ticker)
	stockFirstMentioned = main.get_first_comment_with_ticker(ticker)
	buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
	strat1 = a.test_strategy(strategy1, startAmount)-startAmount
	strat1Total = a.totalTrades
	strat3 = a.test_strategy(strategy3, startAmount)-startAmount
	strat3Total = a.totalTrades
	strat4 = a.test_strategy(strategy4, startAmount)-startAmount
	strat4Total = a.totalTrades
	strat5 = a.test_strategy(strategy5, startAmount)-startAmount
	strat5Total = a.totalTrades
	strat6 = a.test_strategy(strategy6, startAmount)-startAmount
	strat6Total = a.totalTrades
	strat7 = a.test_strategy(strategy7, startAmount)-startAmount
	strat7Total = a.totalTrades

	'''for key, value in main.calc_predicted_direction("MU").iteritems():
		print("{} {}".format(key, value))'''
