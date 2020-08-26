from io import StringIO
from textwrap import dedent
import unittest


from fancyreader_revisited import FancyReader


class FancyReaderTests(unittest.TestCase):

    """Tests for FancyReader."""

    def test_with_files(self):
        reader = FancyReader(StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n"))
        self.assertEqual(len(list(reader)), 2)

    def test_with_list(self):
        text = "a,b,c\n1,2,3\n4,5,6"
        reader = FancyReader(text.splitlines())
        self.assertEqual(len(list(reader)), 2)

    def test_many_columns_and_rows(self):
        text = dedent("""
            first,last,color,saying
            Julia,Spender,purple,Two in the hand is worth one in the fridge
            Sarah,Taylor,green,"Learn from yesterday, live for today"
            Gary,Richter,blue,Be someone you would be proud to know
            Kathleen,Blocker,red,Live everyday like it's your last
            Angelo,Griffith,pink,Don't do today what you could do tomorrow
        """).lstrip()
        reader = FancyReader(text.splitlines())
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
        text = "a,b,c\n1,2,3\n4,5,6"
        reader = FancyReader(text.splitlines())
        row1, row2 = reader
        self.assertEqual(row1.a, '1')
        self.assertEqual(row1.b, '2')
        self.assertEqual(row1.c, '3')
        self.assertEqual(row2.a, '4')
        self.assertEqual(row2.b, '5')
        self.assertEqual(row2.c, '6')

    def test_lazy_looping(self):
        my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
        reader = FancyReader(x for x in my_file)
        self.assertEqual(my_file.tell(), 0)
        self.assertEqual(tuple(next(reader)), ('1', '2', '3'))
        self.assertEqual(list(my_file), ["4,5,6\r\n"])

    def test_row_string_representation(self):
        my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
        reader = FancyReader(my_file)
        self.assertEqual(repr(next(reader)), "Row(a='1', b='2', c='3')")

    def test_row_uses_slots_instead_of_dict(self):
        my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
        reader = FancyReader(my_file)
        row1 = next(reader)
        self.assertTrue(hasattr(row1, '__slots__'))
        with self.assertRaises(AttributeError):
            row1.__dict__

    def test_delimiter(self):
        text = "a|b|c\n1|2|3\n4|5|6"
        reader = FancyReader(text.splitlines(), delimiter='|')
        row1, row2 = reader
        self.assertEqual(row1.a, '1')
        self.assertEqual(row2.b, '5')

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_row_iterability(self):
        text = "a,b,c\n1,2,3\n4,5,6"
        reader = FancyReader(text.splitlines())
        rows = list(reader)
        self.assertEqual(tuple(rows[0]), ('1', '2', '3'))
        self.assertEqual(tuple(rows[1]), ('4', '5', '6'))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_fieldnames_attribute(self):
        # Loop first
        my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
        reader = FancyReader(my_file)
        self.assertEqual(my_file.tell(), 0)
        self.assertEqual(tuple(next(reader)), ('1', '2', '3'))
        self.assertEqual(reader.fieldnames, ['a', 'b', 'c'])

        # Test fieldnames argument
        my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
        reader = FancyReader(my_file, fieldnames=['a', 'b', 'c'])
        self.assertEqual(my_file.tell(), 0)
        self.assertEqual(reader.fieldnames, ['a', 'b', 'c'])
        self.assertEqual(my_file.tell(), 0)

        # Access fieldnames first
        my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
        reader = FancyReader(my_file)
        self.assertEqual(my_file.tell(), 0)
        self.assertEqual(reader.fieldnames, ['a', 'b', 'c'])
        self.assertEqual(my_file.tell(), 7)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_mutable_rows(self):
        text = "a,b,c\n1,2,3\n4,5,6"
        reader = FancyReader(text.splitlines())
        row1, row2 = reader
        self.assertEqual(row1.a, '1')
        row1.a = '9'
        self.assertEqual(row1.a, '9')
        self.assertEqual(row2.a, '4')
        self.assertEqual(tuple(row1), ('9', '2', '3'))
        self.assertEqual(repr(row1), "Row(a='9', b='2', c='3')")


if __name__ == "__main__":
    unittest.main(verbosity=2)
