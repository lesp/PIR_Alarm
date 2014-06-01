#Raspberry Pi PIR Alarm

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

pir = 7
GPIO.setup(pir, GPIO.IN)
