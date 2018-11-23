
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
    timeout=1
           )

def interprete(com):
    com = com.split("|")
    print com
    if com[0] == "OPEN":
     print "hola"


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

def leer_estacion():
 line = []

 while True:
    for c in ser.read():
        line.append(c)
        if c == '|':
            print("Line: " + ''.join(line))
            line = []
            break

 ser.close()










#    try:
#        escribir_estacion(adr,"REQ|"+str(adr))
#        leer = 0
#        texto=""
#        while leer < 50:
#            x = readNumber(hadr)
#            if x == 10:
#              break
#            texto+=chr(x)
#            leer+=1
#        return texto
#    except IOError as e:
#        return "ERROR|CONNECTION_PROBLEM|"+str(adr);

def escribir_estacion(adr,message):
    print "Enviando mensaje --> "
    print message
    hadr=getHexAdr(adr)
    try:
        ser.write(message+'*')
    except IOError as e:
        #print e
        return "ERROR|CONNECTION_PROBLEM|"+str(adr);


#threads = list() 
#t1 = threading.Thread(target=login)
#threads.append(t1)
#t1.start()
 
#threading.Thread(target=scanner_estaciones)
#threads.append(t2) t2.start()
#reset_screen()

while True:
  print "Prueba"
#  texto = raw_input("SEND COMMAND: ")
#  ser.write(texto)
  leer_estacion()
