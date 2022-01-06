import tweepy
import time

auth = tweepy.OAuthHandler('v1wPEFI9mqKdvigCcqQta8kih','7QsAEtgPnxHyvAOi4DyfFN6fL9iO9uyZM3JsmxdnLGcZmojims')

auth.set_access_token('1469326097607278600-9Mt9WfptbOhNH6lASOWmv9NyDtYg54','GWeMQocAfY5u3rhfDPtEUJPTGa13oVm2TrlXeAtqCP2Rv')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


