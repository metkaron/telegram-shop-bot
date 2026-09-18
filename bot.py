import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛍 Каталог")],
            [KeyboardButton(text="📦 Мои заказы"), KeyboardButton(text="💬 Поддержка")]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "👋 Добро пожаловать в Digital Shop!\n\n"
        "Здесь можно покупать цифровые товары и услуги.",
        reply_markup=keyboard
    )


@dp.message()
async def buttons(message: Message):
    if message.text == "🛍 Каталог":
        await message.answer(
            "🛍 КАТАЛОГ\n\n"
            "🎮 Игровые товары\n"
            "💻 IT-услуги\n"
            "🎁 Цифровые товары\n\n"
            "Скоро добавим товары!"
        )

    elif message.text == "📦 Мои заказы":
        await message.answer("📦 У вас пока нет заказов.")

    elif message.text == "💬 Поддержка":
        await message.answer("💬 Напишите администратору: @YOUR_USERNAME")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
