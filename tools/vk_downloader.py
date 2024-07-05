import re
import requests

from config import VK_TOKEN
from aiogram.types import Message
from bs4 import BeautifulSoup
from selenium import webdriver


def get_player_url(message: Message) -> str:
    pattern = r'(https:://)?vk\.com/video(-?\d+)_(\d+).*'
    match = re.search(pattern, message.text)
    owner_id = match.group(2)
    video_id = match.group(3)
    get = f'https://api.vk.com/method/video.get?access_token={VK_TOKEN}&videos={owner_id}_{video_id}&v=5.199'
    request = requests.get(get)
    item = request.json()['response']['items'][0]
    url = item['player']
    filename = f"downloads/{message.from_user.id}_{item['title']}"
    download_video(url, filename)
    return filename + '.mp4'


def download_video(url: str, filename: str) -> None:
    response = requests.get(url, stream=True)
    with open(f'{filename}.mp4', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)


def download_selenium(url: str):
    driver = webdriver.Firefox()
    pattern = r'https:://m\.vk\.com/video(-?\d+)_(\d+).*'
    if re.match(pattern, url):
        pass
    else:
        url = 'https:://m.' + url[url.find('vk'):]
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    download = soup.find('div', attrs={'id': 'theme_color_shim'}).findNext('script').text
    index = download.find('mp4_720')
    driver.get(download[index + 10:download.find('\"', index + 10)])
    driver.quit()
