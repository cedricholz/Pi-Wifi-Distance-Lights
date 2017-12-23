from gpiozero import LED, Button
import time

led1 = LED(17)
led2 = LED(27)

button1 = Button(2)
button2 = Button(3)

button1.when_pressed = led1.on
button2.when_pressed = led2.on

button1.when_released = led1.off
button2.when_released = led2.off

time.sleep(10000)
