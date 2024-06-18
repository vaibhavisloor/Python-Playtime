STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
STOCK_API_KEY = os.getenv('STOCK_API_KEY')

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT,params=stock_params)
response=response.json()["Time Series (Daily)"]

prices_list = [value for key,value in response.items()]

yesterday_closing_price = round(float(prices_list[0]['4. close']),2)
print(yesterday_closing_price)

day_before_yesterday_closing_price = round(float(prices_list[1]['4. close']))
print(day_before_yesterday_closing_price)


difference = round(yesterday_closing_price - day_before_yesterday_closing_price)
print(difference)

percentage_difference = (abs(difference) / day_before_yesterday_closing_price) * 100


if percentage_difference >= 5: 
    news_params={
        "apiKey":NEWS_API_KEY,
        'qInTitle':COMPANY_NAME,
        "language":"en",
    }
    response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles = response.json()["articles"]
    title = [article["title"] for article in articles[:3]]
    print(title)


account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

if difference > 0 :
    symbol = '🔺'
else:
    symbol = '🔻'


text = f' Today the stock moved by {round(percentage_difference,2)} {symbol}.\nThis is the latest news regarding {COMPANY_NAME} :\n'
for t in title:
    text+=f'{t}\n'    

print(text)
message = client.messages.create(
                              body=text,
                              from_='+19523142296',
                              to='+91 99008 55730'
                          )