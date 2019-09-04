#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculates the nth Fibonacci number"""

import argparse

# This is to help coaches and graders identify student assignments
__author__ = "ElizabethS5"


def fib(n):
    """Calculates and returns the nth Fibonacci number."""
    a, b = 0, 1
    num = 0
    while num < n:
        a, b = b, a + b
        num += 1
    return a


def get_arguments():
    """Returns the arguments from the command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'number', help='the nth fibonacci number calulated', type=int)
    return parser.parse_args()


def main():
    """Prints and returns the nth fibonacci number"""
    num = get_arguments().number
    print(f"{num}: {fib(num)}")
    return fib(num)


if __name__ == "__main__":
    main()
