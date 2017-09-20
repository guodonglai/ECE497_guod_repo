#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import math

#initial setup for gpio pins
button1="GP0_6"
button2="GP0_5"
button3="GP0_4"
button4="GP0_3"

gpios=[button1,button2,button3,button4]
for i in range(len(gpios)):
  GPIO.setup(gpios[i],GPIO.IN)

delay=1
size=8
bus=smbus.SMBus(1)
matrix=0x70
begin_x=0
begin_y=0
a='w'
b='a'
c='s'
d='d'
#Map buttons to certain values
map={button1: a, button2: b, button3: c, button4: d}

bus.write_byte_data(matrix,0x21,0)
bus.write_byte_data(matrix,0x81,0)
bus.write_byte_data(matrix,0xe7,0)

initial=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
print("Running...")

bus.write_i2c_block_data(matrix, 0, initial)

def changemap(channel):
    global begin_x
    global begin_y
    global initial
    if GPIO.input(channel):
       if map[channel]=='w':
  	  if begin_y!=0:
	     initial[begin_x*2+1]=initial[begin_x*2+1]+math.pow(2,begin_y)
	     bus.write_i2c_block_data(matrix, 0, initial)
	     begin_y=begin_y-1
       elif map[channel]=='s':
          if begin_y!=size:
             initial[begin_x*2+1]=initial[begin_x*2+1]+math.pow(2,begin_y)
             bus.write_i2c_block_data(matrix, 0, initial)
             begin_y=begin_y+1
       elif map[channel]=='a':
          if begin_x!=0:
            # initial[]
             bus.write_i2c_block_data(matrix, 0, initial)
             begin_x=begin_x-1
       elif map[channel]=='d':
          if begin_x!=size:
            # initial[]
             bus.write_i2c_block_data(matrix, 0, initial)
             begin_x=begin_x+1
for i in range(len(gpios)):
  GPIO.add_event_detect(gpios[i], GPIO.BOTH, callback=updateLED)

