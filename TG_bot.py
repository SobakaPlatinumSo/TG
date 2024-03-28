from server import cond
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import time
import random
import json

Token = "5601155526:AAE5QTrtt9Ibh8mWxdYstdT1EYjxw12k_hY"
bot = Bot(token=Token)
dp = Dispatcher(bot)


@dp.message_handler()
async def Condition(message : types.Message):
	if message.text == "Condition":
		await os.system("python3 server.py")
		await message.answer(cond)
executor.start_polling(dp, skip_updates=True)

		# with open("/home/HomeProject/TG/kostil.txt", "w"):
		# 	pass
		# os.system("mosquitto_pub -h 192.168.31.50 -t test -m Condition -u orangepi -P orangepi")
		# time.sleep(2)
		# with open("/home/HomeProject/TG/kostil.txt", "r") as f:
		# 	lines = f.readlines()
		# data = {}
		# data['cond'] = []
		# data['cond'].append({
		# 	'co2': lines[1],
		# 	'Humidity': '28.57',
		# 	'Temperature': '23.34'
		# })
		# with open("/home/HomeProject/TG/CAC.json", "w") as json_f:
		# 	json.dump(data, json_f)
		# with open("/home/HomeProject/TG/CAC.json") as json_file:
		# 	data = json.load(json_file)
		# 	for c in data['cond']:
		# 		co2 = str(c["co2"])
		# 		Humidity = str(c["Humidity"])
		# 		Temperature = str(c["Temperature"])
		# os.system(f"psql -c 'INSERT INTO cond_data VALUES ({Temperature}, {Humidity}, {co2})' -d condition_db postgres;")
		# await message.answer(f"CO2 {co2} Humidity {Humidity} \n Temperature {Temperature}")