from aiogram import Router
from aiogram.types import Message

from API import raspisanie
from Message import StaticMessages, api_response

router = Router(name='/auth')
groupMethods = raspisanie.RaspisanieAPI('/group/')

@router.message()
async def message_handler(message: Message):
    return await getGroupNameCommand(message=message)

async def getGroupNameCommand(message: Message) -> None:
    await message.answer(StaticMessages.getGroupMsg())
    groupsCommunity = await groupMethods.getCommunity()
    keyboardMarkup = api_response.responseInlineKeyboardMarkup(groupsCommunity, 0)
    await message.answer(
        text='Или выбери среди данных свою',
        reply_markup = keyboardMarkup
    )