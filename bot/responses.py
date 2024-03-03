from constants import DEV_SERVERS, ALPHA_TEST_SERVERS
from time import sleep
import random


PRIOR_SERVERS_ID: list = []
PRIOR_SERVERS_NAME: list = []
for s in [DEV_SERVERS, ALPHA_TEST_SERVERS]:
    PRIOR_SERVERS_ID.extend(s)    
    PRIOR_SERVERS_NAME.extend(s.values())
  

def get_response(user_input: str, username: str, server: str, channel: str, server_id: str) -> str:
    lowered: str = user_input.lower()
    if not server in PRIOR_SERVERS_NAME or not server_id in PRIOR_SERVERS_ID:
        return ""
    else:
        if lowered == '':
            return "perhaps ~\n\tsilence..."
        elif any(greet in lowered for greet in ['hey', 'yo', 'acha', 'hemlo', 'hello', 'hi', 'hemloo', 'hemllo']):
            sleep(0.1)
            return "indeed ~"
        elif lowered == 'link~':
            return "https://discord.com/oauth2/authorize?client_id=1213832039069917206&permissions=964223589440&scope=bot"
    return ''
