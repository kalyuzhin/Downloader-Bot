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
        f"Привет, {message.from_user.full_name}!\nЭтот бот позволяет скачивать различные медиа из YouTube, VK и Instagram!\n\n"
        f"Просто пришли ссылку на видео, которое хочешь скачать :)")


@dispatcher.message()
async def parse_message_handler(message: Message) -> None:
    """
    Хэндлер, который парсит полученное сообщение
    :param message:
    :return:
    """
    if len(parser.vk_parse(message.text)) != 0:
        # resolutions = vk_downloader.parse_page(message.text)
        resolutions = vk_downloader.download_selenium(message.text)
        await message.delete()
        await message.answer('Выберите подходящее вам качество видео:',
                             reply_markup=inline_keyboards.create_inline_keyboard_vk(resolutions).as_markup())
        # await message.answer_video(video=FSInputFile(vk_downloader.get_player_url(message)))
    elif len(parser.youtube_parse(message.text)) != 0:
        await message.delete()
        await message.answer("Выберите подходящее вам качество видео:",
                             reply_markup=inline_keyboards.create_inline_keyboard_yt(message.text).as_markup())


@dispatcher.callback_query()
async def download_youtube_video(callback: CallbackQuery) -> None:
    """
    Отправка видео с YouTube пользователю
    :param callback:
    :return:
    """
    await callback.message.delete()
    await callback.message.answer("Подождите...\nВыполняется загрузка")
    file = youtube_downloader.download_youtube_video(callback)
    await BOT.send_video(chat_id=callback.from_user.id,
                         video=FSInputFile(file))
    await callback.message.delete()
    os.remove(file)
