import requests
import json

URL = "192.168.6.154"
PORT = ":5000"

# get light status
def get_light_color():
    url = "http://" + URL + PORT
    request = url + "/color"

    try:
        r = requests.get(request)
        print(r.text)
    except:
        print('Something went wrong')


# set light status
# TODO
def set_light_color(color_num):
    url = "http://" + URL + PORT
    request = url + "/color"
    params = { 'color' : color_num }
    params_json = json.dumps(params)

    try:
        r = requests.post(request, params_json)
        print(r.text)
    except:
        print('Something went wrong')


if __name__ == "__main__":
    set_light_color(150)
    get_light_color()
