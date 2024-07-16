from bs4 import BeautifulSoup
import requests
import smtplib

mail = "viisloor@gmail.com"
passw = "" #Get this from Google app passwords

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,kn;q=0.7'
}

URL_ENDPOINT = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL_ENDPOINT,headers=headers)
# print(response.text)

soup = BeautifulSoup(response.content,"html.parser")
tags = soup.find_all(class_="priceToPay")
for tag in tags:
    cost=tag.text
if cost < 99.99:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = mail , password=passw)
    connection.sendmail(from_addr=mail, to_addrs="receiver@gmail.com",msg="Subject:Trying SMTP\n\nSent from smtplib")
    connection.close()
else:
    pass    
