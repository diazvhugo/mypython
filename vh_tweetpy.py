#!/usr/bin/python

import json
import oauth2 as oauth
import requests

consumer_key = "Cv6EU0VArgAUNRo084lVLjbD2"
consumer_secret = "b5IyXXJXcShuLQsf7obUtJQj4h0CPvQLJQrOAhJOuBxBGFVt1e"

access_token="84987976-Pmutc5Qa6BaqpvTCNSAOfZ0emCun0SJsKB4NldIrt"
access_token_secret = "We3mPvqQmXJHLiDjLdil1Endxu2a9j2yCzNua2TxSTEum"

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=access_token, secret=access_token_secret)
client = oauth.Client(consumer, access_token)

#timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=diazvhugo&count=1"
timeline_endpoint = "https://api.twitter.com/1.1/trends/place.json?id=23424900"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
	for n in range(0,10):
		print tweets[0]['trends'][n]['name']
#	print data
