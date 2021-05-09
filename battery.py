#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32


def callback(data):
    rospy.loginfo("I heard %s", data.data)


def listener():
    rospy.init_node('battery_reader')
    rospy.Subscriber("battery/charge", Float32, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
