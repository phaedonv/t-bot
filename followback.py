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

#for follower in tweepy.Cursor(api.get_followers).items():
    #follower.follow()
#    print(follower.name + "         followed back")
#    time.sleep(21)

followers = tweepy.Cursor(api.get_followers).items()
friends = tweepy.Cursor(api.get_friends).items()

for f in followers:
    if f not in friends:
        #print(f)
        print("Follow back   " + f.name)
        f.follow()
        time.sleep(10)
    else:
        continue