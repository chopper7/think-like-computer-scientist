# How To Think Like A Computer Scientist
# 8.12. Exercises
# Exercises 2, 3


# 2.)
# "Write a function print_triangular_numbers(n) that prints out the first
# n triangular numbers." On each line, print the numbers from 1 to n.
# Make the output columnar in appearance by including a tab.

'''
Sample output:
1       1
2       3
3       6
4       10
5       15
'''

def print_triangular_numbers(n):
    total = 0
    for num in range(1, n+1):
        total += num
        print("{}\t{}".format(num, total))


########################################################################


# 3.)
# Write a function, is_prime, that takes a single integer argument and
# returns True when the argument is a prime number and False otherwise.

def is_prime(n):
    # 1, 0, and negative numbers are not prime
    if n <= 1:
        return False
    # even numbers are not prime, except for 2
    elif n > 2 and n % 2 == 0:
        return False
    # check odd numbers for divisors
    else:
        # T|F list of whether n is divisible by numbers up to sq.root of n
        divisors = [n % i == 0 for i in range(, round(n**0.5) + 1)]
        if sum(divisors) == 0:  # no divisors found
            return True
        else:                   # at least 1 divisor found
            return False
    

# Alternate Solution
# Hat Tip:
# http://www.secnetix.de/olli/Python/list_comprehensions.hawk
# "The following is yet another way to compute prime numbers. The interesting
# thing is that we first build a list of non-prime numbers, using a single
# list comprehension, then use another list comprehension to get the "inverse"
# of the list, which are prime numbers."

# could substitute n for 50
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
