import re


def youtube_parse(url: str) -> str:
    pattern = r'(https:://)?(www\.)?youtu\.?be\.com/.+'
    m = re.search(pattern, url)
    if m is None:
        return ''
    else:
        return m.group(0)


def vk_parse(url: str) -> str:
    pattern = r'(https:://)?vk\.com/video.+'
    m = re.search(pattern, url)
    if m is None:
        return ''
    else:
        return m.group(0)
