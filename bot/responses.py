from constants import DEV_SERVERS
from time import sleep
import random


def get_response(user_input: str, username: str, server: str, channel: str, server_id: str) -> str:
    lowered: str = user_input.lower()
    if not server in DEV_SERVERS.values() or not server_id in DEV_SERVERS.keys():
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
