import unittest


from permadict import PermaDict


class PermaDictTests(unittest.TestCase):

    """Tests for PermaDict."""

    def test_can_add_key(self):
        d = PermaDict()
        with self.assertRaises(KeyError):
            d[4]
        d[4] = "the number four"
        self.assertEqual(d[4], "the number four")

    def test_equal_to_dict(self):
        d = PermaDict()
        self.assertNotEqual(d, {4: "the number four"})
        d[4] = "the number four"
        self.assertEqual(d, {4: "the number four"})
        self.assertNotEqual(d, {4: "the number five"})
        self.assertEqual(PermaDict({1: 2, 3: 4}), {1: 2, 3: 4})

    def test_can_iterate(self):
        d = PermaDict({'a': 'b', 'c': 'd'})
        self.assertEqual(set(d), {'a', 'c'})

    def test_has_keys_values_and_items(self):
        d = PermaDict({'a': 'b', 'c': 'd'})
        self.assertEqual(set(d.keys()), {'a', 'c'})
        self.assertEqual(set(d.values()), {'b', 'd'})
        self.assertEqual(set(d.items()), {('a', 'b'), ('c', 'd')})

    def test_can_pop_key(self):
        d = PermaDict()
        d[4] = "the number four"
        self.assertEqual(d, {4: "the number four"})
        self.assertEqual(d.pop(4), "the number four")
        self.assertEqual(d, {})

    def test_can_update_with_new_keys(self):
        d = PermaDict()
        d.update({'a': 1})
        self.assertEqual(d, {'a': 1})
        d.update([('b', 2)])
        self.assertEqual(d, {'a': 1, 'b': 2})
        d.update(c=3)
        self.assertEqual(d, {'a': 1, 'b': 2, 'c': 3})

    def test_error_when_changing_value(self):
        d = PermaDict()
        d[4] = "the number four"
        with self.assertRaises(KeyError):
            d[4] = "the number 4"
        self.assertEqual(d, {4: "the number four"})

    def test_error_when_updating_value(self):
        d = PermaDict({1: 2, 3: 4})
        with self.assertRaises(KeyError):
            d.update([(5, 6), (1, 8), (7, 8)])
        self.assertEqual(d, {1: 2, 3: 4, 5: 6})

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_force_set_method(self):
        d = PermaDict({1: 2, 3: 4})
        d.force_set(3, 6)
        d.force_set(5, 6)
        self.assertEqual(d, {1: 2, 3: 6, 5: 6})

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_silent_flag_to_initializer(self):
        d = PermaDict({1: 2, 3: 4}, silent=True)
        d.update([(5, 6), (1, 8), (7, 8)])
        self.assertEqual(d, {1: 2, 3: 4, 5: 6, 7: 8})
        d[3] = 6
        d[9] = 10
        self.assertEqual(d, {1: 2, 3: 4, 5: 6, 7: 8, 9: 10})
        e = PermaDict(silent=True, not_silent=False, super_silent=True)
        self.assertEqual(e, {'not_silent': False, 'super_silent': True})

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_force_argument_to_update(self):
        d = PermaDict({1: 2, 3: 4}, silent=True)
        d.update([(5, 6), (1, 8), (7, 8)], force=True)
        self.assertEqual(d, {1: 8, 3: 4, 5: 6, 7: 8})
        e = PermaDict()
        e.update(a=1, b=2, force=True)
        self.assertEqual(e, {'a': 1, 'b': 2})


if __name__ == "__main__":
    unittest.main(verbosity=2)
