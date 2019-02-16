# Copy of http://stackoverflow.com/a/20104705
from flask import Flask, render_template
from flask_sockets import Sockets
import datetime
import time

app = Flask(__name__)

sockets = Sockets(app)

@sockets.route('/echo')
def echo_socket(ws):
    while True:
    	#message = ws.receive()
        ws.send(str(datetime.datetime.now()))
        time.sleep(.1)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/echo_test', methods=['GET'])
def echo_test():
    return render_template('example.html')

if __name__ == '__main__':
    app.run()
