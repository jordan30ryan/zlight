import requests

URL = "192.168.6.154"
PORT = "5000"

# get light status
def get_light_color():
    url = "http://" + URL + PORT
    request = url + "/color"
    r = requests.get(request)
    print(r)

# set light status
# TODO

if __name__ == "__main__":
    get_light_color()
