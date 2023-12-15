import re
import requests

from config import VK_TOKEN
from aiogram.types import Message


def get_player_url(message: Message) -> str:
    pattern = r'(https:://)?vk\.com/video(-?\d+)_(\d+).*'
    match = re.search(pattern, message.text)
    owner_id = match.group(2)
    video_id = match.group(3)
    get = f'https://api.vk.com/method/video.get?access_token={VK_TOKEN}&videos={owner_id}_{video_id}&v=5.199'
    request = requests.get(get)
    item = request.json()['response']['items'][0]
    url = item['player']
    filename = f"{message.from_user.id}_{item['title']}"
    return filename
