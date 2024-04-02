import requests
from constants import NEKOWEB_INFO_EP, NEOCITIES_INFO_EP, NEKOWEB, NEOCITIES, NEKOWEB_SITE_URL, NEOCITIES_SITE_URL, NENE_CONFIG_PATH, NENE_CONFIG_ALLOWED_PARAMS


def get_site(username: str, host: str) -> str:
    return f'{NEKOWEB_SITE_URL if host == NEKOWEB else NEOCITIES_SITE_URL}'.replace("<site>", username)


def is_url_exists(url: str) -> bool:
    r = requests.head(url, allow_redirects=True)
    return r.status_code == 200

    
def get_config(username: str, host: str) -> dict:
    config: dict = {}
    if not is_url_exists(config_path := f'{get_site(username=username, host=host)}/{NENE_CONFIG_PATH}'):
        return config
    # print(config_path)
    
    resp: dict = requests.get(config_path, allow_redirects=True).json()
    # print(resp)
  
    config.update({key:val for key, val in resp.items() if key in NENE_CONFIG_ALLOWED_PARAMS})
    # print(config)      
    return config


def get_site_info(username: str, host: str) -> tuple[str|int, str]:
    print(NEKOWEB, NEOCITIES, host)
    url = f"{NEKOWEB_INFO_EP if host == NEKOWEB else NEOCITIES_INFO_EP}".replace("<uname>", username)
    print(url)
    res = requests.get(url=url)
    print(res.content)
    status = res.status_code
    if not res.ok:
        return res.content(), status
    
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
    print(data)
    return data, status


example = {
	"nekoweb": {
		"id": 332,
		"title": " .-._.  |  click this stuff!",
		"updates": 84,
		"followers": 12,
  
		"username": "nullcell",
		"views": 4746,
		"created_at": 1708864280000,
		"updated_at": 1710514868734
	},
	"neocities": {
		"result": "success",
		"info": {
			"sitename": "nullcell",
			"views": 3602,
			"hits": 5848,
			"created_at": "Fri, 19 Jan 2024 19:01:31 -0000",
			"last_updated": "Sun, 10 Mar 2024 19:41:14 -0000",
			"domain": None,
			"tags": [
				"programming",
				"nullcell"
			]
		}
	}
}

# cfg = get_config('null', 'nekoweb')
# print(cfg)