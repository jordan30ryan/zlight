import requests
import json
import time
import threading

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

URL = '192.168.6.154'
PORT = ':5000'

# Push button input settings
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

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

def get_button_input():
    while True:
        try:
            if GPIO.input(10) == GPIO.HIGH:
                print('Button was pushed!')
                set_light_color()
        except Exception as e:
            print('error in get_button_input')
            print(e)

def set_light(): 
    while True:
        try:
            c = get_light_color()
            # set light pin to color 
            print(c)
            time.sleep(5)
        except Exception as e:
            print('error in set_light')
            print(e)


def main():
    change_light_color()
    t1 = threading.Thread(target=get_button_input)
    t2 = threading.Thread(target=set_light)

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()


