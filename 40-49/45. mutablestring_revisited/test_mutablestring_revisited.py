import unittest

from mutablestring_revisited import MutableString


class MutableStringTests(unittest.TestCase):

    """Tests for MutableString."""

    def test_constructor(self):
        MutableString("hello")

    def test_equality_and_inequality(self):
        self.assertEqual(MutableString("hello"), "hello")
        self.assertEqual(MutableString("hello"), MutableString("hello"))
        self.assertNotEqual(MutableString("hello"), "hella")
        self.assertNotEqual(MutableString("hello"), MutableString("hella"))
        self.assertIs(MutableString("hello") == "hella", False)
        self.assertIs(MutableString("hello") != "hello", False)
        self.assertIs(MutableString("hello") == MutableString("hella"), False)
        self.assertIs(MutableString("hello") != MutableString("hello"), False)

    def test_string_representation(self):
        self.assertEqual(str(MutableString("hello")), "hello")
        self.assertEqual(repr(MutableString("hello")), "'hello'")

    def test_has_length(self):
        self.assertEqual(len(MutableString("hello")), 5)
        self.assertEqual(len(MutableString("hi")), 2)

    def test_concatenation(self):
        greeting = MutableString("hello")
        self.assertEqual(greeting + "!", "hello!")
        self.assertEqual(greeting + MutableString("!"), "hello!")
        self.assertIs(type(greeting + "!"), MutableString)

    def test_setitem(self):
        greeting = MutableString("hello world")
        self.assertEqual(greeting, "hello world")
        greeting[4] = "a"
        self.assertEqual(greeting, "hella world")
        self.assertNotEqual(greeting, "hello world")

    def test_indexing_works(self):
        greeting = MutableString("hiya")
        self.assertEqual(greeting[-3], "i")
        self.assertIs(type(greeting[-3]), MutableString)

    def test_slicing_works(self):
        greeting = MutableString("hiya")
        self.assertEqual(greeting[-3:], "iya")
        self.assertIs(type(greeting[-3:]), MutableString)

    def test_assigning_into_slices(self):
        greeting = MutableString("hiya")
        greeting[-3:] = "ey!"
        self.assertEqual(greeting, "hey!")

    def test_deleting_indexes_and_slices(self):
        greeting = MutableString("hiya!")
        del greeting[-1]
        self.assertEqual(greeting, "hiya")
        del greeting[:2]
        self.assertEqual(greeting, "ya")

    def test_mutable_sequence_methods(self):
        greeting = MutableString("hey")
        greeting.append("!")
        self.assertEqual(greeting, "hey!")
        greeting.insert(-1, "a")
        self.assertEqual(greeting, "heya!")
        self.assertEqual(greeting.pop(-2), "a")
        self.assertEqual(greeting, "hey!")
        self.assertIs(type(greeting.pop()), MutableString)
        self.assertEqual(greeting, "hey")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_in_place_operations(self):
        string = MutableString("these are")
        string2 = string
        self.assertTrue(string2 == "these are")
        string += MutableString(" words")
        string += "!"
        self.assertEqual(string, "these are words!")
        self.assertIs(string, string2)
        self.assertFalse(string2 == "these are")
        string *= 2
        self.assertIs(string, string2)
        self.assertEqual(string, "these are words!these are words!")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_string_methods(self):
        hiya = MutableString("hiya")
        heya = hiya.replace('i', 'e')
        self.assertEqual(heya, "heya")
        self.assertIs(type(heya), MutableString)
        self.assertEqual(heya.upper(), "HEYA")
        self.assertIs(type(heya.lower()), MutableString)
        self.assertTrue(hiya.endswith('ya'))
        self.assertFalse(hiya.endswith('ye'))
        self.assertTrue(hiya.endswith(('a', 'e')))
        self.assertFalse(hiya.endswith(('i', 'e')))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_joining(self):
        strings = [
            MutableString("these"),
            MutableString("are"),
            MutableString("some"),
            MutableString("words"),
        ]
        self.assertEqual(" ".join(strings), "these are some words")


if __name__ == "__main__":
    unittest.main(verbosity=2)
