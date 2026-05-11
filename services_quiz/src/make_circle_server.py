#! /usr/bin/env python3
import rospy
from math import sqrt
from math import pi
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from services_quiz.srv import MoveInCircle, MoveInCircleResponse

def my_callback(request):
    response = MoveInCircleResponse()
    for i in range(0, request.repetitions):
    	#debug
    	print("Repetition number" + i)
    	verif = make_circle(request.side)
    if not verif:
        print('Error! An obstacle was found.')
        response.complete = False
    else:
        response.complete = True

    return response

def make_circle(radiusVD):
    okVD = 1
    # calculate tangential speed
    velVD.linear.x = velVD.angular.z * radiusVD
    
    # init done angle
    initOdomVD = rospy.wait_for_message(cstODOMVD, Odometry, timeout = 1)
    initAngleVD = initOdomVD.pose.pose.orientation.z
    stopFlagVD = False
    doneAngleVD = 0
    while ok and (not stopFlagVD):
    	# done angle
        crtOdomVD = rospy.wait_for_message(cstODOMVD, Odometry, timeout = 1)
        crtAngleVD = crtOdomVD.pose.pose.orientation.z
        doneAngleVD += crtAngleVD - initAngleVD
        
        # debug
        print("Print done angle: " + doneAngleVD)  
        
        if doneAngleVD > 2 * pi:
        	stopFlagVD = true
        
        
        scanVD = rospy.wait_for_message(cstSCANVD, LaserScan, timeout=1)
        if(scanVD.ranges[90] < 0.2):
        	ok = 0
        
        #debug
        print("Range front: " + scan_inf.ranges[90])
        
        if((not ok) or stopFlagVD):
        	velVD.linear.x = 0
        	velVD.angular.z = 0
        	
        pub.publish(velVD)
        if ok: 
                print('Circle done')
        else:
                print('Obstacle') 
    return ok

def make_circle(duration):
    ok = 1
    
    vel.linear.x = 0.1
    vel.angular.z = 1
    terminate = move_arc(duration)
    return ok 

# init speed cst
cstAngularVD = pi

# init move arg
velVD = Twist()
velVD.linear.x = 0.1
velVD.angular.z = cstAngularVD

# init topics
cstCMDVELVD = '/diffbot/mobile_base_controller/cmd_vel'
cstSCANVD = '/diffbot/scan'
cstODOMVD = '/diffbot/mobile_base_controller/odom'

rospy.init_node('diffbot_make_circle')
my_service = rospy.Service('/make_circle', MoveInCircle, my_callback)
# Create a publisher to the topic /cmd_vel
pub = rospy.Publisher(cstCMDVELVD, Twist, queue_size=1)

rospy.spin()
