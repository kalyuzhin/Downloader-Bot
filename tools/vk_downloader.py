import re
import requests

from config import VK_TOKEN, COOKIE
from aiogram.types import Message
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Cookie': COOKIE,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0',
}


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


def get_resolutions(soup: str) -> dict:
    d = dict()
    index = soup.find('mp4')
    while index != -1:
        if soup[index:index + 7] in d.keys():
            break
        d[soup[index:index + 7]] = soup[index + 10:soup.find("\"", index + 10)]
        index = soup.find('mp4', index + 1)
    return d


def download_selenium(url: str):
    driver = webdriver.Firefox()
    pattern = r'https://m\.vk\.com/video(-?\d+)_(\d+).*'
    if re.match(pattern, url):
        pass
    else:
        url = 'https://m.' + url[url.find('vk'):]
    driver.get(url)
    driver.quit()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    download = soup.find('div', attrs={'id': 'theme_color_shim'}).findNext('script').text
    # print(get_resolutions(download))
    return get_resolutions(download)
    # driver.get(download[index + 10:download.find('\"', index + 10)])
    # driver.quit()


def parse_page(url: str):
    pattern = r'https://m\.vk\.com/video(-?\d+)_(\d+).*'
    if re.match(pattern, url):
        pass
    else:
        url = 'https://m.' + url[url.find('vk'):]
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'html.parser')
    script = soup.find('div', attrs={'id': 'theme_color_shim'}).findNext('script').text
    return get_resolutions(script)
