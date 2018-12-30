import requests
import re
import time
import datetime
import main
import threading
import glob

ITEMS = main.STOCK_TICKERS
lock = threading.Lock()
THREADS = 4

URL = "https://query1.finance.yahoo.com/v7/finance/download/{0}?period1={1}&period2={2}&interval=1d&events=history&crumb={3}"

def get_yahoo_crumb_cookie():
    """
    Get Yahoo crumb cookie value.
    Original Source: https://pypi.python.org/pypi/fix-yahoo-finance
    """
    res = requests.get('https://finance.yahoo.com/quote/SPY/history')
    yahoo_cookie = res.cookies['B']
    yahoo_crumb = None
    pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')
    for line in res.text.splitlines():
        m = pattern.match(line)
        if m is not None:
            yahoo_crumb = m.groupdict()['crumb']
    return yahoo_cookie, yahoo_crumb

for file in glob.glob("data/*.csv"):
	item = file.partition("/")[2].partition(".cs")[0]
	ITEMS.remove(item)

def download_historical(start_Date="20120412", end_Date="20181231"):
	while len(ITEMS) > 0:
		lock.acquire()
		symbol = ITEMS.pop()
		lock.release()
		try:
		    cookieVal = get_yahoo_crumb_cookie()
		    sd = str(int(time.mktime(datetime.datetime.strptime(start_Date, "%Y%m%d").timetuple())))
		    ed = str(int(time.mktime(datetime.datetime.strptime(end_Date, "%Y%m%d").timetuple())))
		    url = URL.format(symbol, sd, ed, cookieVal[1])
		    res = requests.get(url, allow_redirects=True, cookies={'B': cookieVal[0]})
		    file = open("data/{}.csv".format(symbol), 'wb')
		    file.write(res.content)
		    file.close()
		    print("Done with: {}".format(symbol))
		except Exception as exp:
			print exp

if __name__ == '__main__':
	threads = [threading.Thread(target=download_historical) for i in range(THREADS)]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
