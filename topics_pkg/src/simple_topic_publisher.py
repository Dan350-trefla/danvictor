#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32


# ii spun rospy-ului ca vreau sa fac ceva
rospy.init_node('topic_publisher')

# daca vreau sa mai fac si altceva
# rospy.init_node('alt nume aici')

# acum ca am un nod, in care fac ce vreau
# imi declar un publisher
# argumente:
# 	1. '/counter' : cum se numeste topicul unde vreau sa umblu. Daca nu exista, se creeaza
# 	2. Int32 : tipul de date
#	3. queue_size : cate elemente bag odata
pub = rospy.Publisher('/counter', Int32, queue_size = 1)

# ros face 2 procesari pe secunda
rate = rospy.Rate(1)

count = Int32()
count.data = 0

# conditie de oprirte "is_shutdown()"
while not rospy.is_shutdown():
	# publica informatie in topic
	pub.publish(count)
	count.data += 1
	# stai degeaba pana cand e cazu sa continui
	rate.sleep()
