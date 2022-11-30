#!/usr/bin/env python
import tweepy
import sys
import json
import time
import numpy as np
import datetime
import random

from twitter_auth import authenticate
from itertools import cycle

from gpt2_client import GPT2Client
gpt2 = GPT2Client('345M') # This could also be `345M`, `774M`, or `1558M`                 

TEST_TEXT ="""
reply  — 성상형 이아 (@Nam_Gan) May 22, 2016
The first part of the concept and the story of the "E" concept is about the story of the "E" as a whole, the meaning of the "E" and the feelings of it. It is also about the "E" concept's relationship with "E", the emotions of it as a whole and how it relates to the world. The second part of the concept is about the story of the "E" as a whole, the meaning of the "E" and the feelings of it. It is also about the "E" concept's relationship with "E", the emotions of it as a whole and how it relates to the world.
The concept of "E" as a whole is about the "E" as a whole. It is the essence of everything. It is a world and a universe.
This concept is about the "E" concept's relationship with "E", the emotions of it as a whole and how it relates to the world.
The world and the universe are all just manifestations of the essence of "E". The essence of "E" as a whole is the essence of everything .
In order to understand the concept of "E", it is necessary to understand the "E" concept's relation to "E". The essence of "E" as a whole is the essence of everything.
A world is a collection of ideas that exist. What is the essence of the world?
A universe is a collection of ideas that exist. What is the essence of the universe?
The essence of "E" as a whole is the essence of everything.
The essence of "E" as a whole is the essence of everything.
This is the essence of the universe, the essence of everything, the essence of everything.
"E" as a whole is an "E" concept.
The essence of "E" as a whole is the essence of everything .
The essence of "E" as a whole is the essence of everything.
The essence of "E" as a whole is the essence of everything.
This is the essence of the universe, the essence of everything, the essence of everything.
"E" as a whole is the essence of everything.
"E" as a whole is the essence of everything.
"E" as a whole is the essence of everything.
This
"""


USA_GEO_CODE=23424977

def get_trends(api):
    """
    Get trends in USA
    """
    trends1 = api.trends_place(USA_GEO_CODE)
    trends = set([trend['name'] for trend in trends1[0]['trends']
                  if "#" in trend['name']])
    print(trends)

def home_timeline(api, retweet_cnt=10):
    """
    Show popular home timeline tweets
    """

    #Test text splitting
    print(get_clean_tweet(TEST_TEXT))
    #tweets = api.home_timeline()
    tweets = tweepy.Cursor(api.search, q="USA",
                           result_type="popular",
                           lang="en").items(50)
    
    for tweet in tweets:
        print('{retweets} {real_name} (@{name}) said {tweet}\n\n'.format(
            real_name=tweet.author.name,
            name=tweet.author.screen_name,
            tweet=tweet.text,
            retweets=tweet.retweet_count))
        #only respond to retweeted tweets
        #if tweet.retweet_count > retweet_cnt:
        #    try:
        reply_to_specific_tweet(
            api,tweet.author.screen_name,
            tweet.id, tweet.text)
            #except:
             #   print("Failed reply to %s- %s" %
             #         (tweet.author.screen_name,tweet.text))

def reply_indefinitely_to_users(api,filename):
    """
    Cycle through a list of Twitter usernames and reply to their last tweet, indefinitely
    """
    file1 = open(filename, 'r')
    userlist = file1.readlines()
    random.shuffle(userlist)
    for user in cycle(userlist):
        print(user)
        get_last_tweet_and_reply(api,user)

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
                    if (len(x) <= 280) and (len(x) > 20)]
    print("valid_tweets_______",valid_tweets)
    if valid_tweets:
        return np.random.choice(valid_tweets)
    else:
        return np.random.choice(generated_text)[0:240]

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
    api.update_status("@%s %s" % (username, get_clean_tweet(reply)),
                      in_reply_to_status_id=tweetId,
                      auto_populate_reply_metadata=True)
        
def find_tweets(api):
    """
    Find tweets we want
    """
    
    twts = api.search(q="Hello World!")

    #list of specific strings we want to check for in Tweets
    t = ['Hello world!',
         'Hello World!',
         'Hello World!!!',
         'Hello world!!!',
         'Hello, world!',
         'Hello, World!']
    return twts, t


def reply_tweet(api,twt, t):
    """
    Reply to tweets
    """

    for s in twt:
        for i in t:
            if i in s.text:
                print(i,s.text)
                sn = s.user.screen_name
                print(sn, i, s.text)
                m = "@%s Hello!" % (sn)
                s = api.update_status(m, s.id)
                time.sleep(10)
                
if __name__ == "__main__":
    """
    Grab a list of usernames and cycle through it and reply to latest tweets of users
    python3 twitter_post.py twitter.json alex_friends.txt
    """
    auth = authenticate(sys.argv[1])

    #Cycle through a list of users and keep replying forever and ever
    reply_indefinitely_to_users(auth,sys.argv[2])