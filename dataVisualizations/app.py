from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/viz1', methods=['GET'])
def viz1():
	return render_template("viz1.html")

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
