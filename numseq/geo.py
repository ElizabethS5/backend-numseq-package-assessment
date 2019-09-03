#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculate the square, tringle, and cube of a number"""

import argparse

# This is to help coaches and graders identify student assignments
__author__ = "ElizabethS5"


def get_arguments():
    """returns the arguments form the command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'number',
        help='number to be squared, triangled, and cubed', type=int)
    return parser.parse_args()


def square(n):
    """Calculate and return the square of a number"""
    return n ** 2


def triangle(n):
    """Calculate and return the triangle of a number"""
    return sum(num for num in range(1, n + 1))


def cube(n):
    """Calculate and return the cubes of a number"""
    return n ** 3


def main():
    """Prints and returns square, triangle, and cube"""
    num = get_arguments().number
    print(f"{num}: {square(num)} {triangle(num)} {cube(num)}")
    return (square(num), triangle(num), cube(num))


if __name__ == "__main__":
    main()
