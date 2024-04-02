from typing import Final
from dotenv import load_dotenv
import os 


load_dotenv()


TOKEN: Final[str] = os.getenv("BOT_TOKEN")
    # print(TOKEN)

# Servers
DEV_SERVERS: set = {"1213920998965907636": "bots", "": "server bookmark"}
ALPHA_TEST_SERVERS: set = {"00000000000": "nekowebring"}

# hosts
NEKOWEB = "nekoweb"
NEOCITIES = "neocities"

# Endpoints and urls
NEKOWEB_INFO_EP = "https://nekoweb.org/api/site/info/<uname>"
NEKOWEB_SITE_URL = "https://<site>.nekoweb.org"
NEKOWEB_SITE_SS = "https://nekoweb.org/screenshots/<site>/index_large.jpg"

NEOCITIES_INFO_EP = "https://neocities.org/api/info?sitename=<uname>"
NEOCITIES_SITE_URL = "https://<site>.neocities.org"


# NENE
NENE_CONFIG_PATH = 'configs/nene.json'
NENE_CONFIG_ALLOWED_PARAMS = [
    "title", "note", "color", "description", 
    "thumbnail", "tags", "webrings",
]