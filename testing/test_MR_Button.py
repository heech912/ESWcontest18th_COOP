from gpiozero import Button
from time import sleep


ports = [2, 3]
Buttons = []

for port in ports :
    Buttons.append(Button(port))

while True:
    for Button_test in Buttons :
        if (Button_test.is_pressed):
            print(Button_test)
    print("######")
    sleep(0.5)
