from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from vzaimoImporty import dp, bot
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import string
ID=None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#getting moderator's ID
async def make_changes_command(message: types.Message):
    global ID
    ID=message.from_user.id
    await bot.send_message(message.from_user.id, 'At your service, Master', reply_markup=admin_kb.button_case_admin)
    await message.delete()


#start of the job
async def cm_start(message: types.Message):
    if message.from_user.id==ID:
        await FSMAdmin.photo.set()
        await message.reply('Insert an image')

#stop the states
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id==ID:
        current_state=await state.get_state()
        if current_state is None:
            await message.reply('WTF BRO')
            return
        await state.finish()
        await message.reply('Ok')


#catching the first answer of the user
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id==ID:
        async with state.proxy() as data:
            data['photo']=message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Insert the name')

#catching the second answer of the user
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id==ID:
        async with state.proxy() as data:
            data['name']=message.text
        await FSMAdmin.next()
        await message.reply('Insert the description')

#catching the third answer of the user
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id==ID:
        async with state.proxy() as data:
            data['description']=message.text
        await FSMAdmin.next()
        await message.reply('Insert the price')

#catching the last answer of the user and using the given data
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id==ID:

       async with state.proxy() as data:
           data['price']=float(message.text)
       # async with state.proxy() as data:
       #     await message.reply(str(data))
       await sqlite_db.sql_add_command(state)
       await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
#    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} has been deleted.', show_alert=True)
    await callback_query.answer(text=message_about_deletion(callback_query.data.replace("del ", "")), show_alert=True)

@dp.message_handler(commands='Delete')
async def delete_item(message: types.Message):
    if message.from_user.id==ID:
        read=await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n Description: {ret[2]}\n Price: ${ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Delete {ret[1]}', callback_data=f'del {ret[1]}')))

#registering the handlers
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='Load', state=None)
    dp.register_message_handler(cancel_handler, Text(equals='Cancel', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command,commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state="*", commands='Cancel')
    # dp.register_message_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    # dp.register_message_handler(delete_item, commands='Delete')

def message_about_deletion(painting_name:string)->string:
    return f'"{painting_name}" has been deleted.'

