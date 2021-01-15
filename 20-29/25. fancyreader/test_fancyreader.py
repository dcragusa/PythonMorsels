import unittest
from io import StringIO
from textwrap import dedent

from fancyreader import FancyReader


class FancyReaderTests(unittest.TestCase):

    """Tests for FancyReader."""

    def test_with_files(self):
        reader = FancyReader(
            StringIO("1,2,3\r\n4,5,6\r\n"),
            fieldnames=['a', 'b', 'c'],
        )
        self.assertEqual(len(list(reader)), 2)

    def test_with_list(self):
        text = "1,2,3\n4,5,6"
        reader = FancyReader(text.splitlines(), fieldnames=['a', 'b', 'c'])
        self.assertEqual(len(list(reader)), 2)

    def test_many_columns_and_rows(self):
        text = dedent("""
            Julia,Spender,purple,Two in the hand is worth one in the fridge
            Sarah,Taylor,green,"Learn from yesterday, live for today"
            Gary,Richter,blue,Be someone you would be proud to know
            Kathleen,Blocker,red,Live everyday like it's your last
            Angelo,Griffith,pink,Don't do today what you could do tomorrow
        """).lstrip()
        reader = FancyReader(
            text.splitlines(),
            fieldnames=['first', 'last', 'color', 'saying'],
        )
        rows = list(reader)
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[4].color, "pink")
        self.assertEqual(
            rows[1].saying,
            "Learn from yesterday, live for today",
        )
        self.assertEqual(rows[2].first, "Gary")
        self.assertEqual(rows[3].last, "Blocker")

    def test_accessing_attributes_from_rows(self):
        text = "1,2,3\n4,5,6"
        reader = FancyReader(text.splitlines(), fieldnames=['a', 'b', 'c'])
        row1, row2 = reader
        self.assertEqual(row1.a, '1')
        self.assertEqual(row1.b, '2')
        self.assertEqual(row1.c, '3')
        self.assertEqual(row2.a, '4')
        self.assertEqual(row2.b, '5')
        self.assertEqual(row2.c, '6')

    def test_lazy_looping(self):
        my_file = StringIO("1,2,3\r\n4,5,6\r\n")
        reader = FancyReader((x for x in my_file), fieldnames=['a', 'b', 'c'])
        self.assertEqual(my_file.tell(), 0)
        next(reader)
        self.assertEqual(list(my_file), ["4,5,6\r\n"])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_row_iterability_and_string_representation(self):
        text = "1,2,3\n4,5,6"
        reader = FancyReader(text.splitlines(), fieldnames=['a', 'b', 'c'])
        rows = list(reader)
        self.assertEqual(tuple(rows[0]), ('1', '2', '3'))
        self.assertEqual(tuple(rows[1]), ('4', '5', '6'))
        self.assertEqual(repr(rows[0]), "Row(a='1', b='2', c='3')")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_no_fieldnames_specified(self):
        # Test fieldnames argument
        my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
        reader = FancyReader(my_file)
        rows = list(reader)
        self.assertEqual(rows[0].a, '1')
        self.assertEqual(rows[0].b, '2')
        self.assertEqual(rows[0].c, '3')
        self.assertEqual(rows[1].a, '4')
        self.assertEqual(rows[1].b, '5')
        self.assertEqual(rows[1].c, '6')

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_line_num(self):
        text = "a,b,c\n1,2,3\n4,5,6"
        # Reader with fieldnames
        reader = FancyReader(
            text.splitlines(),
            fieldnames=['a', 'b', 'c'],
        )
        self.assertEqual(reader.line_num, 0)
        next(reader)
        self.assertEqual(reader.line_num, 1)
        next(reader)
        self.assertEqual(reader.line_num, 2)

        # Reader without fieldnames
        reader = FancyReader(text.splitlines())
        next(reader)
        self.assertEqual(reader.line_num, 2)
        next(reader)
        self.assertEqual(reader.line_num, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
