#!/usr/bin/env python2
import random
import rospy
from std_msgs.msg import String, Int64


def callback(data):
    if(data.data > 0):
        rospy.loginfo("I have a positive number %d from starter", data.data)


def middle():
    pur = rospy.Publisher('relay', String, queue_size=10)
    rospy.init_node('middleman', anonymous=True)
    while not rospy.is_shutdown():
        rel_msg = random.randint(-100, 100)
        pur.publish(rel_msg)
        rospy.Subscriber('started', Int64, callback)


if __name__ == '__main__':
    try:
        middle()
    except rospy.ROSInterruptException:
        pass
