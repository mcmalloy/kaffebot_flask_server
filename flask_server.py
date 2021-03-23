import json
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/battery', methods=['GET'])
def home():
    # FETCH DATA FROM PUBLISHER
    # RETURN DATA TO APPLICATION
    batteryPercent = 76.5
    batteryVoltage = 4.94
    batteryCurrent = 1.2
    # Python object (dict) called response:
    response = {"batteryPercent": batteryPercent,
        "batteryVoltage": batteryVoltage,
        "batteryCurrent": batteryCurrent
    }
    # CONVERT TO JSON
    jsonResponse = json.dumps(response)
    return str(jsonResponse)


@app.route('/squaremovement', methods=['POST', 'GET'])
def squaremovement():
    if request.method == 'GET':
        print("Getting last known data of square movement")
        return "Getting last known data of square movement"
    if request.method == 'POST':
        size = float(request.args.get('size', None))
        print("Posting new square movement with this size: ")
        print(size)
        test(size)
        return 'OK'


def test(size):
    print("roger that, i got the size: " + str(size))


if __name__ == '__main__':
    app.run()
