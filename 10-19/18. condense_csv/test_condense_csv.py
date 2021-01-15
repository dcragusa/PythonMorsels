import unittest
from textwrap import dedent

from condense_csv import condense_csv


class CondenseCSVTests(unittest.TestCase):

    """Tests for condense_csv."""

    def assertLinesEqual(self, text1, text2):
        self.assertEqual(text1.splitlines(), text2.splitlines())

    def test_two_groups_one_attribute_each(self):
        text = dedent("""
            01,Title,Ran So Hard the Sun Went Down
            02,Title,Honky Tonk Heroes (Like Me)
        """).strip()
        expected = dedent("""
            Num,Title
            01,Ran So Hard the Sun Went Down
            02,Honky Tonk Heroes (Like Me)
        """).strip()
        self.assertLinesEqual(condense_csv(text, id_name='Num'), expected)

    def test_two_groups_multiple_attributes(self):
        text = dedent("""
            01,Artist,Otis Taylor
            01,Title,Ran So Hard the Sun Went Down
            01,Time,3:52
            02,Artist,Waylon Jennings
            02,Title,Honky Tonk Heroes (Like Me)
            02,Time,3:29
        """).strip()
        expected = dedent("""
            Track,Artist,Title,Time
            01,Otis Taylor,Ran So Hard the Sun Went Down,3:52
            02,Waylon Jennings,Honky Tonk Heroes (Like Me),3:29
        """).strip()
        self.assertLinesEqual(condense_csv(text, id_name='Track'), expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_commas_in_data(self):
        text = dedent("""
            01,Artist,Otis Taylor
            01,Title,Ran So Hard the Sun Went Down
            01,Time,3:52
            02,Artist,Waylon Jennings
            02,Title,Honky Tonk Heroes (Like Me)
            02,"Time","3:29"
            03,Artist,David Allan Coe
            03,Title,"Willie, Waylon, And Me"
            03,Time,3:26
        """).strip()
        expected = dedent("""
            Track,Artist,Title,Time
            01,Otis Taylor,Ran So Hard the Sun Went Down,3:52
            02,Waylon Jennings,Honky Tonk Heroes (Like Me),3:29
            03,David Allan Coe,"Willie, Waylon, And Me",3:26
        """).strip()
        self.assertLinesEqual(condense_csv(text, id_name='Track'), expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_read_headers_when_no_id_name_given(self):
        text = dedent("""
            NN,Property,Value
            01,Artist,Otis Taylor
            01,Title,Ran So Hard the Sun Went Down
            01,Time,3:52
            02,Artist,Waylon Jennings
            02,Title,Honky Tonk Heroes (Like Me)
            02,Time,3:29
        """).strip()
        expected = dedent("""
            NN,Artist,Title,Time
            01,Otis Taylor,Ran So Hard the Sun Went Down,3:52
            02,Waylon Jennings,Honky Tonk Heroes (Like Me),3:29
        """).strip()
        self.assertLinesEqual(condense_csv(text), expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_different_property_ordering_and_missing_properties(self):
        text = dedent("""
            01,Artist,Otis Taylor
            01,Title,Ran So Hard the Sun Went Down
            01,Time,3:52
            02,Title,Honky Tonk Heroes (Like Me)
            02,Artist,Waylon Jennings
            02,Time,3:29
            03,Time,3:47
            03,Title,Hear My Train A Coming
        """).strip()
        expected = dedent("""
            NN,Artist,Title,Time
            01,Otis Taylor,Ran So Hard the Sun Went Down,3:52
            02,Waylon Jennings,Honky Tonk Heroes (Like Me),3:29
            03,,Hear My Train A Coming,3:47
        """).strip()
        self.assertLinesEqual(condense_csv(text, id_name='NN'), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
