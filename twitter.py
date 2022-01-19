import tweepy
import time

auth = tweepy.OAuthHandler('um9hhsV5iFlPj1NqRAumVh2hV','RWlyxfNamrI0TygS3ou4FVUpWCSNEFK4h65IRmVucKUU7J0jRQ') #api key and secret

auth.set_access_token('1469326097607278600-6HUXDVhE4muKSAd0vQ62943BwpM3Lm','4cPX8fB6w9zuT1Ojud9uhWtIs5Pksps5Dzjso1fQh09ak') #access token and secret

api = tweepy.API(auth, wait_on_rate_limit=True) # tweeky removed 'wait_on_rate_limit_notify=True' parameter

#screen_name = "TheArtOfFreedom"
user = api.get_user(screen_name='ArtOFreedom_NFT') #actually the screen_name is the Twitter username without the @

#print('name: ' + user.screen_name + ' :: ' + 'ID: ' + str(user.id))

#for follower in tweepy.Cursor(api.get_followers).items():
#    print(follower.name)

search_term = 'NFT'
nrTweets = 500

for tweet in tweepy.Cursor(api.search_tweets, search_term).items(nrTweets):
    try:
        tweet.favorite()
        print('Tweet Liked')
        time.sleep(10)
    #except tweepy.errors.TweepError as e:
        #print(e.reason)
    except StopIteration:
        break     