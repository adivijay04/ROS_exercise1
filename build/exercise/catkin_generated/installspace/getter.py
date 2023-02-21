#!/usr/bin/env python2
import rospy
from std_msgs.msg import String, Int64


def callback(data):
    if(data.data > 0):
        rospy.loginfo("I have positive numbers %d from relay", data.data)


def gotit():
    rospy.init_node('getter', anonymous=True)
    rospy.Publisher('getter', String, queue_size=10)
    rospy.Subscriber('relay', Int64, callback)

    rospy.spin()


if __name__ == '__main__':
    try:
        gotit()
    except rospy.ROSInterruptException:
        pass
