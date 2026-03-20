import yfinance as yf

def load_data(ticker="AAPL", start="2015-01-01"):
    data = yf.download(ticker, start=start)
    return data['Close']
