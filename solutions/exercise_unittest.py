import unittest
from exercise_doctest import cube

class TestStringMethods(unittest.TestCase):

    def test_cube(self):
        self.assertEqual(64, cube(4))

    def test_cube_zero(self):
        self.assertEqual(0, cube(0))

    def test_cube_negative(self):
        self.assertEqual(-64, cube(-4))

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
