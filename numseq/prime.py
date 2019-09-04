#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculates the all primes less than a number
and if a number is prime.
"""

import argparse

# This is to help coaches and graders identify student assignments
__author__ = "ElizabethS5"


def primes(n):
    """Returns the all primes less than a number."""
    primes_list = []
    number = 1
    while number < n:
        number += 1
        if is_prime(number):
            primes_list.append(number)
    return primes_list


def is_prime(m):
    """Returns True if a number is prime or False if it is not."""
    for num in range(2, round(m ** .5) + 1):
        if not m % num:
            return False
    return True


def get_arguments():
    """Returns the arguments from the command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'number',
        help='number for list of smaller primes and check if prime', type=int)
    return parser.parse_args()


def main():
    """Prints and returns primes less than number and if number is prime."""
    num = get_arguments().number
    print(f"{num}: {primes(num)}")
    print(f"Is {num} prime? {is_prime(num)}")
    return (primes(num), is_prime(num))


if __name__ == "__main__":
    main()
