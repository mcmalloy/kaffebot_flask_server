#!/usr/bin/env python
# license removed for brevity
import rospy
import json
from std_msgs.msg import Float32
from std_msgs.msg import Int16
import threading


def voltage_callback(data):
    rospy.loginfo("Battery voltage: %s V", data.data)


def voltage_listener():
    rospy.Subscriber("battery/voltage", Float32, voltage_callback)


def current_callback(data):
    rospy.loginfo("Battery current: %s A", data.data)


def current_listener():
    rospy.Subscriber("battery/current", Float32, current_callback)


def batterytemp_callback(data):
    rospy.loginfo("Battery temperature: %s C", data.data)


def battery_temp_listener():
    rospy.Subscriber("battery/temperature", Int16, batterytemp_callback)


def batterycharge_callback(data):
    rospy.loginfo("Battery charge: %s Ah", data.data)


def battery_charge_listener():
    rospy.Subscriber("battery/charge", Float32, batterycharge_callback)


def fetchbatterydata():
    #rospy.init_node('battery_pub')
    print("...Initializing ROS Node...")
    threading.Thread(target=lambda: rospy.init_node('battery_pub', disable_signals=True)).start()
    voltage = rospy.wait_for_message("battery/voltage", Float32, timeout=None)
    current = rospy.wait_for_message("battery/current", Float32, timeout=None)
    charge = rospy.wait_for_message("battery/charge", Float32, timeout=None)
    temp = rospy.wait_for_message("battery/temperature", Int16, timeout=None)
    cap = rospy.wait_for_message("battery/capacity", Float32, timeout=None)
    print("...Converting to JSON...")
    response = {"batteryCharge": charge.data,
                "batteryVoltage": voltage.data,
                "batteryCurrent": current.data,
                "batteryTemp": temp.data,
                "batteryCapacity": cap.data
                }
    return response

def listener():
    rospy.init_node('battery_pub')
    voltage = rospy.wait_for_message("battery/voltage", Float32, timeout=None)
    current = rospy.wait_for_message("battery/current", Float32, timeout=None)
    charge = rospy.wait_for_message("battery/charge", Float32, timeout=None)
    temp = rospy.wait_for_message("battery/temperature", Int16, timeout=None)
    cap = rospy.wait_for_message("battery/capacity", Float32, timeout=None)
    print("Voltage: [V]", voltage)
    print("Current: [A]", current)
    print("Charge: [Ah]", charge)
    print("Temperature: [C]", temp)
    print("Capacity: [Ah]", cap)


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
