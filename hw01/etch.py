#!/usr/bin/python
import curses
#prompt a user input 
move_length=int(input("enter a grid size" ) )
#initialize a screen
stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
#set up original position
begin_x=0
begin_y=0
stdscr.addstr(begin_y,begin_x,'X')
while True:
#detect keyboard character input click
  c=stdscr.getch()
#determine if the key pressed is wasd
  if c==ord('a'):
#determine if the coordinates is less than 0
    if begin_x!=0:
      begin_x=begin_x-1
      stdscr.addstr(begin_y,begin_x,'X')
  elif c==ord('d'):
    if begin_x!=move_length:
#determine if the coordinates is greater than the boundary
      begin_x=begin_x+1
      stdscr.addstr(begin_y,begin_x,'X')
  elif c==ord('w'):
    if begin_y!=0:
      begin_y=begin_y-1
      stdscr.addstr(begin_y,begin_x,'X')
  elif c==ord('s'):
    if begin_y!=move_length:
      begin_y=begin_y+1
      stdscr.addstr(begin_y,begin_x,'X')
#q is used to quit the game
  elif c==ord('q'):
     break
#c is used to clear the whole screen
  elif c==ord('c'):
     stdscr.clear()
     begin_x=0
     begin_y=0
curses.endwin()
