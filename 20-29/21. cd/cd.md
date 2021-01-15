# cd

This week I'd like you to make a context manager called `cd` which changes directories temporarily.

Say we've made a file in a sub directory:

    >>> from pathlib import Path
    >>> subdir = Path('some_subdirectory')
    >>> subdir.mkdir()
    >>> (subdir / 'my_file.txt').write_text('hello world!')
    12

With the cd context manager we can temporarily change directories to read that file:

    >>> with cd(subdir):
    ...     print(Path('my_file.txt').read_text())
    ...
    hello world!
    >>> Path('my_file.txt').is_file()
    False

Your context manager should be re-entrant and you should ensure that the current directory is always changed 
back even if an exception was raised inside the with block.

The directory change shouldn't occur on creation of the `cd` object but on the use of the `with` block, so your 
context manager can be used like this:

    >>> change_to_subdirectory = cd(subdir)
    >>> Path('my_file.txt').is_file()
    False
    >>> with change_to_subdirectory:
    ...     Path('my_file.txt').is_file()
    ...
    True
    >>> Path('my_file.txt').is_file()
    False

#### Bonus 1

For the first bonus I'd like you to allow your context manager to accept no arguments. If no arguments are 
given, a temporary directory should be created and changed into.

    >>> print(Path.cwd())
    /home/trey
    >>> with cd():
    ...     print(Path.cwd())
    ...
    /tmp/tmp_16wleaw
    >>> print(Path.cwd())
    /home/trey

#### Bonus 2

For the second bonus, your context manager should work with the `with ... as` syntax, returning an object that has:

- a `current` attribute that contains a path-like object representing the directory we've temporarily moved into
- a `previous` attribute that contains a path-like object representing the directory we were in before we used `cd`

```
with cd() as dirs:
    print('previous:', dirs.previous)
    print('current:', dirs.current)
previous: /home/trey
current: /tmp/tmpkzia0cyj
```

#### Bonus 3

For the third bonus, your `cd` object should also have enter and exit methods so we can use it without the 
context manager syntax.

    >>> tempdir = cd()
    >>> tempdir.enter()
    >>> print(Path.cwd())
    /tmp/tmp9fc9qn86
    >>> tempdir.exit()
    >>> print(Path.cwd())
    /home/trey/repos/exercises/problems
