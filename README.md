<h1 align="center">The WSB Index</h1>

<p align="center">
<img src ="static/wsbLogo.png" height="250" width="400">
<h3 align="center">An algorithmic trading strategy to predict market volatility from /r/WallStreetBets comments</h3>
</p>

<h2 align=center><a href="https://www.kaggle.com/theriley106/wallstreetbetscomments">Download the Dataset Here</a></h2>

## Overall Analysis

<p style="font-size:14px;"">
  Total Comments: <b>2,979,131</b></p>

<p style="font-size:14px;"">
  Total Comments Mentioning Valid Securities: <b>281,550</b></p>

<p style="font-size:14px;"">
  First Comment: <b>Wednesday, April 11, 2012 4:46:43 PM</b></p>

#

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

#

### Best Securities by Sentiment Polarity (w/ 50+ Mentions)

|Ticker|Sentiment|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|SPWR|0.11|SunPower Corporation|Technology|Semiconductors|
|NTES|0.0969|NetEase, Inc.|Miscellaneous|Business Services|
|SWKS|0.0949|Skyworks Solutions, Inc.|Technology|Semiconductors|
|NTLA|0.0927|Intellia Therapeutics, Inc.|Health Care|Biotechnology: In Vitro & In Vivo Diagnostic Substances|
|ONCS|0.0912|OncoSec Medical Incorporated|Health Care|Major Pharmaceuticals|

#

### Worst Securities by Sentiment Polarity (w/ 50+ Mentions)

|Ticker|Sentiment|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|TRIL|-0.0415|Trillium Therapeutics Inc.|Health Care|Major Pharmaceuticals|
|LION|-0.0412|Fidelity Southern Corporation|Finance|Major Banks|
|LOCO|-0.0356|El Pollo Loco Holdings, Inc.|Consumer Services|Restaurants|
|RETA|-0.0329|Reata Pharmaceuticals, Inc.|Health Care|Major Pharmaceuticals|
|NEXT|-0.0319|NextDecade Corporation|Public Utilities|Oil & Gas Production|

#

### Tickers based on Trading Volume/Mention Ratio
|Ticker|Volume/Mention|Company|Average Volume|Mentions|
| ------------- |:-------:|:-------:|:-------:|:-------:|
|PT|6.203|Pintec Technology Holdings Limited|9143|1471|
|LINK|8.3809|Interlink Electronics, Inc.|5540|661|
|OLD|10.0424|The Long-Term Care ETF|1767|176|
|PY|11.1917|Principal Shareholder Yield Index ETF|1701|153|
|VALU|38.0743|Value Line, Inc.|3846|101|
|SELF|45.4174|Global Self Storage, Inc.|12626|277|
|SG|51.3975|Sirius International Insurance Group, Ltd.|4677|91|
|BRAC|52.8569|Black Ridge Acquisition Corp.|31027|587|
|APM|53.5876|Aptorum Group Limited|214|4|
|SP|55.1967|SP Plus Corporation|73246|1323|

#

### Most Active Posters on /r/WallStreetBets (Excluding Bots)
|Username|Total Comments|Average Sentiment|Most Mentioned Ticker|
| ------------- |:-------:|:-----:|:-------------:|
theycallme1 | 16967 | 0.0249 | Z |
avgazn247 | 14042 | 0.0247 | MU |
SIThereAndThere | 7915 | 0.0151 | Z |
brutalpancake | 6022 | 0.0288 | MU |
Macabilly | 5554 | 0.0165 | AMD |

#

### Best Tickers Based on Average Upvote Count

|Ticker|Average Upvotes|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|WASH|52.0|Washington Trust Bancorp, Inc.|Finance|Major Banks|
|ALQA|44.0|Alliqua BioMedical, Inc.|Health Care|Medical/Dental Instruments|
|FMBI|39.0|First Midwest Bancorp, Inc.|Finance|Major Banks|
|POOL|33.0|Pool Corporation|Consumer Durables|Industrial Specialties|
|LIND|31.0|Lindblad Expeditions Holdings Inc. |Consumer Services|Transportation Services|

#

### Worst Tickers Based on Average Upvote Count

|Ticker|Average Upvotes|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|CNTY|-8.0|Century Casinos, Inc.|Consumer Services|Hotels/Resorts|
|CTRN|-8.0|Citi Trends, Inc.|Consumer Services|Clothing/Shoe/Accessory Stores|
|ABIL|-4.0|Ability Inc.|Consumer Durables|Telecommunications Equipment|
|DOVA|-3.0|Dova Pharmaceuticals, Inc.|Health Care|Major Pharmaceuticals|
|EEMA|-3.0|iShares MSCI Emerging Markets Asia ETF|n/a|n/a|

#

### Most Popular Tickers Per Day

## Security-Specific Analysis

### MU

Total Comments Mentioning Ticker:

Average Sentiment Towards Ticker:

Average Daily Mentions (ADM):

#### Mentions Per Weekday

#### Stock Performance vs. (Daily Mentions - Average Daily Mentions)

### AMD

### TSLA

### AAPL

### NVDA


## Data Visualizations

### Top-20 Stock Tickers by Total Mentions

<p align="center">
<img src ="static/newTotalMentions.png">
</p>

### Stock Tickers Mentions by Day

### Stock Ticker Mentions by Average Vote Count

## Strategies

### Strategy #1

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


## Notable Revisions

### December 29th 2018

Prior to December 29th, sentiment analysis was done on comments without consideration for the sentiment of the ticker itself.  This overlook returned biased results in favor of companies with ticker names that doubled as valid words in the english dictionary.

To fix this overlook, I modified the string prior to calculating sentiment so that all tickers are replaced with "TSLA" (a sentiment neutral ticker).

An example of the bias caused by this overlook can be seen in the original *Best Securities by Sentiment Polarity* table below (initially published in [commit 89ddf9d](https://github.com/theriley106/TheWSBIndex/commit/89ddf9dd93d96ba8a1722ecc8d05b026feec75b3)).

|Ticker|Sentiment|Company|Sector|Industry|
| ------------- |:-------------:|:-----:|:-------------:|:-----:|
|GOOD|0.4238|Gladstone Commercial Corporation|Consumer Services|Real Estate|
|NICE|0.4114|NICE Ltd|Technology|Computer Manufacturing|
|WIN|0.4112|Windstream Holdings, Inc.|Public Utilities|Telecommunications Equipment|
|LOVE|0.2962|The Lovesac Company|Consumer Services|Other Specialty Stores|
|STRO|0.2424|Sutro Biopharma, Inc.|Health Care|Biotechnology: Biological Products (No Diagnostic Substances)|
