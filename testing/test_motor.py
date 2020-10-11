from gpiozero import Motor
import time

motor = Motor (4, 14)

while True:
    motor.forward(1.0)
    print("t")
    time.sleep(5)
