from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import json
import calendar
import main
import algo

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/viz1', methods=['GET'])
def viz1():
	a = json.load(open("static/AllCounts.json"))
	db = []
	for key, val in a.iteritems():
		db.append({"Ticker": key, "Mentions": val})
	db = sorted(db, key=lambda k: k['Mentions'])[-20:]
	return render_template("viz1.html", DATABASE=db)

@app.route('/totalByDay/<ticker>', methods=['GET'])
def totalByDay(ticker):
	days = list(calendar.day_abbr)
	mentionsByDay = main.get_weekday_by_ticker(ticker.upper())
	db = []
	for i in range(7):
		a = mentionsByDay[str(i)]
		db.append({"Day": days[i], "Mentions": a})
	#db = sorted(db, key=lambda k: k['Mentions'])[-20:]
	return render_template("days.html", DATABASE=db, stock=ticker.upper())

@app.route('/strat1/<ticker>', methods=['GET'])
def testStrat1(ticker):
	ticker = ticker.upper()
	a = main.Trade(ticker)
	startAmount = 1000000
	buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
	strat1 = a.test_strategy(algo.strategy1, startAmount)-startAmount
	strat1Info = a.get_more_info()
	return render_template("lines.html", DATABASE=strat1Info, strategy="Strategy 1", balance='{:,.2f}'.format(startAmount), stock=ticker.upper())

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
