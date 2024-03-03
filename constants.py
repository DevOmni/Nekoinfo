from dotenv import load_dotenv
import os 


load_dotenv()

TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
# print(TOKEN)
