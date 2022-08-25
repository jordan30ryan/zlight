# Color change lights server

## Server
get/change color of light


## Devices
on startup, get light color and set 

on button press, contact server to change color 


## Setup
pip install Flask
pip install rpi.gpio
pip install -U flask-cors


add to /etc/rc.local:
python /home/pi/src/zlight/client/client.py &

RGB LED Control
https://jackw01.github.io/led-control/

commenting out the line dtparam=audio=on in /boot/config.txt


    sudo apt-get install scons swig libev-dev python3-dev python3-setuptools
    git clone --recurse-submodules https://github.com/jackw01/led-control.git
    cd led-control
    git checkout tags/v2.0.0
    pip install pytest-runner
    pip install wheel
    python -m pip install --upgrade pip
    python -m ensurepip
    sudo su
    python3 setup.py develop
    ledcontrol --led_count 150 (add --led_pixel_order GRBW if using RGBW LEDs)


## AWS Notes
Create EC2




