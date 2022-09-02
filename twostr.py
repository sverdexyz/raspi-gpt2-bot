"""
Post a tweet to the Twitter and Nostr pipelines
Requires Twitter Developer API credentials as well as
Nostr Private key to an account
"""
import sys
from twitter_auth import authenticate

import time
from nostr.event import Event
from nostr.relay_manager import RelayManager
from nostr.message_type import ClientMessageType
from nostr.key import generate_private_key, get_public_key


MESSAGE = """Hello Twitter and Hello Nostr.
https://twitter.com/notifications
https://astral.ninja/f43c1f9bff677b8f27b602725ea0ad51af221344f69a6b352a74991a4479bac3
"""

if __name__ == "__main__":
    #Authenticate Twitter
    tw_auth = authenticate(sys.argv[1])
    print(auth)

    #Authenticate Nostr
    
    #Tweet Twitter
    tw_auth.update_status(MESSAGE)
    #Tweet Nostr

