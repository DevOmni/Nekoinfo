from typing import Final
from dotenv import load_dotenv
import os 


load_dotenv()


TOKEN: Final[str] = os.getenv("BOT_TOKEN")
    # print(TOKEN)

# Servers
DEV_SERVERS: set = {"1213920998965907636": "bots", "": "server bookmark"}
ALPHA_TEST_SERVERS: set = {"00000000000": "nekowebring"}

# hosts
NEKOWEB: str = "nekoweb"
NEOCITIES: str = "neocities"

# Endpoints and urls
NEKOWEB_INFO_EP: str = "https://nekoweb.org/api/site/info/<uname>"
NEKOWEB_SITE_URL: str = "https://<site>.nekoweb.org"
NEKOWEB_SITE_SS: str = "https://nekoweb.org/screenshots/<site>/index_large.jpg"

NEOCITIES_INFO_EP: str = "https://neocities.org/api/info?sitename=<uname>"
NEOCITIES_SITE_URL: str = "https://<site>.neocities.org"


# NENE
NENE_CONFIG_PATH: str = 'configs/nene.json'
NENE_CONFIG_ALLOWED_PARAMS: dict[str] = {
    "title":str, 
    "note":str, 
    "color":str, 
    "description":str, 
    "thumbnail":str, 
    
    "tags":list, 
    "webrings":list,
}

ALL_FIELDS: list[str] = [
    "id",
    "username",
    "title",
    "description", 
    "note", 
    "followers",
    "views",
    "hits",
    "domain",
    "updates",
    "created_at",
    "updated_at",
    "color", 
    "tags", 
    "webrings",
    "thumbnail", 
]

ALL_FIELDS_AS_VALUES: list[str] = [
    "id",
    "username",
    "title",
    "description", 
    "note", 

    "followers",
    "views",
    "hits",
    "domain",

    "updates",
    "created_at",
    "updated_at",
    "thumbnail",
]

ALL_LIST_VALUED_FIELDS: list[str] = [ 
    "tags", 
    "webrings",
]

FIELD_MAP: dict[str:dict[str:dict|str]] = {
"thumbnail":   { 'kwargs': {}, 'type': 'thumb'},
"id":          { 'kwargs': {'name': "ID:",              'inline': True}},
"username":    { 'kwargs': {'name': "Username:",        'inline': True}},
"title":       { 'kwargs': {'name': "Title:",           'inline': True}},
"description": { 'kwargs': {'name': "Description:",     'inline': True}}, 
"note":        { 'kwargs': {'name': "Note:",            'inline': True}}, 

"followers":   { 'kwargs': {'name': "Followers:",       'inline': True}},
"views":       { 'kwargs': {'name': "Views:",           'inline': True}},
"hits":        { 'kwargs': {'name': "Hits:",            'inline': True}},
"updates":     { 'kwargs': {'name': "Updates:",         'inline': True}},

"created_at":  { 
    'kwargs': {'name': "Created at:", 'inline': True}, 
    'type': 'date'
},
"updated_at":  { 
    'kwargs': {'name': "Last Updated at:", 'inline': True}, 
    'type': 'date'
},
"domain":      { 'kwargs': {'name': "Domain:", 'inline': True}},

"webrings":      { 
    'kwargs': {'name': "Webrings:", 'inline': True},
    'type': 'list'
},
"tags":      { 
    'kwargs': {'name': "Tags:", 'inline': True},
    'type': 'list'
},
}