#!/usr/bin/env python

import RPi.GPIO as GPIO
import RFID

reader = RFID.RFID()

try:
        text = raw_input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()
