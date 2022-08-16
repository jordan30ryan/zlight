from flask import Flask
from flask import request

app = Flask(__name__)

COLOR = { 'color' : 0 }

# GET color
@app.route('/color', methods=['POST', 'GET'])
def manage_color():
    if request.method == 'POST':
        color = request.form['color']
        print(color)
        db_set_color(color)
        return 'success'
    if request.method == 'GET':
        color = db_get_color()
        return str(color)
    return


def db_get_color():
    return COLOR['color']

def db_set_color(new_color):
    COLOR['color'] = new_color
    return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
