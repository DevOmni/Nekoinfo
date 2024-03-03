from discord.ext import commands
from discord import Intents, Message, Client
from typing import Final
from bot.responses import get_response

#BOT INVITE LINK: https://discord.com/oauth2/authorize?client_id=1213832039069917206&permissions=964223589440&scope=bot

#SETUP BOT
# intent: Intents = Intents.default()
# intent.members = True  # NOQA
# intent.message_content = True  # NOQA <- no quotation (removes sqwigly lines)

intent: Intents = Intents.all()
bot: commands.Bot  = commands.Bot(command_prefix="~", intents=intent)
