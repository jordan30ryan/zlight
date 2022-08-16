import requests

URL = "192.168.6.154"
PORT = ":5000"

# get light status
def get_light_color():
    url = "http://" + URL + PORT
    request = url + "/color"
    r = requests.get(request)
    print(r.text)

# set light status
# TODO
def set_light_color(color_num):
    url = "http://" + URL + PORT
    request = url + "/color"
    params = { 'color' : color_num }
    r = requests.post(request, params)
    print(r.text)

if __name__ == "__main__":
    set_light_color(21)
    get_light_color()
