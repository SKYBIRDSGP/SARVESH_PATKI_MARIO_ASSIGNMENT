#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) #(name datatype string_length)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
   
    while not rospy.is_shutdown(): #chatter is not running
        num_1=5
        num_2=10
        sign='+'
        rospy.loginfo(str(num_1))
        pub.publish(str(num_1))

        rospy.loginfo(str(num_2))
        pub.publish(str(num_2))

        rospy.loginfo(str(sign))
        pub.publish(str(sign))
        rate.sleep()
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:   #to close the program
        pass
