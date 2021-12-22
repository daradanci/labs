from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1=KeyboardButton('/Info')
b2=KeyboardButton('/Forecast')
b3=KeyboardButton('/Exhibit')
# b4=KeyboardButton('Поделиться номером', request_contact=True)
# b5=KeyboardButton('Где я?', request_location=True)
kb_client=ReplyKeyboardMarkup(resize_keyboard=True)
#one_time_keyboard=True

kb_client.add(b1).insert(b2).add(b3)
#.row(b1,b2,b3)