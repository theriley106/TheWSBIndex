import json
import main
import algo
import saveScreenshots


if __name__ == '__main__':
	message = """

# {0} Analysis

<p style="font-size:14px;"">
  Stock Ticker: <b>{1}</b></p>

<p style="font-size:14px;"">
  Total Comments Mentioning Ticker: <b>{2}</b></p>

<p style="font-size:14px;"">
  Average Sentiment Towards Ticker: <b>{3}</b></p>

<p style="font-size:14px;"">
  Stock Mention Ranking (SMR): <b>{4}</b></p>

  <p style="font-size:14px;"">
  Ticker First Mentioned on WSB: <b>{5} Days Ago</b></p>



<p align="center">
<img src ="static/totalByDay_{1}.png">
</p>


## {0} Strategy Specific Returns (Starting w/ $1,000,000)

### Overview
{6}

### Return by Strategy

<b>Note: Trades based on WallStreetBets comments are in BLUE, trades based on holding long-term are in RED</b>

<p align="center">
<img src ="static/strat1_{1}.png">
</p>

<p align="center">
<img src ="static/strat4_{1}.png">
</p>

<p align="center">
<img src ="static/strat5_{1}.png">
</p>

<p align="center">
<img src ="static/strat6_{1}.png">
</p>

<p align="center">
<img src ="static/strat7_{1}.png">
</p>

#
"""
	ticker = raw_input("Ticker: ").upper()
	a = main.Trade(ticker)
	company = main.get_company_by_ticker(ticker)
	startAmount = 1000000
	stockMentionRanking = main.calc_stock_ranking(ticker) + 1
	print(stockMentionRanking)
	totalCount = main.get_total_count_by_ticker(ticker)
	print(totalCount)
	sentiment = main.get_sentiment_by_ticker(ticker)
	print(sentiment)
	mentionsByDay = main.get_weekday_by_ticker(ticker)
	stockFirstMentioned = main.get_first_comment_with_ticker(ticker)
	#print stockFirstMentioned
	table = '''
	|Strategy Name|Total Trades|Return Percentage|Return|Alpha|
| ------------- |:-------:|:-------:|:-------:|:-------:|'''
	buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
	print(" buy and hold ")
	print(buyAndHold)

	strat1 = a.test_strategy(algo.strategy1, startAmount)-startAmount
	typeVal = "Strategy 1"
	returnVal = "${:,.2f}".format(strat1)
	if "-" in str(returnVal):
		returnVal = returnVal.replace("-", "")
		returnVal = "-" + returnVal
	table += "\n|{0}|{1}|{2}%|{3}|0|".format(typeVal, a.totalTrades, round((((float(strat1)/float(startAmount)))*100), 2), returnVal)


	strat4 = a.test_strategy(algo.strategy4, startAmount)-startAmount
	typeVal = "Strategy 4"
	returnVal = "${:,.2f}".format(strat4)
	if "-" in str(returnVal):
		returnVa2 = returnVal.replace("-", "")
		returnVal = "-" + returnVal
	table += "\n|{0}|{1}|{2}%|{3}|0|".format(typeVal, a.totalTrades, round((((float(strat4)/float(startAmount)))*100), 2), returnVal)


	strat5 = a.test_strategy(algo.strategy5, startAmount)-startAmount
	typeVal = "Strategy 5"
	returnVal = "${:,.2f}".format(strat5)
	if "-" in str(returnVal):
		returnVal = returnVal.replace("-", "")
		returnVal = "-" + returnVal
	table += "\n|{0}|{1}|{2}%|{3}|0|".format(typeVal, a.totalTrades, round((((float(strat5)/float(startAmount)))*100), 2), returnVal)

	strat6 = a.test_strategy(algo.strategy6, startAmount)-startAmount
	typeVal = "Strategy 6"
	returnVal = "${:,.2f}".format(strat6)
	if "-" in str(returnVal):
		returnVal = returnVal.replace("-", "")
		returnVal = "-" + returnVal
	table += "\n|{0}|{1}|{2}%|{3}|0|".format(typeVal, a.totalTrades, round((((float(strat6)/float(startAmount)))*100), 2), returnVal)

	strat7 = a.test_strategy(algo.strategy7, startAmount)-startAmount
	typeVal = "Strategy 7"
	returnVal = "${:,.2f}".format(strat7)
	if "-" in str(returnVal):
		returnVal = returnVal.replace("-", "")
		returnVal = "-" + returnVal
	table += "\n|{0}|{1}|{2}%|{3}|0|".format(typeVal, a.totalTrades, round((((float(strat7)/float(startAmount)))*100), 2), returnVal)


	message = message.format(company, ticker, '{:,}'.format(totalCount), round(sentiment, 4), stockMentionRanking, '{:,}'.format(stockFirstMentioned), table)
	print message
	'''for key, value in main.calc_predicted_direction("MU").iteritems():
		print("{} {}".format(key, value))'''
