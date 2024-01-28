import os

os.system("mosquitto_sub -h 192.168.31.50 -t test -u orangepi -P orangepi >> /home/HomeProject/TG/kostil.txt")
