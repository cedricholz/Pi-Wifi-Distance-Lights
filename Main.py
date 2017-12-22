from gpiozero import LED, Button
import Utils as utils
import time

#Cedric 27
#Mom_Dad 22
#Sophie 17
#White 23

filename = 'listener_data.json'

my_name = "sophie"

button1_name = "cedric"
button2_name = "mom_dad"

white_led = LED(23)

names_leds_map = {"cedric":LED(27), "sophie":LED(17), "mom_dad":LED(22)}

button_is_pressed = False

time_to_stay_lit = 7200

def check_for_updates():
    while True:
        if not button_is_pressed:
            utils.get_file_from_ftp_server(filename)
            listener_data = utils.file_to_json(filename)

            my_lamp_lighters = listener_data[my_name]['lamp_lighters']

            times_lit = listener_data[my_name]['times_lit']

            cur_time = time.time()
            for i in range(len(my_lamp_lighters)):
                index = len(my_lamp_lighters) - 1 - i

                time_lit = times_lit[index]

                total_time_lit = cur_time - time_lit

                lighter = my_lamp_lighters[index]
                #Times up
                if total_time_lit > time_to_stay_lit:

                    names_leds_map[lighter].off()
                    del my_lamp_lighters[index]
                    del times_lit[index]
                else:

                    names_leds_map[lighter].on()

            if len(my_lamp_lighters) != len(listener_data[my_name]['lamp_lighters']):
                listener_data[my_name]['lamp_lighters'] = my_lamp_lighters
                listener_data[myname]['times_lit'] = times_lit

                utils.json_to_file(listener_data, filename)
                utils.send_to_ftp_server(filename)

        time.sleep(1)

def button_pressed(loved_one):
    try:
        button_is_pressed = True
        white_led.on()

        utils.get_file_from_ftp_server(filename)
        listener_data = utils.file_to_json(filename)

        persons_lighters = listener_data[loved_one]['lamp_lighters']

        my_lighters = listener_data[my_name]['lamp_lighters']

        cur_time = time.time()

        # Update time
        if my_name in persons_lighters:
            index = persons_lighters.index(my_name)
            listener_data[loved_one]['times_lit'][index] = cur_time
        else:
            listener_data[loved_one]['lamp_lighters'].append(my_name)
            listener_data[loved_one]['times_lit'].append(cur_time)

        # Reciprocate
        if loved_one in my_lighters:
            if my_name in my_lighters:
                index = my_lighters.index(my_name)
                listener_data[my_name]['times_lit'][index] = cur_time
            else:
                listener_data[my_name]['lamp_lighters'].append(my_name)
                listener_data[my_name]['times_lit'].append(cur_time)


        utils.json_to_file(listener_data, filename)
        utils.send_to_ftp_server(filename)

        button_is_pressed = False
    except:
        button_pressed(loved_one)



def button_released():
    white_led.off()


button1 = Button(2)
button2 = Button(3)

button1.when_pressed = lambda : button_pressed(button1_name)
button1.when_released = button_released

button2.when_pressed = lambda : button_pressed(button2_name)
button2.when_released = button_released

check_for_updates()

# Stay on
# import time
#
#
# time.sleep(10000)