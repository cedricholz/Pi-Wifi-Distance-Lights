from gpiozero import LED
import time

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)

led1.on()
led2.on()
led3.on()
led4.on()

time.sleep(10000)