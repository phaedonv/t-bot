import tweepy
import time

auth = tweepy.OAuthHandler('v1wPEFI9mqKdvigCcqQta8kih','7QsAEtgPnxHyvAOi4DyfFN6fL9iO9uyZM3JsmxdnLGcZmojims')

auth.set_access_token('1469326097607278600-9Mt9WfptbOhNH6lASOWmv9NyDtYg54','GWeMQocAfY5u3rhfDPtEUJPTGa13oVm2TrlXeAtqCP2Rv')

api = tweepy.API(auth, wait_on_rate_limit=True) # tweeky removed 'wait_on_rate_limit_notify=True' parameter

#screen_name = "TheArtOfFreedom"
user = api.get_user(screen_name='ArtOFreedom_NFT') #actually the screen_name is the Twitter username without the @

#print('name: ' + user.screen_name + ' :: ' + 'ID: ' + str(user.id))

for follower in tweepy.Cursor(api.get_followers).items():
    print(follower.name)