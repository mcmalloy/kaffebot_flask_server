#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys

def talker(move_straight,turn,duration):
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	rospy.init_node('move_pub', anonymous=True)

	turn_time = duration

	_moveStraight = Twist()
	_moveStraight.linear.x = move_straight
	_moveStraight.angular.z = 0.0

	_turn = Twist()
	_turn.angular.z = turn

	now = rospy.Time.now()
	rate = rospy.Rate(10)	

	while rospy.Time.now() < now + rospy.Duration.from_sec(2):
		pub.publish(_moveStraight)

	now = rospy.Time.now()

	while rospy.Time.now() < now + rospy.Duration.from_sec(turn_time):
		pub.publish(_turn)
		rate.sleep()


if __name__ == '__main__':
	move_straight = float(sys.argv[1])
	turn = float(sys.argv[2])
	duration = float(sys.argv[3])

	try:
		talker(move_straight, turn, duration)
		talker(move_straight, turn, duration)
		talker(move_straight, turn, duration)
		talker(move_straight, turn, duration)
	except rospy.ROSInterruptException: pass
