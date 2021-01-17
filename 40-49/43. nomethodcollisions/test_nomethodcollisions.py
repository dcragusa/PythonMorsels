import unittest

from nomethodcollisions import NoMethodCollisions


class NoMethodCollisionsTests(unittest.TestCase):

    """Tests for NoMethodCollisions."""

    def test_all_unique_class_attributes(self):
        class Point(NoMethodCollisions):
            def __init__(self, x, y, z):
                self.x, self.y, self.z = x, y, z
            def __repr__(self):
                return "{class_name}({x}, {y}, {z})".format(
                    class_name=type(self).__name__,
                    x=self.x,
                    y=self.y,
                    z=self.z,
                )
            def __eq__(self, other):
                return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        p = Point(1, 2, 3)
        q = Point(1, 2, 3)
        self.assertEqual(p, q)
        self.assertEqual(repr(p), "Point(1, 2, 3)")

    def test_overlapping_class_attributes(self):
        with self.assertRaises(Exception):
            class SillyTests(NoMethodCollisions, unittest.TestCase):
                def test_add(self):
                    self.assertEqual(2 + 2, 4)
                def test_subtract(self):
                    self.assertEqual(4 - 2, 2)
                def test_add(self):
                    self.assertEqual(1 + 1, 2)

    def test_non_functions(self):
        from math import sqrt
        class Vector(NoMethodCollisions):
            def __init__(self, x, y, z):
                self.x, self.y, self.z = x, y, z
            @staticmethod
            def root_sum_squared(numbers):
                return sqrt(sum(n**2 for n in numbers))
        self.assertEqual(Vector.root_sum_squared([3, 4]), 5)
        with self.assertRaises(Exception):
            class Vector2(NoMethodCollisions):
                @staticmethod
                def root_sum_squared(numbers):
                    return sqrt(n**2 for n in numbers)
                def __init__(self, x, y, z):
                    self.x, self.y, self.z = x, y, z
                @classmethod
                def root_sum_squared(cls, numbers):
                    return sqrt(n**2 for n in numbers)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_TypeError_is_raised(self):
        with self.assertRaises(TypeError):
            class SillyTests(NoMethodCollisions):
                def test_add(self):
                    self.assertEqual(2 + 2, 4)
                def test_subtract(self):
                    self.assertEqual(4 - 2, 2)
                def test_add(self):
                    self.assertEqual(1 + 1, 2)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_property_redefinition(self):
        class Circle(NoMethodCollisions):
            def __init__(self, radius=1):
                self.radius = radius
            @property
            def diameter(self):
                return self.radius * 2
            @diameter.setter
            def diameter(self, diameter):
                self.radius = diameter / 2
        c1 = Circle(5)
        c2 = Circle(8)
        self.assertEqual(c1.diameter, 10)
        self.assertEqual(c2.diameter, 16)
        c2.diameter = 10
        self.assertEqual(c2.diameter, 10)
        self.assertEqual(c2.radius, 5)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_noncallables_to_be_redefined(self):
        class Cipher(NoMethodCollisions):
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            letter_a = alphabet[0]
            letters = {}
            for letter in alphabet:
                letters[letter] = ord(letter) - ord(letter_a)
        self.assertEqual(Cipher.letters['a'], 0)
        self.assertEqual(Cipher.letters['z'], 25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
