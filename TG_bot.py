from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
import time


Token = "5601155526:AAE5QTrtt9Ibh8mWxdYstdT1EYjxw12k_hY"
bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.message_handler()
async def Condition(message : types.Message):
   if message.text == "Temperature":
      with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt", "w"):
         pass
      os.system("mosquitto_pub -h 192.168.0.150 -t test -m Condition -u user -P orangepi")
      time.sleep(2)
      with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt", "r") as f:
         lines = f.readlines()
      await message.answer(lines[1])
   if message.text == "Humidity":
      with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt", "w"):
         pass
      os.system("mosquitto_pub -h 192.168.0.150 -t test -m Condition -u user -P orangepi")
      time.sleep(2)
      with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt", "r") as f:
         lines = f.readlines()
      await message.answer(lines[2])
   if message.text == "Co2":
      with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt", "w"):
         pass
      os.system("mosquitto_pub -h 192.168.0.150 -t test -m Condition -u user -P orangepi")
      time.sleep(2)
      with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt", "r") as f:
         lines = f.readlines()
      await message.answer(lines[3])
   if message.text == "Condition":
      with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt", "w"):
         pass
      os.system("mosquitto_pub -h 192.168.0.150 -t test -m Condition -u user -P orangepi")
      time.sleep(2)
      with open("/home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt", "r") as f:
         lines = f.readlines()
      await message.answer("Temperature: "  + lines[1] + "Humidity: " + lines[2] + "Co2: " + lines[3])


executor.start_polling(dp, skip_updates=True)
