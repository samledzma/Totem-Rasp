

#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import LCD_I2C
import RFID
import threading
import tarjetasUID

reader = RFID.RFID()
LCD_I2C.lcd_init()


import serial
ser = serial.Serial(
    port='/dev/serial0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1.0
           )

def login():
    bici_uno = '1'
    bici_dos = '1'
    bici_tres = '1'
    bici_cuatro = '1'
    bici_cinco = '1'
    bici_seis = '1'
    while True:
      print "inicio"
      LCD_I2C.lcd_print("    NATURAL     ",LCD_I2C.LCD_LINE_1)
      LCD_I2C.lcd_print("   ADVENTURES   ",LCD_I2C.LCD_LINE_2)
      time.sleep(0.05)
      try:
        id, text = reader.read()
      finally:
        GPIO.cleanup()
      LCD_I2C.lcd_reset()
      LCD_I2C.lcd_print("   DETECTANDO   ",LCD_I2C.LCD_LINE_1) 
      LCD_I2C.lcd_print("     TARJETA    ",LCD_I2C.LCD_LINE_2)
      time.sleep(3)
      print(id)
      if id in tarjetasUID.list:
        LCD_I2C.lcd_reset()
        LCD_I2C.lcd_print("    TARJETA     ",LCD_I2C.LCD_LINE_1)
        LCD_I2C.lcd_print("     VALIDA     ",LCD_I2C.LCD_LINE_2)
        time.sleep(3)
        if id == 584195104236:
          if bici_uno == '1':
            LCD_I2C.lcd_print("  TOME LA BICI  ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("        1       ",LCD_I2C.LCD_LINE_2)
            ser.write('OPEN|1*')
            time.sleep(3)
            bici_uno = '0'
          elif bici_uno == '0':
            LCD_I2C.lcd_print("    BICICLETA   ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("    ENTREGADA   ",LCD_I2C.LCD_LINE_2)
            ser.write('CLOSE|1*')
            time.sleep(3)
            bici_uno = '1'
        if id == 584191169753:
          if bici_dos == '1':
            LCD_I2C.lcd_print("  TOME LA BICI  ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("        2       ",LCD_I2C.LCD_LINE_2)
            ser.write('OPEN|2*')
            time.sleep(3)
            bici_dos = '0'
          elif bici_dos == '0':
            LCD_I2C.lcd_print("   BICICLETA    ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("    ENTREGADA   ",LCD_I2C.LCD_LINE_2)
            ser.write('CLOSE|2*')
            time.sleep(3)
            bici_dos = '1'
        if id == 584191577096:
          if bici_tres == '1':
            LCD_I2C.lcd_print("  TOME LA BICI  ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("        3       ",LCD_I2C.LCD_LINE_2)
            ser.write('OPEN|3*')
            time.sleep(3)
            bici_tres = '0'
          elif bici_tres == '0':
            LCD_I2C.lcd_print("   BICICLETA    ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("    ENTREGADA   ",LCD_I2C.LCD_LINE_2)
            ser.write('CLOSE|3*')
            time.sleep(3)
            bici_tres = '1'
        if id == 584188868453:
          if bici_cuatro == '1':
            LCD_I2C.lcd_print("  TOME LA BICI  ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("        4       ",LCD_I2C.LCD_LINE_2)
            ser.write('OPEN|4*')
            time.sleep(3)
            bici_cuatro = '0'
          elif bici_cuatro == '0':
            LCD_I2C.lcd_print("   BICICLETA    ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("    ENTREGADA   ",LCD_I2C.LCD_LINE_2)
            ser.write('CLOSE|4*')
            time.sleep(3)
            bici_cuatro = '1'
        if id == 584190119981:
          if bici_cinco == '1':
            LCD_I2C.lcd_print("  TOME LA BICI  ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("        5       ",LCD_I2C.LCD_LINE_2)
            ser.write('OPEN|5*')
            time.sleep(3)
            bici_cinco = '0'
          elif bici_cinco == '0':
            LCD_I2C.lcd_print("   BICICLETA    ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("    ENTREGADA   ",LCD_I2C.LCD_LINE_2)
            ser.write('CLOSE|5*')
            time.sleep(3)
            bici_cinco = '1'
        if id == 584198349313:
          if bici_seis == '1':
            LCD_I2C.lcd_print("  TOME LA BICI  ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("        6       ",LCD_I2C.LCD_LINE_2)
            ser.write('OPEN|6*')
            time.sleep(3)
            bici_seis = '0'
          elif bici_seis == '0':
            LCD_I2C.lcd_print("   BICICLETA    ",LCD_I2C.LCD_LINE_1)
            LCD_I2C.lcd_print("    ENTREGADA   ",LCD_I2C.LCD_LINE_2)
            ser.write('CLOSE|6*')
            time.sleep(3)
            bici_seis = '1'
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

while True:
  print "Terminal:"
  texto = raw_input("SEND COMMAND: ")
  ser.write(texto)
