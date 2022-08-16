from flask import Flask
from flask import request
import json 

app = Flask(__name__)

COLOR = { 'color' : 0 }

@app.route('/color', methods=['POST', 'GET'])
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
        return str(color)
    return


def get_color():
    return COLOR['color']

def set_color(new_color):
    COLOR['color'] = new_color
    return

def set_color_serverside():
    COLOR['color'] = COLOR['color'] + 1
    return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
