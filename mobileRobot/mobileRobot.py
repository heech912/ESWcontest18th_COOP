##### CO-OP Demo
##### mobile robot

from communication import nrfConfig,receiver
from mobileRobot.mobileRobotOutput import wheel_FL, wheel_FR, wheel_BL, wheel_BR
from mobileRobot.mobileRobotInput import button_shutdown, button_stop

import time

def motorRotates(motor, val):
    if val > 0 :motor.forward(val)
    else : motor.backward(abs(val))

def mobileRobotMode(mode, motorValueArr):
    if mode != 1 :
        wheel_FL.forward(0)
        wheel_FR.forward(0)
        wheel_BL.forward(0)
        wheel_BR.forward(0)
    else :
        motorRotates(wheel_FL,(motorValueArr[0]/1000))
        motorRotates(wheel_BL,(motorValueArr[1]/1000))
        motorRotates(wheel_FR,(motorValueArr[2]/1000))
        motorRotates(wheel_BR,(motorValueArr[3]/1000))
    return mode
def mobileRobotMain(address):
    nrf = nrfConfig(True, address)
    mode = 2
    motorValue = [0,0,0,0]
    while mode != 3:
        receivedData = receiver(nrf, address)
        print(mode)
        print(motorValue)
        if button_shutdown.is_pressed : 
            print("sdf")
            mode = 3
        if button_stop.is_pressed : 
            mode = 2
            print("ss")
        if receivedData["code"] == "A" : mode = int(receivedData["value"])
        if receivedData["code"] == "B":
            tempArr = receivedData["value"].split('$')
            for i in range(4):
                value = int(tempArr[i])
                motorValue[i] = value % 1000 if value > 1000 else -1 * (value % 1000)

        mode = mobileRobotMode(mode, motorValue)



# ##### PIN configurations
#
# button_estop = Button(12)
# button_shutdown = Button(16)
# led_stop = LED(7)
# led_wait = LED(8)
# led_operational = LED(25)
# motor_FL = Motor(forward=4, backward=14)
# motor_FR = Motor(forward=17, backward =27)
# motor_BL = Motor(forward=22, backward = 23)
# motor_BR = Motor(forward=10, backward = 9)
#
#
# ##### communication configurations
# address = b'cooop'
#
#
#
# ##### Program starts
#
# # LED_good lights on
#
#
# def mobileRobotEStop():
#     print("estop")
#     led_stop.on()
#     led_operational.off()
#     motor_FL.stop()
#     motor_FR.stop()
#     motor_BL.stop()
#     motor_BR.stop()
#
# def mobileRobotStop():
#     print("stop")
#     led_wait.on()
#    # yellow LED ON
#
# def mobileRobotOperates ():
#     print("operational")
#     led_operational.on()
#     led_wait.off()
#     # green LED ON
#     motor_FL.forward()
#     motor_FR.forward()
#     motor_BL.forward()
#     motor_BR.forward()
#     # motor rotates
#
# def mobileRobotMain(status):
#     while(status !="shutdown"):
#
#         if button_shutdown.is_pressed :
#             status = "estop"
#         elif button_estop.is_pressed :
#             status = "operational"
#
#         if status == "stop":
#             mobileRobotStop()
#         elif status == "operational":
#             mobileRobotOperates()
#         elif status == "estop":
#             mobileRobotEStop()
#
#         time.sleep(0.05)
#
#
# mobileRobotMain("stop")
#
# print("System shudown.")
