from types import TracebackType
import unittest

from suppress import suppress


class SuppressTests(unittest.TestCase):

    """Tests for suppress."""

    def test_works_when_no_exception_raised(self):
        with suppress(Exception):
            x = 4
        self.assertEqual(x, 4)

    def test_suppress_specific_exception(self):
        with suppress(ValueError):
            x = 1
            int('hello')
            x = 2
        self.assertEqual(x, 1)
        with suppress(TypeError):
            x = 3
            int(None)
            x = 4
        self.assertEqual(x, 3)

    def test_keyerror_and_index_error(self):
        with suppress(KeyError):
            my_dict = {'key': 'value'}
            my_dict[4]
        self.assertEqual(my_dict, {'key': 'value'})
        with suppress(IndexError):
            my_list = ['item']
            my_list[1]
            self.assertEqual(my_list, ['item'])

    def test_suppresses_parent_exceptions(self):
        with suppress(LookupError):
            my_dict = {'key': 'value'}
            my_dict[4]
        self.assertEqual(my_dict, {'key': 'value'})
        with suppress(LookupError):
            my_list = ['item']
            my_list[1]
            self.assertEqual(my_list, ['item'])

    def test_does_not_suppress_other_exceptions(self):
        with self.assertRaises(KeyError):
            with suppress(IndexError):
                my_dict = {'key': 'value'}
                my_dict[4]
            self.assertEqual(my_dict, {'key': 'value'})
        with self.assertRaises(IndexError):
            with suppress(KeyError):
                my_list = ['item']
                my_list[1]
                self.assertEqual(my_list, ['item'])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_catches_any_number_of_exceptions(self):
        with suppress(ValueError, TypeError):
            int('hello')
        with suppress(IndexError, TypeError):
            int(None)
        with self.assertRaises(KeyError):
            with suppress(IndexError, TypeError):
                {0: 1}[1]
        with suppress(ValueError, SystemError, IndexError, TypeError):
            ['item'][1]

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allows_exception_to_be_viewed(self):
        with suppress(LookupError) as suppressed:
            my_dict = {'key': 'value'}
            my_dict[4]
        self.assertEqual(type(suppressed.exception), KeyError)
        self.assertEqual(type(suppressed.traceback), TracebackType)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_works_as_a_decorator(self):
        @suppress(TypeError)
        def len_or_none(thing):
            return len(thing)
        self.assertEqual(len_or_none(['a', 'b', 'c']), 3)
        self.assertEqual(len_or_none(3.5), None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
