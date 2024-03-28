import os
import time
import subprocess

def main():
	send()
	clear()
	writer(receive())

# отправляет запрос
def send():
	os.system("mosquitto_pub -h 192.168.31.50 -t test -m Condition -u orangepi -P orangepi")
# чистит топик
def clear():
	os.system("mosquitto_pub -h 192.168.31.50 -t test -u orangepi -P orangepi -n -r -d")

# обрабатывает ответ
def receive():
	time.sleep(1)
	process = subprocess.Popen(['mosquitto_sub', '-C', '1', '-h', '192.168.31.50', '-t', 'test', '-u', 'orangepi', '-P', 'orangepi'], stdout=subprocess.PIPE)
	output = process.stdout.read()
	process.terminate()
	return str(output)[2:-3]

# записывает в db
def writer(cond):
	print("condition:", cond)

if __name__ == '__main__':
	main()