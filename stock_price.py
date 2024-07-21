import yfinance as yf
from datetime import datetime

end = datetime.now()
start = datetime(end.year-20,end.month,end.day)
stock="GOOG"

google_data= yf.download(stock,start,end)
google_data.head()