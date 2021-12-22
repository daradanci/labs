from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


#admin's keyboard

button_load=KeyboardButton('/Load')
button_delete=KeyboardButton('/Delete')

button_case_admin=ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)