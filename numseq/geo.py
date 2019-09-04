#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculates the square, tringle, and cube of a number."""

import argparse

# This is to help coaches and graders identify student assignments
__author__ = "ElizabethS5"


def square(n):
    """Calculates and returns the square of a number."""
    return n ** 2


def triangle(n):
    """Calculates and returns the triangle of a number."""
    return sum(num for num in range(1, n + 1))


def cube(n):
    """Calculates and returns the cubes of a number."""
    return n ** 3


def get_arguments():
    """Returns the arguments from the command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'number',
        help='number to be squared, triangled, and cubed', type=int)
    return parser.parse_args()


def main():
    """Prints and returns square, triangle, and cube."""
    num = get_arguments().number
    print(f"{num}: {square(num)} {triangle(num)} {cube(num)}")
    return (square(num), triangle(num), cube(num))


if __name__ == "__main__":
    main()
