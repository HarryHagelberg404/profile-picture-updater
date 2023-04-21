import requests
from requests_oauthlib import OAuth1
from stocks import stock_price
from datetime import datetime
from month_bio import months_passed

current_date = datetime.now()
date = months_passed(current_date)

symbol = "CLS-B.ST"
stock = stock_price("CLS-B.ST")

# Enter your Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Set up OAuth1 authentication
auth = OAuth1(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Set the API endpoint and create the tweet
url = "https://api.twitter.com/2/tweets"
tweet_text = "%s\n%s" % (date, stock)
print(tweet_text)
payload = {"text": tweet_text}

# Make the request to the API
response = requests.post(url, json=payload, auth=auth)

# Check the response status code
if response.status_code == 201:
    print("Tweet posted successfully!")
else:
    print("Error posting tweet: %s" % response.text)