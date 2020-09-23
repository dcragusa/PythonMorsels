import unittest
from contextlib import contextmanager
from io import (
    BytesIO,
    UnsupportedOperation,
    TextIOWrapper,
    DEFAULT_BUFFER_SIZE,
)
from textwrap import dedent
from unittest.mock import patch

from last_lines import last_lines


class LastLinesTests(unittest.TestCase):

    """Tests for last_lines."""

    def test_no_newlines(self):
        contents = "a single line of text"
        filename = 'file1.txt'
        with patch_open(contents, filename):
            self.assertEqual(list(last_lines(filename)), [contents])

    def test_one_newline_at_the_end(self):
        contents = "a single line of text\n"
        filename = 'file2.txt'
        with patch_open(contents, filename):
            self.assertEqual(list(last_lines(filename)), [contents])

    def test_one_newline_in_middle(self):
        contents = "two lines\nof text"
        filename = 'my file.txt'
        reversed_lines = ["of text", "two lines\n"]
        with patch_open(contents, filename):
            self.assertEqual(list(last_lines(filename)), reversed_lines)

    def test_two_newlines_with_one_at_the_end(self):
        contents = "two lines\nof text\n"
        filename = 'hello.txt'
        reversed_lines = ["of text\n", "two lines\n"]
        with patch_open(contents, filename):
            self.assertEqual(list(last_lines(filename)), reversed_lines)

    def test_newlines_at_beginning(self):
        contents = "\n\ntext!\n"
        filename = 'hiya.txt'
        reversed_lines = ["text!\n", "\n", "\n"]
        with patch_open(contents, filename):
            self.assertEqual(list(last_lines(filename)), reversed_lines)

    def test_newlines_at_end(self):
        contents = "text!\n\n\n\n\n"
        filename = 'newlines_at_end.txt'
        reversed_lines = ["\n", "\n", "\n", "\n", "text!\n"]
        with patch_open(contents, filename):
            self.assertEqual(list(last_lines(filename)), reversed_lines)

    def test_many_lines(self):
        numbers = range(1000)
        filename = 'newlines_at_end.txt'
        contents = "\n".join(
            "line {}".format(i)
            for i in numbers
        )
        with patch_open(contents, filename):
            for i, line in zip(reversed(numbers), last_lines(filename)):
                self.assertEqual(line.rstrip(), "line {}".format(i))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_iterator(self):
        filename = 'iterator_test'
        contents = dedent("""
            This is the start
            Of a file
            This is the end
        """).strip()
        with patch_open(contents, filename):
            lines = last_lines(filename)
            self.assertEqual(next(lines), "This is the end")
        self.assertEqual(next(lines), "Of a file\n")
        self.assertEqual(next(lines), "This is the start\n")
        with self.assertRaises(StopIteration):
            next(lines)
        self.assertEqual(list(lines), [])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_lazy_reading(self):
        contents = "hi\n" * 10000
        filename = 'lazy reading'
        with patch_open(contents, filename, max_read=DEFAULT_BUFFER_SIZE) as fake_open:
            lines = last_lines(filename)
            self.assertEqual(len(fake_open.file.reads), 0, 'no reads yet')
            for i in range(10000):
                if i == 100:
                    self.assertLess(
                        len(fake_open.file.reads),
                        3,
                        'should really only be 1 read at this point',
                    )
                self.assertEqual(next(lines), "hi\n")
            self.assertEqual(next(lines, None), None)
        self.assertLess(
            len(fake_open.file.reads),
            10,
            'whole file should be less than 10 reads',
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_unicode_characters(self):
        contents = (
           '\U0001f496 \U0001f601\U0001f31f \u26c4\u274c \u274c \xa9\n'
           '\u2728\u274c \U0001f31f \U0001f496 \U0001f496 \U0001f496 \u2728\n'
           '\u26c4 \U0001f496 \u2728\U0001f496 \u26c4\U0001f601 \U0001f31f\n'
           '\u2728 \U0001f601 \U0001f496 \u26c4 \u274c \u2728 \U0001f31f\n'
           '\U0001f496 \U0001f31f \u2728 \U0001f496 \U0001f601 \u26c4\n'
           '\U0001f496 \xc0 \u26c4 \u26c4 \u274c \U0001f31f \u2728\n'
           '\U0001f31f \U0001f31f \u2728 \U0001f601 \U0001f496 \U0001f31f\n'
           '\U0001f601 \U0001f601 \U0001f31f \u26c4 \U0001f31f \u26c4\n'
           '\U0001f496 \U0001f31f \U0001f31f \u274c \U0001f31f \U0001f31f\n'
           '\U0001f601\u274c\u26c4\u2728\U0001f601\u26c4\u274c\n') * 100
        file_lines = contents.splitlines()
        filename = 'lazy reading'
        with patch_open(contents, filename, max_read=DEFAULT_BUFFER_SIZE):
            lines = last_lines(filename)
            i = 0
            for actual, expected in zip(lines, reversed(file_lines)):
                i += 1
                self.assertEqual(actual.rstrip('\n'), expected)


@contextmanager
def patch_open(contents, filename=None, max_read=None):
    """Monkey-patch built-in open function to return a picky file."""
    def _fake_open(file, mode='r', buffering=-1, encoding=None, errors=None,
                   newline=None, closefd=True, opener=None):

        assert 'w' not in mode
        byte_text = contents.encode('utf-8')
        if 'b' in mode:
            f = PickyBytesIO(byte_text, max_read=max_read)
        else:
            f = PickyStringIO(BytesIO(byte_text), max_read=max_read)
        fake_open.file = f
        return f

    with patch('io.open', side_effect=_fake_open) as fake_open:
        with patch('builtins.open', new=fake_open):
            yield fake_open
    fake_open.assert_called_once()
    if filename:
        args, kwargs = fake_open.call_args
        if args:
            err_msg = "{!r} not {!r}".format(args[0], filename)
            assert str(args[0]) == filename, err_msg
        else:
            err_msg = "{!r} not {!r}".format(kwargs['file'], filename)
            assert str(kwargs['file']) == filename, err_msg


class PickyFile:

    """Mixin for making file objects which are picky about their read sizes."""

    def __init__(self, *args, max_read=None, **kwargs):
        self.max_read = max_read
        self.reads = []
        super().__init__(*args, **kwargs)

    def _log_read(self, size, data):
        self.reads.append((size, self.tell(), len(data)))
        if size == -1 and self.max_read:
            raise MemoryError("Can't read whole file at once")
        if self.max_read and size > self.max_read:
            raise OSError(
                "Can read at most {} characters at a time".format(self.max_read)
            )

    def read(self, size=-1):
        data = super().read(size)
        self._log_read(size, data)
        return data

    def readline(self, size=-1):
        data = super().readline(size)
        self._log_read(size, data)
        return data

    def writable(self):
        return False

    def write(self, *args, **kwargs):
        raise UnsupportedOperation("not writable")

    def writelines(self, *args, **kwargs):
        raise UnsupportedOperation("not writable")


class PickyBytesIO(PickyFile, BytesIO):
    """Fake bytes-based file."""


class PickyStringIO(PickyFile, TextIOWrapper):
    """Fake text-based file."""

    def tell(self, *args, **kwargs):
        try:
            return super().tell(*args, **kwargs)
        except OSError:
            return self.buffer.tell(*args, **kwargs)


if __name__ == "__main__":
    unittest.main(verbosity=2)
