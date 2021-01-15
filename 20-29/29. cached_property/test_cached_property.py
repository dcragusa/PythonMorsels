import gc
import unittest

from cached_property import cached_property


class CachedPropertyTests(unittest.TestCase):

    """Tests for cached_property."""

    def test_accessing_attribute(self):
        from collections import namedtuple
        class Circle(namedtuple('BaseCircle', ['radius'])):
            @cached_property
            def diameter(self):
                return self.radius * 2
        c = Circle(radius=5)
        self.assertEqual(c.diameter, 10)

    def test_does_not_call_getter_function_again(self):
        class Thing:
            called = False
            @cached_property
            def x(self):
                from time import sleep
                sleep(0.01)
                if self.called:
                    raise AssertionError("getter function called again")
                self.called = True
                return self.y
        thing = Thing()
        thing.y = 4
        for i in range(1000):
            self.assertEqual(thing.x, 4)

    def test_attribute_cached_after_first_access(self):
        class Thing:
            @cached_property
            def x(self):
                return self.y
        thing = Thing()
        thing.y = 4
        self.assertEqual(thing.x, 4)
        thing.y = 5
        self.assertEqual(thing.x, 4)

    def test_none_attribute(self):
        class Thing:
            @cached_property
            def x(self):
                return self.y
        thing = Thing()
        thing.y = None
        self.assertEqual(thing.x, None)
        thing.y = 5
        self.assertEqual(thing.x, None)

    def test_error_when_accessing_attribute(self):
        class Thing:
            @cached_property
            def x(self):
                return self.y
        thing = Thing()
        with self.assertRaises(AttributeError):
            thing.x
        thing.y = 5
        self.assertEqual(thing.x, 5)

    def test_setting_attribute_to_override(self):
        class Thing:
            @cached_property
            def x(self):
                return self.y
        thing = Thing()
        thing.y = 4
        self.assertEqual(thing.x, 4)
        thing.x = 5
        self.assertEqual(thing.x, 5)
        self.assertEqual(thing.y, 4)
        thing.y = 8
        self.assertEqual(thing.x, 5)

    def test_two_instances_of_same_class(self):
        class Thing:
            @cached_property
            def x(self):
                return self.y
        thing1 = Thing()
        thing2 = Thing()
        thing1.y = 3
        thing2.y = 4
        self.assertEqual(thing1.x, 3)
        self.assertEqual(thing2.x, 4)
        thing1.y = 5
        self.assertEqual(thing1.x, 3)
        self.assertEqual(thing2.x, 4)

    def test_no_memory_leaks(self):
        class Thing:
            @cached_property
            def x(self):
                return self.y
        self.assertEqual(count_instances_of(Thing), 0)
        thing = Thing()
        thing.y = 5
        self.assertEqual(thing.x, 5)
        self.assertEqual(count_instances_of(Thing), 1)
        del thing
        self.assertEqual(count_instances_of(Thing), 0)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_clearing_cache_by_deleting_attribute(self):
        class Thing:
            @cached_property
            def x(self):
                return self.y
        thing = Thing()
        thing.y = 4
        self.assertEqual(thing.x, 4)
        thing.y = 5
        self.assertEqual(thing.x, 4)
        del thing.x
        self.assertEqual(thing.x, 5)
        thing.x = 6
        thing.y = 9
        self.assertEqual(thing.x, 6)
        del thing.x
        self.assertEqual(thing.x, 9)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_accessing_attribute_on_class(self):
        class Thing:
            @cached_property
            def x(self):
                return self.y
        thing = Thing()
        self.assertEqual(type(Thing.x), cached_property)
        thing.y = 4
        self.assertEqual(Thing.x.__get__(thing, Thing), 4)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_setter_and_deleter_attributes(self):
        class Circle:
            def __init__(self, radius=1):
                self.radius = radius
            @cached_property
            def diameter(self):
                return self.radius * 2
            @diameter.setter
            def diameter(self, diameter):
                if diameter < 0:
                    raise ValueError("Must be positive")
                self.radius = diameter / 2
            @diameter.deleter
            def diameter(self):
                # This is a silly example
                self.radius = 0
        c = Circle(3)
        self.assertEqual(c.diameter, 6)
        c.radius = 4
        self.assertEqual(c.diameter, 6)
        c.diameter = 8
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)
        del c.diameter
        self.assertEqual(c.radius, 0)
        self.assertEqual(c.diameter, 0)


def count_instances_of(cls):
    return sum(
        isinstance(obj, cls)
        for obj in gc.get_objects()
    )


if __name__ == "__main__":
    unittest.main(verbosity=2)
