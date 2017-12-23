from gpiozero import LED, Button
import Utils as utils
import time
from firebase import firebase
import sys

#Cedric 27
#Mom_Dad 22
#Sophie 17
#White 23

# my_name = "cedric"
# button1_name = "sophie"
# button2_name = "mom_dad"

my_name = sys.argv[1]
button1_name = sys.argv[2]
button2_name = sys.argv[3]


white_led = LED(23)

names_leds_map = {"cedric":LED(27), "sophie":LED(17), "mom_dad":LED(22)}

button_is_pressed = False

time_to_stay_lit = 7200

url = utils.get_url()
firebase = firebase.FirebaseApplication(url, None)


def add_member1_to_member2s_lamp_lighters(member1, member2):
    lamp_lighters = get_lamp_lighters(member2)
    lit_times = get_lit_times(member2)

    cur_time = time.time()

    if lamp_lighters == None:
        lamp_lighters = [member1]
        lit_times = [cur_time]
    else:
        if member1 in lamp_lighters:
            index = lamp_lighters.index(member1)
            lit_times[index] = cur_time
        else:
            lamp_lighters.append(member1)
            lit_times.append(cur_time)

    firebase.put('family_members', member2, {'lamp_lighters': lamp_lighters, 'lit_times':lit_times})


def get_lamp_lighters(family_member):
    return firebase.get('/family_members/' + family_member + '/lamp_lighters', None)


def get_lit_times(family_member):
    return firebase.get('/family_members/' + family_member + '/lit_times', None)


def check_for_updates():
    while True:

        my_starting_lamp_lighters = get_lamp_lighters(my_name)

        if my_starting_lamp_lighters != None:

            my_lamp_lighters = my_starting_lamp_lighters[:]

            for lighter in my_lamp_lighters:
                names_leds_map[lighter].on()

            my_lit_times = get_lit_times(my_name)

            cur_time = time.time()
            starting_length = len(my_lamp_lighters)
            for i in range(len(my_starting_lamp_lighters)):
                index = len(my_starting_lamp_lighters) - 1 - i

                time_lit = my_lit_times[index]

                total_time_lit = cur_time - float(time_lit)

                lighter = my_lamp_lighters[index]
                #Times up
                if total_time_lit > time_to_stay_lit:
                    names_leds_map[lighter].off()
                    del my_lamp_lighters[index]
                    del my_lit_times[index]
                else:
                    names_leds_map[lighter].on()
            if len(my_lamp_lighters) == 3:
                white_led.on()
            else:
                white_led.off()

            if len(my_lamp_lighters) != len(my_starting_lamp_lighters):
                firebase.put('family_members', my_name, {'lamp_lighters': my_lamp_lighters, 'lit_times': my_lit_times})

        time.sleep(1)

def button_pressed(loved_one):
    white_led.off()
    sleep(.2)
    white_led.on()

    add_member1_to_member2s_lamp_lighters(my_name, loved_one)

    add_member1_to_member2s_lamp_lighters(my_name, my_name)



def button_released():
    white_led.off()


button1 = Button(2)
button2 = Button(3)

button1.when_pressed = lambda : button_pressed(button1_name)
button1.when_released = button_released

button2.when_pressed = lambda : button_pressed(button2_name)
button2.when_released = button_released

check_for_updates()