import gc
import unittest

from computed_property import computed_property


class ComputedPropertyTests(unittest.TestCase):

    """Tests for computed_property."""

    def test_accessing_attribute(self):
        from collections import namedtuple
        class Circle(namedtuple('BaseCircle', ['radius'])):
            @computed_property('radius')
            def diameter(self):
                return self.radius * 2
        c = Circle(radius=5)
        self.assertEqual(c.diameter, 10)

    def test_does_not_call_getter_function_again(self):
        class Thing:
            called = False
            @computed_property('y')
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
            self.assertTrue(thing.called)

    def test_attribute_cached_until_attribute_changes(self):
        class Thing:
            @computed_property('z')
            def x(self):
                return self.y * self.z
        thing = Thing()
        thing.y, thing.z = 2, 3
        self.assertEqual(thing.x, 6)
        thing.y = 5
        self.assertEqual(thing.x, 6)
        thing.z = 7
        self.assertEqual(thing.x, 35)
        thing.y = 13
        self.assertEqual(thing.x, 35)

    def test_none_attribute(self):
        class Thing:
            @computed_property('y')
            def x(self):
                return self.y, self.z
        thing = Thing()
        thing.y = None
        thing.z = None
        self.assertEqual(thing.x, (None, None))
        thing.z = 5
        self.assertEqual(thing.x, (None, None))
        thing.y = 3
        self.assertEqual(thing.x, (3, 5))
        thing.y = None
        self.assertEqual(thing.x, (None, 5))

    def test_error_when_accessing_attribute(self):
        class Circle:
            @computed_property('radius')
            def diameter(self):
                return self.radius * 2
        c = Circle()
        with self.assertRaises(AttributeError):
            c.diameter
        c.radius = 2
        self.assertEqual(c.diameter, 4)
        del c.radius
        with self.assertRaises(AttributeError):
            c.diameter
        c.radius = 3
        self.assertEqual(c.diameter, 6)

    def test_cannot_set_attribute(self):
        class Circle:
            @computed_property('radius')
            def diameter(self):
                return self.radius * 2
        c = Circle()
        with self.assertRaises(AttributeError):
            c.diameter = 2
        c.radius = 1
        self.assertEqual(c.diameter, 2)
        with self.assertRaises(AttributeError):
            c.diameter = 3
        self.assertEqual(c.diameter, 2)

    def test_two_instances_of_same_class(self):
        class Thing:
            @computed_property('z')
            def x(self):
                return self.y * self.z
        thing1 = Thing()
        thing2 = Thing()
        thing1.y, thing1.z = 2, 3
        thing2.y, thing2.z = 4, 5
        self.assertEqual(thing1.x, 6)
        self.assertEqual(thing2.x, 20)
        thing1.y = 7
        self.assertEqual(thing1.x, 6)
        self.assertEqual(thing2.x, 20)
        thing1.z = 5
        self.assertEqual(thing1.x, 35)
        self.assertEqual(thing2.x, 20)
        thing2.z = 3
        self.assertEqual(thing1.x, 35)
        self.assertEqual(thing2.x, 12)

    def test_objects_are_garbage_collected_properly(self):
        def count_instances(cls):
            return sum(
                isinstance(obj, cls)
                for obj in gc.get_objects()
            )
        class Thing:
            @computed_property('z')
            def x(self):
                return self.y * self.z
        self.assertEqual(count_instances(Thing), 0)
        thing = Thing()
        thing.y, thing.z = 2, 3
        self.assertEqual(thing.x, 6)
        self.assertEqual(count_instances(Thing), 1)
        del thing
        self.assertEqual(count_instances(Thing), 0)

    def test_accessing_attribute_on_class(self):
        class Thing:
            @computed_property('y')
            def x(self):
                return self.y
        thing = Thing()
        self.assertEqual(type(Thing.x), computed_property)
        thing.y = 4
        self.assertEqual(Thing.x.__get__(thing, Thing), 4)
        thing.y = 5
        self.assertEqual(Thing.x.__get__(thing, Thing), 5)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_multiple_dependency_attributes(self):
        from math import hypot
        class RightTriangle:
            def __init__(self, a, b):
                self.a, self.b, self.d = a, b, 0
                self.t = self.u = None
            @computed_property('a', 'b', 't', 'u')
            def c(self):
                return hypot(self.a, self.b) + self.d
        triangle = RightTriangle(3, 4)
        self.assertEqual(triangle.c, 5)
        triangle.d = 4
        self.assertEqual(triangle.c, 5)
        triangle.b = 5
        self.assertAlmostEqual(triangle.c, 9.830951894845301)
        triangle.d = 0
        self.assertAlmostEqual(triangle.c, 9.830951894845301)
        triangle.a = 12
        self.assertEqual(triangle.c, 13)
        triangle.d = -13
        self.assertEqual(triangle.c, 13)
        triangle.u = 0
        self.assertEqual(triangle.c, 0)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_missing_attributes(self):
        class Cube:
            def __init__(self, width, height, depth):
                self.width, self.height, self.depth = width, height, depth
                self.errors = 0
            @computed_property('width', 'height', 'depth')
            def volume(self):
                try:
                    return self.width * self.height * self.depth
                except AttributeError:
                    self.errors += 1
                    return self.errors
        cube = Cube(2, 3, 5)
        self.assertEqual(cube.volume, 30)
        cube.width = 1
        self.assertEqual(cube.volume, 15)
        del cube.height
        self.assertEqual(cube.volume, 1)
        self.assertEqual(cube.volume, 1)
        del cube.depth
        self.assertEqual(cube.volume, 2)
        self.assertEqual(cube.volume, 2)
        cube.height = 7
        self.assertEqual(cube.volume, 3)
        self.assertEqual(cube.volume, 3)
        cube.depth = 3
        self.assertEqual(cube.volume, 21)
        del cube.height
        self.assertEqual(cube.volume, 4)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_setter_attribute(self):
        class Circle:
            def __init__(self, radius=1):
                self.radius = radius
            @computed_property('radius')
            def diameter(self):
                return self.radius * 2
            @diameter.setter
            def diameter(self, diameter):
                if diameter < 0:
                    raise ValueError("Must be positive")
                self.radius = diameter / 2
        c = Circle(3)
        self.assertEqual(c.diameter, 6)
        c.radius = 1
        self.assertEqual(c.diameter, 2)
        c.diameter = 8
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
