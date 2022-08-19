#append followers in an array

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

followers = []

for follower in tweepy.Cursor(api.get_followers).items():
    followers.append(follower.name)
    time.sleep(0)

print(followers[0])