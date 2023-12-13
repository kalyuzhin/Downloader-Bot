import os
import asyncio

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hitalic, hbold, hstrikethrough

file = open('config.py')
TOKEN = file.readline().strip()  # Получение токена из файла(я знаю, что лучше пользоваться переменными окружения)

dispatcher = Dispatcher()

BOT = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
