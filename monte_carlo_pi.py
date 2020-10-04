"""
Imagine a quadrant of a circle is placed inside a square, as shown next, and
we generate some random points inside the square. You can see that some of the points fall
inside the circle while others are outside the circle

We know that the area of a circle is πr^2 and the area of a square is a^2
then we can write this equation
(((πr^2)/4)/a^2)=(number of points inside the circle/number of points inside the square)
then because of a=r
π=4*(number of points inside the circle/number of points inside the square)

this code helps us to find π value with statistically
"""
#import necessary libraries
import numpy as np
import math
import random
import matplotlib.pyplot as plt
#%matplotlib inline

#we initialize the square size and number of points inside the circle and square
square_size = 1
points_inside_circle=0
points_inside_square=0
sample_size=100000
arc=np.linspace(0, np.pi/2, 100)

#We define a function called generate_points()
#which generate random points inside the square
def generate_points(size):
    x=random.random()*size
    y=random.random()*size
    return(x,y)

#we define a function called is_in_circle()
#which will check the point falls in circle or not
def is_in_circle(point, size):
    return math.sqrt(point[0]**2+point[1]**2)<= size

#then we define a function for calculating the π value
def calculate_pi(points_inside_circle, points_inside_square):
    return 4*(points_inside_circle/points_inside_square)

#Then for the number of samples, we generate some random points inside the square and
#increment our points_inside_square variable, and then we will check if the points we
#generated lie inside the circle. If yes, then we increment the points_inside_circle variable: 
plt.axes().set_aspect('equal')
plt.plot(1*np.cos(arc), 1*np.sin(arc))

for i in range(sample_size):
    point=generate_points(square_size)
    plt.plot(point[0], point[1], 'c.')
    points_inside_square += 1
    if is_in_circle(point, square_size):
        points_inside_circle += 1

#Now we calculate the value of π using the compute_pi() , function which will print an
#approximate value of π
print ("approximate value of π is {} ".format (calculate_pi(points_inside_circle, points_inside_square)))   
