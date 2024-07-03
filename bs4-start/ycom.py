import requests
from bs4 import BeautifulSoup
response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text,"html.parser")
# with open("ycom.txt","w+",encoding="utf-8") as file:
#     file.write(str(soup))
for tag in soup.find_all("span",class_="titleline"): 
    tag = tag.find("a")
    print(tag.get("href"))


# Select is for css queries 
# Find is for tags

# print(soup.prettify)