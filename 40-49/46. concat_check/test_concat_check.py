import os
import sys
import unittest
import warnings
from contextlib import contextmanager, ExitStack, redirect_stdout, redirect_stderr
from importlib.machinery import SourceFileLoader
from io import StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile
from textwrap import dedent


class ConcatCheckTests(unittest.TestCase):

    """Tests for concat_check.py."""

    maxDiff = None

    def run_program(self, *file_contents, fix=False):
        with ExitStack() as stack:
            filenames = [
                stack.enter_context(make_file(contents))
                for contents in file_contents
            ]
            args = list(filenames)
            if fix:
                args.append('--fix')
            with warnings.catch_warnings() as w:
                warnings.simplefilter("ignore")
                output = run_program('concat_check.py', args=args)
            if not fix:
                for name, contents in zip(filenames, file_contents):
                    self.assertEqual(
                        Path(name).read_text(),
                        contents,
                        'file {} is unchanged'.format(name),
                    )
        return output, filenames

    def assertImplicitLines(self, output, *line_numbers):
        regex = "^"
        filename = ""
        for n in line_numbers:
            if isinstance(n, int):
                self.assertIn("{}, line {}".format(filename, n), output)
                # Non-colon & non-comma match is a hack for multi-line strings
                regex += r"{}, line {}\b.*[^:,]*\n".format(filename, n)
            else:
                filename = n
        regex += "$"
        self.assertRegex(output, regex)

    def test_one_space_between_double_quotes(self):
        contents = dedent("""
            w = "implicit" "on same line"
            x = "no implicit" + "concatenation"
            y = ["list", "of", "things" "missing comma"]
            z = "just one string"
        """).lstrip('\n')
        output, [filename] = self.run_program(contents)
        self.assertImplicitLines(output, filename, 1, 3)

    def test_multiple_files(self):
        contents1 = dedent("""
            w = "implicit" "on same line"
        """).lstrip('\n')
        contents2 = dedent("""
            x = "no implicit" + "concatenation"
        """).lstrip('\n')
        contents3 = dedent("""
            y = ["list", "of", "things" "missing comma"]
        """).lstrip('\n')
        contents4 = dedent("""
            z = "just one string"
        """).lstrip('\n')
        output, filenames = self.run_program(
            contents1, contents2, contents3, contents4
        )
        self.assertImplicitLines(output, filenames[0], 1, filenames[2], 1)

    def test_mixed_quotes(self):
        contents = dedent("""
            v = print('these' 'two strings')
            w = "implicit" 'on same line'
            x = "no implicit" + "concatenation"
            y = ["list", "of", 'things' "missing comma"]
            z = "just one string"
        """).lstrip('\n')
        output, [filename] = self.run_program(contents)
        self.assertImplicitLines(output, filename, 1, 2, 4)

    def test_no_implicit_concatenation(self):
        contents = dedent("""
            w = "implicit", "on same line"
            x = "no implicit" + "concatenation"
            y = ["list", "of", "things"+"missing comma"]
            z = "just one string"
        """).lstrip('\n')
        output, [filename] = self.run_program(contents)
        self.assertImplicitLines(output)

    def test_edge_cases_that_are_not_implicit(self):
        contents = dedent('''
            empty = ""
            just_a_space = " "
            another_space = ' '
            apostrophe = "'aint"
            quote_in_string = '"To be, or not to be" - Bob Dylan'
            a_multiline_string = """ hello """
        ''').lstrip('\n')
        output, [filename] = self.run_program(contents)
        self.assertImplicitLines(output)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_multiple_lines_and_other_string_types(self):
        multiline_contents = dedent("""
            v = [
                'one',
                'two'
                'three'
            ]
            w = [
                'four',
                'five',
                'six'
            ]
            x = print('hi'
                      'hello'
                      'how are you')
            y = {
                'unique',
                'words'
                'in',
                'set'
            }
            x = print('hi',
                      'hello',
                      'how are you')
        """).lstrip('\n')
        output, [filename] = self.run_program(multiline_contents)
        self.assertImplicitLines(output, filename, 3, 11, 12, 16)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_multiline_strings(self):
        other_string_contents = dedent("""
            print(r"raw string" u"unicode string")
            print(r"nothing implicit", u"here")
            print(rb"raw byte string" br"byte string")
            print(rb"nothing" + b"here either")
            print(U"Unicode string" "unicode string")
            print(U"nor".format("here"))
        """).lstrip('\n')
        output, [filename] = self.run_program(other_string_contents)
        self.assertImplicitLines(output, filename, 1, 3, 5)

        contents = dedent("""
            print("something implicit" u"here")
            print(rb"nothing" + b"here though")
            print(rb"raw byte string" b"byte string")
            print("nothing".format("here either"))
            print(\"""
                two
                multiline
            \""" '''
                strings
                with different quotes
            ''')
        """).lstrip('\n')
        output, [filename] = self.run_program(contents)
        self.assertImplicitLines(output, filename, 1, 3, 8)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_strings_printed_out(self):
        contents = dedent("""
            print("something implicit" u"here")
            print(rb"nothing" + b"here though")
            print(rb"raw byte string" b"byte string")
            print("nothing".format("here either"))
            print(\"""
                two
                multiline
            \""" '''
                strings
                with different quotes
            ''')
            x = [
                "1",
                "2"
                "3",
                "4"
            ]
        """).lstrip('\n')
        output, [filename] = self.run_program(contents)
        self.assertIn('"something implicit"', output)
        self.assertIn('u"here"', output)
        self.assertNotIn('rb"nothing"', output)
        self.assertNotIn('b"here though"', output)
        self.assertIn(dedent('''
            """
                two
                multiline
            """
        ''').strip('\n'), output)
        self.assertIn(dedent("""
            '''
                strings
                with different quotes
            '''
        """).strip('\n'), output)
        self.assertNotIn('"1"', output)
        self.assertIn('"2"', output)
        self.assertIn('"3"', output)
        self.assertNotIn('"4"', output)


class DummyException(Exception):
    """No code will ever raise this exception."""


def run_program(path, args=[], raises=DummyException):
    """
    Run program at given path with given arguments.

    If raises is specified, ensure the given exception is raised.
    """
    old_args = sys.argv
    assert all(isinstance(a, str) for a in args)
    try:
        sys.argv = [path] + args
        with redirect_stdout(StringIO()) as output:
            with redirect_stderr(output):
                try:
                    if '__main__' in sys.modules:
                        del sys.modules['__main__']
                    SourceFileLoader('__main__', path).load_module()
                except raises:
                    return output.getvalue()
                except SystemExit as e:
                    if e.args != (0,):
                        raise SystemExit(output.getvalue()) from e
                if raises is not DummyException:
                    raise AssertionError("{} not raised".format(raises))
                return output.getvalue()
    finally:
        sys.argv = old_args


@contextmanager
def make_file(contents=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode='wt', encoding='utf-8', delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
