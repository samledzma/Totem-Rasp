
#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import LCD_I2C
import RFID
import threading
import tarjetasUID

reader = RFID.RFID()
LCD_I2C.lcd_init()

def login():
 while True:
  print "inicio"
  LCD_I2C.lcd_print("   BIENVENIDO   ",LCD_I2C.LCD_LINE_1)
  LCD_I2C.lcd_print(" A ELECTROBIKE  ",LCD_I2C.LCD_LINE_2)
  time.sleep(0.05)
  try:
   id, text = reader.read()
  finally:
   GPIO.cleanup()
# tarjeta = raw_input("SEND COMMAND: ")
  LCD_I2C.lcd_reset()
  LCD_I2C.lcd_print("   DETECTANDO   ",LCD_I2C.LCD_LINE_1) 
  LCD_I2C.lcd_print("     TARJETA    ",LCD_I2C.LCD_LINE_2)
  time.sleep(3)
  print(id)
  if id in tarjetasUID.list:
   print "Abrir"
   LCD_I2C.lcd_reset()
   LCD_I2C.lcd_print("    TARJETA     ",LCD_I2C.LCD_LINE_1)
   LCD_I2C.lcd_print("     VALIDA     ",LCD_I2C.LCD_LINE_2)
   time.sleep(3)
   LCD_I2C.lcd_print("  TOME LA BICI  ",LCD_I2C.LCD_LINE_1)
   LCD_I2C.lcd_print("        1       ",LCD_I2C.LCD_LINE_2)
   time.sleep(3)
  else:
   LCD_I2C.lcd_reset()
   LCD_I2C.lcd_print("    TARJETA     ",LCD_I2C.LCD_LINE_1)
   LCD_I2C.lcd_print("   INVALIDA     ",LCD_I2C.LCD_LINE_2)
   time.sleep(3)
   LCD_I2C.lcd_print("INTENTE DE NUEVO",LCD_I2C.LCD_LINE_1)
   LCD_I2C.lcd_print("   POR FAVOR    ",LCD_I2C.LCD_LINE_2)
   time.sleep(3)

threads = list()
t1 = threading.Thread(target=login)
threads.append(t1)
t1.start()
#t2 = threading.Thread(target=scanner_estaciones)
#threads.append(t2) t2.start()
#reset_screen()
