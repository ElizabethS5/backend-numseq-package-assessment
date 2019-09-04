#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from numseq.fib import fib
from numseq.geo import square, triangle, cube
from numseq.prime import primes, is_prime

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def test_fib(self):
        print("Fibonacci")
        for i in range(10):
            print(f"{i}: {fib(i)}")

    def test_geo(self):
        print("Geometric numbers (square, triangle, cube)")
        for i in range(10):
            print(f"{i}: {square(i)} {triangle(i)} {cube(i)}")

    def test_prime(self):
        print("Primes")
        prime_list = primes(1000)
        for p in prime_list[-10:]:
            print(p)
        print(f"Is 999981 prime? {is_prime(999981)}")
        print(f"Is 999983 prime? {is_prime(999983)}")


if __name__ == '__main__':
    unittest.main()
