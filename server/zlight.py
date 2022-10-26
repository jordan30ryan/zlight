from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask_httpauth import HTTPTokenAuth
import json 

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

auth = HTTPTokenAuth(scheme='Bearer')
key = open("/usr/etc/key", "r").readline().rstrip('\n')

PURPLE = 'a64dff'
GREEN = '00b359'
OLIVE = '264c00'
DERRY = '0000fe'
PANCAKE = '83c1ff'

COLOR_ORDER = [PURPLE, GREEN, OLIVE, DERRY, PANCAKE]

COLOR = { 'color' : PURPLE, 'index' : 0 }

@auth.verify_token
def verify_token(token): 
    return token == key

@app.route('/color', methods=['POST', 'GET'])
@auth.login_required
@cross_origin()
def manage_color():
    if request.method == 'POST':
        if request.data:
            parameters = json.loads(request.data)
            color = parameters['color']
            print(color)
            set_color(color)
        else:
            set_color_serverside()
        return 'success'
    if request.method == 'GET':
        color = get_color()
        return {'color': color}
    return


def get_color():
    return COLOR['color']

def set_color(new_color):
    COLOR['color'] = new_color
    return

def set_color_serverside():
    idx = COLOR['index']
    idx2 = (idx + 1) % len(COLOR_ORDER)
    COLOR['index'] = idx2
    COLOR['color'] = COLOR_ORDER[idx2]
    return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
