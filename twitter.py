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

#print('name: ' + user.screen_name + ' :: ' + 'ID: ' + str(user.id)) #just testing ;)

#let's create a tweet!

tweet_text = 'Work in progress!'
media_nft = 'media/sound_of_da_police.png'

#status = api.update_status_with_media(tweet_text, media_nft)
#print(status)

#I have to find a way of getting the status-tweet IDs..
#The ID of last tweet is known : 1483865642285551620

#let's try to delete a tweet! 
ID = 1483865642285551620
api.destroy_status(ID)

try:
    api.get_status(ID)
except:
    print('The tweet has beed deleted😎')

   