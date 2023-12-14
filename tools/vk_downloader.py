import re
import requests

# from config import VK_TOKEN
VK = 'vk1.a.aDBZo_Ej6419UGmC-mI2ag8QEdXM7F8VvrE26EnxVU2gk1GrhotWalafsVNACpYLJ5n2sCr1kQ7ivt16CFQM64hCaUj4JKFsIaWwhZdltGz3raPEU0b838i-jPiMNkEBK-IJK1fpjTeIX5YgiPmJvE4mv5qfuAGkGc0EoV2vVWVsFFOhDz_cg4C5C-gl7Vwc'


def get_player_url(url: str) -> str:
    pattern = r'(https:://)?vk\.com/video(-?\d+)_(\d+).*'
    match = re.search(pattern, url)
    owner_id = match.group(2)
    video_id = match.group(3)
    get = f'https://api.vk.com/method/video.get?access_token={VK}&videos={owner_id}_{video_id}&v=5.199'
    request = requests.get(get)
    item = request.json()['response']['items'][0]
    return item['player']
