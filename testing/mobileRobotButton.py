from gpiozero import Button
import time

port_button_shutdown = 2
port_button_stop = 3

button_shutdown = Button(port_button_shutdown)
button_stop = Button(port_button_stop)

def mobileRobotbuttontest():
    while True:
        if button_shutdown.is_pressed : print("Shutdown")
        elif button_stop.is_pressed : print("Stop")
        time.sleep(0.5)

mobileRobotbuttontest()
