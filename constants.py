from typing import Final
from dotenv import load_dotenv
import os 


load_dotenv()

TOKEN: Final[str] = os.getenv("BOT_TOKEN")
print(TOKEN)

DEV_SERVERS: set = {"1213920998965907636": "bots", "": "server bookmark"}
ALPHA_TEST_SERVERS: set = {}
