import asyncio
import logging
import sys

from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from Message import StaticMessages
from Auth.router import router as authRouter


TOKEN = ""
dp = Dispatcher()


@dp.message(CommandStart())
async def startCommand(message: Message) -> None:
    await message.answer(StaticMessages.helloMsg(message.from_user.full_name))

@dp.message()
async def handlerOfAnythink(message: Message) -> None:
    try:
        await message.send_copy(message.chat.id)
    except:
        await message.answer('Incorrect value')


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML, session=session)
    dp.include_router(authRouter)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
