#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int16


def voltage_callback(data):
    rospy.loginfo("Battery voltage: %s V", data.data)


def voltage_listener():
    rospy.Subscriber("battery/voltage", Float32, voltage_callback)

def current_callback(data):
    rospy.loginfo("Battery current: %s A", data.data)


def current_listener():
    rospy.Subscriber("battery/current", Float32, voltage_callback)


def batterytemp_callback(data):
    rospy.loginfo("Battery temperature: %s C", data.data)

def battery_temp_listener():
    rospy.Subscriber("battery/temperature", Int16,batterytemp_callback)

def batterycharge_callback(data):
    rospy.loginfo("Battery charge: %s Ah", data.data)

def battery_charge_listener():
    rospy.Subscriber("battery/charge", Float32, batterycharge_callback)

def listener():
    rospy.init_node('battery_pub')
    voltage_listener()
    current_listener()
    battery_charge_listener()
    battery_temp_listener()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass