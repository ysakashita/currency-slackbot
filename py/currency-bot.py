import json
import os
import slack
import urllib.request

# Account of Slack
slack_token = os.environ["SLACK_TOKEN"]

# Currency API
BASE_URL = 'http://apilayer.net/api/live?access_key='
api_access_key = os.environ["API_ACCESS_KEY"]
URL = BASE_URL + api_access_key

# Get currency (USD-JPYEN)
HEADERS = {"Content-Type":"application/json"}
req = urllib.request.Request(url=URL, headers=HEADERS)

res = urllib.request.urlopen(req)
data = json.load(res)
quotes = data["quotes"]
jpyen = quotes["USDJPY"]

msg = "1 $ = " +  str(jpyen) + " Yen"

# Send message to Slack
client = slack.WebClient(token=slack_token)
client.chat_postMessage(
    channel="#currency",
    text=msg
)
