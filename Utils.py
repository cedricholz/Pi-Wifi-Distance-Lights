import json
import ftplib
from gpiozero import LED
import random
import time

def dance():
    led1 = LED(17)
    led2 = LED(23)
    led3 = LED(27)
    led4 = LED(22)

    leds = [led1, led2, led3, led4]

    def turnon():
        led1.on()
        led2.on()
        led3.on()
        led4.on()

    def turnoff():
        led1.off()
        led2.off()
        led3.off()
        led4.off()

    prev = -1
    for _ in range(10):
        i = random.randint(0, 3)
        while i == prev:
            i = random.randint(0, 3)
        leds[i].on()
        time.sleep(.5)
        leds[i].off()
        prev = i

    for _ in range(2):
        turnon()
        time.sleep(.5)
        turnoff()
        time.sleep(.5)

    turnon()
    time.sleep(3)
    turnoff()

def button_pressed_dance(lighter_led, names_leds_map, white_led):
    led1 = names_leds_map['sophie']
    led2 = names_leds_map['cedric']
    led3 = names_leds_map['mom_dad']
    led4 = white_led

    leds = [led1, led2, led3, led4]

    def turnon():
        led1.on()
        led2.on()
        led3.on()
        led4.on()

    def turnoff():
        led1.off()
        led2.off()
        led3.off()
        led4.off()

    turnoff()

    prev = -1
    for _ in range(4):
        i = random.randint(0, 3)
        while i == prev:
            i = random.randint(0, 3)
        leds[i].on()
        time.sleep(1)
        leds[i].off()
        prev = i

    turnon()
    time.sleep(1)
    led4.off()
    time.sleep(1)
    for n in names_leds_map:
        names_leds_map[n].off()
        time.sleep(1)
    lighter_led.on()
    time.sleep(3)
    lighter_led.off()



def get_url():
    with open("/home/pi/Pi-Wifi-Distance-Lights/server_info.json") as server_file:
        info = json.load(server_file)
        server_file.close()
    return info['url']
