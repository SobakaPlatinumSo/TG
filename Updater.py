import os


os.system("mosquitto_sub -h 192.168.0.150 -t test -u user -P orangepi >> /home/orangepi/HomeProject/Home_project/ACboard_app/CurrentAirCondition.txt")
