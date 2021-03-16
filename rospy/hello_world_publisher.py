#!/usr/bin/env python
import rospy
#from std_msgs.msg import String
from geometry_msgs.msg import Twist
def talker():
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	rospy.init_node('hello_world_publisher', anonymous=True)
	r = rospy.Rate(1) # 10hz
	
	while not rospy.is_shutdown():
		#str = "battery level: %s"%rospy.get_time()
		str = "['linear', 'angular']"
		rospy.loginfo(str)
		pub.publish(str)
		r.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass
