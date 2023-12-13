import asyncio

from config import *


async def main() -> None:
    await dispatcher.start_polling(BOT)


if __name__ == '__main__':
    asyncio.run(main())
