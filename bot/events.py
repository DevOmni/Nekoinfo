from discord import Message
from . import bot
from .responses import get_response

#MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    try:
        response: str = get_response(user_message, str(message.author), message.guild.name, str(message.channel), message.guild.id)
        if response:
            await message.channel.send(response)
    except Exception as e:
        print(f"Some error occurred!\n{e}")


@bot.event
async def on_ready() -> None:
    print(f"\033[96m{bot.user}\033[00m is\033[92m ONLINE! \033[00m")

"""
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    server: str = str(message.guild.name)
    server_id: str = str(message.guild.id)

    print(f'[{server}:{server_id}][{channel}]  {username}: "{user_message}"')
    await send_message(message, user_message)
"""


@bot.command()
async def info(ctx):
    return 

