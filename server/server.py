from flask import Flask
from flask import request
import json 

app = Flask(__name__)

COLOR = { 'color' : 0 }

@app.route('/color', methods=['POST', 'GET'])
def manage_color():
    if request.method == 'POST':
        parameters = json.loads(request.data)
        color = parameters['color']
        print(color)
        set_color(color)
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
