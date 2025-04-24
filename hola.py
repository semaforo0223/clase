from machine import Pin
from time import sleep


LED = Pin(2, Pin.OUT)

while True:
    LED.value(1)
    sleep(1)
    LED.value(0)
    sleep(1)