#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import rcpy
import rcpy.encoder as encoder
import time
import smbus
import math

rcpy.set_state(rcpy.RUNNING)
#initial position of rotary encoder
e2=encoder.get(2)
e3=encoder.get(3)
size=8
bus=smbus.SMBus(1)
matrix=0x70
#initial setup for coordinates of matrix
begin_x=0
begin_y=0

bus.write_byte_data(matrix,0x21,0)
bus.write_byte_data(matrix,0x81,0)
bus.write_byte_data(matrix,0xe7,0)

#make it initially clean
initial=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
#array of leading 1s. For instance, 8 is 100 meaning the third row and 64 is 1000000 meaning the 7th row
zz=[1,2,4,8,16,32,64,128,256]
print("Running...")

bus.write_i2c_block_data(matrix, 0, initial)

while True:
#delay half a second to make sure it turn on only one LED at a time
	time.sleep(0.5)
	if rcpy.get_state()==rcpy.RUNNING:
#compare with previous position, if greater then, then move down else move up
		if encoder.get(2)>e2:
#record the new position into e2
			e2=encoder.get(2)
			if begin_y!=size-1:
				begin_y=begin_y+1
				#update the matrix by concatenating(or operatoin) the current array with zz
				initial[begin_x*2+1]=initial[begin_x*2+1] | zz[begin_y]
				bus.write_i2c_block_data(matrix, 0, initial)
		elif encoder.get(2)<e2:
			e2=encoder.get(2)
			if begin_y!=0:
				begin_y=begin_y-1
				initial[begin_x*2+1]=initial[begin_x*2+1] | zz[begin_y]
				bus.write_i2c_block_data(matrix, 0, initial)
		elif encoder.get(3)>e3:
			e3=encoder.get(3)
		#moving left or right will make x coordinates +/- by 1
			if begin_x!=size-1:
				begin_x=begin_x+1
				print(begin_x)
				initial[begin_x*2+1]=initial[begin_x*2+1] | zz[begin_y]
				bus.write_i2c_block_data(matrix, 0, initial)
		elif encoder.get(3)<e3:
			e3=encoder.get(3)
			if begin_x!=0:
				begin_x=begin_x-1
				initial[begin_x*2+1]=initial[begin_x*2+1] | zz[begin_y]
				bus.write_i2c_block_data(matrix, 0, initial)

