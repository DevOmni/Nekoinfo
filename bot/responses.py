from time import sleep
import random


def get_response(user_input: str, username: str, server: str, channel: str) -> str:
    lowered: str = user_input.lower()
    if server != "server bookmark":
        if lowered == '':
            return "perhaps ~\n\tsilence..."
        elif any(greet in lowered for greet in ['hey', 'yo', 'acha', 'hemlo', 'hello', 'hi', 'hemloo', 'hemllo']):
            sleep(0.1)
            return "indeed ~"
        elif lowered == 'link~':
            return "https://discord.com/api/oauth2/authorize?client_id=1209585590333345853&permissions=1377342586080&scope=bot"
    else:
        if username in ['sanji_074#0000', 'dpsc7777', 'anonymous_1301', 'tensioniseverywhere_55923'] and \
               4.55 <= random.uniform(0.0, 10.0) <= 5.55:
            return "indeed ~"
    return ''
