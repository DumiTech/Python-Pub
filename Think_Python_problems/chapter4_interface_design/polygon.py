from math import pi
import math
from swampy.TurtleWorld import *

world = TurtleWorld()
john = Turtle()

john.delay = 0.05

segment = 12
radius = 30

def square(t, l):
    for _ in range(4):
        fd(t, l)
        rt(t)

square(john, 100)


johnson = Turtle()
square(johnson, 110)

joe = Turtle()
square(joe, 120)



def polygon(t, n, length):
    angle = 360.0 / n
    print(f'\nAngle: {angle} deg')
    for _ in range(n):
        fd(t, length)
        rt(t, angle)

polygon(john, 6, 30)



def circle(t, r):
    circumference = 2 * math.pi * r
    length = circumference / segment
    print(f'\nLength is: {round(length, 2)}')
    polygon(t, segment, length)

    print('\nCircle circumference is: ', round(circumference, 2))

circle(john, radius)


def arc(t, radius, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.rt(step_angle)

arc(john, radius, angle=90)








wait_for_user()