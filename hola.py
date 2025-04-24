from machine import Pin, TouchPad
from time import sleep
#andres makina


touchPrueba = TouchPad(15)
LED = Pin(2, Pin.OUT)

while True:
    touchPrueba.read()
    LED.value(1)
    sleep(0.25)
    LED.value(0)
    sleep(1)
    print(touchPrueba.read())