from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import json
import calendar
import main
import algo
import datetime
import time
from flask_sockets import Sockets
import random



app = Flask(__name__, static_url_path='/static')
sockets = Sockets(app)

balance = [100000]

@sockets.route('/echo')
def echo_socket(ws):
    while True:
    	#message = ws.receive()
        ws.send(str(balance[-1]))
        num = random.randint(1, 10000)
        if random.randint(1,2) == 2:
        	num *= -1
        balance.append(balance[-1] + num)
        time.sleep(.1)


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

@app.route('/viz2', methods=['GET'])
def viz2():
	db = json.load(open("TESLA_DATA.json"))
	return render_template("viz2.html", DATABASE=db)

@app.route('/viz3', methods=['GET'])
def viz3():
	db = json.load(open("TESLA_DATA_COMMENTS.json"))
	return render_template("viz3.html", DATABASE=db)

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

@app.route('/strat3/<ticker>', methods=['GET'])
def testStrat3(ticker):
	ticker = ticker.upper()
	a = main.Trade(ticker)
	startAmount = 1000000
	buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
	strat1 = a.test_strategy(algo.strategy3, startAmount)-startAmount
	strat1Info = a.get_more_info()
	return render_template("lines.html", DATABASE=strat1Info, strategy="Strategy 3", balance='{:,.2f}'.format(startAmount), stock=ticker.upper())

@app.route('/strat4/<ticker>', methods=['GET'])
def testStrat4(ticker):
	ticker = ticker.upper()
	a = main.Trade(ticker)
	startAmount = 1000000
	buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
	strat1 = a.test_strategy(algo.strategy4, startAmount)-startAmount
	strat1Info = a.get_more_info()
	return render_template("lines.html", DATABASE=strat1Info, strategy="Strategy 4", balance='{:,.2f}'.format(startAmount), stock=ticker.upper())

@app.route('/strat5/<ticker>', methods=['GET'])
def testStrat5(ticker):
	ticker = ticker.upper()
	a = main.Trade(ticker)
	startAmount = 1000000
	buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
	strat1 = a.test_strategy(algo.strategy5, startAmount)-startAmount
	strat1Info = a.get_more_info()
	return render_template("lines.html", DATABASE=strat1Info, strategy="Strategy 5", balance='{:,.2f}'.format(startAmount), stock=ticker.upper())

@app.route('/strat6/<ticker>', methods=['GET'])
def testStrat6(ticker):
	ticker = ticker.upper()
	a = main.Trade(ticker)
	startAmount = 1000000
	buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
	strat1 = a.test_strategy(algo.strategy6, startAmount)-startAmount
	strat1Info = a.get_more_info()
	return render_template("lines.html", DATABASE=strat1Info, strategy="Strategy 6", balance='{:,.2f}'.format(startAmount), stock=ticker.upper())

@app.route('/strat7/<ticker>', methods=['GET'])
def testStrat7(ticker):
	ticker = ticker.upper()
	a = main.Trade(ticker)
	startAmount = 1000000
	buyAndHold = a.calc_buy_and_hold(startAmount)-startAmount
	strat1 = a.test_strategy(algo.strategy7, startAmount)-startAmount
	strat1Info = a.get_more_info()
	return render_template("lines.html", DATABASE=strat1Info, strategy="Strategy 7", balance='{:,.2f}'.format(startAmount), stock=ticker.upper())


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
