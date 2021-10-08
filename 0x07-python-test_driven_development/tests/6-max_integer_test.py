#!/usr/bin/python3
"""Test de 6-max_integer_test.py"""

"""
test funcion print max
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestMax Integer es un testing class
     para la funcion max_integer"""

    def test_max(self):
        """ test list"""
        self.assertEqual(max_integer([34, 54, 74, 756, 23]), 758)

    def test_max_iguales(self):
        """testea igual lsit"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_max(self):
        """ testea list negativ numbers"""
        self.assertEqual(max_integer([-32, -43, 5, -4, -748]), 10)

    def test_max_none(self):
        """test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max_error(self):
        """test no int"""
        with self.assertRaises(TypeError):
            max_integer([2, 3, 5, 'lol'])