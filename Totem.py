import RPi.GPIO as GPIO
import time
import LCD_I2C
import RFID
import threading

reader = RFID.RFID()
LCD_I2C.lcd_init()

def login():
 while True:
  LCD_I2C.lcd_print("   BIENVENIDO   ",LCD_I2C.LCD_LINE_1)
  LCD_I2C.lcd_print(" A ELECTROBIKE  ",LCD_I2C.LCD_LINE_2)
  time.sleep(3)
  try:
   id, text = reader.read()
   print(id)
   print(text)
  finally:
   GPIO.cleanup()

threads = list()
t1 = threading.Thread(target=login)
threads.append(t1)
t1.start()
#t2 = threading.Thread(target=scanner_estaciones)
#threads.append(t2) t2.start()
#reset_screen()
