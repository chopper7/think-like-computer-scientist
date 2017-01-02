# How to Think Like a Computer Scientist
# Chapter 6: Functions
# EXERCISES
# .../runestone/static/thinkcspy/Functions/thinkcspyExercises.html


########################################

# Set it up

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)
    
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("fuchsia")
alex.pensize(3)
#alex.speed(2)

# Close screen window when clicked on
wn.exitonclick()

########################################

# EXERCISE 1.
"""Use the drawsquare function we wrote in this chapter in a program
to draw the image shown below. Assume each side is 20 units.
(Hint: notice that the turtle has already moved away from the ending
point of the last square when the program ends.)"""

# my code
dist = 20
for i in range(5):
    drawSquare(alex,dist)
    alex.penup()
    alex.forward(dist*2)
    alex.pendown()

wn.exitonclick()


########################################

# ex_5_2:
"""Write a program to draw this.[SMALLER SQUARES INSIDE BIGGER SQUARES].
Assume the innermost square is 20 units per side, and each successive
square is 20 units bigger, per side, than the one inside it."""

# my code
units = 20  # side length of smallest square
sq_qty = 5  # quantity of squares to be drawn

for i in range(1,sq_qty+1):
    drawSquare(alex, units*i) # draw square (successively larger sides)
    alex.penup()              # don't draw the offset moves
    alex.forward(-units/2)    # offset position backward
    alex.right(90)
    alex.forward(units/2)     # offset position downward
    alex.left(90)
    alex.pendown()            # ready to draw the next square
    
wn.exitonclick()


########################################

# ex_5_3:
"""Write a non-fruitful function
```drawPoly(someturtle, somesides, somesize)```
which makes a turtle draw a regular polygon.
When called with drawPoly(tess, 8, 50),
it will draw a shape like this <OCTAGON>
"""

# ANSWER CODE (similar to code I'd already gone ahead and written earlier)
def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)

drawPoly(tess, 8, 50)


########################################

# ex_5_4:
'''Draw this pretty pattern.
(a number of squares overlaid in a circular pattern, each
square tilted a certain angle from the previous square)
'''
import turtle

wn = turtle.Screen()       # Set up the window and turtle
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color('blue')

quantity = 20  # draw same polygon this many times
side = 75      # length of a side

def drawPolygon(t, sideLength, numSides):
    """Draws n-sided polygon with sides of equal length"""
    angle = 360/numSides
    for i in range(numSides):
      t.forward(sideLength)
      t.left(angle)

for _ in range(quantity):
    drawPolygon(tess, side, 4)  # draw square
    tess.left(360/quantity)     # change heading
    
wn.exitonclick()


########################################

# ex_5_5:
'''The two spirals in this picture differ only by the turn angle. Draw both.'''

# My code didn't work at first, but I was close to being correct; had to peek
# at the answer to complete it. The only difference was that I'd been
# incrementing `side` by 1, but the answer code incremented it by 2.

# To make a differently angled spiral, just change the arg of .right().

import turtle

wn = turtle.Screen()       # Set up the window and turtle
tess = turtle.Turtle()
tess.speed(10)

side = 1
for _ in range(64):
    tess.right(90)
    tess.forward(side)
    side += 2       # push-out the next side

wn.exitonclick()


########################################

# ex_5_6:
'''
Write a non-fruitful function ```drawEquitriangle(someturtle, somesize)```
which calls ```drawPoly``` from the previous question to have its turtle
draw an equilateral triangle.
'''
import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

def drawEquitriangle(turt, size):
    drawPoly(turt, 3, size)

wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(10)

drawEquitriangle(tess, 50)

wn.exitonclick()


########################################

# ex_5_7:
'''
Write a fruitful function ```sumTo(n)``` that returns the sum of all integers
up to and including n. So, ```sumTo(10)``` would be ```1+2+3...+10```,
which would return the value 55.

Use the equation (n * (n + 1)) / 2.

MY NOTE: to add consecutive numbers up to n, you should:
         multiply n times 1 more than n, then halve it.
         (If n is 10, you'd find half of 10 * 11.)

SEE: https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
'''

def sumTo(n):
    return (n * (n + 1)) / 2


# ex_5_13:
'''Rewrite the function sumTo(n). This time use the accumulator pattern.'''
def sumTo(n):
    # your code here
    ans = 0
    for x in range(n+1):
        ans += x
    return ans


########################################

# ex_5_8:
'''
Write a function `areaOfCircle(r)` which returns the area of a circle
of radius r. Make sure you use the math module in your solution
'''

def areaOfCircle(r):
    import math
    return math.pi * r**2  # pie are not square, pie are round!


########################################

# ex_5_10:
'''
Write a non-fruitful function to draw a five pointed star,
where the length of each side is 100 units.

Extend your program... Draw five stars, but between each, pick up the pen,
move forward by 350 units, turn right by 144, put the pen down, and draw
the next star. (Note that you will need to move to the left before drawing
your first star in order to fit everything in the window).
'''

import turtle

# FROM MY FILE "ch4_ch5_EX_drawing_shapes.py"
def drawStar(t, side):
    for _ in range(5):
        t.right(72)  # 360/5
        t.forward(side)
        t.right(72)

# set up screen and turtle

# offset turtle
t.penup()
t.setx(-200)
# draw star, move, draw star, etc (5 stars)(a pentagon-constellation of stars)
drawStar(t, 100)
t.penup()
t.forward(350)
t.right(144)  # hmm... 144 is twice 72, the angle used to make a 5-pointed star


########################################

# ex_5_12:
'''
Write a function called drawSprite that will draw a sprite. The function will
need parameters for the turtle, the number of legs, and the length of the legs.

Invoke the function to create a sprite with 15 legs of length 120.
'''

import turtle

def drawSprite(t, legs, length):
    for _ in range(legs):
        t.left(360/legs)
        t.forward(length)
        t.penup()
        t.forward(-1*length)
        t.pendown()

wn = turtle.Screen()
t = turtle.Turtle()

drawSprite(t, 15, 120)

wn.exitonclick()


########################################

# ex_5_17:
'''
Write a function called fancySquare that will draw a square with 
fancy corners (spites on the corners). You should implement and use
the drawSprite function from above.
'''
        
def fancySquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        drawSprite(t, 7, 20)  # draw a "fancy corner"
        
wn = turtle.Screen()
t = turtle.Turtle()

fancySquare(t, 60)

wn.exitonclick()
