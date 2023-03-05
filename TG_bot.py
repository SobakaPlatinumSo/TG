from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os


Token = "5601155526:AAE5QTrtt9Ibh8mWxdYstdT1EYjxw12k_hY"
bot = Bot(token=Token)
dp = Dispatcher(bot)

async def Update():
   pass

with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt") as f:
   lines = f.readlines()

@dp.message_handler()
async def Condition(message : types.Message):
   if message.text == "Temperature":
      await message.answer(lines[0])
   if message.text == "Humidity":
      await message.answer(lines[1])
   if message.text == "co2":
      await message.answer(lines[2])


executor.start_polling(dp, skip_updates=True)
