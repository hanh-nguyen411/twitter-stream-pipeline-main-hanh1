import os
import tweepy

API_KEY = os.getenv('API_KEY', '')
API_SECRET = os.getenv('API_SECRET', '')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', '')
ACCESS_SECRET = os.getenv('ACCESS_SECRET', '')
BEARER_TOKEN = os.getenv('BEARER_TOKEN', '')


def auth_conf():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    return auth
