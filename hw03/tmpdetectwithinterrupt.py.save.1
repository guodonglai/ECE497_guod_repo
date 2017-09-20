#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
bus=smbus.SMBus(1)
address1=0x48
address2=0x49
Alert1="GP0_6"
Alert2="GP0_5"

gpios=[Alert1,Alert2]
for i in range(len(gpios)):
	GPIO.setup(gpios[i],GPIO.IN)

def printstuff(channel):
	if channel==Alert1:
		temp1=bus.read_byte_data(address1,0)
		temp2=(temp1*9/5+32)
		print(temp2)

	if channel==Alert2:
		temp3=bus.read_byte_data(address2,0)
		temp4=(temp3*9/5+32)
		print(temp4)

for i in range(len(gpios)):
	GPIO.add_event_detect(gpios[i],GPIO.BOTH,callback=printstuff)
while True:
	time.sleep(20)
