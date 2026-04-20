#! /usr/bin/env python3

import rospy
# from std_msgs.msg import ...

rospy.init_node('publisher')
pub = rospy.Publisher('/cmd_vel', ..., queue_size = 1)

rate = rospy.Rate(1)

while not rospy.is_shutdown():
	pub.publish(...)
	rate.sleep()
