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

    for _ in range(10):
        i = random.randint(0, 3)
        leds[i].on()
        time.sleep(.5)
        leds[i].off()

    for _ in range(2):
        turnon()
        time.sleep(.5)
        turnoff()
        time.sleep(.5)

    turnon()
    time.sleep(3)
    turnoff()

def get_file_from_ftp_server(filename):
    try:
        with open("ftp_server_info.json") as server_file:
            info = json.load(server_file)
            server_file.close()

        session = ftplib.FTP(info['ip'], info['user'], info['pass'])

        localfile = open(filename, 'wb')
        session.retrbinary('RETR public_html/' + filename, localfile.write, 1024)

        session.quit()
        localfile.close()
    except:
        print("Error retrieving File")


def get_url():
    with open("server_info.json") as server_file:
        info = json.load(server_file)
        server_file.close()
    return info['url']


def send_to_ftp_server(filename):
    try:
        with open("ftp_server_info.json") as server_file:
            info = json.load(server_file)
            server_file.close()

        session = ftplib.FTP(info['ip'], info['user'], info['pass'])
        file = open(filename, 'rb')
        session.storbinary('STOR public_html/' + filename, file)
        file.close()
        session.quit()
    except:
        print("No ftp info on file")



def file_to_json(filename):
    try:
        file = open(filename, 'r')
        contents = str(file.read())
        posts = json.loads(contents)
        file.close()
        return posts
    except FileNotFoundError:
        print("No such file: " + filename)
        exit(1)


def json_to_file(json_obj, filename):
    try:
        file = open(filename, 'w')
        json.dump(json_obj, file, sort_keys=True, indent=4, separators=(',', ': '))
        file.close()
    except FileNotFoundError:
        print("No such file: " + filename)
        exit(1)


