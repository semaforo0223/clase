from machine import Pin, SPI
from time import sleep
import max7219

# Configuración de SPI y pines
spi = SPI(1, baudrate=1000000, sck=Pin(14), mosi=Pin(13))  # Configura SPI sck = clock, mosi = data
cs = Pin(15, Pin.OUT)  # Configura el pin CS correctamente

class Display:
    def __init__(self, spi, cs, num_matrices):
        self.display = max7219.Matrix8x8(spi, cs, num_matrices)
        self.display.brightness(15)  # Configura el brillo (0-15)
        self.display.fill(0)  # Limpia la pantalla
        self.display.show()  # Muestra los cambios

    def show_message(self, message, duration=5):
        self.display.fill(0)
        self.display.text(message, 0, 0, 1)
        self.display.show()
        sleep(duration)
        self.display.fill(0)
        self.display.show()

    def scroll_message(self, message, speed=0.1):
        for i in range(len(message) * 8):
            self.display.fill(0)
            self.display.text(message, 8 - i, 0, 1)
            self.display.show()
            sleep(speed)

    def clear(self):
        self.display.fill(0)
        self.display.show()

display = Display(spi, cs, 4)  # 4 displays en cascada

# Mostrar "Hola" por 5 segundos
display.show_message("Hola", 5)

# Bucle principal para animaciones
while True:
    display.scroll_message("Hola", 0.1)  # Desplaza el texto hacia la izquierda
    sleep(1)  # Espera un corto tiempo

    # Animación de "BUENAS NOCHES"
    for i in range(256):
        display.display.text("BUENAS NOCHES", 24-i, 0, 1)  # Muestra el texto desplazándose
        display.display.show()
        sleep(0.01)  # Espera un corto tiempo
        display.display.fill(0)  # Limpia la pantalla
        display.display.show()