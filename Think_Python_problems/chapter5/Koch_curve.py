"""
The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch
curve with length x, all you have to do is:
1.  Draw a Koch curve with length x/3.
2.  Turn left 60 degrees.
3.  Draw a Koch curve with length x/3.
4.  Turn right 120 degrees.
5.  Draw a Koch curve with length x/3.
6.  Turn left 60 degrees.
7.  Draw a Koch curve with length x/3.
The exception is if x is less than 3: in that case, you can just draw a straight
line with length x.
1.  Write a function called koch that takes a turtle and a length as parameters,
    and that uses the turtle to draw a Koch curve with the given length.
2.  Write a function called snowflake that draws three Koch curves to make the
    outline of a snowflake.
3.  The Koch curve can be generalized in several ways. See http://en.wikipedia.org/wiki/Koch_snowflake for examples 
and implement your favorite.
"""

from swampy.TurtleWorld import *

world = TurtleWorld()
turtoise = Turtle()

turtoise.delay = 0.01

angle= 60
length = 240

def koch(turtle, length):
    "Draws a koch curve"
    if length < 3:
        turtle.fd(length)
        return

    go = length/3

    koch(turtle, go)
    turtle.lt(angle)
    koch(turtle, go)
    turtle.rt(angle*2)
    koch(turtle, go)
    turtle.lt(angle)
    koch(turtle, go)

def snowflake(turtle, length):
    "Draws a snowflake (a triangle with a Koch curve for each side)."
    for _ in range(3):
        koch(turtle, length)
        turtle.rt(angle*2)

koch(turtoise, length)

turtoise.pu()
turtoise.fd(50)
turtoise.pd()

snowflake(turtoise, length)


wait_for_user()