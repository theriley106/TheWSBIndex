<h1 align="center">The WSB Index</h1>

<p align="center">
<img src ="static/wsbLogo.png" height="350" width="500">
<h3 align="center">An algorithmic trading strategy to predict market volatility from /r/WallStreetBets comments</h3>
</p>

## Data Visualizations

### Top-20 Stock Tickers by Total Mentions

<p align="center">
<img src ="static/newTotalMentions.png">
</p>

### Stock Tickers Mentions by Day

### Stock Ticker Mentions by Average Vote Count

### Language Processing

#### Examples:

Comment: "Short GPRO"

Returns: {'sell': ['GPRO'], 'buy': [], 'calls': [], 'puts': []}

Comment: HIMX, EOG, WPRT, VALE. Some high div paying stocks NLY, PMT, HTS.

Returns: {'sell': [], 'buy': ['HIMX', 'WPRT'], 'calls': [], 'puts': []}


Comment: AAMRQ and ONCS did great for me (and EPZM yesterday)

Returns: {'sell': [], 'buy': ['ONCS', 'EPZM'], 'calls': [], 'puts': []}


Comment: holding ZGNX now. Thanks man!

Returns: {'sell': [], 'buy': ['ZGNX'], 'calls': [], 'puts': []}

Comment: I threw a couple of hundreds on VVUS earnings. It both beat and is up! Yay!

Returns: {'sell': [], 'buy': ['VVUS'], 'calls': [], 'puts': []}

Comment: No. OP is hyping his GPRO bet.

Returns: {'sell': [], 'buy': ['GPRO'], 'calls': [], 'puts': []}

Comment: I closed my SRPT position today as well.  258% gain.

Returns: {'sell': ['SRPT'], 'buy': [], 'calls': [], 'puts': []}

Comment: I think SFM has much better growth opportunty

Returns: {'sell': [], 'buy': ['SFM'], 'calls': [], 'puts': []}

Comment: Though he's doing great in AAPL.

Returns: {'sell': [], 'buy': ['AAPL'], 'calls': [], 'puts': []}

Comment: I have some money to spare after my 300% gain on TSLA puts.

Returns: {'sell': [], 'buy': [], 'calls': [], 'puts': ['TSLA']}

Comment: Disclaimer, I am short Aug 100 covered calls. I am also long AAPL (though that's implied).

Returns: {'sell': [], 'buy': ['AAPL'], 'calls': [], 'puts': []}

Comment: looks like CSIQ is about to turn around tmr....

Returns: {'sell': [], 'buy': ['CSIQ'], 'calls': [], 'puts': []}

Comment: GPRO October $60 Puts

Returns: {'sell': [], 'buy': [], 'calls': [], 'puts': ['GPRO']}

