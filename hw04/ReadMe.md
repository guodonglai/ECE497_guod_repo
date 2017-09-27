#This is a ReadMe.md file
1. buttonetch.py file is the one that uses the rotary encoders to control the 8x8 LED matrix.
To use it, user need to rotate the button, to add one LED at a time.
2. gpio1.c file is the one that controls two internal LED using two push buttons. The USR2 and USR3 are initially on, to turn it off, the user should push gpio25 and gpio17 buttons.
3. gpio2.c file is the one that controls one internal LED using only one push button. To control it, the user need to push gpio1_25 button.
