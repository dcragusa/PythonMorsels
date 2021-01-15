import os.path
import unittest

from make_file import make_file


class MakeFileTests(unittest.TestCase):

    """Tests for make_file."""

    def test_file_created(self):
        with make_file() as filename:
            with open(filename, mode='rt') as my_file:
                contents = my_file.read()
            self.assertEqual(contents, '')

    def test_file_writeable(self):
        with make_file() as filename:
            with open(filename, mode='wt') as my_file:
                my_file.write('hello!')
            with open(filename, mode='rt') as my_file:
                contents = my_file.read()
            self.assertEqual(contents, 'hello!')

    def test_file_deleted_afterward(self):
        with make_file() as filename:
            self.assertTrue(os.path.isfile(filename))
        self.assertFalse(os.path.isfile(filename))

    def test_file_deleted_when_storing_context_manager_object(self):
        context = make_file()
        with context as filename:
            self.assertTrue(os.path.isfile(filename))
        self.assertFalse(os.path.isfile(filename))

    def test_file_deleted_even_after_exception(self):
        class CustomException(ValueError): pass
        with self.assertRaises(CustomException):
            with make_file() as filename:
                self.assertTrue(os.path.isfile(filename))
                raise CustomException("Something went wrong here!")
        self.assertFalse(os.path.isfile(filename))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_file_to_have_initial_contents(self):
        with make_file(contents="hello there!") as filename:
            with open(filename, mode='rt') as my_file:
                contents = my_file.read()
            self.assertEqual(contents, 'hello there!')

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_specifying_directory(self):
        from tempfile import mkdtemp  # This may be a hint
        directory = mkdtemp()
        with make_file(contents="hi\nthere!", directory=directory) as filename:
            self.assertEqual(os.path.dirname(filename), directory)
            with open(filename) as my_file:
                self.assertEqual(my_file.read(), 'hi\nthere!')

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_specifying_file_options(self):
        with make_file(contents=b"hi\nthere!", mode='wb') as filename:
            with open(filename, mode='rt') as my_file:
                self.assertEqual(my_file.read(), 'hi\nthere!')
        with make_file(contents="hi\nthere!", encoding='utf-16-le') as filename:
            with open(filename, encoding='utf-16-le') as my_file:
                self.assertEqual(my_file.read(), 'hi\nthere!')
        with make_file(contents="hi\nthere!", newline='\r') as filename:
            with open(filename, mode='rt', newline='') as my_file:
                self.assertEqual(my_file.read(), 'hi\rthere!')


if __name__ == "__main__":
    unittest.main(verbosity=2)
