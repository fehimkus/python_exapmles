#! /usr/bin/env python
# Import the Python library for ROS
import rospy
# Import the library for generating random numbers
import random
# Import the Twist message from the geometry_msgs package
# Twist data structure is used to represent velocity components
from geometry_msgs.msg import Twist
class RndVelocityGen():
def __init__(self):
# Initiate a node named ’random_velocity’
rospy.init_node(’random_velocity’)
# Create a Publisher object, that will publish on /new_vel topic
# messages of type Twist
self.vel_pub = rospy.Publisher(’/new_vel’, Twist, queue_size=1)
# Creates var of type Twist
self.vel = Twist()
# Assign initial velocities
self.vel.linear.x = 0.5
# m/s
self.vel.angular.z = 0.5
# rad/s
# Set max values for velocities, min is set to 0
self.linear_vel_x_max = 1.2
self.angular_vel_z_max = 0.5
# Set max value for max time interval between velocity changes,
# min is set to 1
self.max_interval = 10
def generate_rnd_values(self):
# Loop until someone stops the program execution
while not rospy.is_shutdown():
# positive x-vel move the robot forward, negative backward
x_forward = random.choice((-1,1))
# positive z-vel rotate robot counterclockwise, negative clockw
z_counterclok = random.choice((-1,1))
self.vel.linear.x
= (x_forward *
random.uniform(0, self.linear_vel_x_max))
self.vel.angular.z = (z_counterclok *
self.vel_pub.publish(self.vel)
now = rospy.get_rostime()
print "Time now: ", now.secs
next = (random.randint(1, self.max_interval))
rospy.loginfo("Twist: [%5.3f, %5.3f], next change in %i secs - ",
self.vel.linear.x, self.vel.angular.z, next)
rospy.sleep(next)
# Sleeps for the selected seconds
if __name__ == ’__main__’:
try:
generator = RndVelocityGen()
generator.generate_rnd_values()
except rospy.ROSInterruptException:
pass
