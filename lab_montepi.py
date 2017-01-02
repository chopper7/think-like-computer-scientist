'''http://interactivepython.org/runestone/
static/thinkcspy/Labs/montepi.html#throwing-darts'''

import turtle
import math
import random

dart = turtle.Turtle()
dart.speed()  # go faster

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.tracer(1000)  # accelerate the drawing of complex graphics


numdarts = 10000
insideCount = 0
for i in range(numdarts):
    dart.up()
    # Coords: Random negative or positive numbers betweeen -1 and 1
    x = random.random()*2 - 1  # Hat tip:
    y = random.random()*2 - 1  # www.posteet.com/view/1559
    dart.setpos(x, y)

    # Set dart color based on whether its within radius of circle center or not,
    # and count the darts inside the circle
    if dart.distance(0.,0.) <= 1.0:
      dart.pencolor('red')
      insideCount += 1
    else:
      dart.pencolor('blue')

    # Make a dot at x,y
    dart.dot(size=5)

# Compute pi and print it
# insideCount/numdarts should approx equal circle area, which in this case is pi
# And the area of square around the circle is 4.
# How does 0.789 relate to 3.14?...
# By multiplying it by 4, not subtracting it! :)

##print(4 - insideCount/numdarts)
print(insideCount/numdarts * 4)

wn.exitonclick()
