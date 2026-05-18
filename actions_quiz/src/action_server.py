#! /usr/bin/env python
import rospy

import actionlib
from actions_quiz.msg import ObjectFeedback, ObjectResult, ObjectAction
from ardrone_autonomy.msg import Navdata

# types
from std_msgs.msg import Empty

# import your custom messages

class ActionServerVD():
    
  # create messages that are used to publish feedback/result
  _feedbackVD = ObjectFeedback()
  _resultVD   = ObjectResult()
  _asVD = None

  _takeoffTopicNameVD = "/ardrone/takeoff"
  _landTopicNameVD = "/ardrone/land"
  _navdataTopicNameVD = "/ardrone/navdata"

  _takeoffPubVD = None
  _landPubVD = None

  _lastAction = "LAND"

  def goal_callback(goal) :
    pyStr = str(goal.data)
    msg = Empty()
    if pyStr == "LAND" :
        self._landPubVD.publish(msg)
        state = 8
        while state == 8 and (not self._asVD.is_preempt_requested()):
            try:
                state = rospy.wait_for_message(self._navdataTopicNameVD, Navdata, 3)
                self._feedback.curVD = "LAND"
                self._asVD.publish_feedback(self._feedbackVD)
            except Exception as e:
                state = -1
                print(e)
            rospy.sleep(1)
    elif pyStr == "TAKEOFF" :
        self._takeoffPubVD.publish(msg)
        state = 6
        while state == 6 and (not self._asVD.is_preempt_requested()):
            try:
                state = rospy.wait_for_message(self._navdataTopicNameVD, Navdata, 3)
                self._feedback.curVD = "LAND"
                self._asVD.publish_feedback(self._feedbackVD)
            except Exception as e:
                state = -1
                print(e)
            rospy.sleep(1)
    else :
        print("invalid goal")
        return
    if self._asVD.is_preempt_requested() :
        print("preempted")
    else :
        self._asVD.set_succeeded(self._resultVD)

  def __init__(self):
    print("init topics")
    self._takeoffPubVD = rospy.Publisher(self._takeoffTopicNameVD, Empty(), queue_size = 1)
    self._landPubVD = rospy.Publisher(self._landTopicNameVD, Empty(), queue_size = 1)
    # let the pubs init
    rospy.sleep(2)
    print("topics init'd")
    # creates the action server
    self._as = actionlib.SimpleActionServer("TLVD", ObjectAction, self.goal_callback, False)
    self._as.start()





    
  def goal_callback(self, goal):
    # this callback is called when the action server is called
    
    # your code here

    
    self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
  rospy.init_node('TLVD')
  ActionServerVD()
  rospy.spin()
