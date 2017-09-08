#!/usr/bin/env python3
import curses
import Adafruit_BBIO.GPIO as GPIO
import time

#initial setup for gpio pins
button1="GP0_6"
button2="GP0_5"
button3="GP0_4"
button4="GP0_3"

gpios=[button1,button2,button3,button4]
for i in range(len(gpios)):
  GPIO.setup(gpios[i],GPIO.IN)
#prompt a user input 
move_length=int(input("enter a grid size" ) )
#initialize a screen
stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
#set up original position
begin_x=0
begin_y=0
a='w'
b='a'
c='s'
d='d'
#Map buttons to certain values
map={button1: a, button2: b, button3: c, button4: d}

def updateLED(channel):
    global begin_x
    global begin_y
    global stdscr 
    if GPIO.input(channel):
       if map[channel]=='w':
          if begin_y!=0:
             begin_y=begin_y-1
             stdscr.addstr(begin_y,begin_x,'X')
#refresh the stdscr whenever the button is pressed
             stdscr.refresh()
       elif map[channel]=='s':
          if begin_y!=move_length:
             begin_y=begin_y+1
             stdscr.addstr(begin_y,begin_x,'X')
             stdscr.refresh()
       elif map[channel]=='a':
#determine if the coordinates is less than 0
          if begin_x!=0:
             begin_x=begin_x-1
             stdscr.addstr(begin_y,begin_x,'X')
             stdscr.refresh()
       elif map[channel]=='d':
          if begin_x!=move_length:
#determine if the coordinates is greater than the boundary
             begin_x=begin_x+1
             stdscr.addstr(begin_y,begin_x,'X')
             stdscr.refresh()

print("Running...")

for i in range(len(gpios)):
  GPIO.add_event_detect(gpios[i], GPIO.BOTH, callback=updateLED)

while True:
  c=stdscr.getch()
   
curses.endwin()


