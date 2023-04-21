import yfinance as yf

def stock_price(symbol):
    # Define the stock ticker symbol and exchange

    # Create a Ticker object to retrieve the stock information
    stock = yf.Ticker(symbol)

    # Try to get the current stock price from the regularMarketPrice attribute, or fall back to the regularMarketOpen attribute
    if "currentPrice" in stock.info:
        price = stock.info["currentPrice"]
    elif "regularMarketPrice" in stock.info:
        price = stock.info["regularMarketPrice"]
    else:
        price = stock.info["regularMarketOpen"]

    # Get the previous day's closing price
    if "previousClose" in stock.info:
        prev_close = stock.info["previousClose"]
    else:
        prev_close = stock.info["regularMarketPreviousClose"]

    # Calculate the percentage change relative to the previous day's closing price
    percent_change = (price - prev_close) / prev_close * 100

    # Create a string with the current stock price and percentage change
    price_str = "The current price of Clinical Laserthermia Systems (CLS B) is {:.3f} SEK ({:.2f}%{})".format(
        price, abs(percent_change), " increase" if percent_change > 0 else " decrease"
    )

    # Write highs and lows
    high = ""
    if "dayHigh" in stock.info:
        high = stock.info["dayHigh"]
    else:
        high = stock.info["regularMarketDayHigh"]

    low = ""
    if "dayLow" in stock.info:
        low = stock.info["dayLow"]
    else:
        low = stock.info["regularMarketDayLow"]

    ret = "%s\nDay high: %s\nDay low: %s" % (price_str, high, low)
    return ret