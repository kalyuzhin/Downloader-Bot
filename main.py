from config import *


async def main() -> None:
    await BOT.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(BOT)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
