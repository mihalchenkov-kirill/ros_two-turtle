#!/usr/bin/python

import rospy
import math
import random

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn


class TurtleFollower:
    # When creating a class, we initiate names, follower speeds and starting positions
    def __init__(self, turtle1_name, turtle2_name, follower_speed):
        self.turtle1_name = turtle1_name
        self.turtle2_name = turtle2_name
        self.follower_speed = follower_speed
        self.pose1 = Pose()
        self.pose2 = Pose()

	# Creating subscribers to the turtle position
        rospy.Subscriber("/" + self.turtle1_name + "/pose", Pose, self.callback_first_t)
        rospy.Subscriber("/" + self.turtle2_name + "/pose", Pose, self.callback_second_t)
	
        # Create a message publisher from cmd_vel
        self.pub = rospy.Publisher("/" + self.turtle2_name + "/cmd_vel", Twist, queue_size=10)

        # Spawning a follower and setting him random coordinates
        spawner = rospy.ServiceProxy('spawn', Spawn)
        spawner(random.uniform(0, 8), random.uniform(0, 8), 0, turtle2_name)

	# Wait for a message from the second turtle and set the position
        pose2_msg = rospy.wait_for_message("/" + self.turtle2_name + "/pose", Pose)
        self.pose2.x = pose2_msg.x
        self.pose2.y = pose2_msg.y

    # Call when a message comes from the first turtle
    def callback_first_t(self, data):
        self.pose1 = data
    
    # Call when a message comes from the second turtle
    def callback_second_t(self, data):
        self.pose2 = data

    # Analysis of turtle positions and motion control
    def follow(self):
        while not rospy.is_shutdown():
            # Calculating the distance and angle between turtles
            x_diff = self.pose1.x - self.pose2.x
            y_diff = self.pose1.y - self.pose2.y
            distance = ((x_diff) ** 2 + (y_diff) ** 2) ** 0.5
            angle_to_target = math.atan2(y_diff, x_diff)

            # Calculation of the absolute angle between turtles
            angle_diff = angle_to_target - self.pose2.theta

            # Forming movement teams
            cmd_vel = Twist()
            cmd_vel.linear.x = self.follower_speed * distance
            cmd_vel.angular.z = 4.0 * angle_diff

            # Sending a motion command to the follower
            self.pub.publish(cmd_vel)
            rospy.sleep(0.1)


if __name__ == '__main__':
    rospy.init_node('turtle_follower_node')

    follower_speed = rospy.get_param('~follower_speed')
    turtle1_name = rospy.get_param('~turtle1_name', 'turtle1')
    turtle2_name = rospy.get_param('~turtle2_name', 'turtle2')

    follower = TurtleFollower(turtle1_name, turtle2_name, follower_speed)
    follower.follow()
