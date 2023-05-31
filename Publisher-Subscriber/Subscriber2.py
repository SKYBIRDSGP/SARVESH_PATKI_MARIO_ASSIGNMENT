#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'Final Ans : %s', data.data)

def listener():

    
    rospy.init_node('listener_2', anonymous=True)

    rospy.Subscriber('chatter_1', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
