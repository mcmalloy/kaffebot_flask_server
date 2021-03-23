import json


def getBattery():
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
