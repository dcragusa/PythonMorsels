import unittest


from tags_equal import tags_equal


class TagsEqualTests(unittest.TestCase):

    """Tests for tags_equal."""

    def test_no_attributes(self):
        self.assertTrue(tags_equal('<b>', '<b>'))
        self.assertFalse(tags_equal('<a>', '<b>'))

    def test_different_case_of_tag_name(self):
        self.assertTrue(tags_equal('<b>', '<B>'))
        self.assertFalse(tags_equal('<b>', '<A>'))

    def test_with_matching_attributes(self):
        self.assertTrue(tags_equal('<img width=400>', '<img width=400>'))
        self.assertTrue(tags_equal('<img width=400>', '<IMG width=400>'))
        self.assertFalse(tags_equal('<img width=400>', '<img width=200>'))
        self.assertFalse(tags_equal('<img width=400>', '<img height=400>'))
        self.assertFalse(tags_equal('<img width=400>', '<IMG height=400>'))

    def test_with_multiple_matching_attributes(self):
        self.assertTrue(tags_equal(
            '<img width=400 height=200>',
            '<img width=400 height=200>',
        ))
        self.assertFalse(tags_equal(
            '<img width=200 height=400>',
            '<img width=400 height=200>',
        ))

    def test_different_order_attributes(self):
        self.assertTrue(tags_equal(
            '<img height=200 width=400>',
            '<img width=400 height=200>',
        ))
        self.assertFalse(tags_equal(
            '<img height=400 width=200>',
            '<img width=400 height=200>',
        ))

    def test_attributes_with_different_case(self):
        self.assertTrue(tags_equal(
            '<input type=hidden>',
            '<input TYPE=hidden>',
        ))
        self.assertTrue(tags_equal(
            '<input type=hidden>',
            '<input Type=hidden>',
        ))
        self.assertFalse(tags_equal(
            '<input type=HIDDEN>',
            '<input TYPO=HIDDEN>',
        ))
        self.assertFalse(tags_equal(
            '<input type=hidden>',
            '<input TYPO=hide>',
        ))

    def test_different_order_and_case(self):
        self.assertTrue(tags_equal(
            '<IMG height=200 width=400>',
            '<img Width=400 Height=200>',
        ))
        self.assertFalse(tags_equal(
            '<img height=400 WIDTH=200>',
            '<Img width=400 HEIGHT=200>',
        ))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_ignore_duplicate_keys(self):
        self.assertTrue(tags_equal(
            '<input type=hidden type=input>',
            '<input type=hidden>',
        ))
        self.assertFalse(tags_equal(
            '<img type=input type=hidden>',
            '<Img type=hidden>',
        ))
        self.assertTrue(tags_equal(
            '<input TYPE=hidden type=input>',
            '<input type=hidden>',
        ))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_valueless_keys(self):
        self.assertTrue(tags_equal(
            '<input type=checkbox checked>',
            '<input checked type=checkbox>',
        ))
        self.assertFalse(tags_equal(
            '<img type=checkbox checked>',
            '<Img type=checkbox>',
        ))
        self.assertTrue(tags_equal(
            '<input type=checkbox checked>',
            '<input type=checkbox CHECKED>',
        ))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_quotes(self):
        self.assertTrue(tags_equal(
            '<input type="text">',
            '<input type=text>',
        ))
        self.assertFalse(tags_equal(
            '<img type="text">',
            '<Img type=hidden>',
        ))
        self.assertTrue(tags_equal(
            '''<input type=text placeholder='Hi there' value="Hi friend">''',
            '<input type=text value="Hi friend" placeholder="Hi there">',
        ))
        self.assertFalse(tags_equal(
            '<input type=text value="Hi there" placeholder="Hi friend">',
            '<input type=text value="Hi friend" placeholder="Hi there">',
        ))


if __name__ == "__main__":
    unittest.main()
