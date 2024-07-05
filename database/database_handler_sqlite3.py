import sqlite3

from aiogram.types import Message


def connect_to_database() -> None:
    global cur
    global connect
    connect = sqlite3.connect('database.db')
    cur = connect.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users_data(ID INTEGER PRIMARY KEY AUTOINCREMENT, USER_ID int, URL TEXT, TELEGRAM_URI TEXT)")
    print("Подключение к базе данных прошло успешно!")
    connect.commit()


def insert_user_into_database(user_id: int) -> None:
    cur.execute(f"INSERT INTO users_data (USER_ID) VALUES (?)", (user_id,))
    connect.commit()


def insert_url_into_database(message: Message) -> None:
    cur.execute(f"INSERT INTO users_data (USER_ID,URL) VALUES (?,?)", (message.from_user.id, message.text,))
    connect.commit()
