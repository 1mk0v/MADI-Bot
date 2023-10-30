from pydantic import BaseModel
from models import Community
from aiogram.types import (
    ReplyKeyboardRemove, ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
    Message
)
from aiogram.utils.keyboard import (
    KeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardBuilder
)
from typing import List


def responseInlineKeyboardMarkup(data, indexStart:int = 0, url:str = None) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    currentData = data[indexStart:indexStart+12]
    for name in currentData:
        builder.button(text=name["value"], url=url, callback_data=str(name['id']))
    builder.adjust(4)
    return builder.as_markup()

def responseReplyKeyboardMarkup(buttonsNames:List[str]) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for name in buttonsNames:
        builder.button(text=name)
    builder.adjust(4)
    builder._validate_size(1)
    keyboardMarkup = builder.as_markup()
    keyboardMarkup.resize_keyboard = True
    return keyboardMarkup