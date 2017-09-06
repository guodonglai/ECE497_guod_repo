#!/usr/bin/python
import curses
import curses.textpad
import time
move_length=int(input("enter a grid size" ) )
stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
begin_x=0
begin_y=0
stdscr.addstr(begin_y,begin_x,'X')
while True:
  c=stdscr.getch()
  if c==ord('a'):
    if begin_x!=0:
      begin_x=begin_x-1
      stdscr.addstr(begin_y,begin_x,'X')
  elif c==ord('d'):
    if begin_x!=move_length:
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
  elif c==ord('q'):
     break
  elif c==ord('c'):
     stdscr.clear()
     begin_x=0
     begin_y=0
curses.endwin()
