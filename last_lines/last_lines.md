This week I'd like you to make a function, `last_lines`, which returns lines in a given ASCII text file in reverse 
order.

For example, given the following file, `my_file.txt`:

    This is a file
    This is line 2
    And this is line 3

The `last_lines` function should work like this:

    >>> for line in last_lines('my_file.txt'):
    ...     print(line, end='')
    ...
    And this is line3
    This is line 2
    This is a file

Note that `last_lines` should return the line ending (usually `\n`) for each line.

Initially, you don't need to worry about efficiency with large files and you can return whatever type of iterable 
you'd like (a list might be easiest).

There are 3 bonuses this week. The first one isn't too tricky, but the second and third bonuses may be quite 
challenging.

#### Bonus 1

For the first bonus, I'd like you to return an iterator from your `last_lines` function.

    >>> lines = last_lines('my_file.txt')
    >>> next(lines)
    'And this is line3\n'
    >>> next(lines)
    'This is line 2\n'
    >>> next(lines)
    'This is a file\n'

#### Bonus 2

For the second bonus, I'd like you to make sure your `last_lines` function reads the given file in chunks at most the 
size of `io.DEFAULT_BUFFER_SIZE` (which should be 8192).

Your function `last_lines` function shouldn't read more than 8192 bytes between each item given.

This means you'll need to skip ahead and read the file from the end.

#### Bonus 3

For the third bonus, I'd like you to assume the given file is a UTF-8 encoded file which might contain any valid 
unicode characters.

This means you'll need to be careful while reading and decoding text, ensuring you aren't decoding some text 
mid-character.
