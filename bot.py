import logging

from aiogram import Bot, Dispatcher, executor, types

#TOKEN
API_TOKEN = 'TOKEN'

users = {}

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    if message.chat.id not in users:
        await message.answer("Привет! Я помогу тебе выучить таблицу умножения!")
        mult = get_mult()
        await message.answer("Получай следующий пример: " + '*'.join(mult))
        users[message.chat.id] = mult
    elif not message.text.isdigit():
        await message.answer("Ты должен ввести цифру!")
    else:
        m = users[message.chat.id]
        if int(m[0])*int(m[1]) == int(message.text):
            await message.answer("Это правильный ответ! Молодец!")
            mult = get_mult()
            await message.answer("Получай следующий пример: " + '*'.join(mult))
            users[message.chat.id] = mult
        else:
            await message.answer("К сожалению, ты ошибся в ответе. Попробуй ещё раз.")



def get_mult():
    import random
    return [str(random.randint(1,9)),str(random.randint(1,9))]

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
