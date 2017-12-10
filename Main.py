from gpiozero import LED, Button
import signal
import Utils as utils
import time

filename = 'listener_data.json'

my_name = "cedric"
my_led = LED(0)

my_led.on()

names_leds_map = {"mom_dad":LED(1), "sophie":LED(2)}

def check_for_updates():
    while True:
        utils.get_file_from_ftp_server(filename)
        listener_data = utils.file_to_json(filename)

        my_lamp_lighter = listener_data[my_name]

        if lit_time != 0:
            cur_time = time.time()
            total_time_lit = time.time() - listener_data[lit_time]

            if total_time_lit > 3600:
                names_leds_map[my_lamp_lighter].off()
                names_leds_map[my_name].on()
                listener_data[lamp_lighter] = "None"
                listener_data[lit_time] = 0
                utils.json_to_file(listener_data, filename)
                utils.send_to_ftp_server(filename)
        time.sleep(0.25)

def button_pressed(lamp_to_light):
    utils.get_file_from_ftp_server(filename)
    listener_data = utils.file_to_json(filename)
    lamp_to_light = buds[lamp_to_light]
    listener_data[lamp_to_light] = my_name
    listener_data[lit_time] = time.time()
    utils.send_to_ftp_server(filename)


buttons = [Button(1), Button(2)]

button_one = Button(1)
button_two = Button(2)

button_one.when_pressed = lambda : button_pressed(1)

button_two.when_pressed = lambda : button_pressed(2)

check_for_updates

pause()