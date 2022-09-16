import os
# REST Api -> Reprasentational state transfer Application programming 
import requests

api_key = os.environ['api_key']

# print(api_key)
url = f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-9-10&to=2022-9-15&sortBy=popularity&language=en&apiKey={api_key}"
r = requests.get(url)
content = r.json()
articles = content["articles"]
for item in articles:
  print(item["title"])
  print("*---------------------------------*")
