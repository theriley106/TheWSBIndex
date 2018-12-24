from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import json

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

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
