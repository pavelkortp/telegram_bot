from aiogram import types
from loader import dp

@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Привіт, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Ти потребуєш допомоги?')