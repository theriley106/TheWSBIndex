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

### Examples:

##### Note: This algo is only being used for stocks traded on the Nasdaq, hence certain *valid* stock tickers are considered *invalid* as we are not actively pursing information on them.

Comment:
> "Short GPRO"

Result:
> {"sell": ["GPRO"], "buy": [], "calls": [], "puts": []}

#
#
```javascript
[
    {
        "comment": "Short GPRO",
        "values": {
            "sell": [
                "GPRO"
            ],
            "buy": [],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "HIMX, EOG, WPRT, VALE. Some high div paying stocks NLY, PMT, HTS.",
        "values": {
            "sell": [],
            "buy": [
                "HIMX",
                "WPRT"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "AAMRQ and ONCS did great for me (and EPZM yesterday)",
        "values": {
            "sell": [],
            "buy": [
                "ONCS",
                "EPZM"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "holding ZGNX now. Thanks man!",
        "values": {
            "sell": [],
            "buy": [
                "ZGNX"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "I threw a couple of hundreds on VVUS earnings. It both beat and is up! Yay!",
        "values": {
            "sell": [],
            "buy": [
                "VVUS"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "No. OP is hyping his GPRO bet.",
        "values": {
            "sell": [],
            "buy": [
                "GPRO"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "I closed my SRPT position today as well.  258% gain.",
        "values": {
            "sell": [
                "SRPT"
            ],
            "buy": [],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "I think SFM has much better growth opportunty",
        "values": {
            "sell": [],
            "buy": [
                "SFM"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "Though he's doing great in AAPL.",
        "values": {
            "sell": [],
            "buy": [
                "AAPL"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "I have some money to spare after my 300% gain on TSLA puts.",
        "values": {
            "sell": [],
            "buy": [],
            "puts": [
                "TSLA"
            ],
            "calls": []
        }
    },
    {
        "comment": "Disclaimer, I am short Aug 100 covered calls. I am also long AAPL (though that's implied).",
        "values": {
            "sell": [],
            "buy": [
                "AAPL"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "looks like CSIQ is about to turn around tmr....",
        "values": {
            "sell": [],
            "buy": [
                "CSIQ"
            ],
            "puts": [],
            "calls": []
        }
    },
    {
        "comment": "GPRO October $60 Puts",
        "values": {
            "sell": [],
            "buy": [],
            "puts": [
                "GPRO"
            ],
            "calls": []
        }
    }

]```


## Outline

Text -> Function -> Returns Value -> Keep track of average value -> (return value - average value) compared to (change in stock price, volatility of stock price, volumen change, spread, etc.)
