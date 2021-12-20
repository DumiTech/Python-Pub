from swampy.TurtleWorld import *

world = TurtleWorld()
turtle = Turtle()

turtle.delay = 0.1


def draw(t, length, n):
    if n == 0:
        return

    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

draw(turtle, 5, 5)

wait_for_user()