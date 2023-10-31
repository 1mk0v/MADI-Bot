import asyncio
import logging
import sys

from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup
)
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    ReplyKeyboardBuilder,
    KeyboardBuilder
)

from Message import StaticMessages
from Message.keyboards import KeyboardFabric
from Auth.router import router as authRouter


TOKEN = "5620314916:AAFd2NaaCj02H8Nwek38Rb_ugKZdpqlERe4"
dp = Dispatcher()


@dp.message(CommandStart())
async def startCommand(message: Message) -> None:
    await message.answer(StaticMessages.helloMsg(message.from_user.full_name))
    myKeyboard = KeyboardFabric()
    await message.answer(
        'Чтобы начать пользоваться ботом, нужно зарегистрироваться.', 
        reply_markup=myKeyboard.getKeyboardWithButton(KeyboardButton(text='/auth'))
    )

async def main() -> None:
    session = AiohttpSession(proxy='http://proxy.sirena-travel.ru:3128')
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML, session=session)
    dp.include_router(authRouter)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
