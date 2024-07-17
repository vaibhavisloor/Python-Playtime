from bs4 import BeautifulSoup
import requests
URL_ENDPOINT = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL_ENDPOINT)


soup = BeautifulSoup(response.content,"html.parser")
tags = soup.find_all(class_="priceToPay")
for tag in tags:
    cost=tag.text
print(cost)    
