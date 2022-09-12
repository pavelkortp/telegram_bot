from aiogram import types
from loader import dp

@dp.message_handler(text='10')
async def buttons_test(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Ти обрав число {message.text}')

@dp.message_handler(text='11')
async def buttons_test(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Ти обрав число {message.text}')

@dp.message_handler(text='100')
async def buttons_test(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Ти обрав число {message.text}')                        