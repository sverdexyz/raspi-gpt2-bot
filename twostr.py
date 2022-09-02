"""
Post a tweet to the Twitter and Nostr pipelines
Requires Twitter Developer API credentials as well as
Nostr Private key to an account
"""
import sys, json, ssl
from twitter_auth import authenticate

import time
from nostr.nostr.event import Event
from nostr.nostr.relay_manager import RelayManager
from nostr.nostr.message_type import ClientMessageType
from nostr.nostr.key import generate_private_key, get_public_key


MESSAGE = """Hello Twitter and Hello Nostr.
https://twitter.com/manfromcastle
https://astral.ninja/f43c1f9bff677b8f27b602725ea0ad51af221344f69a6b352a74991a4479bac3
"""

def auth_nostr(creds_file):
    """
    return nostr private key from credentials file
    """
    with open(creds_file,'r') as f:
        keys = json.load(f)
    return keys    
        
def post_nostr(message, private_key):
    """
    Post event to Nostr given specific relays, and a given privatekey
    """
    relay_manager = RelayManager()
    relay_manager.add_relay("wss://nostr-pub.wellorder.net")
    relay_manager.add_relay("wss://relay.damus.io")
    relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE}) # NOTE: This disables ssl certificate verification
    time.sleep(1.25) # allow the connections to open
    
    #private_key = generate_private_key()
    public_key = get_public_key(private_key)

    event = Event(public_key, MESSAGE)
    event.sign(private_key)

    message = json.dumps([ClientMessageType.EVENT, event.to_json_object()])
    relay_manager.publish_message(message)
    time.sleep(1) # allow the messages to send
    
    relay_manager.close_connections()
    
if __name__ == "__main__":
    #Authenticate Twitter
    tw_auth = authenticate(sys.argv[1])
    print(tw_auth)
    
    #Tweet Twitter
    tw_auth.update_status(MESSAGE)

    #Authenticate Nostr
    keys = auth_nostr(sys.argv[2])
        
    #Tweet Nostr
    post_nostr(MESSAGE, keys['private'])
