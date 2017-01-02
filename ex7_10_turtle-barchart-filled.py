# Exercises 7.10
# .../runestone/static/thinkcspy/Selection/Exercises.html


# ex_6_4
'''
Modify the turtle bar chart program from the previous chapter so that the
bar for any value of 200 or more is filled with red, values between
[100 and 200) are filled yellow, and bars representing values less than 100
are filled green.
'''
import turtle

def drawBar(t, height, fillcolor):
    """ Get turtle t to draw one bar, of height. """
    t.fillcolor(fillcolor)
    t.begin_fill()          # start filling this shape
    t.left(90)
    t.forward(height)
    t.fillcolor('black')    # write the number in black, not the bar color
    t.write(str(height))
    t.fillcolor(fillcolor)  # back to the shape's fillcolor
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()            # stop filling this shape


xs = [48, 117, 200, 240, 160, 260, 20]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()        # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # create tess and set some attributes
tess.color("blue")
tess.pensize(3)

for a in xs:
    # color the bar depending on data values
    if a >= 200:
        #tess.fillcolor("red")
        fc = 'red'
    elif a >= 100:
        #tess.fillcolor("yellow")
        fc = 'yellow'
    else:
        #tess.fillcolor("green")
        fc = 'green'
    # draw bar for current value
    drawBar(tess, a, fc)

wn.exitonclick()


########################################

# ex_6_5
'''
In the turtle bar chart program, what do you expect to happen if one or 
more of the data values in the list is negative? Go back and try it out.
Change the program so that when it prints the text value for the negative
bars, it puts the text above the base of the bar (on the 0 axis)
'''
import turtle

def drawBar(t, height, fillcolor):
    """ Get turtle t to draw one bar, of height. """
    t.fillcolor(fillcolor)
    t.begin_fill()         # start filling this shape
    # start drawing the bar
    t.left(90)
    t.forward(height)
    # write the value at the top or base of bar
    #        if negative value:
    if height <= 0:
        t.penup()
        t.forward(-1*height)
        t.fillcolor('black')
        t.pendown()
        t.write(str(height))
        t.forward(height)
    else:  # if positive value:
        t.fillcolor('black')
        t.write(str(height))
    # finish the bar
    t.fillcolor(fillcolor)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()           # stop filling this shape

xs = [-48, 117, -200, 204, 160, 26]  # data
maxheight = max([abs(x) for x in xs])
bars = len(xs)
border = 10

wn = turtle.Screen()   # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-maxheight-border, 
                       30*bars+border, maxheight+border)

tess = turtle.Turtle() # create tess and set some attributes

for a in xs:
    if a >= 200:
        fc = 'red'
    elif a >= 100:
        fc = 'yellow'
    else:
        fc = 'green'
    drawBar(tess, a, fc)

wn.exitonclick()

## ANSWER CODE is a lot cleaner than mine:
def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()          # start filling this shape
    if height < 0:
        t.write(str(height))
    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()            # stop filling this shape


xs = [48, -50, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
minheight = min(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle()      # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

if minheight > 0:  # lower left corner depends on whether min value is negative
    lly = 0
else:
    lly = minheight - border

wn.setworldcoordinates(0-border, lly, 40*numbars+border, maxheight+border)

#....

########################################

