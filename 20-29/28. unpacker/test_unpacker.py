import unittest
from collections import OrderedDict
from datetime import date

from unpacker import Unpacker


class UnpackerTests(unittest.TestCase):

    """Tests for Unpacker."""

    def test_constructor(self):
        Unpacker()
        Unpacker({'a': 2, 'b': 3})

    def test_indpendence_from_dict(self):
        d = {'a': 2, 'b': 3}
        u = Unpacker(d)
        d['a'] = 4
        u['a'] = 5
        self.assertEqual(d['a'], 4)
        self.assertEqual(u['a'], 5)

    def test_key_access(self):
        u = Unpacker({'a': 2, 'b': 3})
        self.assertEqual(u['a'], 2)
        self.assertEqual(u['b'], 3)

    def test_attribute_access(self):
        u = Unpacker({'a': 2, 'b': 3})
        self.assertEqual(u.a, 2)
        self.assertEqual(u.b, 3)

    def test_key_assignment(self):
        u = Unpacker({'a': 2, 'b': 3})
        u['a'] = 45
        u['b'] = 67
        self.assertEqual(u['a'], 45)
        self.assertEqual(u['b'], 67)

    def test_attribute_assignment(self):
        u = Unpacker({'a': 2, 'b': 3})
        u.a = 45
        u.b = 67
        self.assertEqual(u.a, 45)
        self.assertEqual(u.b, 67)
        self.assertEqual(u['a'], 45)
        self.assertEqual(u['b'], 67)

    def test_only_as_key_access(self):
        u = Unpacker({'shape type': 1, 'identifier': 'Square'})
        self.assertEqual(u.identifier, 'Square')
        self.assertEqual(u['shape type'], 1)

    def test_original_dictionary_unchanged(self):
        bundle = {'a': 2, 'b': 3}
        u = Unpacker(bundle)
        u.c = 4
        self.assertEqual(bundle, {'a': 2, 'b': 3})

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_multiple_assignment(self):
        u = Unpacker(OrderedDict([('a', 12), ('c', 13)]))
        a, c = u
        self.assertEqual(a, u.a)
        self.assertEqual(c, u.c)
        u.b = 14
        self.assertEqual(u['b'], 14)
        a, c, b = u
        self.assertEqual(a, u.a)
        self.assertEqual(c, u.c)
        self.assertEqual(b, u.b)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_multiple_key_assignment(self):
        u = Unpacker({'a': 2, 'c': 3})
        self.assertEqual(repr(u), 'Unpacker(a=2, c=3)')
        self.assertEqual(str(u), 'Unpacker(a=2, c=3)')
        u['b'] = 4
        self.assertEqual(str(u), 'Unpacker(a=2, c=3, b=4)')
        u['c'] = "hi"
        self.assertEqual(str(u), "Unpacker(a=2, c='hi', b=4)")
        u['a'] = date(2020, 1, 1)
        self.assertEqual(
            str(u),
            "Unpacker(a=datetime.date(2020, 1, 1), c='hi', b=4)",
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_multiple_key_return(self):
        u = Unpacker({'a': 2, 'c': 3})
        self.assertEqual(u['a', 'c'], (2, 3))

        u.b = 4
        self.assertEqual(u['b', 'c'], (4, 3))
        u['b', 'a', 'c'] = (5, 6, 7)
        self.assertEqual(u['a'], 6)
        self.assertEqual(u['c'], 7)
        self.assertEqual(u['b'], 5)
        u['a', 'e'] = 100, 300
        u['b', 'c'] = (n**2 for n in [2, 3])
        self.assertEqual(u['a'], 100)
        self.assertEqual(u['e'], 300)
        self.assertEqual(u['b'], 4)
        self.assertEqual(u['c'], 9)
        with self.assertRaises(Exception):  # ValueError preferably
            u['b', 'a', 'c'] = (5, 6)
        with self.assertRaises(Exception):  # ValueError preferably
            u['b', 'a'] = (5, 6, 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
