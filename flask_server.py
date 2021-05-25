import json
from flask import Flask
from flask import request
import random
app = Flask(__name__)


@app.route('/battery', methods=['GET'])
def home():
    # FETCH DATA FROM PUBLISHER
    # RETURN DATA TO APPLICATION
    response = {"batteryCharge": 2.1,
                "batteryVoltage": 14.4,
                "batteryCurrent": 0.1,
                "batteryTemp": 25,
                "batteryCapacity": 2.6
                }
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
        # Odom movement should be logged in the duration and returned with JSON
        print(str(request.args.get('command', None)))
        #move_forward.forwardMovement(str(request.args.get('command', None)))
        if command == "forward":
            return {"velocity": random.randrange(30, 100,1),
                    "rotation": 0}
        elif command == "backwards":
            return {"velocity": -1*random.randrange(30, 100, 1),
                    "rotation": 0}
        elif command == "right":
            return {"velocity": 0,
                    "rotation": random.randrange(0, 10, 1)}
        elif command == "left":
            return {"velocity": 0,
                    "rotation": -1*random.randrange(0, 10, 1)}
        elif command == "stop":
            return {"velocity": 0,
                    "rotation": 0}
        else:
            return{"Error"}


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='localhost')
