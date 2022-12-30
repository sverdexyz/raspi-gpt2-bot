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
import time
#from gpt2_client import GPT2Client
#gpt2 = GPT2Client('345M') # This could also be `345M`, `774M`, or `1558M`                 

from aitextgen import aitextgen
ai = aitextgen(model="EleutherAI/gpt-neo-125M")


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
        except Exception as e:
            print("User %s failed, error %s"% (user, e))

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
    # First two hundred characters of first entry to get a whole sentence. 
    #Split on endoftext
    [print(p) for p in generated_text]
    firsttext = "".join(generated_text).split("/n")
    return np.random.choice(firsttext)[:220]
  

def reply_to_specific_tweet(api,username,tweetId, text):
    """
    Respond to a specific user's input by GPT-2 provided response
    """
    #Invoke GPT2 to formulate a reply
    print("Start generation %s, text %s" % (datetime.datetime.now(), text))
    #reply = gpt2.generate_batch_from_prompts([text])
    #delete first line as it ususally has lot of preamble text
    ascii_count=0
    counter = 0 
    #filter out messages with too much non-ASCII, liek crappy code
    while ascii_count < 260:
        reply = ai.generate_one(prompt=text, max_length=500, repetition_penalty=2.0).replace(text,"").split("\n")[1:]
        reply = " ".join(reply)
        print("end generation %s, reply %s" % (datetime.datetime.now(), reply))
        #WARNING
        #update_status is live tweeting, do it too often or
        #tag famous people and you gonna get shutdown
        #WARNING
        clean = reply[0:270]
        ascii_count = len(clean.encode("ascii", "ignore"))
        print("ascii count %s ", ascii_count)
        counter = counter+1
        if counter > 10:
            return
    print("enough ASCII tweeting")
    api.update_status( clean,
                      in_reply_to_status_id=tweetId,
                      auto_populate_reply_metadata=True)
    print("Tweeted waiting")
    time.sleep(300)
        

if __name__ == "__main__":
    """
    Grab a list of usernames and cycle through it and reply to latest tweets of users
    python3 twitter_post.py twitter.json alex_friends.txt
    """
    auth = authenticate(sys.argv[1])

    #Cycle through a list of users and keep replying forever and ever
    reply_indefinitely_to_users(auth,sys.argv[2])