import tweepy
import configparser
import pandas as pd

#read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authenthication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

#user tweets
#user = 'veritasium'
#limit=100

#tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# search tweets
#for hashtags
keywords = '#Onion'

#for user
#keywords = '#@veritasium'
limit = 1000

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=1000, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

#create DataFrame
columns = ['Time', 'User', 'Tweet', 'Location', 'Retweet Count']
#df_raw = pd.DataFrame(data=list_tweets, columns=['id', 'text', 'user', 'location', 'created_at', 'retweet_count', 'image', 'url'])
data = []

for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text, tweet.user.location, tweet.retweet_count])
    #list_tweets.append([tweet.id, tweet.full_text, tweet.user.screen_name, tweet.user.location, tweet.created_at, tweet.retweet_count, media, url])
    
df = pd.DataFrame(data, columns=columns)

print(df)

df.to_csv('tweet.csv')