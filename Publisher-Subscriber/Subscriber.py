#!/usr/bin/env python3
import rospy
from std_msgs.msg import String




def callback(data):
    global to_measure
    global recieved_numbers
    global counter
    global num
    global sign
    if not data.data.isdigit():
         rospy.loginfo(rospy.get_caller_id() + 'sign : %s', data.data)
         sign = (data.data)
         to_measure=True 

    else:
        rospy.loginfo('checking the numbers')
        if to_measure:
            num[counter] = data.data
            counter = counter + 1
            if counter>=2:
                to_measure=False
                recieved_numbers=True
                counter = 0
    



def listener():

    sum = 0
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    


    pub = rospy.Publisher('chatter_1', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if sign == '+':
            if recieved_numbers:
                sum=int(num[0])+int(num[1])
                
                
        
        if sign == '-':
            if recieved_numbers:
                sum=int(num[0])-int(num[1])
                
               
        if sign == '*':
            if recieved_numbers:
                sum=int(num[0])*int(num[1])
                
               
        if sign == '/':
            if recieved_numbers:
                sum=int(num[0])/int(num[1])
                
        rospy.loginfo(str(sum))
        pub.publish(str(sum))

        rate.sleep()

if __name__ == '__main__':
    to_measure = False
    recieved_numbers = False
    counter = 0
    num = [None]*10
    sign = ''
    listener()
    
