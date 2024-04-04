#!/usr/bin/python3
"""A module to twst a code using unit test"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        #To test max integers for numbers
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 7, 8, 5, -1]), 8)
        self.assertAlmostEqual(max_integer([10, 40, 20, 180, 200]), 200)
        self.assertAlmostEqual(max_integer([200, 40, 10, 180, 199]), 200)
        self.assertAlmostEqual(max_integer([1, 40, 10, 18, -3]), 40)
        self.assertAlmostEqual(max_integer([10]), 10)
        self.assertAlmostEqual(max_integer([10, 40, 200, 180, 199]), 200)
        self.assertAlmostEqual(max_integer([-10, -40, -200, -180]), -10)
        self.assertAlmostEqual(max_integer([10, 40, 200, 180, 199]), 200)
        self.assertAlmostEqual(max_integer([]), None)
