#! /usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def factory(pub):
	local_pub = pub
	def callback(msg):
		VDmove = Twist()
		VDmove.angular.x = 0
		VDmove.angular.y = 0
		VDmove.angular.z = 0
		VDmove.linear.x = 0
		VDmove.linear.y = 0
		VDmove.linear.z = 0
		if(msg.ranges[0]] > 1)
			VDmove.linear.x = 1
		elif(msg.ranges[270] < 1)
			VDmove.angular.z = 1.57
		else
			VDmove.angular.z = -1.57
		local_pub.publish(VDmove)
		
	return callback

rospy.init_node('subscriber')
VDpub = rospy.Subscriber('/cmd_vel', LaserScan, queue_size = 1)

VDrate = rospy.rate(1)
VDcallback = factory(VDpub)

VDsub = rospy.Subscriber('/scan', Twist, callback)
cd 
