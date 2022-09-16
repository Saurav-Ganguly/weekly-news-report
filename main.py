import os
# weekly news report
import requests
import datetime as DT

api_key = os.environ['api_key']

topic = input("What topic of news?: ")
# if topic containes spaces add %20
topic_array = topic.split(" ")
topic_str = "%20".join(topic_array)
date_today = DT.date.today()
date_today_str = date_today.strftime("%Y-%-m-%-d")
date_week_ago = date_today - DT.timedelta(days=7)
date_week_ago_str = date_week_ago.strftime("%Y-%-m-%-d")

url = f"https://newsapi.org/v2/everything?qInTitle={topic_str}&from={date_week_ago_str}&to={date_today_str}&sortBy=popularity&language=en&apiKey={api_key}"
r = requests.get(url)
content = r.json()
articles = content["articles"]
for item in articles:
    print(item["title"])
    print("*---------------------------------*")
