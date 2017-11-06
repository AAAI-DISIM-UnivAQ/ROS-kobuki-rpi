#!/usr/bin/env python

import time
import curses
import rospy
import math
from nav_msgs.msg import Odometry
from kobuki_msgs.msg import BumperEvent
from kobuki_msgs.msg import PowerSystemEvent
from kobuki_project.msg import Status

publisher_status = rospy.Publisher('kobuki_status', Status, queue_size=1)
status = Status()

def pbar(window):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
                publisher_status.publish(status)
                rate.sleep()
                window.addstr(0, 5, "position_x: {}".format(status.x))
                window.addstr(2, 5, "position_y: {}".format(status.y))
                window.addstr(4, 5, "bumper_sx: {}".format(bool(status.left)))
                window.addstr(6, 5, "bumper_fr: {}".format(bool(status.front)))
                window.addstr(8, 5, "bumper_dx: {}".format(bool(status.right)))
                window.addstr(10, 5, "power: {}".format(status.power))
                window.refresh()

def odom(odometry):
        status.x = odometry.pose.pose.position.x
        status.y = odometry.pose.pose.position.y

def bump(bumper):

        state = bumper.state
        bumper = bumper.bumper

        if bumper == 0:
                status.left=state
        elif bumper == 1:
                status.front=state
        else:   
                status.right=state

def PowerEventCallback(data):
    if   ( data.event == PowerSystemEvent.UNPLUGGED ) :
        # rospy.loginfo("Robot unplugged")
        status.power = PowerSystemEvent.UNPLUGGED
    elif ( data.event == PowerSystemEvent.PLUGGED_TO_ADAPTER ) :
        # rospy.loginfo("Robot plugged to adapter")
        status.power = PowerSystemEvent.PLUGGED_TO_ADAPTER
    elif ( data.event == PowerSystemEvent.PLUGGED_TO_DOCKBASE ) :
        # rospy.loginfo("Robot plugged to docking base")
        status.power = PowerSystemEvent.PLUGGED_TO_DOCKBASE
    elif ( data.event == PowerSystemEvent.CHARGE_COMPLETED ) :
        # rospy.loginfo("Robot charge completed")
        status.power = PowerSystemEvent.CHARGE_COMPLETED
    elif ( data.event == PowerSystemEvent.BATTERY_LOW ) :
        # rospy.loginfo("Robot battery low")
        status.power = PowerSystemEvent.BATTERY_LOW
    elif ( data.event == PowerSystemEvent.BATTERY_CRITICAL ) :
        # rospy.loginfo("Robot battery critical")
        status.power = PowerSystemEvent.BATTERY_CRITICAL
    else:
        rospy.loginfo("WARN: Unexpected power system event: %d"%(data.event))

def sense():
        rospy.init_node('sense')
        rospy.Subscriber("/odom", Odometry, odom)
        rospy.Subscriber("/mobile_base/events/power_system", PowerSystemEvent, PowerEventCallback)
        rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, bump)
        curses.wrapper(pbar)


if __name__ == '__main__':
        try:
                sense()
        except rospy.ROSInterruptException:
                pass

