#Reply to tweet based on search term

from config import LIKE

import tweepy
from keys import keys
import time

from timer import countdown
from colorama import Fore

API_KEY = keys['api_key']
API_SECRET = keys['api_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

USER_NAME = keys['user_name']

OPENSEA_LINK = keys['opensea_link']

auth = tweepy.OAuthHandler(API_KEY,API_SECRET) #api key and secret
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET) #access token and secret
api = tweepy.API(auth, wait_on_rate_limit=True) # tweeky removed 'wait_on_rate_limit_notify=True' parameter

#screen_name = "TheArtOfFreedom"
user = api.get_user(screen_name=USER_NAME) #actually the screen_name is the Twitter username without the @

tweet_query = "'drop it' OR 'drop' OR 'drop your unsold' OR 'sold' 'nft'"

public_tweets = api.search_tweets(q=tweet_query) #api.home_timeline()

# API.get_status(id, *, trim_user, include_my_retweet, include_entities, include_ext_alt_text, include_card_uri)

for status in api.user_timeline(since_id = '1556279461699395584'):
    print(status.id)

    print(Fore.LIGHTRED_EX + "...10 seconds before destruction...")
    countdown(10)

    #api.destroy_status(status.id)

