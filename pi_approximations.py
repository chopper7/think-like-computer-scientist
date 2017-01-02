# interactivepython.org/runestone/static/thinkcspy/Functions/thinkcspyExercises.html
# q15_answer

# "Liebniz formula for pi"
# https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... = pi/4

# Looks like it's alternately adding & subtracting every odd denominator fraction;
# and if you multiply that calculation by 4, you'll be close to pi.

# How this function works:
#  start pi accumulator at 0
#  for a series of iterations...
#   add pi accumu. to 1|-1 over current odd denominator (1|-1 alternates sign)
#   change the sign of 1
#   increment denominator to the next odd number
#  after iterating is done, multiply pi accumulator by 4

def myPi_Liebniz(iters):
    ''' Calculate an approximation of PI using the Leibniz
    approximation with iters number of iterations '''
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)
        sign = sign * -1  # alternate positive and negative
        denominator = denominator + 2  # increment by 2 so denominator stays odd

    pi = pi * 4.0
    return pi


## Test it:
##pi_approx = myPi(10000)
##print(pi_approx)


########################################################################

# ex_5_16
# Next, approximation of pi using the Madhava formula for pi
# en.wikipedia.org/wiki/Madhava_of_Sangamagrama#The_value_of_.CF.80_.28pi.29

def myPi_Madhava(iters):
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign / (denominator * 3**i))
        sign = sign * -1
        denominator = denominator + 2

    pi = pi * 12**0.5
    return pi

# works, but may take too much time