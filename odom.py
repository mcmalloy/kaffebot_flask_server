#!/usr/bin/env python
# license removed for brevity
import rospy
import json
from nav_msgs.msg import Odometry
import threading
import move_forward

def listen_to_odom():
    odom_data = rospy.wait_for_message("odom", Odometry, timeout=None)
    return odom_data.twist.twist.linear.x


if __name__ == '__main__':
    try:
        initialize_odom()
        v_x = listen_to_odom()
        print("Linear velocity x: ", v_x)
    except rospy.ROSInterruptException:
        pass
