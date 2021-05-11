#!/usr/bin/env python
# license removed for brevity
import rospy
import time
from std_msgs.msg import Float32
from std_msgs.msg import Int16


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


def listener():
    rospy.init_node('battery_pub')
    voltage = rospy.wait_for_message("battery/voltage", Float32, timeout=None)
    current = rospy.wait_for_message("battery/current", Float32, timeout=None)
    charge = rospy.wait_for_message("battery/charge", Float32, timeout=None)
    temp = rospy.wait_for_message("battery/temperature", Int16, timeout=None)
    print("Voltage: %s [V]", voltage)
    print("Current: %s [A]", current)
    print("Charge: %s [Ah]", charge)
    print("Temperature: %s [C]", temp)


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
