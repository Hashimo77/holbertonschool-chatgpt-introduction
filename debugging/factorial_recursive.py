#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a number recursively.

    Parameters:
        n (int): The number to calculate the factorial of.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the given number.
             Returns 1 if n is 0 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the input number from command-line arguments
f = factorial(int(sys.argv[1]))
print(f)
