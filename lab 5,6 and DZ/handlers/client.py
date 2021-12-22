from aiogram import types, Dispatcher
from vzaimoImporty import dp,bot
from keyboards import kb_client
from data_base import sqlite_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import string

# @dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Have a nice day!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Нужно написать боту в ЛС, чтобы он мог ответить: \nhttps://t.me/telegalegalegabot')

# @dp.message_handler(commands=['Schedule'])
async def information_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'This is the Pixel Buildings collection by famous artist Voxel Pizovski.')

# @dp.message_handler(commands=['Location'])
async def forecast_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'The next artwork collection is devoted to JoJo Part 6 event.')

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('buy '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Congrats!\n "+message_about_buying(callback_query.data.replace("buy ", "")), show_alert=True)
async def menu_command(message: types.Message):
    # await sqlite_db.sql_read(message)
    read = await sqlite_db.sql_read2()
    for ret in read:
        # await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n Description: {ret[2]}\n Price: ${ret[-1]}')
        await bot.send_photo(message.from_user.id, ret[0])
        await bot.send_message(message.from_user.id, text=f'{ret[1]}\n Description: {ret[2]}\n Price: ${ret[-1]}',
                               reply_markup=InlineKeyboardMarkup()
                               .add(InlineKeyboardButton(f'Buy {ret[1]}!', callback_data=f'buy {ret[1]}')))



def register_handlers_client(dp:Dispatcher):
        dp.register_message_handler(command_start, commands=['start','help'])
        dp.register_message_handler(information_command, commands=['Info'])
        dp.register_message_handler(forecast_command, commands=['Forecast'])
        dp.register_message_handler(menu_command, commands=['Exhibit'])

def message_about_buying(painting_name:string)->string:
    return f'You have bought "{painting_name}".'