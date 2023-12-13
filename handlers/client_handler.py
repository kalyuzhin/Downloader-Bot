from config import *
from tools import *
from keyboards import *


@dispatcher.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Хэндлер, который обрабатывает стартовую команду
    :param message:
    :return:
    """
    await message.answer(
        f"{message.from_user.full_name}!\nЭтот бот позволяет скачивать различные медиа из YouTube, VK и Instagram!\n\n"
        f"Просто пришли ссылку на видео, которое хочешь скачать :)")


@dispatcher.message()
async def parse_message_handler(message: Message) -> None:
    """
    Хэндлер, который парсит полученное сообщение
    :param message:
    :return:
    """
    if len(parser.vk_parse(message.text)) != 0:
        pass
    if len(parser.youtube_parse(message.text)) != 0:
        await message.answer("Выберите подходящее вам качество видео:",
                             reply_markup=inline_keyboards.create_inline_keyboard(message.text).as_markup())
