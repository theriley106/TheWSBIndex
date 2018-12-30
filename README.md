<h1 align="center">The WSB Index</h1>

<p align="center">
<img src ="static/wsbLogo.png" height="250" width="400">
<h3 align="center">An algorithmic trading strategy to predict market volatility from /r/WallStreetBets comments</h3>
</p>

## Analysis

### Top Securities by Total Comment Mentions

|Ticker|Mentions|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|MU|33450|Micron Technology, Inc.|Technology|Semiconductors|
|AMD|32526|Advanced Micro Devices, Inc.|Technology|Semiconductors|
|TSLA|12079|Tesla, Inc. |Capital Goods|Auto Manufacturing|
|AAPL|11760|Apple Inc.|Technology|Computer Manufacturing|
|NVDA|11087|NVIDIA Corporation|Technology|Semiconductors|
|AMZN|10835|Amazon.com, Inc.|Consumer Services|Catalog/Specialty Distribution|
|FB|10827|Facebook, Inc.|Technology|Computer Software: Programming, Data Processing|
|Z|9188|Zillow Group, Inc.|Miscellaneous|Business Services|
|MSFT|8137|Microsoft Corporation|Technology|Computer Software: Prepackaged Software|
|QQQ|4939|Invesco QQQ Trust, Series 1|n/a|n/a|

### Best Securities by Sentiment Polarity (w/ 50+ Mentions)

|Ticker|Sentiment|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|GOOD|0.4238|Gladstone Commercial Corporation|Consumer Services|Real Estate|
|NICE|0.4114|NICE Ltd|Technology|Computer Manufacturing|
|WIN|0.4112|Windstream Holdings, Inc.|Public Utilities|Telecommunications Equipment|
|LOVE|0.2962|The Lovesac Company|Consumer Services|Other Specialty Stores|
|STRO|0.2424|Sutro Biopharma, Inc.|Health Care|Biotechnology: Biological Products (No Diagnostic Substances)|

#### This result showed a clear bias for tickers that contain words found in the english language.  The sentiment analysis will have to be rerun with sentiment-neutral words replacing the stock tickers that are present within the comment.


### Worst Securities by Sentiment Polarity (w/ 50+ Mentions)

|Ticker|Sentiment|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|RETA|-0.3441|Reata Pharmaceuticals, Inc.|Health Care|Major Pharmaceuticals|
|SELF|-0.0832|Global Self Storage, Inc.|Consumer Services|Real Estate Investment Trusts|
|CENT|-0.0488|Central Garden & Pet Company|Consumer Durables|Consumer Specialties|
|EXPI|-0.0427|eXp World Holdings, Inc.|Finance|Real Estate|
|DARE|-0.0419|Dare Bioscience, Inc.|Health Care|Major Pharmaceuticals|

### Most Active Posters on /r/WallStreetBets (Excluding Bots)
|Username|Total Comments|Most Mentioned Ticker|Average Sentiment|
| ------------- |:-------:|:-----:|:-------------:|
theycallme1 | 16967 | 0.026 | Z |
avgazn247 | 14042 | 0.0324 | MU |
SIThereAndThere | 7915 | 0.0148 | Z |
brutalpancake | 6022 | 0.0288 | MU |
Macabilly | 5554 | 0.0236 | AMD |

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


## First Comment

Wednesday, April 11, 2012 4:46:43 PM
