#!/usr/bin/env python

import RPi.GPIO as GPIO
import RFID

reader = RFID.RFID()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
