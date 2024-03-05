import discord
from discord import Message, Embed, Color
from discord.ext.commands import Context
from constants import NEKOWEB_INFO_EP, NEKOWEB_SITE_URL, NEKOWEB_SITE_SS
from datetime import datetime, timezone
import requests


def is_url_exists(url: str) -> bool:
    r = requests.head(url)
    return r.status_code == 200


async def create_site_profile_embed(data: dict, username: str, ctx: Context) -> Embed:
    embed: Embed = Embed(
        title=f"Site info of {username}", 
        description=f"Information of site of {username} on nekoweb", timestamp=datetime.utcnow(), 
        color=discord.Color.dark_green()
    )

    embed.set_image(url=NEKOWEB_SITE_SS.replace("<site>", username))
    
    embed.add_field(name="id:", value=f"{data['id']}", inline=True)
    embed.add_field(name="Username:", value=f"{data['username']}", inline=True)
    embed.add_field(name="Title:", value=f"{data['title']}", inline=True)
    
    if is_url_exists(config := f'{NEKOWEB_SITE_URL.replace("<site>", username)}/nene/config.json'):
        config = requests.get(config).json()
        if 'thumbnail' in config:
            embed.set_thumbnail(url=config['thumbnail'])
        if 'description' in config:
            embed.add_field(name="Description:", value=f"{config['description']}", inline=True)
        
    # embed.add_field(name="\t", value="\t", inline=True)
    
    embed.add_field(name="Followers:", value=f"{data['followers']}", inline=True)
    embed.add_field(name="Views:", value=f"{data['views']}", inline=True)
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
