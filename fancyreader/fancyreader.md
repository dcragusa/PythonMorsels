# FancyReader

This week I'd like you to make a custom CSV reader that acts slightly different from both `csv.reader` and `csv.DictReader`.

I'd like you to make a `FancyReader` callable that will accept an iterable of strings (which is what `csv.reader` accepts) and a `fieldnames` attribute representing the headers. This `FancyReader` callable will return an iterator that yields `Row` objects which represent each row.

    >>> lines = ['my,fake,file', 'has,two,rows']
    >>> reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
    >>> for row in reader:
    ...     print(row.w1, row.w2, row.w3)
    ...
    my fake file
    has two rows

Your `FancyReader` should accept all the same arguments as `csv.reader`.

You don't need to worry about headers that are invalid variable names in Python: just assume all headers are valid Python variable names.

#### Bonus 1

For the first bonus, I'd like you to make sure your `Row` objects are iterable and have a nice string representation.

    >>> lines = ['my,fake,file', 'has,two,rows']
    >>> reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
    >>> row = next(reader)
    >>> row
    Row(w1='my', w2='fake', w3='file')
    >>> w1, w2, w3 = row
    >>> w3
    'file'

#### Bonus 2

For the second bonus, I'd like you to make the `fieldnames` attribute optional. If no `fieldnames` attribute is specified, the first row should be automatically be read as a header row (and used in place of `fieldnames`).

    >>> lines = ['w1,w2,w3', 'my,fake,file', 'has,two,rows']
    >>> reader = FancyReader(lines)
    >>> for row in reader:
    ...     print(row.w1, row.w2, row.w3)
    ...
    my fake file
    has two rows

#### Bonus 3

For the third bonus, I'd like the return value of `FancyReader` to have a `line_num` attribute, the same way `csv.reader` does:

    >>> lines = 'red,1\nblue,2\ngreen,3'.splitlines()
    >>> reader = FancyReader(lines, fieldnames=['color', 'numbers'])
    >>> next(reader)
    Row(color='red', number=1)
    >>> reader.line_num
    2
    >>> next(reader)
    Row(color='red', number=1)
    >>> reader.line_num
    3

If you get stumped while working on the bonuses, you may want to take a look at the source code for `DictReader`. You could almost nearly copy what `DictReader` does if you wanted to. But if you want more of a challenge I recommend not looking at the `DictReader` source code (until you get stuck).
