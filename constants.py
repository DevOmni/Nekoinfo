from typing import Final
from dotenv import load_dotenv
import os 


load_dotenv()


TOKEN: Final[str] = os.getenv("BOT_TOKEN")
    # print(TOKEN)

# Servers
DEV_SERVERS: set = {"1213920998965907636": "bots", "": "server bookmark"}
ALPHA_TEST_SERVERS: set = {"00000000000": "nekowebring"}

# Endpoints and urls
NEKOWEB_INFO_EP = "https://nekoweb.org/api/site/info"
NEKOWEB_SITE_URL = "https://<site>.nekoweb.org/"
