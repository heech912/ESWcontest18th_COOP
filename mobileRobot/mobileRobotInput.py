from gpiozero import Button

port_button_shutdown = 2
port_button_stop = 3

button_shutdown = Button(port_button_shutdown)
button_stop = Button(port_button_stop)
