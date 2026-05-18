cmake_minimum_required(VERSION 3.0.2)
project(actions_quiz)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib_msgs
  std_msgs
)

add_action_files(
  FILES
  Object.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES actions_practice
  CATKIN_DEPENDS rospy actionlib_msgs std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
