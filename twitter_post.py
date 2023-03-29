#!/usr/bin/env python
import openai
import tweepy
import sys
import json
import time
import numpy as np
import datetime
import random
import datetime
import random
import re


from twitter_auth import authenticate
from itertools import cycle
from itertools import cycle
import time
#from gpt2_client import GPT2Client
#gpt2 = GPT2Client('345M') # This could also be `345M`, `774M`, or `1558M`                 



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
  

def wait_random_time():
    wait_time = random.uniform(5 * 60, 10 * 60) # generate random number between 2 and 5 minutes in seconds
    time.sleep(wait_time) # wait for the generated amount of time


import requests
import json
import datetime

# Read GPT-3 API key from a file
with open("../gpt3_api_key.txt", "r") as key_file:
    api_key = key_file.read().strip()

def reply_to_specific_tweet(api, username, tweetId, text):
    """
    Respond to a specific user's input by GPT-3.5-turbo provided response
    """
    # Invoke GPT-3.5-turbo to formulate a reply
    print("Start generation %s, text %s" % (datetime.datetime.now(), text))

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    chat_messages = [
        #{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text + ". In your response make sure, you DO NOT refer to yourself as an AI \
        generative model or language model. Furthermore make sure response is SHORTER than 240 characters. NEVER refer \
        to yourself as As an AI language model. Remember your response should sound like you are an internet \
        cryptocurrency enthusiast adopting an uplifting tone"}
    ]
 

    data = {
        "model": "gpt-3.5-turbo",
        "messages": chat_messages,
        "max_tokens": 200,
        "n": 1,
        "stop": None,
        "temperature": 0.8,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    response = requests.post("https://api.openai.com/v1/chat/completions",
                          headers=headers, data=json.dumps(data))
    response_json = response.json()
    print(response_json)
    reply = response_json["choices"][0]["message"]["content"].strip().replace(text, "")
    print("end generation %s, reply %s" % (datetime.datetime.now(), reply))


  # Update status without uploading an image
    api.update_status(reply,
                      in_reply_to_status_id=tweetId,
                      auto_populate_reply_metadata=True)
    print("Tweeted waiting")
    wait_random_time()

if __name__ == "__main__":
    """
    Grab a list of usernames and cycle through it and reply to latest tweets of users
    python3 twitter_post.py twitter.json alex_friends.txt
    """
    auth = authenticate(sys.argv[1])

    #Cycle through a list of users and keep replying forever and ever
    reply_indefinitely_to_users(auth,sys.argv[2])
