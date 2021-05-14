#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import odom
import websockets
import asyncio



def forwardMovement(linearmovement, websocket):
    run_duration = 0.5
    #linearmovement = "Forward"
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('move_pub', anonymous=True)

    move_cmd = Twist()
    if linearmovement == "Forward":
        move_cmd.linear.x = 0.5
    if linearmovement == "Reversing":
        move_cmd.linear.x = -0.5

    move_cmd.linear.y = 0.5
    move_cmd.linear.z = 0.5

    move_cmd.angular.x = 0.0
    move_cmd.angular.y = 0.0
    move_cmd.angular.z = 0.0

    now = rospy.Time.now()
    rate = rospy.Rate(10)
    odom.initialize_odom()
    while rospy.Time.now() < now + rospy.Duration.from_sec(run_duration):
        pub.publish(move_cmd)
        velocity_x = odom.listen_to_odom()
        print("Velocity: ",velocity_x)
        sendVelocity(velocity_x, websocket)
        rate.sleep()

async def sendVelocity(velocity, websocket):
    await websocket.send(velocity)


if __name__ == '__main__':
    try:
        forwardMovement()
    except rospy.ROSInterruptException:
        pass
