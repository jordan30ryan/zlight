import requests
import json
import time
import threading

import board
import neopixel
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

URL = '192.168.6.154'
PORT = ':5000'

# Push button input settings
ButtonChannel = 4
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(ButtonChannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# Neopixel RGB output settings
pixels = neopixel.NeoPixel(board.D18, 1, brightness=0.2)

def get_light_color():
    url = 'http://' + URL + PORT
    request = url + '/color'

    try:
        r = requests.get(request)
        print(r)
        return r.json()['color']
    except Exception as e:
        print('error getting light color')
        raise e

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
            time.sleep(1)

            c = get_light_color()
            colors = hex_to_color_tuple(c)
            print(colors)
            # G, R, B
            pixels[0] = (colors[1], colors[0], colors[2])
        except Exception as e:
            print('error in set_light')
            print(e)


def hex_to_color_tuple(hex_str):
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))


def main():
    GPIO.add_event_detect(ButtonChannel, GPIO.RISING, callback=get_button_input, bouncetime=200)
    #t1 = threading.Thread(target=get_button_input)
    t2 = threading.Thread(target=set_light)

    #t1.start()
    t2.start()


if __name__ == '__main__':
    main()


