import unittest

from romannumeral import RomanNumeral


class RomanNumeralTests(unittest.TestCase):

    """Tests for RomanNumeral."""

    def verify(self, integer, numeral):
        self.assertEqual(int(RomanNumeral(numeral)), integer)
        self.assertNotEqual(int(RomanNumeral(numeral)), integer+1)
        self.assertNotEqual(int(RomanNumeral(numeral)), integer-1)

    def test_single_digit(self):
        self.verify(1, "I")
        self.verify(5, "V")
        self.verify(10, "X")
        self.verify(50, "L")
        self.verify(100, "C")
        self.verify(500, "D")
        self.verify(1000, "M")

    def test_two_digits_ascending(self):
        self.verify(2, "II")
        self.verify(6, "VI")
        self.verify(11, "XI")
        self.verify(15, "XV")
        self.verify(20, "XX")
        self.verify(60, "LX")
        self.verify(101, "CI")
        self.verify(105, "CV")
        self.verify(110, "CX")
        self.verify(150, "CL")
        self.verify(550, "DL")
        self.verify(600, "DC")
        self.verify(1100, "MC")
        self.verify(2000, "MM")

    def test_three_digits_ascending(self):
        self.verify(3, "III")
        self.verify(7, "VII")
        self.verify(12, "XII")
        self.verify(16, "XVI")
        self.verify(21, "XXI")
        self.verify(25, "XXV")
        self.verify(30, "XXX")

    def test_four_digits_ascending(self):
        self.verify(8, "VIII")
        self.verify(13, "XIII")
        self.verify(17, "XVII")
        self.verify(22, "XXII")
        self.verify(26, "XXVI")
        self.verify(31, "XXXI")
        self.verify(35, "XXXV")

    def test_many_digits(self):
        self.verify(1888, "MDCCCLXXXVIII")

    def test_subtractive(self):
        self.verify(4, "IV")
        self.verify(9, "IX")
        self.verify(14, "XIV")
        self.verify(19, "XIX")
        self.verify(24, "XXIV")
        self.verify(29, "XXIX")
        self.verify(40, "XL")
        self.verify(90, "XC")
        self.verify(44, "XLIV")
        self.verify(94, "XCIV")
        self.verify(49, "XLIX")
        self.verify(99, "XCIX")
        self.verify(1999, "MCMXCIX")
        self.verify(1948, "MCMXLVIII")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_from_int_and_string_representation(self):
        self.assertEqual(str(RomanNumeral("I")), "I")
        self.assertEqual(repr(RomanNumeral("CD")), "RomanNumeral('CD')")
        self.assertEqual(str(RomanNumeral.from_int(1)), str(RomanNumeral("I")))
        self.assertEqual(str(RomanNumeral.from_int(10)), "X")
        self.assertEqual(str(RomanNumeral.from_int(21)), "XXI")
        self.assertEqual(str(RomanNumeral.from_int(600)), "DC")
        self.assertEqual(str(RomanNumeral.from_int(2000)), "MM")
        self.assertEqual(str(RomanNumeral.from_int(12)), "XII")
        self.assertEqual(str(RomanNumeral.from_int(25)), "XXV")
        self.assertEqual(str(RomanNumeral.from_int(6)), "VI")
        self.assertEqual(str(RomanNumeral.from_int(4)), "IV")
        self.assertEqual(str(RomanNumeral.from_int(9)), "IX")
        self.assertEqual(str(RomanNumeral.from_int(14)), "XIV")
        self.assertEqual(str(RomanNumeral.from_int(1888)), "MDCCCLXXXVIII")
        self.assertEqual(str(RomanNumeral.from_int(1999)), "MCMXCIX")
        self.assertEqual(str(RomanNumeral.from_int(1948)), "MCMXLVIII")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_adding(self):
        sixty_five = RomanNumeral("LXV")
        eighty_seven = RomanNumeral("LXXXVII")
        self.assertEqual(int(sixty_five + eighty_seven), 152)
        self.assertEqual(type(sixty_five + eighty_seven), RomanNumeral)
        self.assertEqual(int(sixty_five + 87), 152)
        self.assertEqual(type(sixty_five + 87), RomanNumeral)
        self.assertEqual(str(sixty_five + 87), str("CLII"))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_equality_and_ordering(self):
        self.assertEqual(RomanNumeral("I"), 1)
        self.assertNotEqual(RomanNumeral("I"), 2)
        self.assertEqual(RomanNumeral("I"), "I")
        self.assertEqual(RomanNumeral.from_int(10), "X")
        self.assertEqual(RomanNumeral.from_int(21), "XXI")
        self.assertEqual(RomanNumeral.from_int(600), "DC")
        self.assertEqual(RomanNumeral.from_int(2000), "MM")
        self.assertEqual(RomanNumeral.from_int(12), "XII")
        self.assertEqual(RomanNumeral.from_int(25), "XXV")
        self.assertEqual(RomanNumeral.from_int(6), "VI")
        self.assertEqual(RomanNumeral.from_int(4), "IV")
        self.assertEqual(RomanNumeral.from_int(9), "IX")
        self.assertEqual(RomanNumeral.from_int(14), "XIV")
        self.assertEqual(RomanNumeral.from_int(1888), "MDCCCLXXXVIII")
        self.assertEqual(RomanNumeral.from_int(1999), "MCMXCIX")
        self.assertEqual(RomanNumeral.from_int(1948), "MCMXLVIII")
        self.assertLess(RomanNumeral("MCMXLVIII"), RomanNumeral("MCMXCIX"))
        self.assertGreater(RomanNumeral("MCMXCIX"), RomanNumeral("MCMXLVIII"))
        self.assertGreaterEqual(RomanNumeral("IX"), RomanNumeral("III"))
        self.assertLessEqual(RomanNumeral("III"), RomanNumeral("IX"))
        self.assertGreaterEqual(RomanNumeral("X"), RomanNumeral("X"))
        self.assertLessEqual(RomanNumeral("IIII"), RomanNumeral("IV"))
        self.assertFalse(RomanNumeral("V") < RomanNumeral("IV"))
        self.assertFalse(RomanNumeral("V") > RomanNumeral("IX"))
        self.assertFalse(RomanNumeral("V") <= RomanNumeral("IV"))
        self.assertFalse(RomanNumeral("V") >= RomanNumeral("IX"))
        with self.assertRaises(TypeError):
            RomanNumeral("X") < "XX"
        with self.assertRaises(TypeError):
            RomanNumeral("X") <= "XX"
        with self.assertRaises(TypeError):
            RomanNumeral("X") > "XX"
        with self.assertRaises(TypeError):
            RomanNumeral("X") >= "XX"
        self.assertFalse(RomanNumeral("V") < 4)
        self.assertFalse(RomanNumeral("V") > 9)
        self.assertFalse(RomanNumeral("V") <= 4)
        self.assertFalse(RomanNumeral("V") >= 9)
        with self.assertRaises(TypeError):
            RomanNumeral("X") < "XX"
        with self.assertRaises(TypeError):
            RomanNumeral("X") <= "XX"
        with self.assertRaises(TypeError):
            RomanNumeral("X") > "XX"
        with self.assertRaises(TypeError):
            RomanNumeral("X") >= "XX"


if __name__ == "__main__":
    unittest.main(verbosity=2)
