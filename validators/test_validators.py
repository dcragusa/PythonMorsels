import gc
import unittest

from validators import PositiveNumber


class PositiveNumberTests(unittest.TestCase):

    """Tests for PositiveNumber."""

    def test_readable(self):
        class Thing:
            x = PositiveNumber(4)
        thing = Thing()
        self.assertEqual(thing.x, 4)

    def test_write_positive_integer(self):
        class Thing:
            x = PositiveNumber(4)
        thing = Thing()
        thing.x = 1
        self.assertEqual(thing.x, 1)

    def test_write_zero(self):
        class Thing:
            x = PositiveNumber(4)
        thing = Thing()
        with self.assertRaises(ValueError):
            thing.x = 0

    def test_write_negative_integer(self):
        class Thing:
            x = PositiveNumber(4)
        thing = Thing()
        with self.assertRaises(ValueError):
            thing.x = -1

    def test_two_positive_integer_attributes(self):
        class Thing:
            x = PositiveNumber(4)
            y = PositiveNumber(5)
        thing = Thing()
        self.assertEqual(thing.x, 4)
        self.assertEqual(thing.y, 5)
        thing.x = 6
        thing.y = 7
        self.assertEqual(thing.x, 6)
        self.assertEqual(thing.y, 7)

    def test_works_in_initializer(self):
        class Thing:
            x = PositiveNumber(8)
            def __init__(self):
                self.x = 4
        thing = Thing()
        self.assertEqual(thing.x, 4)
        with self.assertRaises(ValueError):
            class Thing:
                x = PositiveNumber(8)
                def __init__(self):
                    self.x = -4
            thing = Thing()

    def test_two_instances_of_same_class(self):
        class Vector:
            x = PositiveNumber(0)
            y = PositiveNumber(0)
            z = PositiveNumber(0)
            def __init__(self, x, y, z):
                self.x, self.y, self.z = x, y, z
        u = Vector(1, 2, 3)
        v = Vector(4, 5, 6)
        self.assertEqual((u.x, u.y, u.z), (1, 2, 3))
        self.assertEqual((v.x, v.y, v.z), (4, 5, 6))

    def test_no_memory_leaks(self):
        class Thing:
            x = PositiveNumber(1)
        self.assertEqual(count_instances_of(Thing), 0)
        thing = Thing()
        self.assertEqual(count_instances_of(Thing), 1)
        self.assertEqual(thing.x, 1)
        thing.x = 8
        self.assertEqual(thing.x, 8)
        del thing
        self.assertEqual(count_instances_of(Thing), 0)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_no_default(self):
        class Thing:
            x = PositiveNumber()
        thing = Thing()
        with self.assertRaises(AttributeError) as cm:
            thing.x
        thing.x = 3
        self.assertEqual(thing.x, 3)
        with self.assertRaises(ValueError):
            thing.x = -3


class ValidatorTests(unittest.TestCase):

    """Tests for Validator."""

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_validate_method_on_new_class(self):
        from collections.abc import Sequence
        from validators import Validator
        class SequenceOnly(Validator):
            def validate(self, value):
                if not isinstance(value, Sequence):
                    raise TypeError("Sequence required")
        class Thing:
            x = SequenceOnly()
        thing = Thing()
        thing.x = 'hello'
        self.assertEqual(thing.x, 'hello')
        thing.x = [1, 2, 3]
        self.assertEqual(thing.x, [1, 2, 3])
        with self.assertRaises(TypeError):
            thing.x = {1, 2, 3}

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_validate_method_required(self):
        from collections.abc import Sequence
        from validators import Validator
        class SequenceOnly(Validator):
            def valid(self, value):
                if not isinstance(value, Sequence):
                    raise TypeError("Sequence required")
        with self.assertRaises(TypeError):
            class Thing:
                x = SequenceOnly()


def count_instances_of(cls):
    return sum(
        isinstance(obj, cls)
        for obj in gc.get_objects()
    )


if __name__ == "__main__":
    unittest.main(verbosity=2)
