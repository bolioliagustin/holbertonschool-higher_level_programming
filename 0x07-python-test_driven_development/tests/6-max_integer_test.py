#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test to the class testmaxintenger"""

    def max(self):
        """ test list"""
        self.assertEqual(max_integer([34, 54, 74, 756, 23]), 758)

    def max_igual(self):
        """testea igual lsit"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def max_negative(self):
        """ testea list negativ numbers"""
        self.assertEqual(max_integer([-32, -43, 5, -4, -748]), 10)

    def max_empty(self):
        """test empty list"""
        self.assertEqual(max_integer([]), None)

    def max_error(self):
        """test no int"""
        with self.assertRaises(TypeError):
            max_integer([2, 3, 5, 'lol'])
