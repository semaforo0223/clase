from machine import Pin, TouchPad
from time import sleep

touchPrueba = TouchPad(15)
LED = Pin(2, Pin.OUT)

while True:
    touchPrueba.read()
    LED.value(1)
    sleep(1)
    LED.value(0)
    sleep(1)
    print(touchPrueba.read())