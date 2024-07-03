import requests
from bs4 import BeautifulSoup


# response = requests.get("https://www.bseindia.com/markets/equity/eqreports/topmarketcapitalization.aspx")
# print(response.text)


with open ("Top Companies\index.txt") as file:
    file = file.read()

soup = BeautifulSoup(file,"html.parser")

for tag in (soup.find_all(name="a",class_="tablebluelink",target="_blank")):
            print(tag.text)