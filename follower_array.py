#append followers in an array

import tweepy
import time

auth = tweepy.OAuthHandler('um9hhsV5iFlPj1NqRAumVh2hV','RWlyxfNamrI0TygS3ou4FVUpWCSNEFK4h65IRmVucKUU7J0jRQ') #api key and secret

auth.set_access_token('1469326097607278600-6HUXDVhE4muKSAd0vQ62943BwpM3Lm','4cPX8fB6w9zuT1Ojud9uhWtIs5Pksps5Dzjso1fQh09ak') #access token and secret

api = tweepy.API(auth, wait_on_rate_limit=True) # tweeky removed 'wait_on_rate_limit_notify=True' parameter

followers = []

for follower in tweepy.Cursor(api.get_followers).items():
    followers.append(follower.name)
    time.sleep(0)

print(ids[0])