STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 

import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



STOCK_API_KEY="V3J813NP8GY0MS35"

NEWS_API_KEY="4e7f83279506465ba385808b5cd8b5df"

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


difference = abs(round(yesterday_closing_price - day_before_yesterday_closing_price,2))
print(difference)

percentage_difference = (difference / day_before_yesterday_closing_price) * 100


if percentage_difference >= 0: 
# if True: 
    news_params={
        "apiKey":NEWS_API_KEY,
        'qInTitle':COMPANY_NAME,
        "language":"en",
    }
    response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles = response.json()["articles"]
    title = [article["title"] for article in articles[:3]]
    print(title)


load_dotenv()
account_sid = os.getenv['account_sid']
auth_token = os.getenv['auth_tok']
client = Client(account_sid, auth_token)

text = f'This is the latest news regarding {COMPANY_NAME} :\n'
for t in title:
    text+=f'{t}\n'    

message = client.messages.create(
                              body=text,
                              from_='+19523142296',
                              to='+91 99008 55730'
                          )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

