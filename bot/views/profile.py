import discord
from discord import Message, Embed, Color
from discord.ext.commands import Context
from constants import NEKOWEB_INFO_EP
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
    

    
    embed.add_field(name="id:", value=f"{data['id']}", inline=True)
    embed.add_field(name="Username:", value=f"{data['username']}", inline=True)
    embed.add_field(name="Title:", value=f"{data['title']}", inline=True)
    # embed.add_field(name="\t", value="\t", inline=True)
    
    embed.add_field(name="Followers:", value=f"{data['followers']}", inline=True)
    embed.add_field(name="Views:", value=f"{data['views']}", inline=True)
    embed.add_field(name="Updates:", value=f"{data['updates']}", inline=True)
    
    embed.add_field(name="Created at:", 
                         value=f"{datetime.fromtimestamp(data['created_at'] / 1000.0, tz=timezone.utc)}", 
                         inline=False)
    
    embed.set_footer(text=f"{username}'s site info")
    
    return embed



