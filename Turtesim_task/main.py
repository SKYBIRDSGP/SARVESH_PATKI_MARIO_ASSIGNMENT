#Starting with our code
import rospy
from geometry_msgs.msg import Twist 

def draw_circle():
    pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=1)
    rospy.init_node("turtle_circle")
    move_cmd = Twist()

for i in range(1,11):
        move_cmd.linear.x = i
    move_cmd.angular.z = i


    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(move_cmd)
        rate.sleep()


if __name__ == '__main__':
    try:
        draw_circle()
    except rospy.ROSInterruptException:
        pass    