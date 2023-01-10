import unittest

class main:
    def SimpleMath(a, b):
        c = a + b
        return c
    pass


class TestSimpleMath(unittest.TestCase):
    def test_equal(self, d, a, b):
        self.assertEqual(main.SimpleMath(a,b),d)

    def test_isnull(self, a, b):
        self.assertFalse(main.SimpleMath(a,b) == None)
    pass
