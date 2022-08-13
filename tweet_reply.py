#Reply to tweet based on search term

import tweepy

from config import LIKE
import time

from keys import keys
from timer import countdown

API_KEY = keys['api_key']
API_SECRET = keys['api_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

USER_NAME = keys['user_name']

OPENSEA_LINK = keys['opensea_link_meow']

auth = tweepy.OAuthHandler(API_KEY,API_SECRET) #api key and secret
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET) #access token and secret
api = tweepy.API(auth, wait_on_rate_limit=True) # tweeky removed 'wait_on_rate_limit_notify=True' parameter

#screen_name = "TheArtOfFreedom"
user = api.get_user(screen_name=USER_NAME) #actually the screen_name is the Twitter username without the @

tweet_query = "'drop it' OR 'drop' OR 'drop your unsold' OR 'sold' 'nft'"

public_tweets = api.search_tweets(q=tweet_query) #api.home_timeline()
nrTweets = 900

replied = []

#print(public_tweets[0].id)
#print(public_tweets[0].user.screen_name, " said: ","'", public_tweets[0].text,"'" " at ", public_tweets[0].created_at)

#print("""🐱 Awesome! 
#👇 check this out 🧡""", OPENSEA_LINK)

my_reply = (f"""
            ✊ Let us all UNITE!  
            ❤🖤 You have to check THIS out 👇 
            {OPENSEA_LINK}
            """)

while True:
    for tweet in tweepy.Cursor(api.search_tweets, tweet_query, result_type='recent', lang="en").items(nrTweets):
        try:
            if tweet.id not in replied:
                api.update_status(status=my_reply, in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)

                print("replied: ", my_reply, ", to ", tweet.user.screen_name, "'s "  'tweet, with ID: ', tweet.id)

                print("""
                        > S L E E P I N G <
                        for 90 seconds
                        . . . . . . . . .
                        """)
                countdown(90)

                replied.append(tweet.id)
                print(f"Tweet with ID:{tweet.id} has been added to known IDs array")
                countdown(3)

        except StopIteration:
            break
        except tweepy.errors.TweepyException as e:
            print(e)


