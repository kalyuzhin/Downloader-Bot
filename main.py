from config import *
from handlers import *
from database import *


async def main() -> None:
    await BOT.delete_webhook(drop_pending_updates=True)
    database_handler_sqlite3.connect_to_database()
    await dispatcher.start_polling(BOT)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
