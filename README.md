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



