import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("7 -5 *")
        self.assertEqual(-35, result)
    def test_divide(self):
        result = rpn.calculate("39 13 /")
        self.assertEqual(3, result)
    def test_power(self):
        result = rpn.calculate("2 7 ^")
        self.assertEqual(128, result)
    def test_toomanythings(self):
        with self.assertRaises(TypeError):
            rpn.calculate("1 2 3 +")
