from twitter import Twitter, OAuth
import tweepy

API_KEY = 'K0jSV4Y344tjaDIhnPMvMXcdS'
API_SECRET = 'eKVkaa1XPsHWUeEwCEdKSVxXsppLNy4w9pAjRbaUFUxOHKqU7C'
ACCESS_TOKEN = '2974951531-VNDr97JIjxSsNpIsTvhQsJqpOKBeXOdGESW7qjv'
ACCESS_TOKEN_SECRET = 'LjpuABZxi3wZfNTjMg98Im7Iof0U8l9GnYYUf8snCTSNO'

twitter_oauth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter(auth=twitter_oauth)

oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(oauth)
