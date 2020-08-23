# make_file

This week I'd like you to write a `make_file` context manager that will create a temporary file that exists only 
within its `with` block.

For example:

    >>> with make_file() as filename:
    ...     open(filename, mode='wt').write('hello!')
    ...     print(open(filename).read())
    ...
    hello!
    >>> print(open(filename).read())
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpujib05m9'

The temporary file that is created should be somewhere that the user has write access to. Python has some helper 
utilities for making temporary files that you'll want to look up.

If you're not familiar with context managers, I definitely recommend looking them up and focusing on the base 
exercise before thinking about any bonuses.

I have written a similar context manager in some of the test files for past Python Morsels exercises, so don't 
look at your old test files while writing this one!

A hint: you may need to close the temporary file you create before you can write to it by name.

#### Bonus 1

For the first bonus, I'd like you to allow initial file contents to be specified with an optional `contents` argument.

    >>> with make_file("hello!") as filename:
    ...     print(open(filename).read())
    ...
    hello!
    >>> with make_file(contents="hi!") as filename:
    ...     print(open(filename).read())
    ...
    hi!

#### Bonus 2

For the second bonus, I'd like you to allow a directory to optionally be specified with a `directory` keyword argument.

The file will be created in the specified directory.

    >>> import os
    >>> with make_file(directory=os.getcwd()) as filename:
    ...     print(filename)
    ...
    /home/trey/tmpfbj5qsv4

#### Bonus 3

For the third bonus, I'd like you to allow options to be sent to the file that's being written.

The options `encoding`, `mode`, and `newline` should all be accepted and used the same way the built-in `open` 
function uses them.

    >>> with make_file(b"bytes!", mode='wb') as filename:
    ...     print(open(filename).read())
    ...
    bytes!
    >>> with make_file("hello!", encoding='utf-16-le') as filename:
    ...     print(open(filename, encoding='utf-16-be').read())
    ...
    栀攀氀氀漀℀
