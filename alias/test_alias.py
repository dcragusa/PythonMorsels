import unittest


from alias import alias


class AliasTests(unittest.TestCase):

    """Tests for alias."""

    def test_mirrors_attribute_on_class(self):
        class Thing:
            one = 4
            two = alias('one')
        thing = Thing()
        self.assertEqual(thing.one, 4)
        self.assertEqual(thing.two, 4)

    def test_mirrors_attribute_from_initializer(self):
        class Thing:
            two = alias('one')
            def __init__(self):
                self.one = 4
        thing = Thing()
        self.assertEqual(thing.one, 4)
        self.assertEqual(thing.two, 4)

    def test_attribute_mirroring_maintained(self):
        class Thing:
            one = 4
            two = alias('one')
        thing = Thing()
        self.assertEqual(thing.one, 4)
        self.assertEqual(thing.two, 4)
        thing.one = 6
        self.assertEqual(thing.one, 6)
        self.assertEqual(thing.two, 6)
        self.assertNotEqual(thing.two, 4)

    def test_attribute_identity(self):
        class Thing:
            two = alias('one')
            def __init__(self, one):
                self.one = one
        my_list = []
        thing = Thing(my_list)
        self.assertIs(thing.one, thing.two, my_list)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_attribute_unwritable_by_default(self):
        class Thing:
            one = 4
            two = alias('one')
        thing = Thing()
        with self.assertRaises(AttributeError):
            thing.two = 6
        self.assertEqual(thing.one, 4)
        self.assertEqual(thing.two, 4)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_writable_attribute(self):
        class Thing2:
            blue = alias('red', write=True)
            red = []
        thing2 = Thing2()
        self.assertIs(thing2.blue, thing2.red)
        thing2.blue = [4, 5]
        self.assertEqual(thing2.blue, [4, 5])
        self.assertIs(thing2.blue, thing2.red)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_attribute_mirrored_on_class(self):
        class Thing:
            one = 4
            two = alias('one')
        self.assertEqual(Thing.one, 4)
        self.assertEqual(Thing.two, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
