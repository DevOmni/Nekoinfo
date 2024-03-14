import discord
from discord import Message, Embed, Color
from discord.ext import commands
from discord.ext.commands import Context
from . import bot
from .responses import get_response
import requests
from constants import NEKOWEB_INFO_EP
from bot.views.profile import create_site_profile_embed
from datetime import datetime, timezone


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
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("chipi chipi chapa chapa"))
    await bot.tree.sync()  # sync slash commands
    print(f"\033[96m{bot.user}\033[00m is\033[92m ONLINE! \033[00m")


@bot.event
async def on_guild_join(guild):
    if guild.system_channel: # If it is not None
        await guild.system_channel.send(f'I\'m here ^-^')


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


# @bot.command()
# async def ping(ctx: Context):
#     await ctx.reply(f"pong {round(bot.latency * 1000)}ms")


@bot.hybrid_command(name="ping", description="pongs back when pinged")
async def ping(interaction: discord.Integration):
    await interaction.reply(content=f"Pong! {round(bot.latency * 1000)}ms")


# @bot.command()
# async def info(ctx: Context, username: str):
#     await ctx.typing()
    
#     res = requests.get(url=f"{NEKOWEB_INFO_EP}/{username}")
#     print(f"res: {res.status_code}")
    
#     if str(res.status_code) != '200' or not len(res.content) > 0:
#         await ctx.reply("This site doesn't exists on nekoweb")
#         return
#     data: dict = res.json()
#     print(f"data: {data}")
    
#     info_embed = await create_site_profile_embed(data, username, ctx)
#     await ctx.reply(content="~~well~~", embed=info_embed)

@bot.hybrid_command(name="info", description="Gives information about the site")
async def info(ctx: discord.Integration, username: str):
    await ctx.typing()
    
    res = requests.get(url=f"{NEKOWEB_INFO_EP}/{username}")
    print(f"res: {res.status_code}")
    
    if str(res.status_code) != '200' or not len(res.content) > 0:
        await ctx.reply("This site doesn't exists on nekoweb")
        return
    data: dict = res.json()
    print(f"data: {data}")
    
    info_embed = await create_site_profile_embed(data, username, ctx)
    await ctx.reply(embed=info_embed)


@bot.hybrid_command(name="webring", description="indexes the members of webring")
async def ping(interaction: discord.Integration, webring: str):
    # embed = await create_webring_index_embed()
    # await interaction.reply(Embed=embed)
    print(webring)
    await interaction.reply(content="not implemented yet :/")


@bot.command()
async def leave(ctx: Context):
    if not ctx.author.display_name in ["~", "max", "null"]:
        await ctx.reply("You don't have permission to do that!") 
    await ctx.reply("see ya ~")
    await ctx.guild.leave()


@bot.hybrid_command(name="join-date", description="shows the join date of the server member")
async def join_date(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.reply(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')
    # await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')

