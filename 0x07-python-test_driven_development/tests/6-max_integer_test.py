#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):
    def test_max(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(max_integer(arr), 4)

        arr = [22, 3, 20, 2]
        self.assertEqual(max_integer(arr), 22)

        arr = [-12, -2, -22, -222]
        self.assertEqual(max_integer(arr), -2)

        arr = [27]
        self.assertEqual(max_integer(arr), 27)

        arr = [None]
        self.assertEqual(max_integer(arr), None)

        arr = [1, 2, -2, 4, 333, 42, 123]
        self.assertEqual(max_integer(arr), 333)

        arr = []
        self.assertEqual(max_integer(arr), None)


if __name__ == "__main__":
    unittest.main()
