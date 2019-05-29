try: 
	import json
except ImportError:
	import simplejson as json

tweets_filename = 'twitter_search.txt'
tweets_file = open(tweets_filename, 'r')


for line in tweets_file:
	try:
		
		if 'text' in tweet:
			print(tweet['id'])
			print(tweet['text'])
			print(tweet['user']['name'])
			
			hashtags = []
			for hashtag in tweet['entities']['hashtags']:
				hashtags.append(hashag['text'])
			print(hashtags)
	except:
		continue