#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32


def callback(data):
    rospy.loginfo("I heard %s V", data.data)


def listener():
    print("yo")
    rospy.init_node('charge_pub')
    rospy.Subscriber("battery/voltage", Float32, callback)
    val = rospy.get_param("~battery_voltage", 30)
    print("Got this value: ")
    print(val)
    rospy.loginfo(val)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass