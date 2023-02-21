#!/usr/bin/env python
import random
import rospy
from std_msgs.msg import Int64


def starting():
    pub = rospy.Publisher('started', Int64, queue_size=10)
    rospy.init_node('starter', anonymous=True)
    while not rospy.is_shutdown():
        hell_st = random.randint(-100, 100)
        rospy.loginfo(hell_st)
        pub.publish(hell_st)


if __name__ == '__main__':
    try:
        starting()
    except rospy.ROSInterruptException:
        pass
