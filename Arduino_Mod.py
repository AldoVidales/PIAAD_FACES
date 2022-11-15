

import serial
import time

def loggin_led():
  ser = serial.Serial("COM12", 9600, writeTimeout = 0)
  time.sleep(2)

  while 1:
    try:
      ser.write("a".encode())
      time.sleep(4)
      ser.close()


    except: # catch *all* exceptions
      break










