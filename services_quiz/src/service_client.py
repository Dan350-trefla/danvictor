#! /usr/bin/env python3

# This is where you will publish the velocity messages to the turtlebot and subscribe to its laserscan data.


import rospy  # Import the Python library for ROS_msgs package
from sensor_msgs.msg import LaserScan
from services_quiz.srv import MoveInCircle, MoveInCircleResponse, MoveInCircleRequest
import sys

rospy.init_node('move_in_circle_node')  # Initiate a Node

rospy.wait_for_service('/make_circle')
move_in_circle = rospy.ServiceProxy('/make_circle', MoveInCircle)

move_in_circle_object = MoveInCircleRequest(2, 3)
complete = move_in_circle(move_in_circle_object)
