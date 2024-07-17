from aiogram.utils.keyboard import InlineKeyboardBuilder
from tools.youtube_downloader import get_resolutions


def create_inline_keyboard_yt(url: str):
    """
    Создает inline-клавиатуру, которая показывает, в каком разрешении возможно скачать видео
    :param url:
    :return:
    """
    builder = InlineKeyboardBuilder()
    for elem in get_resolutions(url):
        builder.button(text=f"{elem}", callback_data=f"set:{url},{elem}")
    return builder


def create_inline_keyboard_vk(resolutions: dict):
    builder = InlineKeyboardBuilder()
    for elem in resolutions.items():
        builder.button(text=f"{elem[0]}", callback_data=f"set:{elem[0]}")  # f"{elem[1]}")
    builder.adjust(1, len(resolutions))
    return builder
