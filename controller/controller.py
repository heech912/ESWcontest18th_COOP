##### CO-OP Demo
##### Controller

# from gpiozero import LED, Button, MCP3008
import time

from communication import nrfConfig, transmitter, encodeData
from controller.controllerInput import joy_x, joy_y, slide, button_stop, button_shutdown, button_start
from controller.controllerOutput import LED_red, LED_green, LED_yellow
from utility import simpleControl


modeCode = [
        {"name" : "stop", "num" : 0},
        {"name" : "start", "num" : 1},
        {"name" : "wait", "num" : 2},
        {"name" : "shutdown", "num" : 3},
        ]

def controllerMode(mode, x, y, nrf, address):
    LED_red.off()
    LED_green.off()
    LED_yellow.off()
    if mode == 0:
        LED_red.on()
        for i  in range(3):
            transmitter(nrf, address, "0" , "A")
            time.sleep(1)
        return 2
    elif mode == 1 :
        motorString = simpleControl(x,y)
        print(motorString)
        transmitter(nrf, address, motorString , "B")
        LED_green.on()
        return 1
    elif mode == 2 :
        LED_yellow.on()
        return 2
    elif mode == 3:
        return 3



def controllerMain(address):
    nrf = nrfConfig(False, address)
    mode = 2
    while mode != 3:
        transmitter(nrf, address, modeCode[mode]["num"], "A")
        if button_stop.is_pressed:
            mode = 0
        if button_start.is_pressed :
            mode = 1
        if button_shutdown.is_pressed:
            mode = 3

        mode = controllerMode(mode, joy_x.value, joy_y.value, nrf, address)



# ##### Button Configurations
#
# Red_button = Button(2)					##### All robot stop
# Grey_button = Button(24)				##### Switch of power
# Green_button = Button(23)				##### Ready
#
# ##### led configurations
#
# Red_led = LED(5)
# Blue_led = LED(3)
# Green_led = LED(4)
#
# ##### MCP channels configurations
#
# joy_x = MCP3008(0)
# joy_y = MCP3008(1)
# slide_distance = MCP3008(2)
# d = 64.075
#
# ##### Controll function
#
# modeEnum = { "Stop" : 0, "Operational":1, "Shutdown" : 2}
#
# def control(Operation_status):
#
#     while (Operation_status != "Shutdown"):
#
#         x = (joy_x.value - 1/2)*2
#         y = (joy_y.value - 1/2)*2
#         s = slide_distance.value*1000 +2*d
#         m = 1/np.abs(x)
#
#         if Red_button.is_pressed:
#             Operation_status = "Stop"
#         if Green_button.is_pressed:
#             Operation_status = "Operational"
#         if Grey_button.is_pressed:
#             LL_value = 0
#             LR_value = 0
#             RL_value = 0
#             RR_value = 0
#             Red_led.on()
#             time.sleep(0.5)
#             Red_led.off()
#             time.sleep(0.5)
#             Red_led.on()
#             time.sleep(0.5)
#             Red_led.off()
#             time.sleep(0.5)
#             Operation_status = "Shutdown"
#
#         if (Operation_status == "Operational"):
#             Blue_led.off()
#             Red_led.off()
#             Green_led.on()
#
#             if x < -0.01 :
#
#                 LL_value = ((x**2+y**2)**(1/2)) * ((m - d)/(m + s/2)) /3
#                 LR_value = ((x**2+y**2)**(1/2)) * ((m + d)/(m + s/2)) /3
#                 RL_value = ((x**2+y**2)**(1/2)) * ((m + s - d)/(m + s/2)) /3
#                 RR_value = ((x**2+y**2)**(1/2)) * ((m + s + d)/(m + s/2)) /3
#
#             elif x > 0.01 :
#
#                 LL_value = (x**2+y**2)**(1/2) * (m + s + d)/(m + s/2) /3
#                 LR_value = (x**2+y**2)**(1/2) * (m + s - d)/(m + s/2) /3
#                 RL_value = (x**2+y**2)**(1/2) * (m + d)/(m + s/2) /3
#                 RR_value = (x**2+y**2)**(1/2) * (m - d)/(m + s/2) /3
#
#             else:
#                 if -0.01 < y < 0.01:
#                     LL_value = 0
#                     LR_value = 0
#                     RL_value = 0
#                     RR_value = 0
#
#                 else :
#                     LL_value = y
#                     LR_value = y
#                     RL_value = y
#                     RR_value = y
#
#         elif (Operation_status == "Stop") :
#
#             Red_led.off()
#             Green_led.off()
#             Blue_led.on()
#
#             LL_value = 0
#             LR_value = 0
#             RL_value = 0
#             RR_value = 0
#
#         #print(LL_value, LR_value, RL_value, RR_value)
#         print(Operation_status)
#         master(b'coop', modeEnum[Operation_status])
#         master(b'soso', modeEnum[Operation_status])
#         time.sleep(0.05)
#
# control("Stop")
