from machine import Pin, SPI
from time import sleep
import max7219


spi = SPI(1, baudrate=1000000, sck=Pin(14), mosi=Pin(13))  # Configura SPI sck = clock, mosi = data
cs = Pin(15, Pin.OUT)  # Configura el pin CS correctamente
display = max7219.Matrix8x8(spi, cs, 4)  # 4 displays in cascade


display.brightness(15)  # Set brightness (0-15)
display.fill(1)  # Clear the display
display.show()  # Show the changes
sleep(1)  # Wait for a second
display.fill(0)  # Clear the display
display.show()  # Show the changes
sleep(2)
display.text("Hola", 0, 0, 1)  # Display text at (x, y) with color 1 (white)  
display.show()  # Show the changes

# Ajuste en el bucle while para evitar que el texto desaparezca inmediatamente
while True:
    display.text("Hola", 8, 0, 1)  # Display text at (x, y) with color 1 (white)
    display.scroll(-1, 0)  # Scroll left by 1 pixel
    display.show()  # Show the changes
    sleep(0.1)  # Wait for a short time

    for i in range(256):
        display.text("BUENAS NOCHES", 24-i, 0, 1)  # Display text at (x, y) with color 1 (white)
        display.show()
        sleep(0.01)  # Wait for a short time
        display.fill(0)  # Clear the display
        display.show()