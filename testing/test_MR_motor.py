from gpiozero import Motor
import time

wheel_FR = Motor(14, 15)
wheel_FL = Motor(4, 17)
wheel_BL = Motor(27,22)
wheel_BR = Motor(23,24)


def allFourWheels(n):
    wheel_FL.forward(n)
    wheel_FR.forward(n)
    wheel_BL.forward(n)
    wheel_BR.forward(n)

while True : 
    for i in range(10):
        vel = 1.0- (float(i)/10.0)
        print(vel)
        allFourWheels(vel)
        #wheel_FL.forward(0.3)
        #wheel_FR.forward(0.3)
        #wheel_BL.forward(0.3)
        #wheel_BR.forward(0.3)
        time.sleep(1)
    wheel_FL.forward(0)
    wheel_FR.forward(0)
    wheel_BL.forward(0)
    wheel_BR.forward(0)
    time.sleep(3)
