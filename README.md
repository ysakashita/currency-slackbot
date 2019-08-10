# currency-slackbot
The bot send a message which is exchange rate from US $ to Japanese Yen. 

## Prepare

1. Get API access key for currencylayer  

The currency-slackbot use the currencylayer's API (https://currencylayer.com/).  
Please sign in [currenclylaer.com](https://currencylayer.com/) and get the API access key in the dashbord on the site.  
(The currenclylaer has a free plan that you can use 250 requests/month.)

2. Install a Slack bot and get "Bot User OAuth Acess Token"  

Please check a [document for slack bot](https://api.slack.com/bot-users)

## How to use the currency-slackbot

1. Set environment value

```bash
$ export SLACK_TOKEN='<Bot User OAuth Acess Token of Slack>'
$ export API_ACCESS_KEY='<API access key of currencylayer>'
```

2. Execute currency-bot.py

```bash
$ pyython py/currency-bot.py
```

If your python3.x environment don't install slackclient package, you should install it.

```
$ pip3 install slackclient
```

## How to deploy to Kubernetes.

You can use the bot in Kubernetes.
Please setup by the following steps.

1.  Create secret

```
$ kubectl create secret generic currency-slackbot \
     --from-literal SLACK_TOKEN='<Bot User OAuth Acess Token of Slack>' \
     --from-literal API_ACCESS_KEY='<API access key of currencylayer>'
```

2. Deploy cronjob

```
$ kubectl deploy -f kubernetes/cronjob.yaml
```
