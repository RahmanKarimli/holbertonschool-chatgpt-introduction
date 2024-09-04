#!/usr/bin/python3

import sys


def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input number. If n is 0, returns 1 as the base case.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Get the integer from the command-line argument, calculate its factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
