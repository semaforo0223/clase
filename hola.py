from machine import Pin
from time import sleep
#andres makina

LED = Pin(2, Pin.OUT)

while True:
    LED.value(1)
    sleep(0.25)
    LED.value(0)
    sleep(2)