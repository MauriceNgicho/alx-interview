#!/usr/bin/python3
"""
Defines a function to get minimum operations
"""


def minOperations(n):
    """
    A function that finds the minimum operations
    """
    operations = 0
    i = 2
    while n > 1:
        while n % i == 0:
            operations += i
            n = n // i
        i += 1
    return operations
