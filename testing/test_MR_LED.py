from gpiozero import LED
from time import sleep

ports = [5, 6, 13]
LEDs = []

for port in ports :
    LEDs.append(LED(port))

while True:
    for LED_test in LEDs :
        LED_test.on()
        sleep(1)
        LED_test.off()
        sleep(1)
