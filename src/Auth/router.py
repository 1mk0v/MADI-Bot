from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from typing import Optional

from API import raspisanie
from Message import StaticMessages
from Message.keyboards import KeyboardFabric

router = Router()

class AuthStates(StatesGroup):
    inputGroup = State() 

@router.message(Command("auth"))
async def makeAuth(message: Message, state: FSMContext):
    groupMethods = raspisanie.RaspisanieAPI('/group/')
    await message.answer(
        text="Выберите свою группу"
    )
    await state.set_state(AuthStates.inputGroup)

@router.message(AuthStates.inputGroup, F.text)
async def inputGroup(message: Message, state: FSMContext):
   """INPUT STATE"""
   pass

@router.callback_query(F.data == 'next')
async def getNextData(callback: CallbackQuery):
    """CALLBACK NEXT"""
    await updateMessage(callback)

@router.callback_query(F.data == 'previous')
async def getNextData(callback: CallbackQuery):
    """CALLBACK PREVIOUS"""
    await updateMessage(callback)

async def updateMessage(callback:CallbackQuery):
    await callback.message.edit_text(
        text="Выберите свою группу"
    )