import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b
    def soustraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(1, 2)
        self.assertEqual(result, 3)
    def test_soustraction(self):
        result = SimpleMath.soustraction(4, 2)
        self.assertEqual(result, 2)
