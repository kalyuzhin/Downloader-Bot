import re

from pytube import YouTube
from aiogram.types import Message


def get_resolutions(url: str) -> list:
    resolutions = []
    yt = YouTube(url)
    for resolution in yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc():
        element = str(resolution)
        resolutions.append(re.search(r'res=\"(\d+p)\"', element).group(1))
    return resolutions


def download_youtube_video(url: Message, resolution: str) -> str:
    yt = YouTube(url.text)
    filename = f'downloads/{yt.title}_{url.from_user.id}.mp4'
    yt.streams.filter(progressive=True, file_extension='mp4', resolution=resolution).first().download(
        filename=filename)
    return filename
