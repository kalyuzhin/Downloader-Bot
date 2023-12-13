import re

from pytube import YouTube
from aiogram.types import Message, CallbackQuery


def get_resolutions(url: str) -> list:
    """
    Возвращает все возможные разрешения по ссылке видео YouTube
    :param url:
    :return: list<str>
    """
    resolutions = []
    yt = YouTube(url)
    for resolution in yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc():
        element = str(resolution)
        resolutions.append(re.search(r'res=\"(\d+p)\"', element).group(1))
    return resolutions


def download_youtube_video(url: CallbackQuery) -> str:
    """

    :param url:
    :param resolution:
    :return: str
    """
    yt = YouTube(url.data.split(',')[0])
    filename = f'downloads/{yt.title}_{url.from_user.id}.mp4'
    yt.streams.filter(progressive=True, file_extension='mp4', resolution=url.data.split(',')[1]).first().download(
        filename=filename)
    return filename
