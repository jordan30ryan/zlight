import requests
import json
import time
import threading

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

URL = '192.168.6.154'
PORT = ':5000'

# Push button input settings
ButtonChannel = 7
LightChannel = 12
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(ButtonChannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(LightChannel, GPIO.OUT) 


# TODO light output settings

def get_light_color():
    url = 'http://' + URL + PORT
    request = url + '/color'

    try:
        r = requests.get(request)
        return r.text
    except Exception as e:
        print('error getting light color')
        print(e)

def change_light_color():
    url = "http://" + URL + PORT
    request = url + "/color"

    try:
        r = requests.post(request)
        print(r.text)
    except Exception as e: 
        print('error sending light color')
        print(e)

def get_button_input(channel):
    try:
        print('Button was pushed!')
        change_light_color()
    except Exception as e:
        print('error in get_button_input')
        print(e)

def set_light(): 
    while True:
        try:
            c = get_light_color()
            print(c)
            # set light pin to color 
            if c == '3':
                st = GPIO.HIGH
            else:
                st = GPIO.LOW
            GPIO.output(LightChannel, st)

            time.sleep(1)
        except Exception as e:
            print('error in set_light')
            print(e)


def main():
    GPIO.add_event_detect(ButtonChannel, GPIO.RISING, callback=get_button_input, bouncetime=200)
    #t1 = threading.Thread(target=get_button_input)
    t2 = threading.Thread(target=set_light)

    #t1.start()
    t2.start()


if __name__ == '__main__':
    main()


