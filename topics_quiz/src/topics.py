#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msgVD):
    moveVD = Twist()

    if msgVD.ranges[0] > 1.0:
        moveVD.linear.x = 0.2
        moveVD.angular.z = 0.0
        print("loc in fata")
    elif msgVD.ranges[0] < 1.0:
        moveVD.linear.x = 0.0
        moveVD.angular.z = 1
        print("nu e loc in fata")
    elif  msgVD.ranges[270] < 1.0:
        moveVD.linear.x = 0.0
        moveVD.angular.z = 1
        print("nu e loc in dreapta")
    elif msgVD.ranges[90] < 1.0:
        moveVD.linear.x = 0.0
        moveVD.angular.z = -1
        print("nu e loc in stanga")

    pubVD.publish(moveVD)

# init
rospy.init_node('turtlebot_topics_node')
pubVD = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
subVD = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
