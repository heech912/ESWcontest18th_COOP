from gpiozero import LED

port_LED_red = 22
port_LED_yellow = 27
port_LED_green = 17

LED_red = LED(port_LED_red)
LED_yellow = LED(port_LED_yellow)
LED_green = LED(port_LED_green)
