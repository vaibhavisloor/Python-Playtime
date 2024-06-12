import requests


response=requests.get("https://catfact.ninja/fact")
print(response.json())
json = response.json()
print(json["fact"])