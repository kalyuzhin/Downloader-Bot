from config import *


@dispatcher.message(CommandStart(), ['help'])
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"{message.from_user.full_name}!\nЭтот бот позволяет скачивать различные медиа из YouTube, VK и Instagram!")
