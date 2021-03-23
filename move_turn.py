#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def angularMovement(angularmovement):
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('move_pub', anonymous=True)

    move_cmd = Twist()
    if angularmovement == "Right":
        move_cmd.angular.x = 0.5
    if angularmovement == "Left":
        move_cmd.angular.x = -0.5

    move_cmd.linear.x = 0.0
    move_cmd.linear.y = 0.0
    move_cmd.linear.z = 0.0

    move_cmd.angular.y = 0.0
    move_cmd.angular.z = 0.0

    now = rospy.Time.now()
    rate = rospy.Rate(10)

    while rospy.Time.now() < now + rospy.Duration.from_sec(1):
        pub.publish(move_cmd)
        rate.sleep()


if __name__ == '__main__':
    try:
        angularMovement()
    except rospy.ROSInterruptException:
        pass
