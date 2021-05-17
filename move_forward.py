#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import asyncio


def forwardMovement(linearmovement):
    rospy.init_node('movement_node', anonymous=True)
    run_duration = 0.5
    # linearmovement = "Forward"
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    move_cmd = Twist()
    if linearmovement == "Forward":
        move_cmd.linear.x = 0.5
    if linearmovement == "Reversing":
        move_cmd.linear.x = -0.5
    if linearmovement == "Stop":
        move_cmd.linear.x = 0.0
        run_duration = 0.05

    move_cmd.linear.y = 0.5
    move_cmd.linear.z = 0.5
    move_cmd.angular.x = 0.0
    move_cmd.angular.y = 0.0
    move_cmd.angular.z = 0.0

    now = rospy.Time.now()
    rate = rospy.Rate(10)
    print("publishing cmd_vel")
    while rospy.Time.now() < now + rospy.Duration.from_sec(run_duration):
        pub.publish(move_cmd)
        rate.sleep()


if __name__ == '__main__':
    try:
        forwardMovement("Forward")
    except rospy.ROSInterruptException:
        pass
