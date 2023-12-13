from config import *
from tools import *


@dispatcher.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"{message.from_user.full_name}!\nЭтот бот позволяет скачивать различные медиа из YouTube, VK и Instagram!")


@dispatcher.message()
async def try_parse(message: Message) -> None:
    parse = parser.vk_parse(message.text) or parser.youtube_parse(message.text)
    if len(parse) != 0:
        vk_downloader
    else:
        await message.answer("Неверная ссылка, повторите попытку")
