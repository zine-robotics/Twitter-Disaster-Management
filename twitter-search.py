try:
	import json
except ImportError:
	import simplejson as json

# Importing the tweepy library for scavenging
import tweepy

# Variables that contain usedful auhenticaion information
ACESS_TOKEN='1043092890400915456-RxJRWkK4uA0yyfxmXXLkEgo5dUd3FZ'
ACCESS_SECRET='LLdYbd8XE7cspcdg2B0TG6OzdTpYW1TIyp6U3aeKR2aYc'
CONSUMER_KEY='StGcTWfO4OcI6HIMc6ETtZ8LL'
CONSUMER_SECRET='7zfyJwVFgmEKW3PM8mPzq2qat0IVlY1YPdbcQ5Q9t9yJGaZxit'

# Setting up tweepy to authenticate with twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

tweets = tweepy.Cursor(api.search, q='%23floods %23india')
List=[]
for status in tweets.items():
	List.append(status._json)

for tweet in List:
	if 'text' in tweet:
		print(tweet['id'])
		print(tweet['text'])
		print(tweet['user']['name'])
			