<h1 align="center">The WSB Index</h1>

<p align="center">
<img src ="static/wsbLogo.png" height="350" width="500">
<h3 align="center">An algorithmic trading strategy to predict market volatility from /r/WallStreetBets comments</h3>
</p>

## Analysis

### Best Securities by Sentiment Polarity

|Ticker|Sentiment|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|CPTA|0.7|Capitala Finance Corp.|n/a|n/a|
|GILT|0.7|Gilat Satellite Networks Ltd.|Technology|Radio And Television Broadcasting And Communications Equipment|
|EFAS|0.7|Global X MSCI SuperDividend EAFE ETF|n/a|n/a|
|GSIT|0.7|GSI Technology, Inc.|Technology|Semiconductors|
|PXI|0.7|Invesco DWA Energy Momentum ETF|n/a|n/a|


### Worst Securities by Sentiment Polarity

|Ticker|Sentiment|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|WMGI|-0.91|Wright Medical Group N.V.|Health Care|Industrial Specialties|
|TCMD|-0.8125|Tactile Systems Technology, Inc.|Health Care|Medical/Dental Instruments|
|OMEX|-0.75|Odyssey Marine Exploration, Inc.|Consumer Services|Marine Transportation|
|PEBK|-0.75|Peoples Bancorp of North Carolina, Inc.|Finance|Major Banks|
|HOMB|-0.7|Home BancShares, Inc.|Finance|Major Banks|

## Data Visualizations

### Top-20 Stock Tickers by Total Mentions

<p align="center">
<img src ="static/newTotalMentions.png">
</p>

### Stock Tickers Mentions by Day

### Stock Ticker Mentions by Average Vote Count

## Language Processing

### Overview

WallStreetBets is a discussion forum about day trading, stocks, options, futures, and anything market related, so it would be innacurate to assume that any comment containing a stock ticker indicated a long position on the security.

From my understanding this is an NLP problem that's relatively difficult to solve.  A *slighly* more accurate way of extracting the type of position from a comment would be to assume a long position unless the word "short" is present in the comment.

Unfortunately, this strategy would fail in comments discussing options, and in our model the purchase of a put option would imply the same sentiment as a short position.

Lastly, the discussion of multiple securities in a single comment can cause confusion as to the implied position relative to each stock ticker.

### Proposed Solution

Rather than using NLTK or RAKE, I created an algorithm present in *main.extract_buy_or_sell()* that attempts to extract the indicated position towards each stock ticker in a comment.  Here is the algorithm in Psuedocode:

```
comment_info = {'puts': [], 'calls': [], 'buy': [], 'sell': []}
for sentence in comment:
    while sentence:
        word = sentence.pop()
        if word == 'buy' or 'buying':
            tempList = []
            while sentence:
                newWord = sentence.pop()
                if newWord is StockTicker:
                    tempList.append(newWord)
                elif newWord == 'puts' and len(tempList) > 0:
                    comment_info['puts'] += tempList
                    tempList.clear()
                    break
                elif newWord == 'calls' and len(tempList) > 0:
                    comment_info['calls'] += tempList
                    tempList.clear()
                    break
            comment_info['buy'] += tempList
        elif word == 'short' or 'shorting':
            while sentence:
                newWord = sentence.pop()
                if newWord is StockTicker:
                    comment_info['sell'] += newWord
                else:
                    break
        elif word == 'sell' or 'sold' or 'close' or 'closing' or 'shorts':
            tempList = []
            while sentence:
                newWord = sentence.pop()
                if newWord is StockTicker:
                    tempList.append(newWord)
               elif newWord == 'puts' and len(tempList) > 0:
                    comment_info['puts'] += tempList
                    tempList.clear()
                    break
                elif newWord == 'calls' and len(tempList) > 0:
                    comment_info['calls'] += tempList
                    tempList.clear()
                    break
                elif newWord == 'shorts' and len(tempList) > 0:
                    comment_info['buy'] += tempList
                    tempList.clear()
                    break
            comment_info['sell'] += tempList
        elif word is StockTicker:
            tempList = [word]
            while sentence:
                newWord = sentence.pop()
                if newWord is StockTicker:
                    tempList.append(newWord)
                elif newWord == 'puts' and len(tempList) > 0:
                    comment_info['puts'] += tempList
                    tempList.clear()
                    break
                elif newWord == 'calls' and len(tempList) > 0:
                    comment_info['calls'] += tempList
                    tempList.clear()
                    break
            comment_info['buy'] += tempList
```

### Examples

##### Note: This algo is only being used for stocks traded on the Nasdaq, hence certain *valid* stock tickers are considered *invalid* as we are not actively pursing information on them.

**"Short GPRO"**

> **{"sell": ["GPRO"], "buy": [], "calls": [], "puts": []}**

**"HIMX, EOG, WPRT, VALE. Some high div paying stocks NLY, PMT, HTS."**

> **{"sell": [], "buy": ["HIMX", "WPRT"], "calls": [], "puts": []}**

**"AAMRQ and ONCS did great for me (and EPZM yesterday)"**

> **{"sell": [], "buy": ["ONCS", "EPZM"], "calls": [], "puts": []}**

**"holding ZGNX now. Thanks man!"**

> **{"sell": [], "buy": ["ZGNX"], "calls": [], "puts": []}**

**"I threw a couple of hundreds on VVUS earnings. It both beat and is up! Yay!"**

> **{"sell": [], "buy": ["VVUS"], "calls": [], "puts": []}**

**"No. OP is hyping his GPRO bet."**

> **{"sell": [], "buy": ["GPRO"], "calls": [], "puts": []}**

**"I closed my SRPT position today as well.  258% gain."**

> **{"sell": ["SRPT"], "buy": [], "calls": [], "puts": []}**

**"I think SFM has much better growth opportunty"**

> **{"sell": [], "buy": ["SFM"], "calls": [], "puts": []}**

**"Though he's doing great in AAPL."**

> **{"sell": [], "buy": ["AAPL"], "calls": [], "puts": []}**

**"I have some money to spare after my 300% gain on TSLA puts."**

> **{"sell": [], "buy": [], "calls": [], "puts": ["TSLA"]}**

**"Disclaimer, I am short Aug 100 covered calls. I am also long AAPL (though that's implied)."**

> **{"sell": [], "buy": ["AAPL"], "calls": [], "puts": []}**

**"looks like CSIQ is about to turn around tmr...."**

> **{"sell": [], "buy": ["CSIQ"], "calls": [], "puts": []}**

**"GPRO October $60 Puts"**

> **{"sell": [], "buy": [], "calls": [], "puts": ["GPRO"]}**
