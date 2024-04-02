import discord
from discord import Message, Embed, Color
from discord.ext.commands import Context
from constants import NEKOWEB_INFO_EP, NEKOWEB_SITE_URL, NEKOWEB_SITE_SS
from datetime import datetime, timezone
from bot.utils import is_url_exists
import requests


# TODO: use dictionary to get embed value and opts from name for ex: "id or username or title" as key
# field_map_key: {name: 'lol', inline: True/False}
# curf = field_map['field_map_key']
# embed.add_field(name=curf['name'], value=f"{data['key']}", inline=curf['inline'])

# THIS DICTS KEYS ARE SEQUENCE SENSITIVE
field_map = {
"id":          {'name': "", 'inline': True},
"username":    {'name': "", 'inline': True},
"title":       {'name': "", 'inline': True},
"description": {'name': "", 'inline': True}, 
"note":        {'name': "", 'inline': True}, 

"followers":   {'name': "", 'inline': True},
"views":       {'name': "", 'inline': True},
"hits":        {'name': "", 'inline': True},
"updates":     {'name': "", 'inline': True},

"created_at":  {'name': "", 'inline': True},
"updated_at":  {'name': "", 'inline': True},
"domain":      {'name': "", 'inline': True},
"thumbnail":   {'name': "", 'inline': True},
}

async def create_site_profile_embed(data: dict, username: str, ctx: Context) -> Embed:
    embed: Embed = Embed(
        title=f"{username}", 
        description=f"site info of {username} on nekoweb", timestamp=datetime.now(), 
        # color=discord.Color.dark_green()
        color='#'
    )

    embed.set_image(url=NEKOWEB_SITE_SS.replace("<site>", username))
    
    embed.add_field(name="id:", value=f"{data['id']}", inline=True)
    embed.add_field(name="Username:", value=f"{data['username']}", inline=True)
    embed.add_field(name="Title:", value=f"{data['title']}", inline=True)

    # custom config data
    # if 'thumbnail' in config:
    #     embed.set_thumbnail(url=config['thumbnail'])
    # if 'description' in config:
    #     embed.add_field(name="Description:", value=f"{config['description']}", inline=True)
        
    # embed.add_field(name="\t", value="\t", inline=True)
    
    embed.add_field(name="Followers:", value=f"{data['followers']}", inline=True)
    embed.add_field(name=f"Views:", value=f"{data['views']}", inline=True)
    embed.add_field(name="Updates:", value=f"{data['updates']}", inline=True)
    
    embed.add_field(name="Created at:", 
                         value=f"{datetime.fromtimestamp(data['created_at'] / 1000.0, tz=timezone.utc)}", 
                         inline=False)
    
    embed.set_footer(text=f"{username}'s site info")
    
    return embed


async def create_webring_index_embed(data: dict, webring: str, ctx: Context) -> Embed:
    embed: Embed = Embed(
        title=f"Members index of {webring}", 
        description=f"Index of members of {webring}", timestamp=datetime.utcnow(), 
        color=discord.Color.dark_blue()
    )
    
    # TODO: complete this functionality
