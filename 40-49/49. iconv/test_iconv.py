import os
import sys
import unittest
import warnings
from contextlib import contextmanager, redirect_stdout, redirect_stderr
from importlib.machinery import SourceFileLoader
from io import BytesIO, TextIOWrapper
from tempfile import NamedTemporaryFile


class IConvTests(unittest.TestCase):

    """Tests for iconv.py"""

    def iconv(
            self,
            arguments,
            contents,
            has_output=False,
            from_encoding=None,
            to_encoding=None,
    ):
        with make_file(contents, encoding=from_encoding) as in_filename:
            with make_file(encoding=to_encoding) as out_filename:
                argument_list = arguments.format(
                    IN=in_filename,
                    OUT=out_filename,
                ).split()

                stdout = run_program('iconv.py', argument_list)
                with open(out_filename, encoding=to_encoding) as out_file:
                    expected = contents if '{OUT}' in arguments else ""
                    self.assertEqual(out_file.read(), expected)
        if not has_output:
            self.assertEqual(stdout, b"")
        return stdout

    def test_neither_from_nor_to_encoding(self):
        self.iconv(
            arguments='{IN} -o {OUT}',
            contents="These are the file contents \u2728",
        )

    def test_from_encoding(self):
        self.iconv(
            arguments='{IN} -o {OUT} -f utf-16be',
            contents="These are the file contents \u2728",
            from_encoding="utf-16be",
        )

    def test_to_encoding(self):
        self.iconv(
            arguments='{IN} -o {OUT} -t utf-32be',
            contents="These are the file contents \u2728",
            to_encoding="utf-32be",
        )

    def test_both_from_and_to_encoding(self):
        self.iconv(
            arguments='{IN} -o {OUT} -f utf-16be -t utf-32le',
            contents="These are the file contents \u2728",
            from_encoding="utf-16be",
            to_encoding="utf-32le",
        )

    def test_long_argument_names(self):
        self.iconv(
            arguments='{IN} --output={OUT} --from-code=utf-16be -t utf-32le',
            contents="These are the file contents \u2728",
            from_encoding="utf-16be",
            to_encoding="utf-32le",
        )
        self.iconv(
            arguments='{IN} --output={OUT} -f utf-16be --to-code=utf-32le',
            contents="These are the file contents \u2728",
            from_encoding="utf-16be",
            to_encoding="utf-32le",
        )

    def test_different_argument_orders(self):
        self.iconv(
            arguments='-f utf-16be --to-code=utf-32le -o {OUT} {IN}',
            contents="These are the file contents \u2728",
            from_encoding="utf-16be",
            to_encoding="utf-32le",
        )
        self.iconv(
            arguments='--output={OUT} {IN} -t utf-32le --from-code=utf-16be',
            contents="These are the file contents \u2728",
            from_encoding="utf-16be",
            to_encoding="utf-32le",
        )

    def test_invalid_encodings(self):
        contents = "\U0001f496"
        with make_file(contents, encoding='utf-16le') as in_file:
            with make_file() as out_file:
                args = [in_file, '-o', out_file, '-f', 'utf-8', '-t', 'utf-8']
                with self.assertRaises(Exception):
                    run_program('iconv.py', args)
                with open(out_file) as out:
                    self.assertEqual(out.read(), "")

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_write_to_standard_output(self):
        contents = "These are the file contents \u2728"
        output = self.iconv(
            arguments='{IN} -f utf-16be',
            contents=contents,
            from_encoding="utf-16be",
            has_output=True,
        )
        self.assertEqual(output, contents.encode(sys.stdout.encoding))
        output = self.iconv(
            arguments='{IN} -f utf-16be -t utf-32le',
            contents=contents,
            from_encoding="utf-16be",
            has_output=True,
        )
        self.assertNotEqual(
            output,
            contents.encode(sys.stdout.encoding),
            "stdout encoding wasn't changed",
        )
        self.assertEqual(output, contents.encode('utf-32le'))

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_read_from_standard_input(self):
        contents = "These are the file contents \u2728"
        # No file specified means read stdin
        with patch_stdin(contents):
            self.iconv(
                arguments='-t utf-32be -o {OUT}',
                contents="These are the file contents \u2728",
                to_encoding="utf-32be",
            )

        # Dash means read stdin
        # -f with stdin requires changing stdin encoding
        with patch_stdin(contents.encode('utf-32be')):
            output = self.iconv(
                arguments='- -f utf-32be -t utf-32le -o {OUT}',
                contents=contents,
                from_encoding="utf-32be",
                to_encoding="utf-32le",
            )

        with patch_stdin(contents.encode('utf-32be')):
            output = self.iconv(
                arguments='{IN} -f utf-16be -t utf-32le',
                contents=contents,
                from_encoding="utf-16be",
                to_encoding="utf-32le",
                has_output=True,
            )
            self.assertEqual(output, contents.encode('utf-32le'))

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_ignore_decoding_errors(self):

        # Reading CP-1252 smart quotes in UTF-8 and ignoring decode errors
        contents = '“Hello!”'
        expected = 'Hello!'
        with make_file(contents, encoding='cp1252') as in_file:
            with make_file() as out_file:
                args = "{IN} -o {OUT} -f utf-8 -t cp1252 -c".format(
                    IN=in_file,
                    OUT=out_file,
                ).split()
                self.assertEqual(run_program('iconv.py', args), b'')
                with open(out_file, encoding='utf-8') as out:
                    self.assertEqual(out.read(), expected)

        # Reading UTF-8 smart quotes in CP-1252 from sys.stdin
        contents = '“Hello!”'
        expected = 'â€œHello!â€'
        with patch_stdin(contents.encode('utf-8')):
            with make_file() as out_file:
                args = "-f cp1252 -t utf-8 -c".split()
                output = run_program('iconv.py', args)
        self.assertEqual(output, expected.encode('utf-8'))


class DummyException(Exception):
    """No code will ever raise this exception."""


def run_program(path, args=[], raises=DummyException):
    """
    Run program at given path with given arguments.

    If raises is specified, ensure the given exception is raised.
    """
    old_args = sys.argv
    assert all(isinstance(a, str) for a in args)
    warnings.simplefilter("ignore", ResourceWarning)
    try:
        sys.argv = [path] + args
        output = TextIOWrapper(
            PermanentBytesIO(),
            encoding=sys.stdout.encoding,
            write_through=True,
        )
        if '__main__' in sys.modules:
            del sys.modules['__main__']
        try:
            with redirect_stdout(output):
                with redirect_stderr(output):
                    SourceFileLoader('__main__', path).load_module()
        except raises:
            return output.buffer.getvalue()
        except SystemExit as e:
            if e.args != (0,):
                raise SystemExit(output.buffer.getvalue()) from e
        finally:
            sys.modules.pop('__main__', None)
        if raises is not DummyException:
            raise AssertionError("{} not raised".format(raises))
        try:
            return output.buffer.getvalue()
        except ValueError as e:
            raise ValueError("Error: sys.stdout was closed") from e
    finally:
        sys.argv = old_args


@contextmanager
def make_file(contents=None, encoding=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode='wt', encoding=encoding, delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


@contextmanager
def patch_stdin(text):
    real_stdin = sys.stdin
    if isinstance(text, str):
        text = text.encode(sys.stdin.encoding)
    sys.stdin = TextIOWrapper(
        PermanentBytesIO(text),
        encoding=sys.stdin.encoding,
        write_through=True,
    )
    try:
        yield sys.stdin
    except EOFError as e:
        raise AssertionError("Read more input than was given") from e
    finally:
        sys.stdin = real_stdin


class PermanentBytesIO(BytesIO):

    _closed = False

    def close(self):
        self._closed = True

    @property
    def closed(self):
        return self._closed


if __name__ == "__main__":
    unittest.main(verbosity=2)
