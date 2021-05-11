import json
from flask import Flask
from flask import request
import rospy
import battery
app = Flask(__name__)


@app.route('/battery', methods=['GET'])
def home():
    # FETCH DATA FROM PUBLISHER
    # RETURN DATA TO APPLICATION
    response = battery.fetchbatterydata()
    print("Returning battery response: ")
    print(response)
    return response


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
    rospy.init_node('battery_pub')
    app.run(host='0.0.0.0')
