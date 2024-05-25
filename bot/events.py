import enum
import discord
from discord import Message, Embed, Color
from discord.ext import commands
from discord.ext.commands import Context
from discord import app_commands

# this bit is a hack for the current situation of `HelpCommand.context` being a ContextVar
# from discord.ext.commands.help import _context as HELP_COMMAND_CONTEXT_HACK
# end hack

from constants import NEKOWEB, NEOCITIES, USAGE_CONTENT
from bot import bot, logger
from bot.responses import get_response
from bot.utils import get_site_info, get_config, is_url_exists
from bot.views.embeds import create_site_profile_embed, create_site_profile_embed_dynamic, create_webring_index_embed


from datetime import datetime, timezone
from typing import Literal, Union, NamedTuple


def is_me():
    def predicate(ctx):
        # print(ctx.author.id)
        return ctx.author.id in [1189802691484983339, 549907435478056971]
    return commands.check(predicate)


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
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(application_id=bot.application_id, type=discord.ActivityType.playing, name="Dead"))  # discord.Game("FINDING ONE PIECE")
    await bot.tree.sync()  # sync slash commands
    # await bot.add_cog(Usage(bot=bot))
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


@bot.hybrid_command(name="ping", description="pongs back when pinged")
async def ping(interaction: discord.Integration):
    await interaction.reply(content=f"Pong! {round(bot.latency * 1000)}ms")


@bot.command(hidden=True)
@is_me()
async def leave(ctx: Context):
    await ctx.reply("see ya ~")
    await ctx.guild.leave()


@bot.command(name="sync", description="syncs the slash commands", aliases=['s'], hidden=True)
@is_me()
async def sync(interaction: discord.Integration):
    await bot.tree.sync()  # sync slash commands
    await interaction.reply(content=f"Synced! {round(bot.latency * 1000)}ms")


@bot.command(name="cfg", description="shows config", hidden=True)
@is_me()
async def cfg(interaction: discord.Integration, username: str, host: Literal[f'{NEKOWEB}', f'{NEOCITIES}']=NEKOWEB):
    await interaction.reply(content=f"## Config: \n```json\n{get_site_info(username, host)}\n```")
 
 

@bot.hybrid_command(name="wring", description="indexes the members of webring", enabled=True)
async def wring(interaction: discord.Integration, webring: str):
    # print(webring)
    embed = await create_webring_index_embed(webring=webring, ctx=interaction)
    await interaction.reply(embed=embed)
    # await interaction.reply(content="not implemented yet :/")


@bot.hybrid_command(name="join-date", description="shows the join date of the server member")
async def join_date(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.reply(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')


@bot.hybrid_command(name="info", description="Gives information about the site")
@app_commands.describe(username="username of the site on the host", host="host of user's site")
async def info(ctx: discord.Integration, username: str, host: Literal[f'{NEKOWEB}', f'{NEOCITIES}']=NEKOWEB):  # NOQA
    await ctx.typing()
    
    data, status = get_site_info(username, host)
    if str(status) != '200' or not len(data) > 0:
        await ctx.reply(f"## This site doesn't exists on {host}")
        print(log_msg := f"[{ctx.guild.name}|{ctx.channel.name}]  {ctx.author.name}: uname[{username}], host[{str(host)}]  SITE NOT FOUND")
        logger.debug(log_msg)
        return
    print(log_msg := f"[{ctx.guild.name}|{ctx.channel.name}]  {ctx.author.name}: uname[{username}], host[{str(host)}]")
    logger.debug(log_msg)
    # print(f"data: {data}")
    
    info_embed = await create_site_profile_embed_dynamic(data, username, ctx)
    
    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='Visit', style=discord.ButtonStyle.url, url=f"https://{username}.{host}.org/"))
    url_view.add_item(discord.ui.Button(label='Report', style=discord.ButtonStyle.danger))
    await ctx.reply(embed=info_embed, view=url_view)


@bot.hybrid_command(name="help", description="Outputs usage of this bot's commands")
async def help( ctx: discord.Integration):
    await ctx.reply(USAGE_CONTENT)
    