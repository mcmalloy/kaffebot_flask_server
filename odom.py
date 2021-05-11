#!/usr/bin/env python
# license removed for brevity
import rospy
import json
from nav_msgs.msg import Odometry
import threading


def fetch_odom_data():
    print("...Initializing ROS Node...")
    threading.Thread(target=lambda: rospy.init_node('battery_pub', disable_signals=True)).start()
    odom_data = rospy.wait_for_message("odom", Odometry, timeout=None)
    print("Odom data: ", odom_data.twist.twist.linear.x)
    return odom_data.twist.twist.linear.x


if __name__ == '__main__':
    try:
        v_x = fetch_odom_data()
        print("Linear velocity x: ", v_x)
    except rospy.ROSInterruptException:
        pass
