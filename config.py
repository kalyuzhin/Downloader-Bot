import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.utils.markdown import hitalic, hbold, hstrikethrough

with open('config.txt') as file:
    TOKEN = file.readline().strip()  # Получение токена из файла(я знаю, что лучше пользоваться переменными окружения)
    VK_TOKEN = file.readline().strip()
    COOKIE = file.readline().strip()

dispatcher = Dispatcher()

BOT = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
