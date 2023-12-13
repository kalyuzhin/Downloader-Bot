from aiogram.utils.keyboard import InlineKeyboardBuilder
from tools.youtube_downloader import get_resolutions


def create_inline_keyboard(url: str):
    """
    Создает inline-клавиатуру, которая показывает, в каком разрешении возможно скачать видео
    :param url:
    :return:
    """
    builder = InlineKeyboardBuilder()
    for elem in get_resolutions(url):
        builder.button(text=f"{elem}", callback_data=f"set:{url},{elem}")
    return builder
