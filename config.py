import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hitalic, hbold, hstrikethrough

file = open('config.txt')
TOKEN = file.readline().strip()  # Получение токена из файла(я знаю, что лучше пользоваться переменными окружения)

dispatcher = Dispatcher()

BOT = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
