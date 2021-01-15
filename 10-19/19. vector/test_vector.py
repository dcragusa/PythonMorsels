import unittest

from vector import Vector


class VectorTests(unittest.TestCase):

    """Tests for Vector."""

    def test_attributes(self):
        v = Vector(1, 2, 3)
        self.assertEqual((v.x, v.y, v.z), (1, 2, 3))

    def test_equality_and_inequality(self):
        self.assertNotEqual(Vector(1, 2, 3), Vector(1, 2, 4))
        self.assertEqual(Vector(1, 2, 3), Vector(1, 2, 3))
        self.assertFalse(Vector(1, 2, 3) != Vector(1, 2, 3))
        v1 = Vector(1, 2, 3)
        v2 = Vector(1, 2, 4)
        v3 = Vector(1, 2, 3)
        self.assertNotEqual(v1, v2)
        self.assertEqual(v1, v3)

    def test_iterable_vector(self):
        x, y, z = Vector(x=1, y=2, z=3)
        self.assertEqual((x, y, z), (1, 2, 3))

    def test_no_weird_extras(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        with self.assertRaises(TypeError):
            len(v1)
        with self.assertRaises(TypeError):
            v1 < v2
        with self.assertRaises(TypeError):
            v1 > v2
        with self.assertRaises(TypeError):
            v1 <= v2
        with self.assertRaises(TypeError):
            v1 >= v2
        with self.assertRaises(TypeError):
            v1 + (1, 2, 3)
        with self.assertRaises(TypeError):
            (1, 2, 3) + v1
        with self.assertRaises(TypeError):
            v1 - (1, 2, 3)
        with self.assertRaises(TypeError):
            v1 * 'a'
        with self.assertRaises(TypeError):
            v1 / v2

    def test_memory_efficient_attributes(self):
        v = Vector(1, 2, 3)
        with self.assertRaises(AttributeError):
            v.a = 3
        with self.assertRaises(AttributeError):
            v.__dict__

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_shifting(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        v3 = v2 + v1
        v4 = v3 - v1
        self.assertEqual((v3.x, v3.y, v3.z), (5, 7, 9))
        self.assertEqual((v4.x, v4.y, v4.z), (v2.x, v2.y, v2.z))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_scaling(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        v3 = v1 * 4
        v4 = 2 * v2
        v5 = v3 / 2
        self.assertEqual((v3.x, v3.y, v3.z), (4, 8, 12))
        self.assertEqual((v4.x, v4.y, v4.z), (8, 10, 12))
        self.assertEqual((v5.x, v5.y, v5.z), (2, 4, 6))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_immutable(self):
        v1 = Vector(1, 2, 3)
        with self.assertRaises(Exception):
            v1.x = 4
        self.assertEqual(v1.x, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
