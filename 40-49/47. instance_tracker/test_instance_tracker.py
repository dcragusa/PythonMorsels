import unittest

from instance_tracker import instance_tracker


class InstanceTrackerTests(unittest.TestCase):

    """Tests for instance_tracker class factory."""

    def test_two_instances(self):
        class Tracked(instance_tracker()):
            pass
        t = Tracked()
        self.assertEqual(set(Tracked.instances), {t})
        u = Tracked()
        self.assertEqual(set(Tracked.instances), {t, u})
        self.assertEqual(Tracked.instances, t.instances)
        self.assertEqual(t.instances, u.instances)

    def test_inheritance_tracks_all_instances(self):
        class Tracked(instance_tracker()):
            def __init__(self, something):
                self.something = something
                super().__init__()
        class A(Tracked):
            pass
        class B(Tracked):
            def __init__(self, something, x):
                self.x = x
                super().__init__(something)
        a = A(something="a")
        self.assertEqual(set(Tracked.instances), {a})
        b = B("b", 3)
        c = B("c", x=4)
        self.assertEqual(set(Tracked.instances), {a, b, c})
        self.assertEqual(a.instances, b.instances)
        self.assertEqual(b.x, 3)
        self.assertEqual(c.x, 4)
        self.assertEqual(a.something, "a")
        self.assertEqual(c.something, "c")

    def test_multiple_inheritance(self):
        class Animal:
            def __init__(self, name):
                self.name = name
        class Squirrel(instance_tracker(), Animal):
            def __init__(self, name, nervousness=0.99):
                self.nervousness = nervousness
                super().__init__(name)
        squirrel1 = Squirrel(name='Mike')
        squirrel2 = Squirrel(name='Carol', nervousness=0.5)
        self.assertEqual(squirrel1.name, 'Mike')
        self.assertEqual(squirrel2.name, 'Carol')
        self.assertEqual(squirrel1.nervousness, 0.99)
        self.assertEqual(squirrel2.nervousness, 0.5)
        self.assertEqual(set(Squirrel.instances), {squirrel1, squirrel2})

    def test_usage_on_two_classes_is_independent(self):
        class A(instance_tracker()):
            pass
        class B(instance_tracker()):
            def __init__(self, x):
                self.x = x
                super().__init__()
        a = A()
        self.assertEqual(set(A.instances), {a})
        b = B(3)
        self.assertEqual(set(B.instances), {b})
        self.assertEqual(set(A.instances), {a})
        self.assertEqual(a.instances, A.instances)
        self.assertEqual(b.instances, B.instances)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_accepts_attribute_name_argument(self):
        class A(instance_tracker('instances')):
            pass
        x = A()
        self.assertEqual(set(A.instances), {x})
        y = A()
        self.assertEqual(set(A.instances), {x, y})

        class B(instance_tracker('_registry')):
            def __init__(self, x):
                self.x = x
                super().__init__()
        b = B(3)
        self.assertEqual(set(B._registry), {b})
        c = B(4)
        self.assertEqual(set(B._registry), {b, c})
        self.assertEqual(b._registry, B._registry)
        with self.assertRaises(AttributeError):
            A._registry

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_works_without_super_calls(self):
        class Tracked(instance_tracker()):
            def __init__(self, something):
                self.something = something
        class A(Tracked):
            pass
        class B(Tracked):
            def __init__(self, something, x):
                self.x = x
                super().__init__(something)
        a = A(something="a")
        self.assertEqual(set(Tracked.instances), {a})
        b = B("b", 3)
        c = B("c", x=4)
        self.assertEqual(set(Tracked.instances), {a, b, c})
        self.assertEqual(a.instances, b.instances)
        self.assertEqual(b.x, 3)
        self.assertEqual(c.x, 4)
        self.assertEqual(a.something, "a")
        self.assertEqual(c.something, "c")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_deleted_instances_are_not_maintained(self):
        class A(instance_tracker()):
            pass
        x = A()
        self.assertEqual(set(A.instances), {x})
        y = A()
        self.assertEqual(set(A.instances), {x, y})
        del x
        self.assertEqual(set(A.instances), {y})
        z = A()
        self.assertEqual(set(A.instances), {y, z})


if __name__ == "__main__":
    unittest.main(verbosity=2)
