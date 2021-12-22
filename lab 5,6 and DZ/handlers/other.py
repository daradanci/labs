from aiogram import types, Dispatcher
import json, string
from vzaimoImporty import dp
dontUnderstandYouMessage="I don't understand you. Do you speak English?"

# @dp.message_handler()
async def echo_send(message: types.Message):
    answer=just_answerer(message.text)
    if(answer!=dontUnderstandYouMessage):
        await message.answer(answer)

#    if {i.lower().translate(str.maketrans('', '', string.punctuation))  for i in message.text.split(' ')}\
#        .intersection(set(json.load(open('cenz.json')))) != set():
#        await message.reply('Speak politely please!')
#        await message.delete()

"""    if message.text == 'Hello!':
        await message.answer('Hello there! How are you?')
    elif message.text == 'I am fine, thanks!':
        await message.answer('What a nice day to see you here!')
    elif message.text == 'test':
        await message.answer('Stop testing me!')
    elif message.text == 'Test':
        await message.answer('No tests are allowed here!')"""
 #  await message.answer(message.text)
 #  await message.reply(message.text)
 #   await bot.send_message(message.from_user.id, message.text)

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)

def just_answerer(message: string)->string:
    dictionary = {
        'Hello!':'Hello there! How are you?',
        'I am fine, thanks!':'What a nice day to see you here!',
        'You too!':':^)',
        'test':'Stop testing me!',
        'Test':'No tests are allowed here!'
    }
    if message in dictionary:
        return dictionary[message]
    else:
        return dontUnderstandYouMessage
"""    if message == 'Hello!':
        return 'Hello there! How are you?'
    elif message == 'I am fine, thanks!':
        return 'What a nice day to see you here!'
    elif message == 'test':
        return 'Stop testing me!'
    elif message == 'Test':
        return 'No tests are allowed here!'
"""