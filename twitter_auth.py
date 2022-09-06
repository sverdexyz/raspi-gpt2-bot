import json
import tweepy

def authenticate(creds_file):
    """                                                                                                                           
    Authenticate using creds file                                                                                                 
    """
    with open(creds_file,'r') as f:
        keys = json.load(f)

    CONSUMER_KEY = keys['CONSUMER_KEY']
    CONSUMER_SECRET = keys['CONSUMER_SECRET']
    ACCESS_TOKEN = keys['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = keys['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

