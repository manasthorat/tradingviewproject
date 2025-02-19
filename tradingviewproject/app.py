from flask import Flask, jsonify, render_template, request
import pandas as pd
from datetime import datetime, timedelta
from SmartApi import SmartConnect
import pyotp
from config import *

app = Flask(__name__)

# Create an object of SmartConnect
obj = SmartConnect(api_key=apikey)

# Define stock options
STOCKS = {
    "NIFTY20MAR2523000CE": {"symbol": "NIFTY20MAR2523000CE", "token": "50223", "exchange": "NFO"},
    "NIFTY20MAR2523000PE": {"symbol": "NIFTY20MAR2523000PE", "token": "50224", "exchange": "NFO"},
    "NIFTY": {"symbol": "NIFTY20MAR2523000CE", "token": "99926000", "exchange": "NSE"},
    "SENSEX": {"symbol": "SENSEX", "token": "99919000", "exchange": "BSE"},
}

def login():
    """
    Function to login and return AUTH and FEED tokens.
    """
    data = obj.generateSession(username, pwd, pyotp.TOTP(token).now())
    return data["data"]["jwtToken"], obj.getfeedToken()

def get_timeframe_mapping(timeframe):
    """
    Returns the correct API timeframe string and date range based on user selection.
    """
    now = datetime.now()
    timeframe_map = {
        "1m": ("ONE_MINUTE", now - timedelta(days=1)),     # Last 1 day
        "5m": ("FIVE_MINUTE", now - timedelta(days=7)),    # Last 7 days
        "15m": ("FIFTEEN_MINUTE", now - timedelta(days=15)),  # Last 15 days
        "1h": ("ONE_HOUR", now - timedelta(days=30)),      # Last 30 days
        "1d": ("ONE_DAY", now - timedelta(days=365)),      # Last 1 year
    }
    return timeframe_map.get(timeframe, ("ONE_MINUTE", now - timedelta(days=1)))

@app.route("/")
def home():
    return render_template("index.html", stocks=STOCKS)

@app.route("/get_candlestick_data")
def get_candlestick_data():
    """
    Fetch and return candlestick data based on selected timeframe & stock symbol.
    """
    auth_token, feed_token = login()

    # Get user-selected parameters
    timeframe = request.args.get("timeframe", "1m")
    stock_key = request.args.get("stock", "NIFTY-CE-50223")  # Default stock

    if stock_key not in STOCKS:
        return jsonify({"error": "Invalid stock symbol."})

    stock_info = STOCKS[stock_key]
    exchange = stock_info["exchange"]
    token = stock_info["token"]

    # Map timeframe to API-compatible interval and date range
    timeperiod, from_date = get_timeframe_mapping(timeframe)
    from_date_str = from_date.strftime("%Y-%m-%d %H:%M")
    to_date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        historicParam = {
            "exchange": exchange,
            "symboltoken": token,
            "interval": timeperiod,
            "fromdate": from_date_str,
            "todate": to_date_str
        }
        api_response = obj.getCandleData(historicParam)
        data = api_response.get("data", [])

        # Convert to TradingView format
        candles = [
            {
                "time": int(pd.to_datetime(row[0]).timestamp()),  # Convert to UNIX timestamp
                "open": row[1],
                "high": row[2],
                "low": row[3],
                "close": row[4]
            }
            for row in data
        ]
        return jsonify(candles)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
