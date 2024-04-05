import discord
from discord import Message, Embed, Color
from discord.ext.commands import Context

from constants import NEKOWEB_INFO_EP, NEKOWEB_SITE_URL, NEKOWEB_SITE_SS, FIELD_MAP, ALL_LIST_VALUED_FIELDS, NEKOWEB, NEOCITIES
from bot.utils import is_url_exists

from datetime import datetime, timezone
import requests


# TODO: use dictionary to get embed value and opts from name for ex: "id or username or title" as key
# field_map_key: {name: 'lol', inline: True/False}
# curf = field_map['field_map_key']
# embed.add_field(name=curf['name'], value=f"{data['key']}", inline=curf['inline'])

# THIS DICTS KEYS ARE SEQUENCE SENSITIVE
# FIELD_MAP


async def create_site_profile_embed(data: dict, username: str, ctx: Context) -> Embed:
    embed: Embed = Embed(
        title=f"{username}", 
        description=f"site info of {username} on {data['host']}", timestamp=datetime.now(), 
        color=Color.from_str('#0000FF')
    )

    print('embed color:', discord.Color.blue)

    embed.set_image(url=NEKOWEB_SITE_SS.replace("<site>", username))
    
    embed.add_field(name="id:", value=f"{data['id']}", inline=True)
    embed.add_field(name="Username:", value=f"{data['username']}", inline=True)
    embed.add_field(name="Title:", value=f"{data['title']}", inline=True)
        
    # embed.add_field(name="\t", value="\t", inline=True)
    
    embed.add_field(name="Followers:", value=f"{data['followers']}", inline=True)
    embed.add_field(name=f"Views:", value=f"{data['views']}", inline=True)
    embed.add_field(name="Updates:", value=f"{data['updates']}", inline=True)
    
    embed.add_field(name="Created at:", 
                         value=f"{datetime.fromtimestamp(data['created_at'] / 1000.0, tz=timezone.utc).strftime('%#d %b %Y %H:%M:%S')}", 
                         inline=False)
    
    embed.set_footer(text=f"{username}'s site info")
    
    return embed

async def create_site_profile_embed_dynamic(data: dict, username: str, ctx: Context) -> Embed:
    print('dynamic info embed')
    embed: Embed = Embed(
        title=f"{username}", 
        description=f"site info of {username} on {data['host']}", 
        timestamp=datetime.now(), 
        color=(Color.from_str(data['color']) if 'color' in data else discord.Color.random())
    )
    if data['host'] == NEKOWEB:
        embed.set_image(url=NEKOWEB_SITE_SS.replace("<site>", username))

    for field in FIELD_MAP:
        if not field in data: continue;
        field_dict = FIELD_MAP[field]
        # print('field:', field, f'\n {data[field]}')
        
        if 'type' in field_dict and field_dict['type'] == 'thumb':
            embed.set_thumbnail(url=data[field], **field_dict['kwargs'])       
            embed.set_image(url=data[field], **field_dict['kwargs'])       
        elif 'type' in field_dict and field_dict['type'] == 'date' and data['host'] == NEKOWEB:
            embed.add_field(
                value=f"{datetime.fromtimestamp(data[field] / 1000.0, tz=timezone.utc).strftime('%d %b %Y %H:%M:%S')}", 
                **field_dict['kwargs']
            )
        elif 'type' in field_dict and field_dict['type'] == 'list' and len(data[field]) > 0:
            print(data[field])
            embed.add_field(value=f"{', '.join(data[field])}", **field_dict['kwargs'])
        elif data[field]: 
            embed.add_field(value=f"{data[field]}", **field_dict['kwargs'])
        
    embed.set_footer(text=f"{username}'s site info")
    return embed


async def create_webring_index_embed(data: dict, webring: str, ctx: Context) -> Embed:
    embed: Embed = Embed(
        title=f"Members index of {webring}", 
        description=f"Index of members of {webring}", timestamp=datetime.utcnow(), 
        color=discord.Color.dark_blue()
    )
    
    # TODO: complete this functionality
