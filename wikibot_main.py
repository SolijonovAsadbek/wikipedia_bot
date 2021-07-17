import aiogram
import wikipedia

wikipedia.set_lang('uz')
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'API_TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands= ['start', 'help'])
async def start(message: types.Message):
    respose = "Assalomu aleykum\nMen Wikipedia_bot man istalgan ma'lumotni \no'zbek tilida sizga taqadim qilaman."
    await message.reply(respose)

@dp.message_handler()
async def req_to_res(message: types.Message):
    #Bu yerda Ma'lum bir xatoliklar bo'lmasligi uchun try except dan foylanamiz.
    try:
        response = wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer("Bunday ma'lumot topilmadi.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)