import turtle
import math

def polygon(t, n, l):
    angle = 360 / n
    for i in range(n):
        t.fd(l)
        t.lt(angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

bob = turtle.Turtle()
# polygon(bob, 8, 50)
circle(bob, 50)
