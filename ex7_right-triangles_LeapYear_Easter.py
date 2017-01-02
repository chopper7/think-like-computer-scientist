# How to Think Like A Computer Scientist
# Ch. 7 Exercises
# interactivepython.org/runestone/static/thinkcspy/Selection/Exercises.html

# "is_right_angle" Triangle
# "is leap year?"
#


# ex_6_10
'''
Write a function "is_rightangled" which, given the length of three sides
of a triangle, will determine whether the triangle is right-angled.
Assume that the third argument to the function is always the longest side.
It will return True if the triangle is right-angled, or False otherwise.

Hint: floating point arithmetic is not always exactly accurate, so it
is not safe to test floating point numbers for equality. If a good programmer
wants to know whether x is equal or close enough to y, they would probably
code it up as
    if  abs(x - y) < 0.001:  # if x is approximately equal to y
[like approximation using "epsilon" in MITx 6001x]
'''

def is_rightangled(a, b, c):
    """
    Given the lengths of the sides of a triangle, determine whether
    the triangle is right-angled. Assumes `c` is the longest side.
    Returns True or False.
    """
    return abs(c**2 - (a**2 + b**2)) < 0.001


#-----------------------------------------------------------------------


# ex_6_11
''' Extend the above program so that the sides can be given to the function in
any order.
'''

def is_rightangled(a, b, c):
    """
    Given the lengths of a triangle's sides, determine whether the
    triangle is right-angled. Side lengths could be in any order.
    Returns True or False.
    """
    # Get the longest side
    sides = [a, b, c]
    i = sides.index(max(a,b,c))
    long_side = sides.pop(i)
    # Get the other two sides
    x, y = sides
    # Is it a right triangle?
    return abs(long_side**2 - (x**2 + y**2)) < 0.001


################################################################

# ex_6_12
'''
A year is a leap year if it is divisible by 4 unless it is a century that is
not divisible by 400. Write a function that takes a year as a parameter and
returns True if the year is a leap year, False otherwise.

My Hint: see my Ruby code for this problem, "leapyear.rb"
    years divisible by 4 but not by 100
    years divisible by both 4 and 400
'''

def isLeap(year):
    """Determine whether a year is a Leap Year in the Gregorian Calendar"""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


################################################################

# ex_6_13
'''
Implement the calculator for the date of Easter. The following algorithm
computes the date for Easter Sunday for any year between 1900 and 2099.

Ask the user to enter a year. Compute the following:
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e

Special note: The algorithm can give a date in April. Also, if the year
is one of four special years (1954, 1981, 2049, or 2076) then subtract 7
from the date.

Your program should print an error message if the user provides a date
that is out of range.
'''

y = int(input("Enter a year between 1900 and 2099: " ))

while y < 1900 or y > 2099:
    print("Invalid year entered")
    y = input("Enter a year between 1900 and 2099, Q to quit: " )
    if y.lower() == 'q':
        print("Goodbye!")
        break
    else:
        y = int(y)
# TO DO -- put the input and data-checking statements in a main function

def getEaster(year):
    """Compute the date of Easter Sunday for any year between 1900 and 2099"""
    # calculate Easter date
    a, b, c = year % 19, year % 4, year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    dateEaster = 22 + d + e

    # check for special years
    if year in (1954, 1981, 2049, 2076):
        dateEaster -= 7

    # Determine month (March or April)
    if dateEaster > 31:
        Easter = "April " + str(dateEaster - 31)
    else:
        Easter = "March " + str(dateEaster)

    return Easter
