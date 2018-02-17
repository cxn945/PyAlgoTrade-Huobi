import pandas as pd
import time

from hbsdk import ApiClient

API_KEY = "API_KEY"
API_SECRET = "API_SECRET"

DEFAULT_SYMBOL='btcusdt'
DEFAULT_PREIOD = 60
headList=["Date Time","Open","High","Low","Close","Volume","Adj Close"]

client = ApiClient(API_KEY, API_SECRET)

# load history of k-line
def load_kline(period = DEFAULT_PREIOD, symbol = DEFAULT_SYMBOL):

    print "start load data, symbol:%s, period: %s minutes" % (symbol, period)
    history = client.mget('/market/history/kline', symbol=symbol, period='%dmin' % period, size=2000)
    print "total raw data count: %d" % len(history)
    jdict= reduce(redf, history, [])
    print "total data of reduce count: %d" % len(history)
    df = pd.DataFrame.from_dict(jdict)
    df.to_csv("2000.csv", index=False, header=headList)

def dtf(x):
    time_local = time.localtime(x)
    return time.strftime("%Y-%m-%d %H:%M:%S",time_local)

def rf(x):
    return [dtf(x.id), x.open, x.high, x.low, x.close, x.vol, x.close]

def redf(x,y):
    return x+[rf(y)]



