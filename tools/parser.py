import re


def youtube_parse(url: str) -> str:
    """
    Проверяет строку на совпадение с паттерном ссылки YouTube
    :param url:
    :return:
    """
    pattern = r'(https:://)?(www\.)?youtu\.?be\.com/.+'
    m = re.search(pattern, url)
    if m is None:
        return ''
    else:
        return m.group(0)


def vk_parse(url: str) -> str:
    """
    Проверяет строку на совпадение с паттерном ссылки VK
    :param url:
    :return:
    """
    pattern = r'(https:://)?vk\.com/video(-?\d+)_(\d+).*'
    m = re.search(pattern, url)
    if m is None:
        return ''
    else:
        return m.group(0)
