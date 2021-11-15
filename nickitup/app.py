from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    
    await msg.reply(f'Я бот. Приятно познакомиться, {msg.from.first_name}')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('Не понимаю, что это значит.')

if __name__ == '__main__':
    logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.DEBUG)

    TOKEN_FILENAME = 'token'
    token = ''
    with open(TOKEN_FILENAME, 'r') as token_file:
        token = token_file.readline()
    bot = Bot(token=token)
    dp = Dispatcher(bot)

   executor.start_polling(dp)