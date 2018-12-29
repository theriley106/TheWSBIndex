import json
import main



if __name__ == '__main__':
	myVals = []
	g = len(main.STOCK_TICKERS)
	for i, val in enumerate(main.STOCK_TICKERS):
		sentiment = main.get_sentiment_by_ticker(val)
		print("{} | {}".format(val, sentiment))
		myVals.append({"ticker": val, "sentiment": sentiment})
		with open('sentimentByTicker.json', 'w') as fout:
			json.dump(myVals, fout)
		print("{}/{}".format(i, g))
