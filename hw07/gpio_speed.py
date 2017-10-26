#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time
#GP1_4 as input # GP1_3 as output
button="GP1_4"
LED="GP1_3"
GPIO.setup(button,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
map={button:LED}
def updateLED(channel):
  print("channel = " + channel)
  state = GPIO.input(channel)
  GPIO.output(map[channel], state)
#  print(map[channel] + " Toggled")

#print("Running...")
GPIO.add_event_detect(button, GPIO.BOTH, callback=updateLED)

#try:
while True:
    time.sleep(100)

#except KeyboardInterrupt:
#  print("Cleaning Up")
#  GPIO.cleanup()
#GPIO.cleanup()
