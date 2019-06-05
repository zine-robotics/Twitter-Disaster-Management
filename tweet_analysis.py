import numpy as np
import pandas as pd
import nltk

tweets = pd.read_csv('./tweet.csv',encoding='ISO-8859-1')

# Data Pre-processing
tweets = tweets.dropna()
tweets.to_csv('./preprocessed_tweets.csv')
