import json
from flask import Flask
from flask import request
import battery
import move_forward
app = Flask(__name__)


@app.route('/battery', methods=['GET'])
def home():
    # FETCH DATA FROM PUBLISHER
    # RETURN DATA TO APPLICATION
    response = battery.fetchbatterydata()
    print("Returning battery response: ")
    print(response)
    return response


@app.route('/move', methods=['POST', 'GET', 'DELETE'])
def move():
    command = str(request.args.get('command', None))
    if request.method == 'GET':
        # Call movement method
        return "Getting last known data of square movement"
    if request.method == 'POST':
        print(str(request.args.get('command', None)))
        move_forward.forwardMovement(str(request.args.get('command', None)))
        return 'OK'


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='localhost')
