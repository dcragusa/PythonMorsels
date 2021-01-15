import unittest

from fuzzystring import FuzzyString


class FuzzyStringTests(unittest.TestCase):

    """Tests for FuzzyString."""

    def test_constructor(self):
        FuzzyString("hello")

    def test_equality_and_inequality_with_same_string(self):
        hello = FuzzyString("hello")
        self.assertEqual(hello, "hello")
        self.assertFalse(hello != "hello")

    def test_equality_with_completely_different_string(self):
        hello = FuzzyString("hello")
        self.assertNotEqual(hello, "Hello there")
        self.assertFalse(hello == "Hello there")
        self.assertNotEqual(hello, "hello there")
        self.assertFalse(hello == "Hello there")

    def test_equality_and_inequality_with_different_case_string(self):
        hello = FuzzyString("hellO")
        self.assertEqual(hello, "Hello")
        self.assertFalse(hello != "Hello")
        self.assertEqual(hello, "HELLO")
        self.assertFalse(hello != "HELLO")

    def test_string_representation(self):
        hello = FuzzyString("heLlO")
        self.assertEqual(str(hello), "heLlO")
        self.assertEqual(repr(hello), repr("heLlO"))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_other_string_comparisons(self):
        apple = FuzzyString("Apple")
        self.assertGreater(apple, "animal")
        self.assertLess("animal", apple)
        self.assertFalse(apple < "animal")
        self.assertFalse("animal" > apple)
        self.assertGreaterEqual(apple, "animal")
        self.assertGreaterEqual(apple, "apple")
        self.assertLessEqual("animal", apple)
        self.assertLessEqual("animal", "animal")
        self.assertFalse(apple <= "animal")
        self.assertFalse("animal" >= apple)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_string_operators(self):
        hello = FuzzyString("heLlO")
        self.assertEqual(hello + "!", "helLo!")
        self.assertNotEqual(hello + "!", "hello")
        self.assertTrue("he" in hello)
        self.assertIn("He", hello)
        self.assertNotIn("He!", hello)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_normalizes_strings(self):
        string = FuzzyString("\u00df and ss")
        self.assertEqual(string, "ss and \u00df")
        string = FuzzyString("ß, ss, \uf9fb, and \u7099")
        self.assertEqual(string, "ss, ß, \u7099, and \uf9fb")

        accent = '\u0301'
        accented_e = FuzzyString('\u00e9')
        self.assertEqual('\u0065\u0301', accented_e)
        self.assertIn(accent, accented_e)


if __name__ == "__main__":
    unittest.main(verbosity=2)
