import requests
from constants import NEKOWEB_INFO_EP, NEOCITIES_INFO_EP, NEKOWEB, NEOCITIES, NEKOWEB_SITE_URL, NEOCITIES_SITE_URL, NENE_CONFIG_PATH, NENE_CONFIG_ALLOWED_PARAMS


# SELECT AND GET SITE URL FROM USERNAME AND HOST
def get_site(username: str, host: str) -> str:
    return f'{NEKOWEB_SITE_URL if host == NEKOWEB else NEOCITIES_SITE_URL}'.replace("<site>", username)


# CHECK IF URL EXIST ON A SITE
def is_url_exists(url: str) -> bool:
    r = requests.head(url, allow_redirects=True)
    return r.status_code == 200

    
# GET NENE CONFIG FROM THE USER'S SITE
def get_config(username: str, host: str) -> dict:
    config: dict = {}
    if not is_url_exists(config_path := f'{get_site(username=username, host=host)}/{NENE_CONFIG_PATH}'):
        return config
    # print(config_path)
    
    try:
        resp: dict = requests.get(config_path, allow_redirects=True).json()
    except Exception as e:
        print('error occurred while parsing config json:', e)
        return config
    else:
        config = {key:val for key, val in resp.items() if key in NENE_CONFIG_ALLOWED_PARAMS}
    # print(resp)
  
    # print(config)      
    return config


# GET SITE INFO ALONG WITH CUSTOM META
def get_site_info(username: str, host: str) -> tuple[dict|str, str|int]:
    url = f"{NEKOWEB_INFO_EP if host == NEKOWEB else NEOCITIES_INFO_EP}".replace("<uname>", username)
    # print(url)
    res = requests.get(url=url)
    status = res.status_code
    if not res.ok:
        return res.content, status
    
    data = res.json()  
    
    # RESPECT NEOCITIES API RESPONSE
    if host == NEOCITIES:
        t_data = data['info']
        data = {
            "host": NEOCITIES,
            "username": t_data['sitename'],
            "views": t_data['views'],
            "created_at":  t_data['created_at'],
            "updated_at":  t_data['last_updated'],
            
            "hits": t_data['hits'],
			"domain": t_data['domain'],
            "tags": t_data['tags']
        }
    else:
        data['host'] = NEKOWEB
    
    data.update(get_config(username=username, host=host))   
    # print(data)
    return data, status
