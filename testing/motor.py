from gpiozero import Motor
import time

wheel_FR = Motor(14, 15)
wheel_FL = Motor(4, 17)
wheel_BL = Motor(27,22)
wheel_BR = Motor(23,24)

for i in range(10):
    wheel_FL.forward(1-i/10)
    wheel_FR.forward(1-i/10)
    wheel_BL.forward(1-i/10)
    wheel_BR.forward(1-i/10)
    time.sleep(1)
