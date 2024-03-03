from typing import Final
from dotenv import load_dotenv
import os 


load_dotenv()

TOKEN: Final[str] = os.getenv("BOT_TOKEN")
print(TOKEN)
