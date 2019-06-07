import re

import numpy as np
import pandas as pd
import nltk

tweets = pd.read_csv('./tweet.csv',encoding='ISO-8859-1')

## Data Pre-processing
tweets.dropna(inplace=True)


# Extracting the text from the tweet
# Reoving URLs, removing @... and the hashtags
tweets.text = tweets.text.apply(lambda x: re.sub(u'https\S+', u'', x))
tweets.text = tweets.text.apply(lambda x: re.sub(u'(\s)@\w+', u'', x))
tweets.text = tweets.text.apply(lambda x: re.sub(u'#', u'', x))
tweets.to_csv('./preprocessed_tweets.csv')
print(tweets.text.head())
