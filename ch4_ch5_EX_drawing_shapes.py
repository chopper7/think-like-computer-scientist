# How to Think Like a Computer Scientist

# Chapter 4 and Chapter 5 Exercises and Lab


################################################################

'''
4.11.6 -- (draw shape filled in with color)
Write a program that asks the user for the number of sides, the length of
the side, the color, and the fill color of a regular polygon. The program
should draw the polygon and then fill it in.
'''

import turtle

sides = int(input("sides? "))
length = int(input("length? "))
color = input('color? ')
fill = input('fill color? ')

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color(color, fill)
alex.hideturtle()

# borrowed this function from exercises I'd done previously in chapters to come
def drawPolygon(tur, sideLen, numSides):
    angle = 360/numSides
    for i in range(numSides):
        tur.forward(sideLen)
        tur.left(angle)

# fill shape with color as follows:
#   begin fill
#   draw the shape
#   end fill
#SEE: http://www.eg.bucknell.edu/~hyde/Python3/TurtleDirections.html#beginfill

alex.begin_fill()
drawPolygon(alex, length, sides)
alex.end_fill()

wn.exitonclick()


################################################################

'''
4.11.9
Draw a Star
'''

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
side = 50

# To draw a star -- Observations
# (I did some sketches by hand to figure out the angles)
#
# angle: 360/number_sides_interior_shape <pentagon>
#        360/5 = 72 degrees
# star is 5 long lines, interior shape (pentagon) has 5 lines too
# Pattern is:
#     turn the angle
#     draw the length of a side
#     turn the angle 

for _ in range(5):
    t.right(72)  # 360/5
    t.forward(side)
    t.right(72)

wn.exitonclick()

# HTLACS draw-star code:
def drawFivePointStar(t, side):
    for i in range(5):
        t.forward(side)
        t.left(216)


################################################################

'''
4.11.10
Write a program to draw a face of a clock [with turtles.]
'''
# go forward (diameter)
# pendown
# go forward (making a line mark)
# penup
# go forward (whitespace twice len of mark)
# stamp
# move back (diameter + length of marks)
# change angle

import turtle

wn = turtle.Screen()
wn.bgcolor("green")

t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.penup()

diam = 100
mark = 10
clockface = 12

for _ in range(12):
    t.left(360//clockface)  # 360/12
    t.forward(diam)
    t.pendown()
    t.forward(mark)
    t.penup()
    t.forward(2*mark)
    t.stamp()
    t.forward(-1 * (diam + 3*mark))

wn.exitonclick()


################################################################

# Lab 4.4, "sinlab2"
# Plotting a sine Wave
# http://interactivepython.org/runestone/static/thinkcspy/Labs/sinlab.html

'''
Plot a single sine wave
We need to set our screen's coordinate system to give us appropriate room
to plot the values of a sine function. To do this, we will use a method of
the Screen class called ```setworldcoordinates```. This method allows us
to change the range of values on the x and y coordinate system for our turtle.

REF - https://docs.python.org/3/library/turtle.html#turtle.setworldcoordinates
'''

import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
# coord args: (lower-left-x, lower-left-y,  upper-right-x, upper-right-y)
wn.setworldcoordinates(0, -1.25, 360, 1.25)

fred = turtle.Turtle()

for x in range(360):
    y = math.sin(math.radians(x))
    fred.goto(x,y)
    
wn.exitonclick()
