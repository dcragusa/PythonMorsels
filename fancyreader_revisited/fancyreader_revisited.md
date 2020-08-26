# Fancyreader revisited

This week I'd like you to revisit the `FancyReader` class you've already made so that it solves a pretty big problem 
that Python's current `csv` module doesn't solve.

First a reminder that the `FancyReader` class accepts an iterable and creates an object which can be used for parsing 
CSV data from that object.

Now the problem:

- `csv.reader` gives lists to you as you loop over it and it doesn't handle headers at all
- `csv.DictReader` handles headers but it gives dictionaries, which aren't nearly as memory efficient as lists or tuples

And our solution: we want to modify the `FancyReader` class we've already made to make sure the objects we're yielding 
are more memory efficient than dictionaries.

    >>> lines = ['w1|w2|w3', 'my|fake|file', 'has|two|rows']
    >>> reader = FancyReader(lines, delimiter='|')
    >>> for row in reader:
    ...     print(row.w1, row.w2, row.w3)
    ...
    my fake file
    has two rows

Like `csv.DictReader` your `FancyReader` class should accept fieldnames, as well as other arguments that `csv.reader` 
accepts (like delimiter).

#### Bonus 1

For the first bonus, I'd like you to make your `Row` objects iterable, so they can be used in an unpacking, kind of 
like `csv.reader`'s lists:

    >>> lines = ['my|fake|file', 'has|two|rows']
    >>> reader = FancyReader(lines, delimiter='|')
    >>> print(*next(reader))
    my fake file
    >>> print(*next(reader))
    has two rows

#### Bonus 2

For the second bonus, I'd like you to create a `fieldnames` attribute on your `FancyReader` objects which should 
provide the headers of the CSV file:

    >>> lines = ['my,fake,file', 'has,two,rows']
    >>> reader = FancyReader(lines)
    >>> reader.fieldnames
    ['my', 'fake', 'file']
    >>> reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
    >>> reader.fieldnames
    >>> ['w1', 'w2', 'w3']

#### Bonus 3

For the third bonus, I'd like you to make your `Row` objects mutable:

    >>> lines = ['my,fake,file', 'has,two,rows']
    >>> rows = list(FancyReader(lines, fieldnames=['w1', 'w2', 'w3']))
    >>> rows[0].w1 = 'your'
    >>> print(*rows[0])
    your fake file

The third bonus may be very challenging.
