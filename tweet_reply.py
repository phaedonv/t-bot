#Reply to tweet based on search term

from config import LIKE

import tweepy
from keys import keys
import time

API_KEY = keys['api_key']
API_SECRET = keys['api_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(API_KEY,API_SECRET) #api key and secret
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET) #access token and secret
api = tweepy.API(auth, wait_on_rate_limit=True) # tweeky removed 'wait_on_rate_limit_notify=True' parameter

#screen_name = "TheArtOfFreedom"
user = api.get_user(screen_name='ArtOFreedom_NFT') #actually the screen_name is the Twitter username without the @

tweet_query = "nft"

public_tweets = api.search_tweets(q=tweet_query) #api.home_timeline()
#print(public_tweets[0].id)
#print(public_tweets[0].user.screen_name, " said: ","'", public_tweets[0].text,"'" " at ", public_tweets[0].created_at)

my_reply = "Awesome!!"
nrTweets = 3

while True:
    for tweet in tweepy.Cursor(api.search_tweets, tweet_query, result_type='recent', lang="en").items(nrTweets):
        try:
            api.update_status(status=my_reply, in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)

            print("replied to ", tweet.user.screen_name, "'s "  'tweet, with ID: ', tweet.id)

            print("""
                    > S L E E P I N G <
                       for 10 seconds
                     . . . . . . . . .
                    """)
            time.sleep(10)

        except StopIteration:
            break
        except tweepy.errors.TweepyException as e:
            print(e)


