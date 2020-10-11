from gpiozero import Button, MCP3008
import math

## anlaogue Input configurations

port_joy_x = 0
port_joy_y = 1
port_slide = 2

joy_x = MCP3008(port_joy_x)
joy_y = MCP3008(port_joy_y)
slide = MCP3008(port_slide)
## digital Input configutartions

port_button_stop = 3
port_button_start = 2
port_button_shutdown = 4

button_stop = Button(port_button_stop)
button_start = Button(port_button_start)
button_shutdown = Button(port_button_shutdown)
