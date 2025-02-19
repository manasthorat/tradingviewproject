from SmartApi import SmartConnect  # or from smartapi.smartConnect import SmartConnect
import pyotp, time, pytz
from datetime import datetime, timedelta
import pandas as pd
from config import *

# Create an object of SmartConnect
obj = SmartConnect(api_key=apikey)

def login():
    """
    Function to login and return AUTH and FEED tokens.
    """
    data = obj.generateSession(username, pwd, pyotp.TOTP(token).now())
    refreshToken = data['data']['refreshToken']
    auth_token = data['data']['jwtToken']
    feed_token = obj.getfeedToken()
    return auth_token, feed_token

def historical_data(exchange,token,from_date, to_date,timeperiod):
    """
    Function to fetch historical data and return it as a Pandas DataFrame.
    """
    try:
        historicParam = {
            "exchange": exchange,
            "symboltoken": token,
            "interval": timeperiod,
            "fromdate": from_date, 
            "todate": to_date
        }
        api_response = obj.getCandleData(historicParam)
        data = api_response['data']
        columns = ['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume']
        df = pd.DataFrame(data, columns=columns)
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df.set_index('DateTime', inplace=True)
        return df
    except Exception as e:
        print("Historic Api failed: {}".format(e))

# Usage Example
auth_token, feed_token = login()

thirty_days_ago = datetime.now() - timedelta(days=30)
from_date = thirty_days_ago.strftime("%Y-%m-%d %H:%M")
to_date = datetime.now().strftime("%Y-%m-%d %H:%M")

exchange = "BSE"
token = 99919000
timeperiod = "FIVE_MINUTE"

df = historical_data(exchange, token, from_date, to_date,timeperiod)
print(df)
