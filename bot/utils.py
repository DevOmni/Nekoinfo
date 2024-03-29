import requests
from constants import NEKOWEB_INFO_EP, NEOCITIES_INFO_EP, NEKOWEB, NEOCITIES

def get_site_info(username: str, host: str) -> tuple[str|int, str]:
    url = f"{NEKOWEB_INFO_EP if host == NEKOWEB else NEOCITIES_INFO_EP}".replace("<uname>", username)
    res = requests.get(url=url)
    
    status = res.status_code
    data = res.json() if res.ok else res.content()

    return data, status, res.ok
