from gpiozero import LED, Button
import Utils as utils
import time

#Cedric 27
#Mom_Dad 22
#Sophie 17
#White 23

filename = 'listener_data.json'

my_name = "mom_dad"

button1_name = "cedric"
button2_name = "sophie"

white_led = LED(23)

names_leds_map = {"cedric":LED(27), "sophie":LED(17), "mom_dad":LED(22)}

def check_for_updates():
    while True:
        utils.get_file_from_ftp_server(filename)
        listener_data = utils.file_to_json(filename)

        my_lamp_lighters = listener_data[my_name]['lamp_lighters']

        times_lit = listener_data[my_name]['times_lit']

        updated_lamp_lighters = my_lamp_lighters[:]
        updated_times_lit = times_lit[:]

        cur_time = time.time()
        for i in range(len(my_lamp_lighters)):
            lighter = my_lamp_lighters[i]
            time_lit = times_list[i]

            total_time_lit = cur_time - time_lit

            #Times up
            if total_time_lit > 7200:
                names_leds_map[lighter].off()
                del updated_lamp_lighters[i]
                del updated_times_lit[i]

            else:
                names_leds_map[lighter].on()

        if len(my_lamp_lighters) != len(updated_lamp_lighters):
            listener_data[my_name]['lamp_lighters'] = updated_lamp_lighters
            listener_data[myname]['times_lit'] = updated_times_lit

            utils.json_to_file(listener_data, filename)
            utils.send_to_ftp_server(filename)

        time.sleep(0.25)

def button_pressed(lamp_to_light):
    white_led.on()

    utils.get_file_from_ftp_server(filename)
    listener_data = utils.file_to_json(filename)

    cur_time = time.time()

    listener_data[lamp_to_light]['lamp_lighters'].append(my_name)
    listener_data[lamp_to_light]['times_lit'].append(cur_time)

    my_lamp_lighters = listener_data[my_name]['lamp_lighters']

    if lamp_to_light in my_lamp_lighters:
        listener_data[my_name]['lamp_lighters'].append(my_name)
        listener_data[my_name]['times_lit'].append(cur_time)


    utils.json_to_file(listener_data, filename)
    utils.send_to_ftp_server(filename)

def button_released():
    white_led.off()


button1 = Button(2)
button2 = Button(3)

button1.when_pressed = lambda : button_pressed(button1_name)
button1.when_released = button_released

button2.when_pressed = lambda : button_pressed(button2_name)
button2.when_released = button_released

check_for_updates()
