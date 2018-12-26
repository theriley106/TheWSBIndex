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
