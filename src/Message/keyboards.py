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

from typing import (
    List, Dict
)


class KeyboardFabric:

    def __init__(
            self,
            data = None
        ) -> None:
        self.data:list = data
        self.dataListIndex:int = 0
        self.keyboard = list()

    def addRowButtons(self, buttons:List[InlineKeyboardButton | KeyboardButton]):
        self.keyboard.append(buttons)

    def getKeyboardWithButton(self, button:InlineKeyboardButton | KeyboardButton):
        self.addRowButtons([button])
        if type(button) == KeyboardButton:
            return self.getKeyboard(ReplyKeyboardBuilder) 
        return self.getKeyboard(InlineKeyboardBuilder)

    def getKeyboard(self, builderType:ReplyKeyboardBuilder | InlineKeyboardBuilder):
        builder = builderType(self.keyboard)
        return builder.as_markup()
    
    def getKeyBoardFromData(self):
        pass

    def getInlineKeyboardBuilder(self, count:int=12, rowSize:int=4, url:str = None) -> InlineKeyboardBuilder:
        builder = InlineKeyboardBuilder()
        for name in self.data[self.dataListIndex:self.dataListIndex+count]:
            builder.button(text=name["value"], url=url, callback_data=str(name['id']))
        return builder

    def responseReplyKeyboardMarkup(self) -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        for name in self.data:
            builder.button(text=name)
        builder.adjust(4)
        builder._validate_size(1)
        keyboardMarkup = builder.as_markup()
        keyboardMarkup.resize_keyboard = True
        return keyboardMarkup


