import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import medicines
import weather


storage = MemoryStorage()
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)


class States(StatesGroup):
    medicine = State()


@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Лекарства 💊', callback_data='medicine')
    btn2 = types.InlineKeyboardButton('Погода 🌤', callback_data='weather')
    markup.row(btn1, btn2)
    await message.reply('Мяяяууу', reply_markup=markup)


@dp.callback_query_handler()
async def medicine(call):
    if call.data == 'medicine':
        await States.medicine.set()
        await call.message.answer('Название лекарства?')
    else:
        await call.message.answer(weather.get_weather())


@dp.message_handler(state=States.medicine)
async def process_medicine(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['medicine'] = message.text
        await message.answer(medicines.get_medicine(data['medicine']))
    await state.finish()





# @dp.message_handler()
# def hello(message):
#     # import pdb; pdb.set_trace()
#     if 'тёма' in message.text.lower() or 'тема' in message.text.lower():
#         if 'hello' in message.text.lower() or 'привет' in message.text.lower(): 
#             bot.reply_to(message, f'Мяу, {message.from_user.first_name} 🐈‍⬛')
#         elif 'хороший' in message.text.lower():
#             bot.reply_to(message, f'Мурррр ❤️')
#         else:
#             bot.reply_to(message, f'Кхкхкхкхкххх')
#     else:
#         pass


executor.start_polling(dp)
