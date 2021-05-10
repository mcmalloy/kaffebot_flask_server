#!/usr/bin/env python
# license removed for brevity
import rospy
import time
from std_msgs.msg import Float32
from std_msgs.msg import Int16


class bat:

    def __init__(self, voltage, current, ah, temp):
        self.voltage = voltage
        self.current = current
        self.ah = ah
        self.temp = temp

    def voltage_callback(data):
        rospy.loginfo("Battery voltage: %s V", data.data)

    def voltage_listener(self):
        rospy.Subscriber("battery/voltage", Float32, self.voltage)

    def current_callback(data):
        rospy.loginfo("Battery current: %s A", data.data)

    def current_listener(data):
        rospy.Subscriber("battery/current", Float32, bat.current_callback)

    def batterytemp_callback(data):
        rospy.loginfo("Battery temperature: %s C", data.data)

    def battery_temp_listener(data):
        rospy.Subscriber("battery/temperature", Int16, bat.batterytemp_callback)

    def batterycharge_callback(data):
        rospy.loginfo("Battery charge: %s Ah", data.data)

    def battery_charge_listener(self):
        rospy.Subscriber("battery/charge", Float32, bat.batterycharge_callback)

    def listener(self):
        rospy.init_node('battery_pub')
        bat.voltage_listener(self)
        bat.current_listener()
        bat.battery_charge_listener()
        bat.battery_temp_listener()
        time.sleep(3)
        print("And the voltage: ")
        print(self.voltage)
    # spin() simply keeps python from exiting until this node is stopped


