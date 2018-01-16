# Fetches tweets for a topic and gives the sentiment values, saves into a file.
import tweepy
from textblob import TextBlob
from configparser import RawConfigParser
config = RawConfigParser()
config.read('config_twitter.ini')
# Step 1 - Authenticate
consumer_key = config['CREDENTIAL']['consumer_key']
consumer_secret = config['CREDENTIAL']['consumer_secret']
access_token = config['CREDENTIAL']['access_token']
access_token_secret = config['CREDENTIAL']['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 3 - Retrieve Tweets, MAX 100
query = input('Enter the words you want to search for tweet : ')
number = int(input('Enter the number you want to search for tweet , MAX 100 : '))
public_tweets = api.search(
                   lang="en",
                   q=query + " -rt",
                   count=number,
                   result_type="recent"
                )

file = open('tweet.csv','w',encoding='UTF-8')

for tweet in public_tweets:
    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    if analysis.polarity * 100 :
        print(tweet.text + '\n')
        print(str(analysis.sentiment))
        file.write(tweet.text+'\n')
        file.write(str(analysis.sentiment)+'\n\n')
        print("")

file.close()
