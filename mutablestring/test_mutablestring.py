import unittest


from mutablestring import MutableString


class MutableStringTests(unittest.TestCase):

    """Tests for MutableString."""

    def test_constructor(self):
        MutableString("hello")
        MutableString(4)

    def test_equality_and_inequality(self):
        self.assertEqual(MutableString("hello"), "hello")
        self.assertEqual(MutableString("hello"), MutableString("hello"))
        self.assertNotEqual(MutableString("hello"), "hella")
        self.assertNotEqual(MutableString("hello"), MutableString("hella"))
        self.assertIs(MutableString("hello") == "hella", False)
        self.assertIs(MutableString("hello") != "hello", False)
        self.assertIs(MutableString("hello") == MutableString("hella"), False)
        self.assertIs(MutableString("hello") != MutableString("hello"), False)

    def test_equality_with_unknown_type(self):
        self.assertIs(MutableString("hello") == 4, False)
        class SillyType:
            def __eq__(self, other):
                return True
        self.assertEqual(MutableString("hello"), SillyType())

    def test_string_representation(self):
        self.assertEqual(str(MutableString("hello")), "hello")
        self.assertEqual(repr(MutableString("hello")), "'hello'")
        self.assertEqual(str(MutableString(['hi', True])), "['hi', True]")
        self.assertEqual(str(MutableString(4)), "4")

    def test_has_length(self):
        self.assertEqual(len(MutableString("hello")), 5)
        self.assertEqual(len(MutableString("hi")), 2)

    def test_indexing_works(self):
        greeting = MutableString("hiya")
        self.assertEqual(greeting[-3], "i")

    def test_slicing_works(self):
        greeting = MutableString("hiya")
        self.assertEqual(greeting[-3:], "iya")

    def test_iterating(self):
        greeting = MutableString("hiya")
        self.assertEqual(list(greeting), ['h', 'i', 'y', 'a'])

    def test_concatenation(self):
        greeting = MutableString("hello")
        self.assertEqual(greeting + "!", "hello!")
        self.assertEqual(greeting + MutableString("!"), "hello!")

    def test_setitem(self):
        greeting = MutableString("hello world")
        self.assertEqual(greeting, "hello world")
        greeting[4] = "a"
        self.assertEqual(greeting, "hella world")
        self.assertNotEqual(greeting, "hello world")

    def test_containment(self):
        hiya = MutableString("hiya")
        self.assertIn("ya", hiya)

    def test_string_methods(self):
        hiya = MutableString("Hiya")
        self.assertEqual(hiya.replace('i', 'e'), "Heya")
        self.assertEqual(hiya.upper(), "HIYA")
        self.assertEqual(hiya.lower(), "hiya")
        self.assertTrue(hiya.endswith('ya'))
        self.assertFalse(hiya.endswith('ye'))
        self.assertTrue(hiya.endswith(('a', 'e')))
        self.assertFalse(hiya.endswith(('i', 'e')))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_assigning_and_deleting_slices(self):
        greeting = MutableString("hiya")
        greeting[-3:] = "ey!"
        self.assertEqual(greeting, "hey!")
        del greeting[-1]
        self.assertEqual(greeting, "hey")
        del greeting[:2]
        self.assertEqual(greeting, "y")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_correct_type_returned(self):
        hiya = MutableString("hiya")
        self.assertIs(type(hiya[-3]), MutableString)
        self.assertIs(type(hiya[-3:]), MutableString)
        self.assertEqual({type(c) for c in hiya}, {MutableString})
        self.assertIs(type(hiya[0]), MutableString)
        hiya[0] = "H"
        self.assertIs(type(hiya[0]), MutableString)
        self.assertIs(type(hiya + "!"), MutableString)
        self.assertIs(type(hiya.replace('i', 'e')), MutableString)
        self.assertIs(type(hiya.lower()), MutableString)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_append_insert_and_pop(self):
        greeting = MutableString("hey")
        greeting.append("!")
        self.assertEqual(greeting, "hey!")
        self.assertEqual(type(greeting[-1]), MutableString)
        greeting.insert(-1, "a")
        self.assertEqual(greeting[-2], "a")
        self.assertEqual(type(greeting[-2]), MutableString)
        self.assertEqual(greeting, "heya!")
        self.assertEqual(greeting.pop(-2), "a")
        self.assertEqual(greeting, "hey!")
        self.assertIs(type(greeting.pop()), MutableString)
        self.assertEqual(greeting, "hey")


if __name__ == "__main__":
    unittest.main(verbosity=2)
