#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

button1="GP0_6"  #PAUSE or MODE
button2="GP0_5"
button3="GP0_4"
button4="GP0_3"

LED1="RED"
LED2="GREEN"
LED3="GP1_4"
LED4="GP1_3"

#buttons and led arrays to simplify the code
BTNS=[button1,button2,button3,button4]
LEDS=[LED1,LED2,LED3,LED4]
# Set the GPIO pins:
for i in range(len(BTNS)):
  GPIO.setup(BTNS[i],GPIO.IN)
for i in range(len(LEDS)):
  GPIO.setup(LEDS[i],GPIO.OUT)

#Map buttons to LEDs
map = {button1: LED1, button2: LED2, button3 :LED3, button4 :LED4}
def updateLED(channel):
  print("channel = " + channel)
  state = GPIO.input(channel)
  GPIO.output(map[channel], state)
  print(map[channel] + " Toggled")

print("Running...")
for i in range(len(BTNS)):
  GPIO.add_event_detect(BTNS[i], GPIO.BOTH, callback=updateLED)


try:
  while True:
    time.sleep(100)

except KeyboardInterrupt:
  print("Cleaning Up")
  GPIO.cleanup()
GPIO.cleanup()

