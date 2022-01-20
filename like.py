#favorite tweet based on search term

from tkinter import N
from turtle import end_fill
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

search_term = 'nft' or '#nft' or 'nftartwork' or 'nftcommunity' or 'cryptoart'
nrTweets = 500
        
for tweet in tweepy.Cursor(api.search_tweets, search_term, result_type='recent', lang="en").items(nrTweets):
    try:
        tweet.favorite()

        #I have to find a way to print the name of the user that tweeted.. 
        #entities example: entities = {'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'BrettLeeWEB3', 'name': 'Brett Lee ♤', 'id': 1448190946688991234, 'id_str': '1448190946688991234', 'indices': [3, 16]}], 'urls': []}
        
        #print(tweet.entities[user_mentions]([name]))
        print('  Tweet ',tweet.id, ' Liked')
        time.sleep(10)
    #except tweepy.errors.TweepError as e:
        #print(e.reason)
    except StopIteration:
        break  