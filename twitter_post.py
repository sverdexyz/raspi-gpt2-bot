#!/usr/bin/env python
import tweepy
import sys
import json
import time
import numpy as np
import datetime
import random
import datetime
import random

from twitter_auth import authenticate
from itertools import cycle
from itertools import cycle

from gpt2_client import GPT2Client
gpt2 = GPT2Client('345M') # This could also be `345M`, `774M`, or `1558M`                 



def reply_indefinitely_to_users(api,filename):
    """
    Cycle through a list of Twitter usernames and reply to their last tweet, indefinitely
    """
    file1 = open(filename, 'r')
    userlist = file1.readlines()
    random.shuffle(userlist)
    for user in cycle(userlist):
        print(user)
        try:
            get_last_tweet_and_reply(api,user)
        except:
            print("User %s failed"% user)

def get_last_tweet_and_reply(api,username):
    """
    Get last tweet for a specific user and reply
    """
    tweet = api.user_timeline(id = username, count = 1)[0]
    print(tweet.text)
    reply_to_specific_tweet(api,username,tweet.id, tweet.text)

def get_clean_tweet(generated_text):
    """
    Split GPT2 outputs on separator and look for short tweets
    """
    # Parse out all "sentences" by splitting on "\n———————\n"
    [print(p+"\n") for p in generated_text]
    #split_text = "".join(generated_text).split(["\n","<|endoftext|>"])[0]
    #print(split_text)
    # Filter out all examples which are longer than 140 characters
    valid_tweets = [x for x in generated_text
                    if (len(x) <= 200) and (len(x) > 20)]
    print("valid_tweets_______",valid_tweets)
    if valid_tweets:
        return np.random.choice(valid_tweets)
    else:
        return np.random.choice(generated_text)[0:200]

def reply_to_specific_tweet(api,username,tweetId, text):
    """
    Respond to a specific user's input by GPT-2 provided response
    """
    #Invoke GPT2 to formulate a reply
    print("Start generation %s, text %s" % (datetime.datetime.now(), text))
    reply = gpt2.generate_batch_from_prompts([text])
    print("end generation %s, reply %s" % (datetime.datetime.now(), reply))
    print("cleaned first reply under 140 characters %s" %
          get_clean_tweet(reply))
    #WARNING
    #update_status is live tweeting, do it too often or
    #tag famous people and you gonna get shutdown
    #WARNING
    api.update_status( get_clean_tweet(reply),
                      in_reply_to_status_id=tweetId,
                      auto_populate_reply_metadata=True)
        

if __name__ == "__main__":
    """
    Grab a list of usernames and cycle through it and reply to latest tweets of users
    python3 twitter_post.py twitter.json alex_friends.txt
    """
    auth = authenticate(sys.argv[1])

    #Cycle through a list of users and keep replying forever and ever
    reply_indefinitely_to_users(auth,sys.argv[2])